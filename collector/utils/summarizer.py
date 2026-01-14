"""
LLM要約ユーティリティ
- OpenRouter APIを使用した記事要約
"""

import os
import re
import requests
from typing import Optional, List, Dict
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def clean_markdown_output(content: str) -> str:
    """
    LLM出力からmarkdownコードブロックを除去する
    ```markdown ... ``` で囲まれている場合、その囲みを削除する
    """
    if not content:
        return content
    
    # ```markdown で始まり ``` で終わる場合
    pattern = r'^```(?:markdown)?\s*\n(.*?)\n```\s*$'
    match = re.match(pattern, content.strip(), re.DOTALL)
    if match:
        return match.group(1).strip()
    
    return content.strip()

# OpenRouter API設定
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-3-flash-preview"  # フォールバック用デフォルトモデル


def get_model() -> str:
    """使用するモデルを環境変数から取得（未設定の場合はデフォルトを使用）"""
    return os.environ.get("OPENROUTER_MODEL", DEFAULT_MODEL)


def load_prompt_template(template_name: str = "summary") -> str:
    """プロンプトテンプレートを読み込む"""
    prompt_path = Path(__file__).parent.parent / "prompts" / f"{template_name}.md"
    if prompt_path.exists():
        return prompt_path.read_text(encoding="utf-8")
    else:
        # フォールバック用の簡易プロンプト
        return """
技術記事を以下のフォーマットで日本語で要約してください：

# {タイトル}

## 要点
- 何が起きたか
- なぜ重要か

## 技術的ポイント
- 主要な技術要素

## 影響・アクション
- 実務への影響

## 元記事
- URL: {URL}
"""


def summarize_article(
    title: str,
    url: str,
    content: str,
    date: str,
    api_key: Optional[str] = None,
    model: Optional[str] = None,
) -> Optional[str]:
    """
    記事をLLMで要約する

    Args:
        title: 記事タイトル
        url: 記事URL
        content: 記事本文
        date: 取得日
        api_key: OpenRouter APIキー
        model: 使用するモデル

    Returns:
        要約されたMarkdown、または失敗時はNone
    """
    api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        logger.error("OPENROUTER_API_KEY is not set")
        return None

    model = model or get_model()
    logger.info(f"Using model: {model}")

    prompt_template = load_prompt_template()

    user_message = f"""
以下の記事を要約してください。

## 記事情報
- タイトル: {title}
- URL: {url}
- 取得日: {date}

## 記事本文
{content}
"""

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/tech-radar",
            "X-Title": "Tech Radar",
        }

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": prompt_template},
                {"role": "user", "content": user_message},
            ],
            "max_tokens": 2000,
            "temperature": 0.3,
        }

        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            timeout=60,
        )
        response.raise_for_status()

        result = response.json()
        summary = result["choices"][0]["message"]["content"]
        summary = clean_markdown_output(summary)

        logger.info(f"Successfully summarized: {title}")
        return summary

    except requests.RequestException as e:
        logger.error(f"API request failed for {title}: {e}")
        return None
    except (KeyError, IndexError) as e:
        logger.error(f"Failed to parse API response for {title}: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error summarizing {title}: {e}")
        return None


def summarize_daily_digest(
    articles: List[Dict],
    date: str,
    api_key: Optional[str] = None,
    model: Optional[str] = None,
) -> Optional[str]:
    """
    複数の記事をまとめて日次ダイジェストとして要約する

    Args:
        articles: 記事情報のリスト（各記事は title, url, content, source, tags を含む）
        date: 日付（YYYY-MM-DD形式）
        api_key: OpenRouter APIキー
        model: 使用するモデル

    Returns:
        日次ダイジェストのMarkdown、または失敗時はNone
    """
    logger.info("=" * 50)
    logger.info("Starting daily digest summarization")
    logger.info(f"Date: {date}, Articles count: {len(articles)}")
    
    api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        logger.error("OPENROUTER_API_KEY is not set - check GitHub secrets")
        logger.error("=" * 50)
        return None
    
    # API keyの一部をログに出力（デバッグ用）
    logger.info(f"API key present: {api_key[:8]}...{api_key[-4:]}")

    model = model or get_model()
    logger.info(f"Using model: {model}")

    if not articles:
        logger.warning("No articles provided for daily digest")
        logger.warning("=" * 50)
        return None

    prompt_template = load_prompt_template("daily_digest")

    # 記事一覧を構築
    articles_text = ""
    for i, article in enumerate(articles, 1):
        articles_text += f"""
---
### 記事 {i}
- **タイトル**: {article.get('title', 'Untitled')}
- **URL**: {article.get('url', '')}
- **ソース**: {article.get('source', '')}
- **タグ**: {', '.join(article.get('tags', []))}

**本文**:
{article.get('content', '')[:3000]}  <!-- 長すぎる場合は切り詰め -->
"""

    user_message = f"""
以下の{len(articles)}件の技術記事を日次ダイジェストとしてまとめてください。

## 日付
{date}

## 記事一覧
{articles_text}
"""

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/tech-radar",
            "X-Title": "Tech Radar",
        }

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": prompt_template},
                {"role": "user", "content": user_message},
            ],
            "max_tokens": 4000,
            "temperature": 0.3,
        }

        logger.info(f"Sending request to OpenRouter API...")
        logger.info(f"Payload size: {len(user_message)} chars")
        
        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            timeout=120,  # 複数記事なのでタイムアウトを延長
        )
        
        logger.info(f"Response status code: {response.status_code}")
        
        if response.status_code != 200:
            logger.error(f"API returned non-200 status: {response.status_code}")
            logger.error(f"Response body: {response.text[:500]}")
        
        response.raise_for_status()

        result = response.json()
        summary = result["choices"][0]["message"]["content"]
        summary = clean_markdown_output(summary)

        logger.info(f"Successfully created daily digest for {date} with {len(articles)} articles")
        logger.info(f"Summary length: {len(summary)} chars")
        logger.info("=" * 50)
        return summary

    except requests.RequestException as e:
        logger.error(f"API request failed for daily digest: {e}")
        logger.error(f"Exception type: {type(e).__name__}")
        logger.error("=" * 50)
        return None
    except (KeyError, IndexError) as e:
        logger.error(f"Failed to parse API response for daily digest: {e}")
        logger.error(f"Response content: {response.text[:500] if 'response' in locals() else 'N/A'}")
        logger.error("=" * 50)
        return None
    except Exception as e:
        logger.error(f"Unexpected error creating daily digest: {e}")
        logger.error(f"Exception type: {type(e).__name__}")
        logger.error("=" * 50)
        return None

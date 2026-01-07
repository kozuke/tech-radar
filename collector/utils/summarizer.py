"""
LLM要約ユーティリティ
- OpenRouter APIを使用した記事要約
"""

import os
import requests
from typing import Optional
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# OpenRouter API設定
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-2.0-flash-001"  # 無料枠対応モデル


def load_prompt_template() -> str:
    """プロンプトテンプレートを読み込む"""
    prompt_path = Path(__file__).parent.parent / "prompts" / "summary.md"
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
    model: str = DEFAULT_MODEL,
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

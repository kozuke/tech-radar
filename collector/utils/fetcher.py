"""
記事取得ユーティリティ
- RSSフィードの解析
- Webページの本文抽出
"""

import feedparser
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


def fetch_rss_entries(url: str, limit: int = 10) -> List[Dict]:
    """
    RSSフィードからエントリを取得する

    Args:
        url: RSSフィードのURL
        limit: 取得する最大件数

    Returns:
        記事エントリのリスト
    """
    try:
        feed = feedparser.parse(url)

        if feed.bozo:
            logger.warning(f"RSS parse warning for {url}: {feed.bozo_exception}")

        entries = []
        for entry in feed.entries[:limit]:
            entries.append({
                "title": entry.get("title", ""),
                "url": entry.get("link", ""),
                "published": entry.get("published", entry.get("updated", "")),
                "summary": entry.get("summary", ""),
            })

        logger.info(f"Fetched {len(entries)} entries from {url}")
        return entries

    except Exception as e:
        logger.error(f"Failed to fetch RSS from {url}: {e}")
        return []


def extract_article_content(url: str, timeout: int = 30) -> Optional[str]:
    """
    WebページからメインコンテンツをHTML抽出する

    Args:
        url: 記事URL
        timeout: タイムアウト秒数

    Returns:
        抽出されたテキスト、または失敗時はNone
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; TechRadarBot/1.0; +https://github.com/tech-radar)"
        }
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # 不要な要素を削除
        for tag in soup(["script", "style", "nav", "header", "footer", "aside", "form"]):
            tag.decompose()

        # articleタグを優先的に探す
        article = soup.find("article")
        if article:
            text = article.get_text(separator="\n", strip=True)
        else:
            # mainタグを試す
            main = soup.find("main")
            if main:
                text = main.get_text(separator="\n", strip=True)
            else:
                # bodyから取得
                body = soup.find("body")
                text = body.get_text(separator="\n", strip=True) if body else ""

        # 空行を整理
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        text = "\n".join(lines)

        # 最大文字数制限（LLMへの入力用）
        max_chars = 15000
        if len(text) > max_chars:
            text = text[:max_chars] + "\n\n[...記事の続きは省略されました...]"

        logger.info(f"Extracted {len(text)} chars from {url}")
        return text

    except requests.RequestException as e:
        logger.error(f"Failed to fetch article from {url}: {e}")
        return None
    except Exception as e:
        logger.error(f"Failed to extract content from {url}: {e}")
        return None


def get_domain(url: str) -> str:
    """URLからドメインを取得"""
    try:
        parsed = urlparse(url)
        return parsed.netloc
    except Exception:
        return ""

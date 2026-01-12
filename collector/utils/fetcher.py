"""
記事取得ユーティリティ
- RSSフィードの解析
- Webページの本文抽出
- 日付フィルタリング
"""

import feedparser
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import logging
from urllib.parse import urlparse
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
import time

logger = logging.getLogger(__name__)


def parse_date(date_str: str) -> Optional[datetime]:
    """
    様々な形式の日付文字列をパースする

    Args:
        date_str: 日付文字列

    Returns:
        datetimeオブジェクト、またはパース失敗時はNone
    """
    if not date_str:
        return None

    # RFC 2822形式（RSSで一般的）
    try:
        return parsedate_to_datetime(date_str)
    except (ValueError, TypeError):
        pass

    # ISO 8601形式
    formats = [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            # タイムゾーンがない場合はUTCとして扱う
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue

    # feedparserの構造体形式
    try:
        if hasattr(date_str, 'tm_year'):
            return datetime(*date_str[:6], tzinfo=timezone.utc)
    except (TypeError, ValueError):
        pass

    logger.debug(f"Could not parse date: {date_str}")
    return None


def is_within_days(date_str: str, days: int = 7) -> bool:
    """
    日付が指定日数以内かどうかを判定する

    Args:
        date_str: 日付文字列
        days: 日数（デフォルト: 7日）

    Returns:
        指定日数以内の場合はTrue
    """
    parsed_date = parse_date(date_str)
    if not parsed_date:
        # パースできない場合は含める（安全側に倒す）
        logger.debug(f"Date parse failed, including article: {date_str}")
        return True

    # タイムゾーン対応
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)

    return parsed_date >= cutoff


def fetch_rss_entries(
    url: str,
    limit: int = 10,
    max_age_days: Optional[int] = 7,
) -> List[Dict]:
    """
    RSSフィードからエントリを取得する

    Args:
        url: RSSフィードのURL
        limit: 取得する最大件数
        max_age_days: 最大日数（この日数以内の記事のみ取得、Noneで無制限）

    Returns:
        記事エントリのリスト
    """
    try:
        feed = feedparser.parse(url)

        if feed.bozo:
            logger.warning(f"RSS parse warning for {url}: {feed.bozo_exception}")

        entries = []
        filtered_count = 0

        for entry in feed.entries:
            if len(entries) >= limit:
                break

            published = entry.get("published", entry.get("updated", ""))

            # 日付フィルタリング
            if max_age_days is not None:
                if not is_within_days(published, max_age_days):
                    filtered_count += 1
                    continue

            entries.append({
                "title": entry.get("title", ""),
                "url": entry.get("link", ""),
                "published": published,
                "summary": entry.get("summary", ""),
            })

        if filtered_count > 0:
            logger.info(f"Filtered out {filtered_count} old entries from {url}")

        logger.info(f"Fetched {len(entries)} entries from {url} (within {max_age_days} days)")
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

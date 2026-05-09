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
import re

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
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%B %d, %Y",
        "%b %d, %Y",
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


def _extract_page_text(url: str, timeout: int = 30) -> Optional[str]:
    """Webページから本文に近いテキストを抽出する。"""
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; TechRadarBot/1.0; +https://github.com/tech-radar)"
    }
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer", "aside", "form"]):
        tag.decompose()

    content = soup.find("article") or soup.find("main") or soup.find("body")
    text = content.get_text(separator="\n", strip=True) if content else ""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)


def _parse_section_date(line: str) -> Optional[datetime]:
    """changelogの見出し行から日付を取り出す。"""
    normalized = re.sub(r"\s+", " ", line).strip()

    # Cursor: "3.3 May 6, 2026" / "May 4, 2026"
    match = re.search(r"(?:\d+(?:\.\d+)*\s+)?([A-Z][a-z]+ \d{1,2}, \d{4})", normalized)
    if match:
        return parse_date(match.group(1))

    # Devin CLI: "2026.4.30-0" / "2026.4.13-0.next"
    match = re.search(r"\b(\d{4})\.(\d{1,2})\.(\d{1,2})(?:[-.\w]*)?\b", normalized)
    if match:
        year, month, day = (int(part) for part in match.groups())
        return datetime(year, month, day, tzinfo=timezone.utc)

    return None


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug[:80] or "update"


def _looks_like_title(line: str) -> bool:
    value = line.strip()
    if len(value) < 4:
        return False
    if value.lower() in {"changelog", "release notes"}:
        return False
    return bool(re.search(r"[A-Za-z0-9]", value))


def fetch_changelog_sections(
    url: str,
    limit: int = 10,
    max_age_days: Optional[int] = 7,
) -> List[Dict]:
    """
    RSSがないchangelog/release notesページから日付単位のセクションを取得する。

    Args:
        url: changelog/release notesページURL
        limit: 取得する最大件数
        max_age_days: 最大日数（この日数以内の記事のみ取得、Noneで無制限）

    Returns:
        記事エントリのリスト
    """
    try:
        text = _extract_page_text(url)
        if not text:
            logger.warning(f"No text extracted from changelog: {url}")
            return []

        lines = text.split("\n")
        sections = []
        current = None

        for line in lines:
            section_date = _parse_section_date(line)
            if section_date:
                if current:
                    sections.append(current)
                current = {
                    "date": section_date,
                    "heading": line,
                    "lines": [line],
                }
                continue

            if current:
                current["lines"].append(line)

        if current:
            sections.append(current)

        entries = []
        seen_urls = set()
        cutoff = None
        if max_age_days is not None:
            cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)

        for section in sections:
            if len(entries) >= limit:
                break
            section_date = section["date"]
            if cutoff is not None and section_date < cutoff:
                continue

            content_lines = section["lines"]
            content = "\n".join(content_lines).strip()
            if not content:
                continue

            title = section["heading"]
            for candidate in content_lines[1:8]:
                if _looks_like_title(candidate) and not _parse_section_date(candidate):
                    title = candidate
                    break

            date_id = section_date.strftime("%Y-%m-%d")
            entry_url = f"{url}#{date_id}-{_slugify(title)}"
            if entry_url in seen_urls:
                continue
            seen_urls.add(entry_url)

            entries.append({
                "title": title,
                "url": entry_url,
                "published": section_date.isoformat(),
                "summary": content,
                "content": content,
            })

        logger.info(f"Fetched {len(entries)} changelog sections from {url} (within {max_age_days} days)")
        return entries

    except requests.RequestException as e:
        logger.error(f"Failed to fetch changelog from {url}: {e}")
        return []
    except Exception as e:
        logger.error(f"Failed to parse changelog from {url}: {e}")
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
        text = _extract_page_text(url, timeout=timeout)

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

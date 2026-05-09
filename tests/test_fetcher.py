from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import pytest
import requests

from utils import fetcher


def test_parse_date_supports_common_formats():
    assert fetcher.parse_date("2026-05-09").date().isoformat() == "2026-05-09"
    assert fetcher.parse_date("May 9, 2026").date().isoformat() == "2026-05-09"
    assert fetcher.parse_date("Sat, 09 May 2026 00:00:00 GMT").tzinfo is not None
    assert fetcher.parse_date("") is None


def test_is_within_days_includes_unparseable_dates():
    assert fetcher.is_within_days("not a date", days=1) is True


def test_fetch_rss_entries_filters_old_entries(monkeypatch):
    now = datetime.now(timezone.utc)
    feed = SimpleNamespace(
        bozo=False,
        entries=[
            {
                "title": "New",
                "link": "https://example.com/new",
                "published": (now - timedelta(days=1)).isoformat(),
                "summary": "new summary",
            },
            {
                "title": "Old",
                "link": "https://example.com/old",
                "published": (now - timedelta(days=30)).isoformat(),
                "summary": "old summary",
            },
        ],
    )
    monkeypatch.setattr(fetcher.feedparser, "parse", lambda url: feed)

    entries = fetcher.fetch_rss_entries("https://example.com/feed", limit=10, max_age_days=7)

    assert entries == [
        {
            "title": "New",
            "url": "https://example.com/new",
            "published": feed.entries[0]["published"],
            "summary": "new summary",
        }
    ]


def test_extract_page_text_removes_non_content_tags(monkeypatch):
    class Response:
        content = b"""
        <html><body><header>Header</header><main><h1>Title</h1><script>x</script><p>Body</p></main></body></html>
        """

        def raise_for_status(self):
            return None

    monkeypatch.setattr(fetcher.requests, "get", lambda *args, **kwargs: Response())

    assert fetcher._extract_page_text("https://example.com") == "Title\nBody"


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("3.3 May 6, 2026", "2026-05-06"),
        ("2026.4.30-0.next", "2026-04-30"),
        ("No date here", None),
    ],
)
def test_parse_section_date(line, expected):
    parsed = fetcher._parse_section_date(line)
    assert (parsed.date().isoformat() if parsed else None) == expected


def test_slugify_and_title_detection():
    assert fetcher._slugify("New Feature: API!") == "new-feature-api"
    assert fetcher._slugify("!!!") == "update"
    assert fetcher._looks_like_title("Release notes") is False
    assert fetcher._looks_like_title("New Slack integration") is True


def test_fetch_changelog_sections_extracts_recent_sections(monkeypatch):
    text = "\n".join(
        [
            "May 9, 2026",
            "New Slack integration",
            "Details about Slack.",
            "May 1, 2026",
            "Older item",
            "Details about older item.",
        ]
    )
    monkeypatch.setattr(fetcher, "_extract_page_text", lambda url: text)

    entries = fetcher.fetch_changelog_sections("https://example.com/changelog", limit=5, max_age_days=None)

    assert len(entries) == 2
    assert entries[0]["title"] == "New Slack integration"
    assert entries[0]["url"] == "https://example.com/changelog#2026-05-09-new-slack-integration"


def test_fetch_changelog_sections_returns_empty_on_request_error(monkeypatch):
    monkeypatch.setattr(
        fetcher,
        "_extract_page_text",
        lambda url: (_ for _ in ()).throw(requests.RequestException("boom")),
    )

    assert fetcher.fetch_changelog_sections("https://example.com/changelog") == []


def test_extract_article_content_truncates_long_text(monkeypatch):
    monkeypatch.setattr(fetcher, "_extract_page_text", lambda url, timeout=30: "a" * 15001)

    text = fetcher.extract_article_content("https://example.com")

    assert len(text) > 15000
    assert text.endswith("[...記事の続きは省略されました...]")


def test_extract_article_content_returns_none_on_request_error(monkeypatch):
    monkeypatch.setattr(
        fetcher,
        "_extract_page_text",
        lambda url, timeout=30: (_ for _ in ()).throw(requests.RequestException("boom")),
    )

    assert fetcher.extract_article_content("https://example.com") is None


def test_get_domain_returns_netloc():
    assert fetcher.get_domain("https://example.com/path") == "example.com"

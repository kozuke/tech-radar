import main as collector_main


def test_load_sources_returns_empty_when_file_missing(monkeypatch, tmp_path):
    monkeypatch.setattr(collector_main, "SOURCES_PATH", tmp_path / "missing.yaml")

    assert collector_main.load_sources() == []


def test_load_sources_reads_yaml(monkeypatch, tmp_path):
    path = tmp_path / "sources.yaml"
    path.write_text("sources:\n  - name: test\n    type: rss\n", encoding="utf-8")
    monkeypatch.setattr(collector_main, "SOURCES_PATH", path)

    assert collector_main.load_sources() == [{"name": "test", "type": "rss"}]


def test_feed_scan_limit_scales_with_max_items():
    assert collector_main.feed_scan_limit(5) == 75
    assert collector_main.feed_scan_limit(1) == collector_main.FEED_SCAN_MIN
    assert collector_main.feed_scan_limit(20) == collector_main.FEED_SCAN_MAX


def test_collect_rss_articles_uses_deep_feed_scan_limit(monkeypatch):
    captured = {}

    def fake_fetch(url, limit, max_age_days):
        captured["limit"] = limit
        return []

    monkeypatch.setattr(collector_main, "fetch_rss_entries", fake_fetch)

    collector_main.collect_rss_articles(
        {"name": "source", "url": "https://example.com/feed", "tags": []},
        max_items=5,
    )

    assert captured["limit"] == collector_main.feed_scan_limit(5)


def test_collect_rss_articles_skips_duplicates_and_missing_content(monkeypatch):
    entries = [
        {"title": "Duplicate", "url": "https://example.com/duplicate"},
        {"title": "No content", "url": "https://example.com/no-content"},
        {"title": "Collected", "url": "https://example.com/collected"},
    ]
    monkeypatch.setattr(collector_main, "fetch_rss_entries", lambda *args, **kwargs: entries)
    monkeypatch.setattr(
        collector_main,
        "extract_article_content",
        lambda url: None if url.endswith("no-content") else "content",
    )
    existing_urls = {"https://example.com/duplicate"}

    articles = collector_main.collect_rss_articles(
        {"name": "source", "url": "https://example.com/feed", "tags": ["AI"]},
        max_items=2,
        existing_urls=existing_urls,
    )

    assert articles == [
        {
            "title": "Collected",
            "url": "https://example.com/collected",
            "content": "content",
            "source": "rss:source",
            "tags": ["AI"],
        }
    ]
    assert "https://example.com/collected" in existing_urls


def test_collect_rss_articles_collects_past_duplicate_block(monkeypatch):
    """先頭が既出でも、走査範囲内の未登録記事を max_items まで収集する。"""
    entries = [
        {"title": f"Dup {i}", "url": f"https://example.com/dup-{i}"}
        for i in range(6)
    ] + [
        {"title": "New 1", "url": "https://example.com/new-1"},
        {"title": "New 2", "url": "https://example.com/new-2"},
    ]
    monkeypatch.setattr(collector_main, "fetch_rss_entries", lambda *args, **kwargs: entries)
    monkeypatch.setattr(collector_main, "extract_article_content", lambda url: "body")

    existing_urls = {e["url"] for e in entries[:6]}

    articles = collector_main.collect_rss_articles(
        {"name": "source", "url": "https://example.com/feed", "tags": ["t"]},
        max_items=2,
        existing_urls=existing_urls,
    )

    assert len(articles) == 2
    assert articles[0]["url"] == "https://example.com/new-1"
    assert articles[1]["url"] == "https://example.com/new-2"


def test_collect_scrape_articles_skips_duplicates_and_limits(monkeypatch):
    entries = [
        {"title": "Duplicate", "url": "https://example.com/duplicate", "content": "duplicate"},
        {"title": "One", "url": "https://example.com/one", "summary": "summary"},
        {"title": "Two", "url": "https://example.com/two", "content": "content"},
    ]
    monkeypatch.setattr(collector_main, "fetch_changelog_sections", lambda *args, **kwargs: entries)
    existing_urls = {"https://example.com/duplicate"}

    articles = collector_main.collect_scrape_articles(
        {"name": "source", "url": "https://example.com/changelog", "tags": ["DevTools"]},
        max_items=1,
        existing_urls=existing_urls,
    )

    assert articles == [
        {
            "title": "One",
            "url": "https://example.com/one",
            "content": "summary",
            "source": "scrape:source",
            "tags": ["DevTools"],
        }
    ]


def test_collect_keyword_articles_is_not_implemented():
    assert collector_main.collect_keyword_articles({"name": "keyword", "query": "AI"}) == []


def test_run_collection_returns_empty_stats_when_no_sources(monkeypatch):
    monkeypatch.setattr(collector_main, "load_sources", lambda: [])

    assert collector_main.run_collection() == {"total": 0, "success": 0, "failed": 0}


def test_run_collection_dry_run_collects_without_summarizing(monkeypatch):
    monkeypatch.setattr(
        collector_main,
        "load_sources",
        lambda: [{"name": "rss-source", "type": "rss", "url": "url", "tags": []}],
    )
    monkeypatch.setattr(collector_main, "get_all_existing_urls", lambda data_dir: set())
    monkeypatch.setattr(collector_main, "get_existing_urls_for_date", lambda date, data_dir: set())
    monkeypatch.setattr(
        collector_main,
        "collect_rss_articles",
        lambda source, max_items, existing_urls, max_age_days: [
            {"title": "title", "url": "https://example.com", "content": "content", "source": "rss", "tags": []}
        ],
    )

    stats = collector_main.run_collection(dry_run=True)

    assert stats["total"] == 1
    assert stats["success"] == 1
    assert stats["failed"] == 0
    assert stats["sources"] == {"rss-source": 1}


def test_run_collection_saves_digest(monkeypatch, tmp_path):
    saved = {}
    monkeypatch.setattr(collector_main, "DATA_DIR", tmp_path)
    monkeypatch.setattr(
        collector_main,
        "load_sources",
        lambda: [{"name": "scrape-source", "type": "scrape", "url": "url", "tags": []}],
    )
    monkeypatch.setattr(collector_main, "get_all_existing_urls", lambda data_dir: set())
    monkeypatch.setattr(collector_main, "get_existing_urls_for_date", lambda date, data_dir: set())
    monkeypatch.setattr(
        collector_main,
        "collect_scrape_articles",
        lambda source, max_items, existing_urls, max_age_days: [
            {"title": "title", "url": "https://example.com", "content": "content", "source": "scrape", "tags": []}
        ],
    )
    monkeypatch.setattr(collector_main, "summarize_daily_digest", lambda articles, date: "# Digest")

    def fake_save_daily_digest(date, articles, summary_content, data_dir):
        saved.update({"date": date, "articles": articles, "summary_content": summary_content, "data_dir": data_dir})
        return {"id": f"{date}__daily-digest"}

    monkeypatch.setattr(collector_main, "save_daily_digest", fake_save_daily_digest)

    stats = collector_main.run_collection(dry_run=False)

    assert stats["success"] == 1
    assert saved["summary_content"] == "# Digest"
    assert saved["data_dir"] == tmp_path


def test_run_collection_records_failed_source_and_unknown_source(monkeypatch):
    monkeypatch.setattr(
        collector_main,
        "load_sources",
        lambda: [
            {"name": "unknown", "type": "unknown"},
            {"name": "broken", "type": "rss", "url": "url", "tags": []},
        ],
    )
    monkeypatch.setattr(collector_main, "get_all_existing_urls", lambda data_dir: set())
    monkeypatch.setattr(collector_main, "get_existing_urls_for_date", lambda date, data_dir: set())
    monkeypatch.setattr(
        collector_main,
        "collect_rss_articles",
        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("boom")),
    )

    stats = collector_main.run_collection()

    assert stats["failed"] == 1
    assert stats["total"] == 0

import json

from utils import storage


def test_generate_slug_normalizes_title():
    assert storage.generate_slug("Hello, Tech Radar! 2026") == "hello-tech-radar-2026"
    assert storage.generate_slug("!!!") == "untitled"
    assert len(storage.generate_slug("a" * 80)) == 50


def test_load_index_returns_empty_index_when_file_missing(tmp_path):
    assert storage.load_index(tmp_path) == {"generated_at": "", "items": []}


def test_load_index_returns_empty_index_when_json_is_invalid(tmp_path):
    (tmp_path / "index.json").write_text("{", encoding="utf-8")

    assert storage.load_index(tmp_path) == {"generated_at": "", "items": []}


def test_save_index_writes_generated_at_and_items(tmp_path):
    assert storage.save_index({"items": [{"id": "item-1"}]}, tmp_path) is True

    saved = json.loads((tmp_path / "index.json").read_text(encoding="utf-8"))
    assert saved["items"] == [{"id": "item-1"}]
    assert saved["generated_at"].endswith("Z")


def test_save_article_creates_markdown_meta_and_index(tmp_path):
    result = storage.save_article(
        date="2026-05-09",
        title="Example Article",
        url="https://example.com/article",
        tags=["AI", "Cloud"],
        source="rss:test",
        summary_content="# Summary",
        data_dir=tmp_path,
    )

    assert result["id"] == "2026-05-09__example-article"
    assert (tmp_path / "items" / "2026-05-09__example-article.md").read_text(encoding="utf-8") == "# Summary"
    meta = json.loads((tmp_path / "items" / "2026-05-09__example-article.meta.json").read_text(encoding="utf-8"))
    assert meta["url"] == "https://example.com/article"
    assert storage.is_url_exists("https://example.com/article", tmp_path) is True


def test_save_daily_digest_creates_and_updates_existing_entry(tmp_path):
    articles = [
        {"url": "https://example.com/a", "tags": ["AI"], "source": "rss:a"},
        {"url": "https://example.com/b", "tags": ["Cloud", "AI"], "source": "rss:b"},
    ]

    first = storage.save_daily_digest("2026-05-09", articles, "# Digest", tmp_path)
    second = storage.save_daily_digest("2026-05-09", articles[:1], "# Updated", tmp_path)

    index = storage.load_index(tmp_path)
    assert first["id"] == second["id"] == "2026-05-09__daily-digest"
    assert len(index["items"]) == 1
    assert index["items"][0]["article_count"] == 1
    assert (tmp_path / "items" / "2026-05-09__daily-digest.md").read_text(encoding="utf-8") == "# Updated"
    assert storage.get_existing_urls_for_date("2026-05-09", tmp_path) == {"https://example.com/a"}
    assert storage.get_all_existing_urls(tmp_path) == {"https://example.com/a"}


def test_existing_url_helpers_return_empty_sets_for_missing_digest(tmp_path):
    storage.save_index({"items": []}, tmp_path)

    assert storage.get_existing_urls_for_date("2026-05-09", tmp_path) == set()
    assert storage.get_all_existing_urls(tmp_path) == set()

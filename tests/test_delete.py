from datetime import datetime, timedelta

import delete
from utils import storage


def _write_index(data_dir, items):
    storage.save_index({"items": items}, data_dir)


def test_delete_article_files_deletes_existing_files(monkeypatch, tmp_path):
    items_dir = tmp_path / "items"
    items_dir.mkdir()
    (items_dir / "article.md").write_text("md", encoding="utf-8")
    (items_dir / "article.meta.json").write_text("{}", encoding="utf-8")
    monkeypatch.setattr(delete, "ITEMS_DIR", items_dir)

    assert delete.delete_article_files("article") is True
    assert not (items_dir / "article.md").exists()
    assert not (items_dir / "article.meta.json").exists()


def test_find_articles_by_age(monkeypatch, tmp_path):
    old_date = (datetime.now() - timedelta(days=20)).strftime("%Y-%m-%d")
    new_date = datetime.now().strftime("%Y-%m-%d")
    _write_index(
        tmp_path,
        [
            {"id": "old", "date": old_date},
            {"id": "new", "date": new_date},
        ],
    )
    monkeypatch.setattr(delete, "DATA_DIR", tmp_path)

    assert delete.find_articles_by_age(10) == [{"id": "old", "date": old_date}]


def test_find_articles_by_pattern_matches_strings_and_lists(monkeypatch, tmp_path):
    _write_index(
        tmp_path,
        [
            {"id": "one", "title": "Cloud Update", "tags": ["AWS"], "source": "rss:a"},
            {"id": "two", "title": "Other", "tags": ["AI"], "source": "rss:b"},
        ],
    )
    monkeypatch.setattr(delete, "DATA_DIR", tmp_path)

    assert [item["id"] for item in delete.find_articles_by_pattern("aws")] == ["one"]
    assert [item["id"] for item in delete.find_articles_by_pattern("rss:b")] == ["two"]


def test_find_articles_by_id_uses_partial_match(monkeypatch, tmp_path):
    _write_index(tmp_path, [{"id": "2026-05-09__daily-digest"}, {"id": "other"}])
    monkeypatch.setattr(delete, "DATA_DIR", tmp_path)

    assert delete.find_articles_by_id("daily") == [{"id": "2026-05-09__daily-digest"}]


def test_delete_articles_dry_run_does_not_update_index(monkeypatch, tmp_path):
    articles = [{"id": "one", "title": "One", "date": "2026-05-09"}]
    _write_index(tmp_path, articles)
    monkeypatch.setattr(delete, "DATA_DIR", tmp_path)

    stats = delete.delete_articles(articles, dry_run=True)

    assert stats == {"total": 1, "deleted": 1, "failed": 0}
    assert storage.load_index(tmp_path)["items"] == articles


def test_delete_articles_deletes_files_and_updates_index(monkeypatch, tmp_path):
    items_dir = tmp_path / "items"
    items_dir.mkdir()
    (items_dir / "one.md").write_text("md", encoding="utf-8")
    (items_dir / "one.meta.json").write_text("{}", encoding="utf-8")
    articles = [
        {"id": "one", "title": "One", "date": "2026-05-09"},
        {"id": "two", "title": "Two", "date": "2026-05-10"},
    ]
    _write_index(tmp_path, articles)
    monkeypatch.setattr(delete, "DATA_DIR", tmp_path)
    monkeypatch.setattr(delete, "ITEMS_DIR", items_dir)

    stats = delete.delete_articles([articles[0]], dry_run=False)

    assert stats == {"total": 1, "deleted": 1, "failed": 0}
    assert storage.load_index(tmp_path)["items"] == [articles[1]]

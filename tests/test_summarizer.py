import requests

from utils import summarizer


def test_clean_markdown_output_removes_fenced_markdown():
    assert summarizer.clean_markdown_output("```markdown\n# Title\n```") == "# Title"
    assert summarizer.clean_markdown_output("  # Title  ") == "# Title"
    assert summarizer.clean_markdown_output("") == ""


def test_get_model_uses_env_or_default(monkeypatch):
    monkeypatch.delenv("OPENROUTER_MODEL", raising=False)
    assert summarizer.get_model() == summarizer.DEFAULT_MODEL

    monkeypatch.setenv("OPENROUTER_MODEL", "custom/model")
    assert summarizer.get_model() == "custom/model"


def test_load_prompt_template_returns_fallback_for_missing_template():
    template = summarizer.load_prompt_template("missing-template")

    assert "技術記事" in template


def test_summarize_article_returns_none_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)

    assert summarizer.summarize_article("title", "https://example.com", "content", "2026-05-09") is None


def test_summarize_article_returns_cleaned_response(monkeypatch):
    class Response:
        def raise_for_status(self):
            return None

        def json(self):
            return {"choices": [{"message": {"content": "```markdown\n# Summary\n```"}}]}

    captured = {}

    def fake_post(url, headers, json, timeout):
        captured["payload"] = json
        captured["headers"] = headers
        captured["timeout"] = timeout
        return Response()

    monkeypatch.setattr(summarizer.requests, "post", fake_post)

    result = summarizer.summarize_article(
        "title",
        "https://example.com",
        "content",
        "2026-05-09",
        api_key="key",
        model="model",
    )

    assert result == "# Summary"
    assert captured["payload"]["model"] == "model"
    assert captured["headers"]["Authorization"] == "Bearer key"
    assert captured["timeout"] == 60


def test_summarize_article_returns_none_on_request_error(monkeypatch):
    monkeypatch.setattr(
        summarizer.requests,
        "post",
        lambda *args, **kwargs: (_ for _ in ()).throw(requests.RequestException("boom")),
    )

    assert summarizer.summarize_article("title", "url", "content", "2026-05-09", api_key="key") is None


def test_summarize_daily_digest_returns_none_without_articles():
    assert summarizer.summarize_daily_digest([], "2026-05-09", api_key="key") is None


def test_summarize_daily_digest_returns_cleaned_response_and_truncates_article(monkeypatch):
    class Response:
        status_code = 200
        text = "ok"

        def raise_for_status(self):
            return None

        def json(self):
            return {"choices": [{"message": {"content": "```markdown\n# Digest\n```"}}]}

    captured = {}

    def fake_post(url, headers, json, timeout):
        captured["payload"] = json
        captured["timeout"] = timeout
        return Response()

    monkeypatch.setattr(summarizer.requests, "post", fake_post)

    result = summarizer.summarize_daily_digest(
        [
            {
                "title": "title",
                "url": "https://example.com",
                "source": "rss:test",
                "tags": ["AI"],
                "content": "a" * 4000,
            }
        ],
        "2026-05-09",
        api_key="key",
        model="model",
    )

    assert result == "# Digest"
    assert captured["payload"]["model"] == "model"
    assert "a" * 3000 in captured["payload"]["messages"][1]["content"]
    assert "a" * 3001 not in captured["payload"]["messages"][1]["content"]
    assert captured["timeout"] == 120


def test_summarize_daily_digest_returns_none_on_malformed_response(monkeypatch):
    class Response:
        status_code = 200
        text = "{}"

        def raise_for_status(self):
            return None

        def json(self):
            return {}

    monkeypatch.setattr(summarizer.requests, "post", lambda *args, **kwargs: Response())

    assert summarizer.summarize_daily_digest(
        [{"title": "title", "url": "url", "content": "content", "source": "source", "tags": []}],
        "2026-05-09",
        api_key="key",
    ) is None

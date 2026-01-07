# 詳細設計

## 1. ディレクトリ構成

```
repo/
├── collector/
│   ├── main.py
│   ├── sources.yaml
│   ├── prompts/
│   │   └── summary.md
│   └── utils/
│
├── data/
│   ├── index.json
│   └── items/
│       ├── {date}__{slug}.md
│       └── {date}__{slug}.meta.json
│
├── site/
│   └── (Astro or VitePress)
│
└── .github/workflows/
    ├── collect.yml
    └── pages.yml
```

## 2. sources.yaml

```yaml
sources:
  - type: rss
    name: postgres_blog
    url: https://example.com/rss
    tags: [postgres]

  - type: keyword
    name: ai_news
    query: "LLM OR OpenAI"
    tags: [ai]
```
## 3. index.json

```json
{
  "generated_at": "2026-01-06T03:00:00Z",
  "items": [
    {
      "id": "2026-01-06__example",
      "date": "2026-01-06",
      "title": "記事タイトル",
      "url": "https://example.com",
      "tags": ["ai"],
      "source": "rss:postgres_blog",
      "summary_path": "data/items/2026-01-06__example.md"
    }
  ]
}
```

## 4. 記事Markdown構造

```md
# 記事タイトル

## 要点
- 何が起きたか
- なぜ重要か

## 技術的ポイント
- 技術要素
- 設計観点

## 影響・アクション
- 実務影響
- 次に調べること

## 元記事
- URL
```

## 5. GitHub Actions

### collect.yml
- cron + workflow_dispatch
- Python実行
- data/更新
- 自動commit

### pages.yml
- pushトリガー
- site build
- Pages deploy

## 6. Secrets
- OPENROUTER_API_KEY

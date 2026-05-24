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

### 個別記事

```md
# 記事タイトル

## 要点

段落形式で何が起きたか、なぜ重要かを2-3文で記述。

## 機能別の概要

（複数の機能アップデート・追加が言及されている場合のみ）

| 機能 | 概要 |
|------|------|
| 機能名 | 1-2文の要約 |

## 技術的ポイント

| 項目 | 詳細 |
|------|------|
| 主要技術 | 使用技術名 |
| 特徴・性能 | 性能値等 |
| 対応環境 | OS、言語等 |

## 影響・アクション

| アクション | 詳細 |
|------------|------|
| 実務への影響 | 影響の説明 |
| 次のステップ | やるべきこと |

## 元記事

> 🔗 **参考リンク**
> - URL: https://...
> - 取得日: 2026-01-07
```

### 日次ダイジェスト

```md
# Tech Radar Daily Digest - 2026-01-07

## 🔥 注目トピック

最も重要なトピックの詳細解説（段落形式）

---

## 📰 今日のニュース

### 大カテゴリ（AI/LLM, クラウド等）

#### サブカテゴリ（Claude Code, AWS等）

##### 記事タイトル

段落形式の要約（2-3文）。

**機能別の概要**（複数の機能アップデート・追加が言及されている場合のみ）

| 機能 | 概要 |
|------|------|
| 機能名 | 1-2文の要約 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | ... |
| 特徴・性能 | ... |

> 🔗 **参考リンク**
> https://...

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| アクション1 | 対象 | 🔴 高 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| ... | サブカテゴリ | ... | ... |
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

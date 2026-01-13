# Tech Radar

技術トレンドを自動取得してGitHub Pagesで参照する仕組み

## 概要

エンジニア向けの技術情報（ブログ、公式リリース、ニュース等）を自動収集し、LLMで要約して蓄積するシステムです。

### 特徴

- **完全自動化**: GitHub Actionsで定期実行
- **無料枠中心**: OpenRouter API（無料モデル対応）を使用
- **データ資産化**: Markdownでローカルに残る
- **拡張性**: 情報源をYAMLで簡単に追加
- **美しいUI**: VitePressで構築された閲覧サイト

## ディレクトリ構成

```
tech-radar/
├── collector/              # 記事収集スクリプト
│   ├── main.py            # メインエントリポイント
│   ├── delete.py          # 記事削除スクリプト
│   ├── sources.yaml       # 情報源定義
│   ├── prompts/           # LLMプロンプト
│   │   ├── summary.md       # 個別記事要約用
│   │   └── daily_digest.md  # 日次ダイジェスト用
│   └── utils/             # ユーティリティモジュール
│       ├── fetcher.py     # RSS/Web取得
│       ├── summarizer.py  # LLM要約
│       └── storage.py     # データ保存
│
├── data/                   # 収集結果（自動更新）
│   ├── index.json         # 記事インデックス
│   └── items/             # 日次ダイジェストファイル
│       ├── {date}__daily-digest.md       # 日次ダイジェスト
│       └── {date}__daily-digest.meta.json
│
├── site/                   # VitePress表示サイト
│   ├── .vitepress/
│   │   ├── config.ts      # サイト設定
│   │   └── theme/         # カスタムテーマ
│   │       ├── components/  # Vueコンポーネント
│   │       └── custom.css   # カスタムスタイル
│   ├── index.md           # トップページ
│   ├── articles/          # 記事一覧ページ
│   ├── tags/              # タグ一覧ページ
│   └── public/            # 静的ファイル
│
├── specs/                  # 仕様書
│   ├── 00_overview.md
│   ├── 01_basic_design.md
│   └── 02_detail_design.md
│
├── .github/workflows/
│   ├── collect.yml        # 定期収集ワークフロー
│   ├── cleanup.yml        # 記事削除ワークフロー
│   └── pages.yml          # GitHub Pagesデプロイ
│
└── requirements.txt
```

## セットアップ

### 1. Collector（記事収集）

```bash
# Python依存関係インストール
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 環境変数設定
export OPENROUTER_API_KEY="your-api-key"
export OPENROUTER_MODEL="google/gemini-3-flash-preview"  # オプション

# 実行（日次ダイジェスト生成）
cd collector
python main.py --max-items 3 --max-age-days 7 --verbose  # 直近7日以内の記事を各ソース最大3件取得

# 記事削除（ドライラン）
python delete.py --older-than 30 --dry-run --verbose

# 記事削除（パターン指定）
python delete.py --pattern "example" --dry-run --verbose

# 記事削除（ID指定）
python delete.py --id "2026-01-01__article-id" --dry-run --verbose
```

OpenRouter APIキーは [openrouter.ai](https://openrouter.ai/) で取得できます。

### 2. Site（閲覧サイト）

```bash
cd site

# 依存関係インストール
npm install

# 開発サーバー起動
npm run dev

# ビルド
npm run build

# ビルド結果のプレビュー
npm run preview
```

開発サーバーは http://localhost:5173 で起動します。

## GitHub Actions設定

### Secrets設定

リポジトリの Settings > Secrets and variables > Actions で以下を設定：

- `OPENROUTER_API_KEY`: OpenRouter APIキー（必須）
- `OPENROUTER_MODEL`: 使用するAIモデル（オプション、未設定時は `google/gemini-3-flash-preview`）
- `SLACK_WEBHOOK_URL`: Slack Incoming Webhook URL（オプション、設定するとデプロイ完了時に通知）

### ワークフロー

| ワークフロー | トリガー | 説明 |
|-------------|---------|------|
| `collect.yml` | 毎日 JST 7:00 / 手動 | 複数ソースから記事を収集し、1日1つの日次ダイジェストを生成 |
| `cleanup.yml` | 手動のみ | 古い記事や条件に合致する記事を削除 |
| `pages.yml` | data/ or site/ 更新時 / collect.yml完了時 | VitePressをビルドしてデプロイ（Slack通知対応） |

### cleanup.yml のオプション

| オプション | 説明 | 例 |
|-----------|------|-----|
| `older_than` | 指定日数より古い記事を削除 | `30`（30日より古い記事） |
| `pattern` | 正規表現でマッチする記事を削除 | `h-1b\|visa` |
| `article_id` | IDに部分一致する記事を削除 | `2026-01-01` |
| `dry_run` | ドライラン（デフォルト: true） | 実際に削除する場合は false に |

**注意**: 少なくとも1つのフィルタ条件（`older_than`、`pattern`、`article_id`）を指定する必要があります。

### GitHub Pages有効化

1. Settings > Pages を開く
2. Source: **GitHub Actions** を選択
3. `pages.yml` が実行されると自動デプロイ

## 情報源の追加

`collector/sources.yaml` を編集：

```yaml
sources:
  # RSSフィード
  - type: rss
    name: example_blog
    url: https://example.com/rss
    tags: [example, tech]

  # キーワード検索（将来実装）
  # - type: keyword
  #   name: ai_news
  #   query: "LLM OR OpenAI"
  #   tags: [ai]
```

### 現在設定されている情報源

#### RSSフィード対応済み
| 名前 | ソース | タグ |
|------|--------|------|
| aws_whats_new | AWS What's New (公式新着情報) | aws, cloud |
| openai_api_changelog | OpenAI API Changelog (GitHub Releases) | ai, chatgpt, openai, api |
| google_developers | Google Developers Blog | ai, gemini, google |
| google_workspace_updates | Google Workspace Updates (NotebookLM含む) | google, notebooklm, workspace |
| anthropic_sdk_releases | Anthropic SDK Releases (GitHub) | ai, claude, anthropic, api |
| claude_code_releases | Claude Code Releases (GitHub) | ai, claude, claude_code, anthropic |

#### スクレイピング対応が必要（未実装）
| 名前 | ソース | タグ |
|------|--------|------|
| gcp_blog | Google Cloud Blog | gcp, cloud |
| gcp_press | Google Cloud Press Releases | gcp, cloud |
| openai_news | OpenAI公式ニュース | ai, chatgpt, openai |
| anthropic_news | Anthropic公式ニュース | ai, claude, anthropic |
| google_ai_blog | Google AI Blog | ai, gemini, google, notebooklm |
| deepmind_blog | DeepMind Blog (Gemini開発元) | ai, gemini, deepmind |
| cognition_devin | Cognition Labs公式 (Devin開発元) | ai, devin, cognition |
| claude_code_changelog | Claude Code CHANGELOG.md | ai, claude, claude_code, anthropic |

## 出力フォーマット

### index.json

```json
{
  "generated_at": "2026-01-07T03:00:00Z",
  "items": [
    {
      "id": "2026-01-07__daily-digest",
      "date": "2026-01-07",
      "title": "Tech Radar Daily Digest - 2026-01-07",
      "type": "daily_digest",
      "article_count": 5,
      "urls": ["https://example.com/article1", "https://example.com/article2"],
      "tags": ["aws", "cloud", "github"],
      "sources": ["rss:aws_blog", "rss:github_blog"],
      "summary_path": "data/items/2026-01-07__daily-digest.md"
    }
  ]
}
```

### 日次ダイジェストMarkdown

```markdown
# Tech Radar Daily Digest - 2026-01-07

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

最も重要なトピックの詳細解説を段落形式で記述...

---

## 📰 今日のニュース

### クラウド

#### AWS

##### Amazon S3が新機能をリリース

S3に新しいストレージクラスが追加されました。これにより、アクセス頻度の低いデータをより低コストで保存できるようになります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | S3 Glacier Instant Retrieval |
| 特徴・性能 | ミリ秒レベルのアクセス |
| 対応環境 | 全リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/...

---

### AI/LLM

#### Claude Code

##### Claude Code v2.x.x がリリース

（同様のフォーマット）

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| S3の新ストレージクラスを検討 | インフラエンジニア | 🟡 中 |
| Claude Codeを最新版に更新 | 開発者全般 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon S3新機能 | AWS | rss:aws_whats_new | https://... |
```

## 開発

### ロードマップ

- [x] 基本的な収集機能
- [x] RSS対応
- [x] LLM要約（OpenRouter）
- [x] GitHub Actions自動化
- [x] VitePress表示サイト
- [x] タグフィルタリング
- [x] 日次ダイジェスト機能（1日1ファイル）
- [x] 記事削除機能
- [ ] キーワード検索対応
- [ ] 記事詳細ページ（要約全文表示）

## ライセンス

MIT

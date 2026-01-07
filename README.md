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
│   ├── sources.yaml       # 情報源定義
│   ├── prompts/           # LLMプロンプト
│   │   └── summary.md
│   └── utils/             # ユーティリティモジュール
│       ├── fetcher.py     # RSS/Web取得
│       ├── summarizer.py  # LLM要約
│       └── storage.py     # データ保存
│
├── data/                   # 収集結果（自動更新）
│   ├── index.json         # 記事インデックス
│   └── items/             # 記事ファイル
│       ├── {date}__{slug}.md
│       └── {date}__{slug}.meta.json
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

# 実行
cd collector
python main.py --max-items 3 --verbose
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

- `OPENROUTER_API_KEY`: OpenRouter APIキー

### ワークフロー

| ワークフロー | トリガー | 説明 |
|-------------|---------|------|
| `collect.yml` | 毎日 JST 15:00 / 手動 | 記事を収集してdata/に保存 |
| `pages.yml` | data/ or site/ 更新時 | VitePressをビルドしてデプロイ |

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

## 出力フォーマット

### index.json

```json
{
  "generated_at": "2026-01-07T03:00:00Z",
  "items": [
    {
      "id": "2026-01-07__example-article",
      "date": "2026-01-07",
      "title": "記事タイトル",
      "url": "https://example.com/article",
      "tags": ["example"],
      "source": "rss:example_blog",
      "summary_path": "data/items/2026-01-07__example-article.md"
    }
  ]
}
```

### 記事Markdown

```markdown
# 記事タイトル

## 要点
- 何が起きたか
- なぜ重要か

## 技術的ポイント
- 技術要素

## 影響・アクション
- 実務影響

## 元記事
- URL: https://example.com/article
- 取得日: 2026-01-07
```

## 開発

### ロードマップ

- [x] 基本的な収集機能
- [x] RSS対応
- [x] LLM要約（OpenRouter）
- [x] GitHub Actions自動化
- [x] VitePress表示サイト
- [x] タグフィルタリング
- [ ] キーワード検索対応
- [ ] 記事詳細ページ（要約全文表示）

## ライセンス

MIT

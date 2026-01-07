# 基本設計

## 1. 採用構成
- 実行基盤：GitHub Actions（cron）
- データ保存：GitHub Repository（Markdown / JSON）
- 表示基盤：GitHub Pages（静的サイト）
- 要約生成：OpenRouter API

## 2. 処理フロー

```
1. Actions起動（定期 or 手動）
2. 情報源定義を読み込み
3. 記事URL収集
4. 既存記事と重複チェック
5. 本文抽出
6. 要約生成（LLM）
7. 成果物を data/ に保存
8. git commit & push
9. Pages 更新
```

## 3. コンポーネント責務

### collector
- 情報源定義の解釈
- URL収集
- 本文抽出
- 要約生成
- 成果物生成

### data
- collectorの成果物置き場
- UI・将来のDBの入力元

### site
- dataを読み込み表示するだけ
- ビジネスロジックを持たない

## 4. データ設計方針
- 再生成可能なものは保存しない（全文など）
- 人が読むものは Markdown
- 機械が読むものは JSON

## 5. 運用ポリシー
- 1記事失敗しても全体は継続
- 既存記事は原則再要約しない

---
title: About
---

# Tech Radar について

## 概要

Tech Radarは、技術情報の収集・要約・蓄積を自動化するシステムです。

エンジニアとして日々大量の技術情報に触れる必要がありますが、情報源が分散しており巡回コストが高く、全文を読む時間もありません。Tech Radarは、これらの課題を解決し、**技術情報の収集・要約・蓄積・閲覧を自動化し、意思決定と学習を高速化する**ことを目的としています。

## 特徴

### 🤖 AI自動要約

OpenRouter APIを使用し、無料のLLMモデルで記事を自動要約します。各記事は以下の構造で整理されます：

- **要点**: 何が起きたか、なぜ重要か
- **技術的ポイント**: 使用技術、設計観点
- **影響・アクション**: 実務への影響、次のステップ

### 📡 多様な情報源

現在、以下の情報源から記事を収集しています：

- PostgreSQL公式ブログ
- AWS公式ブログ
- GitHub公式ブログ
- Google Developers Blog
- Hacker News（100ポイント以上）

### ⚡ 完全自動化

- GitHub Actionsで毎日JST 15:00に自動実行
- 新しい記事のみを処理（重複チェック）
- 収集結果は自動でcommit & push
- GitHub Pagesで自動デプロイ

### 📦 データ資産化

- すべての要約はMarkdownで保存
- Git履歴で変更を追跡可能
- いつでもエクスポート可能

## 技術スタック

| レイヤー | 技術 |
|---------|------|
| 収集スクリプト | Python |
| 要約生成 | OpenRouter API |
| データ保存 | Markdown / JSON |
| 静的サイト | VitePress |
| ホスティング | GitHub Pages |
| 自動化 | GitHub Actions |

## ソースコード

[GitHub Repository](https://github.com/your-username/tech-radar)

## ライセンス

MIT License

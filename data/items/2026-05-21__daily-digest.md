# Tech Radar Daily Digest - 2026-05-21

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは「Google I/O 2026」にて、AI開発プラットフォームの次世代版「Antigravity 2.0」を発表し、AIエージェント開発のパラダイムシフトを加速させています。従来の「Gemini CLI」は「Antigravity CLI」へと統合・移行されることが決定しており、今後は単一のAIアシスタントではなく、複数のエージェントが協調して複雑なワークフローを自律的に解決する「マルチエージェント時代」への本格的な移行が示唆されました。

また、Cursorにおいても「Cursor Automations」が強化され、マルチリポジトリ対応やリポジトリに依存しないエージェント運用が可能になりました。Slackやデータ分析基盤と連携するエージェントテンプレートが公開されるなど、開発ツールが「コードを書く場所」から「業務プロセス全体を自動化するハブ」へと進化している点が、今日の技術トレンドの大きな潮流となっています。

---

## 📰 今日のニュース

### AI/LLM

#### Google

##### Google I/O 2026：Antigravity 2.0とGemini CLIの統合
GoogleはAIエージェント開発プラットフォーム「Antigravity 2.0」を発表しました。Gemini CLIは6月18日にサービス終了し、今後はGo言語で再構築された高速なAntigravity CLIへ完全移行します。これにより、単一のモデル利用から、複数のサブエージェントをオーケストレーションするマルチエージェント開発環境への移行が促進されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Antigravity 2.0, Gemini 3.5, Go言語 |
| 特徴・性能 | マルチエージェントのオーケストレーション、非同期実行 |
| 対応環境 | CLI, デスクトップアプリ |
| 関連サービス | Google AI Studio, Cloud Run, Firebase |

> 🔗 **参考リンク**
> https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/

---

##### Google AI Edge GalleryがMCPをサポート
モバイルデバイス上でGemma 4などのモデルを動かす「Google AI Edge Gallery」が、Model Context Protocol (MCP) に対応しました。これにより、スマホ上のAIエージェントがGoogle WorkspaceやMapsなどの外部ツールと連携し、ローカル環境で複雑なタスクを完結できるようになります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Model Context Protocol (MCP), Gemma 4 |
| 特徴・性能 | ローカルでのツール呼び出し、セッション継続性 |
| 対応環境 | Android (iOSは近日対応) |
| 関連サービス | Google Workspace, Google Maps |

> 🔗 **参考リンク**
> https://developers.googleblog.com/a-smarter-google-ai-edge-gallery-mcp-integration-notifications-and-session-continuity/

---

### 開発ツール

#### Cursor

##### Cursor Automationsの強化とマルチリポジトリ対応
Cursorはエージェントウィンドウ内で自動化設定を完結できる機能を実装しました。特筆すべきは、複数のリポジトリを横断したエージェント運用や、コードベースに依存しない「Slack要約」や「財務レポート作成」などの非コード系エージェントのサポートです。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Cursor Automations, エージェント連携 |
| 特徴・性能 | マルチリポジトリ対応、No-repoエージェント |
| 対応環境 | Cursor IDE |
| 関連サービス | Slack, Databricks, Stripe |

> 🔗 **参考リンク**
> https://cursor.com/changelog#2026-05-20-this-release-brings

---

### クラウド

#### AWS

##### AWS Security Hubが「未使用アクセス」の可視化に対応
Security HubがIAMの未使用権限や認証情報を検出し、組織全体のリスクを統合管理できるようになりました。90日間のアクセス履歴に基づき、最小権限ポリシーの推奨案も自動生成されるため、セキュリティ運用の効率化が期待できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | IAM Access Analyzer, Security Hub |
| 特徴・性能 | 未使用アクセスの自動検出、最小権限ポリシー推奨 |
| 対応環境 | AWS全リージョン |
| 関連サービス | AWS IAM |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/aws-security-hub-unused-access/

---

##### ExtendDB：DynamoDB互換のオープンソースアダプター
AWSはDynamoDB APIをローカルやオンプレミスで利用可能にする「ExtendDB」を発表しました。PostgreSQLをバックエンドとして利用し、アプリケーションコードを変更せずにDynamoDBのプログラミングモデルを開発環境やエッジ環境で再現できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | DynamoDB API, PostgreSQL |
| 特徴・性能 | 互換性のあるローカル開発・テスト環境の構築 |
| 対応環境 | OSS (Apache 2.0) |
| 関連サービス | Amazon DynamoDB |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/aws-extenddb-dynamodb/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Gemini CLIからAntigravity CLIへの移行準備 | 開発者 | 🔴 高 |
| AWS Security Hubでの未使用アクセス権限の確認 | クラウド管理者 | 🟡 中 |
| Cursorの新エージェントテンプレートの試用 | 開発者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Security Hub now uncovers identity risks | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-security-hub-unused-access/) |
| Security Hub Extended expands | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-security-hub-extended/) |
| AWS announces ExtendDB | データベース | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-extenddb-dynamodb/) |
| Google I/O 2026 Developer keynote | AI/LLM | Google | [link](https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/) |
| Google AI Edge Gallery MCP integration | AI/LLM | Google | [link](https://developers.googleblog.com/a-smarter-google-ai-edge-gallery-mcp-integration-notifications-and-session-continuity/) |
| Transitioning Gemini CLI to Antigravity CLI | AI/LLM | Google | [link](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) |
| Cursor Changelog (May 20) | 開発ツール | Cursor | [link](https://cursor.com/changelog#2026-05-20-this-release-brings) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Google I/O 2026にて「Antigravity 2.0」発表、マルチエージェント開発プラットフォームへ進化。

📌 **ピックアップ**
• Google: Gemini CLIがAntigravity CLIへ統合・移行決定
• AWS: Security HubがIAMの未使用アクセス権限を自動検出
• Cursor: マルチリポジトリ対応の自動化エージェントを強化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-21*
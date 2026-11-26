# Tech Radar Daily Digest - 2026-11-26

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは、AIエージェントがGoogle Workspace内のデータに安全かつ効率的にアクセスするための「Workspace MCPサーバー」および「Workspace CLI」を一般公開しました。これは、従来のREST APIとは異なり、エージェントの動的なワークフローに最適化された設計となっており、認証や監査ログ、管理制御が統合されています。これにより、開発者はカスタム統合コードを最小限に抑えつつ、GmailやDriveなどのツールをエージェントに安全に接続できるようになります。

また、Devin（Cognition）においても、MCP（Model Context Protocol）との統合強化やCLIの機能拡充が急速に進んでいます。特にセキュリティと開発者体験の両立が重視されており、AIエージェントが企業環境で実用的なタスクを遂行するための基盤整備が、クラウドプロバイダーとAIプラットフォームの両面で加速していることが伺えます。

---

## 📰 今日のニュース

### AI/LLM

#### Devin / Cognition

##### Devin CLIおよびプラットフォームのアップデート

DevinのCLIおよびプラットフォームにおいて、MCP統合の強化やワークスペース管理機能の改善が行われました。CLIでは並列実行のサポートやパッケージ配布の拡充が行われ、プラットフォーム側ではJira連携の強化やセキュリティスキャン機能の可視化が向上しています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| CLI並列実行 | `devin worker start --concurrency N`により、子セッションが親を待機せずに並列処理可能に。 |
| Jira連携 | @DevinによるJiraタスク割り当て時に、プレイブックの適用や添付ファイルの取り込みが可能に。 |
| セキュリティ | スキャン結果の「Fixes」タブ表示や、脅威モデルに基づくスキャン開始オプションを追加。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | MCP (Model Context Protocol), CLI, OAuth |
| 特徴・性能 | 並列処理の最適化、セキュリティスキャンの可視化 |
| 対応環境 | Linux (.deb/.rpm), macOS, Windows |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview
> https://cli.devin.ai/docs/changelog/stable

---

### クラウド

#### AWS

##### AWS LambdaがMicroVMのオーケストレーションをサポート

AWS Lambdaにおいて、Durable Functionsを用いたMicroVMのオーケストレーション機能が開発者プレビューとして公開されました。これにより、セキュリティスキャナーやCI/CDジョブなど、分離された環境で実行する必要があるタスクのライフサイクル管理が容易になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Lambda, MicroVM, Durable Execution SDK |
| 特徴・性能 | VMレベルの分離、ステート保存、自動リトライ機能 |
| 対応環境 | TypeScript, Python |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-microvm/

##### Amazon EC2 インスタンスの拡充

AWSはGravitonプロセッサを搭載した最新世代のEC2インスタンスを各リージョンで展開しました。特にM9gdおよびC9gdインスタンスでは、新たに「Nitro Isolation Engine」が導入され、数学的に証明可能なクラウドセキュリティの基準が確立されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| M9gd/C9gd | Graviton5搭載。前世代比で最大25%の性能向上とNitro Isolation Engineを初搭載。 |
| M8g | イスラエルリージョンで利用可能に。Graviton4搭載で汎用ワークロード向け。 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-m9gd-asiapacific-seoul/

---

### Workspace

#### Google Workspace

##### Gemini Notebookの学習機能強化

Gemini Notebookのフラッシュカード機能がアップデートされ、学習効率を高めるための新機能が追加されました。画像挿入やストップウォッチ機能、モバイルでの学習リマインダーにより、試験対策やスキル習得の支援が強化されています。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/11/new-study-enhancements-for-flashcards-in-Gemini-Notebook.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Devin CLIの最新版（.deb/.rpm）への更新 | 開発者 | 🟡 中 |
| Lambda MicroVMプレビューの検証（非本番環境） | クラウドエンジニア | 🟡 中 |
| Google MeetハードウェアのUI変更に関する周知 | 管理者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Lambda now supports orchestrating MicroVMs | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-microvm/) |
| Amazon CloudWatch Omni now integrates with PagerDuty | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-omni-pagerduty/) |
| Amazon EC2 M8g instances available in Israel | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-m8g-instances-telaviv-region/) |
| Amazon EC2 M9gd instances available in Seoul | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-m9gd-asiapacific-seoul/) |
| Amazon EC2 C9gd instances in additional regions | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-c9gd-instances-additional-regions/) |
| Simplifying agent access with Workspace MCP | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html) |
| New study enhancements for Flashcards in Gemini Notebook | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/11/new-study-enhancements-for-flashcards-in-Gemini-Notebook.html) |
| Devin Apps & Sessions updates | AI/LLM | Cognition | [link](https://docs.devin.ai/release-notes/overview) |
| Devin CLI Changelog | AI/LLM | Cognition | [link](https://cli.devin.ai/docs/changelog/stable) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

GoogleがWorkspace向けMCPサーバーとCLIを一般公開し、AIエージェントの安全なデータ連携を強化。

📌 **ピックアップ**
• AWS LambdaがMicroVMのオーケストレーションをサポート開始
• Devin CLIが並列実行やJira連携など大幅機能強化
• Gemini Notebookのフラッシュカード機能に画像挿入やリマインダー追加

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-26*
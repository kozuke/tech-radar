# Tech Radar Daily Digest - 2026-06-24

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Google Apps ScriptがWorkspaceの「コアサービス」へ昇格**
Google Apps Scriptが正式にGoogle Workspaceのコアサービスとして認定されました。これにより、他の主要なWorkspaceサービスと同等のエンタープライズレベルのデータ保護、管理コントロール、およびテクニカルサポートが適用されます。これまでセキュリティやコンプライアンス上の懸念から利用を制限していた組織でも、今後は安心して自動化やカスタムソリューションの開発に活用できるようになり、組織内のワークフロー効率化が大きく加速することが期待されます。

**Cursorがカスタマイズ機能を大幅強化**
AIエディタ「Cursor」が、プラグイン、スキル、MCP（Model Context Protocol）を一元管理できる新しい「Customize」ページを公開しました。チーム内での人気ランキング表示や、GitLab/BitBucket/Azure DevOpsからのプラグインリポジトリ取り込みに対応し、チーム開発におけるAIワークフローの共有と拡張性が飛躍的に向上しています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.187 リリース
Claude Codeの最新版では、サンドボックス環境での認証情報へのアクセス制限や、組織ごとのモデル利用制限機能が追加されました。また、リモートセッションの安定性向上や、VSCode拡張機能のレスポンス改善など、開発体験を向上させる多数のバグ修正と機能強化が行われています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code (CLIツール) |
| 特徴・性能 | 認証情報の保護強化、組織レベルのモデル制限、UI操作の改善 |
| 対応環境 | ターミナル環境、VSCode |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.187

#### OpenAI Codex CLI

##### v0.143.0-alpha.5〜9 リリース
OpenAI Codex CLIにおいて、複数のアルファ版リリースが連続して公開されました。主に内部的な改善や安定性の向上が図られており、開発サイクルの加速が伺えます。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.143.0-alpha.9

---

### クラウド

#### AWS

##### Amazon CloudWatch Logsがsyslogのマネージド取り込みに対応
ネットワーク機器やサーバーからのsyslogメッセージを、エージェント不要で直接CloudWatch Logsへ送信可能になりました。TCP/TLS/UDPをサポートし、自動パース機能によりログの分析やセキュリティ調査が容易になります。

##### SageMaker Notebook InstancesでG6eインスタンスが利用可能に
NVIDIA L40s GPUを搭載したG6eインスタンスがSageMakerノートブックで利用可能になりました。最大130億パラメータのLLMのデプロイや、生成AIのファインチューニングなど、高負荷なAI開発タスクを高速化します。

##### Amazon Bedrock AgentCore Memoryのクロスアカウントアクセス対応
複数のAWSアカウント間でメモリリソースを共有できるようになりました。リソースベースのポリシーを用いることで、アカウントを跨いだセマンティック検索やイベント配信が可能となり、マルチアカウント構成でのAIエージェント構築が容易になります。

##### AWS HealthOmicsでプライベートワークフロー向けエフェメラルストレージを提供
バイオインフォマティクスワークフローのタスクごとに、専用の高速な一時ストレージ（/tmp）が割り当てられるようになりました。これにより、ゲノム解析などのI/O負荷が高い処理のパフォーマンスが向上し、コスト効率も改善されます。

##### Amazon Cognitoが顧客管理鍵（CMK）による暗号化をサポート
ユーザープールデータの暗号化にAWS KMSの顧客管理鍵が使用可能になりました。組織のデータガバナンス要件に合わせて、鍵のライフサイクルやアクセス権限を完全に制御できるようになります。

---

### Workspace

#### Google Workspace

##### Google Meetハードウェアのルームコード接続
超音波による近接検知が利用できない環境でも、5桁のルームコードを入力することで会議室のハードウェアに接続可能になりました。

##### SafariからのGoogle Meet参加
iOSデバイスにおいて、アプリをインストールしていなくてもSafariブラウザから直接Google Meetの会議に参加できるようになりました。

##### 管理者パスワードリセットの監視強化
Alert Centerの監視対象が「スーパー管理者」から「すべての管理者ロール」に拡大されました。特権アカウントのセキュリティ監視が強化され、不正アクセスの検知能力が向上します。

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Apps Scriptの利用ポリシー再検討 | 管理者 | 🟡 中 |
| Cursorの「Customize」ページでチーム用MCPの共有 | 開発チーム | 🟡 中 |
| CloudWatch Logsでのsyslog取り込み設定 | インフラ担当 | 🟢 低 |
| 管理者パスワードリセット監視設定の確認 | セキュリティ担当 | 🔴 高 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon CloudWatch Logs supports managed syslog ingestion | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-syslog-ingestion/) |
| SageMaker Notebook Instances now support G6e instance types | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/03/g6e-new-launch-sagemaker-notebook-instances/) |
| Amazon Bedrock AgentCore Memory now supports cross-account access | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/agentcore-memory-cross-account-access) |
| AWS HealthOmics now supports ephemeral storage for private workflows | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/healthomics-scratch-storage/) |
| Amazon Cognito now supports customer managed key for encryption at rest | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cognito-customer-managed-key) |
| v2.1.187 (Claude Code) | AI/LLM | GitHub | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.187) |
| Google Apps Script is now a Google Workspace core service | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/06/google-apps-script-workspace-core-service.html) |
| Plugins, skills, and MCPs (Cursor) | AI/LLM | Cursor | [link](https://cursor.com/changelog#2026-06-22-plugins-skills-and-mcps-let-you-customize-cursor-for-your-workflows-the-new-cust) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
Google Apps ScriptがWorkspaceコアサービスに昇格し、エンタープライズ保護が強化されました。

📌 **ピックアップ**
• Cursorがプラグイン・MCP管理ページを刷新し、チーム開発を強化
• AWS CloudWatch Logsがsyslogのマネージド取り込みに対応
• AWS SageMakerでG6eインスタンスが利用可能に
• iOSのSafariからGoogle Meetへ直接参加可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-24*
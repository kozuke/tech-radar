# Tech Radar Daily Digest - 2026-11-14

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AWSが組織全体のセキュリティ管理を強化する「宣言的ポリシー」を導入**
AWS Security HubのCSPM（クラウドセキュリティ態勢管理）において、AWS Organizationsの宣言的ポリシーによる集中管理がサポートされました。これにより、組織内の全アカウントおよびリージョンに対してセキュリティ標準やコントロールを一括適用し、設定のドリフト（乖離）を自動的に防止することが可能になります。従来の中央設定機能からの移行も容易に設計されており、新規アカウント作成時のベースライン適用も自動化されるため、大規模環境におけるセキュリティガバナンスの効率と信頼性が大幅に向上します。

**Google WorkspaceがAI活用とワークフロー自動化を大幅拡充**
Google Workspace Studioおよび各アプリにおいて、Geminiを活用した「スキル」機能の展開が本格化しました。チーム独自のルールやテンプレートをAIに指示として組み込めるようになり、業務の標準化が加速します。また、ワークフロー自動化に「Wait until」ステップが追加され、特定の日時や期間まで処理を一時停止する柔軟な制御が可能になりました。これらは、組織内のAI活用を単なるチャットから実務プロセスへと昇華させる重要なアップデートです。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.325

Claude Codeの最新版では、zstd圧縮されたレスポンスのデコードにおけるセキュリティ修正が行われました。また、VS Code等の統合ターミナルでのUX改善として、Jupyterノートブックのセル再実行に関するヒント表示や、ポリシーブロック時のリカバリ手順（/rewind, /clear）の提示が追加されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | セキュリティ修正、ターミナルUXの改善、サブエージェントの動作安定化 |
| 対応環境 | CLI / VS Code等の統合ターミナル |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.325

---

#### OpenAI Codex

##### 0.169.0 および関連アルファ版リリース

Codex CLIの最新安定版0.169.0では、ターミナルワークスペースでのサイドチャットタブ対応や、カスタムモデルプロバイダーの追加機能が実装されました。また、複数のアルファ版（0.171.0-alpha.2〜5）が連続してリリースされており、開発が活発に進められています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| サイドチャットタブ | 複数のチャットをタブで切り替え可能になり、再起動後も状態を保持。 |
| カスタムプロバイダー | ターミナルから直接モデルプロバイダーの追加・編集が可能に。 |
| 検索・表示改善 | エージェントコマンドセンターでのタスク検索や、トランスクリプトの折りたたみ機能を追加。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Codex CLI |
| 特徴・性能 | SQLite 3.54への更新、サンドボックス処理の改善 |
| 対応環境 | macOS, Linux, Windows |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.169.0

---

### クラウド

#### AWS

##### Aurora PostgreSQL with express configuration now supported in CloudFormation

Aurora PostgreSQLの「express configuration」がCloudFormationに対応しました。これにより、サーバーレスデータベースの構築とクエリ開始までの時間を短縮しつつ、Infrastructure as Code（IaC）による自動化が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS CloudFormation, Aurora PostgreSQL |
| 特徴・性能 | `withExpressConfiguration` プロパティによる簡素化 |
| 対応環境 | 全AWSリージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-postgresql-cloudformation/

##### Amazon RDS for Oracle reduces downtime for automatic minor version upgrades and scheduled maintenance

RDS for Oracleのメンテナンスに伴うダウンタイムが削減されました。メンテナンス開始の最大30分前にリソースの準備を行うことで、切り替え時のオフライン時間を短縮し、可用性を向上させています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-reduces-maintenance-downtime-for-amvu-scheduled-upgrades/

---

### その他

#### Workspace

##### Google Workspace Weekly Recap - November 13, 2026

Google Workspaceの週次アップデートでは、AIによるラベル付けの承認フロー改善や、Google Chatでのリスト機能強化、Sheetsキャンバスの独立リンク公開機能などが発表されました。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/11/weekly-recap-11-13-2026.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Security Hub CSPMの宣言的ポリシーへの移行検討 | セキュリティ管理者 | 🔴 高 |
| Claude Codeのアップデート（v2.1.325）適用 | 開発者 | 🟡 中 |
| RDS for Oracleのメンテナンスウィンドウ確認 | DB管理者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Aurora PostgreSQL... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-postgresql-cloudformation/ |
| Grok 4.7 now available... | AI/LLM | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/kiro-grok-4-7-aws-govcloud-us/ |
| Amazon RDS for Oracle... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-reduces-maintenance-downtime-for-amvu-scheduled-upgrades/ |
| AWS Security Hub CSPM... | セキュリティ | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-cspm-org-policies/ |
| Amazon Bedrock AgentCore... | AI/LLM | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/bedrock-agentcore-oauth2-discovery/ |
| v2.1.325 | 開発ツール | Claude Code | https://github.com/anthropics/claude-code/releases/tag/v2.1.325 |
| 0.169.0 (他アルファ版) | 開発ツール | OpenAI Codex | https://github.com/openai/codex/releases/tag/rust-v0.169.0 |
| Google Workspace Weekly... | Workspace | Google | http://workspaceupdates.googleblog.com/2026/11/weekly-recap-11-13-2026.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AWS Security Hubの宣言的ポリシー対応と、Google WorkspaceのAI自動化機能が大幅拡充。

📌 **ピックアップ**
• AWS Security Hub: 組織全体でのセキュリティ設定を宣言的ポリシーで一括管理可能に。
• Google Workspace: AIスキル機能とワークフローの「Wait until」ステップが利用可能。
• Claude Code: セキュリティ修正を含むv2.1.325をリリース。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-14*
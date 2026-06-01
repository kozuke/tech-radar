# Tech Radar Daily Digest - 2026-06-02

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Codex CLI (v0.136.0) の大幅アップデートとGoogle Driveの整理機能の一般提供開始**

本日は、開発者向けツールと生産性向上ツールの両面で重要なアップデートがありました。特にOpenAIのCodex CLIは、TUI（ターミナルUI）の操作性向上、セッション管理の強化、そしてWindows環境でのサンドボックス対応など、開発者のワークフローを効率化する多数の改善が含まれています。一方、Google DriveではGeminiを活用したファイル整理機能「Organize My Files」が一般提供を開始し、AIがユーザーのファイル構造を分析して適切なフォルダ移動を提案することで、煩雑なファイル管理の自動化を実現しました。これらのアップデートは、AIを活用した開発・業務効率化がより実用的かつ高度なレベルに達していることを示しています。

---

## 📰 今日のニュース

### AI/LLM

#### OpenAI / Codex

##### Codex CLI v0.136.0 リリース

Codex CLIの最新版では、TUIの表示改善やセッションのアーカイブ機能、App-serverとの連携強化など、開発体験を向上させる多数の機能が追加されました。また、セキュリティ面でも認証フローの刷新やコマンド実行の安全性強化が行われており、より堅牢な開発環境を提供します。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| TUI改善 | OSC 8メタデータによるリンクのクリック対応や、テーブル表示の可読性向上。 |
| セッション管理 | `/archive` コマンドによるセッションのアーカイブと保護機能の追加。 |
| App-server連携 | `codex app-server --stdio` による標準入出力モードのサポート。 |
| セキュリティ | リモート制御のトークン管理刷新や、Gitフック実行の制限による安全性の向上。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Rust, TUI, MCP (Model Context Protocol) |
| 対応環境 | Windows (Alpha), Linux, macOS |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.136.0

---

### クラウド

#### AWS

##### Amazon Quick のセキュリティと接続性強化

Amazon Quickにおいて、顧客管理キー（CMK）によるデータ暗号化と、VPC経由でのMCPサーバー接続がサポートされました。これにより、厳格なセキュリティ要件を持つ企業でも、プライベートネットワーク内のデータソースを安全にAIワークフローへ統合可能になります。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| CMK暗号化 | AWS KMSを利用した顧客管理キーによるデータ暗号化と監査機能の提供。 |
| VPC接続 | インターネットを介さず、VPC内のプライベートなMCPサーバーとQuickを接続。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS KMS, Amazon VPC, MCP |
| 関連サービス | AWS CloudTrail, Amazon EC2, AWS Fargate |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-quick-research-cm-keys

##### Amazon SageMaker Unified Studio のガバナンス強化

SageMaker Unified Studioにおいて、IAM権限境界（Permissions Boundaries）の設定が可能になりました。これにより、組織のSCP（サービスコントロールポリシー）要件を満たしつつ、プロジェクト単位での権限管理を自動化・簡素化できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | IAM, SCP, SageMaker Unified Studio |
| 特徴・性能 | ブループリント設定によるIAMロール作成時の権限境界自動付与 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-sagemaker-scp/

##### Amazon Bedrock AgentCore Identity のシークレット管理改善

AgentCore Identityにおいて、AWS Secrets ManagerのシークレットARNを直接参照可能になりました。これにより、顧客側で管理するタグ付けや自動ローテーション、CMK暗号化などのガバナンスポリシーを適用したままシークレットを利用できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Secrets Manager, Bedrock AgentCore |
| 特徴・性能 | サービス管理型から顧客管理型へのシークレット管理移行 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/agentcore-identity-secrets-manager/

##### Amazon EC2 M8i / M8i-flex インスタンスの提供地域拡大

ニュージーランドリージョンにて、第8世代のM8iおよびM8i-flexインスタンスが利用可能になりました。Intel Xeon 6プロセッサを搭載し、前世代と比較して最大20%のパフォーマンス向上と、AI推論やデータベース処理における大幅な高速化を実現しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Intel Xeon 6, Amazon EC2 |
| 特徴・性能 | PostgreSQLで最大30%、AIモデルで最大40%の高速化 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-m8i-m8i-flex-new-zealand/

---

### Workspace

#### Google Workspace

##### Google Drive のファイル整理機能が一般提供開始

Geminiを活用した「Organize My Files」機能が一般提供されました。Drive内の散らかったファイルを分析し、適切なフォルダへの移動や新規フォルダ作成を提案することで、ユーザーの整理作業を大幅に削減します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Gemini, Google Drive |
| 対応環境 | Google Workspace (Business/Enterprise), Google AI Pro |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/organize-my-files-in-drive-now-generally-available.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Codex CLIのアップデートと新機能の確認 | 開発者 | 🟡 中 |
| AWS環境でのCMK暗号化設定の検討 | セキュリティ担当者 | 🔴 高 |
| Google Driveの整理機能の有効化とテスト | 一般ユーザー/管理者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Quick Research now supports customer managed keys | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-quick-research-cm-keys |
| Amazon Quick now supports VPC connectivity for MCP connections | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-quick-vpc-mcp/ |
| Amazon SageMaker adds permissions boundaries for SCP compliance | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-sagemaker-scp/ |
| Amazon Bedrock AgentCore Identity now allows you to bring your own secrets | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/agentcore-identity-secrets-manager/ |
| Amazon EC2 M8i and M8i-flex instances are now available | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-m8i-m8i-flex-new-zealand/ |
| 0.136.0 | AI/LLM | openai_codex_cli | https://github.com/openai/codex/releases/tag/rust-v0.136.0 |
| Organize My Files in Drive now generally available | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/06/organize-my-files-in-drive-now-generally-available.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Codex CLI v0.136.0のリリースと、Google DriveのAIファイル整理機能「Organize My Files」の一般提供開始。

📌 **ピックアップ**
• Codex CLI: TUI改善やセッション管理強化で開発効率が向上
• AWS: QuickのVPC接続やSageMakerの権限境界などセキュリティ機能が拡充
• Google Drive: Geminiがファイルを自動整理する機能が利用可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-02*
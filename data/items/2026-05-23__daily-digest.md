# Tech Radar Daily Digest - 2026-05-23

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Anthropicが提供するAIコーディングツール「Claude Code」が、バージョン2.1.149へと大幅なアップデートを行いました。今回のリリースでは、利用状況の可視化機能が強化され、スキルやサブエージェント、MCPサーバーごとのコスト内訳が確認可能になったほか、ターミナル上での操作性向上やMarkdownレンダリングの改善など、開発者の生産性に直結する機能が多数追加されています。

また、セキュリティ面でもPowerShellのパーミッションバイパス修正やサンドボックスの書き込み制限の厳格化など、重要な修正が含まれています。AIエージェントによる自動化が進む中で、こうした詳細なコスト管理とセキュリティの強化は、企業導入における信頼性を高める重要なステップであり、今後のAI開発ツールの標準的な機能セットとして定着していくことが予想されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### Claude Code v2.1.149 / v2.1.148

Claude Codeの最新版では、利用状況のカテゴリ別内訳表示やキーボード操作による差分表示のスクロール、Markdownでのチェックボックス表示対応など、UI/UXが大幅に改善されました。また、PowerShellの権限バイパス修正やGitワークツリーのサンドボックス制限強化など、セキュリティと安定性に関する多数のバグ修正が行われています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code (CLIツール) |
| 特徴・性能 | コスト可視化、セキュリティ修正、UI改善 |
| 対応環境 | ターミナル環境 (Bash/PowerShell) |
| 関連サービス | Anthropic Claude, MCP (Model Context Protocol) |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.149

---

#### OpenAI

##### Codex CLI v0.134.0-alpha.1 / alpha.2

OpenAIのCodex CLIにおいて、アルファ版のアップデートがリリースされました。詳細な変更内容は公開されていませんが、継続的な機能改善と安定性の向上が図られています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Codex CLI |
| 特徴・性能 | アルファ版リリース、安定性向上 |
| 対応環境 | CLI環境 |
| 関連サービス | OpenAI API |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.134.0-alpha.2

---

### クラウド

#### AWS

##### Amazon SageMaker Unified Studioの機能拡張

Amazon SageMaker Unified Studioにおいて、Identity CenterおよびIAMベースのドメイン管理機能が強化されました。管理者はコンソール外からプロジェクトの作成やユーザー権限、ネットワーキング設定を統合的に管理可能となり、さらにIAMベースのドメインではGlue Data Catalogに対するビジネスメタデータやガバナンス機能が利用可能になりました。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon SageMaker, AWS Glue |
| 特徴・性能 | ドメイン管理の統合、AI生成メタデータ |
| 対応環境 | AWS全リージョン |
| 関連サービス | AWS Lake Formation, IAM Identity Center |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/domain-management-iam-idc/

---

##### AWS Transformのマイグレーション評価機能強化

AWS Transformにエージェントを活用した高度なマイグレーション評価機能が追加されました。what-ifシナリオの作成やTCO（総所有コスト）の算出、Cloud Value Frameworkに基づいた分析が可能になり、マイグレーションの意思決定を迅速化します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Transform |
| 特徴・性能 | what-ifシナリオ分析、TCO算出 |
| 対応環境 | AWS全リージョン |
| 関連サービス | AWS Discovery Tool, EC2, S3, SQL Server |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/assessment-capabilities-transform

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude Codeをv2.1.149へアップデートし、コスト内訳を確認する | 開発者 | 🔴 高 |
| SageMaker Unified Studioの新しいガバナンス機能を検証する | データエンジニア | 🟡 中 |
| AWSマイグレーションのTCO分析に新機能を利用する | クラウドアーキテクト | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon SageMaker expands domain management | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/domain-management-iam-idc/ |
| New agentic migration assessment capabilities | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/assessment-capabilities-transform |
| Amazon SageMaker adds business metadata | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/sagemaker-catalog-iam-domains/ |
| v2.1.149 | AI/LLM | GitHub | https://github.com/anthropics/claude-code/releases/tag/v2.1.149 |
| v2.1.148 | AI/LLM | GitHub | https://github.com/anthropics/claude-code/releases/tag/v2.1.148 |
| 0.134.0-alpha.2 | AI/LLM | GitHub | https://github.com/openai/codex/releases/tag/rust-v0.134.0-alpha.2 |
| 0.134.0-alpha.1 | AI/LLM | GitHub | https://github.com/openai/codex/releases/tag/rust-v0.134.0-alpha.1 |
| v0.104.1 | AI/LLM | GitHub | https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.104.1 |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Claude Codeがv2.1.149へアップデート。コストの可視化やセキュリティ強化が図られました。

📌 **ピックアップ**
• Claude Code: スキル/サブエージェントごとのコスト内訳表示に対応
• AWS SageMaker: ドメイン管理機能の統合とガバナンス強化
• AWS Transform: エージェントによる高度なマイグレーション評価機能が登場

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-23*
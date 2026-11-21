# Tech Radar Daily Digest - 2026-11-21

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AIエージェントのガバナンスとセキュリティ機能が大幅強化**
GoogleとCognition（Devin）の両社から、AIエージェントの運用におけるガバナンスとセキュリティを強化する重要なアップデートが発表されました。Googleは「Semantic governance policies」をプレビュー公開し、エージェントが実行するツール呼び出しを、自然言語で記述されたポリシーに基づいて事前に検証・遮断する仕組みを提供します。一方、Devinは組織内でのアクセス制御、ユーザーグループ単位の共有設定、および「Devin Bots」による自律的なワークフロー管理機能を導入しました。これらの動きは、AIエージェントが単なる実験段階から、企業内の機密情報や業務プロセスを扱う実運用フェーズへ移行する中で、意図しない動作やデータ漏洩を防ぐための「ガードレール」が不可欠になっていることを示しています。

---

## 📰 今日のニュース

### AI/LLM

#### Google Gemini / Vertex AI

##### AIエージェントの異常検知とガバナンス強化
Googleは、エージェントの異常検知機能（Private Preview）を拡張し、Google Cloud外（AWSやオンプレミス等）で実行されるエージェントの監視にも対応しました。また、自然言語ポリシーでツール呼び出しを制限する「Semantic governance policies」のプレビューや、カスタムUI構築時の認証フローを簡素化するガイドを公開し、エンタープライズ環境での安全なAI活用を支援します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Agent Anomaly Detection, Semantic governance policies |
| 特徴・性能 | Google Cloud外のログ・トレースも分析対象に拡張 |
| 対応環境 | AWS Lambda, Microsoft Foundry, オンプレミス等 |
| 関連サービス | Vertex AI, Cloud Run, Agent Gateway |

> 🔗 **参考リンク**
> https://developers.googleblog.com/agent-anomaly-detection-safeguarding-agents-across-other-clouds/

---

#### Devin (Cognition)

##### Devinの大規模な機能アップデート（アクセス制御・共有・Bots）
Devinは11月17日から20日にかけて、組織内でのリソース共有、アクセス制御、および「Devin Bots」の導入を含む広範なアップデートを実施しました。特に、ユーザーグループ単位での権限管理や、セッションごとの詳細な共有設定が可能になり、企業利用におけるセキュリティとコラボレーション機能が大幅に向上しました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Devin Bots | 独自のメモリと権限を持ち、自律的にタスクを完了させる常駐型エージェント。 |
| アクセス制御 | ユーザーグループ単位でのセッション、シークレット、MCPサーバーの共有が可能に。 |
| セッション共有 | セッションごとに共有範囲（自分のみ、グループ、組織全体）を細かく設定可能。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Devin AI Agent, SCM連携, MCP (Model Context Protocol) |
| 対応環境 | Webアプリ, Slack, Microsoft Teams |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview

---

### クラウド

#### AWS

##### Amazon CloudWatch OmniがAzureに対応
Amazon CloudWatch OmniがMicrosoft Azureのログ、メトリクス、トレースの収集をサポートしました。これにより、マルチクラウド環境を利用するチームは、AWSとAzureのテレメトリを単一のコンソールで統合監視できるようになり、障害発生時のクロスプラットフォームな追跡が容易になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon CloudWatch Omni, Microsoft Entra ID連携 |
| 対応環境 | Azure Public Regions, AWS全リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-omni-microsoft-azure

---

### Workspace

#### Google Workspace

##### クライアントサイド暗号化（CSE）ドキュメントのリアルタイム共同編集
Google Workspaceは、クライアントサイド暗号化（CSE）が適用されたGoogleドキュメントにおいて、リアルタイムでの共同編集を可能にするベータプログラムを開始しました。これまでセキュリティと引き換えに制限されていた同時編集が可能になり、機密性の高い文書作成における生産性が向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Client-side encryption (CSE) |
| 対応環境 | Google Docs (Beta) |
| 関連サービス | Google Drive |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/11/now-available-in-beta-collaborate-in-real-time-on-client-side-encrypted-Google-Docs.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| AIエージェントのガバナンスポリシー策定と検証 | AI開発・運用担当者 | 🔴 高 |
| Devinのユーザーグループ設定とアクセス権限の再確認 | Devin管理者 | 🟡 中 |
| CloudWatch OmniでのAzure連携設定の検討 | クラウドインフラ担当者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon CloudWatch Omni now supports Microsoft Azure | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-omni-microsoft-azure) |
| Web Search on Amazon Bedrock expands language support | AI/LLM | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/11/web-search-amazon-bedrock/) |
| Agent Anomaly Detection: Safeguarding agents | AI/LLM | Google | [URL](https://developers.googleblog.com/agent-anomaly-detection-safeguarding-agents-across-other-clouds/) |
| Collaborate in real-time on CSE Google Docs | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/11/now-available-in-beta-collaborate-in-real-time-on-client-side-encrypted-Google-Docs.html) |
| Introducing Access and Sharing (Devin) | AI/LLM | Devin | [URL](https://docs.devin.ai/release-notes/overview#2026-11-20-introducing-access-and-sharing) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AIエージェントの安全な運用に向けたガバナンス機能が大幅強化されました。

📌 **ピックアップ**
• Google: エージェントの異常検知と自然言語ポリシーによるツール制御を強化
• Devin: 組織内での権限管理と「Devin Bots」による自律ワークフローを導入
• AWS: CloudWatch OmniがAzureの統合監視に対応
• Workspace: 暗号化ドキュメントのリアルタイム共同編集がベータ公開

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-21*
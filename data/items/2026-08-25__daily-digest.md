# Tech Radar Daily Digest - 2026-08-25

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Google Workspaceにおける「Ask Gemini in Chat」の導入とAI活用**
Googleは、Google Chat内に統合された新しいAIインターフェース「Ask Gemini in Chat」を8月26日より順次展開します。これは従来のサイドパネル機能を統合・発展させたもので、GmailやDrive、CalendarなどのWorkspaceデータ全体を横断的に検索し、コンテンツ生成やタスク管理、会議設定をチャット画面から離れることなく実行可能にします。この変更により、従来のサイドパネルは廃止されますが、ユーザーはよりシームレスなワークフローを実現できるようになります。

**Amazon SageMaker HyperPodのRayサポート強化**
Amazon SageMaker HyperPodが、分散AIワークロードのためのオープンソースフレームワーク「Ray」へのサポートを大幅に強化しました。今回のアップデートでは、SageMaker StudioからのRayクラスターの管理、Grafanaによる可視化、ノード自動復旧、ハングジョブ検知などが統合され、本番環境での運用負荷が大幅に軽減されます。これにより、データサイエンティストはインフラ管理に煩わされることなく、対話的な開発と大規模な分散トレーニングを効率的に実行可能となります。

---

## 📰 今日のニュース

### AI/LLM

#### AI Agent

##### How to Evaluate Live & Voice Agents in ADK
Googleは、AI開発キット（ADK）において、音声対話エージェントのライブ評価機能をネイティブサポートしました。シミュレートされたユーザー音声を用いてエージェントの応答を評価するループを構築可能になり、デモレベルから実運用レベルへの信頼性向上を支援します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Google ADK, Gemini Live 2.5 Flash |
| 特徴・性能 | 音声ベースの対話評価、グラフベースのワークフロー評価 |
| 対応環境 | Python環境 |

> 🔗 **参考リンク**
> https://developers.googleblog.com/how-to-evaluate-live-voice-agents-in-adk/

---

### クラウド

#### AWS

##### SageMaker MLflow now supports customer managed keys
SageMaker MLflowが、AWS KMSによる顧客管理キー（CMK）の暗号化をサポートしました。これにより、厳格なセキュリティ要件を持つ組織は、独自のキーでデータを保護し、CloudTrailを通じた詳細な監査が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS KMS, SageMaker MLflow |
| 特徴・性能 | 顧客管理キーによるデータ暗号化、監査機能の強化 |
| 対応環境 | MLflow Appが利用可能な全AWSリージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/sagemaker-mlflow-custom-keys

##### Amazon EKS now supports multiple external OIDC identity providers per cluster
Amazon EKSが、1つのクラスターに対して最大10個の外部OIDCプロバイダーを関連付けられるようになりました。従業員、契約社員、CI/CDシステムなど、異なるユーザー層ごとに独立した認証プロバイダーを直接設定可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon EKS, OIDC |
| 特徴・性能 | クラスターあたり最大10個のプロバイダー設定 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-multiple-oidc-providers

##### Amazon Aurora now supports PostgreSQL 18.4, 17.10, 16.14, 15.18, and 14.23
Amazon Aurora PostgreSQL互換エディションが、最新のPostgreSQLマイナーバージョンに対応しました。CVE対策やAurora固有の機能改善が含まれており、自動マイナーバージョンアップグレードによる計画的な適用が推奨されています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-aurora-postgresql-18-4-17-10-16-14-15-18-14-23/

##### Amazon Connect Customer now supports information extraction for agent voice and chat conversations
Amazon Connectが、音声およびチャット対話からの情報抽出機能を強化しました。通話内容からアカウント番号や理由などの重要情報を自動抽出し、後続のタスク作成やメール通知に活用することで、エージェントの作業負荷を軽減します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-connect-customer-information/

---

### Workspace

#### Google Workspace

##### Now available: A refreshed user interface for Google Meet hardware touch controllers
NeatおよびPolyデバイス向けのGoogle Meetハードウェア用タッチコントローラーのUIが刷新されます。主要な操作ボタンの配置が最適化され、デスクトップ版Google Meetと操作感が統一されることで、会議中の操作性が向上します。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/08/now-available-refreshed-user-interface-for-Google-Meet-hardware-touch-controllers-on-Neat-and-Poly-devices.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Aurora PostgreSQLのマイナーバージョンアップ計画 | DB管理者 | 🔴 高 |
| Ask Gemini in Chatの利用準備と社内周知 | Workspace管理者 | 🟡 中 |
| SageMaker HyperPodのRay新機能の検証 | AIエンジニア | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| SageMaker MLflow now supports customer managed keys | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/08/sagemaker-mlflow-custom-keys) |
| Amazon EKS now supports multiple external OIDC identity providers | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-multiple-oidc-providers) |
| Amazon Aurora now supports PostgreSQL 18.4... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-aurora-postgresql-18-4-17-10-16-14-15-18-14-23/) |
| Amazon SageMaker HyperPod enhances support for Ray | AI/LLM | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-sagemaker-hyperpod-ray) |
| Amazon Connect Customer information extraction | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-connect-customer-information/) |
| How to Evaluate Live & Voice Agents in ADK | AI/LLM | Google | [link](https://developers.googleblog.com/how-to-evaluate-live-voice-agents-in-adk/) |
| Refreshed UI for Google Meet hardware | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/08/now-available-refreshed-user-interface-for-Google-Meet-hardware-touch-controllers-on-Neat-and-Poly-devices.html) |
| Introducing Ask Gemini in Chat | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/08/ask-gemini-in-chat.html) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Google Workspaceで「Ask Gemini in Chat」が提供開始。チャット画面から直接AIを活用し、業務効率化が加速します。

📌 **ピックアップ**
• Google ChatにGeminiが統合され、Workspace横断検索やタスク管理が可能に
• SageMaker HyperPodがRayのサポートを強化し、分散AI開発を効率化
• Amazon AuroraがPostgreSQL最新マイナーバージョンに対応

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-08-25*
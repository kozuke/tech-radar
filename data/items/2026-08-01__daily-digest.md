# Tech Radar Daily Digest - 2026-08-01

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleの「Gemini Enterprise Agent Platform」におけるエージェントおよびモデル評価機能が一般提供（GA）を開始しました。本機能は、開発中のテストから本番環境での稼働まで、一貫した指標でエージェントの品質を測定・比較できる統合エンジンを提供します。20以上の事前構築済み指標に加え、独自の評価基準を定義できる「適応型ルーブリック」を備えており、本番環境でのドリフト検知やシミュレーターを用いたマルチターン対話の検証が可能です。これにより、AIエージェントの信頼性向上と開発サイクルの迅速化が期待されます。

また、AI開発ツール「Devin」の大規模アップデートも注目です。「Changes」タブのUI刷新や、MCP（Model Context Protocol）ツールの実行環境のサーバーサイド移行など、開発体験と運用効率を大幅に向上させる機能が多数追加されました。特にエンタープライズ向けの管理機能やSlack連携の強化は、組織でのAI活用を加速させる重要なアップデートと言えます。

---

## 📰 今日のニュース

### AI/LLM

#### Google Gemini / Genkit

##### Agent and Model Evaluations in Gemini Enterprise Agent Platform are now GA

Gemini Enterprise Agent Platformにて、エージェントとモデルの評価機能が一般提供されました。品質、安全性、ツール使用能力などを測定する20以上の指標が提供され、開発から本番運用まで一貫した品質管理が可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Gemini Enterprise Agent Platform, Cloud Storage |
| 特徴・性能 | 20以上の事前構築済み指標、適応型ルーブリック、ドリフト検知 |
| 関連サービス | Agent Platform SDK, agents-cli, ADK |

> 🔗 **参考リンク**
> https://developers.googleblog.com/agent-and-model-evaluations-in-gemini-enterprise-agent-platform-are-now-ga/

##### Enable on-demand expertise with Agent Skills in Genkit Go

Genkit（Go言語版）において「Agent Skills」機能がサポートされました。必要な時だけ専門知識を読み込む「プログレッシブ・ディスクロージャー」方式を採用することで、トークン消費を抑えつつモデルの精度を維持します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Genkit (Go), LLM |
| 特徴・性能 | SKILL.mdによる専門知識のパッケージ化と動的ロード |
| 対応環境 | Go, TypeScript, Python, Dart |

> 🔗 **参考リンク**
> https://developers.googleblog.com/enable-on-demand-expertise-with-agent-skills-in-genkit-go/

#### Devin

##### Redesigned Changes Tab

Devinの最新リリースでは、ChangesタブのUI刷新やMCPツールの実行環境変更など、広範な機能改善が行われました。特に開発者の生産性を高めるためのUI改善と、エンタープライズ向けの管理機能が強化されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| UI改善 | Changesタブのファイルツリー表示や、セッション管理の整理。 |
| MCP実行環境 | MCPツールをセッションのリモートマシンではなくDevinのサーバーで実行するように変更。 |
| 管理機能 | Slackアクセス制御やGitHubリポジトリの自動化トリガー設定などを強化。 |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-07-31-redesigned-changes-tab

---

### クラウド

#### AWS

##### Amazon Aurora DSQL adds multi-Region cluster support in four more Regions

Amazon Aurora DSQLが新たに4つのリージョンでマルチリージョンクラスターをサポートしました。アクティブ・アクティブ構成による高可用性と強力な整合性を備え、リージョン障害時も継続的なサービス提供が可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Aurora DSQL |
| 特徴・性能 | マルチリージョン・アクティブ・アクティブ構成、強力な整合性 |
| 対応環境 | 欧州・アジア太平洋の計4リージョン追加 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-aurora-dsql-adds-multi-region-clusters-four-more-regions/

##### Amazon CloudWatch announces managed Prometheus collectors

Amazon CloudWatchがマネージドPrometheusコレクターを発表しました。エージェントのデプロイや管理が不要となり、PromQLを使用してAWSリソースのメトリクスを統合的に監視・アラート設定が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon CloudWatch, Prometheus, OpenTelemetry |
| 特徴・性能 | エージェントレスなメトリクス収集、PromQL対応 |
| 関連サービス | EKS, EC2, ECS, MSK, OpenSearch |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/cloudwatch-managed-collectors/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Gemini Agent Platformでの評価パイプライン構築 | AIエンジニア | 🔴 高 |
| LambdaのJavaランタイムをAL2023へ移行計画の策定 | インフラエンジニア | 🔴 高 |
| Devinの最新UIとMCP実行環境の確認 | 開発者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Aurora DSQL adds multi-Region... | クラウド | aws | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-aurora-dsql-adds-multi-region-clusters-four-more-regions/ |
| Amazon RDS for Oracle now offers... | クラウド | aws | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-rds-oracle-r8i-m8i/ |
| AWS Lambda now supports Java 8, 11, 17... | クラウド | aws | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-java-amazon-linux/ |
| Amazon CloudWatch announces managed... | クラウド | aws | https://aws.amazon.com/about-aws/whats-new/2026/07/cloudwatch-managed-collectors/ |
| AWS CodeDeploy now available in five... | クラウド | aws | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-codedeploy-five-additional-regions |
| Agent and Model Evaluations in Gemini... | AI/LLM | google | https://developers.googleblog.com/agent-and-model-evaluations-in-gemini-enterprise-agent-platform-are-now-ga/ |
| Enable on-demand expertise with Agent... | AI/LLM | google | https://developers.googleblog.com/enable-on-demand-expertise-with-agent-skills-in-genkit-go/ |
| Redesigned Changes Tab | AI/LLM | devin | https://docs.devin.ai/release-notes/overview#2026-07-31-redesigned-changes-tab |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Google Gemini Enterprise Agent Platformの評価機能がGAとなり、AIエージェントの品質管理が大幅に強化されました。

📌 **ピックアップ**
• Gemini: エージェント評価機能がGA、一貫した品質測定が可能に
• AWS: Aurora DSQLがマルチリージョン対応を拡大、CloudWatchがマネージドPrometheus収集に対応
• Devin: UI刷新とMCP実行環境のサーバーサイド移行を実施

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-08-01*
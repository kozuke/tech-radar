# Tech Radar Daily Digest - 2026-06-29

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、Amazon GuardDutyにおける「AI-powered investigations（プレビュー）」を発表しました。これは、セキュリティ調査における手動プロセスの負担を軽減し、脅威検知の精度と速度を劇的に向上させる新機能です。ナレッジグラフと脅威インテリジェンスを活用し、過去90日間の関連アクティビティや影響を受けたリソースを数分で分析することで、セキュリティアナリストが「真の脅威」に集中できる環境を提供します。

また、Amazon OpenSearch Serviceにおいても「AI-assisted migrations」が導入されました。SolrやElasticsearchなどの自己管理型環境からAWSへの移行プロセスを、KiroやClaude CodeといったAIツールを活用して自動化・最適化するものです。これらの発表は、AWSがセキュリティ運用やインフラ移行といった複雑で時間のかかるタスクに対し、生成AIを実用的な「エージェント」として組み込む戦略を加速させていることを示しています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude

##### Claude TagがAWS MarketplaceのClaude Enterpriseで利用可能に

Anthropicは、Slackなどのチャネル内で直接Claudeと協働できる「Claude Tag」のベータ版を公開しました。AWS Marketplace経由でClaude Enterpriseを利用しているユーザーは、既存のエンタープライズ契約内でこの機能を利用でき、チャネルごとの権限管理や予算制御が可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Enterprise, Slack連携 |
| 特徴・性能 | チャネルごとのID管理、予算制御、マルチプレイヤー対応 |
| 対応環境 | AWS Marketplace (Claude Enterprise) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/claude-tag-aws-marketplace/

---

### クラウド

#### AWS

##### Amazon Bedrock Guardrailsに自動推論によるポリシー改善ワークフローを追加

Amazon Bedrock Guardrailsの「Automated Reasoning（自動推論）」チェック機能が強化され、ポリシーの精度を向上させるための新しいワークフローが導入されました。自然言語テストを通じた反復的なポリシー改善や、曖昧な翻訳を解消する機能により、生成AIのハルシネーション抑制と信頼性の向上が期待できます。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| 反復的ポリシー改善 | 自然言語テストに基づき、ポリシーを通過させるための変更をシステムが自動推論する。 |
| 曖昧さ解消 | 変数の説明や型定義を自動的に洗練させ、翻訳の曖昧さを低減する。 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-guardrails/

##### Amazon CloudWatchがEKS向けOTel Container Insightsをリリース

Amazon EKS環境において、OpenTelemetry（OTel）を用いた30秒間隔のインフラメトリクス収集が可能になりました。cAdvisorやKube State Metricsなどのオープンソースレシーバーを活用し、PromQLクエリでノードやポッド、ワークロードを横断した監視が容易になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | OpenTelemetry, PromQL, Kubernetes |
| 特徴・性能 | 30秒間隔の粒度、Prometheus/Grafanaとの直接接続 |
| 対応環境 | Amazon EKS |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-otel-amazon-eks/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| GuardDutyのAI調査機能を有効化し、脅威検知の効率化を試す | セキュリティ管理者 | 🔴 高 |
| Bedrock Guardrailsのポリシー改善ワークフローでAI応答の精度を検証する | AIエンジニア | 🟡 中 |
| EKSクラスターの監視をOTel Container Insightsへ移行する検討 | SRE/インフラ担当 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon GuardDuty AI-powered investigations | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-guardduty/ |
| Automated Reasoning checks in Bedrock Guardrails | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-guardrails/ |
| Amazon CloudWatch launches OTel Container Insights | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-otel-amazon-eks/ |
| Claude Tag is now available in beta | Claude | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/claude-tag-aws-marketplace/ |
| Amazon OpenSearch Service now offers AI-assisted migrations | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-opensearch-service-ai-migrations |
| 0.143.0-alpha.29 | OpenAI | openai_codex | https://github.com/openai/codex/releases/tag/rust-v0.143.0-alpha.29 |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AWSがGuardDutyとOpenSearchにAIによる自動化機能を導入し、セキュリティと移行作業の効率化を大幅に強化しました。

📌 **ピックアップ**
• GuardDuty: AIによる脅威調査機能がプレビュー開始
• Bedrock: 自動推論によるポリシー改善ワークフローを追加
• Claude Tag: Slack等のチャネルでClaudeと協働可能に
• CloudWatch: EKS向けOTel Container Insightsが登場

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-29*
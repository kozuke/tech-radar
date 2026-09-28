# Tech Radar Daily Digest - 2026-09-28

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Amazon SageMaker HyperPod Inference Gatewayの登場とAWSのインフラ拡張**

本日は、LLM推論の効率化とAWSのグローバルインフラ拡充が大きな注目を集めています。特に「Amazon SageMaker HyperPod Inference Gateway」は、Kubernetesネイティブなルーティングシステムとして、推論信号に基づいた動的なトラフィック制御を実現し、First-token latencyを最大82%削減するなど、大規模言語モデルの運用コストとパフォーマンスに劇的な改善をもたらします。また、Amazon GameLiftのリージョン・Local Zonesの大幅な拡大により、世界各地での低遅延なゲーム体験提供が可能となり、クラウドインフラの最適化が加速しています。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### Amazon SageMaker HyperPod Inference Gateway for scalable LLM inference

Amazon SageMaker HyperPod Inference Gatewayは、既存のEKS環境にアドオンとして導入可能なGPU対応ルーティングシステムです。推論信号に基づいたリアルタイムなルーティングを行うことで、従来のラウンドロビン方式と比較して大幅なレイテンシ削減を実現します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Kubernetes, Envoy, vLLM, SGLang |
| 特徴・性能 | First-token latency最大82%削減、p99 TTFT 97-98%削減 |
| 対応環境 | Amazon EKS, SageMaker HyperPod |
| 関連サービス | Amazon SageMaker, Amazon EKS |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-hyperpod-inference-gateway/

---

##### AWS Network Security Manager is now generally available

AWS Network Security Managerは、AWS組織全体でファイアウォールやDDoS保護設定を統一・自動化するための包括的な管理ソリューションです。設定のドリフト検知や自動修復機能を備えており、セキュリティ運用のオーバーヘッドを大幅に削減します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS WAF, AWS Shield Advanced |
| 特徴・性能 | セキュリティポリシーの自動展開とドリフト検知 |
| 対応環境 | AWS Organization |
| 関連サービス | AWS WAF, AWS Shield Advanced |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/network-security-manager-us-east-va/

---

##### Run interactive workloads on Amazon EMR on EKS with Spark Connect

Amazon EMR on EKSがSpark Connectをサポートし、SageMaker Unified StudioやローカルIDEから直接対話的なSparkセッションを実行可能になりました。クライアント・サーバーアーキテクチャにより、開発環境を維持したままリモートのEKSクラスター上でSparkジョブをデバッグできます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Apache Spark 3.5/4.1, Spark Connect |
| 特徴・性能 | 永続的なSparkコンテキストによる対話型開発 |
| 対応環境 | Amazon EKS, EMR release 7.14以降 |
| 関連サービス | Amazon SageMaker Unified Studio |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/emr-eks-spark-connect-interactive/

---

##### Amazon GameLift Servers now available in 5 new regions and 8 Local Zones

Amazon GameLift Serversが新たに5つのAWSリージョンと8つのLocal Zonesで利用可能になりました。これにより、世界中のプレイヤーに対してより物理的に近い場所からゲームサーバーを提供し、レイテンシを最小限に抑えることが可能となります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-gamelift-servers-region-expansion-2026

---

##### Amazon RDS supports Multi-AZ for SQL Server Developer Edition

Amazon RDS for SQL ServerがDeveloper EditionでのMulti-AZ配置をサポートしました。Always On Availability Groupsを利用することで、本番環境と同等の高可用性構成を低コストで検証・テストすることが可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-rds-sql-server-multi-az-developer-edition/

---

### AI/LLM

#### OpenAI

##### OpenAI Codex CLI リリース (0.159.0-alpha.8 ～ 0.159.0-alpha.11)

OpenAI Codex CLIのアルファ版が連続してリリースされました。開発の進捗に伴い、複数のマイナーアップデートと修正が適用されています。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| SageMaker HyperPodでの推論レイテンシ検証 | AIエンジニア | 🔴 高 |
| RDS SQL Server Developer EditionでのHA構成テスト | DB管理者 | 🟡 中 |
| 新規リージョンへのGameLiftサーバー展開検討 | ゲーム開発者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Network Security Manager GA | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/network-security-manager-us-east-va/ |
| SageMaker HyperPod Inference Gateway | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-hyperpod-inference-gateway/ |
| EMR on EKS with Spark Connect | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/emr-eks-spark-connect-interactive/ |
| GameLift Region Expansion | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-gamelift-servers-region-expansion-2026 |
| RDS SQL Server Multi-AZ | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-rds-sql-server-multi-az-developer-edition/ |
| Codex CLI Releases | AI | GitHub | https://github.com/openai/codex/releases |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

SageMaker HyperPod Inference Gatewayが登場し、LLM推論のレイテンシが最大82%削減可能に。

📌 **ピックアップ**
• AWS Network Security ManagerがGA、セキュリティ運用の自動化を強化
• EMR on EKSがSpark Connectをサポートし、対話型開発が容易に
• Amazon GameLiftが5リージョン・8 Local Zonesへ拡大
• RDS SQL Server Developer EditionでMulti-AZ構成が利用可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-09-28*
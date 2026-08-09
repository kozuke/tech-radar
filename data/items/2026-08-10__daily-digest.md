# Tech Radar Daily Digest - 2026-08-10

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、セキュリティと運用効率を向上させる重要なアップデートを複数発表しました。特に注目すべきは、AWS WAFにおける「Salt Securityマネージドルールグループ」の導入です。これにより、AIエージェントやMCP（Model Context Protocol）エンドポイントからのトラフィックを含む、高度なAPI攻撃に対する防御が大幅に強化されます。従来の手動設定を不要にし、認証されていないアクセスや異常なクエリを自動的に遮断できるため、APIセキュリティの運用負荷が大幅に軽減されます。

また、Amazon OpenSearch UIにおけるネットワークアクセスコントロールの強化も重要です。IAM条件キーを活用して、承認されたネットワークからのみアクセスを制限できるようになり、組織全体で一貫したデータ境界を構築することが可能になりました。これらのアップデートは、クラウド環境におけるセキュリティの「自動化」と「ガバナンス強化」を強力に推進するものです。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### AWS WAF now supports a Salt Security managed rule group for API and MCP threat detection

AWS WAFでSalt Securityのマネージドルールグループが利用可能になり、APIやAIエージェント、MCPエンドポイントを標的とした脅威の検知・緩和が強化されました。この機能により、ブルートフォース攻撃やSSRF、GraphQLの不正クエリなどを自動的にブロックし、セキュリティ運用を効率化できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS WAF, Salt Security |
| 特徴・性能 | AIエージェント/MCPトラフィックの識別とブロック |
| 対応環境 | AWS Marketplace対応の全リージョン |
| 関連サービス | AWS WAF, AWS Marketplace |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/aws-waf-salt-security-managed-rules/

---

##### AWS Glue Schema Registry is now available in ten more AWS regions

AWS Glue Schema Registryが新たに10のリージョンで利用可能になりました。これにより、ストリーミングデータにおけるスキーマの進化を管理し、データ品質の向上とアプリケーション間の連携を簡素化するサーバーレス機能が、より広範な地域で活用できるようになります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Glue, Apache Avro, JSON, Protobuf |
| 特徴・性能 | ストリーミングデータのスキーマ管理とバリデーション |
| 対応環境 | アジアパシフィック（ニュージーランド、タイ、ハイデラバード、大阪、マレーシア、メルボルン、台北）、メキシコ、イスラエル、カナダ西 |
| 関連サービス | Kafka, Kinesis, Flink, Lambda |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/aws-gsr-10-more-regions

---

##### Amazon OpenSearch UI now supports Network Access Control

Amazon OpenSearch UIにおいて、ネットワークアクセスコントロールがサポートされました。IAM条件キーを使用して、特定のVPCやIPアドレスからのアクセスのみを許可する設定が可能となり、組織全体での一貫したデータ境界の保護が強化されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | IAM条件キー (aws:SourceVpce, aws:SourceVpc, aws:SourceIp) |
| 特徴・性能 | 3段階（プリンシパル、VPCエンドポイント、RCP）でのアクセス制限 |
| 対応環境 | OpenSearch UI提供の全リージョン |
| 関連サービス | Amazon OpenSearch Service |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/opensearch-ui-network-access-control

---

##### AWS Transform for migrations automates post-launch actions

AWS Transformによる移行プロセスにおいて、移行後のアクションの自動化が可能となりました。SSMドキュメントを活用して、テストやカットオーバー直後の設定作業を自動実行することで、サーバーごとの手動設定によるミスを削減し、移行作業の効率を大幅に向上させます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Systems Manager (SSM) |
| 特徴・性能 | 移行後の自動設定実行、マルチアカウント対応 |
| 対応環境 | AWS Transform提供の全リージョン |
| 関連サービス | AWS Systems Manager, EC2 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/aws-transform-for-migrations-automates-post-launch-actions

---

##### Amazon Connect Customer adds one-click drill-down on real-time metrics dashboards

Amazon Connectのリアルタイムメトリクスダッシュボードに、ワンクリックでのドリルダウン機能が追加されました。管理者はサマリー画面から特定のキューやエージェントの活動状況を即座に詳細表示できるため、待ち時間の急増時などの迅速な対応が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Connect Analytics |
| 特徴・性能 | リアルタイムメトリクスの詳細分析（ドリルダウン） |
| 対応環境 | 全商用リージョンおよびAWS GovCloud (US-West) |
| 関連サービス | Amazon Connect |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-connect-drill-down-metrics/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| APIセキュリティの強化（Salt Securityルール適用） | セキュリティ担当者 | 🔴 高 |
| OpenSearch UIへのネットワーク制限設定 | インフラ管理者 | 🟡 中 |
| 移行後の自動化設定（AWS Transform）の確認 | クラウド移行チーム | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS WAF now supports a Salt Security managed rule group | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/08/aws-waf-salt-security-managed-rules/ |
| AWS Glue Schema Registry is now available in ten more AWS regions | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/08/aws-gsr-10-more-regions |
| Amazon OpenSearch UI now supports Network Access Control | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/08/opensearch-ui-network-access-control |
| AWS Transform for migrations automates post-launch actions | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/08/aws-transform-for-migrations-automates-post-launch-actions |
| Amazon Connect Customer adds one-click drill-down | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-connect-drill-down-metrics/ |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWS WAFがSalt Securityのマネージドルールに対応し、AIエージェントやAPIへの攻撃防御が強化されました。

📌 **ピックアップ**
• AWS WAF: AI/MCPトラフィックの自動検知・防御に対応
• OpenSearch UI: ネットワークアクセスコントロールでセキュリティ強化
• AWS Transform: 移行後の設定作業を自動化し工数を削減
• Amazon Connect: リアルタイムダッシュボードのドリルダウン機能追加

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-08-10*
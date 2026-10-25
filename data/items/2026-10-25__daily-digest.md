# Tech Radar Daily Digest - 2026-10-25

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AWSとMegaportが連携した「AWS Interconnect - last mile」のプレビュー開始**
AWSは、Megaportと共同で「AWS Interconnect - last mile」のプレビュー提供を開始しました。これは、支社やデータセンターからAWSへの接続を数クリックで完了させるフルマネージドなネットワークサービスです。従来、複雑な設定が必要だったBGPピアリングやVLAN構成、ASN割り当てなどを自動化し、SDN（Software Defined Network）を活用することでネットワーク構築の摩擦を大幅に軽減します。今後は1Gbpsから100Gbpsまでの動的な帯域幅スケーリングも可能となり、高い可用性と99.99%のSLAを保証することで、エンタープライズのクラウド接続を劇的に簡素化する重要な一歩となります。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### Amazon OpenSearch Service introduces intelligent ingestion for logs and documents in Amazon S3

Amazon OpenSearch Serverlessに、S3上のログやドキュメントを検索可能なコンテンツへ自動変換する「インテリジェント・インジェスト」機能が追加されました。この機能は、データ型の自動検出、ベクトル埋め込みの生成、非構造化データ（PDFやWord等）の解析をフルマネージドで行い、インフラ管理を不要にします。視覚情報のテキスト化機能も備えており、検索体験の向上が期待されます。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| インジェストジョブ | 移行やバックフィルなどの一括データロード用機能。 |
| インジェストストリーム | S3への新規オブジェクト到着に合わせてインデックスを同期する機能。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon OpenSearch Serverless (NextGen) |
| 特徴・性能 | 自動データ型検出、ベクトル埋め込み生成、視覚情報のテキスト化 |
| 対応環境 | JSON, NDJSON, PDF, Word, Markdown等 |
| 関連サービス | Amazon S3 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-opensearch-intelligent-ingestion-logs-documents-s3

---

##### Amazon EMR on EKS reduces EMR charge by 30 percent

Amazon EMR on EKSの利用料金が30%値下げされました。この変更はvCPU時間およびGB時間あたりの料金に適用され、ユーザー側での追加設定なしで自動的に反映されます。これにより、Apache Sparkワークロードをより低コストで実行可能となり、コスト効率が大幅に向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon EMR on EKS |
| 特徴・性能 | EMR料金の30%削減 |
| 対応環境 | EMR on EKSが利用可能な全リージョン |
| 関連サービス | Amazon EKS |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/emr-eks-reduces-emr-charge-30-percent/

---

##### Amazon MSK Connect now supports pausing and resuming connectors

Amazon MSK Connectでコネクタの一時停止と再開が可能になりました。従来はコネクタの停止には削除と再作成が必要でしたが、今回のアップデートにより、設定やオフセットを保持したまま一時停止できるため、メンテナンスやトラブルシューティング時の運用負荷とリスクが軽減されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon MSK Connect |
| 特徴・性能 | 設定・オフセットを保持したままの一時停止・再開 |
| 対応環境 | Amazon MSK Connect対応全リージョン |
| 関連サービス | Amazon MSK |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-connect-pause-resume

---

##### AWS Direct Connect announces 100G expansion in Bangalore, India

インド・バンガロールのNetmagic DC2データセンターにおいて、AWS Direct Connectの100Gbps専用接続が利用可能になりました。これにより、より高速かつ一貫したネットワークパフォーマンスを必要とする企業が、AWSの各リージョンやローカルゾーンへ直接アクセスできるようになります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Direct Connect |
| 特徴・性能 | 100Gbps専用接続の提供 |
| 対応環境 | バンガロール（Netmagic DC2） |
| 関連サービス | AWS Local Zones |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/aws-direct-connect-100g-bangalore/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| EMR on EKSのコスト削減確認 | クラウドインフラ担当者 | 🟢 低 |
| MSK Connectの一時停止機能の運用フローへの組み込み | データエンジニア | 🟡 中 |
| AWS Interconnectのプレビュー検証 | ネットワークエンジニア | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EMR on EKS reduces EMR charge by 30 percent | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/emr-eks-reduces-emr-charge-30-percent/ |
| Amazon OpenSearch Service introduces intelligent ingestion | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-opensearch-intelligent-ingestion-logs-documents-s3 |
| AWS Direct Connect announces 100G expansion in Bangalore | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/aws-direct-connect-100g-bangalore/ |
| Amazon MSK Connect now supports pausing and resuming connectors | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-connect-pause-resume |
| AWS announces AWS Interconnect - last mile preview | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/aws-announces-AWS-interconnect-last-mile-megaport-preview/ |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWSとMegaportが連携した「AWS Interconnect - last mile」のプレビューが開始され、ネットワーク構築が大幅に簡素化されます。

📌 **ピックアップ**
• AWS Interconnect: Megaport連携で拠点接続を数クリックで自動化
• OpenSearch: S3データの検索用インジェストがフルマネージド化
• EMR on EKS: 料金が30%値下げされコスト効率が向上
• MSK Connect: コネクタの一時停止・再開が可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-10-25*
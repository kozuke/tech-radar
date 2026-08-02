# Tech Radar Daily Digest - 2026-08-03

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Amazon MSK ExpressがApache Icebergへのストリーミングデータ直接配信に対応しました。これにより、KafkaトピックをAmazon S3 Tables上のIcebergテーブルとして継続的にマテリアライズすることが可能になります。この機能は、従来のカスタムパイプライン構築に伴う複雑なフォーマット変換や、小規模ファイル問題によるクエリ性能低下を解消し、インフラコストを最大60%、クエリコストを最大30%削減できる見込みです。

また、AWS GovCloudにおいてxAIの「Grok 4.3」およびGoogle DeepMindの「Gemma 4」シリーズがAmazon Bedrockで利用可能になりました。特にGrok 4.3は推論能力を重視した設計で、エージェントワークフローやエンタープライズ向けの複雑なタスクに適しています。一方、Gemma 4は多様なモデルサイズとマルチモーダル対応により、コストやレイテンシに応じた柔軟な選択肢を提供し、政府機関等の厳格な環境下での生成AI活用を加速させます。

---

## 📰 今日のニュース

### AI/LLM

#### Amazon Bedrock

##### Grok 4.3 from xAI is now available on Amazon Bedrock in AWS GovCloud (US-West)

xAIの推論特化型モデル「Grok 4.3」がAWS GovCloudで利用可能になりました。本モデルは推論努力の調整が可能で、ツール利用や指示追従能力に優れており、カスタマーサポートや法務・金融文書の分析など、エンタープライズ用途での活用が期待されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Grok 4.3 (xAI) |
| 特徴・性能 | 推論努力の調整、ツール利用、トークン効率性 |
| 対応環境 | Amazon Bedrock (AWS GovCloud) |
| 関連サービス | Mantle (推論エンジン) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/grok-4-3-bedrock-govcloud/

---

##### Gemma 4 models are now available on Amazon Bedrock in AWS GovCloud (US-West)

Google DeepMindのオープンウェイトモデル「Gemma 4」ファミリーがAWS GovCloudで利用可能になりました。31B、26B-A4B、E2Bの3つのバリエーションが提供され、推論から低レイテンシなインタラクティブ用途まで、幅広いニーズに対応します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Gemma 4 (31B, 26B-A4B, E2B) |
| 特徴・性能 | 256Kトークンのコンテキストウィンドウ、マルチモーダル対応 |
| 対応環境 | Amazon Bedrock (AWS GovCloud) |
| 関連サービス | Amazon Bedrock 推論エンジン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/gemma-4-bedrock-govcloud/

---

### クラウド

#### AWS

##### Amazon MSK Express brokers now deliver data to streaming tables for Apache Iceberg

Amazon MSK ExpressがApache Icebergテーブルへの直接配信をサポートしました。インラインでのコンパクション機能により小規模ファイル問題を解決し、データ鮮度を維持しつつクエリ性能を最適化します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/about-aws/whats-new/2026/07/aws-msk-streaming-tables-for-apache-iceberg

---

##### AWS Managed Microsoft AD now supports Standard to Enterprise Edition upgrade

AWS Managed Microsoft ADにおいて、Standard EditionからEnterprise Editionへのインプレースアップグレードが可能になりました。既存のディレクトリ設定や信頼関係を維持したまま、最大50万オブジェクトまでスケーリングを拡張できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/aws-microsoft-ad-edition-upgrade/

---

##### Amazon OpenSearch Service now supports OpenSearch version 3.7

Amazon OpenSearch Serviceがバージョン3.7に対応しました。ベクトル検索の圧縮技術によるリソース効率化や、クエリインサイト機能の強化により、検索精度の向上とコスト最適化を同時に実現します。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| ベクトル検索 | 1ビットスカラー量子化によりストレージとメモリ消費を削減。 |
| クエリインサイト | 自動クエリ推奨や完了済みクエリのキャッシュ機能を追加。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | OpenSearch 3.7, Faiss, Lucene |
| 特徴・性能 | ベクトル圧縮、ハイブリッド検索最適化 |
| 対応環境 | Amazon OpenSearch Service |
| 関連サービス | Amazon S3 (クエリデータエクスポート) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-opensearch-service/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| MSKからIcebergへの移行検証 | データエンジニア | 🟡 中 |
| OpenSearch 3.7へのアップグレード検討 | 検索基盤担当者 | 🟡 中 |
| Managed ADの容量制限確認とアップグレード | インフラ管理者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon MSK Express brokers now deliver data to streaming tables for Apache Iceberg | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-msk-streaming-tables-for-apache-iceberg |
| Grok 4.3 from xAI is now available on Amazon Bedrock in AWS GovCloud (US-West) | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/grok-4-3-bedrock-govcloud/ |
| Gemma 4 models are now available on Amazon Bedrock in AWS GovCloud (US-West) | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/gemma-4-bedrock-govcloud/ |
| AWS Managed Microsoft AD now supports Standard to Enterprise Edition upgrade | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/08/aws-microsoft-ad-edition-upgrade/ |
| Amazon OpenSearch Service now supports OpenSearch version 3.7 | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-opensearch-service/ |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon MSKがApache Icebergへの直接配信に対応し、データパイプラインのコストと性能を大幅に改善。

📌 **ピックアップ**
• Amazon Bedrock: GovCloudでGrok 4.3とGemma 4が利用可能に
• OpenSearch 3.7: ベクトル検索の効率化とクエリ分析機能が強化
• Managed AD: StandardからEnterpriseへのインプレースアップグレードに対応

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-08-03*
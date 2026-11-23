# Tech Radar Daily Digest - 2026-11-23

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、Amazon Cognitoのマルチリージョンレプリケーション（MRR）の対応リージョンを大幅に拡大しました。これまで16の商用リージョンとAWS GovCloudで利用可能でしたが、新たにアジア太平洋（ハイデラバード、香港、ジャカルタ、マレーシア、メルボルン、ニュージーランド、大阪、台北、タイ）、カナダ（カルガリー）、欧州（ミラノ、スペイン、チューリッヒ）、イスラエル（テルアビブ）、メキシコ（セントラル）、アフリカ（ケープタウン）が追加されました。これにより、データレジデンシーやコンプライアンス要件を満たしつつ、より広範なリージョンで災害復旧（DR）対策が可能となり、ミッションクリティカルなアプリケーションの可用性が向上します。

また、Amazon Neptune ServerlessがAWS Graviton4プロセッサに対応し、最大30%のパフォーマンス向上とより精緻なスケーリングを実現しました。このアップデートにより、生成AIアプリケーションやリアルタイムの不正検知など、負荷が急激に変動するグラフデータベースワークロードにおいて、コスト効率と応答速度の両面で大きな改善が期待されます。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### Amazon Cognito extends multi-Region replication to additional AWS Regions

Amazon Cognitoのマルチリージョンレプリケーション（MRR）が、新たに16のAWSリージョンで利用可能になりました。これにより、ユーザーIDや認証設定のリアルタイム同期がより広範な地域で行えるようになり、DR対策やデータ主権要件への対応が強化されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Cognito, AWS KMS |
| 特徴・性能 | ニアリアルタイムのユーザーデータ同期 |
| 対応環境 | AWS全リージョン（順次拡大中） |
| 関連サービス | AWS KMS (CMKが必要) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-mrr-opt-in-regions/

---

##### Amazon Neptune Serverless now delivers up to 30% better performance and smarter scaling

Amazon Neptune ServerlessがAWS Graviton4プロセッサへ移行し、同一価格で最大30%のパフォーマンス向上を実現しました。スケーリングアルゴリズムも最適化され、生成AIやグラフクエリが多用されるワークロードにおいて、より効率的なリソース活用が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Neptune Serverless, AWS Graviton4 |
| 特徴・性能 | 最大30%の性能向上、動的スケーリングの最適化 |
| 対応環境 | AWS全リージョン |
| 関連サービス | AWS Management Console, AWS CLI |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/aws-neptune-serverless-r8g-generally-available

---

##### Amazon CloudWatch extends the PromQL query window to 30 days

Amazon CloudWatchにおけるOpenTelemetryメトリクスへのPromQLクエリ期間が、従来の7日間から30日間に延長されました。これにより、月次でのSLO（サービスレベル目標）の算出や、長期的なトレンド分析、より信頼性の高いキャパシティ予測が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon CloudWatch, PromQL, OpenTelemetry |
| 特徴・性能 | クエリ期間を7日から30日へ拡大 |
| 対応環境 | PromQL対応の全AWSリージョン |
| 関連サービス | Amazon CloudWatch Dashboards |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-promql-query-30days/

---

### 開発ツール

#### AWS Partner Central

##### Account Mapping and Planning now available in AWS Partner Central

AWS Partner Centralに「Account Mapping and Planning」機能が追加され、パートナーはターゲットアカウントをAWSの記録と自動照合できるようになりました。スプレッドシートによる手動管理を廃止し、AIによるインサイトを活用して、より早期にAWSとの共同営業戦略を立てることが可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/account-mapping-and-planning/

---

##### Demand Center now available in AWS Partner Central

AWS Partner Centralに「Demand Center」が統合され、マーケティングキャンペーンの計画から実行、分析までをAIを活用して一元管理できるようになりました。AIによるコンテンツ生成やリードのエンリッチメント機能により、パートナーの需要創出活動を効率化します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/demand-center-partner-central/

---

### Workspace

#### Google Workspace

##### Email meeting guests from Google Calendar with the full capabilities of Gmail

Googleカレンダーの「ゲストにメールを送信」機能が刷新され、Gmailの作成画面が直接呼び出せるようになりました。リッチテキスト編集、署名、AIによる文章作成支援などが利用可能になり、会議アジェンダの共有や事前確認が大幅に効率化されます。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/11/email-meeting-guests-from-google-Calendar-with-the-full-capabilities-of-Gmail.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Cognito MRRの対象リージョン確認とDR戦略の見直し | クラウドアーキテクト | 🔴 高 |
| Neptune ServerlessのGraviton4移行準備 | DB管理者 | 🟡 中 |
| CloudWatchでの30日SLO監視設定の導入 | SRE/運用担当者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Cognito extends multi-Region replication... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-mrr-opt-in-regions/ |
| Amazon Neptune Serverless now delivers... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/aws-neptune-serverless-r8g-generally-available |
| Amazon CloudWatch extends the PromQL query... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-promql-query-30days/ |
| Account Mapping and Planning now available... | 開発ツール | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/account-mapping-and-planning/ |
| Demand Center now available... | 開発ツール | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/demand-center-partner-central/ |
| Email meeting guests from Google Calendar... | Workspace | Google | http://workspaceupdates.googleblog.com/2026/11/email-meeting-guests-from-google-Calendar-with-the-full-capabilities-of-Gmail.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon Cognitoのマルチリージョンレプリケーションが大幅拡大し、DR対策がより柔軟に。

📌 **ピックアップ**
• Neptune ServerlessがGraviton4対応で30%高速化
• CloudWatchのPromQLクエリ期間が30日に延長
• GoogleカレンダーからGmailのフル機能でゲストへメール送信が可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-23*
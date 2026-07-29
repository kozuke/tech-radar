# Tech Radar Daily Digest - 2026-07-30

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、Oracle Cloud Infrastructure (OCI) とのマルチクラウド接続を実現する「AWS Interconnect - multicloud」の一般提供（GA）を開始しました。これまで、クラウド間を接続する際にはユーザー自身で複雑なネットワークを構築・管理する必要がありましたが、本サービスにより、目的別に最適化された技術を複数のクラウドで柔軟に組み合わせることが可能になります。まずは米国東部（バージニア北部）リージョンから提供が開始され、今後はGoogle Cloudに加え、2026年後半にはMicrosoft Azureへの対応も予定されています。

また、AI開発ツール「Cursor」がiPad版を全有料プラン向けにリリースしました。iPadの大画面に最適化されたレイアウトにより、サイドバーチャットの常時表示や分割画面でのコードレビュー、Apple Pencilを用いた画像への直接コメントなどが可能になりました。モバイル環境での開発・レビュー体験が大幅に向上しており、場所を選ばない開発ワークフローの強化が期待されます。

---

## 📰 今日のニュース

### AI/LLM

#### Cursor

##### Cursor for iPadが全有料プランで利用可能に

CursorのiPad版が正式にリリースされ、有料プランユーザーであれば誰でも利用可能になりました。大画面を活かしたマルチウィンドウ対応や、PR（プルリクエスト）の作成・レビュー・マージまでを完結できる機能が搭載されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| iPad最適化レイアウト | サイドバーチャットの固定や分割画面によるレビュー、ファイル差分のフル表示に対応。 |
| PRレビュー機能 | コメント、チェック、承認を含むPRの全工程をモバイル端末から操作可能。 |
| インボックス機能 | 進行中のタスクやレビューが必要なPRを一覧管理できる専用インボックスを追加。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | モバイル向けIDE、AIエージェント統合 |
| 対応環境 | iPadOS, iOS |
| 関連サービス | Bitbucket, Azure DevOps |

> 🔗 **参考リンク**
> https://cursor.com/changelog#2026-07-29-cursor-for-ipad-is-now-available-on-all-paid-plans

---

### クラウド

#### AWS

##### Amazon Redshift Data APIが大幅機能強化

Amazon Redshift Data APIに、ロングポーリングやセッション管理、バッチ実行の柔軟性向上といった新機能が追加されました。これにより、API呼び出し回数の削減や、ETLパイプラインにおけるエラー処理の効率化が実現します。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| ロングポーリング | SQL完了までレスポンスを待機することで、ポーリング回数を削減。 |
| ListSessions | アクティブなセッションの列挙やフィルタリングが可能に。 |
| 柔軟なバッチ実行 | バッチ内の各文を独立して実行するAUTO_COMMITモードを追加。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Redshift Data API |
| 対応環境 | Provisioned / Serverless |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-data-api-longpolling-listsession-flexiblebatchexecute/

##### AWS WAFにテキスト変換機能が追加

AWS WAFにおいて、リクエスト内容をアプリケーションの解釈に合わせて正規化する新しいテキスト変換機能が導入されました。クエリ引数のパース前変換や、SHA256、コマンドラインデコードなどの高度な変換が可能になり、セキュリティ強度が向上します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-waf/

---

### Workspace

#### Google Workspace

##### Google SheetsとCalendarのUI/機能アップデート

Google Sheetsでは散布図における複数X軸のサポートが追加され、Excelとの互換性が向上しました。また、Google Calendarでは大画面モニター向けに情報の密度を調整できるオプションが追加され、視認性が改善されています。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/create-and-import-scatter-charts-with-multiple-x-series-in-Google-Sheets.html
> http://workspaceupdates.googleblog.com/2026/07/updated-options-to-better-view-google-Calendar-on-large-monitors.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Cursor iPad版の導入検討とワークフローへの組み込み | モバイル開発者 | 🟡 中 |
| Redshift Data APIのバッチ実行モードの活用検討 | データエンジニア | 🟡 中 |
| AWS WAFの新しいテキスト変換ルールによるセキュリティ強化 | セキュリティ担当者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EC2 Auto Scaling Instance Refresh | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-auto-scaling-instance-refresh-cloudformation) |
| Amazon Redshift Data API Updates | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-data-api-longpolling-listsession-flexiblebatchexecute/) |
| AWS WAF Text Transformations | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-waf/) |
| AWS Interconnect - multicloud | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-announces-AWS-interconnect-multicloud-OCI-GA/) |
| Amazon EFS Cross-Account Replication | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-efs-cross-account-replication-aws-gov-cloud-us) |
| Cursor for iPad release | 開発ツール | Cursor | [link](https://cursor.com/changelog#2026-07-29-cursor-for-ipad-is-now-available-on-all-paid-plans) |
| Google Sheets Scatter Charts | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/07/create-and-import-scatter-charts-with-multiple-x-series-in-Google-Sheets.html) |
| Google Calendar Density Options | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/07/updated-options-to-better-view-google-Calendar-on-large-monitors.html) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AWSがOCIとのマルチクラウド接続サービスをGAし、CursorがiPad版を全有料プラン向けにリリースしました。

📌 **ピックアップ**
• AWS Interconnect: クラウド間接続を簡素化する新サービスが登場
• Cursor for iPad: 大画面に最適化されたIDEでモバイル開発が進化
• Redshift Data API: ロングポーリングやバッチ実行の柔軟性が向上
• Google Workspace: Sheetsのグラフ機能とCalendarの表示密度が改善

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-30*
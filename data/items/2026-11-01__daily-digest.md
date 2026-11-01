# Tech Radar Daily Digest - 2026-11-01

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWS WAFにおける「CloudFront向け自動SDK統合」の発表は、セキュリティ運用の負荷を劇的に軽減する重要なアップデートです。これまで、Bot Controlや不正利用防止機能（ATP/ACFP）を利用する際には、すべてのページに手動でスクリプトタグを埋め込む必要があり、これが設定漏れや管理コストの増大を招いていました。今回の機能強化により、CloudFront側で設定を有効にするだけで自動的にSDKが注入されるようになり、アプリケーション側のコード変更やデプロイプロセスを一切変更せずに高度な保護を適用可能になります。

また、Google SlidesにおけるGeminiのアップデートも注目に値します。単一スライドの生成だけでなく、プレゼンテーション全体に対して「スタイルの一括適用」や「複数スライドの要約・統合」といった編集が可能になりました。これにより、資料作成の生産性が大幅に向上するだけでなく、企業内での資料の統一感維持が容易になります。AIが単なるコンテンツ生成ツールから、ドキュメント全体の編集・管理を行うエージェントへと進化していることを示唆しています。

---

## 📰 今日のニュース

### AI/LLM

#### Gemini

##### Edit entire presentations with Gemini in Google Slides

GeminiがGoogle Slidesにおいて、プレゼンテーション全体を対象とした編集機能をサポートしました。サイドパネルからプロンプトを入力することで、スライド全体のスタイル変更、コンテンツの更新、複数スライドの統合などを一括で行うことが可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Gemini (Google AI) |
| 特徴・性能 | スライド全体の一括編集、スタイルの一貫性保持 |
| 対応環境 | Google Slides (英語のみ) |
| 関連サービス | Google Drive |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/10/edit-entire-presentations-with-gemini-in-Google-Slides.html

---

### クラウド

#### AWS

##### Amazon MSK now supports TLS 1.3 for data in transit

Amazon MSKのProvisionedクラスターにおいて、通信の暗号化にTLS 1.3がサポートされました。これにより、より高速かつ安全なデータ転送が可能となり、ポスト量子暗号への備えや厳格なコンプライアンス要件への対応が強化されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | TLS 1.3, MSK Provisioned |
| 特徴・性能 | セキュリティ強化、暗号化通信の高速化 |
| 対応環境 | 全AWSリージョン |
| 関連サービス | Amazon MSK |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-tls/

##### Amazon RDS for Oracle no longer requires automatic minor version upgrades for JVM, Spatial, Locator, and OLAP options

Amazon RDS for Oracleにおいて、JVMやSpatial等のオプションを利用する際の「自動マイナーバージョンアップグレード」が必須ではなくなりました。ユーザーはアップグレードのタイミングを自身で制御できるようになり、運用柔軟性が向上します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/oracle-jvm-spatial-locator-olap-options-amvu-optional/

##### AWS WAF announces automatic SDK integration for Amazon CloudFront distributions

AWS WAFがCloudFront向けに自動SDK統合機能を提供開始しました。これにより、Bot Controlや不正利用防止機能に必要なクライアントサイドのスクリプトタグを自動的にHTMLへ注入でき、設定の簡素化と管理負荷の低減を実現します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/aws-waf-automatic-sdk-integration-amazon-cloudfront/

##### Amazon Connect Customer now supports versioning and aliasing for flows

Amazon Connectにおいて、フローのバージョン管理とエイリアス機能が導入されました。これにより、本番環境のトラフィックに影響を与えずに新しいフローをテストし、エイリアスの切り替えだけで安全にデプロイすることが可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/connect-flows-versioning-aliasing/

##### Managed Prometheus collectors now support Amazon MSK consumer-group metrics

マネージドPrometheusコレクターが、Amazon MSKのコンシューマーグループメトリクスをサポートしました。Kafkaのストリーム健全性やラグをPrometheusやCloudWatchで監視可能になり、ストリーミングアプリケーションのボトルネック特定が容易になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/prometheus-collectors-msk-metrics/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| CloudFrontのWAF設定で自動SDK統合を有効化する | インフラ担当者 | 🔴 高 |
| Amazon Connectのフロー運用にバージョン管理を導入する | コンタクトセンター運用者 | 🟡 中 |
| MSKクラスターのTLSポリシーを1.3へ移行検討する | セキュリティ担当者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon MSK now supports TLS 1.3 | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-tls/ |
| Amazon RDS for Oracle AMVU optional | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/oracle-jvm-spatial-locator-olap-options-amvu-optional/ |
| AWS WAF automatic SDK integration | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/aws-waf-automatic-sdk-integration-amazon-cloudfront/ |
| Amazon Connect flow versioning | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/connect-flows-versioning-aliasing/ |
| Managed Prometheus MSK metrics | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/prometheus-collectors-msk-metrics/ |
| Edit entire presentations with Gemini | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/10/edit-entire-presentations-with-gemini-in-Google-Slides.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWS WAFのCloudFront自動SDK統合により、セキュリティ設定の管理負荷が大幅に軽減されました。

📌 **ピックアップ**
• AWS WAF: CloudFrontでのSDK自動注入により設定漏れを防止
• Google Slides: Geminiによるプレゼン全体の一括編集・スタイル調整が可能に
• Amazon MSK: TLS 1.3サポートとPrometheusでのメトリクス監視が強化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-01*
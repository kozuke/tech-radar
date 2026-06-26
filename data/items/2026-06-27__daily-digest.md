# Tech Radar Daily Digest - 2026-06-27

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、AWS GovCloud (US) において、すべての顧客に対してデフォルトで「米国在住の米国市民による24時間365日の技術サポート」を提供することを発表しました。これまで特別な申請が必要だったサポート体制が標準化されたことで、ITARコンプライアンスや規制要件を重視する政府機関や企業は、より迅速かつ安全に技術的な課題を解決できるようになります。この変更は、クラウドサポートエンジニアが規制環境下で直接作業を行うための権限とツールを即座に利用できることを意味しており、ミッションクリティカルな環境における運用効率とセキュリティが大幅に向上します。

また、Google Workspaceでは、管理者向けに「増分エクスポート（Incremental Exports）」機能が導入されました。これにより、組織全体のデータを毎回再エクスポートする必要がなくなり、直近の変更分のみをGoogle Cloud Storageへ定期的にバックアップ可能となります。バックアップ時間の短縮とストレージコストの削減が実現し、データ損失リスクを最小限に抑えるための高頻度なバックアップ運用が容易になります。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.195

Claude Codeの最新アップデートでは、マウス操作の無効化機能や、ハイフンを含むMCPサーバーの識別子に対する完全一致ルールの導入など、操作性と安定性が向上しました。また、macOSでの音声入力の改善や、Linux環境でのマイク認識の最適化など、開発者の作業環境をサポートする修正が多く含まれています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, MCP (Model Context Protocol) |
| 特徴・性能 | マウス操作制御、音声入力の精度向上、バックアップジョブの安定性改善 |
| 対応環境 | macOS, Linux |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.195

---

### クラウド

#### AWS

##### Amazon EC2 R8g / C8in インスタンスの提供リージョン拡大

AWSは、Graviton4搭載のR8gインスタンスおよび第6世代Intel Xeon搭載のC8inインスタンスの提供リージョンを拡大しました。R8gはメモリ集約型ワークロード向けに最大30%の性能向上を提供し、C8inはネットワーク集約型ワークロード向けに最大600 Gbpsの帯域幅を実現します。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| EC2 R8g | ニュージーランド、タイ、イタリア等で利用可能になり、メモリ負荷の高いDBや分析に適する。 |
| EC2 C8in | 米国オハイオ、アイルランドで利用可能になり、分散コンピューティング等のネットワーク負荷が高い処理に最適。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Graviton4, 第6世代 Intel Xeon Scalable |
| 特徴・性能 | R8g: 最大1.5TBメモリ / C8in: 最大600 Gbpsネットワーク |
| 関連サービス | AWS Nitro System, Amazon EBS |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-r8g-instances-additional-regions/
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-c8in-ireland-ohio/

---

### Workspace

#### Google Workspace

##### Google Workspace Weekly Recap - June 26, 2026

今週のアップデートでは、GeminiによるGoogle Sheetsの数式エラー修正機能や、Safariから直接Google Meetに参加できる機能などが追加されました。また、Google Apps Scriptが正式にコアサービスとなり、エンタープライズレベルのデータ保護が適用されるようになりました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Gemini in Sheets | 数式エラーを分析し、原因の説明と修正案をワンクリックで提供。 |
| Meet (Safari) | iOSデバイスでアプリをインストールせずにブラウザから会議参加が可能。 |
| Apps Script | Google Workspaceのコアサービス化により、エンタープライズ級の保護とサポートを提供。 |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/weekly-recap-06-26-2026.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| AWS GovCloud環境のサポート体制確認 | GovCloud利用者 | 🔴 高 |
| Workspaceの増分エクスポート設定の検討 | Workspace管理者 | 🟡 中 |
| Claude Codeのアップデート適用 | 開発者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EC2 R8g instances... | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-r8g-instances-additional-regions/) |
| Amazon EC2 C8in instances... | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-c8in-ireland-ohio/) |
| Amazon Redshift adds Reserved... | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-redshift-ri-upfront-pricing-rg-instances) |
| AWS GovCloud (US) now offers... | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/default-govcloud-us-based-support/) |
| AWS Backup enhances Amazon S3... | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-backup-amazon-s3-copy-enhancement/) |
| v2.1.195 (Claude Code) | AI/LLM | GitHub | [URL](https://github.com/anthropics/claude-code/releases/tag/v2.1.195) |
| Google Workspace Weekly Recap | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/06/weekly-recap-06-26-2026.html) |
| Streamline your data backups... | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/06/streamline-your-data-backups-for-Google-Workspace.html) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWS GovCloudが米国市民による24/7サポートを標準化し、Google Workspaceがデータバックアップの増分エクスポートに対応しました。

📌 **ピックアップ**
• AWS: EC2 R8g/C8inの提供リージョン拡大とRedshiftの予約インスタンス価格オプション拡充
• AI: Claude Code v2.1.195リリースで操作性と安定性が向上
• Workspace: GeminiによるSheets数式修正やApps Scriptのコアサービス化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-27*
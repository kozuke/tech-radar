# Tech Radar Daily Digest - 2026-09-21

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Amazon Quick（QuickSight）が、自然言語によるシート生成および画像からの分析作成機能を一般公開しました。このアップデートにより、BIダッシュボードの構築プロセスが大幅に効率化されます。ユーザーは自然言語で指示を出すだけで、適切なグラフやフィルタ、計算フィールドを備えたシートを自動生成できるほか、既存のダッシュボード画像から分析を再現することも可能です。

この機能は、BIツール構築における「ゼロからの作成」という手間を省き、既存の資産を再利用・拡張しやすくする点で非常に重要です。特に、他ツールからの移行や、複雑なダッシュボードの迅速なプロトタイピングにおいて、開発者の生産性を大きく向上させることが期待されます。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### Amazon SES now supports tenant-level deliverability insights

Amazon SESのVirtual Deliverability Manager（VDM）が、テナント単位での到達性インサイトに対応しました。これにより、顧客やビジネスユニットごとに送信を分離している環境において、テナントごとの到達率やバウンス率を詳細に監視・分析可能になります。特定のテナントに起因する問題を他への影響なしに特定・修正できるため、大規模なメール配信基盤の運用効率が向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon SES, Virtual Deliverability Manager (VDM) |
| 特徴・性能 | テナント単位のメトリクス可視化、APIによるプログラム的取得 |
| 対応環境 | Amazon SES利用可能な全AWSリージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ses-vdm-tenants/

---

##### Amazon Corretto 27 is now generally available

OpenJDKのディストリビューションであるAmazon Corretto 27が一般公開されました。G1ガベージコレクタのデフォルト化や、TLS 1.3における耐量子ハイブリッド鍵交換の導入など、パフォーマンスとセキュリティの両面で大幅な強化が行われています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| G1 GCのデフォルト化 | 全環境で一貫したパフォーマンスと予測可能な停止時間を実現。 |
| 耐量子TLS 1.3 | 量子コンピュータの脅威に備え、古典的アルゴリズムと耐量子アルゴリズムを組み合わせた鍵交換をサポート。 |
| メモリ効率化 | Compact Object Headersのデフォルト有効化により、Javaオブジェクトのメモリ占有量を削減。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Java (OpenJDK 27) |
| 対応環境 | Linux, Windows, macOS |
| サポート期間 | 2027年4月まで |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-corretto-27-generally-available/

---

##### Amazon ECS deployment observability for Amazon ECS Managed Daemons

Amazon ECSのManaged Daemon向けに、統合されたデプロイメント可視化機能がAWSマネジメントコンソールに追加されました。デプロイの進行状況や失敗要因、ロールバックの経緯を単一の画面で確認できるため、トラブルシューティングの迅速化が期待できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon ECS, AWS Management Console |
| 特徴・性能 | ライフサイクルタイムライン、リソースごとの進捗バー、詳細なエラーログへのリンク |
| 対応環境 | 全AWS商用リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-daemon-deployment-console/

---

##### Amazon Connect Customer can now import evaluation form PDFs using AI

Amazon Connectにおいて、AIを活用してPDF形式の評価フォームを自動的にデジタル化する機能が追加されました。手動でのフォーム再構築が不要となり、既存の品質管理プログラムを迅速にConnectへ移行できるようになります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Connect, 生成AI |
| 特徴・性能 | PDFからの質問・回答・スコアリングの自動抽出、自然言語による微調整 |
| 対応環境 | 東京リージョンを含む主要リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-connect-customer-import-evaluation-form-PDF/

---

### 開発ツール

#### OpenAI Codex CLI

##### OpenAI Codex CLI v0.156.0-alpha.10/11/12

OpenAI Codex CLIのアルファ版リリースが連続して公開されました。現在、詳細な変更ログは確認できませんが、継続的な機能改善とバグ修正が行われているものと推測されます。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| JavaアプリケーションのCorretto 27への移行検証 | Java開発者 | 🟡 中 |
| SESテナント別メトリクスのダッシュボード設定 | メール配信運用担当者 | 🟡 中 |
| ECSデプロイメント画面での監視フロー確認 | インフラエンジニア | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon SES now supports tenant-level deliverability insights | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ses-vdm-tenants/ |
| Amazon Quick now generates individual sheets and builds analyses from an image | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/generate-sheet-and-generate-analysis-from-an-image/ |
| Amazon Corretto 27 is now generally available | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-corretto-27-generally-available/ |
| Amazon ECS deployment observability for Amazon ECS Managed Daemons | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-daemon-deployment-console/ |
| Amazon Connect Customer can now import evaluation form PDFs using AI | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-connect-customer-import-evaluation-form-PDF/ |
| 0.156.0-alpha.12 | OpenAI Codex CLI | openai_codex_cli | https://github.com/openai/codex/releases/tag/rust-v0.156.0-alpha.12 |
| 0.156.0-alpha.11 | OpenAI Codex CLI | openai_codex_cli | https://github.com/openai/codex/releases/tag/rust-v0.156.0-alpha.11 |
| 0.156.0-alpha.10 | OpenAI Codex CLI | openai_codex_cli | https://github.com/openai/codex/releases/tag/rust-v0.156.0-alpha.10 |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon Quickが画像や自然言語からダッシュボードを自動生成する新機能を公開！

📌 **ピックアップ**
• Amazon SES：テナント単位の到達性分析に対応
• Amazon Corretto 27：耐量子TLSやG1 GCデフォルト化でGA
• Amazon ECS：デプロイ可視化機能がコンソールで利用可能に
• Amazon Connect：PDF評価フォームをAIで自動デジタル化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-09-21*
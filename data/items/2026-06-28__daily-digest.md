# Tech Radar Daily Digest - 2026-06-28

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AWSがSQL Server向けセキュリティアップデートを包括的にサポート**
Amazon RDSおよびRDS Custom for SQL Serverにおいて、最新の累積更新プログラム（CU）および一般配布リリース（GDR）のサポートが開始されました。今回のアップデートは、CVE-2026-40370やCVE-2026-32167といった重大な脆弱性に対処するものであり、データベースのセキュリティ強化において極めて重要です。ユーザーはマネジメントコンソールやAWS CLIを通じて迅速にパッチを適用することが推奨されます。

**Devinがコマンドパレットからのセッション管理機能を強化**
AIエンジニアリングツール「Devin」がアップデートされ、コマンドパレット（Cmd+K）から直接セッションのアーカイブ・復元が可能になりました。また、自動化機能における「一度限りの実行」スケジュールの追加や、MCP統合の更新通知機能など、開発者のワークフロー効率を向上させる機能が多数実装されています。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### Amazon RDS Custom now supports the latest CU and GDR updates for Microsoft SQL Server
Amazon RDS Custom for SQL Serverが、最新の累積更新プログラム（CU）および一般配布リリース（GDR）に対応しました。SQL Server 2019および2022の最新バージョンをサポートし、CVE-2026-40370を含む脆弱性への対応が可能となります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon RDS Custom, Microsoft SQL Server |
| 対応バージョン | SQL Server 2019 CU32+GDR, 2022 CU25 |
| 関連サービス | AWS Management Console, AWS SDK/CLI |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-rds-custom-supports-latest-cu-gdr-updates-microsoft-sql-server

---

##### Amazon RDS now supports the latest GDR updates for Microsoft SQL Server
Amazon RDS for SQL Serverが、最新のGDRアップデートに対応しました。SQL Server 2016から2022までの幅広いバージョンを対象とし、CVE-2026-32167およびCVE-2026-32176の脆弱性を修正します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon RDS, Microsoft SQL Server |
| 対応バージョン | SQL Server 2016 SP3, 2017 CU31, 2019 CU32, 2022 CU24 |
| 関連サービス | AWS Management Console, AWS SDK/CLI |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-rds-supports-latest-gdr-updates-microsoft-sql-server

---

##### Amazon OpenSearch Ingestion now available in AWS Europe (Paris) Region
Amazon OpenSearch Ingestionが、欧州（パリ）リージョンで利用可能になりました。これにより、データのフィルタリングや変換、ルーティングをノーコードで処理するフルマネージドなデータ取り込み基盤をパリリージョンで構築できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon OpenSearch Ingestion |
| 対応環境 | AWS Europe (Paris) Region |
| 特徴 | ノーコードでのデータ変換・ルーティング |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/opensearch-ingestion-europe-paris-region-availability

---

##### Amazon Route 53 Global Resolver now supports sharing DNS Views between AWS Accounts
Amazon Route 53 Global Resolverで、AWS RAMを使用したDNSビューの共有が可能になりました。これにより、所有権を移転することなく、複数のAWSアカウント間でプライベートホストゾーンの解決を中央管理できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Route 53 Global Resolver, AWS RAM |
| 機能 | DNSビューのクロスアカウント共有 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-route-53-global-resolver/

---

##### Amazon EC2 High Memory U7in-24TB instances now available in AWS Asia Pacific (Seoul) region
Amazon EC2 High Memory U7in-24TBインスタンスが、アジアパシフィック（ソウル）リージョンで利用可能になりました。第4世代Intel Xeon Scalableプロセッサを搭載し、24 TiBのメモリを備えた本インスタンスは、SAP HANAやSQL ServerなどのミッションクリティカルなDB運用に最適です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon EC2 U7in-24TB |
| 特徴 | 24 TiB DDR5メモリ, 896 vCPUs |
| 対応環境 | AWS Asia Pacific (Seoul) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-u7in-24tb-aws-seoul/

---

### AI/LLM

#### Devin

##### Archive/Unarchive Sessions from Command Palette
Devinの最新アップデートでは、コマンドパレットからのセッション管理や、自動化機能の実行スケジュール設定が追加されました。また、MCP統合の更新通知やUIの改善により、開発体験が向上しています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| セッション管理 | コマンドパレットから直接アーカイブ・復元が可能に。 |
| 自動化スケジュール | 一度限りの実行（Run-once）オプションを追加。 |
| MCP統合 | 更新がある場合にバナーで通知し、ワンクリックで更新可能に。 |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-06-26-archive-unarchive-sessions-from-command-palette

---

#### OpenAI Codex

##### 0.143.0-alpha.27 / 0.143.0-alpha.28
OpenAI Codex CLIのアルファ版リリースが公開されました。詳細な変更ログは現在確認できませんが、継続的な改善が行われています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | OpenAI Codex CLI |
| リリース形式 | Pre-release (alpha) |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.143.0-alpha.28

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| SQL ServerのGDR/CUパッチ適用 | DB管理者 | 🔴 高 |
| Route 53 DNSビュー共有の設計検討 | インフラエンジニア | 🟡 中 |
| Devinの自動化スケジュール機能の確認 | Devinユーザー | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon RDS Custom... | AWS | rss:aws_whats_new | https://aws.amazon.com/... |
| Amazon RDS... | AWS | rss:aws_whats_new | https://aws.amazon.com/... |
| Amazon OpenSearch Ingestion... | AWS | rss:aws_whats_new | https://aws.amazon.com/... |
| Amazon Route 53 Global Resolver... | AWS | rss:aws_whats_new | https://aws.amazon.com/... |
| Amazon EC2 High Memory... | AWS | rss:aws_whats_new | https://aws.amazon.com/... |
| 0.143.0-alpha.28 | OpenAI | rss:openai_codex_cli_releases | https://github.com/... |
| 0.143.0-alpha.27 | OpenAI | rss:openai_codex_cli_releases | https://github.com/... |
| Archive/Unarchive Sessions... | Devin | scrape:devin_release_notes | https://docs.devin.ai/... |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWSのSQL Server向けセキュリティパッチ公開と、Devinのセッション管理機能強化。

📌 **ピックアップ**
• RDS/RDS Customで最新のSQL Server脆弱性修正パッチが利用可能に
• Devinがコマンドパレットからのセッション管理や自動化スケジュールに対応
• EC2 High Memory U7inインスタンスがソウルリージョンで利用可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-28*
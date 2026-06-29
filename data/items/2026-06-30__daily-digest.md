# Tech Radar Daily Digest - 2026-06-30

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**CursorがiOS向けパブリックベータ版をリリース**
AIコードエディタ「Cursor」がiOSアプリを公開し、有料プランユーザー向けに提供を開始しました。最大の特徴は、モバイル端末からクラウド上のAIエージェントを直接操作できる点です。ユーザーは外出先からでもリポジトリを選択し、音声入力やスラッシュコマンドを用いてエージェントに指示を出し、開発環境のテストや検証を行うことが可能です。

また、PCで実行中のエージェントをモバイルから引き継ぐ「リモートコントロール」機能や、ロック画面での進捗確認（Live Activities）、プッシュ通知による完了通知など、モバイル特有のUXが強化されています。これにより、PCを閉じた状態でも開発プロセスを継続できる「常時稼働エージェント」の概念がモバイルへ拡張され、開発者の生産性向上に大きく寄与することが期待されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude / Anthropic
##### Anthropic SDK (Python) v0.113.0 リリース
AnthropicのPython SDKがアップデートされ、2026年3月18日版のWebフェッチ機能およびツール利用へのサポートが追加されました。また、非同期トークンカウント処理におけるバグ修正や、ユーザープロファイルIDの受け入れ対応など、API利用の安定性と柔軟性が向上しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Anthropic Python SDK |
| 特徴・性能 | Webフェッチ対応、トークンカウントの精度向上 |
| 対応環境 | Python環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.113.0

---

#### 開発ツール / AI Agent
##### Cursor for iOS (パブリックベータ)
Cursorのモバイル版がリリースされ、クラウドエージェントの操作、リモートコントロール、Live Activitiesによる進捗監視が可能になりました。PCとモバイル間でのシームレスな開発体験を提供し、外出先からのコードレビューやエージェントへの指示出しを効率化します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Cursor Cloud Agents, iOS |
| 特徴・性能 | 音声入力、リモートコントロール、Live Activities対応 |
| 対応環境 | iOS (有料プランのみ) |

> 🔗 **参考リンク**
> https://cursor.com/changelog#2026-06-29-cursor-for-ios

---

### クラウド

#### AWS
##### AWS WAFがAmazon Bedrock AgentCore Gatewayをサポート
AWS WAFがAmazon Bedrock AgentCore Gatewayに対応し、エージェント型AIワークロードに対する保護が可能になりました。IPベースのアクセス制御やレート制限、Bot制御などをゲートウェイ層で一元管理でき、本番環境におけるAIアプリケーションのセキュリティが強化されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS WAF, Amazon Bedrock AgentCore |
| 特徴・性能 | ゲートウェイ層での一元的なセキュリティ適用 |
| 対応環境 | AWS全リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/aws-waf-amazon-bedrock-agentcore/

##### Amazon MWAA Serverlessが共有VPCをサポート
Amazon MWAA Serverlessが共有VPCサブネットに対応しました。これにより、AWS RAMを利用したマルチアカウント環境において、ネットワーク管理者が一元管理する共有サブネット上でAirflowワークフローを直接起動できるようになり、回避策なしでの運用が可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/

##### Amazon S3サーバーアクセスログの配信先拡大
S3のサーバーアクセスログがAmazon CloudWatch LogsおよびAmazon S3 Tables（Apache Iceberg形式）へ直接配信可能になりました。これにより、CloudWatchでの即時クエリやアラート設定、AthenaやRedshiftを用いたSQLによる高度なログ分析が容易になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-s3-cloudwatch-logs-tables/

---

### Workspace

#### Google Workspace
##### Geminiアプリのデータリージョン対応
Geminiアプリが組織のデータリージョン要件に準拠するようになりました。管理者はEUや米国など、データの保存・処理場所を組織単位（OU）で指定でき、データ主権やコンプライアンス要件を満たしながらGeminiを組織全体で安全に導入可能です。

##### Google ClassroomへのGemini Canvas共有
教育機関向けに、Gemini Canvasで作成したコンテンツ（Webサイト、クイズ、インタラクティブ教材など）を直接Google Classroomへ共有する機能が追加されました。教師と生徒間のコラボレーションが円滑化され、より動的な学習環境の構築を支援します。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/gemini-app-data-regions-support.html
> http://workspaceupdates.googleblog.com/2026/06/educators-and-students-can-now-share-Gemini-Canvas-creations-directly-to-Google-Classroom.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Cursor iOS版の導入検討と設定 | 開発者 | 🟡 中 |
| Bedrock AgentCore GatewayへのWAF適用 | セキュリティ担当 | 🔴 高 |
| Geminiアプリのデータリージョン設定確認 | 管理者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS WAF adds support for Amazon Bedrock AgentCore Gateway | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/aws-waf-amazon-bedrock-agentcore/ |
| Amazon MWAA Serverless now supports shared VPC configurations | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/ |
| Amazon S3 server access logs now deliver to Amazon CloudWatch Logs | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-s3-cloudwatch-logs-tables/ |
| Cursor for iOS | 開発ツール | Cursor | https://cursor.com/changelog#2026-06-29-cursor-for-ios |
| v0.113.0 (Anthropic SDK) | AI/LLM | Anthropic | https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.113.0 |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
CursorがiOSアプリを公開！モバイルからクラウドAIエージェントを直接操作可能に。

📌 **ピックアップ**
• AWS WAFがBedrock AgentCore Gatewayに対応し、AIワークロードの保護を強化
• S3サーバーアクセスログがCloudWatch LogsとS3 Tablesへ直接配信可能に
• Geminiアプリが組織のデータリージョン要件に準拠し、管理者が保存場所を指定可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-30*
# Tech Radar Daily Digest - 2026-11-25

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Google Cloudの「Agent Retrieval」に、マネージドなデータ取り込み（Managed Ingestion）と検索機能（SearchDocuments）がパブリックプレビューとして追加されました。これまでPDFや動画などの非構造化データをAIエージェントで扱うには、パース、チャンク分割、埋め込み、ベクトルDBへの保存といった複雑なパイプラインを自前で構築する必要がありましたが、本機能によりCloud Storage上のファイルを指定するだけで、これらの処理が自動化されます。特に動画検索において、視覚情報と音声の両方を対象とした検索が1つのAPIコールで完結し、根拠となるタイムスタンプ付きの引用が可能になる点は、AIエージェント開発の生産性を劇的に向上させるでしょう。

また、AWS CloudFormationが206の新しいリソースタイプをサポートし、SageMaker HubやBedrock AgentCore PolicyEngineなど、これまでカバーしきれていなかった領域のインフラ管理が標準化されました。AI駆動の内部フレームワークを活用したこのアップデートにより、今後も迅速なリソース対応が期待されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.332

Claude Codeの最新版では、MCPサーバーからのスキル呼び出し機能がベータ版として追加され、より柔軟なツール連携が可能になりました。また、認証エラーの改善や、大規模なログ出力時のフリーズ対策など、開発体験を損なう多くの不具合が修正されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| MCPスキル連携 | MCPサーバーで定義されたスキルを `/` メニューから呼び出し可能に。 |
| PreSkillShellCommand | スキルやコマンドの実行前に、インラインシェルコマンドを拒否できるフックを追加。 |
| セッション管理 | セッション保存失敗時の通知強化や、`/compact` による保存手順の明示化。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, MCP (Model Context Protocol) |
| 特徴・性能 | 大規模ログのメモリ消費抑制、SSE MCPサーバーの接続安定性向上 |
| 対応環境 | VS Code, デスクトップ環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.332

---

#### Gemini

##### From Files to Cited Answers in One API Call

GeminiのAgent Retrieval機能が強化され、ドキュメントや動画のインジェストから検索までをフルマネージドで実行可能になりました。Gemini Embedding 2を活用し、解析から埋め込みまでを自動化することで、開発者はパイプライン構築の工数を大幅に削減できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Gemini Embedding 2, Agent Retrieval |
| 特徴・性能 | PDF/動画の自動パース・チャンク化、引用元（ページ/タイムスタンプ）の提示 |
| 関連サービス | Google Cloud Storage |

> 🔗 **参考リンク**
> https://developers.googleblog.com/from-files-to-cited-answers-in-one-api-call-managed-ingestion-and-searchdocuments-in-agent-retrieval/

---

#### Anthropic SDK

##### v2.14.0

Python SDKの最新版では、Google Cloudプロジェクト向けのデータ制御機能や、コンプライアンス関連のサポートが追加されました。また、HTTPプロキシ設定の挙動が標準的な `httpx` ライブラリの仕様に準拠するよう修正され、より予測可能なネットワーク接続が可能になっています。

> 🔗 **参考リンク**
> https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.14.0

---

### クラウド

#### AWS

##### Amazon Bedrock: Daybreak RedのGovCloud対応

OpenAIのサイバーセキュリティ特化モデル「Daybreak Red (GPT-5.6 Cyber)」が、AWS GovCloud (US) のAmazon Bedrockで利用可能になりました。脆弱性研究やエクスプロイト再現などの高度なタスク向けに最適化されており、厳格なアクセス制御下での運用が可能です。

##### Amazon OpenSearch Serverless: Cape Townリージョン対応

OpenSearch Serverlessがアフリカ（ケープタウン）リージョンで利用可能になりました。サーバーレス化により、エージェントAIや検索ワークロードの運用負荷を軽減し、トラフィックに応じた自動スケーリングとコスト最適化を実現します。

##### AWS CloudFormation: 206の新リソースタイプ追加

CloudFormationの対応リソースが大幅に拡大され、SageMaker HubやEC2 Snapshotなど88サービスで計206タイプが追加されました。AI駆動のフレームワーク導入により、今後も継続的なカバレッジ向上が見込まれます。

##### Amazon Connect: ダッシュボードの時系列グループ化

コンタクトセンターの分析ダッシュボードにおいて、履歴メトリクスを時間間隔（15分、1時間、日次など）でグループ化できるようになりました。これにより、スパイク発生時の詳細な原因分析が容易になります。

##### Amazon RDS for SQL Server: 1インスタンスあたり500DBへ拡大

RDS for SQL Serverの1インスタンスあたりのデータベース上限が100から500に引き上げられました。SaaSプロバイダーやマルチテナントアプリケーションにおいて、インスタンス集約によるコスト削減と管理効率化が期待できます。

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude CodeのアップデートとMCPスキルの試用 | 開発者 | 🟡 中 |
| Agent Retrievalのマネージドインジェスト検証 | AIエンジニア | 🔴 高 |
| RDS SQL ServerのDB集約によるコスト試算 | インフラ管理者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Bedrock adds bedrock-runtime endpoint... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/gpt-daybreak-red-runtime-govcloud/ |
| Amazon OpenSearch Serverless is now available... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-serverless-available-cape-town-region/ |
| AWS CloudFormation makes resource coverage... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/cloudformation-coverage-expansion/ |
| Amazon Connect Customer dashboards... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-connect-time-interval/ |
| Amazon RDS for SQL Server now supports... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/rds-sqlserver-supports-500-databases-per-instance |
| v2.1.332 | Claude Code | claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.332 |
| 0.174.0-alpha.5 | OpenAI | openai_codex_cli_releases | https://github.com/openai/codex/releases/tag/rust-v0.174.0-alpha.5 |
| 0.174.0-alpha.4 | OpenAI | openai_codex_cli_releases | https://github.com/openai/codex/releases/tag/rust-v0.174.0-alpha.4 |
| 0.174.0-alpha.3 | OpenAI | openai_codex_cli_releases | https://github.com/openai/codex/releases/tag/rust-v0.174.0-alpha.3 |
| 0.174.0-alpha.2 | OpenAI | openai_codex_cli_releases | https://github.com/openai/codex/releases/tag/rust-v0.174.0-alpha.2 |
| From Files to Cited Answers in One API Call... | Gemini | google_developers | https://developers.googleblog.com/from-files-to-cited-answers-in-one-api-call-managed-ingestion-and-searchdocuments-in-agent-retrieval/ |
| v2.14.0 | Anthropic | anthropic_sdk_releases | https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.14.0 |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Google Cloudの「Agent Retrieval」が進化し、ファイルから検索までを1つのAPIで完結するマネージド機能がパブリックプレビューに。

📌 **ピックアップ**
• AWS CloudFormationが206のリソースタイプを新規サポート
• Claude CodeがMCPスキル連携に対応し、開発体験が向上
• RDS for SQL Serverが1インスタンスあたり500DBまで対応可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-25*
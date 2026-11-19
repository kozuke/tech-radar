# Tech Radar Daily Digest - 2026-11-19

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、AIエージェントに永続的な記憶機能を提供するサーバーレス機能「Amazon OpenSearch Memory」の一般提供を開始しました。この機能は、エージェントの会話履歴やユーザーの好みを自動的に抽出し、構造化して保存・検索可能にするもので、開発者はインフラのプロビジョニングや複雑な検索システムの構築なしに、コンテキストを保持した高度なAIエージェントを構築できます。

また、Google Workspaceでは、Google Docsにおけるキャプションや相互参照機能の強化、Google Calendarでの時間帯表示の改善や会議バッファ設定の柔軟化など、生産性を高めるアップデートが多数発表されました。特にAIエージェント開発と業務効率化の両面で、ツールがより自律的かつインテリジェントに進化している点が注目されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.328

Claude Codeの最新版では、Amazon BedrockやGoogle CloudのAgent Platformなど主要なプラットフォーム上でClaude Opus 4.6およびSonnet 4.6の「自動モード」が利用可能になりました。また、セキュリティや開発体験を向上させるためのフック機能の強化や、自己ホスト型ランナー向けのメトリクス追加が行われています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Opus 4.6, Sonnet 4.6, OpenTelemetry |
| 特徴・性能 | 自動モード対応、フック失敗時のブロック機能追加 |
| 対応環境 | Amazon Bedrock, Google Cloud, Microsoft Foundry |
| 関連サービス | Claude apps gateway |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.328

---

#### OpenAI Codex

##### 0.172.0-alpha.1 / 0.171.0-alpha.13

OpenAIのCodex CLIツールにおいて、アルファ版のアップデートが連続してリリースされました。主に内部的なコードベースの改善やバグ修正が含まれており、開発環境の安定化に向けた調整が進められています。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.172.0-alpha.1

---

### クラウド

#### AWS

##### Amazon OpenSearch Memory is now generally available

Amazon OpenSearch Serviceに、AIエージェント向けの永続的メモリ機能が追加されました。会話履歴を自動的にインデックス化し、セッションをまたいで文脈を保持することで、エージェントの意思決定精度を向上させます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-memory-generally-available/

##### Introducing the Apache Spark Optimization Agent for AWS Glue ETL

AWS Glue ETL向けに、Sparkジョブのコストとパフォーマンスを最適化するエージェントが導入されました。過去の実行ログを分析し、メモリ不足や並列度の最適化など、具体的な改善案を自動的に提示します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-aws-glue-etl/

##### Amazon SageMaker AI now supports cross-Region inference routing

SageMaker AIにおいて、リージョン間での推論ルーティングがサポートされました。特定リージョンの容量不足や障害時に、自動的に別リージョンのエンドポイントへリクエストを転送することで、推論アプリケーションの可用性を高めます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-cross-region-routing/

##### AWS announces ExtendDB 1.0

DynamoDB APIと互換性を持つオープンソースアダプター「ExtendDB 1.0」がリリースされました。PostgreSQLやMongoDBなどをバックエンドとして利用可能で、オンプレミスやエッジ環境でのDynamoDBワークロード実行を容易にします。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/aws-extenddb-1-0/

##### AWS Transform custom now supports cross-account sharing

AWS Transformの変換定義（TD）を、AWS RAMを介して組織全体や別アカウントと共有可能になりました。プラットフォームエンジニアリングチームが標準化された変換ルールを一元管理し、効率的に展開できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/aws-custom-cross-account-td/

---

### Workspace

#### Google Workspace

##### Google Docsの機能強化

Google Docsでインラインキャプション、相互参照、キャプション一覧の自動生成が可能になりました。これにより、複雑な文書作成時の図表管理や番号付けが自動化され、Microsoft Wordとの互換性も維持されます。

##### Gemini Notebookのサイト生成機能

Gemini Notebookで、ノートや研究資料からインタラクティブなサイトを生成できるようになりました。「make me a site」と入力するだけで、視覚的な説明資料やプロジェクトトラッカーを作成可能です。

##### Google Chatアプリのスタータープロンプト

Google ChatアプリやAIエージェントに、ユーザー向けのスタータープロンプトと説明文を設定可能になりました。ユーザーは初回利用時にアプリの機能を即座に理解し、対話を開始できます。

##### Google Calendarの表示・設定改善

Google Calendarで時間帯の略称表示（ET, PT等）が導入され、時差のある会議調整が容易になりました。また、会議の開始を5分遅らせる、または終了を5分早めるバッファ設定がカレンダー単位で可能になりました。

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| AIエージェントのコンテキスト保持機能の検証 | AI開発者 | 🔴 高 |
| AWS Glueジョブの最適化推奨事項の確認 | データエンジニア | 🟡 中 |
| Google Calendarのバッファ設定の最適化 | 全ユーザー | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon OpenSearch Memory is now generally available | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-memory-generally-available/ |
| Introducing the Apache Spark Optimization Agent for AWS Glue ETL | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-aws-glue-etl/ |
| Amazon SageMaker AI now supports cross-Region inference routing | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-cross-region-routing/ |
| AWS announces ExtendDB 1.0 | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/aws-extenddb-1-0/ |
| AWS Transform custom now supports cross-account sharing | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/aws-custom-cross-account-td/ |
| v2.1.328 | Claude Code | claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.328 |
| 0.172.0-alpha.1 | Codex | openai_codex_cli_releases | https://github.com/openai/codex/releases/tag/rust-v0.172.0-alpha.1 |
| 0.171.0-alpha.13 | Codex | openai_codex_cli_releases | https://github.com/openai/codex/releases/tag/rust-v0.171.0-alpha.13 |
| Add inline captions, cross-references, and tables of captions in Google Docs | Workspace | google_workspace_updates | http://workspaceupdates.googleblog.com/2026/11/add-inline-captions-cross-references-and-tables-of-captions-in-Google-Docs.html |
| Transform your notes and research into dynamic tools with Gemini Notebook | Workspace | google_workspace_updates | http://workspaceupdates.googleblog.com/2026/11/transform-your-notes-and-research-into-dynamic-tools-with-Gemini-Notebook.html |
| Starter prompts and descriptions for Google Chat apps and agents | Workspace | google_workspace_updates | http://workspaceupdates.googleblog.com/2026/11/starter-prompts-and-descriptions-for-Google-Chat-apps-and-agents.html |
| Schedule more easily across time zones with time zone abbreviations in Google Calendar | Workspace | google_workspace_updates | http://workspaceupdates.googleblog.com/2026/11/schedule-more-easily-across-time-zones-with-time-zone-abbreviations-in-Google-Calendar-on-the-web.html |
| Schedule meetings with a default 5-minute buffer in Google Calendar | Workspace | google_workspace_updates | http://workspaceupdates.googleblog.com/2026/11/schedule-meetings-with-default-buffer-google-calendar.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWSがAIエージェント向け永続メモリ機能「Amazon OpenSearch Memory」を一般提供開始。

📌 **ピックアップ**
• AWS GlueにSpark最適化エージェントが登場、コストと性能を自動改善。
• SageMaker AIがリージョン間推論ルーティングに対応し可用性が向上。
• Google Docs/Calendarに生産性を高める新機能が多数追加。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-19*
# Tech Radar Daily Digest - 2026-06-14

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSはAmazon Bedrockにおいて、OpenAIの最新モデル「GPT-5.4」および「GPT-5.5」の提供リージョンを拡大し、米国東部（バージニア北部）で利用可能にしました。GPT-5.5は、複雑な推論やエージェントタスク、高度なコーディング能力を備えた最上位モデルであり、GPT-5.4は長文コンテキストやツール利用に最適化されています。両モデルとも272Kトークンのコンテキストウィンドウをサポートしており、企業はAWSのセキュアな環境下で、より高度な自律型AIエージェントやドキュメントワークフローを構築できるようになります。

また、AWSは「AWS Workload Credentials Provider」を公開しました。これはACM証明書やSecrets Managerのシークレットを、AWS内外のワークロードに対して自動的に配布・キャッシュする軽量なクライアントツールです。証明書の更新やシークレット管理の複雑さを解消し、運用負荷を大幅に軽減するもので、特にセキュリティ要件の厳しい環境での自動化を強力にサポートします。

---

## 📰 今日のニュース

### AI/LLM

#### OpenAI / Claude / Devin

##### OpenAI GPT-5.4 and GPT-5.5 models now available in US East (N. Virginia) on Amazon Bedrock

OpenAIの最先端モデルであるGPT-5.4およびGPT-5.5が、Amazon Bedrockの米国東部（バージニア北部）リージョンで利用可能になりました。これらのモデルは、高度な推論、コーディング、エージェントによる長期実行タスクの遂行に特化しており、企業アプリケーションのAI機能を大幅に強化します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | GPT-5.4, GPT-5.5 |
| 特徴・性能 | 272Kトークンのコンテキストウィンドウ、マルチモーダル入力対応 |
| 対応環境 | Amazon Bedrock (US East N. Virginia) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/openai-gpt-us-east-virginia-amazon/

---

##### v2.1.177 (Claude Code)

Claude Codeの最新バージョンv2.1.177がリリースされました。今回のアップデートでは主にCHANGELOGの更新やフィードの修正といったメンテナンス作業が行われています。

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.177

---

##### 0.140.0-alpha.18 / 0.140.0-alpha.17 (Codex CLI)

OpenAI Codex CLIのアルファ版が連続してリリースされました。開発環境におけるCLIツールの安定性向上や、内部的なコードベースの改善が進められています。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.140.0-alpha.18

---

##### Session Folders (Devin)

AIエンジニアDevinにおいて、セッションの整理機能やSlack経由のモデル切り替え機能が追加されました。ユーザーはセッションをフォルダ分けして管理できるほか、Slack上で「!ultra」「!fast」コマンドを使用して実行中にモデルを切り替えることが可能になりました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Session Folders | サイドバーでセッションをフォルダ分けして管理可能に。 |
| Mid-Session Toggles | Slackコマンドで実行中にモデル（Ultra/Fast）を切り替え可能に。 |
| Custom OAuth | Marketplace MCPサーバーで組織固有のOAuth設定が可能に。 |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-06-12-session-folders

---

### クラウド

#### AWS

##### Amazon Quick now integrates with Snowflake Cortex AI

Amazon QuickがSnowflake Cortex AIとMCP（Model Context Protocol）を通じて統合されました。これにより、自然言語を使用してSnowflake上の構造化データや非構造化ドキュメントをクエリし、自動化されたワークフローを構築することが可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | MCP (Model Context Protocol), Snowflake Cortex AI |
| 特徴・性能 | 自然言語によるデータ分析、マルチステップワークフローの自動化 |
| 関連サービス | Snowflake, Amazon Quick |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-quick-snowflake-cortex-ai/

---

##### Amazon EKS now supports local clusters on AWS Outposts with Amazon EC2 instance store

Amazon EKSのローカルクラスターが、EC2インスタンスストアで起動するAWS Outpostsラックをサポートしました。これにより、クラウドとのネットワーク切断時にも高い可用性を維持しつつ、データレジデンシー要件を満たすKubernetes環境の構築が可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-aws-outposts-ec2-instance-store/

---

##### AWS Lake Formation extends table permissions to access underlying data in Amazon S3

AWS Lake Formationが、Glue Data Catalogのテーブル権限をS3上の直接的なファイルアクセスにまで拡張しました。これにより、SQLクエリとSparkジョブ等でのファイルアクセスに対して、単一の権限管理体系を適用できるようになります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lake-formation-access-data-amazon-s3

---

##### AWS announces AWS Workload Credentials Provider

AWSは、ACM証明書とSecrets Managerのシークレットを自動配布・キャッシュする「AWS Workload Credentials Provider」を発表しました。オープンソースのクライアントツールとして、AWS内外のワークロードにおける証明書更新やシークレット管理を自動化します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/aws-workload-credentials-provider/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| BedrockでGPT-5.5の検証を開始する | AI開発者 | 🔴 高 |
| AWS Workload Credentials Providerの導入検討 | インフラエンジニア | 🟡 中 |
| Devinのセッション整理とSlackコマンドの活用 | Devinユーザー | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Quick now integrates with Snowflake Cortex AI | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-quick-snowflake-cortex-ai/ |
| Amazon EKS now supports local clusters on AWS Outposts... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-aws-outposts-ec2-instance-store/ |
| AWS Lake Formation extends table permissions... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lake-formation-access-data-amazon-s3 |
| AWS announces AWS Workload Credentials Provider | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/aws-workload-credentials-provider/ |
| OpenAI GPT-5.4 and GPT-5.5 models now available... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/openai-gpt-us-east-virginia-amazon/ |
| v2.1.177 | AI/LLM | claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.177 |
| 0.140.0-alpha.18 | AI/LLM | openai_codex_cli_releases | https://github.com/openai/codex/releases/tag/rust-v0.140.0-alpha.18 |
| 0.140.0-alpha.17 | AI/LLM | openai_codex_cli_releases | https://github.com/openai/codex/releases/tag/rust-v0.140.0-alpha.17 |
| Session Folders | AI/LLM | devin_release_notes | https://docs.devin.ai/release-notes/overview#2026-06-12-session-folders |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon BedrockでOpenAIの最新モデル「GPT-5.5」が利用可能に！

📌 **ピックアップ**
• GPT-5.4/5.5がBedrock（バージニア北部）で利用開始
• AWS Workload Credentials Providerで証明書・シークレット管理を自動化
• Amazon QuickがSnowflake Cortex AIと統合、自然言語分析が強化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-14*
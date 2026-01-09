```markdown
# Tech Radar Daily Digest - 2026-01-09

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

1. **AnthropicがClaude Codeのサードパーティ利用をブロック**: GitHubのOpenCodeプロジェクトで、Claude Maxの利用が停止。AnthropicがAPIキーの共有を制限した可能性があり、OpenCodeのようなサードパーティ製クライアントに影響が出ています。

2. **Gemini 3 FlashがGemini CLIで利用可能に**: GoogleのGemini 3 FlashがGemini CLIで利用可能になり、ターミナルベースの作業における高頻度ワークフローをサポートします。Gemini 3 Flashは、エージェントコーディングにおいて78%のSWE-bench Verifiedスコアを達成し、Gemini 3 Proを上回る性能を発揮します。

---

## 📰 今日のニュース

### 💽 データベース

#### Introducing pgpm: A Package Manager for Modular PostgreSQL
- **要点**: PostgreSQLのアプリケーションレベルのロジックを共有・再利用するためのパッケージマネージャpgpmが発表されました。スキーマ、テーブル、関数などをモジュール化し、バージョン管理された単位として配布できます。
- **技術ポイント**: アプリケーションレイヤーでのモジュール化、依存関係管理、バージョン管理された配布
- **リンク**: https://www.postgresql.org/about/news/introducing-pgpm-a-package-manager-for-modular-postgresql-3196/

#### Welcoming three new members to the PostgreSQL Community Code of Conduct Committee
- **要点**: PostgreSQLコミュニティ行動規範委員会に3人の新メンバーが加わりました。DevOps、ソフトウェアパッケージング、機械学習、人事、エンタープライズPostgreSQLの専門家が参加し、コミュニティの安全性と包括性を向上させます。
- **技術ポイント**: コミュニティ管理、行動規範、多様性
- **リンク**: https://www.postgresql.org/about/news/welcoming-three-new-members-to-the-postgresql-community-code-of-conduct-committee-3209/

#### PGConf India 2026: Talks, trainings published and early bird registration closes soon
- **要点**: PGConf India 2026の講演とトレーニングが公開され、早期割引登録が間もなく終了します。
- **技術ポイント**: PostgreSQL, カンファレンス
- **リンク**: https://www.postgresql.org/about/news/pgconf-india-2026-talks-trainings-published-and-early-bird-registration-closes-soon-3208/

### ☁️ クラウド

#### Happy New Year! AWS Weekly Roundup: 10,000 AIdeas Competition, Amazon EC2, Amazon ECS Managed Instances and more (January 5, 2026)
- **要点**: AWSの週刊まとめ。10,000 AIdeasコンペティション、Amazon EC2 M8gn/M8gbインスタンス、AWS Direct Connectのレジリエンス・テスト、AWS Control Towerの新しいSecurity Hubコントロールなどが紹介されています。
- **技術ポイント**: AWS Graviton4, AWS Fault Injection Service, AWS Security Hub
- **リンク**: https://aws.amazon.com/blogs/aws/happy-new-year-aws-weekly-roundup-10000-aideas-competition-amazon-ec2-amazon-ecs-managed-instances-and-more-january-5-2026/

#### AWS Weekly Roundup: Amazon ECS, Amazon CloudWatch, Amazon Cognito and more (December 15, 2025)
- **要点**: AWSの週刊まとめ。Amazon WorkSpaces Secure BrowserのWebコンテンツフィルタリング、Amazon Aurora DSQLの高速クラスタ作成、Kiro powersとの統合、Amazon ECSのカスタムコンテナ停止シグナルなどが紹介されています。
- **技術ポイント**: Amazon WorkSpaces, Amazon Aurora, Amazon ECS
- **リンク**: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-ecs-amazon-cloudwatch-amazon-cognito-and-more-december-15-2025/

#### AWS Weekly Roundup: AWS re:Invent keynote recap, on-demand videos, and more (December 8, 2025)
- **要点**: AWS re:Invent 2025のキーノートのまとめ。AIエージェント、開発者の役割、AWSの主要な属性（セキュリティ、可用性、パフォーマンスなど）が強調されています。
- **技術ポイント**: AIエージェント, クラウドインフラ
- **リンク**: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-reinvent-keynote-recap-on-demand-videos-and-more-december-8-2025/

### 🤖 AI/LLM

#### Real-World Agent Examples with Gemini 3
- **要点**: Gemini 3を活用したエージェントの実際の例が紹介されています。ADK、Agno、Browser Use、Eigentなどのオープンソースフレームワークとの連携を通じて、小売戦略、マルチエージェントシステム、ブラウザ自動化などのタスクを実行します。
- **技術ポイント**: Gemini 3, エージェント, 自動化
- **リンク**: https://developers.googleblog.com/real-world-agent-examples-with-gemini-3/

#### Gemini 3 Flash is now available in Gemini CLI
- **要点**: Gemini 3 FlashがGemini CLIで利用可能になり、ターミナルベースの作業における高頻度ワークフローをサポートします。Gemini 3 Flashは、エージェントコーディングにおいて78%のSWE-bench Verifiedスコアを達成し、Gemini 3 Proを上回る性能を発揮します。
- **技術ポイント**: Gemini 3, Gemini CLI, エージェントコーディング
- **リンク**: https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/

### 🛠️ DevOps

#### Why AI is pushing developers toward typed languages
- **要点**: AIの進化により、開発者が型付き言語を使用する傾向が強まっています。
- **技術ポイント**: 型付き言語, 開発
- **リンク**: https://github.blog/ai-and-ml/llms/why-ai-is-pushing-developers-toward-typed-languages/

#### Agentic AI, MCP, and spec-driven development: Top blog posts of 2025
- **要点**: 2025年のGitHubブログの人気記事を紹介。Agentic AI, MCP, spec-driven developmentなどが取り上げられています。
- **技術ポイント**: Agentic AI, MCP, spec-driven development
- **リンク**: https://github.blog/developer-skills/agentic-ai-mcp-and-spec-driven-development-top-blog-posts-of-2025/

#### WRAP up your backlog with GitHub Copilot coding agent
- **要点**: GitHub Copilotコーディングエージェントを使用してバックログを整理する方法を紹介。
- **技術ポイント**: GitHub Copilot, コーディングエージェント
- **リンク**: https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/

### ⚙️ その他

#### Why I left iNaturalist
- **要点**: iNaturalistの共同創設者が、現在のリーダーシップチームの方向性とスタッフ管理に不満を感じて退職した理由を説明しています。
- **技術ポイント**: コミュニティ, 組織
- **リンク**: https://kueda.net/blog/2026/01/06/why-i-left-inat/

#### Embassy: Modern embedded framework, using Rust and async
- **要点**: Rustとasyncを使用した最新の組み込みフレームワークEmbassyを紹介。安全で効率的な組み込みコードをより速く記述できます。
- **技術ポイント**: Rust, async, 組み込み開発
- **リンク**: https://github.com/embassy-rs/embassy

#### A Developer's Guide to Debugging JAX on Cloud TPUs: Essential Tools and Techniques
- **要点**: Cloud TPU上のJAXをデバッグするためのガイド。ログ、ハードウェアメトリクス、プロファイリングなどのツールとテクニックを紹介します。
- **技術ポイント**: JAX, Cloud TPU, デバッグ
- **リンク**: https://developers.googleblog.com/a-developers-guide-to-debugging-jax-on-cloud-tpus-essential-tools-and-techniques/

---

## 💡 今日のアクションポイント

- PostgreSQLのアプリケーション開発者は、pgpmを試して、データベースロジックの再利用性を向上させることを検討する。
- AWSを利用している場合は、新しいEC2インスタンスやDirect Connectのレジリエンス・テスト機能を活用して、パフォーマンスと信頼性を向上させる。
- Gemini 3 FlashをGemini CLIで試して、ターミナルでのコーディング効率を向上させる。
- JAX on Cloud TPUsを使用している場合は、紹介されているデバッグツールとテクニックを活用して、ワークフローのトラブルシューティングを行う。
- GitHub Copilotコーディングエージェントを使用してバックログを整理し、開発効率を向上させる。

---

## 📚 元記事一覧

| タイトル | ソース | URL |
|---------|--------|-----|
| Introducing pgpm: A Package Manager for Modular PostgreSQL | rss:postgres_blog | https://www.postgresql.org/about/news/introducing-pgpm-a-package-manager-for-modular-postgresql-3196/ |
| Welcoming three new members to the PostgreSQL Community Code of Conduct Committee | rss:postgres_blog | https://www.postgresql.org/about/news/welcoming-three-new-members-to-the-postgresql-community-code-of-conduct-committee-3209/ |
| PGConf India 2026: Talks, trainings published and early bird registration closes soon | rss:postgres_blog | https://www.postgresql.org/about/news/pgconf-india-2026-talks-trainings-published-and-early-bird-registration-closes-soon-3208/ |
| Anthropic blocks third-party use of Claude Code subscriptions | rss:hacker_news | https://github.com/anomalyco/opencode/issues/7410 |
| Why I left iNaturalist | rss:hacker_news | https://kueda.net/blog/2026/01/06/why-i-left-inat/ |
| Embassy: Modern embedded framework, using Rust and async | rss:hacker_news | https://github.com/embassy-rs/embassy |
| Happy New Year! AWS Weekly Roundup: 10,000 AIdeas Competition, Amazon EC2, Amazon ECS Managed Instances and more (January 5, 2026) | rss:aws_blog | https://aws.amazon.com/blogs/aws/happy-new-year-aws-weekly-roundup-10000-aideas-competition-amazon-ec2-amazon-ecs-managed-instances-and-more-january-5-2026/ |
| AWS Weekly Roundup: Amazon ECS, Amazon CloudWatch, Amazon Cognito and more (December 15, 2025) | rss:aws_blog | https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-ecs-amazon-cloudwatch-amazon-cognito-and-more-december-15-2025/ |
| AWS Weekly Roundup: AWS re:Invent keynote recap, on-demand videos, and more (December 8, 2025) | rss:aws_blog | https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-reinvent-keynote-recap-on-demand-videos-and-more-december-8-2025/ |
| Why AI is pushing developers toward typed languages | rss:github_blog | https://github.blog/ai-and-ml/llms/why-ai-is-pushing-developers-toward-typed-languages/ |
| Agentic AI, MCP, and spec-driven development: Top blog posts of 2025 | rss:github_blog | https://github.blog/developer-skills/agentic-ai-mcp-and-spec-driven-development-top-blog-posts-of-2025/ |
| WRAP up your backlog with GitHub Copilot coding agent | rss:github_blog | https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/ |
| A Developer's Guide to Debugging JAX on Cloud TPUs: Essential Tools and Techniques | rss:google_developers | https://developers.googleblog.com/a-developers-guide-to-debugging-jax-on-cloud-tpus-essential-tools-and-techniques/ |
| Real-World Agent Examples with Gemini 3 | rss:google_developers | https://developers.googleblog.com/real-world-agent-examples-with-gemini-3/ |
| Gemini 3 Flash is now available in Gemini CLI | rss:google_developers | https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/ |

---

*生成日: 2026-01-09*
```
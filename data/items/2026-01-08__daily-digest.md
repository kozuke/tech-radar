```markdown
# Tech Radar Daily Digest - 2026-01-08

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

### PostgreSQLのモジュール型パッケージマネージャ「pgpm」登場
PostgreSQLのアプリケーションレベルのコードをモジュール化し、依存関係管理とバージョン管理された配布を可能にする「pgpm」が登場しました。これにより、開発者はデータベースロジックを再利用可能なコンポーネントとしてパッケージ化、テスト、配布できるようになります。これまでPostgreSQL拡張機能はシステムレベルの機能のパッケージ化に使用されてきましたが、pgpmはアプリケーション層でのSQL共有を容易にすることを目指しています。

---

## 📰 今日のニュース

### データベース

#### Introducing pgpm: A Package Manager for Modular PostgreSQL
- **要点**: PostgreSQLのアプリケーションレベルのコードをモジュール化し、依存関係管理とバージョン管理された配布を可能にする「pgpm」が登場。
- **技術ポイント**: アプリケーション層でのSQL共有、モジュール型パッケージング、依存関係管理、バージョン管理された配布。
- **リンク**: https://www.postgresql.org/about/news/introducing-pgpm-a-package-manager-for-modular-postgresql-3196/

#### Welcoming three new members to the PostgreSQL Community Code of Conduct Committee
- **要点**: PostgreSQLコミュニティ行動規範委員会に3人の新メンバーが加わりました。
- **技術ポイント**: コミュニティの多様性と包括性を促進するための取り組み。
- **リンク**: https://www.postgresql.org/about/news/welcoming-three-new-members-to-the-postgresql-community-code-of-conduct-committee-3209/

#### PGConf India 2026: Talks, trainings published and early bird registration closes soon
- **要点**: PGConf India 2026の講演とトレーニングが公開され、早期割引登録がまもなく終了します。
- **技術ポイント**: PostgreSQLに関する知識とネットワーキングの機会。
- **リンク**: https://www.postgresql.org/about/news/pgconf-india-2026-talks-trainings-published-and-early-bird-registration-closes-soon-3208/

#### Amazon Aurora PostgreSQL now supports integration with Kiro powers
- **要点**: Amazon Aurora PostgreSQLがKiro powersとの統合をサポートし、AI支援コーディングによるアプリケーション開発を加速。
- **技術ポイント**: Kiro IDEによるワンクリックインストール、Model Context Protocolサーバーの利用。
- **リンク**: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-ecs-amazon-cloudwatch-amazon-cognito-and-more-december-15-2025/

#### Amazon Aurora DSQL now supports cluster creation in seconds
- **要点**: Amazon Aurora DSQLのデータベースプロビジョニング時間が数分から数秒に短縮され、迅速なプロトタイピングが可能に。
- **技術ポイント**: AWSコンソールクエリエディタ、AIを活用した開発、Aurora DSQL Model Context Protocolサーバー。
- **リンク**: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-ecs-amazon-cloudwatch-amazon-cognito-and-more-december-15-2025/

### AI/LLM

#### Real-World Agent Examples with Gemini 3
- **要点**: Gemini 3を活用した実世界のAIエージェントの例を紹介。ADK、Agno、Browser Useなどのフレームワークとの連携事例を解説。
- **技術ポイント**: Gemini 3の推論能力、状態管理、ツール連携。ADKによるエージェント開発、Agnoによるマルチエージェントシステム構築、Browser Useによるブラウザ自動化。
- **リンク**: https://developers.googleblog.com/real-world-agent-examples-with-gemini-3/

#### Gemini 3 Flash is now available in Gemini CLI
- **要点**: Gemini CLIでGemini 3 Flashが利用可能になり、ターミナルベースの作業における高頻度ワークフローをサポート。
- **技術ポイント**: Gemini 3 Flashの高速性と高品質、エージェントコーディングにおける性能向上。
- **リンク**: https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/

#### Agentic AI, MCP, and spec-driven development: Top blog posts of 2025
- **要点**: 2025年のGitHubブログの人気記事を紹介。Agentic AI、Model Context Protocol (MCP)、仕様駆動開発に関する記事が取り上げられています。
- **技術ポイント**: Agentic AIによるタスク自動化、MCPによるモデルコンテキストの共有、仕様駆動開発による品質向上。
- **リンク**: https://github.blog/developer-skills/agentic-ai-mcp-and-spec-driven-development-top-blog-posts-of-2025/

#### WRAP up your backlog with GitHub Copilot coding agent
- **要点**: GitHub Copilotコーディングエージェントを活用してバックログを効率的に消化する方法を紹介。
- **技術ポイント**: GitHub Copilotによるコード生成、テスト、ドキュメント作成の自動化。
- **リンク**: https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/

### クラウド

#### Happy New Year! AWS Weekly Roundup: 10,000 AIdeas Competition, Amazon EC2, Amazon ECS Managed Instances and more (January 5, 2026)
- **要点**: AWSの最新情報。10,000 AIdeas Competition、Amazon EC2 M8gn/M8gbインスタンス、AWS Direct Connectのレジリエンス・テストなどを紹介。
- **技術ポイント**: AWS Graviton4プロセッサ、AWS Nitro Cards、AWS Fault Injection Service。
- **リンク**: https://aws.amazon.com/blogs/aws/happy-new-year-aws-weekly-roundup-10000-aideas-competition-amazon-ec2-amazon-ecs-managed-instances-and-more-january-5-2026/

#### AWS Weekly Roundup: Amazon ECS, Amazon CloudWatch, Amazon Cognito and more (December 15, 2025)
- **要点**: Amazon WorkSpaces Secure BrowserのWebコンテンツフィルタリング、Amazon Aurora DSQLの高速プロビジョニング、Amazon ECSのカスタムコンテナ停止シグナルなどを紹介。
- **技術ポイント**: Webコンテンツフィルタリング、Aurora DSQL Model Context Protocolサーバー、ECS FargateのSTOPSIGNALサポート。
- **リンク**: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-ecs-amazon-cloudwatch-amazon-cognito-and-more-december-15-2025/

#### AWS Weekly Roundup: AWS re:Invent keynote recap, on-demand videos, and more (December 8, 2025)
- **要点**: AWS re:Invent 2025のキーノートのまとめと、オンデマンドビデオの紹介。
- **技術ポイント**: AIエージェント、Graviton、カスタムシリコン。
- **リンク**: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-reinvent-keynote-recap-on-demand-videos-and-more-december-8-2025/

### セキュリティ

#### Strengthening supply chain security: Preparing for the next malware campaign
- **要点**: サプライチェーンセキュリティを強化し、次のマルウェアキャンペーンに備えるための対策を紹介。
- **技術ポイント**: 脆弱性レポート、インシデント対応、サプライチェーンリスク管理。
- **リンク**: https://github.blog/security/supply-chain-security/strengthening-supply-chain-security-preparing-for-the-next-malware-campaign/

#### ICE Is Going on a Surveillance Shopping Spree
- **要点**: 米国移民・関税執行局（ICE）が監視技術に巨額の予算を投じている現状を批判的に解説。
- **技術ポイント**: ICEによる個人データ収集、監視活動、プライバシー侵害。
- **リンク**: https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree

### その他

#### Kernel bugs hide for 2 years on average. Some hide for 20
- **要点**: Linuxカーネルのバグが発見されるまでの平均期間は2.1年。最長で20年以上潜伏するバグも存在。
- **技術ポイント**: カーネルの脆弱性、バグの潜伏期間、脆弱性検出ツール。
- **リンク**: https://pebblebed.com/blog/kernel-bugs

#### A Developer's Guide to Debugging JAX on Cloud TPUs: Essential Tools and Techniques
- **要点**: Cloud TPUs上でJAXをデバッグするためのツールとテクニックを紹介。
- **技術ポイント**: libtpu、JAX、jaxlib、ロギング、プロファイリング。
- **リンク**: https://developers.googleblog.com/a-developers-guide-to-debugging-jax-on-cloud-tpus-essential-tools-and-techniques/

#### Play Aardwolf MUD
- **要点**: テキストベースのロールプレイングゲーム「Aardwolf MUD」の紹介。
- **技術ポイント**: MUDゲーム、ファンタジー世界、キャラクター育成。
- **リンク**: https://www.aardwolf.com/

---

## 💡 今日のアクションポイント

- PostgreSQLのアプリケーション開発者はpgpmを試して、データベースロジックの再利用性を向上させる。
- AWSを利用している開発者は、Amazon Aurora PostgreSQLとKiro powersの統合を検討し、AI支援コーディングを試す。
- GitHub Copilotを活用して、バックログの消化を効率化する。
- サプライチェーンセキュリティを強化するために、脆弱性レポートとインシデント対応のプロセスを見直す。
- Cloud TPUs上でJAXをデバッグする際に、紹介されたツールとテクニックを活用する。

---

## 📚 元記事一覧

| タイトル | ソース | URL |
|---------|--------|-----|
| Introducing pgpm: A Package Manager for Modular PostgreSQL | rss:postgres_blog | https://www.postgresql.org/about/news/introducing-pgpm-a-package-manager-for-modular-postgresql-3196/ |
| Welcoming three new members to the PostgreSQL Community Code of Conduct Committee | rss:postgres_blog | https://www.postgresql.org/about/news/welcoming-three-new-members-to-the-postgresql-community-code-of-conduct-committee-3209/ |
| PGConf India 2026: Talks, trainings published and early bird registration closes soon | rss:postgres_blog | https://www.postgresql.org/about/news/pgconf-india-2026-talks-trainings-published-and-early-bird-registration-closes-soon-3208/ |
| Kernel bugs hide for 2 years on average. Some hide for 20 | rss:hacker_news | https://pebblebed.com/blog/kernel-bugs |
| Play Aardwolf MUD | rss:hacker_news | https://www.aardwolf.com/ |
| ICE Is Going on a Surveillance Shopping Spree | rss:hacker_news | https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree |
| Happy New Year! AWS Weekly Roundup: 10,000 AIdeas Competition, Amazon EC2, Amazon ECS Managed Instances and more (January 5, 2026) | rss:aws_blog | https://aws.amazon.com/blogs/aws/happy-new-year-aws-weekly-roundup-10000-aideas-competition-amazon-ec2-amazon-ecs-managed-instances-and-more-january-5-2026/ |
| AWS Weekly Roundup: Amazon ECS, Amazon CloudWatch, Amazon Cognito and more (December 15, 2025) | rss:aws_blog | https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-ecs-amazon-cloudwatch-amazon-cognito-and-more-december-15-2025/ |
| AWS Weekly Roundup: AWS re:Invent keynote recap, on-demand videos, and more (December 8, 2025) | rss:aws_blog | https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-reinvent-keynote-recap-on-demand-videos-and-more-december-8-2025/ |
| Agentic AI, MCP, and spec-driven development: Top blog posts of 2025 | rss:github_blog | https://github.blog/developer-skills/agentic-ai-mcp-and-spec-driven-development-top-blog-posts-of-2025/ |
| WRAP up your backlog with GitHub Copilot coding agent | rss:github_blog | https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/ |
| Strengthening supply chain security: Preparing for the next malware campaign | rss:github_blog | https://github.blog/security/supply-chain-security/strengthening-supply-chain-security-preparing-for-the-next-malware-campaign/ |
| A Developer's Guide to Debugging JAX on Cloud TPUs: Essential Tools and Techniques | rss:google_developers | https://developers.googleblog.com/a-developers-guide-to-debugging-jax-on-cloud-tpus-essential-tools-and-techniques/ |
| Real-World Agent Examples with Gemini 3 | rss:google_developers | https://developers.googleblog.com/real-world-agent-examples-with-gemini-3/ |
| Gemini 3 Flash is now available in Gemini CLI | rss:google_developers | https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/ |

---

*生成日: 2026-01-08*
```
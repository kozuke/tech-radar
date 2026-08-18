# Tech Radar Daily Digest - 2026-08-19

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、Amazon Bedrock AgentCoreの機能として「AgentCore payments」の一般提供（GA）を開始しました。この機能は、AIエージェントが有料APIやコンテンツ、MCP（Model Context Protocol）サーバーへのアクセス・決済を自律的に行えるようにするもので、企業が商取引を行うエージェントを大規模に運用するためのセキュリティやガードレール、可観測性を提供します。CoinbaseやStripe Privyウォレットとの統合によりマイクロトランザクションをサポートし、プロトコルレベルでの決済オーケストレーションや支出制限の設定が可能です。

また、OpenAIのCodex CLIにおいても、Amazon Bedrock Runtimeを組み込みプロバイダーとしてサポートするアップデート（v0.148.0）がリリースされました。AIエージェントが自律的にリソースを調達・決済する仕組みと、それを支える推論基盤の連携が強化されており、開発者がAIエージェントを実業務へ導入する際の障壁が大幅に低減されることが期待されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.235

Claude Codeの最新版では、スペルチェック機能の追加や、ターミナルUIにおけるマークダウン表示の改善が行われました。また、バックグラウンドで実行されるクラウドセッションのメモリ・CPU使用率が最適化され、より安定した動作が可能になっています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | メモリ・CPU使用率の改善、スペルチェック機能追加 |
| 対応環境 | macOS/Linux |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.235

#### OpenAI Codex

##### 0.148.0

Codex CLIのメジャーアップデートでは、会話のMarkdownエクスポート機能や、セッションのフォーク・アーカイブ機能が追加されました。特にAmazon Bedrock Runtimeのサポートや、非同期フックによるMCPツールの呼び出しが可能になった点が大きな強化です。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| エクスポート | 会話履歴をMarkdown形式でクリップボードやファイルへ出力可能。 |
| セッション管理 | セッションのフォーク、アーカイブ、復元がTUIから直接操作可能。 |
| Bedrock連携 | AWSプロファイル経由でBedrock Runtimeを組み込みプロバイダーとして利用可能。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Codex CLI (Rust) |
| 特徴・性能 | MCPツールとの非同期連携、コスト見積もりの表示 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.148.0

---

### クラウド

#### AWS

##### AgentCore payments GA

Amazon Bedrock AgentCoreにおいて、AIエージェントが自律的に決済を行うための機能が一般提供されました。CoinbaseやStripeを通じたマイクロ決済に対応し、エンタープライズ環境での安全な運用を支援します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/bedrock-agentcore-payments-ga/

##### Amazon SageMaker Unified Studio アップデート

SageMaker Unified StudioがAWS Glue Data Qualityと連携し、データプロファイリングと異常検知をサポートしました。これにより、データセットの統計的な形状把握や、履歴に基づいた異常値の自動検出が容易になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/smus-data-profiling

##### Amazon MWAA Serverless アップデート

Amazon MWAA ServerlessがPythonOperatorおよびBashOperatorをサポートしました。これにより、データエンジニアリングチームはインフラを別途構築することなく、カスタムPython関数やシェルスクリプトをサーバーレス環境で実行可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/mwaa-serverless-pythonoperator-bashoperator/

##### EC2 R8i インスタンスの提供地域拡大

Intel Xeon 6プロセッサを搭載したR8iインスタンスが、イスラエル（テルアビブ）リージョンで利用可能になりました。メモリ集約型ワークロードにおいて、前世代比で最大15%の価格性能向上と2.5倍のメモリ帯域幅を実現します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-r8i-israel-tel-aviv/

##### IAM Policy Autopilot の機能強化

IAM Policy AutopilotがTerraform planファイルからのポリシー生成に対応しました。インフラ定義からCRUDベースの最小権限ポリシーを自動生成できるため、IaCを用いたAWS環境構築時のセキュリティ設計が効率化されます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/iam-policy-autopilot-now-supports-terraform-plan-files

---

### Workspace

#### Google Calendar

##### 迷惑な招待のブロック機能

Googleカレンダーにおいて、特定のユーザーをブロックすることで、カレンダーへの招待を拒否し、過去のイベントも自動削除する機能が追加されました。このブロック設定はGoogleアカウント全体で共有され、他のGoogle製品でのやり取りにも適用されます。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/08/managing-unsolicited-event-invitations-with-user-blocking-in-Google-Calendar.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Terraform planファイルを用いたIAMポリシー生成の試行 | インフラエンジニア | 🟡 中 |
| Codex CLIをv0.148.0へアップデートしBedrock連携を確認 | AI開発者 | 🟡 中 |
| カレンダーのスパム対策としてブロック機能の仕様確認 | 全ユーザー | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AgentCore payments is now GA | AWS | AWS News | [URL](https://aws.amazon.com/about-aws/whats-new/2026/08/bedrock-agentcore-payments-ga/) |
| SageMaker Unified Studio data profiling | AWS | AWS News | [URL](https://aws.amazon.com/about-aws/whats-new/2026/05/smus-data-profiling) |
| MWAA Serverless Python/Bash support | AWS | AWS News | [URL](https://aws.amazon.com/about-aws/whats-new/2026/08/mwaa-serverless-pythonoperator-bashoperator/) |
| EC2 R8i in Israel | AWS | AWS News | [URL](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-r8i-israel-tel-aviv/) |
| IAM Policy Autopilot Terraform support | AWS | AWS News | [URL](https://aws.amazon.com/about-aws/whats-new/2026/08/iam-policy-autopilot-now-supports-terraform-plan-files) |
| Claude Code v2.1.235 | AI | GitHub | [URL](https://github.com/anthropics/claude-code/releases/tag/v2.1.235) |
| Codex CLI 0.148.0 | AI | GitHub | [URL](https://github.com/openai/codex/releases/tag/rust-v0.148.0) |
| Google Calendar Blocking | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/08/managing-unsolicited-event-invitations-with-user-blocking-in-Google-Calendar.html) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
Amazon Bedrock AgentCoreでAIエージェントの自律決済機能「AgentCore payments」が一般提供開始。

📌 **ピックアップ**
• OpenAI Codex CLIがv0.148.0へ更新、Bedrock Runtime連携やMCPツール呼び出しに対応。
• AWS IAM Policy AutopilotがTerraform planファイルからのポリシー生成をサポート。
• Googleカレンダーにユーザーブロック機能が追加され、スパム招待を自動遮断可能に。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-08-19*
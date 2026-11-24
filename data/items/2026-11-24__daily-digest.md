# Tech Radar Daily Digest - 2026-11-24

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AWS WAFの大幅な機能強化と価格体系の刷新**
AWS WAFにおいて、AIエンドポイント（LLM、MCP、A2A）の自動検出と保護機能が一般提供開始されました。API GatewayやALB、CloudFront配下のAIエンドポイントを自動的に特定し、「AWS WAF AI Security」マネージドルールグループを通じてプロンプトインジェクションや有害コンテンツをブロックします。また、価格体系も簡素化され、設定ごとの課金から「保護対象リソース」「検査トラフィック量」「保護レベル」に基づく予測可能なモデルへと移行しました。これにより、セキュリティ運用のコスト透明性が向上し、AIアプリケーションの安全なデプロイが容易になります。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic
##### v2.1.331 (Claude Code)
Claude Codeの最新版では、Amazon BedrockやGoogle CloudのAgent Platformなど主要なクラウドプラットフォームでの「Code Mode」サポートが追加されました。また、API接続状況の診断機能や、LLMリクエストのトレース情報（トークン使用量やモデル名など）の拡充が行われ、開発者のデバッグ効率が向上しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, MCP, LLM |
| 特徴・性能 | マルチプラットフォーム対応強化、トレース機能拡充 |
| 対応環境 | ターミナル環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.13.0

---

#### OpenAI / Codex
##### 0.172.0
Codex CLIのメジャーアップデートでは、スレッドリンクの追従機能や、コマンド補完（Tabキー）、タスクグループ間のナビゲーションなど、ターミナルでの操作性が大幅に改善されました。また、サンドボックス権限の保持や、プロバイダーエラーの即時報告など、安定性と信頼性に関わる修正も多く含まれています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Codex CLI, Rust |
| 特徴・性能 | 操作性向上、エラーハンドリング強化 |
| 対応環境 | ターミナル |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.172.0

---

#### Google AI
##### セマンティック・ガバナンス・ポリシーによるAIエージェント保護
Googleは、AIエージェントに対する「意図のハイジャック（indirect prompt injection）」を防ぐためのセマンティック・ガバナンス・ポリシーの有効性を発表しました。ユーザーの意図とエージェントの行動を自然言語で照合することで、攻撃成功率を48.7%から0.9%まで劇的に低減させることに成功しています。

> 🔗 **参考リンク**
> https://developers.googleblog.com/did-the-user-ask-for-this-securing-ai-agents-against-intent-hijacking-with-semantic-governance-policies/

---

### クラウド

#### AWS
##### Amazon EC2 X8i インスタンスの提供開始
ニュージーランドリージョンにて、Intel Xeon 6プロセッサを搭載したX8iインスタンスが利用可能になりました。SAP HANAや大規模データベースなどのメモリ集約型ワークロード向けに設計されており、前世代と比較して最大43%のパフォーマンス向上と、最大6TBのメモリ容量を提供します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-x8i-new-zealand/

##### AWS Sign-Inのセッション時間延長
AWS Sign-Inにおいて、最大90日間のセッション持続が可能になりました。IAMユーザーやロールごとに設定可能で、開発者やAIエージェントが頻繁な認証なしで長時間ワークフローを実行できる一方、短命な認証情報を使用することでセキュリティを維持します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/configurable-aws-sign-in-duration/

---

### Workspace

#### Google Workspace
##### Google Meetの1080p対応とGoogle ChatのMarkdown強化
Google MeetのWeb版で、すべてのユーザーに対して1080pビデオ送信がデフォルトで有効化されました。また、Google ChatではアプリやエージェントがMarkdown形式でテーブルや見出しを送信できるようになり、情報の可読性が向上しています。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/11/google-meet-on-web-now-supports-sending-1080p-video-for-all-users-enabled-by-default.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| AWS WAFの新価格体系への移行確認とAI保護の有効化 | クラウド管理者 | 🔴 高 |
| Claude Code / Codex CLIのアップデート適用 | 開発者 | 🟡 中 |
| AIエージェントのセマンティック・ガバナンス導入検討 | AI開発者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EC2 X8i instances... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-x8i-new-zealand/ |
| AWS Sign-In introduces... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/configurable-aws-sign-in-duration/ |
| AWS WAF introduces simplified pricing | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/aws-waf-introduces-simplified-pricing/ |
| AWS WAF AI endpoint discovery | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/waf-ai-endpoint-discovery-protection/ |
| v2.1.331 (Claude Code) | AI/LLM | claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.331 |
| 0.172.0 (Codex) | AI/LLM | openai_codex_cli_releases | https://github.com/openai/codex/releases/tag/rust-v0.172.0 |
| Did the user ask for this? | AI/LLM | google_developers | https://developers.googleblog.com/did-the-user-ask-for-this-securing-ai-agents-against-intent-hijacking-with-semantic-governance-policies/ |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AWS WAFがAIエンドポイントの自動保護機能をリリースし、価格体系を簡素化。

📌 **ピックアップ**
• AWS WAF: AIエンドポイントの自動検出と保護、予測可能な新料金体系へ
• Claude Code/Codex: 開発者向けCLIツールが大幅アップデート
• Google Workspace: Meetの1080p標準化とChatのMarkdown対応

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-24*
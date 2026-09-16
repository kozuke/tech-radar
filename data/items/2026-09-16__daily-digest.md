# Tech Radar Daily Digest - 2026-09-16

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Googleが「ゼロトラストAIエージェント」のランタイムガバナンスを強化**
Googleは、AIエージェントのセキュリティを強化する「ゼロトラスト・エージェント」シリーズの第2弾として、Gemini Enterprise Agent Platformにおけるランタイムガバナンス機能を発表しました。従来のCI/CDパイプラインでの静的なチェックとは異なり、Model Armorやセマンティック・ガバナンス・ポリシーを活用することで、エージェントの「意図」を推論し、動的な異常検知と修復を行うことが可能になります。これにより、単なる構文チェックでは防げなかったソーシャルエンジニアリングや不正なデータアクセスを、プラットフォーム側で一元的に制御できるようになり、企業レベルでの安全なAI活用が大きく前進します。

**AWSがコスト管理とAI開発の運用効率を大幅改善**
AWSは、Billing and Cost Management（BCM）ダッシュボードに「Detected Anomalies」ウィジェットを追加し、コスト異常を可視化する機能を強化しました。また、Amazon SageMaker AIでは、トレーニングや処理ジョブにおいて「インスタンス優先順位リスト」を指定可能になり、高需要期におけるGPUリソースの確保が容易になりました。これらのアップデートは、クラウドコストの透明性向上と、AI開発におけるインフラ調達の自動化・効率化を同時に実現するもので、運用負荷の軽減に直結する重要な改善です。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic SDK

##### Claude Code v2.1.273 / v2.1.272
Claude Codeの最新リリースでは、LLMゲートウェイ向けのリクエストヘッダー追加や、MCPサーバー切断時の通知機能など、開発者体験を向上させる多数の改善が行われました。特に、リモートコントロールセッションのフォーク機能や、パーミッションチェックのバグ修正により、より安全かつ柔軟なAIコーディング環境が提供されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| ゲートウェイヘッダー | LLMゲートウェイ向けにリクエストクラスやエージェントタイプ等のヘッダーを追加。 |
| MCP通知 | MCPサーバーの接続切断時に自動再接続が失敗した場合の通知機能を追加。 |
| セッションフォーク | リモートコントロールセッションをバックグラウンドでフォークする機能を追加。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | 権限管理の強化、セッション管理の柔軟性向上 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.273

---

#### Gemini / Google AI

##### Gemini in Google Workspaceのサードパーティ連携強化
Google WorkspaceのGeminiにおいて、Asana、Atlassian Rovo、HubSpot、Salesforceなどの主要ツールとModel Context Protocol (MCP) を通じて直接連携が可能になりました。これにより、ユーザーはタブを切り替えることなく、GmailやDocs、Sheets等の画面から直接外部ツールの情報を参照・操作できるようになり、ワークフローの分断が解消されます。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/09/connect-to-more-tools-with-gemini-in-Google-Workspace.html

---

### クラウド

#### AWS

##### AWS Billing Conductorのカスタムレート対応
AWS Billing Conductorがカスタムレートおよび使用量ティア価格設定をサポートしました。これにより、パートナーや企業は、AWSの公開オンデマンド料金に依存せず、独自の商用契約に基づいた正確なプロフォーマ請求データをモデル化できるようになります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/AWS-Billing-Conductor-custom-rates-usage-tier

---

### Workspace

#### Google Workspace

##### Gmail検索のAI Overviewsがグローバル展開
Gmail検索において、自然言語でメールの内容を要約・回答する「AI Overviews」機能が、英語設定の全ユーザー（有料プラン）に対してグローバルで利用可能になりました。これにより、膨大なメールの中から必要な情報を探す手間が大幅に削減されます。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/09/gmail-searchs-ai-overviews-now-available-globally.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| BCMダッシュボードへの異常検知ウィジェット追加 | AWS管理者 | 🟡 中 |
| Gemini Workspaceのサードパーティコネクタ設定確認 | 管理者 | 🟡 中 |
| Claude Codeのアップデート適用 | 開発者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Monitor cost anomalies... | AWS | AWS | https://aws.amazon.com/... |
| AWS Billing Conductor... | AWS | AWS | https://aws.amazon.com/... |
| Amazon SageMaker AI... | AI/LLM | AWS | https://aws.amazon.com/... |
| Analyze CloudTrail... | セキュリティ | AWS | https://aws.amazon.com/... |
| Amazon Connect... | その他 | AWS | https://aws.amazon.com/... |
| Claude Code v2.1.273 | AI/LLM | GitHub | https://github.com/... |
| Gemini in Workspace... | Workspace | Google | http://workspaceupdates... |
| Gmail Search AI Overviews... | Workspace | Google | http://workspaceupdates... |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
GoogleがAIエージェントの「意図」を判断するゼロトラスト基盤を発表。

📌 **ピックアップ**
• AWS: コスト異常検知ウィジェットとSageMakerのインスタンス優先順位指定に対応
• Google Workspace: GeminiがAsanaやSalesforce等の外部ツールとMCPで直接連携可能に
• Claude Code: セッション管理や権限周りのバグ修正を含むv2.1.273をリリース

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-09-16*
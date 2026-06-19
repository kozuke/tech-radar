# Tech Radar Daily Digest - 2026-06-19

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Cursorが「常駐型エージェント」による自動化機能を大幅強化**
Cursorは、繰り返し発生するタスクを自動化する「Cursor Automations」をリリースしました。`/automate`スキルを用いることで、自然言語で指示を出すだけでエージェントがトリガーやツール設定を自動構成します。特にGitHub（IssueコメントやPRレビュー等）やSlack（絵文字リアクション）との連携が強化され、クラウドエージェントが「Computer Use」ツールを使用してデモ作成まで行えるようになった点は、開発ワークフローの自律化を大きく前進させるものです。

**GoogleがAIエージェントの協調プロトコル「A2A」の1周年を報告**
Googleは、AIエージェント同士が安全にタスクを委譲・連携するための「Agent-to-Agent (A2A)」プロトコルの1周年を迎えました。APIのような静的な接続とは異なり、エージェントの自律性を維持しつつ、セキュアな境界線（ブラックボックス化）を保ちながら専門的なエージェント間でタスクをハンドオフできる点が特徴です。これにより、単一のLLMのコンテキスト制限を回避し、複雑なワークフローを分散管理することが可能になります。

---

## 📰 今日のニュース

### AI/LLM

#### AI Agent / IDE

##### Cursor Automationsの導入と機能拡張

Cursorは、常駐型エージェントによる自動化機能「Cursor Automations」を導入しました。`/automate`スキルによるタスク設定の自動化に加え、GitHubの各種イベントやSlackの絵文字リアクションをトリガーとしてエージェントを起動可能になり、開発者のルーチンワークを大幅に削減します。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| /automate | 自然言語による指示から自動化設定を生成する新スキル。 |
| GitHubトリガー | IssueコメントやPRレビュー、ワークフロー完了など5種類のトリガーを追加。 |
| Computer Use | クラウドエージェントが自身の環境でデモや成果物を作成する機能。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Cursor Automations, Computer Use |
| 対応環境 | Cursor IDE |

> 🔗 **参考リンク**
> https://cursor.com/changelog#2026-06-18-cursor-automations-save-you-time-by-automating-repetitive-tasks-with-always-on-a

---

##### Devinの機能アップデート

Devinは、コマンドパレット（Cmd+K）による組織切り替えや、Slack連携の強化、PRレビュー時の言語選択機能などを追加しました。特にセキュリティポリシー（SECURITY.md）を考慮したレビューや、Slackスレッドの文脈を保持した応答機能が強化され、チーム開発におけるエージェントの有用性が向上しています。

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-06-17-cmd-k-switch-organization-copy-org-id

---

### クラウド

#### AWS

##### Amazon ECSのサービスオートスケーリングが高速化

Amazon ECSのサービスオートスケーリングが、20秒間隔の高解像度メトリクスに対応しました。これにより、負荷変動に対する検知からスケーリング実行までの時間が大幅に短縮され、従来比でスケーリング開始までの時間が約76%高速化（363秒→86秒）しました。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon ECS, CloudWatch |
| 改善点 | メトリクス解像度を60秒から20秒へ短縮 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ecs-faster-autoscaling/

---

##### Amazon EC2 G7インスタンスの一般提供開始

NVIDIA RTX PRO 4500 Blackwell Server Edition GPUを搭載したG7インスタンスが一般提供開始されました。G6と比較してAI推論性能が最大4.6倍、グラフィックス性能が最大2.1倍向上しており、大規模なAI推論やリアルタイムレンダリングに適しています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-g7-generally-available

---

### Workspace

#### Google Workspace

##### Gemini in Sheetsの言語サポート拡大

Google Sheetsで自然言語からスプレッドシートの構築・編集を行うGeminiの機能が、日本語を含む28言語に拡大されました。これにより、グローバルチームが母国語でデータ分析や財務モデルの構築を効率的に行えるようになります。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/expanded-language-support-for-gemini-in-sheets.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Cursorの最新版へアップデートし、`/automate`を試す | 開発者 | 🔴 高 |
| ECSのサービスオートスケーリング設定を20秒解像度へ見直す | インフラエンジニア | 🟡 中 |
| Gemini in Sheetsの日本語対応状況を確認し業務活用を検討 | 全ユーザー | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon ECS announces faster service auto scaling | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ecs-faster-autoscaling/ |
| Amazon EC2 G7 instances are now generally available | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-g7-generally-available |
| Cursor Automations... | 開発ツール | cursor_changelog | https://cursor.com/changelog#2026-06-18-cursor-automations-save-you-time-by-automating-repetitive-tasks-with-always-on-a |
| How A2A is Building a World of Collaborative Agents | AI/LLM | google_developers | https://developers.googleblog.com/how-a2a-is-building-a-world-of-collaborative-agents/ |
| Expanded language support for Gemini in Sheets | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/06/expanded-language-support-for-gemini-in-sheets.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Cursorが「常駐型エージェント」による自動化機能をリリースし、開発ワークフローの自律化が加速。

📌 **ピックアップ**
• Cursor: `/automate`スキルでGitHub/Slack連携の自動化が容易に
• AWS: ECSオートスケーリングが20秒メトリクス対応で大幅高速化
• Google: Gemini in Sheetsが日本語対応、AIエージェント協調プロトコルA2Aも1周年

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-19*
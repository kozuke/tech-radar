# Tech Radar Daily Digest - 2026-05-30

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AIエージェントの自律性と安全性の向上**
AIコーディングツールにおいて、ユーザーの介入を減らしつつ安全性を確保する「自律実行モード」の進化が目立っています。Cursorは新たに「Auto-review」モードを導入し、シェルコマンドやMCPツール呼び出しを分類器エージェントが判断することで、承認プロンプトを最小化しつつ安全な実行を実現しました。また、Anthropicの「Claude Code」もプラグインの自動読み込みやエージェント機能の強化を継続しており、開発者がAIエージェントに任せられるタスクの範囲が急速に拡大しています。これらのアップデートは、AIが単なるコード生成ツールから、複雑な開発タスクを完遂する自律的なパートナーへと進化していることを示唆しています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic SDK

##### Claude Code v2.1.157
Claude Codeの最新版では、`.claude/skills`ディレクトリ内のプラグインが自動読み込みされるようになり、マーケットプレイスを介さない柔軟な機能拡張が可能になりました。また、エージェント機能の強化や、サンドボックスのネットワーク権限プロンプトの修正など、開発体験を向上させる多数の改善が含まれています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, MCP, Git Worktree |
| 特徴・性能 | プラグイン自動読み込み、エージェント設定の強化、UI/UX修正 |
| 対応環境 | CLI, VS Code, Cursor, Windsurf |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.157

##### Anthropic Python SDK v0.105.1 / v0.105.2
AnthropicのPython SDKがマイナーアップデートされました。PyPIリリースのためのTrusted Publishingへの移行など、内部的な改善が主となっています。

> 🔗 **参考リンク**
> https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.105.2

#### Cursor

##### Auto-review モードの導入
Cursorに「Auto-review」という新しい実行モードが追加されました。Shell、MCP、Fetchツール呼び出しに対し、分類器エージェントが自動的に実行可否を判断することで、ユーザーの承認回数を減らしつつ安全な実行環境を提供します。

> 🔗 **参考リンク**
> https://cursor.com/changelog#2026-05-29-auto-review-is-a-new-run-mode-that-allows-cursor-to-work-for-longer-with-fewer-a

---

### クラウド

#### AWS

##### Amazon SES: インボックス到達率とブロックリスト監視
Amazon SESに、メールがスパムフォルダに振り分けられた割合を可視化する機能と、ドメインやIPが公開ブロックリストに登録されたかを監視する機能が追加されました。これにより、メールの到達率を向上させるための具体的な改善策を講じることが可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ses-global-deliverability/

##### AWS End User Messaging: RCS for Businessの提供地域拡大
RCS for Businessが新たに20カ国で利用可能になり、合計22カ国で展開されました。既存のAPIを変更することなく、検証済みのブランドメッセージを送信でき、非対応端末には自動的にSMSへフォールバックされます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/aws-rcs-countries/

##### AWS Shield Advanced: DDoS攻撃フローログの導入
DDoS攻撃発生時に、パケットレベルのトラフィック詳細をS3やCloudWatch Logsに出力する機能が追加されました。これにより、攻撃のフォレンジック分析や脅威インテリジェンスの収集が容易になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/aws-shield-ddos/

---

### Workspace

#### Google Workspace

##### Google Classroom: 学習目標のタグ付け機能
教育現場向けに、課題やルーブリックに学習基準やスキルをタグ付けできる機能が追加されました。AIが分析をサポートし、学生の進捗状況を可視化することで、指導のギャップを特定しやすくなります。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/05/keep-track-of-student-progress-with-learning-standards-and-skills-in-Google-Classroom.html

##### NotebookLM: Google Driveとの自動同期
NotebookLMがGoogle Driveと自動同期するようになり、ソースファイルが更新されるとノートブック内の情報も自動的に最新化されるようになりました。また、Powerschool Schoologyとの連携も強化されています。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/05/weekly-recap-05-29-2026.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude Codeをv2.1.157にアップデートする | 開発者 | 🟡 中 |
| Cursorの「Auto-review」設定を確認・有効化する | 開発者 | 🔴 高 |
| Amazon SESの到達率メトリクスを確認し設定を見直す | インフラ担当 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon SES inbox placement metrics | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ses-global-deliverability/) |
| AWS End User Messaging RCS | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-rcs-countries/) |
| Amazon Connect tasks 90 days | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-connect-customer-tasks-90day-schedule) |
| AWS Shield Advanced DDoS logs | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-shield-ddos/) |
| Redshift Serverless 4-RPU | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-redshift-serverless-4-rpu-seven-regions/) |
| Claude Code v2.1.157 | AI/LLM | GitHub | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.157) |
| Cursor Auto-review | AI/LLM | Cursor | [link](https://cursor.com/changelog#2026-05-29-auto-review-is-a-new-run-mode-that-allows-cursor-to-work-for-longer-with-fewer-a) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AIエージェントの自律実行モードが進化、Cursorの「Auto-review」やClaude Codeのプラグイン自動化で開発効率が向上。

📌 **ピックアップ**
• Cursor: 新モード「Auto-review」でAI実行の承認フローを効率化
• AWS: SESの到達率可視化やShieldのDDoSログ機能が強化
• Google: Classroomの学習進捗追跡やNotebookLMのDrive同期がアップデート
👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-30*
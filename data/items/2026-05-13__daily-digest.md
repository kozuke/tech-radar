# Tech Radar Daily Digest - 2026-05-13

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは、AIエージェントの構築を支援する「Agent Development Kit (ADK)」を活用した、長期稼働型AIエージェントの設計手法を公開しました。従来のステートレスなチャットボットとは異なり、数週間単位の業務（新入社員のオンボーディングなど）を完遂するために、「永続的なメモリスキーマ」「イベント駆動型の休止ゲート」「マルチエージェントによる委任」という3つのアーキテクチャシフトを提唱しています。これにより、コンテキストの喪失やトークンコストの増大、推論のハルシネーションといった課題を解決し、エンタープライズ環境での実用的なAI活用を可能にします。

また、AWSではLambda Managed Instancesにおける「スケジュールベースのスケーリング」がサポートされました。Amazon EventBridge Schedulerとの統合により、予測可能なトラフィック変動に合わせてLambdaの容量を事前に調整することが可能となり、コスト最適化とパフォーマンスの安定化が容易になります。同時にEventBridge SchedulerのAPIが大幅に拡充され、より広範なAWSサービスをコードレスで自動化できるようになりました。

---

## 📰 今日のニュース

### AI/LLM

#### Google

##### Build Long-running AI agents that pause, resume, and never lose context with ADK

ステートレスなチャットボットの限界を克服し、数週間にわたる長期的なワークフローを完遂するためのAIエージェント構築手法が公開されました。ADKを使用し、永続的なメモリ管理やイベント駆動型の設計を取り入れることで、コンテキストを維持したままタスクを中断・再開できる堅牢なエージェントを実現します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Agent Development Kit (ADK), LLM |
| 特徴・性能 | 長期記憶保持、イベント駆動型休止、マルチエージェント委任 |
| 対応環境 | クラウド環境 |
| 関連サービス | Google Cloud AI |

> 🔗 **参考リンク**
> https://developers.googleblog.com/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/

---

#### Claude Code

##### v2.1.140

Claude Codeの最新版では、エージェントツールのマッチング精度の向上や、設定のホットリロード時の不具合修正が行われました。特にバックグラウンドサービスの安定性向上や、Windows環境でのイベントループのスタック修正など、開発体験を改善する多くのバグフィックスが含まれています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | エージェントツール改善、Windows環境の安定性向上 |
| 対応環境 | macOS, Windows, Linux |
| 関連サービス | Anthropic Claude |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.140

---

### クラウド

#### AWS

##### AWS Lambda supports scheduled scaling for functions on Lambda Managed Instances

Lambda Managed Instancesにおいて、Amazon EventBridge Schedulerを用いたスケジュールベースのスケーリングが可能になりました。これにより、業務時間やイベント開催などの予測可能なトラフィック変動に対し、事前に容量を調整することでコスト削減とパフォーマンス維持を両立できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Lambda, Amazon EventBridge Scheduler |
| 特徴・性能 | 事前予約による容量スケーリング、コスト最適化 |
| 対応環境 | AWS Lambda Managed Instances対応リージョン |
| 関連サービス | Amazon EC2 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/aws-lambda-managed-instances/

---

### Workspace

#### Google Workspace

##### Use NotebookLM in your Google Workspace Studio flows

Google Workspace Studioにおいて、NotebookLMをAI知識ソースとして利用可能になりました。「Ask NotebookLM」ステップを追加することで、ノートブック内の洞察や要約に基づいた回答を自動生成できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Google Workspace Studio, NotebookLM |
| 特徴・性能 | AIナレッジベースの自動化フローへの統合 |
| 対応環境 | Google Workspace (Business/Enterprise/Education) |
| 関連サービス | Gemini for Google Workspace |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/05/notebooklm-in-workspace-studio.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Lambdaのスケジュールスケーリング設定の確認 | AWSインフラ管理者 | 🟡 中 |
| 長期稼働エージェントの設計手法のドキュメント確認 | AI開発者 | 🟡 中 |
| Workspace StudioへのNotebookLM統合の試用 | Google Workspace管理者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Lambda supports scheduled scaling... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/aws-lambda-managed-instances/ |
| Amazon EventBridge Scheduler adds 619 new SDK API actions... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-eventbridge-sdk-integrations/ |
| Amazon SageMaker Feature Store now supports SageMaker Python SDK V3 | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-sagemaker-feature-store-pyv3/ |
| v2.1.140 | AI/LLM | GitHub | https://github.com/anthropics/claude-code/releases/tag/v2.1.140 |
| rust-v0.131.0-alpha.10 | AI/LLM | GitHub | https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.10 |
| 0.131.0-alpha.9 | AI/LLM | GitHub | https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.9 |
| Build Long-running AI agents... | AI/LLM | Google | https://developers.googleblog.com/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/ |
| Use NotebookLM in your Google Workspace Studio flows | Workspace | Google | http://workspaceupdates.googleblog.com/2026/05/notebooklm-in-workspace-studio.html |
| Google Workspace Assignments LTI™ and Gemini LTI™ are now available for Moodle | Workspace | Google | http://workspaceupdates.googleblog.com/2026/05/workspace-assignments-lti-and-gemini-lti-for-moodle.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Googleが長期稼働AIエージェントの設計手法を公開し、AWS Lambdaがスケジュールスケーリングに対応しました。

📌 **ピックアップ**
• Google ADK: 長期タスクを完遂するAIエージェントの設計手法を公開
• AWS Lambda: EventBridge連携でスケジュールベースのスケーリングが可能に
• Google Workspace: StudioフローでNotebookLMが利用可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-13*
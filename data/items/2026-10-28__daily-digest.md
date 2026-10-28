# Tech Radar Daily Digest - 2026-10-28

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Amazon ECSがNVIDIA MPSによるGPU共有をサポート**
Amazon ECSがNVIDIA Multi-Process Service (MPS) をサポートし、単一のNVIDIA GPU上で複数のECSタスクを並列実行可能になりました。これにより、小規模な推論や埋め込み生成など、GPUリソースをフル活用しないワークロードにおいて、インフラコストの削減とGPU稼働率の向上が期待できます。特筆すべきは、アプリケーションコードの変更が不要である点と、ECSがMPS制御デーモンの健全性を監視し、異常時には自動的にタスクを健全なインスタンスへ移動させる自動復旧機能を備えている点です。

**DevinがUIを刷新し「Activity」タブを統合**
AIエンジニアリングツール「Devin」が大幅なアップデートを行い、従来の「Progress」と「Shell」タブを統合した「Activity」タブを導入しました。これにより、Devinの全操作が単一のストリームで可視化され、検索やフィルタリングが容易になりました。また、Artifactsのインライン表示機能や、Slack連携の強化、Terraformプロバイダーへの新リソース追加など、開発者のワークフロー効率を向上させる機能が多数実装されています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.312 リリース

Claude Codeの最新版では、OIDCのユーザーIDクレーム対応や、フルスクリーンモードでのクリック送信機能が追加されました。また、大規模なCLAUDE.mdファイルの上書き防止や、Bashコマンド実行時のパス解決の修正など、エージェントの操作性と信頼性を高めるバグ修正が多数含まれています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, OIDC, Bash |
| 特徴・性能 | ユーザー認証の柔軟性向上、ファイル編集の安全性強化 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.312

---

#### OpenAI Codex CLI

##### 0.165.0 および関連アルファ版

Codex CLIの最新安定版0.165.0では、Google Cloud Vertex AIプロバイダーの統合や、GPT-6.1 Terraモデルの追加が行われました。また、セッション管理の改善や、推論時の「推論努力（reasoning effort）」の動的変更がデフォルトで有効化されるなど、エージェントの推論能力を最大限に引き出すための機能強化が図られています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Vertex AI統合 | Google Cloud Vertex AIをモデルプロバイダーとして利用可能に。 |
| 推論努力の変更 | 会話中にモデルの推論コストや深さを調整可能に。 |
| Memory v2 | 新規プロファイルでデフォルト有効化、外部エージェントメモリのインポートに対応。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Rust, OpenAI API, GCP Vertex AI |
| 特徴・性能 | セッション管理の効率化、MCPツールリクエストのキャンセル処理改善 |
| 対応環境 | CLI |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.165.0

---

#### Google Gemini / A2UI

##### Fast, reliable A2UI, with swappable inference formats

Googleは、生成UI（A2UI）の応答速度を劇的に改善する「A2UI Express」を発表しました。従来のJSON形式に代わる中間フォーマットを採用することで、推論速度を最大3倍、レイアウト決定モデルとの組み合わせで最大80倍の高速化を実現し、生成UIのUXを大幅に向上させます。

> 🔗 **参考リンク**
> https://developers.googleblog.com/fast-reliable-a2ui/

---

### クラウド

#### AWS

##### Amazon Aurora Serverlessが最大384 ACUまで拡張

Aurora PostgreSQL互換エディションにおいて、最大容量が従来の256 ACUから384 ACUへ50%拡大されました。これにより、バースト性の高いエージェントAIアプリケーションなど、高い計算リソースを必要としつつもアイドル時にはゼロまでスケールダウンさせたいワークロードへの適応力が向上しました。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-serverless-supports-384-acu/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| ECSのGPU共有設定の検証 | GPUワークロードを持つインフラエンジニア | 🔴 高 |
| DevinのActivityタブの操作確認 | Devinユーザー | 🟡 中 |
| Aurora Serverlessの最大容量設定の再検討 | Aurora PostgreSQL利用者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon ECS now supports GPU sharing... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ecs-gpu-sharing-nvidia-mps/ |
| SageMaker MLflow Apps now support MLflow 3.16 | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/mflow-version-3-16/ |
| Amazon Aurora serverless now supports up to 384 ACUs | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-serverless-supports-384-acu/ |
| Amazon ElastiCache for Valkey now supports changing durability | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/elasticache-changing-durability/ |
| Amazon Corretto October 2026 Patch Updates | 開発ツール | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-corretto-oct-2026-patch-updates |
| v2.1.312 | AI/LLM | claude_code | https://github.com/anthropics/claude-code/releases/tag/v2.1.312 |
| 0.165.0 | AI/LLM | openai_codex | https://github.com/openai/codex/releases/tag/rust-v0.165.0 |
| Fast, reliable A2UI, with swappable inference formats | AI/LLM | google_dev | https://developers.googleblog.com/fast-reliable-a2ui/ |
| Building Conversational Commerce with Multi-Agent Swarms | AI/LLM | google_dev | https://developers.googleblog.com/building-conversational-commerce-with-multi-agent-swarms-on-gcp-a-working-prototype/ |
| New Activity Tab Replaces Progress and Shell | AI/LLM | devin | https://docs.devin.ai/release-notes/overview#2026-10-26-new-activity-tab-replaces-progress-and-shell |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon ECSがNVIDIA MPSによるGPU共有をサポートし、インフラコスト削減と効率化が加速！

📌 **ピックアップ**
• DevinがUIを刷新し「Activity」タブへ統合、操作性が大幅向上
• Aurora Serverlessが最大384 ACUへ拡張、AIワークロードに最適化
• Googleが生成UIの応答速度を最大80倍にする「A2UI Express」を発表

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-10-28*
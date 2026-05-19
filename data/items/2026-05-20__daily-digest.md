# Tech Radar Daily Digest - 2026-05-20

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは「Google I/O '26」に合わせて、オンデバイスAI開発を加速させる「Tensor ML SDK」のベータ版を公開しました。このSDKは、Pixel 10シリーズ以降のデバイスに搭載されたGoogle TensorチップのTPU（Tensor Processing Unit）を直接活用可能にするもので、これまで実験的プログラム（EAP）として提供されていた機能が正式に開発者へ開放されました。LiteRT（旧TensorFlow Lite）と統合されたことで、PyTorchやTFLiteモデルをTPU向けに最適化・コンパイルし、低遅延かつプライバシーに配慮したAI体験をアプリに組み込めるようになります。

また、同時に発表された「LiteRT-LM」は、Gemma 4などの大規模言語モデルをエッジ環境で高速実行するための推論エンジンです。Android、iOS、Web（WebGPU）の各プラットフォームで動作し、マルチトークン予測（MTP）技術などを駆使することで、モバイル端末上でも極めて高いトークン生成速度を実現しています。これにより、開発者はクラウドへの依存を減らし、デバイスの性能を最大限に引き出した次世代のAIアプリケーションを構築できるようになります。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic SDK

##### Claude Code v2.1.144 / v2.1.145
Claude Codeの最新アップデートでは、バックグラウンドセッションの管理機能が大幅に強化されました。`claude --bg`で開始したセッションのレジューム対応や、エージェントの処理状況をJSONで取得できる機能が追加され、スクリプトやステータスバーとの連携が容易になっています。また、プラグインのブラウズ機能の改善や、Bashコマンド実行時のパーミッション制御のバグ修正など、開発体験を向上させる細かな改善が多数含まれています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI, Agentic Workflow |
| 特徴・性能 | バックグラウンドセッション管理、JSON出力対応 |
| 対応環境 | CLI (macOS/Linux/Windows) |
| 関連サービス | Anthropic API |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.145

---

##### Anthropic SDK Python v0.103.0 / v0.103.1
Python向けAnthropic SDKがアップデートされ、セルフホスト型サンドボックスのサポートが追加されました。これにより、CMA（Claude Model API）環境下でのより柔軟なコード実行環境の構築が可能になります。また、ツール呼び出しに関連するバグ修正も行われており、安定性が向上しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Python SDK, Sandbox |
| 特徴・性能 | セルフホストサンドボックス対応 |
| 対応環境 | Python 3.x |
| 関連サービス | Anthropic API |

> 🔗 **参考リンク**
> https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.103.1

---

#### Gemini / Google AI

##### Google Tensor SDK Beta & LiteRT-LM
GoogleはTensor ML SDKをベータへ移行し、PixelデバイスのTPUを活用したオンデバイスAI開発を本格化させました。同時にリリースされたLiteRT-LMは、Gemma 4をエッジで高速実行するための最適化エンジンであり、AndroidやiOS、Web環境で高い推論パフォーマンスを提供します。

**技術ポイント**

| 項目 | 詳細 |
|------|解析 |
| 主要技術 | LiteRT, Tensor TPU, Gemma 4 |
| 特徴・性能 | マルチトークン予測(MTP)による高速推論 |
| 対応環境 | Android, iOS, Web |
| 関連サービス | Google Pixel 10+, Google AI Edge |

> 🔗 **参考リンク**
> https://developers.googleblog.com/google-tensor-sdk-beta-with-litert/

---

### クラウド

#### AWS

##### Amazon ECSのデプロイ一時停止機能
Amazon ECSでサービスデプロイメントの途中で処理を一時停止（PAUSE）できる機能が追加されました。これにより、手動承認や統合テスト、カスタム自動化プロセスをデプロイフローに組み込むことが可能になり、安全なリリース管理が実現します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon ECS, EventBridge |
| 特徴・性能 | 最大14日間のデプロイ一時停止、APIによる継続/ロールバック |
| 対応環境 | 全AWS商用リージョン |
| 関連サービス | CloudWatch, AWS CDK/Terraform |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ecs-pause-continue-deployments/

---

### 開発ツール

#### Cursor

##### CursorのJira統合
CursorがJiraと連携し、チケットベースでのAIエージェント起動が可能になりました。Jiraのチケット内容をコンテキストとしてCursorに読み込ませ、バグ修正や機能追加のコード生成を直接依頼し、完了後にプルリクエストのリンクをJiraに反映させることができます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Cursor AI Agent, Jira API |
| 特徴・性能 | チケットコンテキストの自動読み込み、PR連携 |
| 対応環境 | Cursor IDE, Jira Cloud |
| 関連サービス | Jira Rovo |

> 🔗 **参考リンク**
> https://cursor.com/changelog#2026-05-19-cursor-is-now-available-in-jira

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude Codeを最新版にアップデートし、バックグラウンドセッション機能を試す | 開発者 | 🟡 中 |
| ECSのデプロイ一時停止機能を検証し、手動承認フローを導入する | SRE/DevOps | 🔴 高 |
| CursorのJira統合を設定し、チケット駆動開発の効率化を図る | 開発チーム | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon MWAA supports Airflow 3.2 | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-mwaa-now-supports-apache-airflow-3-2/) |
| Amazon Inspector in Taipei | セキュリティ | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-inspector-taipei/) |
| ECS pause/continue deployments | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ecs-pause-continue-deployments/) |
| Claude Code v2.1.145 | AI/LLM | Anthropic | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.145) |
| Cursor Jira Integration | 開発ツール | Cursor | [link](https://cursor.com/changelog#2026-05-19-cursor-is-now-available-in-jira) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
GoogleがTensor ML SDKベータ版とLiteRT-LMを公開し、PixelデバイスでのオンデバイスAI開発が本格化。

📌 **ピックアップ**
• Claude Codeがバックグラウンドセッション管理を強化し、開発効率が向上。
• Amazon ECSがデプロイの一時停止・継続機能をサポートし、リリース管理が柔軟に。
• CursorがJiraと統合し、チケットから直接AIエージェントを起動可能に。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-20*
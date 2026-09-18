# Tech Radar Daily Digest - 2026-09-18

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、Elastic Beanstalkにおいて、共有インフラ上で複数のアプリケーションを効率的に管理・実行できる「Cluster Mode」を発表しました。これまで環境ごとに個別のリソースが必要だったのに対し、本モードではAmazon EKSを基盤とした共有プール上でアプリケーションを稼働させることで、スケーリング時のコスト最適化と運用効率の向上が期待できます。GitHub Actionsとの連携も強化されており、CI/CDパイプラインを通じたシームレスなデプロイが可能です。

また、GoogleはSpeakeasyと提携し、OpenAPI仕様からクライアントSDKを生成するツールスイートをオープンソース化しました。AIを活用した開発環境において、SDK生成のプロプライエタリなツールに依存することによるプラットフォームリスクを排除し、開発者がより堅牢で標準化されたインターフェースを構築できる環境を整える狙いがあります。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.275

Claude Codeの最新版では、Claude.aiアカウントのスキルやプラグインをターミナルセッションと同期する機能が追加されました。また、メッセージを即座に送信する「send-now」キーの導入や、認証フローの改善が行われ、開発体験が大幅に向上しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | アカウント同期機能、UI/UX改善、バグ修正 |
| 対応環境 | ターミナル環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.275

---

#### OpenAI Codex CLI

##### 0.155.0

Codex CLIのメジャーアップデートでは、実験的な音声会話機能やTUIでの推論サマリー表示、Touch IDによるMCPリクエスト認証などが導入されました。エージェント管理機能の強化やセキュリティのハードニングも行われており、よりセキュアでインタラクティブな開発支援ツールへと進化しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Rust, OpenAI Codex |
| 特徴・性能 | 音声会話、Touch ID認証、エージェント管理 |
| 対応環境 | macOS, Windows (WSL) |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.155.0

---

#### Google GenAI

##### Why client SDK generation belongs in the open

GoogleはSpeakeasyと協力し、OpenAPIベースのSDK生成ツールをオープンソース化しました。これにより、AIモデル（Gemini等）のAPIを利用する際のクライアントライブラリ生成におけるベンダーロックインを回避し、開発者がより柔軟にSDKを管理できるようになります。

> 🔗 **参考リンク**
> https://developers.googleblog.com/why-client-sdk-generation-belongs-in-the-open/

---

#### Devin

##### Live Voice Mode

AIエージェントDevinにライブ音声モードが追加され、リアルタイムでの音声対話が可能になりました。また、Slack連携の強化やVMの再起動アクション、セキュリティスキャンの強制適用など、実務での運用性を高めるアップデートが多数行われています。

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-09-16-live-voice-mode

---

### クラウド

#### AWS

##### AWS Transfer Family: SFTPサーバーでの送信元IP保持

AWS Transfer FamilyがNLB配下のSFTPサーバーにおいて、Proxy Protocol v2を用いた送信元IPの保持をサポートしました。これにより、IPベースのアクセス制御や監査ログの正確性が向上し、コンプライアンス要件への対応が容易になります。

##### AWS HealthOmics: IAMセッションポリシーのサポート

AWS HealthOmicsがIAMセッションポリシーに対応しました。これにより、ワークフロー実行ごとに動的に権限を制限することが可能となり、マルチテナント環境でのセキュリティ分離が容易になります。

##### AWS Batch: 一括ジョブキャンセル・終了

AWS Batchで最大50件のジョブを一度にキャンセル・終了できるAPIが追加されました。大規模なバッチ処理の運用負荷が軽減され、ジョブの状態監視も容易になります。

##### Amazon EC2 T8i インスタンスの一般提供開始

第6世代Intel Xeon 6プロセッサを搭載したT8iインスタンスが登場しました。T3インスタンスと比較して最大30%の価格性能向上を実現しており、CI/CDやマイクロサービスなど幅広いワークロードに適しています。

> 🔗 **参考リンク**
> - [Transfer Family](https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/)
> - [HealthOmics](https://aws.amazon.com/about-aws/whats-new/2026/09/omics-iam-session-policy/)
> - [Batch](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/)
> - [EC2 T8i](https://aws.amazon.com/about-aws/whats-new/2026/09/ec2-t8i-instances-ga/)

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| SFTPサーバーのログ監査設定の見直し | インフラ管理者 | 🟡 中 |
| Elastic Beanstalk Cluster Modeの検証 | アプリ開発者 | 🟡 中 |
| Codex CLIのアップデートとTouch ID設定 | 開発者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Transfer Family source IP preservation | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/ |
| AWS HealthOmics IAM session policies | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/omics-iam-session-policy/ |
| AWS Batch bulk job cancellation | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/aws-batch-bulk-cancellation/ |
| Amazon EC2 T8i instances | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/ec2-t8i-instances-ga/ |
| Elastic Beanstalk Cluster Mode | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/elastic-beanstalk-cluster-mode/ |
| Claude Code v2.1.275 | AI/LLM | GitHub | https://github.com/anthropics/claude-code/releases/tag/v2.1.275 |
| Codex CLI 0.155.0 | AI/LLM | GitHub | https://github.com/openai/codex/releases/tag/rust-v0.155.0 |
| Google GenAI SDK generation | AI/LLM | Google | https://developers.googleblog.com/why-client-sdk-generation-belongs-in-the-open/ |
| Devin Live Voice Mode | AI/LLM | Devin | https://docs.devin.ai/release-notes/overview#2026-09-16-live-voice-mode |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWS Elastic Beanstalkが共有インフラで複数アプリを管理する「Cluster Mode」を発表。

📌 **ピックアップ**
• AWS: SFTPの送信元IP保持やバッチの一括操作、新EC2インスタンスが登場。
• AI: Claude CodeやCodex CLIが機能強化、GoogleはSDK生成ツールをOSS化。
• Devin: ライブ音声モードやセキュリティスキャン強化など実務機能を拡充。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-09-18*
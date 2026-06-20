# Tech Radar Daily Digest - 2026-06-21

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Amazon SageMaker AIにおける推論エンドポイントの可観測性強化**
Amazon SageMaker AIに、生成AI推論ワークロードの運用を効率化する新しい可観測性機能が導入されました。これまでCloudWatchで手動で行っていたメトリクスの検索や、レイテンシのスパイクとGPU負荷・KVキャッシュ枯渇との相関分析が自動化され、Time to First Token（TTFT）やトークン毎秒などの主要指標がリアルタイムで可視化されます。これにより、運用チームはボトルネックを数分で特定可能となり、AI投資のパフォーマンスを最大化できます。また、Grafanaユーザー向けにPromQLエンドポイントも提供され、既存の監視環境への統合も容易です。

**DevinにおけるMCPマーケットプレイスの大幅拡充**
AIエンジニアリングエージェント「Devin」において、MCP（Model Context Protocol）マーケットプレイスが大幅に強化されました。Miro、Mixpanel、Honeycombなど48以上の新しいコネクタが追加され、42のベータ版MCPが正式リリースとなりました。さらに、GitLabとの連携が強化され、ユーザーIDでのマージリクエスト作成や、Devin ReviewによるGitLab MRのインテリジェントなレビューが可能になりました。エンタープライズ向けの管理機能も拡充されており、AIエージェントによる開発自動化の適用範囲が大きく広がっています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code
##### v2.1.185
API応答待ちのストリーム表示におけるメッセージが改善されました。「No response from API」という表現から、より前向きな「Waiting for API response」に変更され、タイムアウトのトリガー時間が10秒から20秒に延長されました。

#### OpenAI / Codex
##### 0.142.0-alpha.7
Codex CLIのプレリリース版が公開されました。詳細な変更ログは公開されていませんが、安定性向上に向けた修正が含まれていると推測されます。

#### AI Agent / Devin
##### MCP Marketplace Expansion
MCPコネクタの拡充に加え、GitLab連携の強化、ファイル操作の可視化、UIの改善など多岐にわたるアップデートが行われました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| MCPコネクタ拡充 | 48以上の新規コネクタ追加と42のベータ版が正式版へ移行。 |
| GitLab連携 | ユーザーIDでのMR作成や、Devin ReviewによるMRの自動レビューに対応。 |
| 管理機能 | エンタープライズ向けにMCPサーバーごとの詳細な使用状況管理ページを追加。 |

---

### クラウド

#### AWS
##### Ministral-3-14B-Instruct for multimodal reasoning and agentic AI is now available in Amazon SageMaker JumpStart
Mistral AIの14BパラメータモデルがSageMaker JumpStartで利用可能になりました。画像解析とテキスト処理を組み合わせたマルチモーダル推論や、ネイティブな関数呼び出しによるエージェント構築に最適化されています。

##### Amazon EKS now supports customer-routed control plane egress
EKSのコントロールプレーンからのアウトバウンド通信を、ユーザー自身のVPC経由でルーティングできるようになりました。これにより、プライベートなOIDCプロバイダーやWebhookサーバーへのアクセスをセキュアに制御可能です。

##### Amazon SNS now supports sending SMS in the Asia Pacific (Seoul) Region
ソウルリージョンにおいて、Amazon SNS経由でのSMS送信が可能になりました。AWS End User Messagingを通じて、世界200以上の国と地域へメッセージを配信できます。

##### Amazon GameLift Servers adds new container fleet improvements
コンテナフリートの柔軟性が向上し、Linuxの権限カスタマイズや、同一インスタンス内のコンテナ間ネットワーク情報の取得が可能になりました。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon SageMaker, EKS, SNS, GameLift |
| 特徴・性能 | エッジ向けマルチモーダルAI、VPC内通信制御、SMSグローバル配信 |
| 対応環境 | AWS全リージョン（一部機能はリージョン制限あり） |
| 関連サービス | CloudWatch, AWS Organizations, Unreal Engine/Unity |

> 🔗 **参考リンク**
> [Ministral-3-14B](https://aws.amazon.com/about-aws/whats-new/2026/06/ministral-3-14b-on-sagemaker-jumpstart/)
> [EKS Egress](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-customer-routed-control-plane-egress)
> [SageMaker Observability](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-sagemaker-ai-inference/)
> [SNS SMS Seoul](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-sns-supports-sending-sms-seoul-region/)
> [GameLift Containers](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-gamelift-servers-container-fleet-improvements)
> [Claude Code](https://github.com/anthropics/claude-code/releases/tag/v2.1.185)
> [Codex CLI](https://github.com/openai/codex/releases/tag/rust-v0.142.0-alpha.7)
> [Devin Release Notes](https://docs.devin.ai/release-notes/overview#2026-06-19-mcp-marketplace-expansion)

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| SageMakerの推論エンドポイント監視設定の確認 | AIエンジニア | 🔴 高 |
| EKSのコントロールプレーン通信経路の要件確認 | クラウドアーキテクト | 🟡 中 |
| DevinのGitLab連携設定とMCPコネクタの確認 | 開発チーム | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Ministral-3-14B... | AI/LLM | aws_whats_new | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/ministral-3-14b-on-sagemaker-jumpstart/) |
| Amazon EKS... | クラウド | aws_whats_new | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-customer-routed-control-plane-egress) |
| Amazon SageMaker AI... | クラウド | aws_whats_new | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-sagemaker-ai-inference/) |
| Amazon SNS... | クラウド | aws_whats_new | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-sns-supports-sending-sms-seoul-region/) |
| Amazon GameLift... | クラウド | aws_whats_new | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-gamelift-servers-container-fleet-improvements) |
| v2.1.185 | AI/LLM | claude_code | [URL](https://github.com/anthropics/claude-code/releases/tag/v2.1.185) |
| 0.142.0-alpha.7 | AI/LLM | openai_codex | [URL](https://github.com/openai/codex/releases/tag/rust-v0.142.0-alpha.7) |
| MCP Marketplace Expansion | AI/LLM | devin | [URL](https://docs.devin.ai/release-notes/overview#2026-06-19-mcp-marketplace-expansion) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
Amazon SageMaker AIの推論可観測性向上と、DevinのMCPマーケットプレイス大幅拡充が発表されました。

📌 **ピックアップ**
• SageMaker: 推論エンドポイントのリアルタイム監視機能が追加
• Devin: GitLab連携強化と48以上のMCPコネクタが利用可能に
• AWS: EKSのVPC内ルーティングやソウルリージョンのSMS送信に対応

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-21*
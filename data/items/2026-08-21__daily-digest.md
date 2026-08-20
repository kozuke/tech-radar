# Tech Radar Daily Digest - 2026-08-21

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Amazon EKSの証明書管理が自動化**
Amazon EKSで、クラスターの証明書（CA）ローテーションを管理されたライフサイクル内で自動的に実行可能になりました。これまで手動対応が必要だったCA更新プロセスが、AWSによる自動通知や後継CAの自動追加、ロールバック機能の提供により、運用負荷が大幅に軽減されます。特に2018年のサービス開始当初から運用されているクラスターはCAの有効期限が近づいており、今回の機能追加は長期運用におけるセキュリティと可用性維持の観点で極めて重要です。

**SageMaker AI Studioで生成AIの推論構成を最適化**
Amazon SageMaker AI Studioに「Generative AI Inference Recommendation」が統合されました。これにより、開発者はコードを書くことなく、レイテンシ、スループット、コストなどの目標に合わせて最適なインスタンスや最適化手法（推論構成）を自動的にベンチマーク・選定できるようになります。従来、数週間を要していた手動のチューニング作業が数時間に短縮され、本番環境へのデプロイまでのリードタイムが劇的に改善されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic
##### Claude Code v2.1.238 / v2.1.237
Claude Codeの最新リリースでは、Bash風のキーバインド設定や、プラグインマーケットプレイスでのヘッダー管理機能が追加されました。また、回答の簡潔さを重視する「Concise」出力スタイルが導入され、ユーザーの好みに合わせた対話体験が可能になっています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | キーバインドのカスタマイズ、メモリリークの修正、出力スタイルの制御 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.238

---

#### OpenAI Codex CLI
##### Codex CLI v0.149.0
Codex CLIのメジャーアップデートにより、タスク管理用のインタラクティブダッシュボードや、作業ディレクトリ管理コマンド（/cd, /pwd等）が追加されました。また、ネットワークやプロキシ環境の診断機能「codex doctor」が強化され、トラブルシューティングが容易になっています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Codex CLI (Rust) |
| 特徴・性能 | TUIの操作性向上、Vimキーバインドの拡充、診断機能の強化 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.149.0

---

#### Devin
##### Devin リリースノート（2026-08-19）
DevinのUltraセッションにおいて、モデルの劣化や回復を通知する機能が追加されました。また、UIの改善として「Preview」タブの「Browser」への名称変更や、PRタブの高速化、Slack連携の強化など、開発体験を向上させる細かなアップデートが多数行われています。

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-08-19-model-degradation-notifications

---

### クラウド

#### AWS
##### Amazon CloudFront: S3 Multi-Region Access PointsのOAC対応
CloudFrontがS3 Multi-Region Access Points (MRAP) に対するOrigin Access Control (OAC) をサポートしました。これにより、カスタムLambda@Edge関数を介さず、ネイティブな設定のみでグローバルなS3バケットへのアクセスをセキュアに制限できるようになり、パフォーマンスとセキュリティが向上します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudfront-oac-s3-mrap

---

##### AWS Direct Connect: インバウンドプレフィックス制御の導入
Direct Connectにおいて、VIFごとのインバウンドルートプレフィックス割り当てを管理する機能が導入されました。最大1,000プレフィックスまで割り当て可能となり、大規模ネットワークのルーティング設計が柔軟になりました。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/aws-direct-connect-new-prefix-controls

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| EKSクラスターのCA有効期限確認とローテーション計画の策定 | EKS管理者 | 🔴 高 |
| SageMaker AIでの推論最適化の試行 | AIエンジニア | 🟡 中 |
| Claude Code / Codex CLIのアップデート適用 | 開発者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EKS CA rotation | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-certificate-authority-ca-rotation-automated-lifecycle-management) |
| CloudFront OAC for S3 MRAP | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudfront-oac-s3-mrap) |
| SageMaker Inference Recommendation | AI/LLM | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/08/generative-ai-inference-recommendation-for-amazon-sagemaker-now-available-in-the-sagemaker-ai-studio) |
| Direct Connect Prefix Controls | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-direct-connect-new-prefix-controls) |
| Claude Code v2.1.238 | AI/LLM | Anthropic | [URL](https://github.com/anthropics/claude-code/releases/tag/v2.1.238) |
| Codex CLI v0.149.0 | AI/LLM | OpenAI | [URL](https://github.com/openai/codex/releases/tag/rust-v0.149.0) |
| Devin Release Notes | AI/LLM | Cognition | [URL](https://docs.devin.ai/release-notes/overview#2026-08-19-model-degradation-notifications) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
Amazon EKSのCAローテーション自動化と、SageMaker AIでの推論構成最適化機能がリリースされました。

📌 **ピックアップ**
• EKS: 証明書管理の自動化により運用負荷を大幅軽減
• SageMaker: 生成AIモデルの推論構成をノーコードで最適化
• CLIツール: Claude CodeとCodex CLIが機能強化され操作性が向上

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-08-21*
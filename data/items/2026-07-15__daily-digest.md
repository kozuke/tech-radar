# Tech Radar Daily Digest - 2026-07-15

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは、Pixel 10シリーズ向けに最適化されたオンデバイスAI技術を公開しました。カスタムSoC「Google Tensor」と最新のTPUを活用することで、インターネット接続なしで動作する「Gemma 4 E2B」モデルや、音声・テキストでスマホの機能を直接操作する「Mobile Actions」を実現しています。この技術は、プライバシーを完全に保護しながら、オフライン環境での高度な推論や画像認識を可能にするもので、エッジAIの新たなスタンダードとなることが期待されます。

また、AWSはAIワークロードのセキュリティを強化する「Amazon GuardDuty AI Protection」を発表しました。Amazon BedrockやSageMakerを標的としたプロンプトインジェクションや、リソースを過剰消費させるコストハーベスティング攻撃などを自動検知します。AI導入が加速する中で、手動設定なしでAI特有の脅威を可視化できる点は、エンタープライズ環境におけるAI運用の安全性向上に大きく寄与するでしょう。

---

## 📰 今日のニュース

### AI/LLM

#### Google
##### Systems Engineering Playbook: Qwen 3.5-397Bの最適化

Googleは、Qwen 3.5-397B MoEモデルをTPU v7x（Ironwood）上で効率的に動作させるためのエンジニアリング手法を公開しました。モデルをモジュール化し、再利用可能なカーネルを活用することで、推論性能をデコード重視で約3.1倍、プリフィル重視で約4.7倍向上させています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | MoE (Mixture-of-Experts), JAX/Pallas, vLLM, SGLang |
| 特徴・性能 | 推論性能を最大4.7倍向上、17Bパラメータの動的アクティブ化 |
| 対応環境 | TPU v7x (Ironwood) |

> 🔗 **参考リンク**
> https://developers.googleblog.com/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/

---

#### Claude Code
##### v2.1.208 / v2.1.209 リリース

Claude Codeの最新アップデートでは、スクリーンリーダー対応モードの追加や、Vimモードでのキーマッピング設定など、開発者の生産性を高める機能が多数追加されました。また、バックグラウンドセッションの安定性向上や、大規模なMarkdownテーブルのレンダリング最適化など、UI/UXの改善も行われています。

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.208

---

### クラウド

#### AWS
##### AWS Elastic Disaster RecoveryのEBS初期化レート対応

AWS DRSがAmazon EBSボリュームの初期化レート設定をサポートしました。これにより、DR時のボリューム復旧速度を予測可能にし、データベースなどのI/O負荷が高いワークロードのリカバリタイム目標（RTO）達成を支援します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-hydration/

##### AWS Lambdaコンソールでのコーディングエージェント設定

AWS Lambdaコンソールに、コーディングエージェントをワンクリックでセットアップできるプロンプトが追加されました。AWS ServerlessスキルやMCPサーバーを自動構成することで、開発者は環境構築の摩擦を減らし、即座にサーバーレス開発を開始できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-prompt-coding-agents/

---

### Workspace

#### Google Workspace
##### Gmail「Help me write」のカスタムリファイン機能

Gmailの「Help me write」機能が強化され、プリセット以外の指示を自由に入力してドラフトを修正できるようになりました。ユーザーは「締め切りを追加して」といった具体的な指示をプロンプトバーに入力するだけで、即座にメールの内容を調整可能です。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/new-refinement-capabilities-allow-custom-editing-with-Help-me-write-in-Gmail.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| GuardDuty AI Protectionの有効化 | セキュリティ管理者 | 🔴 高 |
| Lambda開発環境のMCP設定確認 | サーバーレス開発者 | 🟡 中 |
| Google Meetハードウェアのフィードバック確認 | IT管理者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Elastic Disaster Recovery... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-hydration/ |
| AWS Lambda console... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-prompt-coding-agents/ |
| Amazon GuardDuty AI Protection... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-guardduty-ai-protection-aws/ |
| Systems Engineering Playbook... | AI/LLM | Google | https://developers.googleblog.com/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/ |
| Unlocking the Next Era... | AI/LLM | Google | https://developers.googleblog.com/unlocking-the-next-era-of-on-device-ai-with-google-tensor-and-pixel/ |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

GoogleがPixel 10向けオンデバイスAI技術を公開、AWSはAIワークロード向け脅威検知を発表。

📌 **ピックアップ**
• Google: Qwen 3.5 MoEのTPU最適化で推論性能が最大4.7倍に向上。
• AWS: GuardDutyがAIサービス（Bedrock等）の脅威検知に対応。
• Claude Code: スクリーンリーダー対応やVimモード強化など大幅アップデート。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-15*
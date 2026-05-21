# Tech Radar Daily Digest - 2026-05-22

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは、AIエージェント開発を加速させる「Agent Development Kit (ADK)」のKotlin版およびAndroid版（v0.1.0）をリリースしました。このフレームワークは、クラウド上のLLMと、Android端末上の「Gemini Nano」などのオンデバイスモデルをシームレスに連携させるハイブリッドなAIエージェント構築を可能にします。特に、プライバシーを重視するデータ処理をローカルで完結させつつ、複雑なタスクをクラウドでオーケストレーションする柔軟なアーキテクチャを実現しており、モバイルアプリ開発におけるAI実装のハードルを大幅に下げることが期待されます。

また、AWSは「Amazon SageMaker AI」においてOpenAI互換APIのサポートを開始しました。これにより、既存のOpenAI SDKやLangChainなどのツールを利用している開発者は、コードを書き換えることなく、エンドポイントURLを変更するだけでSageMakerの推論環境へ移行可能です。自社VPC内でのデータ管理や、ファインチューニング済みモデルの活用が容易になるため、エンタープライズ環境での生成AI導入がさらに加速するでしょう。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / SDK

##### Claude Code v2.1.147 / v2.1.146
マルチエージェントオーケストレーションを可能にする「Workflow」ツールの追加や、コードレビュー機能（旧simplify）の強化が行われました。また、Windows環境でのPowerShellツール動作の安定化や、大規模ファイル編集時のdiffレンダリング性能が向上しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, TypeScript |
| 特徴・性能 | 確定的なマルチエージェント制御、diff描画最適化 |
| 対応環境 | Windows, macOS, Linux |
| 関連サービス | GitHub, Anthropic API |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.147

##### Anthropic Python SDK v0.104.0
ストリーミング時の思考プロセス（thinking block）におけるトークン消費量を推定する「thinking-token-count」ベータ機能が追加されました。これにより、コスト管理やレスポンスの最適化がより精密に行えるようになります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Python SDK |
| 特徴・性能 | 思考トークン数の推定サポート |
| 対応環境 | Python 3.x |
| 関連サービス | Claude API |

> 🔗 **参考リンク**
> https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.104.0

#### OpenAI / Codex CLI

##### Codex CLI v0.133.0
ゴール管理機能がデフォルトで有効化され、複数ターンにわたる進捗追跡が可能になりました。また、プラグインの発見・管理機能が強化され、より高度なエージェント拡張が容易になっています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Rust, CLI |
| 特徴・性能 | ゴール追跡、プラグインエコシステムの拡張 |
| 対応環境 | Linux, Windows, macOS |
| 関連サービス | OpenAI API |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.133.0

#### Google / Gemini

##### Gemini for Home の機能拡充
Google Homeプラットフォームにおいて、カメラのインテリジェンス向上や「Ask Home」による家庭内データの検索機能が強化されました。ハードウェアパートナー向けには、AI搭載デバイスを迅速に開発できるリファレンスデザインプログラムが提供されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Gemini, Google Home API |
| 特徴・性能 | カメラ映像の文脈理解、家庭内センサーデータの要約 |
| 対応環境 | Google Homeエコシステム |
| 関連サービス | Google Cloud, Gemini Nano |

> 🔗 **参考リンク**
> https://developers.googleblog.com/empowering-service-providers-and-hardware-partners-with-gemini-for-home/

---

### クラウド

#### AWS

##### Amazon EC2 インスタンスの拡充（Hyderabadリージョン）
インドのHyderabadリージョンにて、第4世代Intel Xeon Scalableプロセッサを搭載したC7i-flex、M7i-flex、M7iインスタンスが利用可能になりました。既存のx86ベースインスタンスと比較して最大15〜19%の価格性能比向上が見込まれます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon EC2, Intel Sapphire Rapids |
| 特徴・性能 | 最大19%の価格性能比向上 |
| 対応環境 | AWS Asia Pacific (Hyderabad) |
| 関連サービス | Amazon EC2 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ec2-c7i-flex-m7i-flex-m7i-instances-HYD-region/

##### SageMaker Unified Studio の機能強化
Glueジョブのサブネット間リトライ機能が自動化されました。これにより、特定のサブネットやAZで障害が発生した際、手動介入なしで別のサブネットでジョブを再実行でき、データパイプラインの耐障害性が向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Glue, Amazon SageMaker |
| 特徴・性能 | 自動コネクタプロビジョニングによるリトライ耐性 |
| 対応環境 | AWS全リージョン |
| 関連サービス | AWS Glue, VPC |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/sagemaker-unified-studio-glue/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| SageMaker推論エンドポイントのOpenAI互換API移行検討 | AIエンジニア | 🔴 高 |
| AndroidアプリへのADK導入によるオンデバイスAI検討 | モバイル開発者 | 🟡 中 |
| Claude CodeのアップデートとWorkflow機能のテスト | 開発者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EC2 C7i-flex... | クラウド | aws_whats_new | https://aws.amazon.com/... |
| SageMaker Unified Studio... | クラウド | aws_whats_new | https://aws.amazon.com/... |
| Amazon SageMaker AI now supports OpenAI-compatible APIs | AI/LLM | aws_whats_new | https://aws.amazon.com/... |
| v2.1.147 (Claude Code) | AI/LLM | claude_code | https://github.com/... |
| v2.1.146 (Claude Code) | AI/LLM | claude_code | https://github.com/... |
| 0.133.0 (Codex) | AI/LLM | openai_codex | https://github.com/... |
| 0.133.0-alpha.4 (Codex) | AI/LLM | openai_codex | https://github.com/... |
| Empowering Service Providers... | AI/LLM | google_dev | https://developers.googleblog.com/... |
| Announcing ADK for Kotlin... | AI/LLM | google_dev | https://developers.googleblog.com/... |
| v0.104.0 (Anthropic SDK) | AI/LLM | anthropic_sdk | https://github.com/... |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

GoogleがKotlin/Android向けAIエージェント開発キット(ADK)を公開し、AWS SageMakerがOpenAI互換APIに対応しました。

📌 **ピックアップ**
• Google ADK: クラウドとオンデバイス(Gemini Nano)のハイブリッドAI構築が可能に
• AWS SageMaker: OpenAI SDKから直接接続可能になり、移行コストが大幅低減
• Claude Code: マルチエージェント制御機能「Workflow」が追加

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-22*
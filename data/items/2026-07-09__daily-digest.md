# Tech Radar Daily Digest - 2026-07-09

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AWSが「Network Scanning」を導入し、公開リソースの可視化を強化**
AWS Security Hubに新たに「Network Scanning」機能が追加されました。これは、セキュリティグループやルートテーブルの設定ベースの推測ではなく、実際にインターネットから対象リソースへプローブを送信することで、公開されているIPアドレス、仮想マシン、ロードバランサーを特定するものです。この機能により、意図せず公開状態になっているリソースを正確に検出し、リスクを可視化することが可能になります。既存のネットワーク到達可能性の分析と組み合わせることで、より強固なセキュリティ体制の構築が期待されます。

**Googleが「Google Vids」の多言語対応を拡大**
Google SlidesのコンテンツをAI生成のスクリプトや音声、アニメーションを用いて動画化する「Google Vids」が、新たに7言語（日本語、フランス語、ドイツ語、イタリア語、韓国語、ポルトガル語、スペイン語）に対応しました。これまで英語のみに限定されていたAI動画生成機能が主要言語に広がったことで、グローバルなビジネス環境や教育現場でのプレゼンテーション作成の効率化が大きく進む見込みです。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.205 / v2.1.204 リリース

Claude Codeの最新アップデートでは、自動モードの安全性向上や多数のバグ修正が行われました。特に、セッションスクリプトファイルへの不正な改ざんを防ぐルールや、メモリ使用量を大幅に削減するストリーミング方式への変更など、開発体験と安定性が強化されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code (Anthropic) |
| 特徴・性能 | メモリ使用量400MB削減、Windows環境の安定性向上 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.205

#### OpenAI Codex CLI

##### v0.143.0 およびアルファ版リリース

Codex CLIの最新版では、リモートプラグインのデフォルト有効化や、macOS/Windowsのシステムプロキシ対応が実施されました。また、Amazon Bedrock経由での最新モデル（Sol, Terra, Luna）への対応など、エンタープライズ利用を意識した機能強化が目立ちます。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| リモートプラグイン | デフォルトで有効化され、npmソースやバージョン管理が強化。 |
| システムプロキシ | macOS/WindowsのPAC/WPAD設定を介した通信が可能に。 |
| モデル対応 | Amazon BedrockのGPT-5.6シリーズ（Sol, Terra, Luna）をサポート。 |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.143.0

#### Google Gemini

##### AI Race Coachの構築事例

Google Developer Expertsが、AntigravityとGeminiを活用してリアルタイムのAIレースコーチを開発しました。物理演算とリアルタイムのテレメトリデータを組み合わせることで、ドライバーに対してコンマ1秒を削るための具体的なアドバイスを提示する「Trustable AI」の構築に成功しています。

> 🔗 **参考リンク**
> https://developers.googleblog.com/bridging-the-domain-gap-ai-race-coach-built-with-antigravity-and-gemini/

---

### クラウド

#### AWS

##### AWS Builder Centerの無料サンドボックス環境

AWS Builder Centerにおいて、個人アカウントやクレジットカードなしで利用可能な無料のサンドボックス環境が提供開始されました。ワークショップ受講者は8時間限定でAWSリソースを自由に試用でき、学習のハードルが大幅に下がります。

##### Amazon Redshift RGインスタンスの「trailing track」対応

RedshiftのGravitonベースRGインスタンスが、安定性を重視する「trailing track (P201)」で利用可能になりました。RA3インスタンスと比較して最大2.4倍のクエリ性能と30%のコスト削減を実現します。

##### Amazon Aurora DSQLのCDC機能がGA

Aurora DSQLの変更データキャプチャ（CDC）機能が一般提供開始されました。データベースの変更をAmazon Kinesis Data Streamsへリアルタイムにストリーミング可能となり、イベント駆動型アーキテクチャの構築が容易になります。

##### Amazon Connectのタスク・メール対応

Amazon Connectにおいて、音声だけでなくタスクやメールを含めた統合的な予測・計画・スケジューリングが可能になりました。全チャネルを横断した効率的なエージェント配置が実現します。

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| AWS Security HubでNetwork Scanningを有効化する | セキュリティ担当者 | 🔴 高 |
| Claude Codeをv2.1.205へアップデートする | 開発者 | 🟡 中 |
| Google Vidsの多言語対応を確認する | コンテンツ作成者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Builder Center Now Offers Free Sandbox Environments | AWS | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-builder-center-sandbox/) |
| AWS Security Hub now offers Network Scanning | AWS | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-network-scanning/) |
| Amazon Redshift RG instances now available on the trailing track | AWS | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-graviton-rg-instances-trailing-track) |
| Amazon Aurora DSQL change data capture (CDC) Is now generally available | AWS | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-aurora-dsql-cdc-ga/) |
| Amazon Connect Customer now supports forecasting... | AWS | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-connect-customer-agent-scheduling-tasks/) |
| v2.1.205 | Claude Code | GitHub | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.205) |
| v2.1.204 | Claude Code | GitHub | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.204) |
| rust-v0.144.0-alpha.3 | Codex CLI | GitHub | [link](https://github.com/openai/codex/releases/tag/rust-v0.144.0-alpha.3) |
| 0.144.0-alpha.2 | Codex CLI | GitHub | [link](https://github.com/openai/codex/releases/tag/rust-v0.144.0-alpha.2) |
| 0.144.0-alpha.1 | Codex CLI | GitHub | [link](https://github.com/openai/codex/releases/tag/rust-v0.144.0-alpha.1) |
| 0.143.0 | Codex CLI | GitHub | [link](https://github.com/openai/codex/releases/tag/rust-v0.143.0) |
| Bridging the Domain Gap: AI Race Coach | AI | Google | [link](https://developers.googleblog.com/bridging-the-domain-gap-ai-race-coach-built-with-antigravity-and-gemini/) |
| Convert your Google Slides to videos in 7 additional languages | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/07/convert-your-google-slides-to-videos-in-7-additional-languages.html) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWS Security Hubが公開リソースを自動検出する「Network Scanning」を導入しました。

📌 **ピックアップ**
• AWS: セキュリティ可視化機能の強化とRedshift/Auroraの機能拡充
• AI: Claude Codeの安定性向上とCodex CLIの最新版リリース
• Workspace: Google Vidsが日本語を含む7言語に対応

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-09*
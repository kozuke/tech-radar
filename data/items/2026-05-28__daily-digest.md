# Tech Radar Daily Digest - 2026-05-28

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは「Google I/O」にて、AI時代を見据えたGoogle Payの進化と、開発者向けの新たなAI統合ツールを発表しました。既存の決済インフラを維持しつつ、AIエージェントが商取引を支援する「Universal Commerce Protocol (UCP)」への対応や、開発環境に直接統合可能な「Google Pay & Wallet Developer MCPサーバー」の公開が大きな柱です。これにより、開発者は既存のバックエンドを活かしながら、AIエージェントによるトラブルシューティングやコード生成、トレンド分析を効率化できるようになります。

また、Google WorkspaceにおいてもAI活用が加速しています。Google Meetでは「Ask Gemini」のアクセス性が向上し、サイドパネルがより使いやすい位置へ配置されました。さらに、Connected SheetsではBigQuery MLとTimesFMを活用した「異常検知機能」が追加され、SQLの知識がなくても時系列データの外れ値を自動的に特定可能となりました。これらのアップデートは、AIを単なるチャットボットとしてではなく、業務フローやデータ分析の基盤に深く組み込むというGoogleの戦略を明確に示しています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.152

Claude Codeの最新アップデートでは、コードレビュー機能が強化され、修正提案を直接ワーキングツリーに適用可能になりました。また、セッション開始時のフック機能やプラグインマーケットプレイスの管理設定が拡充され、開発者のワークフローに合わせた柔軟なカスタマイズが容易になっています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | コードレビューの自動適用、セッション管理の柔軟性向上 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.152

---

#### OpenAI Codex

##### 0.135.0-alpha.1 / 0.135.0-alpha.2

OpenAIのCodex CLIに関するプレリリース版が公開されました。詳細な変更ログは現在確認できませんが、継続的な改善が行われています。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.135.0-alpha.2

---

### クラウド

#### AWS

##### SageMaker Notebook Instancesのインスタンスタイプ拡充

SageMaker Notebook Instancesにおいて、P5.4xlおよびP5en.48xlインスタンスが利用可能になりました。H100およびH200 GPUを搭載したこれらのインスタンスは、大規模言語モデル（LLM）の学習や推論、HPCアプリケーションのパフォーマンスを大幅に向上させます。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| P5.4xl | NVIDIA H100 GPUを搭載し、従来のGPUインスタンス比で最大4倍の高速化と40%のコスト削減を実現。 |
| P5en.48xl | H200 GPUと第4世代Intel Xeonを搭載し、メモリ帯域とCPU-GPU間通信を強化、レイテンシを最大35%改善。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon SageMaker, NVIDIA H100/H200 |
| 特徴・性能 | LLM学習/推論の高速化、高帯域通信 |
| 対応環境 | AWS各リージョン（東京含む） |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/03/p5-4xl-new-instance-launch-sagemaker-notebook-instances/

##### Amazon EMRでApache Spark 4.0.2をサポート

Amazon EMRがApache Spark 4.0.2の一般提供を開始しました。ANSI SQLのサポート強化やVARIANTデータ型の導入により、データエンジニアリングのアクセシビリティが向上し、Apache Iceberg v3による強固なトランザクション管理と監査機能が提供されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Apache Spark 4.0.2, Apache Iceberg v3 |
| 特徴・性能 | ANSI SQLサポート、FGAC（細粒度アクセス制御） |
| 関連サービス | AWS Lake Formation |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-emr-apache-spark/

---

### Workspace

#### Google Workspace

##### Google MeetおよびConnected Sheetsのアップデート

Google Meetの「Ask Gemini」がUI改善によりアクセスしやすくなり、Connected SheetsではBigQueryデータを対象としたAI異常検知機能が利用可能になりました。また、Workspace Studioに対して管理者がステップやスターター単位で利用制限をかけられる詳細な制御機能が追加されました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Ask Gemini in Meet | プロンプトボックスを画面左下に移動し、発見性と操作性を向上。 |
| 異常検知 (Connected Sheets) | BigQuery MLとTimesFMを活用し、SQL不要で時系列データから外れ値を自動抽出。 |
| Workspace Studio管理 | 管理者が組織単位やグループ単位でStudioの各機能を有効/無効化可能に。 |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/05/ask-gemini-in-google-meet-is-becoming-more-easily-accessible-on-web.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| 大規模モデル学習環境のP5/P5enへの移行検討 | MLエンジニア | 🟡 中 |
| EMR環境のSpark 4.0.2へのアップグレード検証 | データエンジニア | 🟡 中 |
| Workspace Studioの機能制限設定の確認 | 管理者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| SageMaker Notebook Instances now support P5.4xl | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/03/p5-4xl-new-instance-launch-sagemaker-notebook-instances/) |
| SageMaker Notebook Instances now support P5en.48xl | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/02/p5en-new-instance-launch-sagemaker-notebook-instances/) |
| Amazon EMR now supports Apache Spark 4.0.2 | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-emr-apache-spark/) |
| v2.1.152 | AI/LLM | Claude | [URL](https://github.com/anthropics/claude-code/releases/tag/v2.1.152) |
| 0.135.0-alpha.2 | AI/LLM | OpenAI | [URL](https://github.com/openai/codex/releases/tag/rust-v0.135.0-alpha.2) |
| 0.135.0-alpha.1 | AI/LLM | OpenAI | [URL](https://github.com/openai/codex/releases/tag/rust-v0.135.0-alpha.1) |
| The latest updates to Google Pay | AI/LLM | Google | [URL](https://developers.googleblog.com/the-latest-updates-to-google-pay/) |
| Ask Gemini in Google Meet accessibility | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/05/ask-gemini-in-google-meet-is-becoming-more-easily-accessible-on-web.html) |
| Anomaly detection in Connected Sheets | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/05/easily-identify-data-irregularities-with-anomaly-detection-in-Connected-Sheets.html) |
| Granular admin controls for Workspace Studio | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/05/more-granular-admin-controls-for-Workspace-Studio-steps-and-starters.html) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

GoogleがAIエージェント時代の商取引基盤「Universal Commerce Protocol」を発表し、WorkspaceでもAI活用が大幅強化されました。

📌 **ピックアップ**
• AWS: SageMakerでH100/H200搭載のP5インスタンスが利用可能に
• Claude Code: コードレビュー修正の自動適用など機能拡充
• Google: SheetsでのAI異常検知やMeetのUI改善などWorkspace機能が進化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-28*
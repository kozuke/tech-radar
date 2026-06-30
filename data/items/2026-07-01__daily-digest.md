# Tech Radar Daily Digest - 2026-07-01

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Anthropicは、次世代モデル「Claude Sonnet 5」を発表し、同社のコーディングエージェント「Claude Code」のデフォルトモデルとして採用しました。このモデルは100万トークンのコンテキストウィンドウをネイティブでサポートし、8月31日までの期間限定でプロモーション価格（$2/$10 per Mtok）が適用されます。また、Googleは「ADK for Go 2.0」をリリースし、グラフベースのワークフローエンジンや人間による介入（Human-in-the-loop）機能を導入しました。これらの動きは、AIエージェントの構築において、より複雑な推論と信頼性の高いワークフロー管理が標準化されつつあることを示しています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic

##### Claude Code v2.1.197 / v2.1.196

Claude Codeの最新アップデートにより、デフォルトモデルが「Claude Sonnet 5」に変更されました。また、組織単位でのデフォルトモデル設定、チャット内でのファイル添付機能の強化、セキュリティの改善（MCPサーバーの承認フロー見直し）など、開発者の生産性と安全性を高める多数の機能が追加されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| モデル更新 | Claude Sonnet 5をデフォルト採用し、1Mトークンのコンテキストに対応。 |
| 組織設定 | 管理者が組織ごとのデフォルトモデルを指定可能に。 |
| セキュリティ | 信頼されていないワークスペースでのMCPサーバー自動実行を制限。 |
| UX改善 | チャットへのファイル添付、セッション名の自動生成、サイドパネルの安定性向上。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Sonnet 5, MCP (Model Context Protocol) |
| 特徴・性能 | 1Mトークンコンテキスト, プロモーション価格適用 |
| 対応環境 | CLIツール (claude-code) |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.197

---

#### Gemini / Google

##### ADK Go 2.0 リリース

Googleは、Go言語で信頼性の高いマルチエージェントアプリケーションを構築するための「ADK Go 2.0」を公開しました。グラフベースのワークフローエンジンにより、複雑なエージェントの分岐やループ、人間による承認プロセスを直感的に記述・管理できるようになりました。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Go言語, グラフベースワークフローエンジン |
| 特徴・性能 | 人間介入(HITL)の組み込み, 動的オーケストレーション |
| 関連サービス | Gemini Enterprise Agent Platform |

> 🔗 **参考リンク**
> https://developers.googleblog.com/announcing-adk-go-20/

---

### クラウド

#### AWS

##### AWS CloudFormation / CDK の機能強化

AWSは、CloudFormationおよびCDKにおいて、デプロイ前のバリデーション機能と「Expressモード」を導入しました。これにより、設定ミスを即座に検知し、インフラ構築時の待機時間を最大4倍短縮することで、開発者のフィードバックループを大幅に加速させます。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| プリデプロイ検証 | スタック操作時に共通のデプロイエラーを即座に検知。 |
| Expressモード | リソースの安定化待機をスキップし、設定適用完了時点でデプロイを終了。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS CloudFormation, AWS CDK |
| 特徴・性能 | デプロイ時間最大4倍高速化, 警告機能の拡充 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation-cdk/

---

### Workspace

#### Google Workspace

##### Gemini in Drive / Slides のモバイル対応強化

Googleは、DriveのAI OverviewsやAsk Gemini機能をモバイルアプリで提供開始しました。また、Google Slidesではプロンプトからプレゼンテーションを生成・編集可能になり、Gmailではモバイル端末から委任アカウントの管理が可能になるなど、モバイル環境での生産性が大幅に向上しています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| AI Overviews (Drive) | 検索結果のトップにAIによる要約を表示。 |
| Ask Gemini (Drive) | 複数ファイルにまたがる対話型分析をモバイルで実現。 |
| Gemini in Slides | プロンプトからネイティブ編集可能なスライドを生成。 |
| Gmail委任 | モバイルアプリから委任されたアカウントのメール管理が可能に。 |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/ai-overviews-in-drive-now-available-on-mobile.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude Codeをv2.1.197にアップデート | 開発者 | 🔴 高 |
| CloudFormation Expressモードの検証 | インフラエンジニア | 🟡 中 |
| ADK Go 2.0でのエージェント設計検討 | Go開発者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon CloudWatch Logs enriches log events... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cloudwatch-logs-resource-tags/ |
| AWS CloudFormation and CDK accelerate... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation/ |
| AWS CloudFormation and CDK express mode... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation-cdk/ |
| Amazon RDS Enhances IAM Database Authentication... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-rds-iam/ |
| AWS Parallel Computing Service supports... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/aws-parallel-computing-service-upgrade/ |
| v2.1.197 (Claude Code) | AI/LLM | Anthropic | https://github.com/anthropics/claude-code/releases/tag/v2.1.197 |
| v2.1.196 (Claude Code) | AI/LLM | Anthropic | https://github.com/anthropics/claude-code/releases/tag/v2.1.196 |
| Driving the Agent Quality Flywheel... | AI/LLM | Google | https://developers.googleblog.com/driving-the-agent-quality-flywheel-from-your-coding-agent/ |
| Build reliable multi-agent applications... | AI/LLM | Google | https://developers.googleblog.com/announcing-adk-go-20/ |
| AI Overviews in Drive now available on mobile | Workspace | Google | http://workspaceupdates.googleblog.com/2026/06/ai-overviews-in-drive-now-available-on-mobile.html |
| Work with delegated Gmail accounts... | Workspace | Google | http://workspaceupdates.googleblog.com/2026/06/work-with-delegated-gmail-accounts-from-mobile-devices.html |
| Ask Gemini in Drive now available on mobile | Workspace | Google | http://workspaceupdates.googleblog.com/2026/06/ask-gemini-in-drive-now-available-on-mobile.html |
| Create fully native and editable presentations... | Workspace | Google | http://workspaceupdates.googleblog.com/2026/06/create-fully-native-and-editable-presentations-with-Gemini-in-Google-Slides.html |
| v0.115.0 (Anthropic SDK) | AI/LLM | Anthropic | https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.115.0 |
| v0.114.0 (Anthropic SDK) | AI/LLM | Anthropic | https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.114.0 |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Anthropicが「Claude Sonnet 5」を発表し、Claude Codeのデフォルトモデルとして採用を開始。

📌 **ピックアップ**
• Claude Codeがアップデート、1Mトークン対応とセキュリティ強化。
• Googleが「ADK Go 2.0」をリリース、グラフベースのマルチエージェント構築を支援。
• AWS CloudFormationがデプロイ高速化と事前検証機能を強化。
• Google WorkspaceのGemini機能がモバイルアプリで大幅拡充。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-01*
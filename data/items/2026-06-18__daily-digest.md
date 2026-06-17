# Tech Radar Daily Digest - 2026-06-18

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AIエージェントの進化が加速しており、特に「エージェント間の連携」と「開発環境のクラウド移行」が大きな転換点を迎えています。Googleが発表した「Agentic Resource Discovery (ARD)」は、組織の境界を超えてAIエージェントがツールやスキルを安全に発見・検証するための標準仕様であり、エージェントエコシステムの相互運用性を高める重要な一歩です。

一方、CursorやDevinといった主要なAIエージェント開発ツールでは、クラウド環境の活用が標準化されています。Cursorはクラウド環境のセットアップを10分以内に短縮し、ローカル環境を汚さずに並列でタスクを処理する「クラウドサブエージェント」機能を強化しました。これらの動きは、AIエージェントが単なるコード生成ツールから、自律的に環境を構築・検証し、複雑なワークフローを完結させる「実行主体」へと進化していることを示しています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code, OpenAI, Google, Devin, Cursor

##### Claude Code v2.1.181 リリース
Claude Codeの最新版では、プロンプトから設定を変更できる `/config` コマンドや、macOSでのApple Events権限の追加など、操作性と環境適応性が向上しました。特に、API接続の自動リトライ機能や、長文ストリーミングの表示改善により、開発者の体験がよりスムーズになっています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| /config コマンド | プロンプトから直接設定値（thinking=false等）を変更可能に。 |
| サンドボックス設定 | `sandbox.allowAppleEvents` によりmacOSでの外部連携を制御可能。 |
| 接続安定化 | API接続切断時の自動リトライ機能を追加。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Bun runtime 1.4, MCP |
| 特徴・性能 | 起動時の設定取得待ちを最適化し、レスポンスを改善 |
| 対応環境 | macOS, Linux, Windows |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.181

---

##### Cursor: クラウドエージェント機能の強化
Cursorは、クラウド環境のセットアップを10分以内に完了させる機能や、ローカルとクラウド間でのセッションハンドオフを導入しました。`/in-cloud` コマンドにより、ローカル環境を維持したまま、独立したVM上で並列的にタスクを実行することが可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | クラウドVM, 共有ターミナル |
| 特徴・性能 | 環境スナップショットによる高速起動と並列処理 |
| 関連サービス | .cursor/environment.json |

> 🔗 **参考リンク**
> https://cursor.com/changelog#2026-06-17-this-release-introduces-updates-to

---

##### Devin: プラグインシステムとガバナンス強化
Devin CLIにプラグイン機能が導入され、GitHubやローカルフォルダからスキルセットを共有・インストール可能になりました。また、企業向けにコマンドの許可/拒否リストやプラグインのインストール制限など、高度なガバナンス機能が追加されています。

> 🔗 **参考リンク**
> https://cli.devin.ai/docs/changelog/stable#2026-07-16-plugins

---

### クラウド

#### AWS

##### AWS Glue Interactive SessionsがSpark Connectに対応
AWS Glue Interactive SessionsがApache Spark Connectをサポートし、SageMaker Unified StudioやVS Codeなどの使い慣れたIDEから直接Glueのサーバーレス環境へ接続可能になりました。これにより、ローカル環境とGlue環境の依存関係を分離し、開発効率を向上させます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Apache Spark Connect |
| 特徴・性能 | クライアントと実行環境の分離による安定性向上 |
| 対応環境 | SageMaker Unified Studio, Jupyter, VS Code |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/aws-glue-interactive-sessions-spark-connect-smus-notebooks

---

##### Amazon RDSがGraviton5 (M9g) インスタンスに対応
RDS for PostgreSQL, MySQL, MariaDBでGraviton5ベースのM9gインスタンスが利用可能になりました。前世代と比較して最大30%の性能向上と、最大23%の価格性能比改善を実現しています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-rds-postgresql-mysql-mariadb-m9g-instances/

---

### Workspace

#### Google Workspace

##### Google Vids: AIアバターと動画生成機能の強化
Google Vidsにおいて、Gemini 3.1 FlashとVeo 3.1を活用したAIアバター機能が大幅に強化されました。アバターのプリセット数が53種類に拡大し、24言語への対応や、カスタムアバターへのアクション指示が可能になっています。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/enhanced-ai-avatars-vids.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Cursorのクラウド環境設定（.cursor/environment.json）の導入検討 | 開発者 | 🔴 高 |
| AWS GlueのSpark Connect移行による開発環境の刷新 | データエンジニア | 🟡 中 |
| Google Vidsの新しいAIアバター機能の試用 | コンテンツ制作者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Glue Interactive Sessions... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-glue-interactive-sessions-spark-connect-smus-notebooks) |
| AWS HealthOmics... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-healthomics-real-time-engine-log-streaming/) |
| AWS DevOps Agent... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-devops-agent-release-management/) |
| Amazon RDS... M9g instances | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-rds-postgresql-mysql-mariadb-m9g-instances/) |
| Amazon Aurora... MySQL 5.7... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/rds-mysql-es-extension/) |
| v2.1.181 (Claude Code) | AI/LLM | GitHub | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.181) |
| A2UI + MCP Apps | AI/LLM | Google | [link](https://developers.googleblog.com/a2ui-and-mcp-apps/) |
| Agentic Resource Discovery | AI/LLM | Google | [link](https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/) |
| Custom event colors in Google Calendar | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/06/custom-event-colors-in-google-calendar.html) |
| Enhanced AI avatar... Google Vids | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/06/enhanced-ai-avatars-vids.html) |
| Create longer Veo videos... | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/06/create-longer-veo-videos-and-generate-multiple-at-once-in-Google-Vids.html) |
| Plugins (Devin) | AI/LLM | Devin | [link](https://cli.devin.ai/docs/changelog/stable#2026-07-16-plugins) |
| Cursor Changelog (Jun 17) | AI/LLM | Cursor | [link](https://cursor.com/changelog#2026-06-17-this-release-introduces-updates-to) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AIエージェントのクラウド環境活用が標準化。CursorのクラウドサブエージェントやGoogleのARD仕様策定など、自律的な開発・検証環境が進化しています。

📌 **ピックアップ**
• Cursor: クラウド環境の高速セットアップと並列サブエージェント機能を追加
• AWS: GlueがSpark Connectに対応、RDSがGraviton5(M9g)をサポート
• Google: VidsのAIアバターが大幅強化、ARD仕様でエージェント連携を標準化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-18*
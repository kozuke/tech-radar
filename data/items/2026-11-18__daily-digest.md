# Tech Radar Daily Digest - 2026-11-18

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**GoogleがAndroid開発の高速化とAI統合を大幅に強化**
Googleは、Android開発におけるビルド・同期時間を劇的に短縮する「Another Build File Service (ABFS)」をオープンソースとして公開しました。ABFSは、Linuxカーネルレベルでのファイルシステム最適化とキャッシュ技術により、Androidのビルド時間を約80分から2分強へと短縮し、開発効率を飛躍的に向上させます。また、Google AI Studioでは「Gemini 4 Hydrogen」を活用し、プロンプトからフルスタックのAndroidアプリを生成・デプロイできる環境を構築しました。これにより、データベース設定からPlayストアへの公開までを数分で完結できる、AIエージェント主導の開発ワークフローが実現しました。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic
##### v2.1.327（Claude Code）
Claude Codeの最新版では、GitHubアプリのインストール変更時の確認機能や、トークンをコマンドラインから隠すためのJSON読み込み機能が追加されました。また、リモート制御やセッション管理における不具合修正が行われ、より安定した開発体験を提供します。

##### v2.10.0（Anthropic SDK）
Python SDKのアップデートにより、請求ポリシーのベータサポートや、支出制限到達時のエラーコード追加など、エンタープライズ利用を想定した管理機能が強化されました。

#### OpenAI / Codex
##### 0.170.0（Codex CLI）
Codex CLIのメジャーアップデートでは、TUIでのWebRTC音声通話対応や、OpenTelemetryの認証ヘッダー自動更新機能が追加されました。また、MCPサーバーの環境間分離やWindows環境でのファイル操作の安定性が大幅に向上しています。

#### Google / Gemini
##### Gemini 4 Hydrogen: ロボティクス向けモデル
汎用ロボティクス向けに最適化された「Gemini 4 Hydrogen」が発表されました。Google Antigravityプラットフォームと統合され、ロボットのセットアップから制御コードの生成までをAIが支援する「Robotics plugin」が利用可能になりました。

##### Gemini-powered data classification
Google DriveにおけるAIデータ分類機能が一般提供開始されました。管理者は自然言語で分類ルールを定義でき、リアルタイムでのラベル付け状況の監視や、DLPポリシーとの連携による機密データの保護が可能になります。

#### Devin
##### v3000.13.4（CLI）
Devin CLIの修正版では、モデルストリームのスタックに対するリトライロジックが改善されました。また、Vimモードの操作性向上や、組織切り替えの柔軟性が高められています。

---

### クラウド

#### AWS
##### Amazon EMR 8.2
EMR 8.2はLTSリリースとして、Spark 4.1.3やIceberg 1.11.0を搭載し、ガバナンスとパフォーマンスを強化しました。特にDelta Lakeの同時書き込み対応や、Lake Formationによるきめ細かなアクセス制御が全デプロイオプションで利用可能です。

##### Apache Spark Optimization Agent
EMR Serverless向けに、Sparkジョブのコストとパフォーマンスを分析し、最適化案を自動提示するエージェントが導入されました。設定変更の根拠が平易な言葉で提示され、開発者はインフラやコードの改善を迅速に行えます。

##### AWS Transform (MAP連携)
AWS TransformにMigration Acceleration Program (MAP)のライフサイクル管理機能が統合されました。資格確認からインセンティブ支払いまでをエージェントワークフローで自動化し、パートナーの移行案件推進を加速させます。

##### EC2 C8gn / C8ine インスタンス
Graviton4搭載のC8gnがイスラエルリージョンで、Intel Xeon搭載のC8ineが欧州（アイルランド）リージョンで利用可能になりました。ネットワーク集約型ワークロードにおいて、前世代比で最大43%の性能向上を実現します。

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Android開発環境へのABFS導入検討 | Android開発者 | 🔴 高 |
| EMR Serverlessでの最適化エージェント試用 | データエンジニア | 🟡 中 |
| Google DriveのAI分類ルール設定とテスト | セキュリティ管理者 | 🟡 中 |
| Claude Code / Codex CLIのアップデート | AI開発ツール利用者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EMR 8.2 is now available | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-emr-8.2/) |
| Apache Spark Optimization Agent | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/apache-spark-optimization-agent/) |
| AWS Transform MAP integration | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/map-integration-with-aws-transform/) |
| EC2 C8gn in Israel | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-c8gn/) |
| EC2 C8ine in Ireland | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-c8ine) |
| Claude Code v2.1.327 | AI/LLM | Anthropic | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.327) |
| Codex CLI 0.170.0 | AI/LLM | OpenAI | [link](https://github.com/openai/codex/releases/tag/rust-v0.170.0) |
| ABFS for massive Git repos | 開発ツール | Google | [link](https://developers.googleblog.com/accelerating-development-for-massive-git-repositories/) |
| Gemini 4 Hydrogen Robotics | AI/LLM | Google | [link](https://developers.googleblog.com/gemini-hydrogen-for-robotics/) |
| Full-stack Android with Gemini | AI/LLM | Google | [link](https://developers.googleblog.com/build-full-stack-android-apps-with-gemini-in-google-ai-studio/) |
| Gemini-powered data classification | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/11/gemini-powered-data-classification-in-Google-Drive-is-now-generally-available.html) |
| Anthropic SDK v2.10.0 | AI/LLM | Anthropic | [link](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.10.0) |
| Devin CLI v3000.13.4 | AI/LLM | Cognition | [link](https://cli.devin.ai/docs/changelog/stable#2026-11-17-fixed) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

GoogleがAndroidビルドを劇的に高速化する「ABFS」を公開し、GeminiによるフルスタックAndroidアプリ生成環境を強化しました。

📌 **ピックアップ**
• AWS EMR 8.2リリース：Spark 4.1.3搭載とガバナンス強化
• Gemini 4 Hydrogen：ロボティクス向け高速モデルと開発ツールが登場
• EMR Serverless：Sparkジョブのコスト・性能最適化エージェントが利用可能に
• Google Drive：GeminiによるAIデータ分類機能が一般提供開始

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-18*
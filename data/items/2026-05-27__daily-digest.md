# Tech Radar Daily Digest - 2026-05-27

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AIエージェント開発ツールおよびクラウドインフラのアップデートが目立つ一日となりました。特に注目すべきは、Devin CLIの大型アップデートです。Gemini 3.5 Flashモデルへの対応や、クラウドセッションへのアタッチ機能、MCP（Model Context Protocol）の権限管理強化など、開発者の生産性を直接的に高める機能が多数追加されました。これにより、エージェントとの協調作業がより柔軟かつ効率的になり、特に大規模な開発プロジェクトでの活用が期待されます。

また、AWSではRDSのMulti-AZレプリケーションにおいて「ENA Express」がサポートされました。これにより、可用性を維持しつつネットワークパフォーマンスが大幅に向上し、書き込み負荷の高いデータベースワークロードの遅延が改善されます。インフラの最適化とAI開発ツールの進化が同時に進んでおり、開発環境のモダン化が加速しています。

---

## 📰 今日のニュース

### AI/LLM

#### Devin (Cognition)

##### Devin CLI v2026.5.26-0 リリース

Devin CLIが大幅にアップデートされ、Gemini 3.5 Flashモデルのサポートや、クラウドセッションへのアタッチ機能が追加されました。また、MCPサーバーの権限管理の柔軟性向上や、エディタ連携（Windsurf等）によるコンテキスト共有の強化が行われ、AIエージェントとの開発体験が向上しています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| モデル対応 | Gemini 3.5 Flashモデルをサポート。 |
| セッション管理 | `/cloud-attach` コマンドで既存のクラウドセッションにTUI経由で接続可能に。 |
| MCP強化 | Figma MCPの認証簡略化や、サーバー単位での権限一括承認機能を追加。 |
| エディタ連携 | Windsurf等で開いているファイルやカーソル位置をエージェントが認識可能に。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | MCP (Model Context Protocol), ATIFフォーマット |
| 特徴・性能 | トークン使用量・コストの可視化、コンテキスト圧縮の最適化 |
| 対応環境 | CLI, 各種ターミナル（VS Code, Ghostty, iTerm2等） |

> 🔗 **参考リンク**
> https://cli.devin.ai/docs/changelog/stable#2026-05-26-added

---

#### OpenAI Codex

##### Codex CLI v0.134.0 リリース

Codex CLIの最新版では、ローカルの会話履歴検索機能や、プロファイル管理の刷新が行われました。MCPセットアップの改善や、読み取り専用ツールの並列実行対応など、開発者のワークフローを効率化する機能が拡充されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| 検索機能 | ローカル会話履歴の全文検索とプレビュー表示に対応。 |
| プロファイル管理 | `--profile` をCLIやTUIの主要セレクタとして統一。 |
| MCP改善 | サーバーごとの環境変数設定やOAuthオプションの強化。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Rust, MCP, WebSocket |
| 特徴・性能 | 実行サーバーの再接続信頼性向上、Windows TUIの描画修正 |
| 対応環境 | CLI, Windows/macOS/Linux |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.134.0

---

### クラウド

#### AWS

##### Amazon RDSがMulti-AZレプリケーションでENA Expressをサポート

RDSのMulti-AZ構成において、可用性を損なうことなくネットワークパフォーマンスを最適化する「ENA Express」が利用可能になりました。SRDプロトコルを活用することで、AZ間レプリケーションの帯域幅が最大25Gbpsに向上し、書き込み遅延の変動が抑制されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | ENA Express, AWS SRDプロトコル |
| 特徴・性能 | 最大25Gbpsの単一フロー帯域幅、遅延の安定化 |
| 対応環境 | MariaDB, MySQL, PostgreSQL, Db2, Oracle |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-rds-ena-express-multiAZ/

---

##### AWS GovCloudでM8i/R8iインスタンスを提供開始

Intel Xeon 6プロセッサを搭載した最新の汎用（M8i）およびメモリ最適化（R8i）インスタンスが、AWS GovCloud (US-East)で利用可能になりました。前世代と比較して最大15%の価格性能向上と、2.5倍のメモリ帯域幅を実現しています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ec2-m8i-m8i-flex-govcloud-east/

---

### Workspace

#### Google Workspace

##### Google Chatで「Polly」が利用可能に

Google Chat内でインタラクティブな投票を作成できる「Polly」が統合されました。チームの意思決定を迅速化し、アプリの切り替えによるコンテキストスイッチを減らすことで、ワークフロー内での合意形成をスムーズにします。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/05/simplify-decision-making-with-polly-now-available-for-Google-Chat.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Devin CLIのアップデートと新モデル(Gemini 3.5 Flash)の試用 | AI開発者 | 🔴 高 |
| RDS Multi-AZインスタンスへのENA Express適用検討 | インフラエンジニア | 🟡 中 |
| Google Workspaceの新アイコンデザインの確認 | 全ユーザー | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon RDS now supports ENA Express... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-rds-ena-express-multiAZ/ |
| Amazon EC2 M8i/M8i-flex in GovCloud | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ec2-m8i-m8i-govcloud-east/ |
| Amazon EC2 R8i/R8i-flex in GovCloud | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ec2-r8i-r8i-govcloud-east/ |
| 0.134.0 (Codex CLI) | AI/LLM | OpenAI | https://github.com/openai/codex/releases/tag/rust-v0.134.0 |
| Enhancing Android Checkout with Google Pay | 開発ツール | Google | https://developers.googleblog.com/enhancing-android-checkout-with-dynamic-callbacks-in-google-pay/ |
| Simplify decision-making with Polly | Workspace | Google | http://workspaceupdates.googleblog.com/2026/05/simplify-decision-making-with-polly-now-available-for-Google-Chat.html |
| Fresh visual identity for Workspace icons | Workspace | Google | http://workspaceupdates.googleblog.com/2026/05/introducing-fresh-visual-identity-for-Google-Workspace-app-icons.html |
| Added (Devin CLI Changelog) | AI/LLM | Devin | https://cli.devin.ai/docs/changelog/stable#2026-05-26-added |
| Share canvases from Cursor | 開発ツール | Cursor | https://cursor.com/changelog#2026-05-20-you-can-now-share-canvases-from-cursor-with-your-team |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Devin CLIがGemini 3.5 Flashに対応し、クラウドセッション連携やMCP権限管理が大幅強化されました。

📌 **ピックアップ**
• Devin CLI: クラウドセッションへのアタッチやエディタ連携が進化。
• AWS RDS: Multi-AZレプリケーションでENA Expressをサポートし性能向上。
• Google Chat: 意思決定を効率化する投票ツール「Polly」が利用可能に。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-27*
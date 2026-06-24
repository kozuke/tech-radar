# Tech Radar Daily Digest - 2026-06-25

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Claude Codeの大規模アップデートとAIエージェント開発の加速**
AnthropicのAI開発ツール「Claude Code」がv2.1.191へアップデートされ、エージェントの信頼性と操作性が大幅に向上しました。特に、会話履歴の復元機能やバックグラウンドエージェントの永続化、CPU使用率の約37%削減など、長時間の開発セッションにおける安定性が強化されています。また、Google ClassroomへのGemini統合拡大や、Devin CLIのサブエージェント設定追加など、AIエージェントを実務環境へ組み込む動きが加速しており、AIが単なるチャットボットから「自律的な作業者」へと進化するフェーズに入っています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic
##### v2.1.191 / v2.1.190
Claude Codeの最新版では、`/rewind`による会話復元や、バックグラウンドエージェントの停止処理の修正など、開発体験を改善する多数の機能が追加されました。また、ストリーミング時のCPU負荷を約37%削減し、長時間のセッションにおけるメモリ消費も最適化されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| 会話管理 | `/rewind`による会話復元や、エージェントの永続化を改善。 |
| UI/UX | ターミナルでの表示崩れ修正や、Vimモードの検索ヒント強化。 |
| パフォーマンス | ストリーミング時のCPU使用率を約37%削減し、メモリ効率を向上。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 対応環境 | macOS, Windows Terminal, Linux |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.191

---

#### AI Agent / Devin
##### Devin CLI アップデート
Devin CLIにおいて、サブエージェントへのデフォルトモデル設定や、コミットメッセージからDevinの言及を抑制する設定が追加されました。また、MCP（Model Context Protocol）レジストリの起動時キャッシュにより、サーバーの準備時間が短縮されています。

> 🔗 **参考リンク**
> https://cli.devin.ai/docs/changelog/stable#2026-08-18-added

---

### クラウド

#### AWS
##### Amazon EC2 AMI Watermarks
Amazon EC2でAMIにカスタム識別子（ウォーターマーク）を埋め込めるようになりました。これにより、AMIの出自追跡や、特定のウォーターマークを持つAMIのみを起動許可するガバナンスポリシーの適用が可能になります。

##### Amazon EMR Serverless ライブ設定更新
EMR Serverlessにおいて、アプリケーションを再起動することなく、最大キャパシティやカスタムイメージ設定を更新できるようになりました。これにより、実行中のジョブを中断せずに運用負荷を軽減できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS EC2, EMR Serverless |
| 特徴・性能 | 再起動なしのライブ設定変更、AMIのメタデータ追跡 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/ec2-image-watermarks-allowed-images

---

### Workspace

#### Google Workspace
##### Google Groupsのセキュリティ強化
Google Groupsにおいて「内部」「外部」の分類が厳格化され、外部メンバーの追加権限や可視性が明確化されました。管理者は組織のセキュリティ要件に合わせて、これらのラベルをAdminコンソールから調整可能です。

##### Gemini in Google Classroomのアップデート
GeminiタブがAndroid/iOSアプリでも利用可能になり、教師はモバイル環境からクイズ生成や授業案の作成が行えるようになりました。また、Nano Banana 2モデルを用いたインフォグラフィックやスライド生成機能も追加されています。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/stricter-classifications-for-google-groups-to-enhance-data-security-and-privacy.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude Codeをv2.1.191へアップデート | 開発者 | 🟡 中 |
| EC2 AMIのガバナンスポリシー確認 | クラウド管理者 | 🟡 中 |
| Google Groupsの分類設定のレビュー | Workspace管理者 | 🔴 高 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EC2 AMI Watermarks | クラウド | AWS | [リンク](https://aws.amazon.com/about-aws/whats-new/2026/06/ec2-image-watermarks-allowed-images) |
| EMR Serverless ライブ更新 | クラウド | AWS | [リンク](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-emr-serverless/) |
| Claude Code v2.1.191 | AI/LLM | GitHub | [リンク](https://github.com/anthropics/claude-code/releases/tag/v2.1.191) |
| Google Groups セキュリティ強化 | Workspace | Google | [リンク](http://workspaceupdates.googleblog.com/2026/06/stricter-classifications-for-google-groups-to-enhance-data-security-and-privacy.html) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
Claude Codeがv2.1.191へアップデート。CPU負荷の大幅削減と会話復元機能で開発効率が向上しました。

📌 **ピックアップ**
• AWS EC2でAMIの出自を追跡するウォーターマーク機能が追加
• EMR Serverlessが再起動なしのライブ設定変更に対応
• Google Groupsのセキュリティ分類が厳格化、管理権限が明確に
• Gemini in Google Classroomがモバイルアプリに対応

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-25*
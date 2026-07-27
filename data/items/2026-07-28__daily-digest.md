# Tech Radar Daily Digest - 2026-07-28

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Google Meetの「Take notes for me（メモを取って）」機能が大幅に強化され、会議中に共有されたスライドや図表を自動的にスクリーンショットとしてメモに埋め込む機能がまもなく一般提供されます。これまでは音声の文字起こしが中心でしたが、視覚的なコンテキストが加わることで、会議の振り返りがより直感的かつ正確になります。管理者は、このスクリーンショット機能を「常に許可」するか「録画時のみ許可」するかを事前に設定可能であり、プライバシー保護と利便性のバランスを組織単位で制御できる点が重要です。

また、AWS Security HubがModel Context Protocol (MCP) に対応し、Claude Desktopから直接セキュリティ調査が可能になりました。自然言語による問い合わせで攻撃経路の可視化や推奨される修正案の取得が可能となり、セキュリティ運用におけるコンテキストスイッチを劇的に削減します。AIエージェントがセキュリティ運用に深く統合される、実用的な一歩と言えるでしょう。

---

## 📰 今日のニュース

### AI/LLM

#### AI Agent

##### AWS Security Hub MCP App brings exposure findings into your AI-assisted workflow (Preview)

AWS Security Hubの調査結果をClaude Desktopから直接操作できるMCPサーバーがプレビュー公開されました。自然言語でセキュリティの脆弱性や攻撃経路を照会し、AIによる分析と視覚的なレポートを受け取れるため、セキュリティ担当者の調査効率が大幅に向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Model Context Protocol (MCP) |
| 特徴・性能 | 読み取り専用ツールによる安全な調査、自然言語による対話型分析 |
| 対応環境 | AWS商用リージョン（Security Hub対応環境） |
| 関連サービス | AWS Security Hub, Claude Desktop |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-mcp-app/

---

### クラウド

#### AWS

##### Amazon GameLift Streams now supports Custom Aspect Ratio and Dynamic Resolution

Amazon GameLift Streamsがカスタムアスペクト比と動的解像度調整に対応しました。デバイスに応じた最適な表示が可能になり、ネットワーク状況に応じて解像度を自動調整することで、ストリーミングの安定性とユーザー体験が向上します。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Custom Aspect Ratio | モバイルやウルトラワイドなど、デバイスに合わせた解像度をセッションごとに設定可能。 |
| Dynamic Resolution | ネットワーク帯域の変動に合わせて解像度を自動調整し、フレーム落ちを防ぐ。 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams/

##### AWS Elemental MediaTailor adds configurable ad timeout and concurrency controls

AWS Elemental MediaTailorにおいて、広告決定サーバー（ADS）のタイムアウト設定や並列リクエストの制御が可能になりました。これにより、ライブイベントやVOD配信における広告の充填率向上や、動画再生開始の高速化が実現します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/mediatail-configurable-ad-timeout-and-concurrency

##### Amazon RDS for SQL Server now supports restoring TDE databases on Mult-AZ instances

RDS for SQL Serverにおいて、TDE（透過的データ暗号化）で保護されたデータベースをMulti-AZインスタンスへ直接リストアできるようになりました。従来必要だったSingle-AZへの一時的な移行が不要となり、高可用性と暗号化の両立が容易になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/rds-sql-server-supports-tde-for-maz/

##### AWS Clean Rooms supports larger worker types up to 32 vCPUs for SQL

AWS Clean RoomsでSQL分析用のワーカータイプが強化され、最大32 vCPU/244GBメモリを選択可能になりました。大規模データセットに対する複雑なクエリ処理が高速化され、分析コストの最適化に寄与します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-clean-rooms-32-vcpu-worker-types-sql/

---

### Workspace

#### Google Workspace

##### Visual screenshots in Google Meet meeting notes will soon be generally available

Google MeetのAIメモ機能が強化され、プレゼン資料のスクリーンショットが自動的にメモに埋め込まれるようになります。管理者は現在、組織単位でこの機能の利用可否や条件を設定可能です。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/visual-screenshots-in-google-meet-meeting-notes-will-soon-be-generally-available-pre-configure-admin-settings-in-advance.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Google Meetのスクリーンショット設定を確認・構成する | Workspace管理者 | 🔴 高 |
| AWS Security Hub MCP Appを試用して調査フローを改善する | セキュリティエンジニア | 🟡 中 |
| GameLift Streamsの新SDKをダウンロードし、動的解像度を有効化する | ゲーム開発者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon GameLift Streams... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams/ |
| AWS Security Hub MCP App... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-mcp-app/ |
| AWS Elemental MediaTailor... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/mediatail-configurable-ad-timeout-and-concurrency |
| Amazon RDS for SQL Server... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/rds-sql-server-supports-tde-for-maz/ |
| AWS Clean Rooms supports... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-clean-rooms-32-vcpu-worker-types-sql |
| 0.146.0-alpha.13 | その他 | openai_codex | https://github.com/openai/codex/releases/tag/rust-v0.146.0-alpha.13 |
| 0.146.0-alpha.12 | その他 | openai_codex | https://github.com/openai/codex/releases/tag/rust-v0.146.0-alpha.12 |
| Visual screenshots in Google Meet... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/07/visual-screenshots-in-google-meet-meeting-notes-will-soon-be-generally-available-pre-configure-admin-settings-in-advance.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Google Meetが会議中のスライドを自動でメモに埋め込む機能を提供開始。

📌 **ピックアップ**
• AWS Security HubがClaude Desktopと連携し、AIによるセキュリティ調査が可能に
• Amazon GameLift Streamsが動的解像度調整に対応し、ストリーミング品質が向上
• AWS RDS for SQL ServerがTDE環境でのMulti-AZリストアをサポート

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-28*
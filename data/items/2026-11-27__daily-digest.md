# Tech Radar Daily Digest - 2026-11-27

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、マネージドなEnvoyプロキシ環境を提供する「Elastic Load Balancing (ELB) for Envoy」の一般提供（GA）を開始しました。これまでプラットフォームチームが自前で管理していたEnvoyのアップグレード、セキュリティパッチ適用、キャパシティ管理をAWSが代行するマネージドサービスです。各プロキシはAWS Nitro Systemによるハードウェア分離環境で実行されるため、Envoyの脆弱性がシステム全体に波及するリスクを低減できます。

既存のEnvoy設定や拡張機能をそのまま移行できる柔軟性を持ちつつ、AWS Certificate ManagerやAWS WAFといったAWSのネイティブ機能と容易に統合可能です。特にKubernetes環境でEnvoy Gatewayを利用している場合、インフラプロバイダーを追加するだけでシームレスにELB for Envoyへ移行できるため、運用負荷の軽減とセキュリティの強化を同時に実現したい組織にとって非常に重要なアップデートとなります。

---

## 📰 今日のニュース

### AI/LLM

#### AI Agent

##### Sessions & Workspace（Devin）

Devinの最新アップデートでは、削除されたファイルの内容をChangesペインで確認可能になるなど、開発体験が向上しました。また、Slack Enterprise Grid環境でのBot利用の改善や、大規模組織向けのAPIパフォーマンス最適化、インシデント対応時の言語設定追加など、エンタープライズ利用を意識した機能強化が図られています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| 開発体験向上 | 削除済みファイルの内容表示や、Botチャットのセッション状態保持機能を追加。 |
| エンタープライズ機能 | サービスユーザー一覧のページネーション対応や、管理者によるセッション権限の自己付与が可能に。 |
| 連携強化 | AutomationsによるSlackへの通知機能や、Devin Oncallでの応答言語設定を追加。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AI Agent, Slack API, v3 API |
| 特徴・性能 | 大規模組織でのAPIタイムアウト解消、柔軟な権限管理 |
| 対応環境 | Webブラウザ, Slack, Microsoft Teams |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-11-26-sessions-workspace

---

#### Amazon Transcribe

##### Amazon Transcribe Turbo: more accurate transcripts and natural turn-taking for voice agents

Amazon Transcribe Turboがパブリックプレビューとなり、音声エージェント向けの高度な機能が追加されました。特に「Semantic turn-taking」は、沈黙だけでなく文脈や韻律から発話終了を判断するため、自然な会話体験を提供します。また、実行時に動的なコンテキストを渡す「Runtime ASR hints」により、メニュー選択などの認識精度が大幅に向上しました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Semantic turn-taking | 文脈と韻律に基づいた発話終了検知により、自然なターンテーキングを実現。 |
| Runtime ASR hints | ターンごとに期待されるエンティティやメニュー項目を提示し、認識精度を向上。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | 音声認識(ASR), 機械学習モデル |
| 特徴・性能 | 英語でのメニュー認識精度が87%から97%へ向上、応答遅延約615ms |
| 対応環境 | AWS US East (Ohio) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/transcribe-turbo-preview/

---

### クラウド

#### AWS

##### Amazon RDS for PostgreSQL マイナーバージョンアップ

Amazon RDS for PostgreSQLが最新のマイナーバージョン（18.7, 17.12, 16.16, 15.20, 14.25）をサポートしました。これらは既知の脆弱性（CVE）への対応やバグ修正を含んでおり、セキュリティ維持のためにアップグレードが推奨されています。AWS Organizationsのアップグレードロールアウトポリシーを活用することで、低優先度環境から段階的に適用可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | PostgreSQL, Amazon RDS |
| 特徴・性能 | セキュリティパッチ、バグ修正 |
| 関連サービス | AWS Organizations, RDS Blue/Green Deployments |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-postgresql-18-7-17-12-16-16-15-20-14-25/

---

##### Amazon EC2 C9g / M9g インスタンスの提供リージョン拡大

AWS Graviton5プロセッサを搭載したC9gおよびM9gインスタンスの提供リージョンが拡大されました。C9gは演算集約型ワークロード向けに最大25%の性能向上を実現し、M9gはメモリ集約型ワークロードに最適化されています。両インスタンスはNitro Isolation Engineを初搭載し、数学的に証明されたクラウドセキュリティを提供します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Graviton5, AWS Nitro System |
| 特徴・性能 | Graviton4比で最大25%の性能向上、Nitro Isolation Engineによる分離 |
| 対応環境 | EC2 (各リージョン) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-c9g-instances-additional-regions/
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-m9g-instances-additional-regions/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| RDS PostgreSQLのマイナーバージョンアップ計画策定 | DB管理者 | 🔴 高 |
| ELB for Envoyの検証（セルフ管理Envoyからの移行検討） | プラットフォームエンジニア | 🟡 中 |
| Devinの最新機能（権限管理・通知設定）の確認 | Devin利用者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon RDS for PostgreSQL supports minor versions... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-postgresql-18-7-17-12-16-16-15-20-14-25/ |
| Amazon EC2 C9g instances are now available... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-c9g-instances-additional-regions/ |
| Amazon EC2 M9g instances now available... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-m9g-instances-additional-regions/ |
| Elastic Load Balancing for Envoy is now generally available | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/elastic-load-balancing-for-envoy-generally-available |
| Amazon Transcribe Turbo: more accurate transcripts... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/transcribe-turbo-preview/ |
| 0.174.0-alpha.8 | AI/LLM | openai_codex_cli | https://github.com/openai/codex/releases/tag/rust-v0.174.0-alpha.8 |
| Sessions & Workspace | AI/LLM | devin_release_notes | https://docs.devin.ai/release-notes/overview#2026-11-26-sessions-workspace |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWSのマネージドEnvoyサービス「ELB for Envoy」が一般提供開始。運用負荷を大幅軽減します。

📌 **ピックアップ**
• RDS for PostgreSQLの最新マイナー版がリリース。脆弱性対応のため更新を推奨。
• Graviton5搭載のEC2 C9g/M9gインスタンスが提供リージョンを拡大。
• Amazon Transcribe Turboがプレビュー開始。音声エージェントの会話精度が向上。
• Devinがエンタープライズ向け権限管理やSlack連携を強化。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-27*
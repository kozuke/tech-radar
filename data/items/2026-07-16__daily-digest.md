# Tech Radar Daily Digest - 2026-07-16

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、Amazon CloudWatch Logsにおいて「Intelligent-Tiering（インテリジェント階層化）」ストレージ機能を発表しました。これにより、ログのアクセスパターンに基づいて「標準」「低頻度アクセス」「アーカイブ即時アクセス」の3つの階層へ自動的にデータが分類されます。これまでログの長期保存には手動でのフィルタリングやエクスポートが必要でしたが、本機能により運用負荷を下げつつ、コストを最適化しながら同一のクエリ体験を維持できるようになります。

また、Google Chatにおいても外部コラボレーションの強化が発表されました。これまで外部ユーザーとの会話は1対1に限られていましたが、今回のアップデートにより、複数の外部ユーザーを含むグループ会話の作成が可能になります。これにより、組織外のパートナーとのリアルタイムな連携が大幅に効率化され、ビジネスコミュニケーションの柔軟性が向上します。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.211 および v2.1.210
Claude Codeの最新アップデートでは、サブエージェントの思考プロセスをストリーム出力に含める機能が追加されるなど、開発体験の向上が図られています。また、パーミッション管理の強化や、セッション管理、UIの表示不具合など、多数のバグ修正が行われました。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code (Anthropic) |
| 特徴・性能 | サブエージェントの可視化、パーミッション制御の厳格化 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> [v2.1.211](https://github.com/anthropics/claude-code/releases/tag/v2.1.211) / [v2.1.210](https://github.com/anthropics/claude-code/releases/tag/v2.1.210)

---

#### OpenAI Codex CLI

##### 0.145.0-alpha.12〜14
OpenAI Codex CLIのアルファ版リリースが連続して行われました。主に内部的な改善や安定性の向上が進められており、開発者向けのプレリリース版として提供されています。

> 🔗 **参考リンク**
> [0.145.0-alpha.14](https://github.com/openai/codex/releases/tag/rust-v0.145.0-alpha.14)

---

### クラウド

#### AWS

##### Amazon CloudWatch Logs Intelligent-Tiering
ログデータのアクセス頻度に応じてストレージ階層を自動最適化する機能です。30日未アクセスで「低頻度アクセス」、90日未アクセスで「アーカイブ即時アクセス」へ自動移行し、コスト削減を実現します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-intelligent-tiering/

##### Amazon MQ for RabbitMQ のストレージ設定
RabbitMQブローカーにおいて、インスタンスタイプとは独立してEBSストレージサイズを設定可能になりました。これにより、メッセージングワークロードの要件に合わせてストレージ容量を柔軟に調整できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-mq-rabbitmq-configurable-storage/

##### RDS/AuroraのGraviton4インスタンス拡充
R8gおよびM8gインスタンスが、RDSおよびAuroraのより多くのリージョンで利用可能になりました。Graviton3と比較して最大40%のパフォーマンス向上と、最大29%の価格性能比改善が見込まれます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-rds-aurora-r8g-m8g-regions/

##### R8gd/M8gdのリージョン拡大とOptimized Reads
ローカルNVMe SSDを活用した「Optimized Reads」をサポートするR8gd/M8gdインスタンスの提供リージョンが拡大されました。複雑なクエリの高速化やインデックス再構築の効率化に貢献します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-rds-aurora-r8gd-m8gd-regions/

##### Amazon Cognitoのパスワードハッシュインポート
CSVファイルによるユーザーインポート時に、パスワードハッシュを含めることが可能になりました。bcrypt、scrypt、Argon2id、PBKDF2などのアルゴリズムをサポートし、移行時のユーザーのパスワードリセットの手間を省きます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cognito-password-hash-import/

---

### Workspace

#### Google Chat

##### 外部コラボレーターとのグループ会話
Google Chatで外部ユーザーを含むグループDMが作成可能になりました。外部メンバーが含まれる会話にはバッジが表示され、管理者は既存の外部スペース用設定を通じてアクセスを制御できます。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/now-available-group-conversations-with-external-collaborators-in-Google-Chat.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| CloudWatch LogsのIntelligent-Tiering設定確認 | インフラ管理者 | 🟡 中 |
| 外部ユーザーとのグループDM設定の有効化確認 | Google Workspace管理者 | 🟡 中 |
| RDS/Auroraのインスタンスタイプ最適化検討 | DB管理者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon CloudWatch Logs... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-intelligent-tiering/ |
| Amazon MQ now supports... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-mq-rabbitmq-configurable-storage/ |
| Amazon RDS and Aurora... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-rds-aurora-r8g-m8g-regions/ |
| Amazon RDS and Aurora... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-rds-aurora-r8gd-m8gd-regions/ |
| Amazon Cognito now supports... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cognito-password-hash-import/ |
| v2.1.211 | AI/LLM | Claude Code | https://github.com/anthropics/claude-code/releases/tag/v2.1.211 |
| v2.1.210 | AI/LLM | Claude Code | https://github.com/anthropics/claude-code/releases/tag/v2.1.210 |
| 0.145.0-alpha.14 | AI/LLM | OpenAI | https://github.com/openai/codex/releases/tag/rust-v0.145.0-alpha.14 |
| 0.145.0-alpha.13 | AI/LLM | OpenAI | https://github.com/openai/codex/releases/tag/rust-v0.145.0-alpha.13 |
| 0.145.0-alpha.12 | AI/LLM | OpenAI | https://github.com/openai/codex/releases/tag/rust-v0.145.0-alpha.12 |
| Now available: group conversations... | Workspace | Google | http://workspaceupdates.googleblog.com/2026/07/now-available-group-conversations-with-external-collaborators-in-Google-Chat.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWS CloudWatch Logsがストレージの自動階層化に対応し、コストと運用効率が向上しました。

📌 **ピックアップ**
• CloudWatch Logs: アクセス頻度に応じた自動ストレージ階層化を開始
• Google Chat: 外部ユーザーを含むグループ会話が可能に
• AWS RDS/Aurora: Graviton4インスタンスの提供リージョンが拡大

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-16*
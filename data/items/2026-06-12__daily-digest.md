# Tech Radar Daily Digest - 2026-06-12

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Amazon Aurora PostgreSQL 18への対応と監視機能の強化**
AWSはAmazon Aurora PostgreSQL-Compatible Editionにおいて、最新のメジャーバージョン18への対応を開始しました。このアップデートでは、クエリパフォーマンスを向上させる「B-treeスキップスキャン」や、統計情報を維持したままアップグレード可能な機能が導入され、運用負荷の軽減とパフォーマンスの安定化が期待できます。また、Amazon Managed Service for Prometheusにおいても「ネイティブヒストグラム」のサポートや、順序不同のサンプル取り込み機能が追加されました。これにより、分散システムにおけるメトリクスの精度が向上し、より信頼性の高い監視環境の構築が可能になります。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.173

Claude Codeの最新リリースでは、Fable 5モデル名に含まれる「[1m]」サフィックスの正規化処理が修正され、自動的にストリップされるようになりました。また、Windows環境でサンドボックスが有効な場合に発生していた不要な警告メッセージも解消されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | モデル名正規化の改善、Windowsでの警告修正 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.173

---

#### OpenAI Codex CLI

##### 0.140.0-alpha.8 〜 0.140.0-alpha.12

OpenAIのCodex CLIにおいて、複数のアルファ版リリースが連続して公開されました。継続的な改善とバグ修正が行われており、開発環境におけるCLIツールの安定化が進められています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Codex CLI |
| 対応環境 | RustベースのCLIツール |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.140.0-alpha.12

---

#### Devin

##### Devin Review: Pending PR Reviews Canceled on New Commits

Devinのレビュー機能が強化され、PRに新しいコミットがプッシュされた際に進行中のレビューが自動キャンセルされるようになりました。また、Figma MCPの公式統合や、Slack連携のメッセージレンダリング改善など、開発効率を高める機能が多数追加されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| 自動キャンセル | 新規コミット時に進行中のPRレビューを自動停止 |
| Figma MCP | 公式Figma MCPサーバーの提供開始 |
| Slack連携 | メッセージのレンダリング改善およびエコー機能の追加 |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-06-10-devin-review-pending-pr-reviews-canceled-on-new-commits

---

### クラウド

#### AWS

##### Amazon Aurora now supports PostgreSQL major version 18

Amazon Aurora PostgreSQLがメジャーバージョン18に対応しました。クエリパフォーマンスの向上だけでなく、大規模な整数セット操作を効率化する「pg_roaringbitmap」拡張機能が利用可能になり、データベース層での高度なデータ処理が強化されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Aurora PostgreSQL 18.3 |
| 特徴・性能 | B-treeスキップスキャン、統計維持アップグレード |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-aurora-postgresql-major-version-18/

---

##### AWS Elastic Beanstalk console now integrates CloudWatch Logs in the Logs tab

Elastic Beanstalkのコンソールから直接CloudWatch Logsを確認できるようになりました。これにより、ロググループやストリームを探すためにコンソールを切り替える必要がなくなり、運用効率が大幅に向上します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/elastic-beanstalk-cloudwatch-logs/

---

##### Amazon MWAA Serverless now supports Amazon EventBridge notifications

Amazon MWAA ServerlessがAmazon EventBridgeと統合され、ワークフローやタスクの状態変化をイベントとして通知できるようになりました。これにより、ワークフローの失敗時の自動アラートや、依存関係のあるパイプラインの自動再実行など、イベント駆動型の自動化が容易になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-eventbridge/

---

##### Amazon Managed Service for Prometheus now supports Native Histograms

Prometheusのネイティブヒストグラムがサポートされ、高精度なメトリクス分布の取得が可能になりました。指数バケット化により、メモリ効率を維持しつつ、より正確なテールレイテンシの分析を実現します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-managed-service-prometheus-native-histograms/

---

##### Amazon Managed Service for Prometheus now supports out of order sample ingestion

Prometheusにおいて、順序不同のサンプル取り込みとルールクエリのオフセット設定がサポートされました。これにより、ネットワーク遅延やバッチ処理によるデータ欠落を防ぎ、監視データの整合性が向上します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-managed-service-prometheus-outoforder-ingestion/

---

### Workspace

#### Google Workspace

##### Google Vault now supports retention rules and litigation holds for Gemini app

Google VaultがGeminiアプリの会話データに対する保持ルールと訴訟ホールドに対応しました。これにより、組織はGeminiの利用履歴を法規制やコンプライアンス要件に従って管理・保存できるようになります。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/google-vault-now-supports-retention-rules-and-litigation-holds-for-Gemini-app.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Aurora PostgreSQL 18へのアップグレード計画策定 | DB管理者 | 🟡 中 |
| Prometheusのネイティブヒストグラム導入検討 | SRE/DevOps | 🟡 中 |
| GeminiアプリのVault保持ポリシー設定確認 | セキュリティ管理者 | 🔴 高 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Aurora now supports PostgreSQL 18 | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-aurora-postgresql-major-version-18/ |
| Elastic Beanstalk CloudWatch Logs integration | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/elastic-beanstalk-cloudwatch-logs/ |
| MWAA Serverless EventBridge support | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-eventbridge/ |
| Prometheus Native Histograms | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-managed-service-prometheus-native-histograms/ |
| Prometheus out of order ingestion | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-managed-service-prometheus-outoforder-ingestion/ |
| Claude Code v2.1.173 | AI/LLM | GitHub | https://github.com/anthropics/claude-code/releases/tag/v2.1.173 |
| OpenAI Codex CLI (alpha 8-12) | AI/LLM | GitHub | https://github.com/openai/codex/releases/tag/rust-v0.140.0-alpha.12 |
| Devin Review updates | AI/LLM | Devin | https://docs.devin.ai/release-notes/overview#2026-06-10-devin-review-pending-pr-reviews-canceled-on-new-commits |
| Google Vault for Gemini | Workspace | Google | http://workspaceupdates.googleblog.com/2026/06/google-vault-now-supports-retention-rules-and-litigation-holds-for-Gemini-app.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon Aurora PostgreSQL 18対応開始と、Prometheusの監視機能が大幅強化されました。

📌 **ピックアップ**
• Aurora PostgreSQL 18：パフォーマンス向上と統計維持アップグレードに対応
• Prometheus：ネイティブヒストグラムと順序不同データの取り込みをサポート
• Google Vault：Geminiアプリのデータ保持と訴訟ホールドに対応
• Devin：PRレビューの自動キャンセル機能など開発効率を改善

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-12*
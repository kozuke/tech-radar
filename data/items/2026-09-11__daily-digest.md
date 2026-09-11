# Tech Radar Daily Digest - 2026-09-11

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Cursorが大規模開発を自動化する「Projects」をリリース**
Cursorは、長期的な開発タスクや大規模なマイグレーション、アプリ開発全体を管理・実行できる「Projects」機能を発表しました。この機能は、メインのコーディネーターエージェントがタスクを計画し、数千ものサブエージェントに作業を委譲する階層的な構造を持っています。クラウド上で常時稼働するため、PCを閉じても作業が継続されるほか、Slack連携やスケジュール実行による自律的なタスク処理も可能です。開発の文脈を長期間維持し、エージェント間で知識を共有することで、プロジェクトの進行とともにエージェントがより効率的に機能する仕組みとなっています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic
##### Claude Code v2.1.268 リリース
Claude Codeの最新版では、ゲートウェイ機能の強化やパフォーマンス改善が行われました。特に、管理設定を通じたコスト管理の徹底や、セッション状態の削除オプションの追加など、企業利用におけるガバナンスとリソース管理が強化されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, MCP, Anthropic API |
| 特徴・性能 | CPU負荷の低減、WebFetchのタイムアウト設定追加 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.268

---

##### Anthropic SDK Python v1.5.0
Python向けAnthropic SDKがアップデートされ、Managed Agents向けのツール権限管理や、GitHubリポジトリの認証なしマウント機能が追加されました。開発者がより柔軟にエージェントを構築できるAPI拡張が行われています。

> 🔗 **参考リンク**
> https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.5.0

---

#### Devin
##### Devin CLI アップデート
Devin CLIに新しいモード切り替えコマンド（`/code`, `/smart`, `/bypass`）や、ツールごとの無効化設定が追加されました。また、モデルの拒否に対する自動フォールバック機能や、エージェントがシェルを動的に選択できる機能などが導入され、操作性と自律性が向上しています。

> 🔗 **参考リンク**
> https://cli.devin.ai/docs/changelog/stable#2026-09-10-added

---

### クラウド

#### AWS
##### AWS Lambdaの機能強化とAmazon MQのアップデート
AWS Lambdaでは、欧州Sovereign Cloudでの再帰ループ検出機能の提供開始や、Pydantic AIとの統合による耐久性のあるエージェント実行が可能になりました。また、Amazon MQはRabbitMQ 4.3をサポートし、クォーラムキューの最適化や優先度設定が強化されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Lambda再帰ループ検出 | 欧州Sovereign Cloudで利用可能になり、誤設定による無限ループを自動停止。 |
| Lambda Durable Functions | Pydantic AIと統合し、AIエージェントの実行状態を保持して中断からの再開をサポート。 |
| Amazon MQ (RabbitMQ 4.3) | クォーラムキューの圧縮や32段階の優先度設定、ネイティブな遅延リトライに対応。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Lambda, Amazon MQ, RabbitMQ 4.3 |
| 関連サービス | Amazon S3, SQS, SNS, Pydantic AI |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/lambda-recursion-europe-sovereign-cloud

---

##### AWS Transform for .NET と API Gatewayのログ機能強化
AWS Transform for .NETは、モダン化されたコードに対するユニットテストの自動生成機能を搭載しました。一方、Amazon API Gatewayは実行ログの容量を1MBまで拡張し、S3やFirehoseなど複数の送信先へ柔軟にルーティング可能になりました。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/aws-transform-net-unit-tests

---

### Workspace

#### Google Workspace
##### Google Sheetsの機能拡張とGemini Notebookの管理強化
Google SheetsはAndroidデバイスでのGemini利用が可能になり、さらにスプレッドシートのセル上限が1,000万から2,000万セルへ倍増しました。また、管理コンソールではGemini Notebookの外部共有設定がより細かく制御できるようになりました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Sheets Android版Gemini | モバイル環境でデータ分析やチャート生成が可能に。 |
| Sheets セル上限拡大 | 1,000万セルから2,000万セルへ倍増し、大規模データに対応。 |
| Gemini Notebook共有管理 | 管理者がドメイン、OU、グループ単位で外部共有の可否や範囲を設定可能に。 |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/09/doubled-cell-limits-in-google-sheets-now-generally-available.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Cursor Projectsのベータ利用を開始し、長期タスクの自動化を試す | 開発者 | 🔴 高 |
| AWS Lambdaの再帰ループ検出設定を確認する | クラウドエンジニア | 🟡 中 |
| Google Sheetsのセル上限拡大に伴うデータ設計の見直し | データアナリスト | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Lambda recursive loop detection... | クラウド | AWS | https://aws.amazon.com/... |
| AWS Transform for .NET now generates... | 開発ツール | AWS | https://aws.amazon.com/... |
| Amazon API Gateway now supports 1 MB... | クラウド | AWS | https://aws.amazon.com/... |
| AWS Lambda durable functions integrates... | AI/LLM | AWS | https://aws.amazon.com/... |
| Amazon MQ now supports RabbitMQ 4.3 | クラウド | AWS | https://aws.amazon.com/... |
| v2.1.268 (Claude Code) | AI/LLM | Anthropic | https://github.com/... |
| Gemini in Google Sheets... | Workspace | Google | http://workspaceupdates... |
| Manage external sharing for Gemini Notebook... | Workspace | Google | http://workspaceupdates... |
| Doubled cell limits in Google Sheets... | Workspace | Google | http://workspaceupdates... |
| v1.5.0 (Anthropic SDK) | AI/LLM | Anthropic | https://github.com/... |
| Added (Devin CLI) | AI/LLM | Cognition | https://cli.devin.ai/... |
| Today we're launching Projects in Cursor | AI/LLM | Cursor | https://cursor.com/... |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Cursorが大規模開発を自律的にこなす「Projects」機能をリリースしました。

📌 **ピックアップ**
• Cursor Projects: 長期タスクをサブエージェントに委譲し、クラウドで常時実行。
• AWS Lambda: 再帰ループ検出の拡大とPydantic AIとの統合による耐久性向上。
• Google Sheets: セル上限が2,000万セルへ倍増し、Android版Geminiも利用可能に。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-09-11*
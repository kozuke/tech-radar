# Tech Radar Daily Digest - 2026-09-25

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Amazon EventBridgeのエンタープライズ向け刷新**
Amazon EventBridgeが、エンタープライズ規模での利用を想定した新しい「カスタムイベントバス」をリリースしました。今回のアップデートでは、AWS Resource Access Managerを介したアカウント間でのイベントバス共有が可能になり、厳密な順序保証やコンテンツベースの重複排除機能がネイティブでサポートされました。これにより、複雑な分散システムにおけるチーム間の疎結合化が促進され、SaaSやAWSサービス間でのイベント駆動型アーキテクチャの構築がより堅牢かつ柔軟になります。

**Google Cloud API GatewayによるREST APIのMCP化**
Google Cloud API Gatewayが、REST APIをModel Context Protocol (MCP) ツールとして公開する機能をパブリックプレビューで開始しました。OpenAPI仕様にアノテーションを追加するだけで、既存のREST APIをGeminiなどのAIエージェントから直接呼び出し可能なツールへと変換できます。これにより、開発者はAIエージェントのために別途MCPサーバーを構築・運用する必要がなくなり、既存の認証やクォータ設定を維持したまま、AIによる業務自動化を迅速に実装できるようになります。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / OpenAI Codex

##### Claude Code v2.1.282 リリース
Claude Codeの最新版では、広幅ターミナルでの表示最適化やテレメトリ設定の可視化機能が追加されました。また、セッション継続時の履歴処理やAPIエラー時のリトライロジックが大幅に改善され、安定性が向上しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | セッション継続時の思考ブロック保持、APIエラーハンドリングの強化 |
| 対応環境 | ターミナル環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.282

##### OpenAI Codex CLI (rust-v0.158.0-alpha系)
Codex CLIのアルファ版リリースが複数回行われ、継続的な機能改善とバグ修正が実施されています。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases

#### Google Gemini / AI Agent

##### MaxTextによるOLMo 3 7Bの学習再現
Google CloudのMaxTextを用いて、AI2の「OLMo 3 7B」モデルの学習をTPU上で完全に再現することに成功しました。このケーススタディでは、PyTorchからJAXへのモデル変換や、学習中のリソース変動に対する耐性、TPU世代間での移植性が実証されました。

> 🔗 **参考リンク**
> https://developers.googleblog.com/reproducing-olmo-3-7b-pre-training-in-maxtext-case-study-of-large-scale-training-on-tpus/

---

### クラウド

#### AWS

##### AWS Lambda Durable Functionsの欧州ソブリンクラウド対応
Lambda Durable FunctionsがAWS European Sovereign Cloudで利用可能になりました。これにより、コンプライアンス要件の厳しい環境下でも、ステートフルなAIワークフローや複雑なプロセスオーケストレーションをLambda上で構築できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/durablefunctions-european-sovereign-cloud/

##### Amazon RDS for PostgreSQLのアップデート
RDS for PostgreSQLにて、PostgreSQL 19 Beta 4のプレビュー環境対応および、耐量子計算機暗号（PQ-TLS）鍵交換のサポートが開始されました。また、MySQL向けにはExtended Supportのマイナーバージョンが更新されています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/postgresql-post-quantum-tls-key-exchange/

---

### Workspace

#### Google Workspace

##### Google DocsとGemini Notebookの連携
Google Docs内でGemini Notebookをコンテキストソースとして指定可能になりました。これにより、特定の研究資料やナレッジベースに基づいたドキュメント作成が、タブを切り替えることなく効率的に行えます。

##### 管理機能の強化
管理コンソールにて、管理者ロールの期間限定割り当てが可能になりました。また、Google Meetハードウェア（Logitech製）での在室人数カウント機能や、Google Sheetsでのピボットテーブル手動並べ替え機能などが追加されています。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| EventBridgeの新しいカスタムイベントバスへの移行検討 | クラウドアーキテクト | 🟡 中 |
| REST APIのMCP化によるAIエージェント連携の検証 | バックエンド開発者 | 🟡 中 |
| Workspaceの管理者ロール一時割り当て機能の導入 | IT管理者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EventBridge relaunches... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/eventbridge-relaunches-custom-event-buses/ |
| AWS Lambda durable functions... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/09/durablefunctions-european-sovereign-cloud/ |
| Turn your REST APIs into MCP... | AI/LLM | Google | https://developers.googleblog.com/turn-your-rest-apis-into-mcp-tools-with-google-cloud-api-gateway/ |
| Reproducing OLMo 3 7B... | AI/LLM | Google | https://developers.googleblog.com/reproducing-olmo-3-7b-pre-training-in-maxtext-case-study-of-large-scale-training-on-tpus/ |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon EventBridgeの刷新と、Google Cloud API GatewayによるREST APIのMCP化が発表されました。

📌 **ピックアップ**
• EventBridge: チーム間共有や順序保証を強化した新カスタムイベントバスが登場。
• API Gateway: REST APIをAIエージェント用MCPツールとして公開可能に。
• Workspace: Gemini Notebook連携や管理者権限の一時付与機能が追加。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-09-25*
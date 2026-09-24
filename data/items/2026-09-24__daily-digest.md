# Tech Radar Daily Digest - 2026-09-24

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AIエージェントの運用・監視を統合する「Amazon CloudWatch Omni」が登場**
AWSは、AIエージェントやアプリケーションの観測性を高める「Amazon CloudWatch Omni」を一般公開しました。OpenTelemetryの相互運用性とCloudWatchの信頼性を組み合わせた本サービスは、単なる監視ツールを超え、AI開発のライフサイクル全体を支援します。特に、LangGraphやCrewAIなどの主要フレームワークで構築されたAIエージェントに対し、プロンプトやモデル呼び出しごとの品質評価や実験を可能にする点が画期的です。IDE拡張機能やWebコンソールを通じて、自然言語によるテレメトリの問い合わせや、根本原因の特定を効率化できるため、AI開発の生産性が大幅に向上することが期待されます。

**Cursorが「ラストマイル」を自動化する2つの新ボットを投入**
Cursorは、コードのデプロイとセキュリティを強化する「Rollouts」と「Security Review」という2つの新ボットをTeamsおよびEnterpriseプラン向けにリリースしました。Rolloutsはプルリクエストからデプロイ後の環境までを監視し、回帰テストやヘルスチェックを自動化して、問題発生時に通知や修正提案を行います。一方、Security Reviewはプルリクエストごとにコードベース全体をコンテキストとして読み込み、SQLインジェクションや認証バイパスなどの脆弱性を特定します。これにより、開発からリリースまでの最終工程における品質と安全性が大幅に強化されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code
##### v2.1.281 リリース
Claude Codeの最新版では、Claude Apps Gatewayのサポート強化やMCP（Model Context Protocol）関連の機能改善が行われました。特に、BedrockへのIAMロールによるアクセスや、MCPサーバーの検証機能が追加され、企業環境での利用がよりセキュアかつ柔軟になっています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Claude Apps Gateway | 新しいClaude Desktopキーのサポートや、BedrockへのIAMロールによる認証機能を追加。 |
| MCP機能 | URLモードの elicitation（引き出し）や、プラグイン検証時のセキュリティチェックを強化。 |
| セッション管理 | 巨大なセッションの再開時の安定性向上や、クラッシュの修正を実施。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, MCP, Amazon Bedrock |
| 特徴・性能 | 認証強化、セッション復元機能の最適化 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.281

---

#### Google AI
##### Antigravity SDKがローカルAIモデルをサポート
GoogleのAntigravity SDKが、Gemma 4 26Bなどのローカルモデル実行に対応しました。LiteRTを活用することで、プライバシー保護やオフライン環境でのエージェント実行が可能になり、クラウドモデルとのハイブリッド構成による効率的なワークフロー構築が実現します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Antigravity SDK, LiteRT, Gemma 4 26B |
| 特徴・性能 | ローカルGPU/RAMを活用したオフライン推論 |
| 対応環境 | Python環境 (推奨: 24GB以上のVRAM) |

> 🔗 **参考リンク**
> https://developers.googleblog.com/introducing-support-for-local-ai-models-in-the-antigravity-sdk/

---

### クラウド

#### AWS
##### Amazon Bedrock Managed Knowledge Baseのデータソース拡張
Amazon BedrockのRAGサービスが、SalesforceとZendeskをネイティブコネクタとしてサポートしました。これにより、カスタムパイプラインを構築することなく、既存のナレッジベースをAIエージェントの根拠として直接同期できるようになり、サポートボット等の開発が大幅に簡素化されます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-managed-knowledge-base-salesforce-zendesk-native-data-source-connectors/

##### Amazon EMRのLTSリリース開始
Amazon EMRがApache Spark 4.1を搭載したLong Term Support (LTS) リリースを開始しました。36ヶ月間のサポートが提供され、Apache Iceberg v3へのフル対応やSpark Connectエンドポイントのサポートなど、大規模データ処理の安定性と機能性が向上しています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-emr-long-term-support-spark-4-1/

---

### Workspace

#### Google Sheets
##### 手動計算モードの導入
Google Sheetsに手動計算設定が追加されました。大規模なデータセットや複雑な数式を含むシートにおいて、自動再計算を一時停止することで、編集時のパフォーマンスを維持し、意図したタイミングで一括更新を行うことが可能になります。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/09/new-manual-calculation-setting-in-Google-Sheets.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| CloudWatch Omniの導入検討（AIエージェント監視） | AI開発チーム | 🔴 高 |
| CursorのRollouts/Security Reviewの有効化 | 開発チーム | 🔴 高 |
| Salesforce/ZendeskナレッジのBedrock同期設定 | インフラ/AI担当 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Bedrock Managed Knowledge Base... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-managed-knowledge-base-salesforce-zendesk-native-data-source-connectors/) |
| Amazon Connect Customer... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-connect-routing-step-data/) |
| Amazon CloudWatch Omni... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-cloudwatch-omni-ai/) |
| Amazon EMR introduces LTS... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-emr-long-term-support-spark-4-1/) |
| Amazon Route 53 Resolver... | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/09/route-53-resolver-gen2-outposts/) |
| v2.1.281 (Claude Code) | AI/LLM | GitHub | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.281) |
| 0.158.0-alpha.x (Codex) | AI/LLM | GitHub | [link](https://github.com/openai/codex/releases/tag/rust-v0.158.0-alpha.6) |
| Introducing Support for Local AI Models... | AI/LLM | Google | [link](https://developers.googleblog.com/introducing-support-for-local-ai-models-in-the-antigravity-sdk/) |
| New manual calculation setting... | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/09/new-manual-calculation-setting-in-Google-Sheets.html) |
| Fixed (Devin) | AI/LLM | Devin | [link](https://cli.devin.ai/docs/changelog/stable#2026-09-22-fixed) |
| Cursor bots (Rollouts/Security) | AI/LLM | Cursor | [link](https://cursor.com/changelog#2026-09-23-today-we-re-launching-two-cursor-bots-for-the-last-mile-of-shipping-code-rollout) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AIエージェントの監視を統合する「Amazon CloudWatch Omni」と、Cursorのデプロイ・セキュリティ自動化ボットが登場しました。

📌 **ピックアップ**
• CloudWatch Omni: AIエージェントの品質評価と観測性を統合
• Cursor新機能: デプロイ監視「Rollouts」と脆弱性検知「Security Review」
• Bedrock: Salesforce/Zendeskのネイティブコネクタに対応

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-09-24*
# Tech Radar Daily Digest - 2026-09-06

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Amazon Bedrock Managed Knowledge Baseにおいて、データソース連携の利便性が大幅に向上しました。SharePoint、OneDrive、Confluenceに対する「ユーザー管理型セットアップ」が導入され、IT管理者の介入なしに個人の資格情報で直接データソースを接続可能になりました。さらに、ServiceNowがネイティブコネクタとして追加され、ナレッジ記事やサービスカタログの自動取り込みが容易になったほか、データソースの自動同期スケジューリング機能も実装されました。これらのアップデートにより、RAG（検索拡張生成）アプリケーションの構築・運用負荷が劇的に軽減され、企業内データの活用がより迅速かつ自律的に行えるようになります。

---

## 📰 今日のニュース

### AI/LLM

#### AI Agent

##### Devin CLI v3000.6.12 アップデート

DevinのCLIが更新され、サブエージェントへの依存度が削減されました。また、長時間実行タスクにおけるトークン効率を改善するため、バックグラウンドでのキャッシュリフレッシュタスクが追加されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AI Agent, CLI |
| 特徴・性能 | トークン効率の向上、エージェント構成の最適化 |

> 🔗 **参考リンク**
> https://cli.devin.ai/docs/changelog/stable#2026-09-03-changed

---

#### OpenAI Codex

##### rust-v0.154.0-alpha.4 リリース

OpenAIのCodex CLIに関連するRust実装のアルファ版がリリースされました。詳細な変更ログは現在確認できませんが、開発環境のアップデートが含まれています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Rust, OpenAI Codex |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.154.0-alpha.4

---

### クラウド

#### AWS

##### Amazon Bedrock Managed Knowledge Base 機能強化

Bedrockのマネージドナレッジベースにおいて、データソース接続の簡素化、ServiceNowのネイティブサポート、および自動同期スケジューリングが導入されました。これにより、RAG構築におけるデータ取り込みの自動化と運用効率が大幅に向上します。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| ユーザー管理型セットアップ | 管理者権限なしでSharePoint等のデータソースを接続可能に。 |
| ServiceNowコネクタ | ServiceNowのナレッジ記事やカタログを直接RAGに取り込み可能。 |
| 自動同期スケジューリング | 日次・週次・月次での自動同期設定が可能に。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | RAG, Amazon Bedrock |
| 関連サービス | SharePoint, OneDrive, Confluence, ServiceNow |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-managed-knowledge-base-user-managed-setup-sharepoint-onedrive-confluence/

---

##### Amazon SageMaker AI Batch Transform が G6e インスタンスをサポート

SageMakerのBatch Transformが、NVIDIA L40S GPUを搭載したG6eインスタンスに対応しました。これにより、大規模言語モデルや拡散モデルなどのGPU負荷の高いオフライン推論処理をより高速に実行可能となります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | SageMaker Batch Transform, NVIDIA L40S |
| 特徴・性能 | GPU集約型ワークロードのパフォーマンス向上 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-batch-transform-g6e-instances/

---

##### Amazon EC2 C9g/C9gd インスタンスが東京リージョンで利用可能に

AWS Graviton5プロセッサを搭載したC9gおよびC9gdインスタンスが東京リージョンに導入されました。前世代と比較して最大25%のコンピューティング性能向上を実現し、Nitro Isolation Engineによる高度なセキュリティを提供します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Graviton5, Nitro System |
| 特徴・性能 | 前世代比最大25%の性能向上、数学的に証明されたセキュリティ |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/ec2-c9g-c9gd-asia-pacific-tokyo/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Bedrockの自動同期設定の有効化 | RAG開発者 | 🔴 高 |
| ServiceNow連携の検証 | 社内ヘルプデスク担当 | 🟡 中 |
| Graviton5インスタンスへの移行検討 | インフラエンジニア | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Bedrock Managed Knowledge Base... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-managed-knowledge-base-user-managed-setup-sharepoint-onedrive-confluence/ |
| Amazon Bedrock Managed Knowledge Base... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-managed-knowledge-base-servicenow-native-data-source-connector/ |
| Amazon Bedrock Managed Knowledge Base... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-managed-knowledge-base-automatic-sync-scheduling-data-source-connectors/ |
| Amazon SageMaker AI Batch Transform... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-batch-transform-g6e-instances/ |
| Amazon EC2 C9g and C9gd instances... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/ec2-c9g-c9gd-asia-pacific-tokyo/ |
| rust-v0.154.0-alpha.4 | AI | openai_codex_cli | https://github.com/openai/codex/releases/tag/rust-v0.154.0-alpha.4 |
| Changed | AI | devin_cli | https://cli.devin.ai/docs/changelog/stable#2026-09-03-changed |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon Bedrockがデータソース連携を大幅強化！SharePoint等の個人認証対応やServiceNowのネイティブ接続、自動同期が可能に。

📌 **ピックアップ**
• Bedrock: データソース接続の簡素化と自動同期機能が追加
• SageMaker: Batch TransformがG6eインスタンスに対応
• EC2: 東京リージョンでGraviton5搭載C9gインスタンスが利用可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-09-06*
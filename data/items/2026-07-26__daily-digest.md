# Tech Radar Daily Digest - 2026-07-26

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、AIエージェントの性能を客観的かつ再現性高く評価するためのオープンソースベンチマーク「aws-bench」を発表しました。これまでAIモデルやエージェントの評価は各社独自の基準で行われることが多く、AWS環境における実用的なタスク（調査、トラブルシューティング、インフラ構築など）の遂行能力を測定する標準的な指標が求められていました。aws-benchは、実際のAWS利用状況に基づいたテストケースと、自然言語クエリに対する正解データを提供することで、開発者がモデルの改善やエージェントのパフォーマンス向上を効率的に進めることを可能にします。

また、Anthropicの最新モデル「Claude Opus 5」がAWSで利用可能となりました。コーディング能力や長期間稼働するエージェントの信頼性が大幅に向上しており、Amazon Bedrock経由ではゼロデータリテンション（ZDR）がデフォルトで有効化されるなど、エンタープライズレベルのデータガバナンス要件を満たした設計となっています。これらの発表は、AIエージェントの「実用性」と「信頼性」を重視するAWSの戦略を強く反映しており、今後の開発現場におけるAI活用がより高度化することが期待されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude / Anthropic

##### Claude Opus 5 is now available on AWS

AWS上でAnthropicの最新モデル「Claude Opus 5」が利用可能になりました。コーディングや複雑な分析タスクにおいて高い性能を発揮し、Amazon BedrockまたはClaude Platform on AWSを通じてアクセス可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Opus 5 |
| 特徴・性能 | コーディング能力向上、長期間稼働エージェント対応、ZDR対応 |
| 対応環境 | Amazon Bedrock, Claude Platform on AWS |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/claude-opus-5-aws/

---

#### Devin / Cognition

##### Redesigned Model Picker

Devinにおいて、モデル選択メニューの刷新やSlack連携の強化など、大幅なUI/UXアップデートが行われました。特にSlackからのWindowsセッション開始やネットワークアクセス承認が可能になり、開発フローの効率化が図られています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| モデルピッカー刷新 | 1つのメニューで能力、Fusion、速度、モードを統合管理可能に。 |
| Slack連携強化 | Windowsセッション開始、ネットワークアクセス承認がSlackから可能に。 |
| スラッシュコマンド | /askコマンド等の導入により、モード切り替えが容易に。 |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-07-24-redesigned-model-picker

---

### クラウド

#### AWS

##### Amazon Connect now supports audio optimization for Azure Virtual Desktop and Windows 365 Cloud PC

Amazon Connectにおいて、Azure Virtual DesktopおよびWindows 365 Cloud PC環境での音声最適化がサポートされました。メディアトラフィックを仮想デスクトップからローカルデバイスへリダイレクトすることで、通話品質が大幅に向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Connect, AVD, Windows 365 |
| 特徴・性能 | 音声品質の向上、ローカルデバイスへのメディアリダイレクト |
| 対応環境 | Azure Virtual Desktop, Windows 365 Cloud PC |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-connect/

---

##### Amazon ECS Service Connect now supports Zone-Aware routing

Amazon ECS Service Connectでゾーンアウェアルーティングがサポートされました。同一アベイラビリティゾーン（AZ）内のトラフィックを優先することで、クロスAZデータ転送コストの削減とレイテンシの改善を実現します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon ECS Service Connect |
| 特徴・性能 | 同一AZ内トラフィック優先、自動負荷分散 |
| 対応環境 | 全AWS商用リージョンおよびGovCloud |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-service-connect-zone-aware/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| ECS Service Connectの再デプロイによるゾーンアウェア化 | インフラ担当 | 🔴 高 |
| Claude Opus 5の評価とBedrockへの統合検討 | AIエンジニア | 🟡 中 |
| DevinのSlack連携設定の更新とワークフロー見直し | 開発チーム | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Connect now supports audio optimization... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-connect/ |
| Claude Opus 5 is now available on AWS | AI/LLM | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/claude-opus-5-aws/ |
| Opus 4.8, Sonnet 5... on Kiro in AWS GovCloud | AI/LLM | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/kiro-opus-sonnet-monitoring-launch-aws-govcloud-us/ |
| AWS announces aws-bench | AI/LLM | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-bench/ |
| Amazon ECS Service Connect now supports Zone-Aware routing | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-service-connect-zone-aware/ |
| v2.1.220 (Claude Code) | AI/LLM | GitHub | https://github.com/anthropics/claude-code/releases/tag/v2.1.220 |
| rust-v0.146.0-alpha.11 (Codex) | AI/LLM | GitHub | https://github.com/openai/codex/releases/tag/rust-v0.146.0-alpha.11 |
| Redesigned Model Picker (Devin) | AI/LLM | Devin | https://docs.devin.ai/release-notes/overview#2026-07-24-redesigned-model-picker |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AWSがAIエージェント評価用ベンチマーク「aws-bench」を発表、Claude Opus 5もAWSで利用可能に。

📌 **ピックアップ**
• AWS：ECS Service Connectがゾーンアウェアルーティングに対応しコスト削減へ。
• AWS：Amazon ConnectがAVD/Cloud PCでの音声最適化をサポート。
• Devin：モデルピッカー刷新やSlack連携強化など大幅アップデート。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-26*
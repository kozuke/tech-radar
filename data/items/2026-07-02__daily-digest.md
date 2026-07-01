# Tech Radar Daily Digest - 2026-07-02

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは、AIエージェント開発の信頼性と生産性を向上させるための「ADK 2.0」および「Genkit Agents API」を発表しました。ADK 2.0は、LLMの柔軟性と従来のコードによる決定論的な実行を組み合わせることで、エンタープライズ環境でのエージェントのループやハルシネーションといった課題を解決します。また、GenkitのAgents APIは、会話型AIに必要なメッセージ履歴やツールループ、永続化などの複雑な実装を共通インターフェースで抽象化し、TypeScriptやGoなどでフルスタックなエージェント開発を加速させます。

これらの発表は、AIエージェントをプロトタイプから本番環境へ移行させる際の「信頼性」と「開発効率」という二大障壁を解消するものであり、開発者がビジネスロジックに集中できる環境を整える重要な一歩となります。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / Anthropic

##### v2.1.198

Claude Codeの最新版では、ChromeでのClaude利用が一般公開され、バックグラウンドエージェントの通知機能やデータ可視化スキル（/dataviz）が追加されました。また、AWS上のClaude Platformへの対応や、エージェントの自律的なコミット・PR作成機能の強化により、開発ワークフローの自動化が大幅に向上しています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Claude in Chrome | ブラウザ上でのClaude利用が一般公開。 |
| バックグラウンド通知 | エージェントの入力待ちや完了時に通知フックが発火。 |
| /dataviz | チャートやダッシュボード設計のための可視化スキルを追加。 |
| AWS連携 | Gateway経由でAWS上のClaude Platformをプロバイダーとして利用可能に。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, Anthropic API |
| 特徴・性能 | ネットワークエラー時のリトライ強化、コンテキスト圧縮の改善 |
| 対応環境 | macOS, VS Code, CLI |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.198

---

#### Google / Gemini

##### ML Development in VS Code with Google Cloud Power

Googleは、VS Codeから直接Google CloudのWorkbench Notebooksを利用できる拡張機能をリリースしました。これにより、ローカルのIDE環境を維持したまま、クラウド上の高性能なコンピューティングリソースを活用したML開発が可能となり、コンテキストスイッチを最小限に抑えたシームレスな開発体験を提供します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Google Cloud Workbench, VS Code Extension |
| 特徴・性能 | ローカルIDEとクラウドコンピューティングの統合 |
| 対応環境 | VS Code (Jupyter拡張機能と併用) |

> 🔗 **参考リンク**
> https://developers.googleblog.com/ml-development-in-vs-code-with-google-cloud-power-workbench-extension-now-available/

---

### クラウド

#### AWS

##### Amazon Bedrock AgentCore increases default runtime quota limits

Amazon Bedrock AgentCoreのデフォルト実行クォータが引き上げられ、スケーラビリティが大幅に向上しました。これにより、US East/Westリージョンでは最大5,000の同時アクティブセッション、その他リージョンでも2,500セッションをサポートし、高スループットなAIエージェントワークロードをより容易に構築可能です。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-increases-default-runtime-quota-limits/

##### Amazon CloudWatch supports creating alarms from log queries

CloudWatchログクエリから直接アラームを作成できるようになりました。これにより、メトリクスフィルターを作成する中間ステップが不要となり、ログ分析ワークフロー内で異常検知やアラート設定を完結させることが可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-log-alarms/

---

### 開発ツール

#### Cursor

##### We've expanded (Team Marketplaces)

Cursorはチームマーケットプレイスを拡張し、Team MCPサーバーの配布や組織グループ単位でのアクセス制限をサポートしました。管理者はMCPサーバーを一元管理してIDEやCLIに配布できるため、チーム全体での開発環境の標準化とセキュリティ強化が容易になります。

> 🔗 **参考リンク**
> https://cursor.com/changelog#2026-06-30-we-ve-expanded

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude Codeの最新版(v2.1.198)へのアップデート | 開発者 | 🟡 中 |
| VS CodeへのGoogle Cloud Workbench拡張機能の導入検討 | データサイエンティスト | 🟡 中 |
| Bedrock AgentCoreのクォータ上限確認と負荷テスト | インフラエンジニア | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Bedrock AgentCore increases default runtime quota limits | クラウド | aws | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-increases-default-runtime-quota-limits/ |
| Amazon CloudWatch supports creating alarms from log queries | クラウド | aws | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-log-alarms/ |
| v2.1.198 | AI/LLM | claude_code | https://github.com/anthropics/claude-code/releases/tag/v2.1.198 |
| ML Development in VS Code with Google Cloud Power | AI/LLM | google | https://developers.googleblog.com/ml-development-in-vs-code-with-google-cloud-power-workbench-extension-now-available/ |
| Why we built ADK 2.0 | AI/LLM | google | https://developers.googleblog.com/why-we-built-adk-20/ |
| Build agentic full-stack apps with Genkit | AI/LLM | google | https://developers.googleblog.com/build-agentic-full-stack-apps-with-genkit/ |
| We've expanded | 開発ツール | cursor | https://cursor.com/changelog#2026-06-30-we-ve-expanded |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

GoogleがAIエージェント開発を加速する「ADK 2.0」と「Genkit Agents API」を発表、信頼性と効率を両立。

📌 **ピックアップ**
• Claude Code v2.1.198: Chrome対応や可視化スキル追加で自動化が進化
• VS Code: Google Cloud Workbench拡張機能でML開発がより快適に
• AWS: Bedrock AgentCoreのクォータ拡大とCloudWatchのログアラーム機能強化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-02*
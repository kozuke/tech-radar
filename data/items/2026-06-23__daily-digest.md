# Tech Radar Daily Digest - 2026-06-23

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AIエージェントの「プロアクティブ化」と評価手法の進化**
AIコーディングエージェントは、指示を待つ受動的なアシスタントから、文脈を継続的に把握し、リスクを予見して診断結果を提示する「プロアクティブ（先見的）なエンジン」へと進化しています。Googleの研究チームは、従来のタスク完了型ベンチマーク（SWE-Benchなど）では不十分であると指摘し、エージェントが「何が重要か」を判断し、いつ介入すべきかを決定する「洞察ポリシー（Insight Policy）」の評価が不可欠であると提唱しています。このアプローチでは、過去のバグ修正履歴から「高次的な目標」を抽出し、それをグラウンドトゥルースとしてエージェントの洞察を評価する手法が取られており、AI開発が単なるコード生成から、より高度なエンジニアリング支援へとシフトしていることを示しています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.186
Claude Codeの最新版では、CLI経由でのMCPサーバー認証機能の強化や、エージェントのワークフロー管理機能が拡充されました。特にSSH環境での利用を想定した非対話型ログインや、チーム開発におけるエージェント間の連携強化が図られています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| MCP認証 | `claude mcp login`コマンドによるCLI認証と、SSH環境向けの`--no-browser`サポートを追加。 |
| ワークフロー管理 | ステータスフィルタリング機能の追加や、エージェントの「スキル」セクションの可視化を実現。 |
| チーム連携 | `teammateMode`の設定追加や、サブエージェントへの権限継承の厳格化を実施。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude CLI, MCP (Model Context Protocol) |
| 特徴・性能 | ストリーミング処理の安定性向上、バックグラウンドタスクの制御改善 |
| 対応環境 | CLI環境 (iTerm2等) |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.186

---

#### OpenAI Codex (CLI)

##### 0.142.0
OpenAI Codex CLIのメジャーアップデートがリリースされ、エージェントの自律性と管理機能が大幅に強化されました。特にマルチエージェントの委任制御や、Web検索機能の統合、コスト管理機能が拡充されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| エージェント管理 | マルチエージェントの委任設定（プロアクティブ/明示的）や、トークン予算の管理機能を追加。 |
| プラグイン/検索 | リモートプラグインの整理と、URL制限付きのインデックス化されたWeb検索モードを実装。 |
| ユーティリティ | `/usage`コマンドによるクレジット管理や、UTC時刻のクエリ機能を追加。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Rust, OpenAI API |
| 特徴・性能 | 起動およびセッションレイテンシの削減、ログ出力の最適化 |
| 対応環境 | Linux, macOS, Windows (クロスプラットフォーム) |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.142.0

---

#### Google AI/Gemini

##### Google Agent Development Kit (ADK) と A2Aプロトコル
Googleは、言語の異なるエージェント同士を連携させる「Agent2Agent (A2A) プロトコル」を活用したマルチエージェント開発キットを紹介しました。これにより、Pythonで書かれた抽出エージェントとGoで書かれた検証エージェントを単一のパイプラインとして統合可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Agent2Agent (A2A) プロトコル, ADK |
| 特徴・性能 | 言語非依存のサービス間連携、リモートエージェントのローカルサブエージェント化 |
| 関連サービス | Gemini, Google Cloud |

> 🔗 **参考リンク**
> https://developers.googleblog.com/build-cross-language-multi-agent-team-with-google-agent-development-kit-and-a2a/

---

### クラウド

#### AWS

##### AWS Lambda MicroVMs
AWSは、VMレベルの隔離環境を瞬時に起動・保持できる「Lambda MicroVMs」を発表しました。Firecracker技術をベースにしており、AI生成コードやユーザー提供コードを安全かつ高速に実行するための専用環境を提供します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Firecracker, Docker |
| 特徴・性能 | VMレベルの隔離、即時起動、最大8時間の状態保持 |
| 対応環境 | AWS Lambdaコンソール, CDK, Agent Toolkit |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-microvms/

---

### Workspace

#### Google Sheets

##### Geminiによる数式エラー診断
Google SheetsにGeminiが統合され、数式エラーをワンクリックで診断・修正できるようになりました。複雑な計算式のエラー原因を自然言語で解説し、修正案を提示することで、データ分析の効率を大幅に向上させます。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/troubleshoot-formula-errors-in-sheets.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Lambda MicroVMsの検証（AIコード実行環境の構築） | クラウドエンジニア | 🔴 高 |
| Claude Code v2.1.186へのアップデートとMCP設定確認 | 開発者 | 🟡 中 |
| Google Sheetsの数式診断機能の有効化確認 | データアナリスト | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS HealthOmics now supports Nextflow profiles | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-healthomics-nextflow-profiles/) |
| AWS introduces Lambda MicroVMs | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-microvms/) |
| AWS Network Firewall updates default drop action | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-updates-default-drop-action) |
| AWS Batch now supports customer-ordered instance allocation | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/batch-ordered-allocation-strategies/) |
| AWS IAM Identity Center separate quotas | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-identity-center-separate-quotas/) |
| v2.1.186 (Claude Code) | AI/LLM | GitHub | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.186) |
| 0.142.0 (Codex) | AI/LLM | GitHub | [link](https://github.com/openai/codex/releases/tag/rust-v0.142.0) |
| Measuring What Matters with Jules | AI/LLM | Google | [link](https://developers.googleblog.com/measuring-what-matters-with-jules/) |
| Build Cross-Language Multi-Agent Team | AI/LLM | Google | [link](https://developers.googleblog.com/build-cross-language-multi-agent-team-with-google-agent-development-kit-and-a2a/) |
| Troubleshoot formula errors with Gemini | Workspace | Google | [link](http://workspaceupdates.googleblog.com/2026/06/troubleshoot-formula-errors-in-sheets.html) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AIエージェントが「タスク完了」から「先見的な洞察」へと進化、評価手法も刷新へ。

📌 **ピックアップ**
• AWS Lambda MicroVMs: AIコード実行に最適なVMレベル隔離環境が登場
• Claude Code v2.1.186: MCP認証強化とワークフロー管理機能が拡充
• Google Sheets: Geminiによる数式エラーの自動診断・修正機能が追加

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-23*
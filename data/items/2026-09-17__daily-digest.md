# Tech Radar Daily Digest - 2026-09-17

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Gemini Enterprise Agent Platformにおける「Agent Anomaly Detection」のプレビュー開始**
AIエージェントの自律性が高まる一方で、意図しないツール操作や権限の拡大といった「行動リスク」が深刻化しています。Googleが発表した「Agent Anomaly Detection」は、エージェントの推論トレースやツール呼び出しログを非同期で分析し、OWASPの「Agentic Top 10」に基づいた異常行動を検知する監査レイヤーです。特筆すべきは、ライブリクエストのパスから外れて非同期で動作するため、パフォーマンスへの影響がない点です。これにより、企業はエージェントの利便性を損なうことなく、セキュリティとガバナンスを強化できるため、エンタープライズ環境でのAI導入が加速すると期待されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.274

Claude Codeの最新アップデートでは、メモリ不足時の警告表示やMCPサーバー接続時のタイムアウト制御など、安定性と信頼性を高める修正が多数行われました。特に、セッションがループに陥る問題の自己修復機能や、大規模なプロジェクトでの言語サーバーによるパフォーマンス低下の改善が含まれています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, MCP (Model Context Protocol) |
| 特徴・性能 | メモリ警告、Postgres接続タイムアウト延長、セッション自己修復 |
| 対応環境 | CLI環境 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.274

---

#### OpenAI Codex

##### v152.2.0 および 0.155.0-alpha.11〜14

OpenAIのCodex CLIにおいて、複数のアルファ版およびマイナーアップデートがリリースされました。主に内部的なRust実装の最適化や依存関係の更新が行われており、開発者向けのCLIツールとしての安定性向上が図られています。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rusty-v8-v152.2.0

---

### クラウド

#### AWS

##### Amazon SageMaker AIがNVIDIA Nemotron 3.5 Lightningのサーバーレスカスタマイズに対応

Amazon SageMaker AIで、NVIDIAの最新モデル「Nemotron 3.5 Lightning」のサーバーレスなファインチューニングが可能になりました。SFT、DPO、RFTといった手法をサポートし、インフラ管理不要で自社データに最適化されたモデルを構築できるため、コストとレイテンシの削減に貢献します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon SageMaker, NVIDIA Nemotron 3.5 |
| 特徴・性能 | サーバーレスでのSFT/DPO/RFT対応 |
| 対応環境 | 東京リージョン含む主要リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sagemaker-ft-nemotron-3-5-lightning/

##### Amazon WorkSpacesがNVIDIA Blackwell GPUインスタンスに対応

Amazon WorkSpacesが、最新のNVIDIA RTX PRO 4500 Blackwell GPUを搭載した「Graphics G7」バンドルをサポートしました。前世代と比較して最大2.1倍のグラフィックス性能を実現し、CADや3Dレンダリング、AI支援設計などの高負荷なワークロードをクラウド上で快適に実行可能です。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-workspaces-nvidia-blackwell-gpu-instances/

---

### Workspace

#### Google Workspace

##### Google Meetホームページでの会議室・場所詳細の表示

Google Meetのホームページ上で、会議室や物理的な場所の詳細が直接確認できるようになりました。ユーザーの現在地やカレンダー設定に基づき、最適な会議室を優先表示したり、Googleマップと連携してオフサイト会議への経路案内を行ったりすることで、会議開始前の準備を効率化します。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/09/view-conference-room-and-meeting-location-details-directly-on-the-Google-Meet-homepage.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude Codeのアップデート適用 | 開発者 | 🟡 中 |
| SageMakerでのNemotron 3.5活用検討 | AIエンジニア | 🟡 中 |
| WorkSpaces G7インスタンスの検証 | インフラ管理者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon SageMaker AI... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sagemaker-ft-nemotron-3-5-lightning/ |
| AWS Client VPN... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/aws-client-vpn-macos-golden-gate/ |
| New AWS experience... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/New-AWS-Builder-Experience |
| Amazon WorkSpaces adds... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-workspaces-nvidia-blackwell-gpu-instances/ |
| Amazon Connect... | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/09/connect-customer-custom-metrics-tag/ |
| v2.1.274 | Claude Code | claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.274 |
| Agent Anomaly Detection... | Gemini | google_developers | https://developers.googleblog.com/agent-anomaly-detection-now-in-private-preview-on-the-gemini-enterprise-agent-platform/ |
| View conference room... | Workspace | google_workspace_updates | http://workspaceupdates.googleblog.com/2026/09/view-conference-room-and-meeting-location-details-directly-on-the-Google-Meet-homepage.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Gemini Enterprise Agent Platformに、AIエージェントの異常行動を検知する「Agent Anomaly Detection」がプレビュー登場。

📌 **ピックアップ**
• SageMakerがNVIDIA Nemotron 3.5のサーバーレスカスタマイズに対応
• Amazon WorkSpacesがBlackwell GPU搭載のG7インスタンスをサポート
• Claude Code v2.1.274リリースで安定性とパフォーマンスが向上

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-09-17*
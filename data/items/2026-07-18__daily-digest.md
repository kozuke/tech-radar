# Tech Radar Daily Digest - 2026-07-18

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Googleの「NotebookLM」が「Gemini Notebook」へ名称変更**
Googleは、AIを活用したリサーチツールである「NotebookLM」を「Gemini Notebook」へとリブランドすることを発表しました。この変更は単なる名称の刷新にとどまらず、今後同ツールがGoogleのエコシステム全体でより広範な役割を担い、進化していく方針を示唆しています。既存の共有ノートブックやユーザーリンクは自動リダイレクトにより引き続き利用可能であり、管理者側での特別な設定変更は不要です。

**CursorのSlack連携機能が大幅強化**
AIエディタ「Cursor」のSlack連携機能がアップデートされ、タスク実行前の計画提示やマルチリポジトリ環境への対応、チャンネル横断的なワークフローが可能になりました。特に、タスク開始前に計画を共有し、ユーザーが介入・修正できるようになった点は、AIエージェントの自律的な動作に対する信頼性と制御性を高める重要な改善です。また、Slack上でのUIも整理され、より複雑な開発環境での利用がスムーズになりました。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.212

Claude Codeの最新版では、エージェントの暴走を防ぐためのセッション制限機能が強化されました。Web検索やサブエージェントの生成回数に上限が設けられ、長時間実行されるMCPツール呼び出しは自動的にバックグラウンドへ移行するよう改善されています。また、ファイル操作を伴うBashコマンド実行時の安全性が向上し、Windows環境でのプロセス管理も最適化されました。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | セッション制限（Web検索/サブエージェント）、自動バックグラウンド処理 |
| 対応環境 | macOS, Linux, Windows |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.212

---

#### OpenAI Codex CLI

##### 各種リリース（0.144.5 / python-v0.144.4等）

OpenAIのCodex CLIにおいて、危険なコマンドの検知機能が強化され、より明確な拒否理由が提示されるようになりました。また、Python版ではAmazon Bedrock利用時のカスタムトランスポート設定がサポートされ、認証やヘッダーの柔軟なカスタマイズが可能になりました。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Codex CLI |
| 特徴・性能 | 危険コマンド検知強化、Amazon Bedrockカスタムトランスポート対応 |
| 関連サービス | Amazon Bedrock |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.144.5

---

### クラウド

#### AWS

##### Amazon GameLift StreamsのIAMロール対応

Amazon GameLift StreamsでストリームセッションにIAMロールを割り当てることが可能になりました。これにより、アプリケーションコードを変更することなく、S3やDynamoDBなどのAWSリソースへ安全にアクセスできるようになります。

##### Amazon OpenSearch UIのダッシュボード移行機能

OpenSearch Dashboardsから新しいOpenSearch UIへの移行が「ワンクリック」で可能になりました。テナントや保存済みオブジェクトをシームレスにワークスペースへ引き継ぐことができ、運用負荷が大幅に軽減されます。

##### AWS Sustainabilityの機能拡張

AWS Sustainabilityサービスにおいて、炭素排出量データに加え、年間水消費量（water withdrawals）データが確認可能になりました。リージョン、サービス、アカウント単位での可視化により、環境負荷の包括的な把握を支援します。

##### Amazon Redshiftのインスタンス拡充

RedshiftにGravitonベースの「rg.large」および「rg.12xlarge」インスタンスが追加されました。既存のRA3インスタンスと比較して最大2.4倍のクエリ性能と30%のコスト削減を実現し、ワークロードに応じた柔軟なサイジングが可能になります。

##### Amazon EC2 High Memory U7in-24TBの提供リージョン拡大

SAP HANAやSQL Serverなどのミッションクリティカルなデータベース向けである「U7in-24TB」インスタンスが、欧州（パリ）リージョンでも利用可能になりました。

---

### Workspace

#### Google Workspace

##### 週次アップデート

Google Workspaceでは、Windowsログイン時のFIDO2セキュリティキー対応や、Gmailの「Help me write」におけるカスタムリファイン機能の追加が行われました。また、Google VidsではGemini Omniモデルによる高品質な動画生成と編集機能が強化されています。

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude Codeのアップデートとセッション制限設定の確認 | 開発者 | 🟡 中 |
| OpenSearch UIへのダッシュボード移行の検討 | インフラ管理者 | 🟢 低 |
| AWS Sustainabilityでの水消費量データの確認 | サステナビリティ担当 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon GameLift Streams IAM support | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-gamelift-streams-iam/ |
| OpenSearch UI migration | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-opensearch-ui-one-click-dashboard-migration |
| AWS Sustainability water data | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-sustainability-water-withdrawals/ |
| Redshift rg instance sizes | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-adds-rg-large-12xlarge-instance-sizes |
| EC2 U7in-24TB Paris | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-high-memory-europe/ |
| Claude Code v2.1.212 | AI/LLM | GitHub | https://github.com/anthropics/claude-code/releases/tag/v2.1.212 |
| Codex CLI releases | AI/LLM | GitHub | https://github.com/openai/codex/releases |
| Google Workspace Weekly | Workspace | Google | http://workspaceupdates.googleblog.com/2026/07/weekly-recap-07-17-2026.html |
| Cursor in Slack update | 開発ツール | Cursor | https://cursor.com/changelog#2026-07-17 |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
Googleの「NotebookLM」が「Gemini Notebook」へ名称変更、CursorのSlack連携が大幅強化されました。

📌 **ピックアップ**
• Claude Codeがセッション制限機能を追加し、エージェントの暴走を防止
• AWS GameLift StreamsがIAMロール認証に対応し、セキュリティを強化
• Amazon RedshiftにGravitonベースの新しいインスタンスサイズが追加

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

*生成日: 2026-07-18*
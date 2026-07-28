# Tech Radar Daily Digest - 2026-07-29

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Google WorkspaceにおけるGeminiの統合が大幅に強化され、Google Docs内で直接ビジュアル生成・編集が可能になったほか、コメントワークフローのAI支援機能が導入されました。これにより、ユーザーはドキュメントを離れることなく、文章の文脈に基づいたインフォグラフィックや図表の作成、さらにはコメントの要約や返信案の生成が可能になります。

また、AWSではDataSyncの「Enhanced mode」がAmazon EFSやFSx for Lustre、HDFS、Azure Blob Storageなど幅広いストレージに対応しました。これにより、大規模なデータ移行やAI/機械学習のトレーニングパイプラインにおけるデータ転送の効率と柔軟性が飛躍的に向上します。これらのアップデートは、AIを活用した生産性向上と、クラウドインフラの運用効率化という現在の技術トレンドを象徴する動きと言えます。

---

## 📰 今日のニュース

### AI/LLM

#### Google Workspace

##### Generate and edit visuals with Gemini in Google Docs

Google Docs内でGeminiを使用して、ドキュメントの文脈に基づいた画像、図表、インフォグラフィックを直接生成・編集できるようになりました。自然言語プロンプトで既存のビジュアルのスタイル変更やアスペクト比の調整も可能で、外部ツールへの切り替えなしにドキュメント作成を完結できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Gemini (Google Workspace) |
| 対応環境 | Web版 Google Docs |
| 関連サービス | Google Drive |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/generate-and-edit-visuals-with-gemini-in-Google-Docs.html

---

##### Streamline collaboration in Google Docs with Gemini-powered comment workflows

Google Docsのコメント機能にGeminiが統合され、スレッドの要約や未解決課題の抽出、文脈に応じた返信案の作成が可能になりました。これにより、コラボレーションにおけるフィードバックの把握と対応が迅速化され、ドキュメント編集の生産性が向上します。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/streamline-collaboration-in-google-docs-with-Gemini-powered-comment-workflows.html

---

#### Anthropic SDK

##### Anthropic Python SDK アップデート (v0.120.1 / v0.120.2)

AnthropicのPython SDKが更新され、MCP (Model Context Protocol) SDK v2への対応や依存関係の修正が行われました。これにより、最新のMCP仕様を利用したAIエージェント開発がより安定して行えるようになります。

> 🔗 **参考リンク**
> https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.120.2

---

### 開発ツール

#### Cursor

##### Cursor Startプランの提供開始

インド市場向けに月額₹649の「Cursor Start」プランが提供開始されました。Grok 4.5モデルへのアクセスやクラウドエージェント、iOS版Cursorによるリモート制御などが含まれており、新興市場におけるAIエージェント開発の普及を加速させる狙いがあります。

> 🔗 **参考リンク**
> https://cursor.com/changelog#2026-07-28-we-re-introducing

---

### クラウド

#### AWS

##### Amazon EKS Provisioned Control Planeの高速化

EKSのProvisioned Control Planeにおいて、Horizontal Pod Autoscaler (HPA) の同期並行性が最大40倍に引き上げられました。これにより、負荷変動に対するPodのオートスケーリング応答速度が大幅に改善され、大規模クラスタの運用効率が高まります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-provisioned-control/

##### AWS DataSync Enhanced modeの機能拡張

AWS DataSyncのEnhanced modeが、EFS、FSx for Lustre、HDFS、Azure Blob Storageなどの主要ストレージに対応しました。また、Hyper-V環境へのエージェント展開もサポートされ、大規模なデータ移行やAI学習用データの転送がより柔軟かつ高速に行えるようになりました。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-datasync-amazon-efs-fsx-lustre/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Google DocsでGeminiビジュアル機能を試す | Google Workspaceユーザー | 🟡 中 |
| EKSクラスタのHPA応答性を確認する | クラウドエンジニア | 🟢 低 |
| DataSyncのEnhanced mode対応状況を確認する | データ基盤エンジニア | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EKS Provisioned Control Plane... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-provisioned-control/ |
| AWS Console Home... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-console-home-cost-and-usage-eu-sovereign-cloud |
| Second-generation AWS Outposts racks... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-outposts-asia-pacific-mumbai/ |
| AWS DataSync Enhanced mode... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-datasync-amazon-efs-fsx-lustre/ |
| AWS DataSync Enhanced mode adds HDFS... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-datasync-hdfs-azure-blob-hyper-v/ |
| Generate and edit visuals with Gemini... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/07/generate-and-edit-visuals-with-gemini-in-Google-Docs.html |
| Streamline collaboration... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/07/streamline-collaboration-in-google-docs-with-Gemini-powered-comment-workflows.html |
| v0.120.2 / v0.120.1 | AI/LLM | anthropic_sdk | https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.120.2 |
| Cursor Start | 開発ツール | cursor | https://cursor.com/changelog#2026-07-28-we-re-introducing |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Google DocsがGeminiで進化！ビジュアル生成やコメント要約が可能に。

📌 **ピックアップ**
• Google Docs: Geminiによる画像生成・編集とコメントワークフロー支援が開始
• AWS DataSync: Enhanced modeがEFS/FSx/HDFS等に対応し移行が高速化
• EKS: HPA同期並行性が40倍に向上しオートスケーリングが高速化
• Cursor: インド市場向けに新プラン「Cursor Start」が登場

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

*生成日: 2026-07-29*
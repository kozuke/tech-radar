# Tech Radar Daily Digest - 2026-07-10

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは、ブラウザ上で高性能なAI推論を実現するJavaScriptライブラリ「LiteRT.js」を発表しました。これは、オンデバイス推論ライブラリであるLiteRT（旧TensorFlow Lite）をWeb環境へ移植したもので、WebAssemblyを活用することで、従来のTensorFlow.jsよりも大幅なパフォーマンス向上を実現しています。開発者は、既存の`.tflite`モデルをWebブラウザ上で直接実行できるため、サーバーコストの削減、低遅延、そしてユーザーのプライバシー保護を両立したAIアプリケーションを構築可能です。

また、Amazon SageMaker HyperPodでは、Slurmクラスターに対して「Deep Health Checks（詳細ヘルスチェック）」機能が追加されました。これにより、トレーニング開始前にGPUアクセラレータやネットワーク接続の健全性を自動的に検証できるようになり、不健全なノードによる計算リソースの浪費を未然に防ぐことが可能になります。AIモデルの学習規模が拡大する中で、インフラの信頼性と運用効率を向上させる重要なアップデートと言えます。

---

## 📰 今日のニュース

### AI/LLM

#### Google

##### LiteRT.js, Google's high performance Web AI Inference

LiteRT.jsは、LiteRTのJavaScriptバインディングとして、Webブラウザ上でAIモデルをローカル実行するための強力なランタイムです。WebAssemblyとXNNPACK（CPU）、ML Drift（GPU）などのハードウェアアクセラレーションを活用し、Web開発者が低遅延かつセキュアなAI体験を提供できるようにします。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | WebAssembly, LiteRT, XNNPACK, WebNN |
| 特徴・性能 | ネイティブに近いハードウェアアクセラレーション、低遅延 |
| 対応環境 | モバイルおよびデスクトップWebブラウザ |

> 🔗 **参考リンク**
> https://developers.googleblog.com/litertjs-googles-high-performance-web-ai-inference/

---

#### OpenAI (Codex CLI)

##### Codex CLI リリースアップデート (v0.144.0 - v0.145.0-alpha.2)

Codex CLIの最新リリースでは、機能強化とバグ修正が多数行われました。特に「writes」アプリ承認モードの追加や、MCPツールでの対話型認証のサポートなど、開発者のワークフローを効率化する機能が拡充されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| writesモード | 読み取り専用アクションを許可しつつ、書き込み時に承認を求めるモードを追加。 |
| MCP認証 | 実験的オプションなしで、MCPツールが対話的に認証を要求可能に。 |
| 互換性修正 | GitHubのメタデータ変更に対するインストール処理の信頼性向上。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Rust, CLI, MCP (Model Context Protocol) |
| 関連サービス | ChatGPT, Amazon Bedrock |

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases

---

### クラウド

#### AWS

##### Amazon Timestream for InfluxDB: EventBridge連携

Amazon Timestream for InfluxDBが、データベースの状態変化イベントをAmazon EventBridgeに発行するようになりました。これにより、スケーリング完了や障害発生などのイベントをトリガーに、LambdaやStep Functionsを用いた自動化ワークフローを容易に構築できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/timestream-influxdb-eventbridge/

##### AWS Client VPN: 4つの新リージョンに対応

AWS Client VPNが、カナダ（カルガリー）、メキシコ（セントラル）、ニュージーランド、台北の4つの新しいAWSリージョンで利用可能になりました。リモートワーク環境のセキュアな接続を、より広範な地域で展開できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-client-vpn-four-additional-regions/

##### Amazon SageMaker: 関連機能のアップデート

SageMaker Unified StudioおよびFeature Storeにおいて、管理機能やデータ取り込みの効率化が図られました。特にFeature Storeのバッチ書き込み機能は、高スループットなデータインジェクションを可能にします。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| カスタムアセットタイプ | SageMaker Unified Studioで任意の形式の資産をカタログ化可能に。 |
| BatchWriteRecord | 複数のレコードを単一リクエストで書き込み、高スループットを実現。 |
| ListRecords | レコードIDを知らなくてもFeature Store内のレコードを一覧・監査可能に。 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/smus-custom-asset-types-iam/

---

### Workspace

#### Google Workspace

##### Inbound SCIMサポートの一般提供開始

Google Workspaceで、SCIMプロトコルを用いたインバウンド同期が一般提供されました。外部のIDプロバイダー（IdP）や人事システム（HRIS）とディレクトリをリアルタイムで同期し、ユーザーのプロビジョニングや権限管理を自動化することで、セキュリティと管理効率を向上させます。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/streamline-identity-lifecycle-management-in-Google-Workspace-with-new-inbound-SCIM-support.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| LiteRT.jsのデモを確認し、Web AIの導入を検討する | Web開発者 | 🟡 中 |
| SageMaker HyperPodのDeep Health Checkを有効化する | MLエンジニア | 🔴 高 |
| Google WorkspaceのInbound SCIM設定を確認・導入する | IT管理者 | 🔴 高 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Timestream for InfluxDB... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/timestream-influxdb-eventbridge/ |
| AWS Client VPN extends availability... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-client-vpn-four-additional-regions/ |
| Amazon SageMaker Unified Studio... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/smus-custom-asset-types-iam/ |
| Amazon SageMaker HyperPod... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/deep-health-check-continuous-slurm/ |
| Amazon SageMaker Feature Store... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/07/amzn-sgm-feature-store-batch-write-list/ |
| Codex CLI Releases (v0.144.0-v0.145.0) | AI/LLM | OpenAI | https://github.com/openai/codex/releases |
| LiteRT.js, Google's high performance... | AI/LLM | Google | https://developers.googleblog.com/litertjs-googles-high-performance-web-ai-inference/ |
| Streamline identity lifecycle... | Workspace | Google | http://workspaceupdates.googleblog.com/2026/07/streamline-identity-lifecycle-management-in-Google-Workspace-with-new-inbound-SCIM-support.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
GoogleがWebブラウザ向け高性能AI推論ライブラリ「LiteRT.js」を発表。

📌 **ピックアップ**
• LiteRT.js: WebAssembly活用でブラウザAI推論を高速化
• SageMaker HyperPod: Slurmクラスターの健全性チェック機能を追加
• Google Workspace: Inbound SCIM対応でID管理を自動化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-10*
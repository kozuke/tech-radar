# Tech Radar Daily Digest - 2026-06-03

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Kubernetes 1.36のサポート開始とAWSサービスの機能強化**
AWSは、Amazon EKSおよびEKS DistroにおいてKubernetes 1.36のサポートを開始しました。今回のバージョンでは、コンテナのルート権限をホスト側の非特権ユーザーにマッピングする「User Namespaces」が正式リリースされたほか、Podの再起動なしでCPU/メモリのリソースを調整できる「In-Place Pod-Level Resources Vertical Scaling」が導入され、運用効率が大幅に向上します。また、AWS Configでは「内部サービスリンクルール」がサポートされ、Security HubなどのAWSサービスが独自にルール評価を管理できるようになり、より統合されたセキュリティ運用が可能となりました。これらのアップデートは、クラウドネイティブな環境におけるスケーラビリティとセキュリティの両面を強化する重要な一歩です。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.161 / v2.1.160

Claude Codeの最新アップデートでは、テレメトリの強化やUIの改善に加え、セキュリティ面での重要な変更が行われました。特にシェル起動ファイルやビルドツール設定ファイルへの書き込み時にユーザーへの確認を求める仕様が追加され、意図しないコード実行を防止する安全対策が強化されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| セキュリティ強化 | シェル起動ファイルやビルド設定ファイルへの書き込み時に確認プロンプトを表示。 |
| テレメトリ | OTELリソース属性をメトリクスラベルに追加し、チームやリポジトリ単位での分析が可能に。 |
| UI/UX改善 | 実行中のエージェントの進捗表示や、未使用コネクタの折りたたみ表示に対応。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI, OpenTelemetry |
| 対応環境 | Linux, Windows, macOS |

> 🔗 **参考リンク**
> [https://github.com/anthropics/claude-code/releases](https://github.com/anthropics/claude-code/releases)

---

#### Devin

##### 宣言的構成への移行とエンタープライズ機能の拡充

Devinは、従来の環境設定を廃止し、宣言的構成（ブループリント）へ完全に移行することを発表しました。また、エンタープライズ向けにシークレット管理やビルドのピン留め、MCPサーバーの許可リスト設定など、ガバナンスと運用管理を強化する機能が多数追加されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| 宣言的構成 | 従来の環境設定を廃止し、ブループリントによる構成管理へ移行。 |
| エンタープライズ管理 | シークレット管理、ビルドのピン留め、MCPサーバーの許可リスト設定を追加。 |
| Devin Review | PR内のバグをワンクリックで修正する「Auto-fix」ボタンを実装。 |

> 🔗 **参考リンク**
> [https://docs.devin.ai/release-notes/overview](https://docs.devin.ai/release-notes/overview)

---

### クラウド

#### AWS

##### Amazon ElastiCache for Valkeyの耐久性サポート

Amazon ElastiCache for Valkeyにおいて、データ損失を許容できないワークロード向けに耐久性オプションが追加されました。マルチAZでのトランザクションログ記録により、フェイルオーバー時や再起動時のデータ保護が可能となり、AIエージェントの長期記憶やリアルタイム在庫管理など、より広範な用途での利用が期待されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Valkey 9.0, Multi-AZ |
| 特徴・性能 | 同期書き込み（データ損失ゼロ）と非同期書き込み（マイクロ秒レイテンシ）を選択可能 |

> 🔗 **参考リンク**
> [https://aws.amazon.com/about-aws/whats-new/2026/06/durability-amazon-elasticache](https://aws.amazon.com/about-aws/whats-new/2026/06/durability-amazon-elasticache)

---

### Workspace

#### Google Workspace

##### Workspace Studioでのループ処理機能追加

Google Workspace Studioのフローにおいて、リスト形式のデータに対するループ処理が可能になりました。「Ask Gemini」ステップの出力形式をリストに設定し、「Repeat for each」ステップを使用することで、Googleスプレッドシートの行ごとの処理や、会議メモからのタスク一括作成などが自動化できます。

> 🔗 **参考リンク**
> [http://workspaceupdates.googleblog.com/2026/06/introducing-ability-to-loop-over-list-of-items-in-Workspace-Studio.html](http://workspaceupdates.googleblog.com/2026/06/introducing-ability-to-loop-over-list-of-items-in-Workspace-Studio.html)

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| EKSクラスターの1.36へのアップグレード計画策定 | クラウドエンジニア | 🟡 中 |
| Claude Codeの最新版へのアップデートとセキュリティ設定確認 | 開発者 | 🔴 高 |
| Devinの宣言的構成（ブループリント）への移行準備 | Devin利用者 | 🔴 高 |
| ElastiCacheの耐久性オプションの評価 | インフラエンジニア | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon EKS... Kubernetes 1.36 | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-eks-distro-kubernetes-version-1-36) |
| AWS Config... internal service linked rules | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-config-supports-internal-service-linked-rules) |
| AWS Deadline Cloud... persistent storage | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/deadline-cloud/persistent-storage) |
| Amazon SageMaker Studio... quick setup | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/01/quick-setup-model-customization-sagemaker-studio/) |
| Amazon ElastiCache for Valkey... durability | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/durability-amazon-elasticache) |
| v2.1.161 / v2.1.160 | AI/LLM | Claude | [URL](https://github.com/anthropics/claude-code/releases) |
| rust-v0.137.0-alpha.1-3 | AI/LLM | OpenAI | [URL](https://github.com/openai/codex/releases) |
| Loop over list in Workspace Studio | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/06/introducing-ability-to-loop-over-list-of-items-in-Workspace-Studio.html) |
| Migrating to declarative configuration | AI/LLM | Devin | [URL](https://docs.devin.ai/release-notes/overview) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AWSがKubernetes 1.36のサポートを開始し、EKSでの運用効率が大幅に向上しました。

📌 **ピックアップ**
• Claude Code: セキュリティ強化とUI改善を含む最新版リリース
• Devin: 宣言的構成への移行とエンタープライズ管理機能の拡充
• ElastiCache: Valkey向けに耐久性オプション（マルチAZ）を提供開始
• Workspace Studio: リストデータのループ処理が可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

*生成日: 2026-06-03*
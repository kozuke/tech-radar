# Tech Radar Daily Digest - 2026-11-12

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは、生成AIエージェントが対話だけでなく、インタラクティブなUIを直接生成・表示するためのオープンプロトコル「A2UI 1.0」を正式リリースしました。これまでのAIエージェントはテキストベースの回答が主流でしたが、A2UIを用いることで、エージェントがフォームやチャートなどの動的なUIコンポーネントを提示できるようになります。開発者はWeb、Android、iOS向けのSDKを活用して、ブランドの設計システムに準拠したUIを構築でき、ユーザーはGeminiやClaudeなどのAIアシスタント上で、より直感的かつ効率的な操作が可能になります。

また、AWSはSageMaker JumpStartにおいて、DeepSeek-V4シリーズおよびOrnith-1.0シリーズという強力なオープンウェイトモデル群の提供を開始しました。特にDeepSeek-V4.1-Flashは、独自のCEDアーキテクチャとFP4 KVキャッシュ技術により、エージェントワークロードにおけるコスト効率と推論速度を大幅に向上させています。これらのモデルは、単一のコンシューマー向けGPUでも動作可能な設計となっており、開発者が最先端のAI機能を低コストで本番環境に導入できる環境が整いつつあります。

---

## 📰 今日のニュース

### AI/LLM

#### Google

##### A2UI 1.0: Build delightful, fast, reliable, agentic experiences

A2UI 1.0は、AIエージェントがテキストだけでなくインタラクティブなUIを生成・表示するためのオープンプロトコルです。このプロトコルにより、ユーザーはAIとの対話の中で直接フォーム入力やデータ確認が可能になり、エージェント体験の質が劇的に向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | A2UIプロトコル、生成UI (Generative UI) |
| 対応環境 | Web, Android, iOS (レンダラーSDK), Python, TypeScript, Dart (エージェントSDK) |
| 関連サービス | Gemini, Claude (MCP対応アプリ) |

> 🔗 **参考リンク**
> https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/

---

#### AWS（AIモデル）

##### Ornith-1.0-9B and Ornith-1.0-35B models now available on Amazon SageMaker JumpStart

DeepReinforce AIのオープンソース・エージェント型コーディングモデル「Ornith-1.0」シリーズがSageMaker JumpStartに追加されました。9Bおよび35Bのモデルは、強化学習を用いてコード生成の最適化を行っており、単一GPU環境でも高いコーディング性能を発揮します。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Ornith-1.0-9B | Qwen 3.5ベースの軽量モデル。256Kトークンのコンテキストを持ち、ノートPC等の単一GPUで動作可能。 |
| Ornith-1.0-35B | MoEアーキテクチャを採用したモデル。高い性能と効率を両立し、エージェントワークロードに適した設計。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | 強化学習 (RL), Mixture-of-Experts (MoE) |
| 特徴・性能 | Terminal-Bench 2.1等でSOTA性能を記録 |
| 対応環境 | Amazon SageMaker JumpStart |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/01/ornith-1-0-9b-ornith-1-0-35b-on-sagemaker-jumpstart/

---

##### DeepSeek-V4-Pro, DeepSeek-V4-Flash, and DeepSeek-V4.1-Flash models now available on Amazon SageMaker JumpStart

DeepSeekの最新MoEモデル群がSageMaker JumpStartで利用可能になりました。推論、コーディング、マルチモーダルタスクに特化したモデルが提供され、特にV4.1-Flashは圧縮技術により高いコスト効率を実現しています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| DeepSeek-V4-Pro | 1.6Tパラメータのフラッグシップモデル。1Mトークンのコンテキストで複雑な推論に対応。 |
| DeepSeek-V4-Flash | 284Bパラメータの効率重視モデル。低コストで高速な推論が可能。 |
| DeepSeek-V4.1-Flash | マルチモーダル対応の次世代エージェントモデル。CSA2技術でKVキャッシュを大幅削減。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Mixture-of-Experts (MoE), Causal Encoder-Decoder (CED) |
| 特徴・性能 | FP4 KVキャッシュによるメモリ効率化 |
| 対応環境 | Amazon SageMaker JumpStart |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/01/deepseek-v4-pro-v4-flash-v4.1-flash-on-sagemaker-jumpstart/

---

### クラウド

#### AWS

##### AWS Network Security Manager now available in AWS European Sovereign Cloud and Additional New Regions

AWS Network Security Managerが欧州Sovereign Cloudを含む31の新しいリージョンで利用可能になりました。WAFやShieldのセキュリティポリシーを大規模かつ自動的に管理・適用できるため、運用負荷の軽減と一貫したセキュリティ体制の構築が可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS WAF, AWS Shield, セキュリティ自動化 |
| 対応環境 | AWS European Sovereign Cloud, その他31リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/network-security-mgr-eu-sovereign-cloud/

---

##### AWS Cloud WAN now supports Flow Logs

AWS Cloud WANでVPC Flow Logsがサポートされました。これにより、グローバルネットワーク全体を流れるトラフィックを中央で可視化でき、トラブルシューティングやセキュリティ監査が容易になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | VPC Flow Logs, Cloud WAN |
| 関連サービス | Amazon CloudWatch Logs, S3, Data Firehose |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/aws-cloud-wan-flow-logs/

---

##### Amazon EKS Provisioned Control Plane now offers a 24 GB etcd database on 4XL and 8XL tiers

Amazon EKSのProvisioned Control Planeにおいて、etcdデータベースの容量が16GBから24GBへ50%拡大されました。大規模なAI/MLワークロードやCI/CDパイプラインなど、大量のKubernetesオブジェクトを扱う環境での安定性が向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon EKS, etcd |
| 対応環境 | EKS v1.34以降 (4XL/8XL tier) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-provisioned-control-plane-larger-etcd-database/

---

### Workspace

#### Google Workspace

##### Publish a Sheets canvas as a standalone link

Google Sheetsの「canvas」機能で作成したミニアプリを、元のスプレッドシートを共有することなく、読み取り専用の単独リンクとして公開できるようになりました。プロジェクトの進捗やダッシュボードを関係者に安全に共有する際に役立ちます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Google Sheets canvas, Gemini |
| 対応環境 | Google Sheets (Web) |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/11/publish-sheets-canvas-as-standalone-link.html

---

##### Organize and communicate complex information with numbered and nested lists in Google Chat

Google Chatで番号付きリストおよびネストされたリストが利用可能になりました。プロジェクト計画や会議メモなど、複雑な情報を構造化して伝えることができ、最大5レベルまでのネストに対応しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Markdown, Google Chat API |
| 対応環境 | Web, Android, iOS |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/11/organize-and-communicate-complex-information-with-numbered-and-nested-lists-in-Google-Chat.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| A2UI 1.0のドキュメントを確認し、エージェントUIの導入を検討する | AI開発者 | 🔴 高 |
| SageMaker JumpStartでDeepSeek-V4/Ornithモデルを試用する | AIエンジニア | 🟡 中 |
| EKS 4XL/8XL環境のetcd容量拡大を確認し、必要に応じて設定を確認する | インフラエンジニア | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Ornith-1.0-9B and Ornith-1.0-35B models... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/ornith-1-0-9b-ornith-1-0-35b-on-sagemaker-jumpstart/ |
| DeepSeek-V4-Pro, DeepSeek-V4-Flash... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/deepseek-v4-pro-v4-flash-v4.1-flash-on-sagemaker-jumpstart/ |
| AWS Network Security Manager... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/network-security-mgr-eu-sovereign-cloud/ |
| AWS Cloud WAN now supports Flow Logs | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/aws-cloud-wan-flow-logs/ |
| Amazon EKS Provisioned Control Plane... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-provisioned-control-plane-larger-etcd-database/ |
| 0.170.0-alpha.2 | AI/LLM | openai_codex | https://github.com/openai/codex/releases/tag/rust-v0.170.0-alpha.2 |
| 0.170.0-alpha.1 | AI/LLM | openai_codex | https://github.com/openai/codex/releases/tag/rust-v0.170.0-alpha.1 |
| 0.169.0-alpha.11.1 | AI/LLM | openai_codex | https://github.com/openai/codex/releases/tag/rust-v0.169.0-alpha.11.1 |
| 0.169.0-alpha.11 | AI/LLM | openai_codex | https://github.com/openai/codex/releases/tag/rust-v0.169.0-alpha.11 |
| 0.167.2 | AI/LLM | openai_codex | https://github.com/openai/codex/releases/tag/rust-v0.167.2 |
| A2UI 1.0: Build delightful... | AI/LLM | google_developers | https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/ |
| Publish a Sheets canvas as a standalone link | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/11/publish-sheets-canvas-as-standalone-link.html |
| Organize and communicate complex information... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/11/organize-and-communicate-complex-information-with-numbered-and-nested-lists-in-Google-Chat.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

GoogleがAIエージェント向けUIプロトコル「A2UI 1.0」を公開、対話型UIの進化が加速。

📌 **ピックアップ**
• Google: AIエージェントがインタラクティブな画面を生成する「A2UI 1.0」をリリース。
• AWS: SageMaker JumpStartでDeepSeek-V4やOrnith-1.0など最新AIモデル群が利用可能に。
• AWS: Cloud WANのFlow Logs対応やEKSのetcd容量拡大などクラウド基盤も強化。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-12*
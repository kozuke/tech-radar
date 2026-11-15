# Tech Radar Daily Digest - 2026-11-15

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWS Systems Managerの「Cloud Connector」がGoogle Cloudに対応し、マルチクラウド環境の運用管理が大幅に効率化されました。これまでAWS、オンプレミス、Azureを対象としていた集中管理機能がGoogle Cloud上の仮想マシンにも拡張され、エージェントの手動インストールなしでSSM Agentの自動デプロイが可能になります。これにより、パッチ管理や自動化ランブック、セッションマネージャーといった運用ワークフローを、クラウドプロバイダーを跨いで単一のインターフェースで統合できるため、運用負荷の低減とガバナンスの標準化が期待されます。

また、AIエンジニアリングツール「Devin」のアップデートも注目です。UIのドイツ語対応に加え、ワークスペースの操作性が大幅に改善されました。特に、生成物（Artifacts）をチャット横のコンパクトなレールに集約するUI変更や、セッションファイルエディタの保存方式の明示化（Cmd/Ctrl+S）など、開発者のワークフローに直結するUXの洗練が進んでいます。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### AWS Secrets Manager now supports cross-account replication

AWS Secrets Managerがアカウント間レプリケーションに対応し、プライマリシークレットの同期コピーを別のアカウントに保持できるようになりました。これにより、共有KMSキーや複雑なポリシー設定なしで、バックアップや災害復旧、あるいはセキュリティ分離された環境でのシークレット利用が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Secrets Manager, AWS KMS |
| 特徴・性能 | 自動同期、独立したリソースとしての管理 |
| 対応環境 | Secrets Manager対応全リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-manager-cross-account/

##### Amazon SageMaker Unified Studio now supports layout customization for designations

SageMaker Unified Studioにおいて、ユーザーの役割（Designation）に応じたUIレイアウトのカスタマイズが可能になりました。管理者はデータエンジニアやMLエンジニアといった役割ごとに表示するツールを制御でき、プロジェクトメンバーは自身の役割に必要な機能のみにアクセスできるため、ガバナンスと操作性が向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon SageMaker Unified Studio |
| 特徴・性能 | 役割ベースのナビゲーション制御 |
| 対応環境 | SageMaker Unified Studio対応全リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-studio-layout-customization/

##### AWS Batch on Amazon EKS adds Linux capabilities, seccomp, and pod-level settings

AWS Batch on Amazon EKSが、Linux機能やseccompプロファイルなどの高度なKubernetesセキュリティコンテキスト設定をサポートしました。これにより、Pod Security Standardsの制限付きプロファイルを適用する環境において、最小権限の原則に基づいた安全なジョブ実行が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Batch, Amazon EKS, Kubernetes |
| 特徴・性能 | セキュリティコンテキストのきめ細かな制御 |
| 対応環境 | AWS Batch対応全リージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/

##### AWS Marketplace now supports VAT credit notes for deemed supply refunds

AWS Marketplaceのセラー向けに、VAT（付加価値税）クレジットノートのセルフサービス提出機能が追加されました。返金時のVAT文書作成プロセスが簡素化され、AWS Partner Centralを通じて直接処理が可能になったことで、事務作業の効率化と透明性が向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Marketplace, AWS Partner Central |
| 特徴・性能 | VAT返金処理のセルフサービス化 |
| 対応環境 | EU加盟国、ノルウェー、英国 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/aws-marketplace-vat-credit-notes/

### AI/LLM

#### Devin

##### German UI Language

DevinのUIがドイツ語に対応し、開発現場で使われる専門用語を反映したローカライズが提供されました。また、Artifactsの表示レール化やエディタの保存操作の変更など、UI/UXの大幅な刷新が行われ、より効率的な開発体験を実現しています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| UI言語設定 | ドイツ語（Deutsch）の選択が可能に。 |
| ワークスペースUI | 生成物をチャット横のレールに集約し、視認性を向上。 |
| セッション管理 | ファイル保存を自動から手動（Cmd/Ctrl+S）へ変更。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Devin AI Agent |
| 特徴・性能 | GitLab Merge Trains対応、レビュー分析機能強化 |
| 対応環境 | Webブラウザ |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-11-13-german-ui-language

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Google Cloud VMのSSM管理統合の検証 | インフラ管理者 | 🔴 高 |
| Secrets Managerのクロスアカウントレプリケーション設定確認 | セキュリティ担当 | 🟡 中 |
| Devinの新しいUI操作（保存方法・Artifacts）の習熟 | 開発者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Secrets Manager now supports cross-account replication | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-manager-cross-account/ |
| Amazon SageMaker Unified Studio now supports layout customization | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-studio-layout-customization/ |
| AWS Batch on Amazon EKS adds Linux capabilities | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/ |
| AWS Marketplace now supports VAT credit notes | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/aws-marketplace-vat-credit-notes/ |
| AWS Systems Manager simplifies onboarding of Google Cloud VMs | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/11/systems-manager-google-cloud-support/ |
| German UI Language | AI | Devin | https://docs.devin.ai/release-notes/overview#2026-11-13-german-ui-language |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWS Systems ManagerがGoogle Cloudに対応し、マルチクラウド管理がよりシームレスに。

📌 **ピックアップ**
• AWS Secrets Managerがアカウント間レプリケーションをサポート
• SageMaker Unified Studioで役割に応じたUIレイアウトが可能に
• AIツール「Devin」がUIを刷新、Artifactsのレール表示などで操作性が向上

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-15*
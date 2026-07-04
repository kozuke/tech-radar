# Tech Radar Daily Digest - 2026-07-05

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Amazon EKSにおけるKubernetesバージョンロールバック機能のサポートは、運用上の安全性と柔軟性を大きく向上させる重要なアップデートです。これまで、一度アップグレードしたクラスターのバージョンを戻すことは困難でしたが、本機能によりアップグレード後7日以内であれば以前のマイナーバージョンへ安全にロールバックが可能となりました。

この機能は、API互換性やアドオンの整合性などを自動チェックする「ロールバック準備状況インサイト」と連携しており、リスクを最小限に抑えた運用を支援します。特にEKS Auto Modeを利用している場合は、ワーカーノードの復旧まで自動化されるため、本番環境でのアップグレードに伴う心理的・技術的ハードルが大幅に下がることが期待されます。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### Amazon ECS Express Mode now supports custom task definitions

Amazon ECS Express Modeがカスタムタスク定義に対応しました。これにより、既存のCI/CDパイプラインやインフラ構成を維持しつつ、Express Modeの簡便なデプロイ体験を享受できるようになります。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| カスタムタスク定義 | 既存のECS設定や高度なタスクレベルのカスタマイズをExpress Modeで利用可能。 |
| 高度な拡張 | 可観測性・セキュリティサイドカー、カスタムヘルスチェック、FireLensによるログルーティング等に対応。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon ECS Express Mode |
| 対応環境 | 全AWSリージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-express-mode-custom-task-def/

---

##### Amazon EKS now supports Kubernetes version rollback

Amazon EKSでKubernetesのバージョンロールバックが可能になりました。アップグレード後に問題が発生した場合、7日以内であれば以前のマイナーバージョンへ安全に戻すことができます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon EKS, Kubernetes |
| 特徴・性能 | ロールバック準備状況インサイトによる自動チェック、EKS Auto Modeでの自動復旧 |
| 対応環境 | 全AWSリージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-version-rollback

---

##### Amazon Managed Service for Prometheus achieves FedRAMP High and DoD IL-4/5 authorization in AWS GovCloud (US)

Amazon Managed Service for Prometheusが、AWS GovCloud (US)においてFedRAMP HighおよびDoD IL-4/5の認証を取得しました。これにより、高いセキュリティ基準が求められる政府機関や公共セクターの組織でも、スケーラブルな監視環境を安心して利用可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-prometheus-fedramp-high/

---

##### AWS Security Agent now available in Asia Pacific (Mumbai), Asia Pacific (Singapore), and South America (São Paulo)

AWS Security Agent（AWS Continuumの一部）が新たに3つのリージョンで利用可能になりました。STRIDEベースの脅威モデリングやコードレビュー、ペネトレーションテストなどのセキュリティ機能を開発ライフサイクルに統合できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-agent-asia-pacific/

---

##### Amazon RDS for Db2 now supports self-managed Active Directory

Amazon RDS for Db2が、セルフマネージド型のActive Directory（AD）と直接ドメイン参加できるようになりました。Kerberos認証を用いたシングルサインオンが可能になり、AWS Managed Microsoft ADを介さず既存のIDインフラを直接活用できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-rds-db2-supports-self-managed-active-directory

---

### AI/LLM

#### Claude Code

##### v2.1.201

Claude Codeの最新バージョンv2.1.201がリリースされました。今回のアップデートでは、Claude Sonnet 5セッションにおいて、会話の途中で発生していた不要なシステムロールによるハーネスリマインダーが抑制されるよう改善されています。

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.201

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| EKSアップグレード手順へのロールバック計画の追加 | クラウドエンジニア | 🔴 高 |
| ECS Express Modeでのカスタムタスク定義の検証 | アプリケーション開発者 | 🟡 中 |
| RDS for Db2のAD認証設定の最適化（セルフマネージドAD移行） | DB管理者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon ECS Express Mode now supports custom task definitions | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-express-mode-custom-task-def/ |
| Amazon EKS now supports Kubernetes version rollback | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-version-rollback |
| Amazon Managed Service for Prometheus... | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-prometheus-fedramp-high/ |
| AWS Security Agent now available... | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-agent-asia-pacific/ |
| Amazon RDS for Db2 now supports self-managed Active Directory | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-rds-db2-supports-self-managed-active-directory |
| v2.1.201 | Claude Code | rss:claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.201 |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon EKSで待望の「Kubernetesバージョンロールバック」機能がサポートされました。

📌 **ピックアップ**
• EKS: アップグレード後7日以内のバージョン戻しが可能に
• ECS: Express Modeがカスタムタスク定義に対応
• RDS for Db2: セルフマネージドADとの直接連携をサポート
• Claude Code: v2.1.201リリースでセッション挙動を改善

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-05*
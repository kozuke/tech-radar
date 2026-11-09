# Tech Radar Daily Digest - 2026-11-09

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、Amazon FSx for LustreのIntelligent-Tieringストレージクラスにおいて、メタデータIOPSを従来の12,000から192,000へと16倍に引き上げました。この大幅な性能向上により、ファイルやディレクトリの作成・リスト・読み取り・削除といったメタデータ操作が劇的に高速化されます。特に、膨大な数のファイルを扱う機械学習研究やHPC（ハイパフォーマンスコンピューティング）ワークロードにおいて、処理時間の短縮とストレージコストの最適化が期待されます。

また、Devin（AIエージェント）の大規模なアップデートが実施されました。サイドバーのUI改善やサイドチャットのキューイング機能、Gerrit連携の強化、エンタープライズ向けの管理機能拡充など、開発効率と組織的な運用を支援する機能が多数追加されています。AIエージェントがより複雑な開発ワークフローに深く統合され、実用性が一段と高まっています。

---

## 📰 今日のニュース

### AI/LLM

#### Devin

##### Devinの機能アップデート（2026-11-06）

Devinのサイドバーに「子セッションを表示」スイッチが追加され、セッション管理が整理されました。また、サイドチャットでのメッセージキューイングや、APIキー取得時のステップバイステップガイド表示など、AIとの対話および開発体験を向上させる機能が多数実装されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| セッション管理 | サイドバーの「子セッションを表示」スイッチで親子関係の表示を制御可能に。 |
| サイドチャット | 実行中のサイドチャットに対してメッセージの割り込みやキューイングが可能に。 |
| 連携・認証 | Gerritの権限同期やJira管理接続のアプリ内完結など、外部ツールとの連携を強化。 |
| エンタープライズ | セッション共有のデフォルト設定や組織ごとのアクセス制限、マシンカタログの可視化を改善。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AIエージェント, Gerrit, Jira, MCP |
| 特徴・性能 | 開発ワークフローの自動化と組織管理の強化 |
| 対応環境 | Webブラウザ（Devinアプリ） |
| 関連サービス | GitHub, GitLab, Gerrit, Jira |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-11-06-reveal-child-sessions-switch-in-the-sidebar

---

### クラウド

#### AWS

##### IAM Roles Anywhereが証明書失効チェックを自動化

IAM Roles Anywhereが、証明書失効リスト（CRL）配布ポイント（CDP）を使用した自動失効チェックに対応しました。これにより、手動でCRLをインポートし直す運用負荷が解消され、セキュリティ体制が強化されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | IAM Roles Anywhere, PKI, CRL |
| 特徴・性能 | CDP URLからの自動ダウンロードと定期的なリフレッシュ |
| 対応環境 | AWS全商用リージョン |
| 関連サービス | AWS Private Certificate Authority |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/iam-roles-anywhere-cdp/

##### Amazon OpenSearch Serviceがエージェントトレースをサポート

OpenSearch Serviceの最適化エンジンがOpenTelemetryトレースを含むエージェントトレースに対応しました。ログとトレースを同一プラットフォームで管理可能になり、ツールを切り替えることなくリクエストやエージェントセッションの追跡、障害箇所の特定が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | OpenSearch 3.7, OpenTelemetry |
| 特徴・性能 | ログとトレースの統合管理、ネスト構造の保持 |
| 対応環境 | 特定のAWSリージョン（東京含む） |
| 関連サービス | Amazon OpenSearch Ingestion |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-service-support-traces

##### Amazon RDS for OracleがセルフマネージドActive Directory認証に対応

RDS for Oracleが、AWS Managed Microsoft ADを介さずに、オンプレミスやEC2上のセルフマネージドActive Directoryと直接連携できるようになりました。Kerberos認証を利用したユーザー認証・認可がよりシンプルに構成可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Kerberos, Active Directory |
| 特徴・性能 | 信頼関係の設定不要で直接ドメイン参加が可能 |
| 対応環境 | RDS for Oracleが利用可能な全商用リージョン |
| 関連サービス | Amazon RDS, Microsoft Active Directory |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-kerberos-self-managed-ad/

##### AWS Security Hub Network ScanningがGovCloud (US)で利用可能に

インターネットからの到達性を実際にスキャンするNetwork Scanning機能が、AWS GovCloud (US)でも利用可能になりました。設定上の到達可能性だけでなく、実際にポートが公開されているかを検出し、リスクを自動的に相関分析します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Security Hub, ネットワークスキャン |
| 特徴・性能 | 実際の到達性確認とリスクの自動相関分析 |
| 対応環境 | AWS GovCloud (US) |
| 関連サービス | AWS Security Hub Essentials |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-network-scanning-govcloud/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| FSx for Lustreのメタデータ性能検証 | HPC/MLエンジニア | 🔴 高 |
| IAM Roles AnywhereのCRL自動チェック有効化 | セキュリティ管理者 | 🟡 中 |
| Devinのサイドチャット・キュー機能の試用 | 開発者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| IAM Roles Anywhere now supports automatic certificate revocation checking | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/iam-roles-anywhere-cdp/ |
| Amazon OpenSearch Service optimized engine now supports agent traces | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-service-support-traces |
| Amazon FSx for Lustre delivers 16x higher metadata IOPS | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-fsx-for-lustre-intelligent-tiering-16x-higher-metadata-iops |
| Amazon RDS for Oracle now supports Kerberos authentication with self-managed Active Directory | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-kerberos-self-managed-ad/ |
| AWS Security Hub Network Scanning now available in AWS GovCloud (US) | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-network-scanning-govcloud/ |
| “Reveal Child Sessions” Switch in the Sidebar | Devin | scrape:devin_release_notes | https://docs.devin.ai/release-notes/overview#2026-11-06-reveal-child-sessions-switch-in-the-sidebar |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon FSx for LustreがメタデータIOPSを16倍に強化し、AI/HPCワークロードの処理を高速化。

📌 **ピックアップ**
• AWS: IAM Roles Anywhereが証明書失効チェックを自動化。
• AWS: OpenSearchがエージェントトレースに対応し、ログ統合を強化。
• Devin: サイドバーUI改善やGerrit連携など、AI開発体験が大幅向上。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-09*
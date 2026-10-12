# Tech Radar Daily Digest - 2026-10-12

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Amazon GuardDutyのRDS Protectionが大幅に強化され、ログイン異常だけでなく、データ流出や破壊といった悪意あるクエリパターンの検知が可能になりました。これまで、データベースに対する攻撃は正規のアプリケーション挙動と見分けがつきにくく、検知が困難でしたが、本機能は機械学習を用いて正常なクエリパターンのベースラインを構築することで、エージェントレスかつ設定変更不要で脅威を特定します。

また、AWS Private CAにおいても、証明書発行に関する詳細なログがCloudTrail経由で取得可能となりました。これにより、発行失敗の理由や証明書の内容、要求者の詳細をリアルタイムで追跡できるようになり、コンプライアンス監査やセキュリティ運用が大幅に効率化されます。これらのアップデートは、クラウド環境におけるデータ保護とガバナンスの強化を強力に支援するものです。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### Amazon GuardDuty RDS Protection now detects data exfiltration and destruction in Aurora and RDS databases

Amazon GuardDutyのRDS Protectionが拡張され、Aurora PostgreSQLおよびRDS for PostgreSQLを対象に、データ流出や破壊を目的とした攻撃の検知が可能になりました。機械学習ベースの異常検知により、エージェントや設定変更なしでデータベースのクエリパターンを監視し、従来のツールでは見逃されていた脅威を特定します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon GuardDuty, 機械学習 (ML) |
| 特徴・性能 | エージェントレス、設定変更不要、行動ベースライン分析 |
| 対応環境 | Amazon Aurora PostgreSQL, Amazon RDS for PostgreSQL |
| 関連サービス | Amazon CloudWatch, AWS CloudTrail |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/guardduty-rds-data-exfiltration/

---

##### AWS Private CA now provides detailed certificate issuance logs

AWS Private CAは、証明書発行の詳細なログをCloudTrail経由で提供するようになりました。発行成功時だけでなく失敗時も含め、証明書の内容や要求者のID、署名ステータスが記録されるため、監査やインベントリ管理、アルゴリズム移行の追跡が容易になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Private CA, AWS CloudTrail |
| 特徴・性能 | 発行失敗時の理由記録、X.509フィールドの完全キャプチャ |
| 対応環境 | AWS Private CA提供全リージョン |
| 関連サービス | Amazon EventBridge, Amazon Athena |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/aws-private-ca-certificate-issuance-logs/

---

##### TwelveLabs Pegasus 1.5 model now available on Amazon Bedrock

動画から構造化されたタイムコード付きメタデータを生成する「TwelveLabs Pegasus 1.5」がAmazon Bedrockで利用可能になりました。動画の内容を一度のパスで解析し、特定のシーンやスピーカーの変更、ブランドの出現などを抽出できるため、大規模な動画ライブラリの検索性が大幅に向上します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | TwelveLabs Pegasus 1.5, 動画解析AI |
| 特徴・性能 | タイムコード付きメタデータ生成、事前インデックス不要 |
| 対応環境 | Amazon Bedrock (USおよびグローバルリージョン) |
| 関連サービス | Amazon Bedrock |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/twelve-labs-pegasus-1-5-aws/

---

##### Amazon EC2 C8gb instances now generally available in additional regions

AWS Graviton4プロセッサを搭載したAmazon EC2 C8gbインスタンスが、新たに複数のリージョンで利用可能になりました。Graviton3と比較して最大30%の性能向上を実現し、高いEBS帯域幅とネットワーク性能により、高パフォーマンスなファイルシステムやクラスタワークロードに最適です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Graviton4, Amazon EC2 |
| 特徴・性能 | 最大300 Gbps EBS帯域, 1600K IOPS |
| 対応環境 | US, EU, Africaの主要リージョン |
| 関連サービス | Elastic Fabric Adapter (EFA) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ec2-c8gb/

---

##### AWS Batch now supports Amazon EKS access entry authentication

AWS BatchがAmazon EKSのアクセスエントリ認証をサポートしました。これにより、APIベースでIAMプリンシパルにKubernetesクラスタへのアクセス権を付与できるようになり、従来のConfigMap管理よりもシンプルで効率的な認証ライフサイクル管理が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Batch, Amazon EKS, IAM |
| 特徴・性能 | API駆動の認証管理、aws-auth ConfigMapの代替 |
| 対応環境 | AWS Batch対応全リージョン |
| 関連サービス | Amazon EKS |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/aws-batch-access-entries/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| GuardDuty RDS Protectionのデータアクティビティ監視を有効化する | DB管理者/セキュリティ担当 | 🔴 高 |
| Private CAのログを確認し、監査プロセスを自動化する | セキュリティ担当 | 🟡 中 |
| Graviton4搭載C8gbインスタンスへの移行検証を開始する | インフラエンジニア | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| TwelveLabs Pegasus 1.5 model now available on Amazon Bedrock | AI/LLM | AWS | https://aws.amazon.com/about-aws/whats-new/2026/10/twelve-labs-pegasus-1-5-aws/ |
| Amazon GuardDuty RDS Protection now detects data exfiltration and destruction | セキュリティ | AWS | https://aws.amazon.com/about-aws/whats-new/2026/10/guardduty-rds-data-exfiltration/ |
| Amazon EC2 C8gb instances now generally available | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ec2-c8gb/ |
| AWS Batch now supports Amazon EKS access entry authentication | 開発ツール | AWS | https://aws.amazon.com/about-aws/whats-new/2026/10/aws-batch-access-entries/ |
| AWS Private CA now provides detailed certificate issuance logs | セキュリティ | AWS | https://aws.amazon.com/about-aws/whats-new/2026/10/aws-private-ca-certificate-issuance-logs/ |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Amazon GuardDutyがRDSのデータ流出検知に対応し、セキュリティ監視が大幅強化されました。

📌 **ピックアップ**
• GuardDuty RDS Protectionがデータ破壊・流出攻撃を検知可能に
• AWS Private CAが詳細な証明書発行ログをCloudTrailで提供開始
• TwelveLabs Pegasus 1.5がBedrockで利用可能に
• EC2 C8gbインスタンスが提供リージョンを拡大

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-10-12*
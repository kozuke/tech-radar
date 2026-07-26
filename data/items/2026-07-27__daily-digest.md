# Tech Radar Daily Digest - 2026-07-27

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、.NET開発者向けに「AWS Lambda Durable Execution SDK」の一般提供を開始しました。これにより、C#開発者はカスタムの進捗管理や外部オーケストレーションサービスを構築することなく、決済処理パイプラインやAIエージェントのオーケストレーション、承認ワークフローといった長期間実行される複雑なワークフローをLambda上で直接実装可能になります。

このSDKは、Lambdaのイベント駆動モデルを拡張し、最大1年間の実行中断や自動的なチェックポイント保存をサポートします。ローカルエミュレータも提供されており、デプロイ前に開発環境でデバッグが可能なため、サーバーレスアプリケーションの堅牢性と開発効率が大幅に向上することが期待されます。

---

## 📰 今日のニュース

### クラウド

#### AWS

##### AWS Lambda durable execution SDK for .NET is now generally available

AWS Lambda Durable Execution SDK for .NETが一般提供され、C#開発者がLambda上で長期間実行されるワークフローを容易に構築できるようになりました。このSDKは、外部サービスへの依存を減らし、複雑なマルチステップ処理をLambda内で完結させることを可能にします。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| 進捗管理 | ワークフローの各ステップの進捗を自動的にチェックポイントとして保存。 |
| 外部イベント待機 | 外部イベントを待機するために最大1年間の実行中断が可能。 |
| ローカルエミュレータ | デプロイ前にローカル環境でワークフローを構築・デバッグできる機能。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Lambda, .NET (C#) |
| 対応環境 | .NET toolchain (NuGet経由) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/lambdadf-dotnet/

---

##### Amazon CloudWatch Logs now supports Application Load Balancer logs

Amazon CloudWatch LogsがApplication Load Balancer (ALB) のログを「Vended Logs」として直接サポートしました。これにより、ALBのアクセスログや接続ログ、ヘルスチェックログをCloudWatch上で直接分析可能になり、ネットワークトラブルの特定やトラフィックパターンの監視が簡素化されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon CloudWatch Logs, ALB |
| 特徴・性能 | Insightsクエリによる分析、Live Tailによるリアルタイム監視 |
| 関連サービス | Amazon Data Firehose, Amazon S3 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-logs/

---

##### Amazon EC2 I8ge instances are now generally available in additional AWS regions

Graviton4プロセッサを搭載したストレージ最適化インスタンス「I8ge」が、欧州（ロンドン）およびカナダ（中部）リージョンで利用可能になりました。前世代のIm4gnと比較して、コンピューティング性能が最大60%、ストレージI/O性能が最大55%向上しており、大規模データセットを扱うワークロードに適しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Graviton4, 第3世代AWS Nitro SSD |
| 特徴・性能 | 最大120TBのNVMeストレージ、180 Gbpsのネットワーク帯域 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-i8ge-additional-regions/

---

##### Announcing region expansion of G7e instances on SageMaker AI inference

Amazon SageMaker AI推論において、G7eインスタンスがアジアパシフィック（ソウル、東京）および欧州（ロンドン）リージョンへ拡大されました。NVIDIA Blackwell GPUを搭載し、前世代のG6eと比較して最大2.3倍の推論性能を実現しており、大規模言語モデル（LLM）の推論や生成AIワークロードの高速化に貢献します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | NVIDIA RTX PRO 6000 Blackwell GPU, 5th Gen Intel Xeon |
| 特徴・性能 | 最大768GBのGPUメモリ、最大1,600 GbpsのEFA帯域 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/g7e-sagemaker-ai/

---

##### Announcing region expansion of G6 instances on SageMaker AI Inference

Amazon SageMaker AI推論におけるG6インスタンスが、AWS GovCloud (US-East) リージョンで利用可能になりました。NVIDIA L4 GPUを搭載したこのインスタンスは、高い価格性能比を提供し、政府機関などがコンプライアンス要件を満たしながら生成AI推論を実行することを支援します。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | NVIDIA L4 Tensor Core GPU, 3rd Gen AMD EPYC |
| 特徴・性能 | G4dn比で最大2倍のディープラーニング推論性能 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/g6-sagemaker-ai-inference/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| .NETプロジェクトでのワークフロー実装検討 | .NET開発者 | 🟡 中 |
| ALBログのCloudWatch統合設定の確認 | インフラエンジニア | 🟡 中 |
| SageMaker推論リージョンの最適化検討 | AI/MLエンジニア | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Lambda durable execution SDK for .NET is now generally available | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/lambdadf-dotnet/ |
| Amazon CloudWatch Logs now supports Application Load Balancer logs | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-logs/ |
| Amazon EC2 I8ge instances are now generally available in additional AWS regions | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/aws-i8ge-additional-regions/ |
| Announcing region expansion of G7e instances on SageMaker AI inference | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/g7e-sagemaker-ai/ |
| Announcing region expansion of G6 instances on SageMaker AI Inference | AWS | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/g6-sagemaker-ai-inference/ |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

.NET向け「AWS Lambda Durable Execution SDK」が一般提供開始、長期間のワークフロー構築が容易に。

📌 **ピックアップ**
• ALBログがCloudWatch Logsで直接分析可能に
• Graviton4搭載「I8ge」インスタンスが欧州・カナダで利用可能に
• SageMaker推論用G7e/G6インスタンスが対象リージョンを拡大

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-27*
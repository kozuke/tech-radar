# Tech Radar Daily Digest - 2026-10-13

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、サーバーレスコンピューティングの新たな形態として「AWS Lambda Web Functions」を発表しました。これは、従来のイベント駆動型関数とは異なり、ExpressやHonoといった一般的なWebフレームワークをそのまま利用し、HTTPリクエストを直接処理できる仕組みです。単一の実行環境で複数のリクエストを並列処理できるため、コールドスタートの影響を大幅に低減できるほか、AI推論エンドポイントやSSRアプリケーションの構築に最適化されています。

また、この新機能と合わせて、Amazon CloudFrontがLambda Web Functionsをオリジンとして直接サポートすることも発表されました。これにより、エッジでのTLS終端やキャッシュ、AWS WAFによるセキュリティ保護を、アプリケーションコードの変更なしに適用可能となります。サーバーレスアーキテクチャの柔軟性と、Webサーバーとしての利便性を両立させる重要なアップデートと言えます。

---

## 📰 今日のニュース

### AI/LLM

#### Amazon Bedrock

##### Amazon Bedrock AgentCoreの短期メモリに消費ベースの料金体系を導入

Amazon Bedrock AgentCoreの短期メモリ（STM）において、イベントごとの定額制から、データの取り込み・取得・保存量に応じた消費ベースの料金体系へと変更されました。これにより、頻繁に小さなイベントを書き込むエージェント開発者は、利用量に応じたコスト最適化が可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon Bedrock AgentCore |
| 料金モデル | 取り込み($1.00/GB)、取得($0.20/GB)、保存($0.10/GB-月) |
| 管理機能 | TTL（Time To Live）設定によるストレージコスト管理 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-memory-consumption-based-pricing

---

#### Devin

##### Devinがセッションをまたぐ「メモリ」と「ドリーミング」機能を搭載

AIコーディングエージェントのDevinが、ユーザーの作業内容を学習・記憶し、セッションをまたいで活用する機能を実装しました。夜間に過去のセッションを振り返る「ドリーミング」プロセスを経て記憶を洗練させるほか、UIのカスタマイズ性や通知設定の細分化など、開発体験を向上させる多数の機能強化が行われました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| メモリ機能 | ユーザーの作業内容を学習し、セッション間で知識を保持する。 |
| ドリーミング | 夜間に過去のセッションをレビューし、記憶を整理・洗練させる。 |
| 設定同期 | ユーザー設定がサーバー保存され、デバイスやアプリ間で同期される。 |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-10-09-memory-and-dreaming

---

### クラウド

#### AWS

##### Amazon CloudFrontがAWS Lambda Web Functionsをオリジンとしてサポート

Amazon CloudFrontがLambda Web Functionsをオリジンとして直接サポートを開始しました。これにより、エッジでのTLS終端やキャッシュ、AWS WAFによる保護を、アプリケーションコードを変更することなく適用できるようになり、Webアプリケーションのパフォーマンスとセキュリティが向上します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-lambda-web-functions-origin/

##### Amazon EC2 G7インスタンスが欧州リージョン（フランクフルト・ストックホルム）で利用可能に

NVIDIA RTX PRO 4500 Blackwell Server Edition GPUを搭載したEC2 G7インスタンスが、欧州の2リージョンで利用可能になりました。G6インスタンスと比較してAI推論性能が最大4.6倍、グラフィックス性能が最大2.1倍に向上しており、AIモデルのデプロイやリアルタイムレンダリングに適しています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-g7-european-regions/

##### Amazon Connectでステップバイステップガイドの自動入力機能が強化

Amazon Connectにおいて、顧客との会話から抽出した情報をステップバイステップガイドのフォームに自動入力する機能が追加されました。予約番号や通話要約などを自動反映させることで、エージェントの作業時間を短縮し、データ入力ミスを削減します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/10/connect-customer-prefills-guides-acw

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Lambda Web Functionsの検証と移行検討 | Webアプリ開発者 | 🔴 高 |
| Bedrock AgentCoreのコスト試算とTTL設定 | AIエンジニア | 🟡 中 |
| Devinのメモリ設定の確認とカスタマイズ | Devinユーザー | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon CloudFront now supports AWS Lambda Web Functions as an origin | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-lambda-web-functions-origin/ |
| Amazon EC2 G7 instances now available in Europe | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-g7-european-regions/ |
| Amazon Connect Customer now prefills step-by-step guides | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/connect-customer-prefills-guides-acw |
| AWS Lambda announces Lambda Web Functions | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-web-functions/ |
| Announcing consumption-based pricing for Bedrock AgentCore | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-memory-consumption-based-pricing |
| Memory and dreaming | AI/LLM | devin_release_notes | https://docs.devin.ai/release-notes/overview#2026-10-09-memory-and-dreaming |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWSがHTTPリクエストを直接処理可能な「Lambda Web Functions」を発表、CloudFrontとの統合でWebアプリ開発がより効率的に。

📌 **ピックアップ**
• AWS Lambda Web Functions: Express/Hono対応のサーバーレスWeb実行環境
• Amazon Bedrock: AgentCoreの短期メモリ料金が消費ベースに変更
• Devin: セッションをまたぐ記憶機能「メモリ」と「ドリーミング」を実装

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-10-13*
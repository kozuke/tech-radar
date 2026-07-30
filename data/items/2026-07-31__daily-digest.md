# Tech Radar Daily Digest - 2026-07-31

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

AWSは、ネットワークの可視性と制御を大幅に強化する2つの重要なアップデートを発表しました。まず「AWS Direct Connect」におけるBGPルート可視化機能の提供開始により、オンプレミスとAWS間で交換されるルート情報（ASパスやコミュニティ値など）をコンソール上で直接確認可能になりました。これにより、ハイブリッドネットワークにおける複雑なルーティングトラブルの切り分けが大幅に効率化されます。

さらに「AWS Transit Gateway」では、待望のポリシーベースルーティング（PBR）が一般提供されました。従来は宛先IPのみに基づいていたルーティングが、送信元IP、ポート、プロトコルなどの属性に基づいて制御可能となり、特定のトラフィックをファイアウォールへ転送したり、環境ごとにルーティングドメインを分離したりといった高度なトラフィック制御が、追加のインフラなしで実現可能となりました。

---

## 📰 今日のニュース

### AI/LLM

#### OpenAI / Bedrock

##### Amazon BedrockにおけるOpenAI GPT-5.6モデルの値下げ
Amazon Bedrockで提供されているOpenAIの「GPT-5.6 Luna」および「GPT-5.6 Terra」モデルの推論料金が大幅に引き下げられました。Lunaは最大80%、Terraは20%の値下げとなり、開発者はより低コストで高度な推論能力をアプリケーションに組み込むことが可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | OpenAI GPT-5.6 (Luna, Terra) |
| 改善点 | 推論コストの最大80%削減 |
| 対応環境 | US East/Westリージョン |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-terra-luna-pricing-bedrock/

---

#### Devin (Cognition)

##### Devinの機能アップデートとCLIの強化
AIエンジニアリングツール「Devin」のWebアプリおよびCLIが大幅にアップデートされました。Web版では差分の単語レベルハイライトやSlack連携の強化が行われ、CLI版では「スマート権限モード」の導入や、プラグインによるMCPサーバー・カスタムサブエージェントの拡張機能が追加されました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| スマート権限モード | ルーチン作業を自動承認し、破壊的操作のみをプロンプトする安全な実行モード。 |
| プラグイン拡張 | MCPサーバーやカスタムサブエージェントをルールとしてセッションに組み込み可能。 |
| 差分表示 | 変更箇所を単語単位でハイライトし、コードレビューの効率を向上。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Devin AI, MCP (Model Context Protocol) |
| 特徴・性能 | 自動承認による開発効率化とセキュリティのバランス |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-07-29-word-level-diff-highlights

---

### クラウド

#### AWS

##### Amazon Redshift RGインスタンスが「trailing track」に対応
Amazon RedshiftのGravitonベースであるRGインスタンス（rg.large, rg.12xlarge）が、安定性を重視する「trailing track」で利用可能になりました。これにより、本番環境でより安定したバージョンを維持しつつ、高いコストパフォーマンスを享受できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Graviton, Amazon Redshift |
| 特徴・性能 | RA3比で最大2.4倍のクエリ性能、30%のコスト削減 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-rg-large-12xlarge-trailing-track

##### IAM Policy Simulatorのコンソール統合と機能強化
IAM Policy Simulatorが独立したサイトからIAMコンソール内へ統合されました。SCP（サービスコントロールポリシー）のシミュレーションや、条件キーの検証、特定のポリシーを除外した「What-if」分析が可能になり、セキュリティ検証の利便性が向上しました。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/iam-policy-simulator-iam-console/

---

### Workspace

#### Google Workspace

##### Google FormsでGeminiを活用したクイズ作成が可能に
Google Formsの「Help me create」機能で、Geminiを用いたクイズの自動生成が可能になりました。プロンプトやGoogleドライブ内のドキュメントを指定することで、正解付きのクイズを即座に作成でき、教育や研修の準備時間を大幅に短縮します。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/use-gemini-in-google-forms-to-quickly-create-a-new-quiz.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Transit GatewayのPBR設定を確認し、複雑なルーティングを簡素化する | ネットワーク管理者 | 🔴 高 |
| BedrockのGPT-5.6モデルを利用している場合、コスト削減設定を確認する | AIエンジニア | 🟡 中 |
| Devinのスマート権限モードを試し、開発フローの自動化を検討する | 開発者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Direct Connect BGP visibility | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-direct-connect-bgp-visibility/) |
| Redshift RG instances trailing track | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-redshift-rg-large-12xlarge-trailing-track) |
| IAM Policy Simulator update | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/iam-policy-simulator-iam-console/) |
| Bedrock OpenAI pricing | AI/LLM | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-terra-luna-pricing-bedrock/) |
| Transit Gateway PBR | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-transit-gateway-policy-based-routing/) |
| Devin Release Notes | AI/LLM | Devin | [link](https://docs.devin.ai/release-notes/overview#2026-07-29-word-level-diff-highlights) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
AWSネットワーク機能が大幅強化：Direct ConnectのBGP可視化とTransit Gatewayのポリシーベースルーティングが提供開始。

📌 **ピックアップ**
• Amazon Bedrock：OpenAI GPT-5.6モデルが最大80%値下げ。
• Devin：CLIのスマート権限モードとプラグイン拡張機能が追加。
• Google Forms：Geminiによるクイズ自動生成機能がリリース。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-31*
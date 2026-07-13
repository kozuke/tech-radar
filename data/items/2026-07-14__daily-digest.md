# Tech Radar Daily Digest - 2026-07-14

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

OpenAIの最新モデル「GPT-5.6」シリーズ（Sol, Terra, Luna）がAmazon Bedrockで一般提供開始されました。推論能力に特化したフラッグシップモデル「Sol」から、コスト効率を重視した「Luna」まで、用途に応じた3つのティアが提供されます。特に注目すべきは、エージェントワークフローにおける「プロンプトキャッシング」のサポートで、繰り返し発生するコンテキストのコストを最大90%削減可能です。これにより、自律的なコーディングエージェントや大規模なデータ分析など、高負荷なAIアプリケーションの構築がより実用的かつ経済的になります。

また、Amazon SageMaker JumpStartにおいても、Googleのマルチモーダルモデル「Gemma-4-E2B-it」や、OpenAIのPII（個人情報）検出・マスキングモデル「privacy-filter」が利用可能となりました。これにより、AWS環境上での高度なAIアプリケーション開発から、セキュアなデータ処理パイプラインの構築まで、一貫したインフラストラクチャでの運用が可能となり、企業のAI導入がさらに加速することが期待されます。

---

## 📰 今日のニュース

### AI/LLM

#### OpenAI / AWS

##### OpenAI GPT-5.6 Sol, Terra, and Luna now generally available on Amazon Bedrock

OpenAIの最新モデルであるGPT-5.6シリーズがAmazon Bedrockで利用可能になりました。推論、性能、コストのバランスに応じて3つのモデルが提供され、特にエージェント型ワークフローでのコスト最適化が強化されています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| GPT-5.6 Sol | 推論能力を最大化したフラッグシップモデル。 |
| GPT-5.6 Terra | GPT-5.5相当の性能を半分のコストで実現。 |
| GPT-5.6 Luna | 高速かつ低価格な推論に特化したモデル。 |
| プロンプトキャッシング | 繰り返し使用するコンテキストのコストを90%削減。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | GPT-5.6 (Sol, Terra, Luna) |
| 特徴・性能 | エージェントコーディング、長期間の分析に最適化 |
| 対応環境 | Amazon Bedrock (US Eastリージョン) |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-sol-terra/

---

#### SageMaker JumpStart

##### Gemma-4-E2B-it for is now available in Amazon SageMaker JumpStart

Google DeepMindのマルチモーダルモデル「Gemma-4-E2B-it」がSageMaker JumpStartに追加されました。テキスト、画像、音声を統合的に処理し、推論モードによるステップバイステップの思考が可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Gemma-4-E2B-it (Google DeepMind) |
| 特徴・性能 | マルチモーダル入力、ネイティブ関数呼び出し対応 |
| 関連サービス | Amazon SageMaker JumpStart |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/gemma-4-e2b-on-sagemaker-jumpstart/

---

##### OpenAI privacy-filter for PII detection and masking is now available in Amazon SageMaker JumpStart

OpenAIのPII検出・マスキングモデル「privacy-filter」がSageMaker JumpStartで利用可能になりました。高スループットなデータサニタイズ処理をオンプレミスやAWS環境で実行可能です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | OpenAI privacy-filter |
| 特徴・性能 | 高速なトークン分類、PII spanの自動検出 |
| 関連サービス | Amazon SageMaker JumpStart |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/privacy-filter-on-sagemaker-jumpstart/

---

### クラウド

#### AWS

##### Amazon DocumentDB (with MongoDB compatibility) now available as a skill in the Agent Toolkit for AWS

Amazon DocumentDBが「Agent Toolkit for AWS」のスキルとして統合されました。AIエージェントがクラスタのプロビジョニングや移行、パフォーマンスチューニングを自動化できるようになります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Agent Toolkit for AWS, DocumentDB |
| 特徴・性能 | 7つのワークフロー（プロビジョニング、移行、チューニング等）を自動化 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-documentdb-agent-skill

---

##### Amazon Managed Service for Prometheus is now available in Asia Pacific (New Zealand) Region

Amazon Managed Service for Prometheusがニュージーランドリージョンで利用可能になりました。大規模な運用メトリクスの監視とアラート設定が、より地理的に近い環境で実行可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-prometheus-new-zealand/

---

### Workspace

#### Google Workspace

##### Google Credential Provider for Windows (GCPW) now supports FIDO2-compliant physical security keys

GCPWがWindowsログイン時の第二認証要素としてFIDO2準拠の物理セキュリティキーをサポートしました。これにより、組織はWindows端末のログインにおいてより強固な多要素認証を強制できるようになります。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/google-credential-provider-for-windows-now-supports-FIDO2-compliant-physical-security-keys-as-a-second-factor-for-authentication.html

---

### 開発ツール

#### OpenAI Codex CLI

##### OpenAI Codex CLI リリース情報 (v0.144.2 - v0.145.0-alpha.7)

OpenAI Codex CLIの複数のアルファ版およびマイナーアップデートがリリースされました。主にバグ修正や内部的なプロンプトポリシーの調整が行われています。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| GPT-5.6のプロンプトキャッシングを検証しコスト削減を検討 | AI開発者 | 🔴 高 |
| DocumentDBスキルをAgent Toolkitに導入し運用自動化を試す | インフラエンジニア | 🟡 中 |
| GCPWのFIDO2対応による認証ポリシーの更新 | セキュリティ管理者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| OpenAI GPT-5.6... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-sol-terra/ |
| Amazon Managed Service for Prometheus... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-prometheus-new-zealand/ |
| Amazon DocumentDB... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-documentdb-agent-skill |
| Gemma-4-E2B-it... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/gemma-4-e2b-on-sagemaker-jumpstart/ |
| OpenAI privacy-filter... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/privacy-filter-on-sagemaker-jumpstart/ |
| Codex CLI Releases | 開発ツール | openai_codex | https://github.com/openai/codex/releases |
| GCPW FIDO2 Support | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/07/google-credential-provider-for-windows-now-supports-FIDO2-compliant-physical-security-keys-as-a-second-factor-for-authentication.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

OpenAIの最新モデル「GPT-5.6」シリーズがAmazon Bedrockで提供開始。プロンプトキャッシングでコストを大幅削減可能に。

📌 **ピックアップ**
• GPT-5.6 (Sol/Terra/Luna) がBedrockで利用可能に
• SageMaker JumpStartにGemma-4-E2BとOpenAI privacy-filterが追加
• Amazon DocumentDBがAgent Toolkitのスキルとして利用可能に
• GCPWがWindowsログイン時のFIDO2セキュリティキー認証をサポート

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-14*
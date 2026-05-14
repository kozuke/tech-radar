# Tech Radar Daily Digest - 2026-05-15

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**Amazon Bedrockが「Advanced Prompt Optimization」を発表**
Amazon Bedrockに、プロンプトの最適化とモデル移行を支援する強力な新ツールが導入されました。これまで数日から数週間を要していたプロンプトの調整や評価プロセスを自動化し、最大5つのモデル間でパフォーマンスを同時比較できるのが特徴です。評価指標やコスト、レイテンシを考慮したフィードバックループにより、モデルの移行時や既存モデルの性能向上において、エンジニアの作業負荷を劇的に軽減します。

**Google Genkitが「Middleware」機能を導入**
AIエージェント開発フレームワーク「Genkit」に、生成プロセスを拡張・保護するミドルウェア機能が追加されました。リトライ処理、フォールバック（モデル切り替え）、ツール実行の承認フローなどをパイプラインに組み込むことが可能になり、プロダクション環境で求められる信頼性と安全性を容易に実装できるようになりました。TypeScript、Go、Dartに対応しており、エージェント開発の堅牢性が大きく向上します。

---

## 📰 今日のニュース

### AI/LLM

#### AI Agent / 開発ツール

##### Devin: 開発体験と管理機能のアップデート
Devinの最新アップデートでは、スナップショットの削除機能や、MCP環境変数でのマルチライン入力対応など、開発効率を向上させる機能が多数追加されました。また、設定画面の刷新やモバイルUIの改善、APIの機能強化が行われ、エンタープライズ環境での運用管理がよりスムーズになりました。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Devin AI Agent, MCP (Model Context Protocol) |
| 特徴・性能 | マルチライン環境変数対応、設定画面のハブ型UI刷新 |
| 対応環境 | Webブラウザ, モバイルアプリ |
| 関連サービス | V3 API, エンタープライズ管理パネル |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview

---

##### Claude Code v2.1.142 リリース
Claude Codeの最新版では、バックグラウンドセッションの設定を細かく制御するためのフラグ群が追加されました。また、FastモードのデフォルトモデルがOpus 4.7に更新され、各種バグ修正やターミナル表示の改善が行われています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, Opus 4.7 |
| 特徴・性能 | 設定フラグの拡充, Fastモードのモデル更新 |
| 対応環境 | CLI, macOS/Windows/Linux |
| 関連サービス | MCP, GitHub App |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.142

---

### クラウド

#### AWS

##### Amazon CloudFront: mTLS Passthrough Modeのサポート
CloudFrontが相互TLS（mTLS）認証におけるパススルーモードをサポートしました。これにより、エッジ側で証明書検証を行わず、オリジンサーバーへ直接クライアント証明書を転送できるため、既存のmTLSインフラをそのまま活用可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Amazon CloudFront, mTLS |
| 特徴・性能 | 証明書検証のオリジン委譲, 追加コストなし |
| 対応環境 | AWS CloudFront |
| 関連サービス | Amazon EBS, Nitro System |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-cloudfront-mtls-passthrough/

---

##### Amazon EC2 M3 Ultra Mac インスタンスの一般提供開始
Appleシリコン「M3 Ultra」を搭載したMacインスタンスが一般提供されました。M4 Maxと比較してメモリやコア数が大幅に強化されており、Xcodeシミュレーターの並列実行やオンデバイスMLワークロードの高速化に最適です。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Apple M3 Ultra, AWS Nitro System |
| 特徴・性能 | 28コアCPU, 60コアGPU, 256GBメモリ |
| 対応環境 | AWS US East/West |
| 関連サービス | Amazon EBS, Xcode |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ec2-m3-ultra-mac-instances-generally-available/

---

### Workspace

#### Google Workspace

##### SAMLアプリ向けデフォルトContext-Aware Access (CAA)
組織内の全SAMLアプリケーションに対して、一括でコンテキスト認識アクセス（CAA）ポリシーを適用可能になりました。個別の設定なしでベースラインのセキュリティを確保できるため、管理者の運用負荷が大幅に軽減されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | SAML, Context-Aware Access |
| 特徴・性能 | 全SAMLアプリへの一括ポリシー適用, 監視/アクティブモード |
| 対応環境 | Google Workspace Admin Console |
| 関連サービス | Cloud Identity |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/05/default-CAA-for-SAML.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Bedrockのプロンプト最適化ツールを試す | AIエンジニア | 🔴 高 |
| Genkitミドルウェアでエージェントの信頼性を向上させる | バックエンド開発者 | 🔴 高 |
| CloudFront mTLS設定の移行検討 | インフラエンジニア | 🟡 中 |
| SAMLアプリのCAAポリシー設定を確認する | 管理者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon CloudFront Passthrough Mode | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-cloudfront-mtls-passthrough/) |
| Bedrock Advanced Prompt Optimization | AI/LLM | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-bedrock-advanced-prompt-optimization-migration-tool/) |
| EC2 M3 Ultra Mac GA | クラウド | AWS | [link](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ec2-m3-ultra-mac-instances-generally-available/) |
| Claude Code v2.1.142 | 開発ツール | GitHub | [link](https://github.com/anthropics/claude-code/releases/tag/v2.1.142) |
| Genkit Middleware | AI/LLM | Google | [link](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) |
| Devin Release Notes | AI/LLM | Devin | [link](https://docs.devin.ai/release-notes/overview) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
Amazon Bedrockのプロンプト最適化ツールと、Google Genkitのミドルウェア機能がリリースされました。

📌 **ピックアップ**
• Bedrock: プロンプト最適化とモデル比較が自動化
• Genkit: ミドルウェアでエージェントの信頼性と安全性を強化
• AWS: M3 Ultra Macインスタンスが一般提供開始
• CloudFront: mTLSのパススルーモードをサポート

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-15*
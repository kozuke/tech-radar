# Tech Radar Daily Digest - 2026-05-06

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**GoogleがAIエージェント開発の標準化を加速する「Agents CLI」を発表**
AIエージェントが実験的なスクリプトから本番環境へと移行する中、開発インフラの断片化が大きな課題となっています。Googleは、GeminiやClaude CodeなどのAIコーディングアシスタントとGoogle Cloudのスタックを直接接続する「Agents CLI」を導入しました。このツールにより、開発者は単一のコマンドでエージェントの構築、シミュレーション、評価、デプロイまでをシームレスに行うことが可能になります。特に、エージェント開発における「コンテキストの過負荷」や「ローカルとクラウドの乖離」といった問題を解決し、開発期間を劇的に短縮することを目指しています。

**AWSが次世代GPUインスタンス「P6-B300」を投入**
AWSは、NVIDIA Blackwell Ultra GPUを8基搭載した「Amazon EC2 P6-B300」インスタンスを北米リージョンで提供開始しました。前世代のP6-B200と比較して、ネットワーク帯域幅が2倍、GPUメモリが1.5倍に強化されており、数兆パラメータ規模の巨大な基盤モデル（FM）やLLMの学習・推論に最適化されています。これにより、AIワークロードにおける学習時間の短縮と、より高度な推論処理の実現が期待されます。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code
##### Claude Code v2.1.132 / v2.1.131 / v2.1.129
Claude Codeのアップデートが連続してリリースされました。最新版では、BashツールでのセッションID管理の強化や、全画面レンダラーの制御オプション追加、各種キー操作やエディタ連携のバグ修正が行われました。特に、プラグインのURL指定機能や、Homebrew/WinGet経由の自動アップデート機能が追加され、開発体験が大幅に向上しています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, CLI, Bash |
| 特徴・性能 | セッション管理の強化、プラグイン機能の拡張 |
| 対応環境 | macOS, Windows, Linux |
| 関連サービス | Anthropic API, VS Code, JetBrains |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases

---

#### OpenAI
##### OpenAI Python SDK v2.35.1 / v2.35.0
OpenAIのPython SDKが更新され、Image 2モデルのサポート強化やAPIパラメータのドキュメント修正が行われました。また、レガシーなPython CLIが削除されるなど、ライブラリの整理が進んでいます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | OpenAI Python SDK |
| 特徴・性能 | Image 2モデル対応、レガシーコードの削除 |
| 対応環境 | Python |
| 関連サービス | OpenAI API |

> 🔗 **参考リンク**
> https://github.com/openai/openai-python/releases

---

#### Google AI
##### LiteRTによるオンデバイスAIの最適化
Googleは、モバイルやIoTデバイスで高性能なAIを実現する「LiteRT」の活用事例を紹介しました。NPU（Neural Processing Unit）を活用することで、Google Meetの背景処理やEpic Gamesのリアルタイムアニメーションなど、消費電力とパフォーマンスを両立させた高度なAI体験が可能になっています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | LiteRT, NPU, Android |
| 特徴・性能 | 低レイテンシ、省電力、NPUアクセラレーション |
| 対応環境 | Android, iOS, IoT |
| 関連サービス | Google Meet, Unreal Engine |

> 🔗 **参考リンク**
> https://developers.googleblog.com/building-real-world-on-device-ai-with-litert-and-npu/

---

### クラウド

#### AWS
##### AWS Site-to-Site VPNの帯域幅変更機能
AWS Site-to-Site VPNにおいて、既存の接続を削除することなくトンネル帯域幅（Standard/Large）を変更可能になりました。IPアドレスや設定を維持したままアップグレードできるため、オンプレミス側の設定変更が不要となり、運用負荷が大幅に軽減されます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | AWS Site-to-Site VPN |
| 特徴・性能 | 無停止での帯域幅変更、設定維持 |
| 対応環境 | AWS全リージョン（一部除く） |
| 関連サービス | AWS VPC |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/05/aws-site-to-site-vpn-modify-bandwidth/

---

### Workspace

#### Google Workspace
##### Workspace Studioの機能強化とChromeでのスキル機能
Google Workspace Studioで、Meetの会議出力に基づくワークフロー起動や、カレンダーの「時間ブロック」機能が追加されました。また、ブラウザ版Geminiでプロンプトを「スキル」として保存し、ワンクリックで呼び出せる機能が提供開始されました。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Google Workspace Studio, Gemini in Chrome |
| 特徴・性能 | ワークフロー自動化、プロンプトの再利用 |
| 対応環境 | Webブラウザ |
| 関連サービス | Google Meet, Google Calendar |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/05/improvements-to-meet-starter-step-and-Calendar-time-blocking-capabilities-in-Google-Workspace-Studio.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Claude Codeを最新版(v2.1.132)へアップデート | 開発者 | 🟡 中 |
| AWS VPNの帯域幅設定を見直し、必要に応じてアップグレード | インフラエンジニア | 🟢 低 |
| Gemini in Chromeで頻繁に使うプロンプトを「スキル」として保存 | 全ユーザー | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Site-to-Site VPN... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/aws-site-to-site-vpn-modify-bandwidth/ |
| Amazon EC2 P6-B300... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ec2-p6-b300-us-east |
| AWS Marketplace... | クラウド | AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/aws-marketplace-agreements-api/ |
| Claude Code v2.1.132 | AI/LLM | GitHub | https://github.com/anthropics/claude-code/releases/tag/v2.1.132 |
| ... | ... | ... | ... |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
GoogleがAIエージェント開発を効率化する「Agents CLI」を発表、AWSは次世代GPUインスタンス「P6-B300」を投入。

📌 **ピックアップ**
• Claude Codeがアップデート、プラグインや自動更新機能が強化
• Google Workspace Studioで会議自動化やカレンダー連携が進化
• AWS VPNの帯域幅変更が設定維持のまま可能に

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-05-06*
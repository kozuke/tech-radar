# Tech Radar Daily Digest - 2026-06-17

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AWSが生成AI開発を加速する新ツール「AWS Blocks」と「AWS Transform」の機能強化を発表**
AWSは、インフラ構築の複雑さを排除し、TypeScriptでバックエンドを構築できるオープンソースフレームワーク「AWS Blocks」のパブリックプレビューを開始しました。ローカル環境での開発からAWSへのデプロイまでシームレスに行える点が特徴です。また、既存の「AWS Transform」では、生成AIワークロードのモデル移行を自動化する機能が追加され、OpenAIやGoogle GeminiからAmazon Bedrockへの移行を、コード変更を最小限に抑えつつコスト最適化を考慮して実行可能になりました。これにより、開発者はインフラ管理の負担を減らし、AIアプリケーションの構築と運用に集中できる環境が整います。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code / OpenAI

##### Claude Code v2.1.179 リリース
Claude Codeの最新版では、ストリーミング接続の中断時のエラー処理が改善され、部分的なレスポンスが保持されるようになりました。また、WSL2環境でのマウスホイールスクロールの不具合や、大規模ディレクトリツリーでのサンドボックス設定の最適化など、開発体験を向上させる複数のバグ修正が行われています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code CLI |
| 特徴・性能 | 接続安定性の向上、UI/UXのバグ修正 |
| 対応環境 | Linux, WSL2, VS Code |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.179

##### OpenAI Codex CLI (rust-v0.141.0-alphaシリーズ)
OpenAIはCodex CLIのアルファ版（v0.141.0-alpha.1〜4）を連続リリースしました。詳細な変更ログは公開されていませんが、継続的な機能改善と安定化に向けたアップデートが進行中です。

> 🔗 **参考リンク**
> https://github.com/openai/codex/releases/tag/rust-v0.141.0-alpha.4

---

### クラウド

#### AWS

##### AWS Transform for Mainframeのワークフロー刷新
メインフレームのモダナイゼーションにおいて、評価からコード生成までを追跡可能な「Reimagine」ワークフローが導入されました。これにより、z/OS COBOLやPL/Iのワークロードを、ビジネス機能の抽出からクラウドネイティブなコード生成まで一貫して自動化し、監査可能な形で移行できるようになります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/aws-transform-mainframe-traceable-reimagine-workflow/

##### Amazon Redshift RGインスタンスの提供地域拡大
AWS Gravitonプロセッサを搭載したRedshift RGインスタンスが、アフリカ（ケープタウン）、アジアパシフィック（バンコク）、メキシコ（セントラル）の3地域で利用可能になりました。既存のRA3インスタンスと比較して最大4.2倍の価格性能比を実現し、Spectrumスキャン料金の廃止によりデータレイククエリのコスト削減も可能です。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-redshift-rg-instances-3-additional-regions/

---

### Google / Workspace

#### Gemini / Google Workspace

##### Google VoiceでのAIノートテイク機能
Google Voiceにおいて、通話内容を録音・文字起こしし、要約とアクションアイテムを自動生成する「Take notes for me」機能が提供開始されました。通話終了後にGmailで要約が送信され、Voiceアプリ内に詳細が保存されるため、手動でのメモ取りが不要になります。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/AI-note-taking-in-google-voice.html

##### Gemini in Chromeの提供地域拡大
Chromeブラウザ内のGemini機能が、ラテンアメリカ、アフリカ、中東などへ拡大されました。ブラウザのタブ内容に基づいた要約やコンテンツ生成、Gemini Liveによる音声対話などが、データガバナンスを維持した状態で利用可能になります。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/06/expanded-availability-gemini-in-chrome.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| AWS Blocksのプレビューを試してバックエンド構築を効率化する | 開発者 | 🟡 中 |
| AWS Transformで生成AIモデルのBedrock移行計画を策定する | AIエンジニア | 🔴 高 |
| Google VoiceのAIノート機能を有効化し、会議メモを自動化する | 管理者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Transform supports model-to-model migration | AI/LLM | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-transform-model-to-model-assessments) |
| AWS Transform for mainframe workflow | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-transform-mainframe-traceable-reimagine-workflow/) |
| AWS Sign-in policy updates | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-sign-in/) |
| Redshift RG instances expansion | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-redshift-rg-instances-3-additional-regions/) |
| AWS Blocks preview | クラウド | AWS | [URL](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-blocks-preview) |
| Claude Code v2.1.179 | AI/LLM | GitHub | [URL](https://github.com/anthropics/claude-code/releases/tag/v2.1.179) |
| OpenAI Codex CLI alpha releases | AI/LLM | GitHub | [URL](https://github.com/openai/codex/releases/tag/rust-v0.141.0-alpha.4) |
| Sign in with Google security metadata | その他 | Google | [URL](https://developers.googleblog.com/enhance-security-and-trust-new-session-metadata-in-sign-in-with-google/) |
| TPU Developer Hub launch | AI/LLM | Google | [URL](https://developers.googleblog.com/unlocking-the-power-of-the-tpu-stack-introducing-our-new-developer-hub/) |
| Gemini app chat controls | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/06/temporary-chats-and-conversation-deletion-control-for-gemini.html) |
| Gemini in Chrome expansion | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/06/expanded-availability-gemini-in-chrome.html) |
| AI note-taking in Google Voice | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/06/AI-note-taking-in-google-voice.html) |
| Google Chat discoverable spaces | Workspace | Google | [URL](http://workspaceupdates.googleblog.com/2026/06/discoverable-space-setting-chat.html) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AWSがインフラ構築を簡略化する「AWS Blocks」と、生成AIモデルのBedrock移行を自動化する「AWS Transform」の新機能を発表しました。

📌 **ピックアップ**
• Claude Code: 接続安定性やUIのバグを修正したv2.1.179をリリース
• Google Voice: 通話内容を自動で要約・記録するAIノート機能を導入
• Redshift: Graviton搭載RGインスタンスの提供地域を拡大

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-06-17*
# Tech Radar Daily Digest - 2026-07-17

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Googleは「Gemini Enterprise Agent Platform」の強化として、Parallel Web Systemsと提携し、GeminiモデルにリアルタイムのWeb検索結果をグラウンディング（根拠付け）させる機能を統合しました。これにより、企業はLLMの推論能力と最新のWeb情報を組み合わせ、金融や法務などの高度な専門性が求められる領域で、正確かつ検証可能なAIエージェントを構築可能になります。

また、Google Workspaceの「Google Vids」においても大規模なアップデートが実施されました。最新の「Gemini Omni」モデルを搭載することで、ユーザーは自身の分身となるパーソナルアバターの生成や、テキスト指示による動画の高度な編集が可能になりました。これらの機能は、企業における動画コンテンツ制作の効率を劇的に向上させ、専門的なスタジオ環境なしでの高品質なプレゼンテーション作成を後押しします。

---

## 📰 今日のニュース

### AI/LLM

#### Google

##### Expanding Choice in Gemini Enterprise Agent Platform: Introducing Grounding with Parallel Web Search

Gemini Enterprise Agent PlatformがParallel Web Systemsとネイティブ統合され、高品質なリアルタイムWeb検索結果をグラウンディングに利用可能になりました。これにより、AIエージェントは最新の公開情報に基づいた正確な回答と、正確なソース引用を提供できるようになります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Gemini Enterprise Agent Platform, Parallel Web Search API |
| 特徴・性能 | LLM最適化された構造化データ、正確な引用注釈 |
| 関連サービス | Google Cloud Marketplace, Gemini API, Agent Studio |

> 🔗 **参考リンク**
> https://developers.googleblog.com/expanding-choice-in-gemini-enterprise-agent-platform-introducing-grounding-with-parallel-web-search/

---

#### Anthropic

##### v0.117.0

Anthropic SDK for Pythonの最新版がリリースされ、AIの思考プロセスを拡張する「dreaming」機能や、MCP（Model Context Protocol）Tunnelsのサポートが追加されました。また、セキュリティ強化として、トレースバック情報から認証情報を除外する修正も行われています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Anthropic SDK (Python) |
| 特徴・性能 | dreamingサポート, MCP Tunnels対応 |
| セキュリティ | SecretStrによる認証情報の保護 |

> 🔗 **参考リンク**
> https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.0

---

### クラウド

#### AWS

##### Amazon Managed Grafana achieves FedRAMP High authorization in AWS GovCloud (US)

Amazon Managed GrafanaがAWS GovCloud (US) リージョンにおいてFedRAMP Highの認定を取得しました。これにより、連邦政府機関や公共部門のユーザーは、厳格なセキュリティ要件を満たしながら、AWSおよびハイブリッド環境の運用メトリクスを可視化・監視できるようになります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-grafana-fedramp-high/

##### Track cost efficiency trends directly in Billing and Cost Management Dashboards with the new Cost Efficiency widget

AWS Billing and Cost Managementダッシュボードに「Cost Efficiency」ウィジェットが追加されました。コスト効率の推移を可視化し、Cost Optimization Hubと直接連携することで、最適化の推奨事項に対して即座に行動を起こすことが可能になります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/monitor-cost-efficiency-using-dashboards/

---

### Workspace

#### Google Workspace

##### Cast yourself in AI video clips using your personal avatar with Gemini Omni in Vids

Google VidsにGemini Omniが統合され、ユーザー自身のパーソナルアバターを作成・利用できるようになりました。セキュアな検証プロセスを経て、自身の分身を動画内のキャラクターとして配置することで、撮影スタジオなしでの動画制作が可能になります。

##### Generate higher quality AI video clips and edit any video with Gemini Omni in Vids

Gemini Omniの搭載により、Google Vidsでの動画生成品質が向上しました。さらに、テキスト指示だけで動画の色調補正や背景ノイズの除去、スタイルの変更といった高度な編集が可能になり、動画制作のワークフローが簡素化されます。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| パーソナルアバター | 自身の外見をアバター化し、Vids内の動画に配置可能。 |
| テキスト編集 | テキスト指示で色調やスタイル、背景音の編集が可能。 |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/cast-yourself-in-ai-video-clips-using-your-personal-avatar-with-Gemini-Omni-in-Vids.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Google Vidsの新しいアバター・編集機能の試用 | コンテンツ制作者 | 🟡 中 |
| AWS BillingダッシュボードへのCost Efficiencyウィジェット追加 | クラウド管理者 | 🟢 低 |
| Anthropic SDKのv0.117.0へのアップデート | 開発者 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Managed Grafana... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-grafana-fedramp-high/ |
| Track cost efficiency... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/monitor-cost-efficiency-using-dashboards |
| Amazon EC2 now surfaces... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-public-images-ssm-parameters |
| Amazon S3 Event Notifications... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-s3-event-notifications-system-generated-tags/ |
| PostgreSQL 19 Beta 2... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/07/postgresql-19-beta-2-amazon-rds-database-preview-environment/ |
| Evolving Spec-Driven Development... | AI/LLM | google_developers | https://developers.googleblog.com/evolving-spec-driven-development-conductor-now-supports-antigravity/ |
| Building scalable AI agents... | AI/LLM | google_developers | https://developers.googleblog.com/building-scalable-ai-agents-with-modular-prompt-transpilation/ |
| Expanding Choice in Gemini... | AI/LLM | google_developers | https://developers.googleblog.com/expanding-choice-in-gemini-enterprise-agent-platform-introducing-grounding-with-parallel-web-search/ |
| New Google Meet 'Take notes...' | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/07/new-google-meet-take-notes-for-me-settings-for-admins-and-end-users.html |
| Cast yourself in AI video... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/07/cast-yourself-in-ai-video-clips-using-your-personal-avatar-with-Gemini-Omni-in-Vids.html |
| Generate higher quality AI... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/07/generate-higher-quality-ai-video-clips-and-edit-any-video-with-Gemini-Omni-in-Vids.html |
| Expanded language support... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/07/expanded-language-support-for-gemini-in-Google-Docs.html |
| Easily control the emotions... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/06/easily-steer-ai-voiceover-and-avatar-speaking-with-emotions-pacing-and-sound-effects.html |
| v0.117.0 | AI/LLM | anthropic_sdk | https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.0 |
| Quote Text in Your Messages | AI/LLM | devin_release | https://docs.devin.ai/release-notes/overview#2026-07-15-quote-text-in-your-messages |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Google Gemini Enterprise Agent PlatformがParallel Web検索と統合され、AIエージェントの正確性が大幅に向上しました。

📌 **ピックアップ**
• Google VidsがGemini Omniを搭載し、アバター生成やテキスト編集に対応
• Amazon Managed GrafanaがFedRAMP High認定を取得
• Anthropic SDKが「dreaming」機能やMCP Tunnelsをサポート

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-17*
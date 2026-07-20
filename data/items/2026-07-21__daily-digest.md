# Tech Radar Daily Digest - 2026-07-21

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Google Cloudにおける「Ray on TPU」の正式サポートが開始されました。これまで実験的な位置付けであったTPU上でのRay実行が、Ray 2.55以降、公式のプリビルドイメージとサポート体制によって「ファーストクラス」のアクセラレータとして統合されました。これにより、開発者はGPU向けに書いたRayコードを、GKE（Google Kubernetes Engine）上でTPUスライスを予約するだけで、最小限の変更でTPUの高速な計算リソースを活用できるようになります。

また、AI開発ツール界隈では、Claude Code（v2.1.216）やDevin CLI（v3000.1.27）といった主要なAIエージェントツールのアップデートが相次いでいます。特にClaude Codeでは、ファイルシステム分離の柔軟性向上や、長時間セッションでのパフォーマンス改善など、実用性を高める修正が多数行われました。これらの動きは、AIエージェントが単なる実験から、複雑な開発ワークフローを支える堅牢なツールへと進化していることを示しています。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code

##### v2.1.216

Claude Codeの最新版では、ファイルシステム分離設定の追加や、長時間セッションにおけるパフォーマンス低下の修正が行われました。また、認証トークンの回転に伴うエラー処理の改善や、@メンション機能の安定性向上など、開発体験を損なう細かいバグが広範囲に修正されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, TypeScript |
| 特徴・性能 | 長時間セッションの正規化コスト最適化、OAuth認証の安定化 |
| 対応環境 | CLI環境 |
| 関連サービス | Anthropic Claude |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.216

---

#### Devin

##### v3000.1.27

Devin CLIの最新アップデートでは、MCPサーバーのOAuth設定の柔軟性向上や、コマンドフックへのセッションID付与など、拡張性が強化されました。また、コマンド実行時の権限プロンプトのスコープ最適化や、ファイル操作・画像処理の効率化により、長時間のAIコーディングセッションにおけるコストと遅延が削減されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Devin CLI, MCP (Model Context Protocol) |
| 特徴・性能 | 権限プロンプトのスコープ最適化、セッション起動の高速化 |
| 対応環境 | CLI環境 |
| 関連サービス | Cognition AI |

> 🔗 **参考リンク**
> https://cli.devin.ai/docs/changelog/stable#2026-07-19-added

---

#### Google AI

##### Run Ray on TPU: The foundations

Ray 2.55からGoogle Cloud TPUが公式サポートされ、GKEを用いた分散コンピューティングが容易になりました。TPUスライスという固定グループの概念をRayが理解することで、大規模なAIモデルの学習や推論を、GPUと同様の感覚でTPU上で実行可能になります。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Ray, Google Cloud TPU, GKE |
| 特徴・性能 | TPUスライスのトポロジー認識、公式プリビルドイメージ対応 |
| 対応環境 | Google Cloud Platform |
| 関連サービス | Google Kubernetes Engine |

> 🔗 **参考リンク**
> https://developers.googleblog.com/run-ray-on-tpu-part-1-the-foundations/

---

### クラウド

#### AWS

##### AWS Data Exports now provides standardized Amazon Bedrock product metadata

AWS Data Exports（CUR 2.0）において、Amazon Bedrockのコスト管理用メタデータが標準化されました。これにより、モデル名や推論タイプ、機能（On-Demand/Batch）などが構造化データとして取得可能になり、FinOpsチームはカスタムロジックなしでBedrockの利用コストを正確に把握できるようになります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-data-exports-amazon-bedrock-product-metadata/

##### Amazon EC2 R8i and R8i-flex instances are now available in additional regions

Intel Xeon 6プロセッサを搭載したR8iおよびR8i-flexインスタンスが、ストックホルムおよびチューリッヒリージョンで利用可能になりました。前世代と比較して最大15%の価格性能向上と、2.5倍のメモリ帯域幅を実現しており、データベースやAI推論ワークロードに適しています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-r8i-r8i-flex-instances-in-stockholm-zurich-regions/

##### Selectively log network activity events by identity in AWS CloudTrail

AWS CloudTrailのネットワークアクティビティイベントにおいて、IAMアイデンティティに基づいたフィルタリングが可能になりました。特定のユーザーによるVPCエンドポイントアクセスのみをログに記録することで、セキュリティ監視の精度を維持しつつ、ログコストとノイズを大幅に削減できます。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/aws-cloudtrail-filter-useridentity-advance-selectors/

##### Amazon Connect delivers more natural agentic voice experiences

Amazon Connectが50以上の言語と100以上の新しい音声オプションに対応しました。AIエージェントの応答速度や感情表現を調整する機能が追加され、より人間らしく自然な対話体験を顧客に提供できるようになります。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-connect-agentic-voice/

##### Amazon EC2 I8ge instances are now available in AWS GovCloud (US) Regions

AWS Graviton4搭載のストレージ最適化インスタンス「I8ge」が、AWS GovCloud（US）で利用可能になりました。最大120TBのNVMeストレージと高いネットワーク帯域を提供し、大規模データセットを扱う高負荷なワークロードに最適化されています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-i8ge-instances-aws-govcloud-us-regions/

---

### Workspace

#### Google Sheets

##### Import and create combo charts in Google Sheets

Google Sheetsでコンボチャートの作成とインポートが強化されました。異なるスケールや指標を持つデータセットを一つのグラフで可視化できるようになり、Microsoft Excelからのインポート時にも第2軸の設定が保持されるようになっています。

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/07/import-and-create-combo-charts-in-Google-Sheets.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Bedrockのコスト分析レポートの更新確認 | FinOps担当者 | 🟡 中 |
| AIエージェントツールのアップデート適用 | 開発者 | 🟡 中 |
| CloudTrailのネットワークログフィルタ設定見直し | セキュリティ担当者 | 🔴 高 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| AWS Data Exports... | AWS | aws_whats_new | [Link](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-data-exports-amazon-bedrock-product-metadata/) |
| Amazon EC2 R8i... | AWS | aws_whats_new | [Link](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-r8i-r8i-flex-instances-in-stockholm-zurich-regions/) |
| Selectively log network... | AWS | aws_whats_new | [Link](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-cloudtrail-filter-useridentity-advance-selectors/) |
| Amazon Connect... | AWS | aws_whats_new | [Link](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-connect-agentic-voice/) |
| Amazon EC2 I8ge... | AWS | aws_whats_new | [Link](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-i8ge-instances-aws-govcloud-us-regions/) |
| v2.1.216 | Claude Code | claude_code_releases | [Link](https://github.com/anthropics/claude-code/releases/tag/v2.1.216) |
| 0.145.0-alpha.25 | OpenAI | openai_codex_cli_releases | [Link](https://github.com/openai/codex/releases/tag/rust-v0.145.0-alpha.25) |
| Run Ray on TPU... | AI | google_developers | [Link](https://developers.googleblog.com/run-ray-on-tpu-part-1-the-foundations/) |
| Import and create... | Workspace | google_workspace_updates | [Link](http://workspaceupdates.googleblog.com/2026/07/import-and-create-combo-charts-in-Google-Sheets.html) |
| Added (Devin) | AI | devin_cli_changelog | [Link](https://cli.devin.ai/docs/changelog/stable#2026-07-19-added) |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

Google CloudでRay on TPUが正式サポートされ、AIアクセラレータの活用が加速。

📌 **ピックアップ**
• AWS Bedrockのコスト管理用メタデータが標準化され、FinOpsが容易に。
• Claude CodeやDevin CLIがアップデート、開発エージェントの性能が向上。
• AWS CloudTrailでIAM単位のネットワークログフィルタリングが可能に。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-07-21*
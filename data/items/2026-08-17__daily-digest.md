# Tech Radar Daily Digest - 2026-08-17

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

Google Workspaceにおいて、Geminiを活用した「Sheets canvas」の提供が開始されました。これはスプレッドシートのデータを自然言語プロンプトで操作し、Kanbanボードやダッシュボードといったインタラクティブなミニアプリへと変換できる機能です。単なる可視化にとどまらず、キャンバス上での操作が元のシートに即座に反映される双方向の同期機能を備えており、非エンジニアでも複雑なデータ管理ツールを構築可能です。

また、対面会議の議事録を自動生成する「Take Notes for me」機能が対面会議にも対応しました。これにより、ビデオ会議だけでなくオフラインの打ち合わせでも、Geminiが自動的に要約やアクションアイテムをGoogleドキュメントにまとめ、共有する環境が整いました。これらのアップデートは、AIが単なる生成ツールから、業務プロセスそのものを変革する実務プラットフォームへと進化していることを示唆しています。

---

## 📰 今日のニュース

### AI/LLM

#### AWS SageMaker JumpStart

##### FLUX.2-small-decoderおよびgemma-4-12B-itモデルの追加

Amazon SageMaker JumpStartに、画像生成の効率化に寄与する「FLUX.2-small-decoder」と、マルチモーダル理解に優れた「gemma-4-12B-it」が追加されました。前者はVRAM消費を抑えつつ高速なデコードを実現し、後者はエンコーダーレス構造により高い推論性能とエージェント機能を両立しています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| FLUX.2-small-decoder | FLUX.2の標準デコーダーを置き換え、低VRAMで約1.4倍の高速化を実現。 |
| gemma-4-12B-it | テキスト・画像・音声を統合理解し、エージェントワークフローをサポート。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | 蒸留VAEデコーダー、マルチモーダルTransformer |
| 特徴・性能 | 高解像度での高速化、16GB RAMでの動作 |
| 対応環境 | Amazon SageMaker JumpStart |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/01/flux.2-small-decoder-gemma-4-12B-it-on-sagemaker-jumpstart/

##### 特化型モデル（langcache, Mellum2, LightOnOCR）の追加

Redis、JetBrains、LightOnが提供する3つのモデルがSageMaker JumpStartに加わりました。セマンティックキャッシュの最適化から、コード生成、高精度なOCRまで、特定の業務ニーズに特化したモデルが利用可能になります。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| langcache-embed-v3-small | LLMの冗長な呼び出しを減らすセマンティックキャッシュ用モデル。 |
| Mellum2-12B-A2.5B-Thinking | Mixture-of-Experts採用のコード生成・推論特化モデル。 |
| LightOnOCR-2-1B | ドキュメントをMarkdownやJSONへ変換する軽量OCRモデル。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Mixture-of-Experts, Vision-Language Model |
| 特徴・性能 | 131kトークンのコンテキスト長、9倍の軽量化 |
| 対応環境 | Amazon SageMaker JumpStart |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/01/langcache-embed-v3-small-mellum2-12B-A2.5B-thinking-lightOnOCR-2-1B-on-sagemaker-jumpstart/

##### GLM-5.2 FP8、Nemotron-Nano-12B-v2等の追加

長期間のタスク実行やエージェント開発に特化したモデル群が追加されました。特にGLM-5.2は100万トークンのコンテキストウィンドウをサポートし、プロジェクト全体のエンジニアリングを単一タスクで完結させる能力を備えています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| GLM-5.2 FP8 | 1Mトークンのコンテキストを扱い、長期間のソフトウェア開発を支援。 |
| NVIDIA-Nemotron-Nano-12B-v2 | Mamba-2とTransformerのハイブリッドで高スループットを実現。 |
| GLM-OCR | 複雑な数式や表を含むドキュメントをMarkdown等に変換。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | FP8量子化、Mamba-2ハイブリッド |
| 特徴・性能 | 6倍の推論スループット、128kコンテキスト長 |
| 対応環境 | Amazon SageMaker JumpStart |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/01/glm-5.2-fp8-nemotron-nano-12b-v2-glm-ocr-on-sagemaker-jumpstart/

---

### クラウド

#### AWS

##### Amazon RDS for MariaDB 12.3のサポート開始

Amazon RDS for MariaDBが最新のLTSリリースである12.3をサポートしました。Oracle互換機能の追加やJSONネイティブ検証のサポート、クエリ最適化の改善が含まれており、移行コストの低減とパフォーマンス向上が期待できます。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | MariaDB 12.3.2 |
| 特徴・性能 | Oracle TO_DATE互換、IS JSON述語、JOIN最適化 |
| 関連サービス | AWS Database Migration Service, Blue/Green Deployments |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-rds-mariadb-1232-available/

##### 高メモリインスタンス U7i がサンパウロリージョンで利用可能に

24TiBのDDR5メモリを搭載したU7in-24TBインスタンスが、AWS南米（サンパウロ）リージョンで利用可能になりました。SAP HANAやOracleなどのミッションクリティカルなインメモリデータベースの運用に最適化されています。

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | 第4世代Intel Xeon Scalable (Sapphire Rapids) |
| 特徴・性能 | 24TiBメモリ, 896 vCPU, 100Gbps EBS帯域 |

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-high-memory-u7i-south-america

---

### Workspace

#### Google Workspace

##### Google Sheetsの機能強化とConnected Sheetsの改善

Google Sheetsにおいて、Excelからのインポート精度向上や、Connected SheetsでのBigQuery分析機能が強化されました。特にリストパラメータや列エイリアス機能により、データ分析の柔軟性と可読性が大幅に向上しています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Sheets canvas | 自然言語でスプレッドシートをインタラクティブなアプリ化。 |
| Take Notes for me | 対面会議の議事録を自動生成し、Googleドキュメントに保存。 |
| Connected Sheets | リストパラメータと列エイリアスによるBigQuery分析の柔軟化。 |
| Calendar Admin | 招待の自動追加設定を組織単位で詳細に制御可能に。 |

> 🔗 **参考リンク**
> http://workspaceupdates.googleblog.com/2026/08/weekly-recap-08-14-2026.html

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| MariaDB 12.3へのアップグレード検証 | DB管理者 | 🟡 中 |
| Google Calendarの招待自動追加設定の確認 | 管理者 | 🟡 中 |
| Sheets canvasを用いた業務プロセスの自動化検討 | 業務担当者 | 🟢 低 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon RDS for MariaDB now supports MariaDB 12.3 | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-rds-mariadb-1232-available/ |
| FLUX.2-small-decoder and gemma-4-12B-it models... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/flux.2-small-decoder-gemma-4-12B-it-on-sagemaker-jumpstart/ |
| langcache-embed-v3-small, Mellum2-12B-A2.5B-Thinking... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/langcache-embed-v3-small-mellum2-12B-A2.5B-thinking-lightOnOCR-2-1B-on-sagemaker-jumpstart/ |
| GLM-5.2 FP8, NVIDIA-Nemotron-Nano-12B-v2... | AI/LLM | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/glm-5.2-fp8-nemotron-nano-12b-v2-glm-ocr-on-sagemaker-jumpstart/ |
| Amazon EC2 High Memory U7i instances... | クラウド | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-high-memory-u7i-south-america |
| Google Workspace Weekly Recap - August 14, 2026 | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/08/weekly-recap-08-14-2026.html |
| New admin controls for adding invitations... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/08/new-admin-controls-for-adding-invitations-to-Google-Calendar.html |
| Take Notes for me for in-person meetings... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/08/take-notes-with-me-for-in-person-meetings-is-now-available.html |
| Use Sheets canvas to visualize data... | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/08/use-google-sheets-canvas-to-visualize-data.html |
| New usability features in Connected Sheets | Workspace | google_workspace | http://workspaceupdates.googleblog.com/2026/08/new-usability-features-connected-sheets-google.html |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**
Google WorkspaceでGeminiを活用した「Sheets canvas」が公開され、スプレッドシートがインタラクティブなアプリへと進化しました。

📌 **ピックアップ**
• AWS SageMaker JumpStartにFLUX.2やGemmaなど最新モデルが多数追加
• Amazon RDS for MariaDB 12.3が利用可能に
• Google Meetの議事録作成機能が対面会議にも対応
• Google SheetsとBigQueryの連携機能が大幅強化

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-08-17*
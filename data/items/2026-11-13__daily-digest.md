# Tech Radar Daily Digest - 2026-11-13

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

**AIエージェントのセキュリティと信頼性向上に向けた新機能が続々登場**
AIエージェントが実務で利用される機会が増える中、セキュリティと制御性を高めるアップデートが相次いでいます。Googleは「Agent Anomaly Detection」の有効性を公開し、エージェントによる不正な指示（プロンプトインジェクション）の検知能力を実証しました。一方、AWSはAmazon CognitoでOAuth 2.0トークン交換をサポートし、エージェントがユーザーの代理として特定の権限のみを持つトークンで下流サービスを呼び出せる仕組みを導入しました。これらの動きは、AIエージェントを「実験」から「安全な業務遂行ツール」へと進化させる重要なステップです。

---

## 📰 今日のニュース

### AI/LLM

#### Claude Code, Devin

##### Claude Code v2.1.323 リリース
Claude Codeに実験的な「Code Mode」が追加され、Claude自身がJavaScriptを記述してツールを呼び出すことが可能になりました。また、プラグインの型チェック機能や、Perforceモードの通知、Artifactへの.docxファイルアップロード対応など、開発者体験を向上させる多数の改善が含まれています。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| Code Mode | ClaudeがJavaScriptを書いてツールを呼び出す実験的機能。 |
| プラグイン強化 | TypeScriptフックの型チェックや、エンジンバージョン管理の厳格化。 |
| ユーザー体験 | 認証情報の不足時やモデル制限時のオプションメニュー表示、Artifactの.docx対応。 |

**技術ポイント**

| 項目 | 詳細 |
|------|------|
| 主要技術 | Claude Code, TypeScript, JavaScript |
| 特徴・性能 | ツール呼び出しの自動化、プラグインの安全性向上 |

> 🔗 **参考リンク**
> https://github.com/anthropics/claude-code/releases/tag/v2.1.323

##### Devin 11月11日・12日アップデート
Devinのセッション管理とセキュリティ機能が大幅に強化されました。セッションのカード統合やリマインダー機能の追加に加え、Devin ReviewのUI刷新や、Veracode/Black Duckとの連携によるセキュリティスキャン機能の強化（ベータ）が行われました。

**機能別の概要**

| 機能 | 概要 |
|------|------|
| セッション管理 | 関連リクエストのカード統合や、ドラッグ＆ドロップ操作の改善。 |
| Devin Review | UIの刷新と、自動修正設定の個別化。 |
| セキュリティ | 複数接続へのスキャン同期や、Veracode/Black Duckとの連携。 |

> 🔗 **参考リンク**
> https://docs.devin.ai/release-notes/overview#2026-11-12-sessions-workspace

#### Google Gemini

##### Geminiと制約ソルバーによるGo言語のバグ検出
Googleは、GeminiとZ3制約ソルバーを組み合わせることで、ファジングテストでは見逃されがちなGo言語のランタイムパニックを特定する手法を公開しました。コンパイラのSSA最適化で残った境界チェックトラップをソルバーで解析することで、効率的なバグ検出を実現しています。

> 🔗 **参考リンク**
> https://developers.googleblog.com/catch-go-bugs-that-fuzzing-misses-with-gemini-and-a-constraint-solver/

---

### クラウド

#### AWS

##### Amazon CognitoがOAuth 2.0トークン交換をサポート
Amazon CognitoがRFC 8693に準拠したトークン交換をサポートしました。これにより、AIエージェントやサービスがユーザーの代理として行動する際、元のトークンよりも権限を制限した新しいトークンを発行でき、セキュリティが大幅に向上します。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-token-exchange/

##### Amazon Aurora/RDSでGraviton5 (R9g) インスタンスが利用可能に
Graviton5ベースのR9gインスタンスがAuroraおよびRDSで一般提供開始されました。Graviton4と比較して最大30%のパフォーマンス向上と、最大22%の価格性能比改善を実現しています。

> 🔗 **参考リンク**
> https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-aurora-rds-postgresql-mysql-mariadb-r9g-instances/

---

## 💡 今日のアクションポイント

| アクション | 対象者 | 優先度 |
|------------|--------|--------|
| Cognitoのトークン交換機能を活用したエージェント権限の最小化検討 | AWS利用者 | 🔴 高 |
| Claude Codeの「Code Mode」を試用し、ツール呼び出しの効率化を確認 | 開発者 | 🟡 中 |
| RDS/AuroraのGraviton5インスタンスへの移行検証 | インフラ担当 | 🟡 中 |

---

## 📚 元記事一覧

| タイトル | カテゴリ | ソース | URL |
|---------|----------|--------|-----|
| Amazon Cognito now supports OAuth 2.0 token exchange | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-token-exchange/ |
| Amazon Aurora and RDS now support Graviton5-based R9g database instances | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-aurora-rds-postgresql-mysql-mariadb-r9g-instances/ |
| Amazon MWAA now supports fine-grained access control | AWS | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/11/mwaa-fine-grained-access-control/ |
| v2.1.323 (Claude Code) | AI | claude_code | https://github.com/anthropics/claude-code/releases/tag/v2.1.323 |
| Catch Go bugs that fuzzing misses with Gemini | AI | google_developers | https://developers.googleblog.com/catch-go-bugs-that-fuzzing-misses-with-gemini-and-a-constraint-solver/ |
| Sessions & Workspace (Devin) | AI | devin_release_notes | https://docs.devin.ai/release-notes/overview#2026-11-12-sessions-workspace |

---

## 📢 Slack通知用サマリー

<!-- SLACK_SUMMARY_START -->
🚀 **今日の注目ポイント**

AIエージェントのセキュリティ強化：Cognitoのトークン交換サポートとGoogleの異常検知技術が公開。

📌 **ピックアップ**
• Claude Code v2.1.323：実験的な「Code Mode」追加でツール呼び出しを自動化。
• AWS RDS/Aurora：Graviton5 (R9g) インスタンスで最大30%の性能向上。
• Devin：セキュリティスキャン機能の強化とセッション管理の改善。

👉 詳細はサイトでチェック！
<!-- SLACK_SUMMARY_END -->

---

*生成日: 2026-11-13*
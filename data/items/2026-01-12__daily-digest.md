# Tech Radar Daily Digest - 2026-01-12

今日の技術ニュースから注目のトピックをお届けします。

---

## 🔥 注目トピック

### Gemini 3 Flash が Gemini CLI で利用可能に
Google の Gemini 3 Flash が Gemini CLI で利用可能になりました。これにより、ターミナルベースの作業で一般的な高頻度ワークフローをサポートします。Gemini 3 Flash は、エージェントによるコーディングにおいて 78% の SWE-bench Verified スコアを達成し、Gemini 3 Pro よりも低いコストで利用できます。また、Agent Development Kit (ADK) for TypeScript が発表され、TypeScript と JavaScript の開発者は、使い慣れた言語とエコシステムを使用して、強力な AI エージェントとマルチエージェントシステムを構築、効率化、デプロイできます。

---

## 📰 今日のニュース

### AI/LLM

#### Gemini 3 Flash is now available in Gemini CLI
- **要点**: GoogleのGemini 3 FlashがGemini CLIで利用可能になり、高速かつ低コストで高品質なコーディングが可能になりました。
- **技術ポイント**: SWE-bench Verified スコア 78% を達成し、Gemini 3 Pro よりも低コストで利用可能。
- **リンク**: https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/

#### Conductor: Introducing context-driven development for Gemini CLI
- **要点**: Gemini CLI の新しい拡張機能である Conductor は、コンテキスト駆動開発を導入し、コードと共に永続的な Markdown ファイルで正式な仕様と計画を作成できます。
- **技術ポイント**: プロジェクトのコンテキストをチャットウィンドウからコードベースに移行し、リポジトリを単一の信頼できる情報源として扱います。
- **リンク**: https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/

#### Introducing Agent Development Kit for TypeScript: Build AI Agents with the Power of a Code-First Approach
- **要点**: Agent Development Kit (ADK) for TypeScript が発表され、TypeScript と JavaScript の開発者は、使い慣れた言語とエコシステムを使用して、強力な AI エージェントとマルチエージェントシステムを構築できます。
- **技術ポイント**: コードファーストのアプローチにより、エージェントのロジック、ツール、オーケストレーションを TypeScript で直接定義できます。
- **リンク**: https://developers.googleblog.com/introducing-agent-development-kit-for-typescript-build-ai-agents-with-the-power-of-a-code-first-approach/

#### Developer’s guide to multi-agent patterns in ADK
- **要点**: Google Agent Development Kit (ADK) を使用して、マルチエージェントシステムの設計パターンを解説しています。
- **技術ポイント**: Sequential Pipeline、Coordinator/Dispatcher パターンなど、8 つの主要な設計パターンを紹介し、モジュール性、テスト容易性、信頼性を向上させます。
- **リンク**: https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/

#### Introducing A2UI: An open project for agent-driven interfaces
- **要点**: エージェントが生成するインターフェースのためのオープンプロジェクト A2UI が発表されました。
- **技術ポイント**: A2UI は、エージェントが現在の会話に最適なインターフェースを生成し、フロントエンドアプリケーションに送信できる形式と実装を提供します。
- **リンク**: https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/

#### v2.1.5, v2.1.4, v2.1.3, v2.1.2, v2.1.1
- **要点**: AnthropicのClaude-codeのアップデート。
- **技術ポイント**: 環境変数の追加、バグ修正、機能改善など。
- **リンク**:
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.5
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.4
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.3
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.2
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.1

#### v2.15.0
- **要点**: OpenAI Pythonライブラリのアップデート。
- **技術ポイント**: レスポンスにcompleted_atプロパティを追加。
- **リンク**: https://github.com/openai/openai-python/releases/tag/v2.15.0

### クラウド

#### Amazon SageMaker HyperPod now validates service quotas before creating clusters on console
- **要点**: Amazon SageMaker HyperPod コンソールが、クラスター作成前に AWS アカウントのサービスクォータを検証するようになりました。
- **技術ポイント**: クラスター構成に対してアカウントレベルのクォータを自動的にチェックし、クォータ超過の可能性がある場合に警告を表示します。
- **リンク**: https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-sagemaker-hyperpod-validates-service-quotas/

#### Amazon Lex launches configurable voice activity detection sensitivity
- **要点**: Amazon Lex が、ボットロケールごとに設定可能な 3 つの VAD 感度レベルを提供するようになりました。
- **技術ポイント**: デフォルト、高、最大の設定があり、さまざまなノイズ環境に対応します。
- **リンク**: https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-lex-configurable-voice-activity-detection-sensitivity/

#### Amazon Connect now provides agent screen recording status tracking
- **要点**: Amazon Connect が、Amazon EventBridge を使用して、エージェントの画面録画ステータスをほぼリアルタイムで CloudWatch で表示する機能を提供するようになりました。
- **技術ポイント**: 画面録画の成功/失敗、失敗コード、クライアントバージョン、ブラウザバージョン、OS、録画の開始/終了時間などのステータスを追跡できます。
- **リンク**: https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-connect-agent-screen-recording-status-tracking

#### Amazon Redshift Serverless is now available in the AWS Asia Pacific (New Zealand) region
- **要点**: Amazon Redshift Serverless が AWS アジアパシフィック (ニュージーランド) リージョンで一般提供されるようになりました。
- **技術ポイント**: データウェアハウスのプロビジョニングと管理なしに、分析を実行およびスケーリングできます。
- **リンク**: https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-redshift-serverless-aws-asia-pacific-new-zealand-region

#### Amazon Inspector adds Java Gradle support and expands ecosystem coverage
- **要点**: Amazon Inspector が Java Gradle のサポートを追加し、MySQL、MariaDB、PHP などのカバレッジを拡張しました。
- **技術ポイント**: Lambda 関数と ECR イメージのスキャンで、Java Gradle のインベントリと脆弱性スキャンをサポートします。
- **リンク**: https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-inspector-java-gradle-ecosystem/

### Workspace

#### Set Google Forms to automatically stop accepting responses based on date and time or response count
- **要点**: Googleフォームで、日付と時間または回答数に基づいて、回答の受付を自動的に停止するように設定できます。
- **技術ポイント**: フォームの作成者は、特定の期日または回答数に達するとフォームを自動的に閉じるように設定できます。
- **リンク**: http://workspaceupdates.googleblog.com/2026/01/forms-stop-collecting-responses.html

#### Google Workspace Updates Weekly Recap - January 9, 2026
- **要点**: Google Workspace の週次アップデートのまとめ。
- **技術ポイント**: Apple Intelligence Writing Tools の管理、Dropbox から Google Drive へのファイル移行、Gemini を使用した Classroom でのポッドキャスト形式のオーディオレッスン生成などが含まれます。
- **リンク**: http://workspaceupdates.googleblog.com/2026/01/weekly-recap-01-09-2026.html.html

#### Emojis reactions in Gmail will now be on by default
- **要点**: Gmail での絵文字リアクションがデフォルトでオンになります。
- **技術ポイント**: 2026 年 2 月 9 日から、Gmail での絵文字リアクションがデフォルトで有効になります。管理者は、管理コンソールでこの機能を無効にできます。
- **リンク**: http://workspaceupdates.googleblog.com/2026/01/emojis-reactions-in-gmail-will-be-on-by-default.html

#### More user control for “Take notes for me” in Google Meet
- **要点**: Google Meet で「Take notes for me」のユーザーコントロールが強化されました。
- **技術ポイント**: ユーザーは、会議を主催するたびに「Take notes for me」を自動的に開始するかどうかを選択できます。
- **リンク**: http://workspaceupdates.googleblog.com/2026/01/google-meet-take-notes-for-me-controls.html

#### Control Speech Translation in Google Meet for your users
- **要点**: Google Meet での音声翻訳の管理機能が追加されました。
- **技術ポイント**: 管理者は、管理コンソールでこの機能を制御できます。この機能は、Gemini for Meet 管理設定が有効になっている場合にのみ利用可能です。
- **リンク**: http://workspaceupdates.googleblog.com/2026/01/control-speech-translation-in-meet.html

---

## 💡 今日のアクションポイント

- Gemini 3 Flash を Gemini CLI で試して、高速なコーディングを体験する。
- Amazon SageMaker HyperPod のクォータ検証機能を活用して、AI/ML クラスターの作成を効率化する。
- Google Forms の自動停止設定を利用して、データ収集を効率的に管理する。
- Amazon Inspector を使用して、Java Gradle プロジェクトの脆弱性スキャンを強化する。
- Google Meet の音声翻訳機能を試して、多言語コミュニケーションを円滑にする。

---

## 📚 元記事一覧

| タイトル | ソース | URL |
|---------|--------|-----|
| Amazon SageMaker HyperPod now validates service quotas before creating clusters on console | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-sagemaker-hyperpod-validates-service-quotas/ |
| Amazon Lex launches configurable voice activity detection sensitivity | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-lex-configurable-voice-activity-detection-sensitivity/ |
| Amazon Connect now provides agent screen recording status tracking | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-connect-agent-screen-recording-status-tracking |
| Amazon Redshift Serverless is now available in the AWS Asia Pacific (New Zealand) region | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-redshift-serverless-aws-asia-pacific-new-zealand-region |
| Amazon Inspector adds Java Gradle support and expands ecosystem coverage | rss:aws_whats_new | https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-inspector-java-gradle-ecosystem/ |
| v2.1.5 | rss:claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.5 |
| v2.1.4 | rss:claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.4 |
| v2.1.3 | rss:claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.3 |
| v2.1.2 | rss:claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.2 |
| v2.1.1 | rss:claude_code_releases | https://github.com/anthropics/claude-code/releases/tag/v2.1.1 |
| v2.15.0 | rss:openai_sdk_releases | https://github.com/openai/openai-python/releases/tag/v2.15.0 |
| Gemini 3 Flash is now available in Gemini CLI | rss:google_developers | https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/ |
| Conductor: Introducing context-driven development for Gemini CLI | rss:google_developers | https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/ |
| Introducing Agent Development Kit for TypeScript: Build AI Agents with the Power of a Code-First Approach | rss:google_developers | https://developers.googleblog.com/introducing-agent-development-kit-for-typescript-build-ai-agents-with-the-power-of-a-code-first-approach/ |
| Developer’s guide to multi-agent patterns in ADK | rss:google_developers | https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/ |
| Introducing A2UI: An open project for agent-driven interfaces | rss:google_developers | https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/ |
| Set Google Forms to automatically stop accepting responses based on date and time or response count | rss:google_workspace_updates | http://workspaceupdates.googleblog.com/2026/01/forms-stop-collecting-responses.html |
| Google Workspace Updates Weekly Recap - January 9, 2026 | rss:google_workspace_updates | http://workspaceupdates.googleblog.com/2026/01/weekly-recap-01-09-2026.html.html |
| Emojis reactions in Gmail will now be on by default | rss:google_workspace_updates | http://workspaceupdates.googleblog.com/2026/01/emojis-reactions-in-gmail-will-be-on-by-default.html |
| More user control for “Take notes for me” in Google Meet | rss:google_workspace_updates | http://workspaceupdates.googleblog.com/2026/01/google-meet-take-notes-for-me-controls.html |
| Control Speech Translation in Google Meet for your users | rss:google_workspace_updates | http://workspaceupdates.googleblog.com/2026/01/control-speech-translation-in-meet.html |

---

*生成日: 2026-01-12*
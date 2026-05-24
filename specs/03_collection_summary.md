# 取得コンテンツ・取得方法・要約方法

この文書は、現行実装における Tech Radar の収集対象、取得方式、要約方式をまとめたものです。

## 1. 取得対象コンテンツ

取得対象は `collector/sources.yaml` で管理する。現在有効なソースは以下の通り。

| 種別 | name | URL | 主なタグ | 備考 |
|------|------|-----|----------|------|
| rss | aws_whats_new | https://aws.amazon.com/about-aws/whats-new/recent/feed/ | aws, cloud | AWS公式新着情報 |
| rss | claude_code_releases | https://github.com/anthropics/claude-code/releases.atom | ai, claude, claude_code, anthropic | Claude Code の GitHub Releases |
| rss | openai_codex_cli_releases | https://github.com/openai/codex/releases.atom | ai, chatgpt, openai, codex, codex_cli | OpenAI Codex CLI の GitHub Releases |
| rss | google_developers | https://developers.googleblog.com/feeds/posts/default | ai, gemini, google | Google Developers Blog |
| rss | google_workspace_updates | https://workspaceupdates.googleblog.com/atom.xml | google, notebooklm, workspace | Google Workspace Updates |
| rss | anthropic_sdk_releases | https://github.com/anthropics/anthropic-sdk-python/releases.atom | ai, claude, anthropic, api | Anthropic Python SDK の GitHub Releases |
| scrape | devin_release_notes | https://docs.devin.ai/release-notes/overview | ai, devin, cognition | Devin Release Notes |
| scrape | devin_cli_changelog | https://cli.devin.ai/docs/changelog/stable | ai, devin, cognition, cli | Devin for Terminal Changelog |
| scrape | cursor_changelog | https://cursor.com/changelog | ai, cursor, editor | Cursor Changelog |

現在は `keyword` 型の収集関数もあるが、実装は将来拡張用のプレースホルダーで、記事は返さない。

コメントアウトされている候補ソースとして、Anthropic 公式ニュースと OpenAI 公式ニュースがある。GCP Blog、DeepMind Blog、Google AI Blog は、コストや優先度の理由で低優先度として扱われている。

## 2. 収集条件

標準の運用条件は以下。

| 項目 | 現在値 | 実装箇所 |
|------|--------|----------|
| 取得対象期間 | 直近7日以内 | `--max-age-days` のデフォルト |
| ソースごとの最大件数 | 3件 | `--max-items` のデフォルト |
| 実行日 | JST の当日 | 日次ダイジェストの日付に使用 |
| 重複除外 | 過去の全ダイジェストに含まれる URL を除外 | `get_all_existing_urls()` |
| 同一実行内の重複除外 | 取得済み URL を `existing_urls` に追加して除外 | RSS/scrape 共通 |
| 保存単位 | 1日1つの日次ダイジェスト | `data/items/{YYYY-MM-DD}__daily-digest.md` |

GitHub Actions では `collect.yml` が毎日 UTC 22:17、JST 7:17 に実行される。手動実行では `max_items`、`max_age_days`、`source`、`dry_run` を指定できる。

## 3. 取得方法

### RSS/Atom

`type: rss` のソースは `feedparser` で RSS/Atom フィードを解析する。

処理の流れ:

1. `fetch_rss_entries()` がフィードを取得する。
2. `published` または `updated` を記事日付として読む。
3. `max_age_days` の範囲外の記事を除外する。日付をパースできない場合は安全側として対象に含める。
4. 各ソースの上限より多めに `max_items * 2` 件まで候補を取得する。
5. 過去ダイジェストまたは同一実行で収集済みの URL を除外する。
6. 候補記事の URL に対して本文抽出を行う。
7. 本文抽出に成功したものだけを日次ダイジェストの入力にする。

RSS エントリからは `title`、`url`、`published`、`summary` を取得する。ただし要約に使う本文は、原則として記事 URL から HTML を取得して抽出した本文である。

### Changelog/Release Notes のスクレイピング

`type: scrape` のソースは、RSS がない changelog または release notes ページを対象にする。

処理の流れ:

1. 対象ページを HTTP GET する。
2. HTML から `script`、`style`、`nav`、`header`、`footer`、`aside`、`form` を除去する。
3. `article`、`main`、`body` の優先順で本文に近いテキストを抽出する。
4. テキスト行から日付見出しを検出する。
5. 日付ごとのセクションに分割する。
6. `max_age_days` の範囲外のセクションを除外する。
7. セクション内の先頭付近からタイトルらしい行を探し、見つからなければ日付見出しをタイトルにする。
8. 元 URL に日付とタイトル由来の slug を付けた疑似 URL を作り、重複除外に使う。
9. セクション本文をそのまま日次ダイジェストの入力にする。

現在の日付検出は、Cursor の `May 6, 2026` 系の表記と Devin CLI の `2026.4.30-0` 系の表記を想定している。

### HTML 本文抽出

RSS 記事の本文抽出と scrape ページのテキスト抽出は、共通して `requests` と BeautifulSoup を使う。

主な仕様:

- User-Agent は `Mozilla/5.0 (compatible; TechRadarBot/1.0; +https://github.com/tech-radar)`。
- HTTP タイムアウトは標準 30 秒。
- 本文候補は `article`、`main`、`body` の優先順。
- 抽出後は空行を除去し、行単位で整形する。
- RSS 記事本文は LLM 入力用に最大 15,000 文字までに制限し、超過分は省略メッセージを付ける。

## 4. 要約方法

現在の通常フローでは、個別記事ごとの要約は行わず、収集した記事群をまとめて日次ダイジェストとして1回で要約する。

要約は OpenRouter の Chat Completions API を使う。

| 項目 | 内容 |
|------|------|
| API | `https://openrouter.ai/api/v1/chat/completions` |
| API キー | `OPENROUTER_API_KEY` |
| モデル | `OPENROUTER_MODEL`。未設定時は `google/gemini-3-flash-preview` |
| プロンプト | `collector/prompts/daily_digest.md` |
| max_tokens | 4000 |
| temperature | 0.3 |
| timeout | 120 秒 |

日次ダイジェストの入力には、各記事について以下を渡す。

- タイトル
- URL
- ソース名
- タグ
- 本文の先頭 3,000 文字

出力は日本語 Markdown として生成する。プロンプトでは、以下の構成を要求している。

- `Tech Radar Daily Digest - {日付}` のタイトル
- 注目トピック
- カテゴリ別の今日のニュース
- 記事ごとの段落形式の要約（2-3文）
- 複数機能のアップデート・追加が言及されている場合は、機能別の概要表
- 技術ポイントの表
- 参考リンク
- 今日のアクションポイント
- 元記事一覧
- Slack 通知用サマリー

LLM が Markdown コードブロックで返した場合は、保存前に外側の ```markdown ... ``` を除去する。

## 5. 保存方法

要約結果は `save_daily_digest()` により保存する。

保存されるファイル:

| ファイル | 内容 |
|----------|------|
| `data/items/{YYYY-MM-DD}__daily-digest.md` | 生成された日次ダイジェスト本文 |
| `data/items/{YYYY-MM-DD}__daily-digest.meta.json` | 記事数、URL、タグ、ソースなどのメタデータ |
| `data/index.json` | サイト表示用のインデックス |

メタデータには、記事数、含まれる URL、集約したタグ、集約したソース、作成日時が含まれる。

## 6. 失敗時の扱い

- ソース設定が空の場合は収集を終了する。
- 記事が1件も集まらなかった場合は保存しない。
- RSS 記事で本文抽出に失敗したものはスキップする。
- OpenRouter API キーがない、API エラー、レスポンス解析失敗、空の要約の場合は保存しない。
- `dry_run` の場合は、収集対象をログ出力するだけで要約と保存は行わない。


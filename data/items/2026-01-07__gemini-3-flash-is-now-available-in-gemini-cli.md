```markdown
# Gemini 3 Flash が Gemini CLI で利用可能に

## 要点
- Gemini 3 Flash が Gemini CLI で利用可能になり、ターミナルベースの作業における高頻度ワークフローをサポート。
- Gemini 3 Flash は、エージェントコーディングにおいて SWE-bench Verified スコア 78% を達成し、Gemini 3 Pro よりも低コストで高速。

## 技術的ポイント
- Gemini 3 Flash は、推論、ツール利用、マルチモーダル機能において高いパフォーマンスを発揮。
- 大規模なコンテキストウィンドウを処理し、ノイズから重要な情報を抽出して正確な編集を実行可能。
- `asyncio` を使用した Python スクリプト生成による同時実行ユーザーのシミュレーションで、Web アプリケーションの負荷テストを迅速に実行。

## 影響・アクション
- Gemini CLI を最新バージョン (0.21.1) にアップデートして Gemini 3 Flash を利用可能にする。
- `/settings` でプレビュー機能を有効にし、`/model` で Gemini 3 を選択。
- Gemini 3 Flash を利用して、プロトタイプの構築やインフラ管理をより高速かつ効率的に行う。

## 元記事
- URL: https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/
- 取得日: 2026-01-07
```
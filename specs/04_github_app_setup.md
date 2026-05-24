# GitHub App セットアップ手順

`main` ブランチに ruleset（`protect main`）を適用した場合、`collect.yml` / `cleanup.yml` の `git push` は **PR 必須ルール** により拒否されます。

`github-actions[bot]` は ruleset の bypass list に追加できないため、**専用 GitHub App** を作成し、bypass 権限を付与して workflow から App token で push します。

## 前提

| 項目 | 内容 |
|------|------|
| 料金 | GitHub Free で利用可能（App 作成・インストールに追加料金なし） |
| 対象 workflow | `collect.yml`（日次ダイジェスト commit）、`cleanup.yml`（記事削除 commit） |
| 対象外 | `pages.yml`（push しない）、`test.yml`（PR 用 CI） |

## 全体の流れ

```
1. GitHub App を作成
2. 権限・鍵を設定
3. リポジトリにインストール
4. ruleset の bypass list に App を追加
5. Secrets / Variables を登録
6. workflow を App token 利用に変更
7. 動作確認
```

---

## 1. GitHub App を作成

> **注意:** Developer settings は **リポジトリの Settings にはありません**。  
> 右上の **自分のアカウント** の Settings から開きます。

### 行き方（2通り）

**A. 直接 URL（いちばん早い）**

- App 一覧: https://github.com/settings/apps
- 新規作成: https://github.com/settings/apps/new

**B. UI から**

1. GitHub 右上の **プロフィールアイコン** をクリック
2. **Settings** をクリック（`Your repositories` や `tech-radar` の Settings **ではない**）
3. 左サイドバーを **一番下までスクロール**
4. **Developer settings** → **GitHub Apps** → **New GitHub App**

左サイドバーの並び（下の方）:

```
...
Codespaces
...
← ここから下にスクロール
Developer settings   ← これ
```

### 基本設定

| 項目 | 推奨値 |
|------|--------|
| GitHub App name | `tech-radar-bot`（任意・リポジトリ内で一意） |
| Homepage URL | `https://github.com/kozuke/tech-radar` |
| Webhook | **Active** のチェックを **外す**（不要） |
| Where can this GitHub App be installed? | **Only on this account** |

### Repository permissions

| Permission | Access |
|------------|--------|
| **Contents** | Read and write |

その他の権限は **No access** のままでよい。

### Subscribe to events

Webhook を無効にしているため設定不要。

4. **Create GitHub App** をクリック

---

## 2. 秘密鍵を生成

1. 作成した App の設定ページを開く
2. **Private keys** → **Generate a private key**
3. ダウンロードされた `.pem` ファイルを安全な場所に保管（再ダウンロード不可）

---

## 3. App ID を控える

App 設定ページ上部の **App ID**（数字）をメモする。

例: `1234567`

---

## 4. リポジトリにインストール

1. App 設定ページ左サイドバー → **Install App**
2. 自分のアカウントの **Install** をクリック
3. **Only select repositories** → `tech-radar` を選択
4. **Install**

---

## 5. ruleset に bypass を追加

1. リポジトリ → **Settings** → **Rules** → **Rulesets**
2. `protect main` を開く
3. **Bypass list** → **Add bypass**
4. 検索欄に App 名（例: `tech-radar-bot`）を入力
5. 表示された **GitHub App** を選択 → **Add selected**
6. Bypass mode は **Always allow**（collect / cleanup は PR ではなく direct push のため）

> `github-actions[bot]` は bypass list に表示されません。必ず **GitHub App** を選んでください。

---

## 6. Secrets / Variables を登録

`tech-radar` → **Settings** → **Secrets and variables** → **Actions**

> **重要:** App ID と秘密鍵は **別タブ** に登録します。App ID を Secret タブだけに入れると `Input required and not supplied: app-id` エラーになります。

**Variables タブ**（Repository variables）

| Name | 値 |
|------|-----|
| `TECH_RADAR_APP_ID` | 手順 3 で控えた App ID（例: `3837213`） |

**Secrets タブ**（Repository secrets）

| Name | 値 |
|------|-----|
| `TECH_RADAR_APP_PRIVATE_KEY` | ダウンロードした `.pem` ファイルの **全文** |

---

## 7. workflow を変更

`collect.yml` / `cleanup.yml` は App token を使うよう設定済みです。主な変更点:

- `actions/create-github-app-token@v1` で installation token を発行
- `actions/checkout@v4` の `token` に App token を指定
- commit 作者を `tech-radar-bot[bot]` に設定

```yaml
      - name: Generate GitHub App token
        id: app-token
        uses: actions/create-github-app-token@v1
        with:
          app-id: ${{ vars.TECH_RADAR_APP_ID }}
          private-key: ${{ secrets.TECH_RADAR_APP_PRIVATE_KEY }}

      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ steps.app-token.outputs.token }}
```

commit / push ステップでは git user を App 名に合わせます。

```yaml
      - name: Commit and push
        run: |
          git config --local user.name "tech-radar-bot[bot]"
          git config --local user.email "3837213+tech-radar-bot[bot]@users.noreply.github.com"
          git add data/
          git commit -m "chore: add daily digest $(date +'%Y-%m-%d')"
          git push
```

---

## 8. 動作確認

### チェックリスト

- [ ] ruleset bypass list に App が追加されている
- [ ] `TECH_RADAR_APP_ID`（Variable）が設定されている
- [ ] `TECH_RADAR_APP_PRIVATE_KEY`（Secret）が設定されている
- [ ] workflow の checkout が App token を使用している

### 確認方法

1. **Actions** → **Collect Articles** → **Run workflow**（dry_run: false）
2. 成功し、`main` に commit されることを確認
3. commit 作者が `tech-radar-bot[bot]` になっていることを確認

失敗時は Actions ログの `remote:` メッセージを確認する。

| エラー | 原因の例 |
|--------|----------|
| `Input required and not supplied: app-id` | `TECH_RADAR_APP_ID` が **Variables** 未登録（Secret タブのみに入れている） |
| `Resource not accessible by integration` | App の Contents 権限不足 |
| `Changes must be made through a pull request` | bypass list に App 未追加、または checkout が GITHUB_TOKEN のまま |
| `Bad credentials` | 秘密鍵の形式不正、App ID の typo |

---

## 代替案: Admin PAT（手軽だが非推奨）

個人リポジトリで急ぎの場合:

1. fine-grained PAT を作成（Contents: Read and write、`tech-radar` のみ）
2. Secret `ADMIN_PAT` として登録
3. ruleset bypass に **Repository admin** を追加
4. checkout の `token: ${{ secrets.ADMIN_PAT }}` を指定

PAT は漏洩リスク・有効期限管理が必要なため、長期運用は GitHub App を推奨。

---

## 関連ドキュメント

- [Installing your own GitHub App](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app)
- [Creating rulesets for a repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
- [actions/create-github-app-token](https://github.com/actions/create-github-app-token)

---
layout: home

hero:
  name: "Tech Radar"
  text: "技術トレンドを自動収集"
  tagline: LLMで要約された技術記事を毎日お届け
  image:
    src: /logo.svg
    alt: Tech Radar
  actions:
    - theme: brand
      text: 記事を見る
      link: /articles/
    - theme: alt
      text: タグ一覧
      link: /tags/
    - theme: alt
      text: GitHub
      link: https://github.com/your-username/tech-radar

features:
  - icon: 🤖
    title: AI自動要約
    details: OpenRouter APIを使用してLLMが記事を自動要約。重要なポイントを素早く把握できます。
  - icon: 📡
    title: 多様な情報源
    details: PostgreSQL、AWS、GitHub、Hacker Newsなど、主要な技術ブログから自動収集。
  - icon: 🏷️
    title: タグ分類
    details: 技術カテゴリごとにタグ付け。興味のある分野だけを効率的にチェック。
  - icon: ⚡
    title: 毎日自動更新
    details: GitHub Actionsで毎日自動実行。常に最新の技術情報をキャッチアップ。
---

<script setup>
import ArticleList from './.vitepress/theme/components/ArticleList.vue'
</script>

## 最新記事

<ArticleList :limit="5" />

<div style="text-align: center; margin-top: 2rem;">
  <a href="/tech-radar/articles/" class="VPButton medium brand">すべての記事を見る →</a>
</div>

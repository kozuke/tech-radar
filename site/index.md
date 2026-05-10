---
layout: page
lastUpdated: false
---

<script setup>
import ArticleList from './.vitepress/theme/components/ArticleList.vue'
</script>

<section class="top-hero">
  <div>
    <p class="top-kicker">Daily Tech Briefing</p>
    <h1>Tech Radar</h1>
    <p class="top-summary">技術系ブログ・公式リリース・チェンジログを毎日収集し、LLM で要約した日次ダイジェストとして配信しています。</p>
  </div>
  <nav class="top-actions" aria-label="主要リンク">
    <a href="./tags/" class="VPButton medium brand">タグから探す</a>
    <a href="./about" class="VPButton medium alt">About</a>
  </nav>
</section>

<section class="top-articles" aria-labelledby="latest-articles">
  <div class="top-section-heading">
    <h2 id="latest-articles">Latest Issues</h2>
  </div>

  <ArticleList featuredFirst showStats showTagPanel showFilter />
</section>

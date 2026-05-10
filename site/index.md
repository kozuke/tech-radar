---
layout: page
lastUpdated: false
head:
  - - link
    - rel: stylesheet
      href: /tr-design.css
  - - link
    - rel: stylesheet
      href: /tech-radar/tr-design.css
---

<script setup>
import ArticleList from './.vitepress/theme/components/ArticleList.vue'
</script>

<section class="top-hero">
  <div>
    <p class="top-kicker">Daily Tech Briefing</p>
    <h1>Tech Radar</h1>
    <p class="top-summary">LLMで要約した技術記事を毎日更新。</p>
  </div>
  <nav class="top-actions" aria-label="主要リンク">
    <a href="./tags/" class="VPButton medium brand">タグから探す</a>
    <a href="./about" class="VPButton medium alt">About</a>
  </nav>
</section>

<section class="top-articles" aria-labelledby="latest-articles">
  <div class="top-section-heading">
    <h2 id="latest-articles">最新記事</h2>
  </div>

  <ArticleList featuredFirst showStats showTagPanel showFilter />
</section>

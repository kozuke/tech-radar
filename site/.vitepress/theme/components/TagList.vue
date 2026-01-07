<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

interface Article {
  id: string
  date: string
  title: string
  url: string
  tags: string[]
  source: string
  summary_path: string
}

interface IndexData {
  generated_at: string
  items: Article[]
}

const articles = ref<Article[]>([])
const loading = ref(true)

onMounted(async () => {
  try {
    const response = await fetch('/tech-radar/data/index.json')
    if (!response.ok) {
      const devResponse = await fetch('../../data/index.json')
      if (!devResponse.ok) throw new Error('Failed to load')
      const data: IndexData = await devResponse.json()
      articles.value = data.items || []
    } else {
      const data: IndexData = await response.json()
      articles.value = data.items || []
    }
  } catch (e) {
    console.error('Failed to load articles:', e)
    articles.value = []
  } finally {
    loading.value = false
  }
})

// タグと記事数のマップ
const tagCounts = computed(() => {
  const counts = new Map<string, number>()
  articles.value.forEach(a => {
    a.tags.forEach(tag => {
      counts.set(tag, (counts.get(tag) || 0) + 1)
    })
  })
  return counts
})

// ソートされたタグ一覧
const sortedTags = computed(() => {
  return Array.from(tagCounts.value.entries())
    .sort((a, b) => b[1] - a[1])
})

// タグサイズの計算（記事数に応じて）
const getTagSize = (count: number) => {
  const max = Math.max(...tagCounts.value.values())
  if (count >= max * 0.7) return 'large'
  return ''
}
</script>

<template>
  <div class="tag-list">
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
    </div>

    <div v-else-if="sortedTags.length === 0" class="no-articles">
      <p>タグがありません</p>
    </div>

    <div v-else class="tag-cloud">
      <a
        v-for="[tag, count] in sortedTags"
        :key="tag"
        :href="`/tech-radar/articles/?tag=${tag}`"
        :class="['tag', getTagSize(count)]"
      >
        {{ tag }} ({{ count }})
      </a>
    </div>
  </div>
</template>

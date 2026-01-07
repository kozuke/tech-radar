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

const props = defineProps<{
  limit?: number
  tag?: string
  showFilter?: boolean
}>()

const articles = ref<Article[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const selectedTag = ref<string>(props.tag || '')
const searchQuery = ref('')

// 記事データを読み込み
onMounted(async () => {
  try {
    // ビルド時はdata/index.jsonを参照
    const response = await fetch('/tech-radar/data/index.json')
    if (!response.ok) {
      // 開発時のフォールバック
      const devResponse = await fetch('../../data/index.json')
      if (!devResponse.ok) {
        throw new Error('Failed to load articles')
      }
      const data: IndexData = await devResponse.json()
      articles.value = data.items || []
    } else {
      const data: IndexData = await response.json()
      articles.value = data.items || []
    }
  } catch (e) {
    console.error('Failed to load articles:', e)
    error.value = '記事の読み込みに失敗しました'
    articles.value = []
  } finally {
    loading.value = false
  }
})

// フィルタリングされた記事
const filteredArticles = computed(() => {
  let result = articles.value

  // タグフィルター
  if (selectedTag.value) {
    result = result.filter(a => a.tags.includes(selectedTag.value))
  }

  // 検索フィルター
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(a =>
      a.title.toLowerCase().includes(query) ||
      a.tags.some(t => t.toLowerCase().includes(query))
    )
  }

  // 件数制限
  if (props.limit) {
    result = result.slice(0, props.limit)
  }

  return result
})

// 全タグを取得
const allTags = computed(() => {
  const tagSet = new Set<string>()
  articles.value.forEach(a => a.tags.forEach(t => tagSet.add(t)))
  return Array.from(tagSet).sort()
})

// 日付フォーマット
const formatDate = (dateStr: string) => {
  const date = new Date(dateStr)
  return date.toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

// ソース名の短縮表示
const formatSource = (source: string) => {
  return source.replace('rss:', '').replace(/_/g, ' ')
}

// 記事詳細ページのパスを生成
const getArticlePath = (article: Article) => {
  // summary_pathからパスを生成
  // data/items/2026-01-07__example.md -> /articles/2026-01-07__example
  const filename = article.summary_path.split('/').pop()?.replace('.md', '') || article.id
  return `/articles/${filename}`
}
</script>

<template>
  <div class="article-list">
    <!-- フィルターセクション -->
    <div v-if="showFilter" class="filter-section">
      <div style="display: flex; gap: 1rem; flex-wrap: wrap; align-items: center;">
        <div>
          <label for="tag-filter">タグ:</label>
          <select id="tag-filter" v-model="selectedTag">
            <option value="">すべて</option>
            <option v-for="tag in allTags" :key="tag" :value="tag">
              {{ tag }}
            </option>
          </select>
        </div>
        <div style="flex: 1; min-width: 200px;">
          <label for="search">検索:</label>
          <input
            id="search"
            v-model="searchQuery"
            type="text"
            placeholder="タイトルやタグで検索..."
            style="width: 100%;"
          />
        </div>
      </div>
    </div>

    <!-- ローディング -->
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
    </div>

    <!-- エラー -->
    <div v-else-if="error" class="no-articles">
      <p>{{ error }}</p>
    </div>

    <!-- 記事なし -->
    <div v-else-if="filteredArticles.length === 0" class="no-articles">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
      <p>記事がありません</p>
      <p style="font-size: 0.9rem;">収集を実行すると記事が表示されます</p>
    </div>

    <!-- 記事一覧 -->
    <div v-else>
      <div v-for="article in filteredArticles" :key="article.id" class="article-card">
        <h3>
          <a :href="`/tech-radar/articles/${article.id}.html`">
            {{ article.title }}
          </a>
        </h3>

        <div class="article-meta">
          <span class="date">
            📅 {{ formatDate(article.date) }}
          </span>
          <span class="source">
            📰 {{ formatSource(article.source) }}
          </span>
          <a :href="article.url" target="_blank" rel="noopener noreferrer" class="original-link">
            🔗 元記事
          </a>
        </div>

        <div class="tags">
          <a
            v-for="tag in article.tags"
            :key="tag"
            :href="`/tech-radar/tags/?tag=${tag}`"
            class="tag"
          >
            {{ tag }}
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

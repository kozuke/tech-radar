<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

interface Article {
  id: string
  date: string
  title: string
  type?: string
  // 個別記事の場合
  url?: string
  source?: string
  // daily_digestの場合
  urls?: string[]
  sources?: string[]
  article_count?: number
  tags: string[]
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
  featuredFirst?: boolean
  showStats?: boolean
  showTagPanel?: boolean
}>()

const articles = ref<Article[]>([])
const generatedAt = ref('')
const loading = ref(true)
const error = ref<string | null>(null)
const selectedTag = ref<string>(props.tag || '')
const searchQuery = ref('')

const getTagFromQuery = () => {
  if (typeof window === 'undefined') return props.tag || ''
  return new URLSearchParams(window.location.search).get('tag') || props.tag || ''
}

const getTagFilterPath = (tag: string) => `/tech-radar/?tag=${encodeURIComponent(tag)}`

const selectTag = (tag: string, event: MouseEvent) => {
  event.preventDefault()
  selectedTag.value = tag
  if (typeof window !== 'undefined') {
    window.history.pushState({}, '', getTagFilterPath(tag))
  }
}

const syncTagFromQuery = () => {
  selectedTag.value = getTagFromQuery()
}

// 記事データを読み込み
onMounted(async () => {
  syncTagFromQuery()
  if (typeof window !== 'undefined') {
    window.addEventListener('popstate', syncTagFromQuery)
  }

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
      generatedAt.value = data.generated_at || ''
    } else {
      const data: IndexData = await response.json()
      articles.value = data.items || []
      generatedAt.value = data.generated_at || ''
    }
  } catch (e) {
    console.error('Failed to load articles:', e)
    error.value = '記事の読み込みに失敗しました'
    articles.value = []
  } finally {
    loading.value = false
  }
})

onUnmounted(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('popstate', syncTagFromQuery)
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

const featuredArticle = computed(() => {
  if (!props.featuredFirst) return null
  return filteredArticles.value[0] || null
})

const listArticles = computed(() => {
  if (!props.featuredFirst) return filteredArticles.value
  return filteredArticles.value.slice(1)
})

// 全タグを取得
const allTags = computed(() => {
  const tagSet = new Set<string>()
  articles.value.forEach(a => a.tags.forEach(t => tagSet.add(t)))
  return Array.from(tagSet).sort()
})

const tagCounts = computed(() => {
  const counts = new Map<string, number>()
  articles.value.forEach(a => {
    a.tags.forEach(tag => {
      counts.set(tag, (counts.get(tag) || 0) + 1)
    })
  })
  return counts
})

const topTags = computed(() => {
  return Array.from(tagCounts.value.entries())
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .slice(0, 10)
})

const totalSourceCount = computed(() => {
  return articles.value.reduce((total, article) => {
    if (article.type === 'daily_digest') return total + (article.article_count || 0)
    return total + 1
  }, 0)
})

const latestArticleDate = computed(() => {
  return articles.value[0]?.date || generatedAt.value
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

const formatShortDate = (dateStr: string) => {
  if (!dateStr) return '-'
  const date = new Date(dateStr)
  return date.toLocaleDateString('ja-JP', {
    month: 'short',
    day: 'numeric'
  })
}

// ソース名の短縮表示
const formatSource = (source: string | string[] | undefined) => {
  if (!source) return ''
  if (Array.isArray(source)) {
    return source.map(s => s.replace('rss:', '').replace(/_/g, ' ')).join(', ')
  }
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
      <div class="filter-row">
        <div class="filter-field filter-field-tag">
          <label for="tag-filter">タグ:</label>
          <select id="tag-filter" v-model="selectedTag">
            <option value="">すべて</option>
            <option v-for="tag in allTags" :key="tag" :value="tag">
              {{ tag }}
            </option>
          </select>
        </div>
        <div class="filter-field filter-field-search">
          <label for="search">検索:</label>
          <input
            id="search"
            v-model="searchQuery"
            type="text"
            placeholder="タイトルやタグで検索..."
          />
        </div>
        <p class="filter-result">
          {{ filteredArticles.length }}件
        </p>
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

    <template v-else>
      <div v-if="showStats" class="article-stats" aria-label="記事の状態">
        <div class="article-stat">
          <span>最新更新</span>
          <strong>{{ formatShortDate(latestArticleDate) }}</strong>
        </div>
        <div class="article-stat">
          <span>記事</span>
          <strong>{{ articles.length }}</strong>
        </div>
        <div class="article-stat">
          <span>ソース</span>
          <strong>{{ totalSourceCount }}</strong>
        </div>
        <div class="article-stat">
          <span>タグ</span>
          <strong>{{ allTags.length }}</strong>
        </div>
      </div>

      <!-- 記事一覧 -->
      <div :class="['article-content', { 'with-tag-panel': showTagPanel }]">
        <div class="article-feed">
          <article v-if="featuredArticle" class="article-card article-card-featured">
            <div v-if="featuredArticle.tags.length" class="featured-label">
              {{ featuredArticle.tags[0] }}
            </div>
            <h3>
              <a :href="`/tech-radar/articles/${featuredArticle.id}.html`">
                {{ featuredArticle.title }}
              </a>
            </h3>

            <div class="article-meta">
              <span class="date">
                📅 {{ formatDate(featuredArticle.date) }}
              </span>
              <span v-if="featuredArticle.type === 'daily_digest'" class="source">
                📰 {{ featuredArticle.article_count }}件のソースから
              </span>
              <span v-else class="source">
                📰 {{ formatSource(featuredArticle.source) }}
              </span>
              <a v-if="featuredArticle.url" :href="featuredArticle.url" target="_blank" rel="noopener noreferrer" class="original-link">
                🔗 元記事
              </a>
            </div>

            <div class="tags">
              <a
                v-for="tag in featuredArticle.tags"
                :key="tag"
                :href="getTagFilterPath(tag)"
                class="tag"
                @click="selectTag(tag, $event)"
              >
                {{ tag }}
              </a>
            </div>
          </article>

          <article v-for="article in listArticles" :key="article.id" class="article-card">
            <h3>
              <a :href="`/tech-radar/articles/${article.id}.html`">
                {{ article.title }}
              </a>
            </h3>

            <div class="article-meta">
              <span class="date">
                📅 {{ formatDate(article.date) }}
              </span>
              <span v-if="article.type === 'daily_digest'" class="source">
                📰 {{ article.article_count }}件のソースから
              </span>
              <span v-else class="source">
                📰 {{ formatSource(article.source) }}
              </span>
              <a v-if="article.url" :href="article.url" target="_blank" rel="noopener noreferrer" class="original-link">
                🔗 元記事
              </a>
            </div>

            <div class="tags">
              <a
                v-for="tag in article.tags"
                :key="tag"
                :href="getTagFilterPath(tag)"
                class="tag"
                @click="selectTag(tag, $event)"
              >
                {{ tag }}
              </a>
            </div>
          </article>
        </div>

        <aside v-if="showTagPanel" class="top-tag-panel" aria-label="注目タグ">
          <div class="top-tag-panel-heading">
            <h3>注目タグ</h3>
            <a href="/tech-radar/tags/">一覧</a>
          </div>
          <a
            v-for="[tag, count] in topTags"
            :key="tag"
            :href="getTagFilterPath(tag)"
            class="top-tag-row"
            @click="selectTag(tag, $event)"
          >
            <span>{{ tag }}</span>
            <strong>{{ count }}</strong>
          </a>
        </aside>
      </div>
    </template>
  </div>
</template>

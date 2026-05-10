import { defineComponent, ref, onMounted, onUnmounted, computed, mergeProps, unref, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrIncludeBooleanAttr, ssrLooseContain, ssrLooseEqual, ssrRenderList, ssrRenderAttr, ssrInterpolate, ssrRenderStyle, ssrRenderClass } from "vue/server-renderer";
import { w as withBase } from "./Content.DXcVHMZc.js";
const _sfc_main = /* @__PURE__ */ defineComponent({
  __name: "ArticleList",
  __ssrInlineRender: true,
  props: {
    limit: {},
    tag: {},
    showFilter: { type: Boolean },
    featuredFirst: { type: Boolean },
    showStats: { type: Boolean },
    showTagPanel: { type: Boolean }
  },
  setup(__props) {
    const props = __props;
    const articles = ref([]);
    const generatedAt = ref("");
    const loading = ref(true);
    const error = ref(null);
    const selectedTag = ref(props.tag || "");
    const searchQuery = ref("");
    const getTagFromQuery = () => {
      if (typeof window === "undefined") return props.tag || "";
      return new URLSearchParams(window.location.search).get("tag") || props.tag || "";
    };
    const getTagFilterPath = (tag) => withBase(`/?tag=${encodeURIComponent(tag)}`);
    const syncTagFromQuery = () => {
      selectedTag.value = getTagFromQuery();
    };
    const siteDataUrl = `${"/tech-radar/"}data/index.json`;
    onMounted(async () => {
      syncTagFromQuery();
      if (typeof window !== "undefined") {
        window.addEventListener("popstate", syncTagFromQuery);
      }
      try {
        const response = await fetch(siteDataUrl);
        if (!response.ok) {
          throw new Error(`Failed to load articles: ${response.status}`);
        }
        const data = await response.json();
        articles.value = data.items || [];
        generatedAt.value = data.generated_at || "";
      } catch (e) {
        console.error("Failed to load articles:", e);
        error.value = "記事の読み込みに失敗しました";
        articles.value = [];
      } finally {
        loading.value = false;
      }
    });
    onUnmounted(() => {
      if (typeof window !== "undefined") {
        window.removeEventListener("popstate", syncTagFromQuery);
      }
    });
    const filteredArticles = computed(() => {
      let result = articles.value;
      if (selectedTag.value) {
        result = result.filter((a) => a.tags.includes(selectedTag.value));
      }
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase();
        result = result.filter(
          (a) => a.title.toLowerCase().includes(query) || a.tags.some((t) => t.toLowerCase().includes(query))
        );
      }
      if (props.limit) {
        result = result.slice(0, props.limit);
      }
      return result;
    });
    const featuredArticle = computed(() => {
      if (!props.featuredFirst) return null;
      return filteredArticles.value[0] || null;
    });
    const listArticles = computed(() => {
      if (!props.featuredFirst) return filteredArticles.value;
      return filteredArticles.value.slice(1);
    });
    const allTags = computed(() => {
      const tagSet = /* @__PURE__ */ new Set();
      articles.value.forEach((a) => a.tags.forEach((t) => tagSet.add(t)));
      return Array.from(tagSet).sort();
    });
    const tagCounts = computed(() => {
      const counts = /* @__PURE__ */ new Map();
      articles.value.forEach((a) => {
        a.tags.forEach((tag) => {
          counts.set(tag, (counts.get(tag) || 0) + 1);
        });
      });
      return counts;
    });
    const topTags = computed(() => {
      return Array.from(tagCounts.value.entries()).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])).slice(0, 10);
    });
    const totalSourceCount = computed(() => {
      return articles.value.reduce((total, article) => {
        if (article.type === "daily_digest") return total + (article.article_count || 0);
        return total + 1;
      }, 0);
    });
    const latestArticleDate = computed(() => {
      var _a;
      return ((_a = articles.value[0]) == null ? void 0 : _a.date) || generatedAt.value;
    });
    const formatDate = (dateStr) => {
      const date = new Date(dateStr);
      return date.toLocaleDateString("ja-JP", {
        year: "numeric",
        month: "short",
        day: "numeric"
      });
    };
    const formatShortDate = (dateStr) => {
      if (!dateStr) return "-";
      const date = new Date(dateStr);
      return date.toLocaleDateString("ja-JP", {
        month: "short",
        day: "numeric"
      });
    };
    const formatSource = (source) => {
      if (!source) return "";
      if (Array.isArray(source)) {
        return source.map((s) => s.replace("rss:", "").replace(/_/g, " ")).join(", ");
      }
      return source.replace("rss:", "").replace(/_/g, " ");
    };
    const getArticlePath = (article) => {
      var _a;
      const filename = ((_a = article.summary_path.split("/").pop()) == null ? void 0 : _a.replace(".md", "")) || article.id;
      return withBase(`/articles/${filename}.html`);
    };
    return (_ctx, _push, _parent, _attrs) => {
      _push(`<div${ssrRenderAttrs(mergeProps({ class: "article-list" }, _attrs))}>`);
      if (__props.showFilter) {
        _push(`<div class="filter-section"><div class="filter-row"><div class="filter-field filter-field-tag"><label for="tag-filter">タグ:</label><select id="tag-filter"><option value=""${ssrIncludeBooleanAttr(Array.isArray(selectedTag.value) ? ssrLooseContain(selectedTag.value, "") : ssrLooseEqual(selectedTag.value, "")) ? " selected" : ""}>すべて</option><!--[-->`);
        ssrRenderList(allTags.value, (tag) => {
          _push(`<option${ssrRenderAttr("value", tag)}${ssrIncludeBooleanAttr(Array.isArray(selectedTag.value) ? ssrLooseContain(selectedTag.value, tag) : ssrLooseEqual(selectedTag.value, tag)) ? " selected" : ""}>${ssrInterpolate(tag)}</option>`);
        });
        _push(`<!--]--></select></div><div class="filter-field filter-field-search"><label for="search">検索:</label><input id="search"${ssrRenderAttr("value", searchQuery.value)} type="text" placeholder="タイトルやタグで検索..."></div><p class="filter-result">${ssrInterpolate(filteredArticles.value.length)}件 </p></div></div>`);
      } else {
        _push(`<!---->`);
      }
      if (loading.value) {
        _push(`<div class="loading"><div class="spinner"></div></div>`);
      } else if (error.value) {
        _push(`<div class="no-articles"><p>${ssrInterpolate(error.value)}</p></div>`);
      } else if (filteredArticles.value.length === 0) {
        _push(`<div class="no-articles"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg><p>記事がありません</p><p style="${ssrRenderStyle({ "font-size": "0.9rem" })}">収集を実行すると記事が表示されます</p></div>`);
      } else {
        _push(`<!--[-->`);
        if (__props.showStats) {
          _push(`<div class="article-stats" aria-label="記事の状態"><div class="article-stat"><span>最新更新</span><strong>${ssrInterpolate(formatShortDate(latestArticleDate.value))}</strong></div><div class="article-stat"><span>記事</span><strong>${ssrInterpolate(articles.value.length)}</strong></div><div class="article-stat"><span>ソース</span><strong>${ssrInterpolate(totalSourceCount.value)}</strong></div><div class="article-stat"><span>タグ</span><strong>${ssrInterpolate(allTags.value.length)}</strong></div></div>`);
        } else {
          _push(`<!---->`);
        }
        _push(`<div class="${ssrRenderClass(["article-content", { "with-tag-panel": __props.showTagPanel }])}"><div class="article-feed">`);
        if (featuredArticle.value) {
          _push(`<article class="article-card article-card-featured">`);
          if (featuredArticle.value.tags.length) {
            _push(`<div class="featured-label">${ssrInterpolate(featuredArticle.value.tags[0])}</div>`);
          } else {
            _push(`<!---->`);
          }
          _push(`<h3><a${ssrRenderAttr("href", getArticlePath(featuredArticle.value))}>${ssrInterpolate(featuredArticle.value.title)}</a></h3><div class="article-meta"><span class="date"> 📅 ${ssrInterpolate(formatDate(featuredArticle.value.date))}</span>`);
          if (featuredArticle.value.type === "daily_digest") {
            _push(`<span class="source"> 📰 ${ssrInterpolate(featuredArticle.value.article_count)}件のソースから </span>`);
          } else {
            _push(`<span class="source"> 📰 ${ssrInterpolate(formatSource(featuredArticle.value.source))}</span>`);
          }
          if (featuredArticle.value.url) {
            _push(`<a${ssrRenderAttr("href", featuredArticle.value.url)} target="_blank" rel="noopener noreferrer" class="original-link"> 🔗 元記事 </a>`);
          } else {
            _push(`<!---->`);
          }
          _push(`</div><div class="tags"><!--[-->`);
          ssrRenderList(featuredArticle.value.tags, (tag) => {
            _push(`<a${ssrRenderAttr("href", getTagFilterPath(tag))} class="tag">${ssrInterpolate(tag)}</a>`);
          });
          _push(`<!--]--></div></article>`);
        } else {
          _push(`<!---->`);
        }
        _push(`<!--[-->`);
        ssrRenderList(listArticles.value, (article) => {
          _push(`<article class="article-card"><h3><a${ssrRenderAttr("href", getArticlePath(article))}>${ssrInterpolate(article.title)}</a></h3><div class="article-meta"><span class="date"> 📅 ${ssrInterpolate(formatDate(article.date))}</span>`);
          if (article.type === "daily_digest") {
            _push(`<span class="source"> 📰 ${ssrInterpolate(article.article_count)}件のソースから </span>`);
          } else {
            _push(`<span class="source"> 📰 ${ssrInterpolate(formatSource(article.source))}</span>`);
          }
          if (article.url) {
            _push(`<a${ssrRenderAttr("href", article.url)} target="_blank" rel="noopener noreferrer" class="original-link"> 🔗 元記事 </a>`);
          } else {
            _push(`<!---->`);
          }
          _push(`</div><div class="tags"><!--[-->`);
          ssrRenderList(article.tags, (tag) => {
            _push(`<a${ssrRenderAttr("href", getTagFilterPath(tag))} class="tag">${ssrInterpolate(tag)}</a>`);
          });
          _push(`<!--]--></div></article>`);
        });
        _push(`<!--]--></div>`);
        if (__props.showTagPanel) {
          _push(`<aside class="top-tag-panel" aria-label="注目タグ"><div class="top-tag-panel-heading"><h3>注目タグ</h3><a${ssrRenderAttr("href", unref(withBase)("/tags/"))}>一覧</a></div><!--[-->`);
          ssrRenderList(topTags.value, ([tag, count]) => {
            _push(`<a${ssrRenderAttr("href", getTagFilterPath(tag))} class="top-tag-row"><span>${ssrInterpolate(tag)}</span><strong>${ssrInterpolate(count)}</strong></a>`);
          });
          _push(`<!--]--></aside>`);
        } else {
          _push(`<!---->`);
        }
        _push(`</div><!--]-->`);
      }
      _push(`</div>`);
    };
  }
});
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add(".vitepress/theme/components/ArticleList.vue");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
export {
  _sfc_main as _
};

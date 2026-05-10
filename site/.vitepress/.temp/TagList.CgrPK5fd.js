import { defineComponent, ref, onMounted, computed, mergeProps, useSSRContext } from "vue";
import { ssrRenderAttrs, ssrRenderList, ssrRenderAttr, ssrRenderClass, ssrInterpolate } from "vue/server-renderer";
import { w as withBase } from "./Content.DXcVHMZc.js";
const _sfc_main = /* @__PURE__ */ defineComponent({
  __name: "TagList",
  __ssrInlineRender: true,
  setup(__props) {
    const articles = ref([]);
    const loading = ref(true);
    const siteDataUrl = `${"/tech-radar/"}data/index.json`;
    onMounted(async () => {
      try {
        const response = await fetch(siteDataUrl);
        if (!response.ok) {
          throw new Error(`Failed to load articles: ${response.status}`);
        }
        const data = await response.json();
        articles.value = data.items || [];
      } catch (e) {
        console.error("Failed to load articles:", e);
        articles.value = [];
      } finally {
        loading.value = false;
      }
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
    const sortedTags = computed(() => {
      return Array.from(tagCounts.value.entries()).sort((a, b) => b[1] - a[1]);
    });
    const getTagSize = (count) => {
      const max = Math.max(...tagCounts.value.values());
      if (count >= max * 0.7) return "large";
      return "";
    };
    const getTagFilterPath = (tag) => withBase(`/?tag=${encodeURIComponent(tag)}`);
    return (_ctx, _push, _parent, _attrs) => {
      _push(`<div${ssrRenderAttrs(mergeProps({ class: "tag-list" }, _attrs))}>`);
      if (loading.value) {
        _push(`<div class="loading"><div class="spinner"></div></div>`);
      } else if (sortedTags.value.length === 0) {
        _push(`<div class="no-articles"><p>タグがありません</p></div>`);
      } else {
        _push(`<div class="tag-cloud"><!--[-->`);
        ssrRenderList(sortedTags.value, ([tag, count]) => {
          _push(`<a${ssrRenderAttr("href", getTagFilterPath(tag))} class="${ssrRenderClass(["tag", getTagSize(count)])}">${ssrInterpolate(tag)} (${ssrInterpolate(count)}) </a>`);
        });
        _push(`<!--]--></div>`);
      }
      _push(`</div>`);
    };
  }
});
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add(".vitepress/theme/components/TagList.vue");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
export {
  _sfc_main as _
};

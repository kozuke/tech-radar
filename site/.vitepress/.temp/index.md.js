import { ssrRenderAttrs, ssrRenderComponent } from "vue/server-renderer";
import { _ as _sfc_main$1 } from "./ArticleList.XiQ0_1Iq.js";
import { useSSRContext } from "vue";
import "./Content.DXcVHMZc.js";
import "@vueuse/core";
const __pageData = JSON.parse('{"title":"","description":"","frontmatter":{"layout":"page","lastUpdated":false},"headers":[],"relativePath":"index.md","filePath":"index.md"}');
const __default__ = { name: "index.md" };
const _sfc_main = /* @__PURE__ */ Object.assign(__default__, {
  __ssrInlineRender: true,
  setup(__props) {
    return (_ctx, _push, _parent, _attrs) => {
      _push(`<div${ssrRenderAttrs(_attrs)}><section class="top-hero"><div><p class="top-kicker">Daily Tech Briefing</p><h1>Tech Radar</h1><p class="top-summary">LLMで要約した技術記事を毎日更新。</p></div><nav class="top-actions" aria-label="主要リンク"><a href="./tags/" class="VPButton medium brand">タグから探す</a><a href="./about" class="VPButton medium alt">About</a></nav></section><section class="top-articles" aria-labelledby="latest-articles"><div class="top-section-heading"><h2 id="latest-articles">最新記事</h2></div>`);
      _push(ssrRenderComponent(_sfc_main$1, {
        featuredFirst: "",
        showStats: "",
        showTagPanel: "",
        showFilter: ""
      }, null, _parent));
      _push(`</section></div>`);
    };
  }
});
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("index.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
export {
  __pageData,
  _sfc_main as default
};

import { ssrRenderAttrs, ssrRenderComponent } from "vue/server-renderer";
import { _ as _sfc_main$1 } from "./TagList.CgrPK5fd.js";
import { useSSRContext } from "vue";
import "./Content.DXcVHMZc.js";
import "@vueuse/core";
const __pageData = JSON.parse('{"title":"タグ一覧","description":"","frontmatter":{"title":"タグ一覧","lastUpdated":false},"headers":[],"relativePath":"tags/index.md","filePath":"tags/index.md"}');
const __default__ = { name: "tags/index.md" };
const _sfc_main = /* @__PURE__ */ Object.assign(__default__, {
  __ssrInlineRender: true,
  setup(__props) {
    return (_ctx, _push, _parent, _attrs) => {
      _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="タグ一覧" tabindex="-1">タグ一覧 <a class="header-anchor" href="#タグ一覧" aria-label="Permalink to &quot;タグ一覧&quot;">​</a></h1><p class="page-lead">気になる技術カテゴリから、ホームの記事一覧を絞り込めます。</p>`);
      _push(ssrRenderComponent(_sfc_main$1, null, null, _parent));
      _push(`</div>`);
    };
  }
});
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("tags/index.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
export {
  __pageData,
  _sfc_main as default
};

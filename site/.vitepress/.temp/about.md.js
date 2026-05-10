import { ssrRenderAttrs } from "vue/server-renderer";
import { useSSRContext } from "vue";
import { _ as _export_sfc } from "./plugin-vue_export-helper.1tPrXgE0.js";
const __pageData = JSON.parse('{"title":"About","description":"","frontmatter":{"title":"About","lastUpdated":false},"headers":[],"relativePath":"about.md","filePath":"about.md"}');
const _sfc_main = { name: "about.md" };
function _sfc_ssrRender(_ctx, _push, _parent, _attrs, $props, $setup, $data, $options) {
  _push(`<div${ssrRenderAttrs(_attrs)}><h1 id="tech-radar-について" tabindex="-1">Tech Radar について <a class="header-anchor" href="#tech-radar-について" aria-label="Permalink to &quot;Tech Radar について&quot;">​</a></h1><p class="page-lead">技術ニュースを収集し、LLMで日次ダイジェストにまとめる小さな閲覧サイトです。</p><div class="info-grid"><section><h2>見るもの</h2><p>AWS、AI開発ツール、Google Workspace、主要SDKなどの更新情報を横断して確認できます。</p></section><section><h2>使い方</h2><p>ホームで検索するか、タグから関心領域を絞り込んでください。各記事から日次ダイジェストの詳細を読めます。</p></section><section><h2>仕組み</h2><p>収集結果はMarkdownとJSONで保存し、VitePressで静的サイトとして配信しています。</p></section></div></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("about.md");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const about = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);
export {
  __pageData,
  about as default
};

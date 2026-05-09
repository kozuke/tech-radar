from pathlib import Path


ARTICLE_LIST = Path("site/.vitepress/theme/components/ArticleList.vue")
TAG_LIST = Path("site/.vitepress/theme/components/TagList.vue")


def test_article_list_reads_tag_query_parameter_for_filtering():
    component = ARTICLE_LIST.read_text(encoding="utf-8")

    assert "new URLSearchParams(window.location.search).get('tag')" in component
    assert "syncTagFromQuery()" in component
    assert "window.addEventListener('popstate', syncTagFromQuery)" in component
    assert "window.removeEventListener('popstate', syncTagFromQuery)" in component


def test_article_card_tag_links_to_filtered_article_list():
    component = ARTICLE_LIST.read_text(encoding="utf-8")

    assert "const getTagFilterPath = (tag: string)" in component
    assert "`/tech-radar/?tag=${encodeURIComponent(tag)}`" in component
    assert ':href="getTagFilterPath(tag)"' in component
    assert '@click="selectTag(tag, $event)"' in component
    assert "/tech-radar/tags/?tag=" not in component


def test_tag_list_uses_encoded_article_filter_links():
    component = TAG_LIST.read_text(encoding="utf-8")

    assert "const getTagFilterPath = (tag: string)" in component
    assert "`/tech-radar/?tag=${encodeURIComponent(tag)}`" in component
    assert ':href="getTagFilterPath(tag)"' in component

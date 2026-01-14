#!/usr/bin/env python3
"""
Tech Radar Collector
技術記事を収集し、日次ダイジェストを生成してdata/に保存する
"""

import argparse
import logging
import yaml
from pathlib import Path
from datetime import datetime
from typing import List, Dict

from utils.fetcher import fetch_rss_entries, extract_article_content
from utils.summarizer import summarize_daily_digest
from utils.storage import (
    load_index,
    save_daily_digest,
    get_existing_urls_for_date,
)

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# パス設定
COLLECTOR_DIR = Path(__file__).parent
SOURCES_PATH = COLLECTOR_DIR / "sources.yaml"
DATA_DIR = COLLECTOR_DIR.parent / "data"


def load_sources() -> List[Dict]:
    """情報源定義を読み込む"""
    if not SOURCES_PATH.exists():
        logger.error(f"Sources file not found: {SOURCES_PATH}")
        return []

    try:
        with open(SOURCES_PATH, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return config.get("sources", [])
    except Exception as e:
        logger.error(f"Failed to load sources: {e}")
        return []


def collect_rss_articles(
    source: Dict,
    max_items: int = 5,
    existing_urls: set = None,
    max_age_days: int = 7,
) -> List[Dict]:
    """
    RSSソースから記事を収集する（要約はしない）

    Args:
        source: ソース定義
        max_items: 処理する最大件数
        existing_urls: 既存のURLセット（重複チェック用）
        max_age_days: 最大日数（この日数以内の記事のみ取得）

    Returns:
        収集した記事のリスト（本文含む）
    """
    name = source.get("name", "unknown")
    url = source.get("url", "")
    tags = source.get("tags", [])
    existing_urls = existing_urls or set()

    logger.info(f"Collecting from RSS source: {name} (max {max_age_days} days old)")

    # 日付フィルタリング付きで取得
    entries = fetch_rss_entries(url, limit=max_items * 2, max_age_days=max_age_days)

    articles = []
    for entry in entries:
        if len(articles) >= max_items:
            break

        article_url = entry.get("url", "")
        if not article_url:
            continue

        # 重複チェック
        if article_url in existing_urls:
            logger.debug(f"Skipping existing article: {article_url}")
            continue

        title = entry.get("title", "Untitled")
        logger.info(f"Fetching content: {title}")

        # 本文抽出
        content = extract_article_content(article_url)
        if not content:
            logger.warning(f"Failed to extract content: {article_url}")
            continue

        articles.append({
            "title": title,
            "url": article_url,
            "content": content,
            "source": f"rss:{name}",
            "tags": tags,
        })

        # URLを既存リストに追加（同一実行内での重複防止）
        existing_urls.add(article_url)

    return articles


def collect_keyword_articles(
    source: Dict,
    max_items: int = 5,
    existing_urls: set = None,
) -> List[Dict]:
    """
    キーワード検索ソースから記事を収集する（将来の拡張用）

    Args:
        source: ソース定義
        max_items: 処理する最大件数
        existing_urls: 既存のURLセット

    Returns:
        収集した記事のリスト
    """
    name = source.get("name", "unknown")
    query = source.get("query", "")

    logger.info(f"Keyword source '{name}' with query '{query}' - not implemented yet")

    # TODO: SerpApi等を使った検索実装
    return []


def run_collection(
    max_items_per_source: int = 3,
    max_age_days: int = 7,
    dry_run: bool = False,
    source_filter: str = None,
) -> Dict:
    """
    メイン収集処理
    1. 全ソースから記事を収集（日付フィルタリング適用）
    2. 収集した記事をまとめて日次ダイジェストとして要約
    3. 1つのMarkdownファイルとして保存

    Args:
        max_items_per_source: ソースごとの最大処理件数
        max_age_days: 最大日数（この日数以内の記事のみ取得）
        dry_run: Trueの場合は保存しない
        source_filter: 特定のソースのみ処理する場合の名前

    Returns:
        処理結果の統計
    """
    sources = load_sources()
    if not sources:
        logger.error("No sources configured")
        return {"total": 0, "success": 0, "failed": 0}

    today = datetime.now().strftime("%Y-%m-%d")
    
    logger.info(f"Filtering articles from the last {max_age_days} days")
    
    # 今日のダイジェストに既に含まれているURLを取得
    existing_urls = get_existing_urls_for_date(today, DATA_DIR)
    logger.info(f"Found {len(existing_urls)} existing URLs for {today}")

    stats = {"total": 0, "success": 0, "failed": 0, "sources": {}}
    all_articles = []

    # 全ソースから記事を収集
    for source in sources:
        source_name = source.get("name", "unknown")
        source_type = source.get("type", "")

        # フィルタリング
        if source_filter and source_name != source_filter:
            continue

        try:
            if source_type == "rss":
                articles = collect_rss_articles(
                    source, max_items_per_source, existing_urls, max_age_days
                )
            elif source_type == "keyword":
                articles = collect_keyword_articles(
                    source, max_items_per_source, existing_urls
                )
            else:
                logger.warning(f"Unknown source type: {source_type}")
                continue

            stats["sources"][source_name] = len(articles)
            stats["total"] += len(articles)
            all_articles.extend(articles)

        except Exception as e:
            logger.error(f"Error collecting from source {source_name}: {e}")
            stats["failed"] += 1

    # 記事が収集できなかった場合
    if not all_articles:
        logger.warning("=" * 50)
        logger.warning("NO NEW ARTICLES COLLECTED")
        logger.warning("Possible reasons:")
        logger.warning("  1. All articles were filtered by max_age_days")
        logger.warning("  2. All articles already exist in today's digest")
        logger.warning("  3. Failed to fetch/extract content from all sources")
        logger.warning(f"  - max_age_days: {max_age_days}")
        logger.warning(f"  - existing_urls count: {len(existing_urls)}")
        if existing_urls:
            logger.warning(f"  - existing_urls sample: {list(existing_urls)[:3]}")
        logger.warning("=" * 50)
        return stats

    logger.info(f"Collected {len(all_articles)} articles total")
    logger.info("Collected article URLs:")
    for article in all_articles:
        logger.info(f"  - {article['url']}")

    if dry_run:
        logger.info("[DRY RUN] Would create daily digest with:")
        for article in all_articles:
            logger.info(f"  - {article['title']} ({article['source']})")
        stats["success"] = len(all_articles)
        return stats

    # 日次ダイジェストを生成
    logger.info("Generating daily digest summary...")
    digest_content = summarize_daily_digest(
        articles=all_articles,
        date=today,
    )

    if not digest_content:
        logger.error("=" * 50)
        logger.error("FAILED TO GENERATE DAILY DIGEST")
        logger.error("The LLM summarization returned empty/None")
        logger.error("Check OPENROUTER_API_KEY and model availability")
        logger.error("=" * 50)
        stats["failed"] = len(all_articles)
        return stats

    logger.info(f"Generated digest content length: {len(digest_content)} chars")

    # 保存
    logger.info(f"Saving daily digest to {DATA_DIR}/items/{today}__daily-digest.md")
    result = save_daily_digest(
        date=today,
        articles=all_articles,
        summary_content=digest_content,
        data_dir=DATA_DIR,
    )

    if result:
        stats["success"] = len(all_articles)
        logger.info("=" * 50)
        logger.info(f"SUCCESS: Saved daily digest for {today}")
        logger.info(f"File: {DATA_DIR}/items/{today}__daily-digest.md")
        logger.info(f"Articles count: {len(all_articles)}")
        logger.info("=" * 50)
    else:
        stats["failed"] = len(all_articles)
        logger.error("=" * 50)
        logger.error("FAILED TO SAVE DAILY DIGEST")
        logger.error("Check file permissions and disk space")
        logger.error("=" * 50)

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Tech Radar Collector - 技術記事を収集・要約する"
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=3,
        help="ソースごとの最大処理件数 (default: 3)",
    )
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=7,
        help="記事の最大日数 - この日数以内の記事のみ取得 (default: 7)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="保存せずに処理をシミュレートする",
    )
    parser.add_argument(
        "--source",
        type=str,
        default=None,
        help="特定のソースのみ処理する",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="詳細なログを出力する",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    logger.info("Starting Tech Radar collection...")
    logger.info(f"Data directory: {DATA_DIR}")
    logger.info(f"Max age: {args.max_age_days} days")

    # データディレクトリの初期化
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "items").mkdir(parents=True, exist_ok=True)

    # 収集実行
    stats = run_collection(
        max_items_per_source=args.max_items,
        max_age_days=args.max_age_days,
        dry_run=args.dry_run,
        source_filter=args.source,
    )

    logger.info("=" * 50)
    logger.info("Collection completed!")
    logger.info(f"Total articles collected: {stats['total']}")
    logger.info(f"Successfully processed: {stats['success']}")
    logger.info(f"Failed: {stats['failed']}")
    logger.info(f"By source: {stats.get('sources', {})}")
    
    # 結果のサマリー
    if stats['total'] == 0:
        logger.warning("NO ARTICLES WERE COLLECTED - check source filters and max_age_days")
    elif stats['success'] == 0 and stats['total'] > 0:
        logger.warning("ARTICLES COLLECTED BUT NOT SAVED - check summarization and storage")
    elif stats['success'] > 0:
        logger.info(f"DIGEST SAVED SUCCESSFULLY with {stats['success']} articles")
    logger.info("=" * 50)


if __name__ == "__main__":
    main()

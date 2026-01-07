#!/usr/bin/env python3
"""
Tech Radar Collector
技術記事を収集し、要約を生成してdata/に保存する
"""

import argparse
import logging
import yaml
from pathlib import Path
from datetime import datetime
from typing import List, Dict

from utils.fetcher import fetch_rss_entries, extract_article_content
from utils.summarizer import summarize_article
from utils.storage import is_url_exists, save_article, load_index, save_index

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


def process_rss_source(source: Dict, max_items: int = 5, dry_run: bool = False) -> int:
    """
    RSSソースを処理する

    Args:
        source: ソース定義
        max_items: 処理する最大件数
        dry_run: Trueの場合は保存しない

    Returns:
        処理した記事数
    """
    name = source.get("name", "unknown")
    url = source.get("url", "")
    tags = source.get("tags", [])

    logger.info(f"Processing RSS source: {name}")

    entries = fetch_rss_entries(url, limit=max_items * 2)  # 重複を考慮して多めに取得

    processed = 0
    for entry in entries:
        if processed >= max_items:
            break

        article_url = entry.get("url", "")
        if not article_url:
            continue

        # 重複チェック
        if is_url_exists(article_url, DATA_DIR):
            logger.debug(f"Skipping existing article: {article_url}")
            continue

        title = entry.get("title", "Untitled")
        logger.info(f"Processing: {title}")

        if dry_run:
            logger.info(f"[DRY RUN] Would process: {title}")
            processed += 1
            continue

        # 本文抽出
        content = extract_article_content(article_url)
        if not content:
            logger.warning(f"Failed to extract content: {article_url}")
            continue

        # 要約生成
        today = datetime.now().strftime("%Y-%m-%d")
        summary = summarize_article(
            title=title,
            url=article_url,
            content=content,
            date=today,
        )

        if not summary:
            logger.warning(f"Failed to summarize: {title}")
            continue

        # 保存
        result = save_article(
            date=today,
            title=title,
            url=article_url,
            tags=tags,
            source=f"rss:{name}",
            summary_content=summary,
            data_dir=DATA_DIR,
        )

        if result:
            processed += 1
            logger.info(f"Saved: {title}")

    return processed


def process_keyword_source(source: Dict, max_items: int = 5, dry_run: bool = False) -> int:
    """
    キーワード検索ソースを処理する（将来の拡張用）

    Args:
        source: ソース定義
        max_items: 処理する最大件数
        dry_run: Trueの場合は保存しない

    Returns:
        処理した記事数
    """
    name = source.get("name", "unknown")
    query = source.get("query", "")

    logger.info(f"Keyword source '{name}' with query '{query}' - not implemented yet")

    # TODO: SerpApi等を使った検索実装
    return 0


def run_collection(
    max_items_per_source: int = 3,
    dry_run: bool = False,
    source_filter: str = None,
) -> Dict:
    """
    メイン収集処理

    Args:
        max_items_per_source: ソースごとの最大処理件数
        dry_run: Trueの場合は保存しない
        source_filter: 特定のソースのみ処理する場合の名前

    Returns:
        処理結果の統計
    """
    sources = load_sources()
    if not sources:
        logger.error("No sources configured")
        return {"total": 0, "success": 0, "failed": 0}

    stats = {"total": 0, "success": 0, "failed": 0, "sources": {}}

    for source in sources:
        source_name = source.get("name", "unknown")
        source_type = source.get("type", "")

        # フィルタリング
        if source_filter and source_name != source_filter:
            continue

        try:
            if source_type == "rss":
                count = process_rss_source(source, max_items_per_source, dry_run)
            elif source_type == "keyword":
                count = process_keyword_source(source, max_items_per_source, dry_run)
            else:
                logger.warning(f"Unknown source type: {source_type}")
                continue

            stats["sources"][source_name] = count
            stats["success"] += count
            stats["total"] += count

        except Exception as e:
            logger.error(f"Error processing source {source_name}: {e}")
            stats["failed"] += 1

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

    # データディレクトリの初期化
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "items").mkdir(parents=True, exist_ok=True)

    # 収集実行
    stats = run_collection(
        max_items_per_source=args.max_items,
        dry_run=args.dry_run,
        source_filter=args.source,
    )

    logger.info("=" * 50)
    logger.info("Collection completed!")
    logger.info(f"Total articles processed: {stats['success']}")
    logger.info(f"Failed: {stats['failed']}")
    logger.info(f"By source: {stats['sources']}")


if __name__ == "__main__":
    main()

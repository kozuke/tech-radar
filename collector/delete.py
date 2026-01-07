#!/usr/bin/env python3
"""
Tech Radar Article Deleter
古い記事や特定条件に合致する記事を削除する
"""

import argparse
import logging
import re
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional

from utils.storage import load_index, save_index

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# パス設定
COLLECTOR_DIR = Path(__file__).parent
DATA_DIR = COLLECTOR_DIR.parent / "data"
ITEMS_DIR = DATA_DIR / "items"


def delete_article_files(item_id: str) -> bool:
    """
    記事ファイル（.md と .meta.json）を削除する

    Args:
        item_id: 記事ID

    Returns:
        削除成功したかどうか
    """
    md_path = ITEMS_DIR / f"{item_id}.md"
    meta_path = ITEMS_DIR / f"{item_id}.meta.json"

    deleted = False

    if md_path.exists():
        try:
            md_path.unlink()
            logger.info(f"Deleted: {md_path.name}")
            deleted = True
        except Exception as e:
            logger.error(f"Failed to delete {md_path.name}: {e}")

    if meta_path.exists():
        try:
            meta_path.unlink()
            logger.info(f"Deleted: {meta_path.name}")
            deleted = True
        except Exception as e:
            logger.error(f"Failed to delete {meta_path.name}: {e}")

    return deleted


def find_articles_by_age(days: int) -> List[Dict]:
    """
    指定日数より古い記事を検索する

    Args:
        days: 何日前より古い記事を対象にするか

    Returns:
        対象記事のリスト
    """
    index = load_index(DATA_DIR)
    cutoff_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

    old_articles = []
    for item in index.get("items", []):
        item_date = item.get("date", "")
        if item_date and item_date < cutoff_date:
            old_articles.append(item)

    return old_articles


def find_articles_by_pattern(pattern: str, search_fields: List[str] = None) -> List[Dict]:
    """
    正規表現パターンに合致する記事を検索する

    Args:
        pattern: 検索パターン（正規表現）
        search_fields: 検索対象フィールド（デフォルト: title, url, tags, source）

    Returns:
        対象記事のリスト
    """
    if search_fields is None:
        search_fields = ["title", "url", "tags", "source", "id"]

    index = load_index(DATA_DIR)
    regex = re.compile(pattern, re.IGNORECASE)

    matched_articles = []
    for item in index.get("items", []):
        for field in search_fields:
            value = item.get(field, "")
            # tagsはリストなので結合
            if isinstance(value, list):
                value = " ".join(value)
            if regex.search(str(value)):
                matched_articles.append(item)
                break  # 1つでもマッチしたら追加して次へ

    return matched_articles


def find_articles_by_id(article_id: str) -> List[Dict]:
    """
    IDで記事を検索する（部分一致）

    Args:
        article_id: 記事ID（部分一致）

    Returns:
        対象記事のリスト
    """
    index = load_index(DATA_DIR)

    matched_articles = []
    for item in index.get("items", []):
        if article_id in item.get("id", ""):
            matched_articles.append(item)

    return matched_articles


def delete_articles(
    articles: List[Dict],
    dry_run: bool = False,
) -> Dict:
    """
    記事を削除する

    Args:
        articles: 削除対象の記事リスト
        dry_run: Trueの場合は実際に削除しない

    Returns:
        削除結果の統計
    """
    stats = {"total": len(articles), "deleted": 0, "failed": 0}

    if not articles:
        logger.info("No articles to delete")
        return stats

    # インデックスを読み込み
    index = load_index(DATA_DIR)
    items = index.get("items", [])
    article_ids = {a["id"] for a in articles}

    for article in articles:
        item_id = article.get("id", "")
        title = article.get("title", "Untitled")
        date = article.get("date", "")

        if dry_run:
            logger.info(f"[DRY RUN] Would delete: [{date}] {title} ({item_id})")
            stats["deleted"] += 1
            continue

        # ファイル削除
        if delete_article_files(item_id):
            stats["deleted"] += 1
            logger.info(f"Deleted: [{date}] {title}")
        else:
            stats["failed"] += 1
            logger.warning(f"Failed to delete files for: {title}")

    # インデックスから削除（dry_runでない場合）
    if not dry_run and stats["deleted"] > 0:
        new_items = [item for item in items if item["id"] not in article_ids]
        index["items"] = new_items
        save_index(index, DATA_DIR)
        logger.info(f"Updated index.json: {len(items)} -> {len(new_items)} items")

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Tech Radar Article Deleter - 記事を削除する"
    )
    parser.add_argument(
        "--older-than",
        type=int,
        default=None,
        help="指定日数より古い記事を削除する",
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default=None,
        help="正規表現パターンに合致する記事を削除する（タイトル、URL、タグ、ソースを検索）",
    )
    parser.add_argument(
        "--id",
        type=str,
        default=None,
        help="記事IDに部分一致する記事を削除する",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="削除せずにシミュレートする",
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

    # 少なくとも1つのフィルタ条件が必要
    if not any([args.older_than, args.pattern, args.id]):
        parser.error("At least one of --older-than, --pattern, or --id is required")

    logger.info("Starting Tech Radar article deletion...")

    # 削除対象の記事を収集
    articles_to_delete = []

    if args.older_than is not None:
        articles = find_articles_by_age(args.older_than)
        logger.info(f"Found {len(articles)} articles older than {args.older_than} days")
        articles_to_delete.extend(articles)

    if args.pattern:
        articles = find_articles_by_pattern(args.pattern)
        logger.info(f"Found {len(articles)} articles matching pattern: {args.pattern}")
        articles_to_delete.extend(articles)

    if args.id:
        articles = find_articles_by_id(args.id)
        logger.info(f"Found {len(articles)} articles matching ID: {args.id}")
        articles_to_delete.extend(articles)

    # 重複を除去
    seen_ids = set()
    unique_articles = []
    for article in articles_to_delete:
        if article["id"] not in seen_ids:
            seen_ids.add(article["id"])
            unique_articles.append(article)

    logger.info(f"Total unique articles to delete: {len(unique_articles)}")

    # 削除実行
    stats = delete_articles(unique_articles, dry_run=args.dry_run)

    logger.info("=" * 50)
    logger.info("Deletion completed!")
    logger.info(f"Total targeted: {stats['total']}")
    logger.info(f"Deleted: {stats['deleted']}")
    logger.info(f"Failed: {stats['failed']}")


if __name__ == "__main__":
    main()

"""
データ保存ユーティリティ
- index.json の読み書き
- 記事ファイルの保存
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# デフォルトのデータディレクトリ
DEFAULT_DATA_DIR = Path(__file__).parent.parent.parent / "data"


def generate_slug(title: str) -> str:
    """
    タイトルからスラッグを生成する

    Args:
        title: 記事タイトル

    Returns:
        URL-safeなスラッグ
    """
    # 英数字とハイフン以外を削除
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    # 空白をハイフンに
    slug = re.sub(r"[\s_]+", "-", slug)
    # 連続するハイフンを1つに
    slug = re.sub(r"-+", "-", slug)
    # 前後のハイフンを削除
    slug = slug.strip("-")
    # 最大50文字
    return slug[:50] if slug else "untitled"


def load_index(data_dir: Optional[Path] = None) -> Dict:
    """
    index.jsonを読み込む

    Args:
        data_dir: データディレクトリ

    Returns:
        インデックスデータ
    """
    data_dir = data_dir or DEFAULT_DATA_DIR
    index_path = data_dir / "index.json"

    if index_path.exists():
        try:
            with open(index_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse index.json: {e}")
            return {"generated_at": "", "items": []}
    else:
        return {"generated_at": "", "items": []}


def save_index(data: Dict, data_dir: Optional[Path] = None) -> bool:
    """
    index.jsonを保存する

    Args:
        data: インデックスデータ
        data_dir: データディレクトリ

    Returns:
        成功したかどうか
    """
    data_dir = data_dir or DEFAULT_DATA_DIR
    data_dir.mkdir(parents=True, exist_ok=True)
    index_path = data_dir / "index.json"

    try:
        data["generated_at"] = datetime.utcnow().isoformat() + "Z"
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved index.json with {len(data.get('items', []))} items")
        return True
    except Exception as e:
        logger.error(f"Failed to save index.json: {e}")
        return False


def is_url_exists(url: str, data_dir: Optional[Path] = None) -> bool:
    """
    URLが既にインデックスに存在するかチェック

    Args:
        url: チェックするURL
        data_dir: データディレクトリ

    Returns:
        存在するかどうか
    """
    index = load_index(data_dir)
    existing_urls = {item.get("url") for item in index.get("items", [])}
    return url in existing_urls


def save_article(
    date: str,
    title: str,
    url: str,
    tags: List[str],
    source: str,
    summary_content: str,
    data_dir: Optional[Path] = None,
) -> Optional[Dict]:
    """
    記事を保存してインデックスを更新する

    Args:
        date: 記事日付 (YYYY-MM-DD)
        title: 記事タイトル
        url: 記事URL
        tags: タグリスト
        source: ソース名
        summary_content: 要約内容

    Returns:
        作成されたアイテムデータ、または失敗時はNone
    """
    data_dir = data_dir or DEFAULT_DATA_DIR
    items_dir = data_dir / "items"
    items_dir.mkdir(parents=True, exist_ok=True)

    slug = generate_slug(title)
    item_id = f"{date}__{slug}"

    # Markdownファイルを保存
    md_filename = f"{item_id}.md"
    md_path = items_dir / md_filename

    try:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(summary_content)
        logger.info(f"Saved article: {md_filename}")
    except Exception as e:
        logger.error(f"Failed to save article {md_filename}: {e}")
        return None

    # メタデータJSONを保存
    meta = {
        "id": item_id,
        "date": date,
        "title": title,
        "url": url,
        "tags": tags,
        "source": source,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }

    meta_filename = f"{item_id}.meta.json"
    meta_path = items_dir / meta_filename

    try:
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"Failed to save meta {meta_filename}: {e}")

    # インデックスを更新
    index = load_index(data_dir)
    item_entry = {
        "id": item_id,
        "date": date,
        "title": title,
        "url": url,
        "tags": tags,
        "source": source,
        "summary_path": f"data/items/{md_filename}",
    }

    # 既存のアイテムを更新または追加
    items = index.get("items", [])
    existing_ids = {item["id"] for item in items}
    if item_id not in existing_ids:
        items.insert(0, item_entry)  # 新しいものを先頭に
        index["items"] = items
        save_index(index, data_dir)

    return item_entry


def save_daily_digest(
    date: str,
    articles: List[Dict],
    summary_content: str,
    data_dir: Optional[Path] = None,
) -> Optional[Dict]:
    """
    日次ダイジェストを保存してインデックスを更新する

    Args:
        date: 日付 (YYYY-MM-DD)
        articles: 含まれる記事のメタデータリスト
        summary_content: ダイジェスト内容

    Returns:
        作成されたアイテムデータ、または失敗時はNone
    """
    data_dir = data_dir or DEFAULT_DATA_DIR
    items_dir = data_dir / "items"
    items_dir.mkdir(parents=True, exist_ok=True)

    item_id = f"{date}__daily-digest"
    title = f"Tech Radar Daily Digest - {date}"

    # 全記事のタグを集約
    all_tags = set()
    for article in articles:
        all_tags.update(article.get("tags", []))
    tags = sorted(list(all_tags))

    # 全記事のソースを集約
    sources = list(set(article.get("source", "") for article in articles if article.get("source")))

    # 含まれるURLのリスト
    urls = [article.get("url", "") for article in articles if article.get("url")]

    # Markdownファイルを保存
    md_filename = f"{item_id}.md"
    md_path = items_dir / md_filename

    try:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(summary_content)
        logger.info(f"Saved daily digest: {md_filename}")
    except Exception as e:
        logger.error(f"Failed to save daily digest {md_filename}: {e}")
        return None

    # メタデータJSONを保存
    meta = {
        "id": item_id,
        "date": date,
        "title": title,
        "type": "daily_digest",
        "article_count": len(articles),
        "urls": urls,
        "tags": tags,
        "sources": sources,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }

    meta_filename = f"{item_id}.meta.json"
    meta_path = items_dir / meta_filename

    try:
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"Failed to save meta {meta_filename}: {e}")

    # インデックスを更新
    index = load_index(data_dir)
    item_entry = {
        "id": item_id,
        "date": date,
        "title": title,
        "type": "daily_digest",
        "article_count": len(articles),
        "urls": urls,
        "tags": tags,
        "sources": sources,
        "summary_path": f"data/items/{md_filename}",
    }

    # 既存のアイテムを更新または追加
    items = index.get("items", [])
    
    # 同じ日のダイジェストがあれば更新、なければ追加
    existing_idx = None
    for i, item in enumerate(items):
        if item.get("id") == item_id:
            existing_idx = i
            break
    
    if existing_idx is not None:
        items[existing_idx] = item_entry
    else:
        items.insert(0, item_entry)
    
    index["items"] = items
    save_index(index, data_dir)

    return item_entry


def get_existing_urls_for_date(date: str, data_dir: Optional[Path] = None) -> set:
    """
    指定日のダイジェストに含まれている既存URLを取得する
    
    Args:
        date: 日付 (YYYY-MM-DD)
        data_dir: データディレクトリ
        
    Returns:
        既存URLのセット
    """
    data_dir = data_dir or DEFAULT_DATA_DIR
    index = load_index(data_dir)
    
    item_id = f"{date}__daily-digest"
    
    for item in index.get("items", []):
        if item.get("id") == item_id:
            return set(item.get("urls", []))
    
    return set()

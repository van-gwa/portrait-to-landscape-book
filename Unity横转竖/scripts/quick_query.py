#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速查询脚本 - 在命令行中查询预制体信息

使用示例:
  python3 quick_query.py "UI_Chat"           # 查询预制体信息
  python3 quick_query.py --guid "0043689f..."  # 查询使用该GUID的预制体
  python3 quick_query.py --similar "UI_Chat"   # 查询相似预制体
  python3 quick_query.py --sprite-count 100    # 查询精灵数超过100的预制体
"""

import os
import sys
import json
import argparse
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Set

# 设置stdout编码为UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"
INDEX_FILE = os.path.join(VAULT_DIR, "prefab_sprites_index.json")

class QuickQuery:
    def __init__(self):
        self.index = {}
        self.guid_to_prefabs = defaultdict(list)
        self.load_index()

    def load_index(self):
        """加载索引"""
        if not os.path.exists(INDEX_FILE):
            print(f"❌ 索引文件不存在: {INDEX_FILE}")
            return False

        try:
            with open(INDEX_FILE, 'r', encoding='utf-8') as f:
                self.index = json.load(f)

            # 构建GUID反向索引
            for prefab_path, data in self.index.items():
                for guid in data.get('guids', []):
                    self.guid_to_prefabs[guid].append(prefab_path)

            return True
        except Exception as e:
            print(f"❌ 加载失败: {e}")
            return False

    def find_prefab_by_name(self, name: str) -> List[str]:
        """按名称搜索预制体"""
        results = []
        search_lower = name.lower()

        for prefab_path, data in self.index.items():
            if search_lower in data['prefab_name'].lower():
                results.append(prefab_path)

        return results

    def query_prefab(self, prefab_path: str):
        """查询单个预制体"""
        if prefab_path not in self.index:
            # 尝试按名称搜索
            matches = self.find_prefab_by_name(prefab_path)
            if not matches:
                print(f"❌ 未找到预制体: {prefab_path}")
                return
            if len(matches) > 1:
                print(f"⚠️  找到多个匹配:")
                for i, m in enumerate(matches, 1):
                    print(f"   {i}. {self.index[m]['prefab_name']} ({m})")
                return
            prefab_path = matches[0]

        data = self.index[prefab_path]

        print(f"\n📄 {data['prefab_name']}")
        print(f"{'='*60}")
        print(f"路径        : {prefab_path}")
        print(f"精灵数      : {data['sprite_count']}")
        print(f"文件引用    : {data['ref_count']}")
        print(f"GUID数      : {len(data['guids'])}")
        print(f"{'='*60}")

        print(f"\n🎨 使用的GUID (共{len(data['guids'])}个):")
        for i, guid in enumerate(data['guids'], 1):
            usage_count = len(self.guid_to_prefabs[guid])
            print(f"  {i:2d}. {guid} (在{usage_count}个预制体中使用)")

    def query_by_guid(self, guid: str):
        """查询使用特定GUID的预制体"""
        prefabs = self.guid_to_prefabs.get(guid, [])

        if not prefabs:
            print(f"❌ 未找到使用该GUID的预制体: {guid}")
            return

        print(f"\n🔍 使用GUID '{guid}' 的预制体 (共{len(prefabs)}个):")
        print(f"{'='*60}")

        for i, prefab_path in enumerate(sorted(prefabs), 1):
            data = self.index[prefab_path]
            print(f"{i:3d}. {data['prefab_name']:30s} ({prefab_path})")

    def query_similar(self, prefab_name: str, threshold: float = 0.3, limit: int = 10):
        """查询相似预制体"""
        matches = self.find_prefab_by_name(prefab_name)

        if not matches:
            print(f"❌ 未找到预制体: {prefab_name}")
            return

        prefab_path = matches[0]
        data = self.index[prefab_path]
        target_guids = set(data['guids'])

        similarities = []

        for other_path, other_data in self.index.items():
            if other_path == prefab_path:
                continue

            other_guids = set(other_data['guids'])
            intersection = len(target_guids & other_guids)
            union = len(target_guids | other_guids)

            if union > 0:
                similarity = intersection / union
                if similarity >= threshold:
                    similarities.append((other_path, similarity, intersection))

        similarities.sort(key=lambda x: x[1], reverse=True)

        print(f"\n🔎 与 '{data['prefab_name']}' 相似的预制体 (相似度 >= {threshold*100:.0f}%):")
        print(f"{'='*60}")
        print(f"{'相似度':<10} {'共享资源':<10} {'预制体':<50}")
        print(f"{'-'*70}")

        for i, (sim_path, similarity, shared) in enumerate(similarities[:limit], 1):
            sim_data = self.index[sim_path]
            print(f"{similarity*100:6.1f}% {'':4s} {shared:6d} {'':4s} {sim_data['prefab_name']}")

        if len(similarities) > limit:
            print(f"\n... 还有 {len(similarities) - limit} 个相似预制体")

    def query_by_sprite_count(self, min_count: int = 0, max_count: int = None):
        """按精灵数筛选"""
        results = []

        for prefab_path, data in self.index.items():
            count = data['sprite_count']
            if count >= min_count and (max_count is None or count <= max_count):
                results.append((prefab_path, count))

        results.sort(key=lambda x: x[1], reverse=True)

        print(f"\n📊 精灵数 {min_count}" + (f"-{max_count}" if max_count else "+") + f" 的预制体 (共{len(results)}个):")
        print(f"{'='*60}")
        print(f"{'精灵数':<10} {'预制体':<50}")
        print(f"{'-'*60}")

        for prefab_path, count in results[:20]:
            data = self.index[prefab_path]
            print(f"{count:6d} {'':4s} {data['prefab_name']}")

        if len(results) > 20:
            print(f"\n... 还有 {len(results) - 20} 个预制体")


def main():
    parser = argparse.ArgumentParser(
        description="预制体快速查询工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python3 quick_query.py "UI_Chat"                    # 查询预制体
  python3 quick_query.py --guid "0043689f..."         # 查询使用该GUID的预制体
  python3 quick_query.py --similar "UI_Chat"          # 查询相似预制体
  python3 quick_query.py --sprite-count 100           # 查询精灵数超过100的预制体
  python3 quick_query.py --sprite-count 50 --max 100  # 查询精灵数50-100的预制体
        """
    )

    parser.add_argument('prefab', nargs='?', help='预制体名称或路径')
    parser.add_argument('--guid', help='按GUID搜索')
    parser.add_argument('--similar', help='查询相似预制体')
    parser.add_argument('--similarity', type=float, default=0.3, help='相似度阈值 (0-1)')
    parser.add_argument('--sprite-count', type=int, help='查询精灵数超过N的预制体')
    parser.add_argument('--max', type=int, help='精灵数的最大值')
    parser.add_argument('--limit', type=int, default=10, help='查询结果数量限制')

    args = parser.parse_args()

    query = QuickQuery()

    if not query.index:
        return

    if args.guid:
        query.query_by_guid(args.guid)
    elif args.similar:
        query.query_similar(args.similar, threshold=args.similarity, limit=args.limit)
    elif args.sprite_count is not None:
        query.query_by_sprite_count(min_count=args.sprite_count, max_count=args.max)
    elif args.prefab:
        query.query_prefab(args.prefab)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

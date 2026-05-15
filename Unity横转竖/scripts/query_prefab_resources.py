#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
查询预制体资源索引，找到使用相同资源的预制体
"""

import os
import sys
import json
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Set

# 设置stdout编码为UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"
INDEX_FILE = os.path.join(VAULT_DIR, "prefab_sprites_index.json")

class PrefabResourceQuery:
    def __init__(self):
        self.index = {}
        self.guid_to_prefabs = defaultdict(list)  # guid -> [prefab_names]
        self.load_index()

    def load_index(self):
        """加载索引文件"""
        if not os.path.exists(INDEX_FILE):
            print(f"❌ 索引文件不存在: {INDEX_FILE}")
            return False

        try:
            with open(INDEX_FILE, 'r', encoding='utf-8') as f:
                self.index = json.load(f)
            print(f"✅ 加载索引成功，共 {len(self.index)} 个预制体")

            # 构建 GUID 到预制体的映射
            for prefab_path, data in self.index.items():
                for guid in data.get('guids', []):
                    self.guid_to_prefabs[guid].append(prefab_path)

            print(f"✅ 构建GUID索引完成，共 {len(self.guid_to_prefabs)} 个唯一GUID")
            return True
        except Exception as e:
            print(f"❌ 加载索引失败: {e}")
            return False

    def find_prefabs_by_guid(self, guid: str) -> List[str]:
        """查找使用特定GUID的所有预制体"""
        return self.guid_to_prefabs.get(guid, [])

    def find_similar_prefabs(self, prefab_path: str, min_shared_guids: int = 1) -> Dict[str, int]:
        """找到与指定预制体使用相同资源的其他预制体

        返回: {prefab_path: 共享GUID数}
        """
        if prefab_path not in self.index:
            print(f"❌ 预制体不在索引中: {prefab_path}")
            return {}

        prefab_guids = set(self.index[prefab_path]['guids'])
        similar = {}

        for other_prefab, data in self.index.items():
            if other_prefab == prefab_path:
                continue

            other_guids = set(data['guids'])
            shared = len(prefab_guids & other_guids)

            if shared >= min_shared_guids:
                similar[other_prefab] = shared

        # 按共享GUID数排序
        return dict(sorted(similar.items(), key=lambda x: x[1], reverse=True))

    def find_prefabs_by_sprite_count(self, min_count: int = 0, max_count: int = None) -> List[tuple]:
        """按精灵数量筛选预制体

        返回: [(prefab_path, sprite_count)]
        """
        results = []
        for prefab_path, data in self.index.items():
            count = data['sprite_count']
            if count >= min_count and (max_count is None or count <= max_count):
                results.append((prefab_path, count))

        return sorted(results, key=lambda x: x[1], reverse=True)

    def list_all_prefabs(self) -> List[str]:
        """列出所有预制体"""
        return sorted(self.index.keys())

    def print_prefab_info(self, prefab_path: str):
        """打印预制体详细信息"""
        if prefab_path not in self.index:
            print(f"❌ 预制体不在索引中: {prefab_path}")
            return

        data = self.index[prefab_path]
        print(f"\n📄 {data['prefab_name']}")
        print(f"路径: {prefab_path}")
        print(f"精灵数: {data['sprite_count']}")
        print(f"总引用数: {data['ref_count']}")
        print(f"GUID列表: {', '.join(data['guids'][:5])}", end="")
        if len(data['guids']) > 5:
            print(f" ... ({len(data['guids']) - 5} more)")
        else:
            print()

    def export_similarity_report(self, output_file: str = None):
        """导出相似性分析报告"""
        if output_file is None:
            output_file = os.path.join(VAULT_DIR, "prefab_similarity_report.md")

        report = "# 预制体资源相似性分析报告\n\n"
        report += f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        report += f"总预制体数: {len(self.index)}\n\n"

        # 按精灵数分类
        report += "## 按精灵数分类\n\n"
        prefabs_by_count = defaultdict(list)
        for prefab_path, data in self.index.items():
            count = data['sprite_count']
            prefabs_by_count[count].append(prefab_path)

        for count in sorted(prefabs_by_count.keys(), reverse=True):
            prefabs = prefabs_by_count[count]
            report += f"### {count} 个精灵 ({len(prefabs)} 个预制体)\n\n"
            for p in prefabs[:10]:
                report += f"- {p}\n"
            if len(prefabs) > 10:
                report += f"- ... 还有 {len(prefabs) - 10} 个\n"
            report += "\n"

        # 导出到文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"✅ 报告已保存: {output_file}")


def main():
    query = PrefabResourceQuery()

    if not query.index:
        print("无法继续，请先运行 extract_prefab_sprites.py")
        return

    # 示例操作
    print("\n" + "="*60)
    print("📊 预制体资源查询工具")
    print("="*60)

    # 统计
    print("\n📈 基本统计:")
    print(f"   总预制体数: {len(query.index)}")
    print(f"   唯一GUID数: {len(query.guid_to_prefabs)}")

    # 精灵数TOP 10
    print("\n🏆 精灵数TOP 10:")
    top_10 = query.find_prefabs_by_sprite_count()[:10]
    for prefab_path, count in top_10:
        name = query.index[prefab_path]['prefab_name']
        print(f"   {count:3d} - {name}")

    # 导出报告
    query.export_similarity_report()


if __name__ == "__main__":
    main()

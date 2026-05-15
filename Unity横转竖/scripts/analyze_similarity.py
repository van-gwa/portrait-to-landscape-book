#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高级分析：找出结构相近的界面
基于共享资源（GUID）的相似度算法
"""

import os
import sys
import json
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Set
from pathlib import Path

# 设置stdout编码为UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"
INDEX_FILE = os.path.join(VAULT_DIR, "prefab_sprites_index.json")
OUTPUT_DIR = os.path.join(VAULT_DIR, "similarity_analysis")
os.makedirs(OUTPUT_DIR, exist_ok=True)

class SimilarityAnalyzer:
    def __init__(self):
        self.index = {}
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
            return True
        except Exception as e:
            print(f"❌ 加载索引失败: {e}")
            return False

    def calculate_similarity(self, guids1: Set[str], guids2: Set[str]) -> float:
        """
        计算两个GUID集合的相似度（Jaccard相似度）
        范围: 0-1，1表示完全相同
        """
        if not guids1 and not guids2:
            return 1.0
        if not guids1 or not guids2:
            return 0.0

        intersection = len(guids1 & guids2)
        union = len(guids1 | guids2)

        if union == 0:
            return 0.0

        return intersection / union

    def find_similar_prefabs(self, prefab_path: str, threshold: float = 0.3, limit: int = 20) -> List[Tuple[str, float, int]]:
        """
        找出与指定预制体相似的其他预制体

        参数:
            prefab_path: 目标预制体路径
            threshold: 相似度阈值 (0-1)
            limit: 返回结果的最大数量

        返回:
            [(prefab_path, similarity, shared_guids_count)]
        """
        if prefab_path not in self.index:
            print(f"❌ 预制体不在索引中: {prefab_path}")
            return []

        target_guids = set(self.index[prefab_path]['guids'])
        similarities = []

        for other_path, other_data in self.index.items():
            if other_path == prefab_path:
                continue

            other_guids = set(other_data['guids'])
            similarity = self.calculate_similarity(target_guids, other_guids)

            if similarity >= threshold:
                shared_count = len(target_guids & other_guids)
                similarities.append((other_path, similarity, shared_count))

        # 按相似度排序
        similarities.sort(key=lambda x: x[1], reverse=True)

        return similarities[:limit]

    def cluster_by_similarity(self, threshold: float = 0.5) -> Dict[str, List[str]]:
        """
        将预制体聚类，相似度高的分为一组

        返回: {cluster_id: [prefab_paths]}
        """
        processed = set()
        clusters = {}
        cluster_id = 0

        prefab_paths = list(self.index.keys())

        for i, prefab1 in enumerate(prefab_paths):
            if prefab1 in processed:
                continue

            cluster = [prefab1]
            processed.add(prefab1)

            guids1 = set(self.index[prefab1]['guids'])

            for prefab2 in prefab_paths[i+1:]:
                if prefab2 in processed:
                    continue

                guids2 = set(self.index[prefab2]['guids'])
                similarity = self.calculate_similarity(guids1, guids2)

                if similarity >= threshold:
                    cluster.append(prefab2)
                    processed.add(prefab2)

            if len(cluster) > 1:  # 只保存有多个成员的集群
                clusters[f"cluster_{cluster_id}"] = cluster
                cluster_id += 1

        return clusters

    def analyze_resource_usage(self) -> Dict:
        """分析资源的使用情况"""
        guid_usage = defaultdict(list)

        for prefab_path, data in self.index.items():
            for guid in data['guids']:
                guid_usage[guid].append(prefab_path)

        # 按使用频率排序
        sorted_usage = sorted(
            guid_usage.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )

        return dict(sorted_usage)

    def generate_similarity_report(self, prefab_path: str, top_n: int = 20) -> str:
        """生成某个预制体的相似性报告"""
        if prefab_path not in self.index:
            return f"❌ 预制体不存在: {prefab_path}"

        prefab_name = self.index[prefab_path]['prefab_name']
        target_guids = set(self.index[prefab_path]['guids'])

        report = f"# {prefab_name} - 相似性分析报告\n\n"
        report += f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        report += f"## 基本信息\n\n"
        report += f"| 属性 | 值 |\n"
        report += f"|------|----|\n"
        report += f"| 预制体 | `{prefab_path}` |\n"
        report += f"| 精灵数 | {self.index[prefab_path]['sprite_count']} |\n"
        report += f"| GUID数 | {len(target_guids)} |\n"

        # 找相似预制体
        similar = self.find_similar_prefabs(prefab_path, threshold=0.2, limit=top_n)

        report += f"\n## 相似的界面 (TOP {len(similar)})\n\n"

        if similar:
            report += "| 相似度 | 共享资源 | 预制体 |\n"
            report += "|--------|---------|--------|\n"
            for sim_path, similarity, shared_count in similar:
                sim_name = self.index[sim_path]['prefab_name']
                report += f"| {similarity*100:.1f}% | {shared_count} | `{sim_path}` |\n"
        else:
            report += "\n*无相似的预制体*\n"

        # 资源信息
        report += f"\n## 使用的资源 (GUID)\n\n"
        for guid in sorted(target_guids):
            usage_count = len([p for p in self.index if guid in self.index[p]['guids']])
            report += f"- `{guid}` (在{usage_count}个预制体中使用)\n"

        return report

    def generate_global_analysis(self) -> str:
        """生成全局分析报告"""
        report = "# 全局相似性分析\n\n"
        report += f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        # 资源使用统计
        guid_usage = self.analyze_resource_usage()

        report += f"## 资源使用统计\n\n"
        report += f"- 总GUID数: {len(guid_usage)}\n"
        report += f"- 总预制体数: {len(self.index)}\n"
        report += f"- 平均每个预制体使用的资源: {sum(len(self.index[p]['guids']) for p in self.index) / len(self.index):.1f}\n\n"

        report += f"### 最常用的资源 (TOP 20)\n\n"
        report += "| GUID | 使用次数 | 预制体示例 |\n"
        report += "|------|---------|----------|\n"

        for guid, prefabs in list(guid_usage.items())[:20]:
            example_prefabs = ", ".join([self.index[p]['prefab_name'] for p in prefabs[:3]])
            report += f"| `{guid}` | {len(prefabs)} | {example_prefabs}{'...' if len(prefabs) > 3 else ''} |\n"

        # 预制体复杂度分布
        report += f"\n## 预制体复杂度分布\n\n"

        complexity_bins = defaultdict(list)
        for prefab_path, data in self.index.items():
            sprite_count = data['sprite_count']
            if sprite_count < 50:
                bin_key = "简单 (<50)"
            elif sprite_count < 100:
                bin_key = "中等 (50-100)"
            elif sprite_count < 150:
                bin_key = "复杂 (100-150)"
            else:
                bin_key = "超复杂 (>150)"
            complexity_bins[bin_key].append(prefab_path)

        for bin_key in ["简单 (<50)", "中等 (50-100)", "复杂 (100-150)", "超复杂 (>150)"]:
            if bin_key in complexity_bins:
                count = len(complexity_bins[bin_key])
                percentage = count / len(self.index) * 100
                report += f"- **{bin_key}**: {count} 个 ({percentage:.1f}%)\n"

        # 使用最多的预制体
        report += f"\n## 精灵数 TOP 20\n\n"
        sorted_prefabs = sorted(
            self.index.items(),
            key=lambda x: x[1]['sprite_count'],
            reverse=True
        )

        report += "| 排名 | 预制体 | 精灵数 | GUID数 |\n"
        report += "|------|--------|--------|--------|\n"

        for i, (path, data) in enumerate(sorted_prefabs[:20], 1):
            report += f"| {i} | {data['prefab_name']} | {data['sprite_count']} | {len(data['guids'])} |\n"

        return report

    def export_analysis(self, prefab_path: str = None):
        """导出分析结果"""
        if prefab_path and prefab_path in self.index:
            # 单个预制体分析
            report = self.generate_similarity_report(prefab_path)
            prefab_name = self.index[prefab_path]['prefab_name']
            output_file = os.path.join(OUTPUT_DIR, f"{prefab_name}_similarity.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"✅ 报告已保存: {output_file}")
        else:
            # 全局分析
            report = self.generate_global_analysis()
            output_file = os.path.join(OUTPUT_DIR, "global_similarity_analysis.md")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"✅ 全局分析报告已保存: {output_file}")


def main():
    analyzer = SimilarityAnalyzer()

    if not analyzer.index:
        print("无法继续，请先运行 extract_prefab_sprites.py")
        return

    print("\n" + "="*60)
    print("🔍 预制体相似性分析工具")
    print("="*60)

    # 生成全局分析
    print("\n📊 生成全局分析报告...")
    analyzer.export_analysis()

    # 示例：分析几个TOP预制体
    print("\n📈 分析TOP预制体...")
    top_prefabs = sorted(
        analyzer.index.items(),
        key=lambda x: x[1]['sprite_count'],
        reverse=True
    )[:5]

    for prefab_path, data in top_prefabs:
        print(f"\n🔎 分析: {data['prefab_name']}")
        analyzer.export_analysis(prefab_path)

    print("\n" + "="*60)
    print("✅ 分析完成！结果保存在 similarity_analysis/ 目录")
    print("="*60)


if __name__ == "__main__":
    main()

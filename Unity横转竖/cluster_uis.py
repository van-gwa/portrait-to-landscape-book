#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import math
from collections import defaultdict

def load_features(json_file):
    """加载特征数据"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['all_uis']

def calculate_similarity(ui1, ui2):
    """计算两个UI的相似度 (0~1, 越接近1越相似)"""
    # 多维度相似度计算

    # 1. 尺寸相似度 (宽高)
    width_diff = abs(ui1['width'] - ui2['width'])
    height_diff = abs(ui1['height'] - ui2['height'])
    size_sim = max(0, 1 - (width_diff + height_diff) / 3000)  # 分母可调

    # 2. 节点数相似度
    node_diff = abs(ui1['total_nodes'] - ui2['total_nodes'])
    node_sim = max(0, 1 - node_diff / 100)

    # 3. X轴分布相似度
    x_dist_sim = 1.0 if ui1['x_distribution'] == ui2['x_distribution'] else 0.3

    # 4. 特征标志相似度
    feature_match = sum(1 for f in ['has_list', 'has_image_bg', 'has_spine']
                       if ui1[f] == ui2[f])
    feature_sim = feature_match / 3

    # 5. 宽高比相似度
    aspect_diff = abs(ui1['aspect_ratio'] - ui2['aspect_ratio'])
    aspect_sim = max(0, 1 - aspect_diff)

    # 综合相似度 (加权平均)
    similarity = (
        size_sim * 0.3 +
        node_sim * 0.2 +
        x_dist_sim * 0.25 +
        feature_sim * 0.15 +
        aspect_sim * 0.1
    )

    return similarity

def cluster_uis(uis, similarity_threshold=0.65):
    """将UI按相似度聚类"""
    clusters = []
    used = set()

    for i, ui1 in enumerate(uis):
        if i in used:
            continue

        cluster = [ui1]
        used.add(i)

        # 找所有与ui1相似的UI
        for j, ui2 in enumerate(uis):
            if j <= i or j in used:
                continue

            sim = calculate_similarity(ui1, ui2)
            if sim >= similarity_threshold:
                cluster.append(ui2)
                used.add(j)

        clusters.append(cluster)

    return clusters

def characterize_cluster(cluster):
    """为集群生成特征描述"""
    if not cluster:
        return None

    # 统计集群内的特征
    widths = [ui['width'] for ui in cluster]
    heights = [ui['height'] for ui in cluster]
    node_counts = [ui['total_nodes'] for ui in cluster]

    avg_width = sum(widths) / len(widths)
    avg_height = sum(heights) / len(heights)
    avg_nodes = sum(node_counts) / len(node_counts)

    x_dists = defaultdict(int)
    for ui in cluster:
        x_dists[ui['x_distribution']] += 1

    dominant_x_dist = max(x_dists.items(), key=lambda x: x[1])[0]

    has_list_count = sum(1 for ui in cluster if ui['has_list'])
    has_image_bg_count = sum(1 for ui in cluster if ui['has_image_bg'])
    has_spine_count = sum(1 for ui in cluster if ui['has_spine'])

    description = {
        'size': len(cluster),
        'avg_width': round(avg_width, 1),
        'avg_height': round(avg_height, 1),
        'width_range': (round(min(widths), 1), round(max(widths), 1)),
        'height_range': (round(min(heights), 1), round(max(heights), 1)),
        'avg_nodes': round(avg_nodes, 1),
        'node_range': (min(node_counts), max(node_counts)),
        'dominant_x_distribution': dominant_x_dist,
        'x_distribution_breakdown': dict(x_dists),
        'has_list_count': has_list_count,
        'has_image_bg_count': has_image_bg_count,
        'has_spine_count': has_spine_count,
        'ui_names': [ui['ui_name'] for ui in cluster[:5]]  # 前5个示例
    }

    return description

if __name__ == '__main__':
    print("[*] Loading feature data...")
    uis = load_features(r'D:\obsidianProject\portrait-to-landscape\Unity横转竖\all_ui_features.json')

    print(f"[+] Loaded {len(uis)} UIs")

    print("[*] Clustering UIs by similarity (threshold=0.65)...")
    clusters = cluster_uis(uis, similarity_threshold=0.65)

    print(f"[+] Found {len(clusters)} clusters")

    # 按集群大小排序
    clusters.sort(key=len, reverse=True)

    # 生成报告
    report = {
        'total_uis': len(uis),
        'total_clusters': len(clusters),
        'clusters': []
    }

    print("\n" + "="*80)
    print("CLUSTERING RESULTS (by cluster size)")
    print("="*80)

    for idx, cluster in enumerate(clusters, 1):
        chars = characterize_cluster(cluster)
        report['clusters'].append({
            'cluster_id': idx,
            'characteristics': chars
        })

        print(f"\nCluster {idx} (Size: {len(cluster)})")
        print(f"  Avg Size: {chars['avg_width']:.0f} x {chars['avg_height']:.0f} px")
        print(f"  Size Range: {chars['width_range'][0]:.0f}~{chars['width_range'][1]:.0f} x {chars['height_range'][0]:.0f}~{chars['height_range'][1]:.0f}")
        print(f"  Avg Nodes: {chars['avg_nodes']:.0f} ({chars['node_range'][0]}-{chars['node_range'][1]})")
        print(f"  X Distribution: {chars['dominant_x_distribution']}")
        print(f"  Features: List={chars['has_list_count']}, BG={chars['has_image_bg_count']}, Spine={chars['has_spine_count']}")
        print(f"  Sample UIs: {', '.join(chars['ui_names'])}")

    # 保存详细报告
    output_file = r'D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_clustering_report.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n[+] Detailed report saved to {output_file}")

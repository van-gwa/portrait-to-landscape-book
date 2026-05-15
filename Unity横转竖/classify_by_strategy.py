#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from collections import defaultdict

def load_features(json_file):
    """加载特征数据"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['all_uis']

def classify_by_strategy(uis):
    """按处理策略重新分类UI"""

    type_a = []  # 可拆分的宽UI
    type_b = []  # 紧凑小型UI
    type_c = []  # 无列表的宽展示UI
    type_d = []  # 特殊场景 (不处理)
    others = []  # 其他

    for ui in uis:
        w = ui['width']
        h = ui['height']
        nodes = ui['total_nodes']
        has_list = ui['has_list']
        x_dist = ui['x_distribution']

        # Type D: 特殊场景 (宽度 > 1500 或异常)
        if w > 1500:
            type_d.append(ui)
            continue

        # Type B: 紧凑小型
        if w < 600 and nodes < 30:
            type_b.append(ui)
            continue

        # Type A: 可拆分的宽UI
        if 600 <= w <= 1200 and has_list and x_dist == 'left-center-right':
            type_a.append(ui)
            continue

        # Type C: 无列表的宽展示UI
        if 500 <= w <= 1200 and not has_list and x_dist in ['left-center-right', 'center-right']:
            type_c.append(ui)
            continue

        # 其他
        others.append(ui)

    return {
        'type_a': type_a,
        'type_b': type_b,
        'type_c': type_c,
        'type_d': type_d,
        'others': others
    }

def analyze_type(uis, type_name):
    """分析某类型的详细特征"""

    if not uis:
        return None

    widths = [u['width'] for u in uis]
    heights = [u['height'] for u in uis]
    nodes_list = [u['total_nodes'] for u in uis]
    has_list_count = sum(1 for u in uis if u['has_list'])
    has_image_bg_count = sum(1 for u in uis if u['has_image_bg'])
    has_spine_count = sum(1 for u in uis if u['has_spine'])

    # X轴分布统计
    x_dist_breakdown = defaultdict(int)
    for u in uis:
        x_dist_breakdown[u['x_distribution']] += 1

    analysis = {
        'type': type_name,
        'count': len(uis),
        'percentage': round(100 * len(uis) / 1401, 1),
        'size': {
            'width': {
                'min': round(min(widths), 1),
                'max': round(max(widths), 1),
                'avg': round(sum(widths) / len(widths), 1)
            },
            'height': {
                'min': round(min(heights), 1),
                'max': round(max(heights), 1),
                'avg': round(sum(heights) / len(heights), 1)
            }
        },
        'nodes': {
            'min': min(nodes_list),
            'max': max(nodes_list),
            'avg': round(sum(nodes_list) / len(nodes_list), 1)
        },
        'features': {
            'has_list': has_list_count,
            'has_image_bg': has_image_bg_count,
            'has_spine': has_spine_count
        },
        'x_distribution': dict(x_dist_breakdown),
        'sample_uis': [u['ui_name'] for u in uis[:10]]
    }

    return analysis

if __name__ == '__main__':
    print("[*] Loading features...")
    uis = load_features(r'D:\obsidianProject\portrait-to-landscape\Unity横转竖\all_ui_features.json')

    print("[*] Classifying by strategy...")
    classified = classify_by_strategy(uis)

    report = {
        'total_uis': len(uis),
        'classification': {}
    }

    print("\n" + "="*80)
    print("CLASSIFICATION BY STRATEGY")
    print("="*80)

    for type_key in ['type_a', 'type_b', 'type_c', 'type_d', 'others']:
        type_uis = classified[type_key]
        analysis = analyze_type(type_uis, type_key.upper())

        if analysis:
            report['classification'][type_key] = analysis

            print(f"\n{type_key.upper()} - {analysis['type']} ({analysis['count']} UIs, {analysis['percentage']}%)")
            print(f"  Size: {analysis['size']['width']['avg']:.0f} x {analysis['size']['height']['avg']:.0f} px")
            print(f"         (W: {analysis['size']['width']['min']:.0f}~{analysis['size']['width']['max']:.0f}, "
                  f"H: {analysis['size']['height']['min']:.0f}~{analysis['size']['height']['max']:.0f})")
            print(f"  Nodes: {analysis['nodes']['avg']:.0f} ({analysis['nodes']['min']}-{analysis['nodes']['max']})")
            print(f"  Features: List={analysis['features']['has_list']}, BG={analysis['features']['has_image_bg']}, Spine={analysis['features']['has_spine']}")
            print(f"  X Distribution: {analysis['x_distribution']}")
            print(f"  Sample: {', '.join(analysis['sample_uis'][:5])}")

    # 保存报告
    output_file = r'D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_classification_by_strategy.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n[+] Strategy classification saved to {output_file}")

    # 汇总表
    print("\n" + "="*80)
    print("SUMMARY TABLE")
    print("="*80)

    for type_key in ['type_a', 'type_b', 'type_c', 'type_d', 'others']:
        analysis = report['classification'].get(type_key)
        if analysis:
            print(f"{type_key:<15} {analysis['count']:>4} ({analysis['percentage']:>5.1f}%) "
                  f"Avg:{analysis['size']['width']['avg']:>6.0f}x{analysis['size']['height']['avg']:<6.0f} "
                  f"Nodes:{analysis['nodes']['avg']:>5.0f}")

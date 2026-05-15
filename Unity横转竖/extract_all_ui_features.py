#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import json
from pathlib import Path
from collections import defaultdict

class UIFeatureExtractor:
    """从全部prefab提取布局特征，用于后续聚类"""

    def __init__(self, prefabs_root):
        self.prefabs_root = prefabs_root
        self.all_features = []

    def extract_nodes(self, prefab_path):
        """从prefab提取节点位置信息"""
        try:
            with open(prefab_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            return None

        nodes = {}
        gos = {}

        # 提取GameObject
        go_pattern = r'--- !u!1 &(\d+)\nGameObject:(.*?)(?=--- !u!|\Z)'
        for match in re.finditer(go_pattern, content, re.DOTALL):
            obj_id = match.group(1)
            obj_block = match.group(2)
            name_match = re.search(r'm_Name:\s*(.+?)(?=\n|$)', obj_block)
            if name_match:
                name = name_match.group(1).strip()
                if name and not name.startswith('!u!'):
                    gos[obj_id] = name

        # 提取RectTransform
        rt_pattern = r'--- !u!224 &(\d+)\nRectTransform:(.*?)(?=--- !u!|\Z)'
        for match in re.finditer(rt_pattern, content, re.DOTALL):
            rt_id = match.group(1)
            rt_block = match.group(2)

            go_match = re.search(r'm_GameObject:\s*\{fileID:\s*(\d+)', rt_block)
            if go_match:
                go_id = go_match.group(1)
                if go_id not in gos:
                    continue

                name = gos[go_id]

                pos_match = re.search(r'm_AnchoredPosition:\s*\{x:\s*([-\d.]+),\s*y:\s*([-\d.]+)\}', rt_block)
                size_match = re.search(r'm_SizeDelta:\s*\{x:\s*([-\d.]+),\s*y:\s*([-\d.]+)\}', rt_block)

                if pos_match and size_match:
                    try:
                        pos_x = float(pos_match.group(1))
                        pos_y = float(pos_match.group(2))
                        size_x = float(size_match.group(1))
                        size_y = float(size_match.group(2))

                        if size_x > 20 or size_y > 20:
                            nodes[name] = {
                                'pos': (pos_x, pos_y),
                                'size': (size_x, size_y)
                            }
                    except:
                        pass

        return nodes if nodes else None

    def analyze_features(self, nodes, ui_name):
        """分析单个UI的布局特征"""
        if not nodes:
            return None

        try:
            all_x = [n['pos'][0] for n in nodes.values()]
            all_y = [n['pos'][1] for n in nodes.values()]

            if not all_x:
                return None

            min_x, max_x = min(all_x), max(all_x)
            min_y, max_y = min(all_y), max(all_y)
            width = max_x - min_x
            height = max_y - min_y

            # X轴分布
            center_x = sum(all_x) / len(all_x)
            left_threshold = center_x - width * 0.25
            right_threshold = center_x + width * 0.25

            left_nodes = {n: nodes[n] for n in nodes
                         if nodes[n]['pos'][0] < left_threshold}
            center_nodes = {n: nodes[n] for n in nodes
                           if left_threshold <= nodes[n]['pos'][0] <= right_threshold}
            right_nodes = {n: nodes[n] for n in nodes
                          if nodes[n]['pos'][0] > right_threshold}

            # Y轴分布
            center_y = sum(all_y) / len(all_y)
            top_threshold = center_y + height * 0.25
            bottom_threshold = center_y - height * 0.25

            top_nodes = {n: nodes[n] for n in nodes
                        if nodes[n]['pos'][1] > top_threshold}
            middle_nodes = {n: nodes[n] for n in nodes
                           if bottom_threshold <= nodes[n]['pos'][1] <= top_threshold}
            bottom_nodes = {n: nodes[n] for n in nodes
                           if nodes[n]['pos'][1] < bottom_threshold}

            # 节点特征统计
            has_list = any('List' in n or 'Scroll' in n for n in nodes)
            has_image_bg = any(
                'Bg' in n and nodes[n]['size'][0] > 300 and nodes[n]['size'][1] > 150
                for n in nodes
            )
            has_spine = any('Spine' in n or 'Image' in n for n in nodes)

            features = {
                'ui_name': ui_name,
                'total_nodes': len(nodes),
                'width': round(width, 1),
                'height': round(height, 1),
                'aspect_ratio': round(width / height, 2) if height > 0 else 0,

                # X轴分布
                'left_count': len(left_nodes),
                'center_count': len(center_nodes),
                'right_count': len(right_nodes),
                'left_ratio': round(len(left_nodes) / len(nodes), 2),
                'center_ratio': round(len(center_nodes) / len(nodes), 2),
                'right_ratio': round(len(right_nodes) / len(nodes), 2),

                # Y轴分布
                'top_count': len(top_nodes),
                'middle_count': len(middle_nodes),
                'bottom_count': len(bottom_nodes),

                # 特征标志
                'has_list': has_list,
                'has_image_bg': has_image_bg,
                'has_spine': has_spine,

                # X分布特征描述
                'x_distribution': 'left-center-right' if (len(left_nodes) > 0 and len(center_nodes) > 0 and len(right_nodes) > 0) else (
                    'left-center' if (len(left_nodes) > 0 and len(center_nodes) > 0) else (
                    'center-right' if (len(center_nodes) > 0 and len(right_nodes) > 0) else 'center'
                )),

                # Y分布特征描述
                'y_distribution': f"top:{len(top_nodes)} mid:{len(middle_nodes)} bot:{len(bottom_nodes)}"
            }

            return features

        except Exception as e:
            return None

    def scan_all_prefabs(self):
        """扫描所有prefab并提取特征"""
        print("[*] Starting scan of all prefabs...")
        count = 0

        for root, dirs, files in os.walk(self.prefabs_root):
            for file in files:
                if file.endswith('.prefab'):
                    prefab_path = os.path.join(root, file)
                    ui_name = file.replace('.prefab', '')
                    module = os.path.basename(os.path.dirname(prefab_path))

                    nodes = self.extract_nodes(prefab_path)
                    if nodes:
                        features = self.analyze_features(nodes, ui_name)
                        if features:
                            features['module'] = module
                            features['path'] = prefab_path
                            self.all_features.append(features)
                            count += 1

                            if count % 100 == 0:
                                print(f"[+] Processed {count} UIs...")

        print(f"[+] Total {count} UIs processed")
        return self.all_features

    def generate_summary_report(self):
        """生成统计汇总报告"""
        if not self.all_features:
            return None

        # 按宽度分组
        width_groups = defaultdict(list)
        for f in self.all_features:
            w_bucket = int(f['width'] / 50) * 50
            width_groups[w_bucket].append(f)

        # 按X分布特征分组
        x_dist_groups = defaultdict(list)
        for f in self.all_features:
            x_dist_groups[f['x_distribution']].append(f)

        # 按节点数分组
        node_count_groups = defaultdict(list)
        for f in self.all_features:
            bucket = int(f['total_nodes'] / 10) * 10
            node_count_groups[bucket].append(f)

        # 特征统计
        has_list_count = sum(1 for f in self.all_features if f['has_list'])
        has_image_bg_count = sum(1 for f in self.all_features if f['has_image_bg'])
        has_spine_count = sum(1 for f in self.all_features if f['has_spine'])

        summary = {
            'total_uis': len(self.all_features),
            'width_distribution': {str(k): len(v) for k, v in sorted(width_groups.items())},
            'x_distribution_types': {k: len(v) for k, v in x_dist_groups.items()},
            'node_count_distribution': {f"{k}~{k+10}": len(v) for k, v in sorted(node_count_groups.items())},
            'feature_stats': {
                'has_list': has_list_count,
                'has_image_bg': has_image_bg_count,
                'has_spine': has_spine_count,
            },
            'width_range': {
                'min': min(f['width'] for f in self.all_features),
                'max': max(f['width'] for f in self.all_features),
                'avg': round(sum(f['width'] for f in self.all_features) / len(self.all_features), 1)
            },
            'height_range': {
                'min': min(f['height'] for f in self.all_features),
                'max': max(f['height'] for f in self.all_features),
                'avg': round(sum(f['height'] for f in self.all_features) / len(self.all_features), 1)
            }
        }

        return summary

    def save_results(self, output_file):
        """保存全部特征到JSON"""
        data = {
            'summary': self.generate_summary_report(),
            'all_uis': self.all_features
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"[+] Results saved to {output_file}")
        return output_file


if __name__ == '__main__':
    prefabs_root = r"D:\CursorProject\Dadian - 副本\Arts\Assets\ArtResources\UIs\Prefabs"

    extractor = UIFeatureExtractor(prefabs_root)
    features = extractor.scan_all_prefabs()

    output_file = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖\all_ui_features.json"
    extractor.save_results(output_file)

    # 打印摘要
    summary = extractor.generate_summary_report()
    print("\n" + "="*80)
    print("SUMMARY REPORT")
    print("="*80)
    print(f"Total UIs: {summary['total_uis']}")
    print(f"\nWidth distribution:")
    for w_range, count in sorted(summary['width_distribution'].items()):
        print(f"  {w_range}px: {count}")
    print(f"\nX-axis distribution types:")
    for x_type, count in summary['x_distribution_types'].items():
        print(f"  {x_type}: {count}")
    print(f"\nFeature statistics:")
    for feat, count in summary['feature_stats'].items():
        print(f"  {feat}: {count}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取每个界面的背景图（最大的图片）
生成完整的背景图清单
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', write_through=True)

ANALYSIS_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖\prefab_final_analysis"
OUTPUT_FILE = os.path.join(os.path.dirname(ANALYSIS_DIR), "background_image_list.md")

class BackgroundImageExtractor:
    def __init__(self):
        self.data = []

    def parse_markdown(self, filepath):
        """解析Markdown笔记，提取最大的图片"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            prefab_name = os.path.splitext(os.path.basename(filepath))[0]

            # 提取路径信息
            path_match = re.search(r'\*\*路径\*\*: `([^`]+)`', content)
            path_info = path_match.group(1) if path_match else "Unknown"

            # 提取所有Image组件
            images = []

            # 从Image资源详细清单部分提取
            image_section_match = re.search(
                r'## 📋 Image资源详细清单.*?(?=\n---|\n## )',
                content,
                re.DOTALL
            )

            if image_section_match:
                image_section = image_section_match.group(0)
                # 匹配表格行
                lines = image_section.split('\n')
                for line in lines:
                    if '|' in line and '完整路径' not in line and '-----' not in line:
                        parts = [p.strip() for p in line.split('|')]
                        if len(parts) >= 6:  # 确保有足够的列
                            path = parts[1].strip('`')
                            size_str = parts[2]
                            asset_name = parts[3].strip('**').strip()
                            file_id = parts[4].strip('`')
                            guid = parts[5].strip('`')

                            # 解析尺寸
                            size_match = re.match(r'([0-9.]+)×([0-9.]+)', size_str)
                            if size_match:
                                width = float(size_match.group(1))
                                height = float(size_match.group(2))
                                area = width * height

                                images.append({
                                    'type': 'Image',
                                    'path': path,
                                    'width': width,
                                    'height': height,
                                    'area': area,
                                    'size_str': size_str,
                                    'asset_name': asset_name,
                                    'file_id': file_id,
                                    'guid': guid
                                })

            # 从RawImage资源详细清单部分提取
            rawimage_section_match = re.search(
                r'## 📦 RawImage资源详细清单.*?(?=\Z)',
                content,
                re.DOTALL
            )

            if rawimage_section_match:
                rawimage_section = rawimage_section_match.group(0)
                if '无RawImage组件' not in rawimage_section:
                    lines = rawimage_section.split('\n')
                    for line in lines:
                        if '|' in line and '完整路径' not in line and '-----' not in line:
                            parts = [p.strip() for p in line.split('|')]
                            if len(parts) >= 6:
                                path = parts[1].strip('`')
                                size_str = parts[2]
                                asset_name = parts[3].strip('**').strip()
                                file_id = parts[4].strip('`')
                                guid = parts[5].strip('`')

                                size_match = re.match(r'([0-9.]+)×([0-9.]+)', size_str)
                                if size_match:
                                    width = float(size_match.group(1))
                                    height = float(size_match.group(2))
                                    area = width * height

                                    images.append({
                                        'type': 'RawImage',
                                        'path': path,
                                        'width': width,
                                        'height': height,
                                        'area': area,
                                        'size_str': size_str,
                                        'asset_name': asset_name,
                                        'file_id': file_id,
                                        'guid': guid
                                    })

            # 找最大的图片
            if images:
                # 排除尺寸为0的图片
                valid_images = [img for img in images if img['area'] > 0]

                if valid_images:
                    # 按面积排序，取最大的
                    largest = sorted(valid_images, key=lambda x: x['area'], reverse=True)[0]

                    self.data.append({
                        'prefab_name': prefab_name,
                        'path': path_info,
                        'bg_type': largest['type'],
                        'bg_path': largest['path'],
                        'bg_width': largest['width'],
                        'bg_height': largest['height'],
                        'bg_size': largest['size_str'],
                        'bg_asset': largest['asset_name'],
                        'bg_file_id': largest['file_id'],
                        'bg_guid': largest['guid'],
                        'bg_area': largest['area'],
                        'total_images': len(images)
                    })
                else:
                    # 所有图片都是0尺寸，记录为None
                    self.data.append({
                        'prefab_name': prefab_name,
                        'path': path_info,
                        'bg_type': None,
                        'bg_path': None,
                        'bg_width': 0,
                        'bg_height': 0,
                        'bg_size': '-',
                        'bg_asset': '[All Zero]',
                        'bg_file_id': '-',
                        'bg_guid': '-',
                        'bg_area': 0,
                        'total_images': len(images)
                    })

        except Exception as e:
            print(f"Error parsing {filepath}: {e}")

    def process_all(self):
        """处理所有笔记文件"""
        print("[Info] Processing all analysis files...")

        md_files = []
        for root, dirs, files in os.walk(ANALYSIS_DIR):
            for file in files:
                if file.endswith('.md'):
                    md_files.append(os.path.join(root, file))

        md_files = sorted(md_files)
        print(f"[Info] Found {len(md_files)} markdown files")

        for i, filepath in enumerate(md_files, 1):
            if i % 200 == 1 or i == len(md_files):
                print(f"[Progress] Processing {i}/{len(md_files)}")

            self.parse_markdown(filepath)

        print(f"[Info] Extracted {len(self.data)} prefabs")

    def generate_markdown(self):
        """生成Markdown清单"""
        md = """# 背景图清单

**生成时间**: {time}
**总预制体数**: {total}

---

## 📊 统计信息

| 指标 | 数值 |
|------|------|
| 总预制体数 | {total} |
| 有背景图的 | {with_bg} |
| 无背景图的 | {no_bg} |
| Image背景 | {image_bg} |
| RawImage背景 | {rawimage_bg} |

---

## 📋 完整清单

按预制体名称排序

| # | 预制体名称 | 背景图类型 | 资源名称 | 尺寸 (宽×高) | FileID | GUID |
|---|----------|---------|--------|----------|--------|------|
""".format(
            time=__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            total=len(self.data),
            with_bg=len([d for d in self.data if d['bg_asset'] != '[All Zero]']),
            no_bg=len([d for d in self.data if d['bg_asset'] == '[All Zero]']),
            image_bg=len([d for d in self.data if d['bg_type'] == 'Image']),
            rawimage_bg=len([d for d in self.data if d['bg_type'] == 'RawImage'])
        )

        # 按预制体名称排序
        sorted_data = sorted(self.data, key=lambda x: x['prefab_name'])

        for idx, item in enumerate(sorted_data, 1):
            bg_type_str = item['bg_type'] or 'None'
            md += f"| {idx} | `{item['prefab_name']}` | {bg_type_str} | **{item['bg_asset']}** | {item['bg_size']} | `{item['bg_file_id']}` | `{item['bg_guid']}` |\n"

        # 添加资源GUID索引
        md += "\n---\n\n## 🔍 资源GUID索引\n\n"
        md += "**按GUID分组，显示哪些预制体使用了相同的背景资源**\n\n"

        # 按GUID分组
        guid_groups = {}
        for item in self.data:
            if item['bg_guid'] != '-':
                guid = item['bg_guid']
                asset = item['bg_asset']
                if guid not in guid_groups:
                    guid_groups[guid] = {'asset': asset, 'prefabs': []}
                guid_groups[guid]['prefabs'].append(item['prefab_name'])

        for guid in sorted(guid_groups.keys()):
            info = guid_groups[guid]
            asset = info['asset']
            prefabs = sorted(info['prefabs'])

            md += f"### {asset}\n\n"
            md += f"GUID: `{guid}`\n\n"
            md += f"使用该背景的预制体 ({len(prefabs)}个):\n\n"

            for prefab in prefabs[:50]:  # 显示前50个
                md += f"- {prefab}\n"

            if len(prefabs) > 50:
                md += f"- ... 还有 {len(prefabs) - 50} 个\n"

            md += "\n"

        # 添加按资源名称分类
        md += "\n---\n\n## 🎨 按资源名称分类\n\n"

        asset_groups = {}
        for item in self.data:
            if item['bg_asset'] != '[All Zero]':
                asset = item['bg_asset']
                if asset not in asset_groups:
                    asset_groups[asset] = []
                asset_groups[asset].append(item['prefab_name'])

        for asset in sorted(asset_groups.keys()):
            prefabs = sorted(asset_groups[asset])
            md += f"### {asset} ({len(prefabs)}个预制体)\n\n"
            for prefab in prefabs[:20]:
                md += f"- {prefab}\n"
            if len(prefabs) > 20:
                md += f"- ... 还有 {len(prefabs) - 20} 个\n"
            md += "\n"

        return md

    def save_report(self):
        """保存报告"""
        markdown = self.generate_markdown()

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"[Info] Report saved to: {OUTPUT_FILE}")


def main():
    extractor = BackgroundImageExtractor()

    print("[Info] Extracting background images from all prefabs...")
    extractor.process_all()

    print("[Info] Generating report...")
    extractor.save_report()

    print("[Info] Done!")


if __name__ == "__main__":
    main()

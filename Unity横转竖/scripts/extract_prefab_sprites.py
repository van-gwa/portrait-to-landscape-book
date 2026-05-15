#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
遍历Unity预制体，提取引用的图片资源信息，生成Obsidian笔记
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Set, Tuple

# 设置stdout编码为UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 配置
PREFABS_DIR = r"D:\CursorProject\Dadian\Arts\Assets\ArtResources\UIs\Prefabs"
VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"
NOTES_DIR = os.path.join(VAULT_DIR, "prefab_analysis")
OUTPUT_JSON = os.path.join(VAULT_DIR, "prefab_sprites_index.json")

class PrefabSpriteExtractor:
    def __init__(self):
        self.sprites = {}  # 存储 guid -> 精灵信息
        self.prefabs = {}  # 存储预制体信息
        os.makedirs(NOTES_DIR, exist_ok=True)

    def find_all_prefabs(self) -> List[str]:
        """递归找出所有预制体文件"""
        prefabs = []
        for root, dirs, files in os.walk(PREFABS_DIR):
            for file in files:
                if file.endswith('.prefab'):
                    prefabs.append(os.path.join(root, file))
        return sorted(prefabs)

    def extract_sprites_from_prefab(self, prefab_path: str) -> Dict:
        """从预制体中提取所有精灵资源"""
        sprites_data = {
            "sprites": [],
            "texts": [],
            "images": [],
            "raw_refs": []
        }

        try:
            with open(prefab_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 提取所有的 sprite 引用 (m_Sprite)
            sprite_pattern = r'm_Sprite:\s*\{fileID:\s*([^,}]*),\s*guid:\s*([^,}]*),\s*type:\s*([^}]*)\}'
            sprite_matches = re.findall(sprite_pattern, content)

            for file_id, guid, sprite_type in sprite_matches:
                file_id = file_id.strip()
                guid = guid.strip()
                sprite_type = sprite_type.strip()

                sprite_entry = {
                    "guid": guid,
                    "fileID": file_id,
                    "type": sprite_type,
                    "reference_count": 0
                }

                # 计算这个精灵被引用的次数
                ref_count = len(re.findall(f'guid: {re.escape(guid)}', content))
                sprite_entry["reference_count"] = ref_count

                sprites_data["sprites"].append(sprite_entry)

            # 提取图片组件的详细信息 (Image component)
            image_pattern = r'--- !u!114 &(\d+)\nMonoBehaviour:.*?m_Script: \{fileID: 11500000, guid: fe87c0e1cc204ed48ad3b37840f39efc'

            # 提取所有引用的文件ID和GUID对
            all_refs_pattern = r'fileID: ([^,}]*),\s*guid: ([^,}]*)'
            all_refs = set()
            for match in re.finditer(all_refs_pattern, content):
                file_id, guid = match.groups()
                if guid.strip() and file_id.strip():
                    all_refs.add((file_id.strip(), guid.strip()))

            sprites_data["raw_refs"] = [
                {"fileID": fid, "guid": guid} for fid, guid in all_refs
            ]

            # 提取 RectTransform 的尺寸信息
            size_pattern = r'm_SizeDelta:\s*\{x:\s*([^,]+),\s*y:\s*([^}]+)\}'
            sizes = re.findall(size_pattern, content)
            if sizes:
                sprites_data["sizes"] = [
                    {"x": float(x.strip()), "y": float(y.strip())}
                    for x, y in sizes
                ]

        except Exception as e:
            print(f"❌ 解析失败 {prefab_path}: {e}")
            return None

        return sprites_data

    def get_relative_path(self, full_path: str) -> str:
        """获取相对于Prefabs目录的相对路径"""
        rel_path = os.path.relpath(full_path, PREFABS_DIR)
        return rel_path.replace('\\', '/')

    def generate_markdown_note(self, prefab_path: str, sprites_data: Dict) -> str:
        """生成Markdown笔记"""
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_path = self.get_relative_path(prefab_path)

        md = f"""# {prefab_name}

**预制体路径**: `{rel_path}`
**完整路径**: `{prefab_path}`
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 资源统计

| 指标 | 数值 |
|------|------|
| 精灵引用数 | {len(sprites_data['sprites'])} |
| 所有文件引用 | {len(sprites_data['raw_refs'])} |
| 大小数据点 | {len(sprites_data.get('sizes', []))} |

---

## 🎨 精灵资源清单 (Sprites)

"""

        if sprites_data['sprites']:
            md += "\n| GUID | FileID | 类型 | 引用次数 |\n"
            md += "|------|--------|------|--------|\n"
            for sprite in sprites_data['sprites']:
                md += f"| `{sprite['guid']}` | {sprite['fileID']} | {sprite['type']} | {sprite['reference_count']} |\n"
        else:
            md += "\n*无直接精灵引用*\n"

        md += "\n---\n\n## 📦 所有文件引用 (Raw References)\n\n"

        if sprites_data['raw_refs']:
            md += f"共 {len(sprites_data['raw_refs'])} 个引用\n\n"
            md += "| GUID | FileID |\n"
            md += "|------|--------|\n"
            for ref in sprites_data['raw_refs'][:50]:  # 只显示前50个
                md += f"| `{ref['guid']}` | {ref['fileID']} |\n"
            if len(sprites_data['raw_refs']) > 50:
                md += f"\n*... 还有 {len(sprites_data['raw_refs']) - 50} 个引用（完整数据在JSON文件中）*\n"
        else:
            md += "\n*无引用*\n"

        md += "\n---\n\n## 📏 尺寸信息\n\n"

        if sprites_data.get('sizes'):
            md += f"检测到 {len(sprites_data['sizes'])} 个尺寸数据点\n\n"
            md += "| X | Y | 描述 |\n"
            md += "|---|---|------|\n"
            for i, size in enumerate(sprites_data['sizes'][:20]):
                md += f"| {size['x']:.1f} | {size['y']:.1f} | 数据点 {i+1} |\n"
            if len(sprites_data['sizes']) > 20:
                md += f"\n*... 还有 {len(sprites_data['sizes']) - 20} 个尺寸数据*\n"
        else:
            md += "\n*无尺寸数据*\n"

        md += f"\n---\n\n## 📄 源数据\n\n```json\n"
        md += json.dumps(sprites_data, indent=2, ensure_ascii=False)
        md += "\n```\n"

        return md

    def save_note(self, prefab_path: str, markdown: str) -> str:
        """保存笔记到Obsidian"""
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_dir = os.path.dirname(self.get_relative_path(prefab_path))

        # 在notes目录中建立相同的目录结构
        note_dir = os.path.join(NOTES_DIR, rel_dir)
        os.makedirs(note_dir, exist_ok=True)

        note_path = os.path.join(note_dir, f"{prefab_name}.md")

        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        return note_path

    def process_all_prefabs(self):
        """处理所有预制体"""
        prefabs = self.find_all_prefabs()
        print(f"📂 找到 {len(prefabs)} 个预制体")

        success_count = 0
        failed_count = 0

        all_sprites_index = {}

        for i, prefab_path in enumerate(prefabs, 1):
            prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
            rel_path = self.get_relative_path(prefab_path)

            print(f"\n[{i}/{len(prefabs)}] 处理: {rel_path}")

            sprites_data = self.extract_sprites_from_prefab(prefab_path)

            if sprites_data:
                markdown = self.generate_markdown_note(prefab_path, sprites_data)
                note_path = self.save_note(prefab_path, markdown)

                # 索引这个预制体
                all_sprites_index[rel_path] = {
                    "prefab_name": prefab_name,
                    "sprite_count": len(sprites_data['sprites']),
                    "ref_count": len(sprites_data['raw_refs']),
                    "note_path": note_path,
                    "sprites": sprites_data['sprites'],
                    "guids": [s['guid'] for s in sprites_data['sprites']]
                }

                print(f"✅ 成功 - 精灵: {len(sprites_data['sprites'])}, 引用: {len(sprites_data['raw_refs'])}")
                print(f"   笔记: {note_path}")
                success_count += 1
            else:
                print(f"❌ 失败")
                failed_count += 1

        # 保存索引
        with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
            json.dump(all_sprites_index, f, indent=2, ensure_ascii=False)

        print(f"\n\n{'='*60}")
        print(f"📊 处理完成")
        print(f"成功: {success_count} / {len(prefabs)}")
        print(f"失败: {failed_count} / {len(prefabs)}")
        print(f"索引文件: {OUTPUT_JSON}")
        print(f"笔记目录: {NOTES_DIR}")
        print(f"{'='*60}")

        return all_sprites_index

if __name__ == "__main__":
    extractor = PrefabSpriteExtractor()
    extractor.process_all_prefabs()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终版预制体分析 - 完整Image和RawImage资源分析
包含：Image组件、RawImage组件、资源名称、GUID、FileID
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', write_through=True)

PREFABS_DIR = r"D:\CursorProject\Dadian\Arts\Assets\ArtResources\UIs\Prefabs"
ASSETS_DIR = r"D:\CursorProject\Dadian\Arts\Assets"
VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"
OUTPUT_DIR = os.path.join(VAULT_DIR, "prefab_final_analysis")
os.makedirs(OUTPUT_DIR, exist_ok=True)

class FinalAnalyzer:
    def __init__(self):
        # 缓存GUID -> 资源路径的映射
        self.guid_cache = {}
        self.load_guid_mapping()

    def load_guid_mapping(self):
        """从项目的.meta文件中提取GUID到资源名称的映射"""
        print("[Info] Loading GUID to asset name mapping...")

        # 遍历Assets目录找所有.meta文件
        for root, dirs, files in os.walk(ASSETS_DIR):
            for file in files:
                if file.endswith('.meta'):
                    meta_path = os.path.join(root, file)
                    asset_name = file[:-5]  # 去掉.meta后缀
                    asset_rel_path = os.path.relpath(os.path.join(root, asset_name), ASSETS_DIR)

                    try:
                        with open(meta_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                        # 从.meta文件中提取guid
                        guid_match = re.search(r'guid: ([a-f0-9]+)', content)
                        if guid_match:
                            guid = guid_match.group(1)
                            self.guid_cache[guid] = asset_rel_path
                    except:
                        pass

        print(f"[Info] Loaded {len(self.guid_cache)} GUID mappings")

    def get_asset_name_by_guid(self, guid):
        """根据GUID获取资源名称"""
        if guid in self.guid_cache:
            asset_path = self.guid_cache[guid]
            # 只返回文件名
            return os.path.basename(asset_path)
        return None

    def analyze_prefab(self, prefab_path):
        """完整分析单个预制体，提取Image和RawImage资源"""
        try:
            with open(prefab_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            gameobjects = {}

            # 提取所有GameObject
            gameobject_matches = re.finditer(
                r'--- !u!1 &(\d+)\nGameObject:(.*?)(?=\n--- !u!|\Z)',
                content,
                re.DOTALL
            )

            for match in gameobject_matches:
                go_id = match.group(1)
                go_block = match.group(2)

                name_match = re.search(r'm_Name: (.+?)(?:\n|$)', go_block)
                name = name_match.group(1).strip() if name_match else f"[GO_{go_id}]"

                gameobjects[go_id] = {
                    'name': name,
                    'children': [],
                    'parent': None,
                    'sprite': None,        # Image组件的资源
                    'texture': None,       # RawImage组件的资源
                    'path': name,
                    'components': []       # 记录所有组件
                }

            # 提取RectTransform中的层级关系
            rect_transform_pattern = r'--- !u!224 &(\d+)\nRectTransform:(.*?)(?=\n--- !u!|\Z)'

            for match in re.finditer(rect_transform_pattern, content, re.DOTALL):
                rect_id = match.group(1)
                rect_block = match.group(2)

                go_match = re.search(r'm_GameObject: \{fileID: (\d+)\}', rect_block)
                if not go_match:
                    continue

                go_id = go_match.group(1)

                # 提取父节点
                parent_match = re.search(r'm_Father: \{fileID: (\d+)\}', rect_block)
                parent_id = parent_match.group(1) if parent_match else '0'

                # 提取子节点
                children_match = re.search(r'm_Children:(.*?)(?:\n  m_|\Z)', rect_block, re.DOTALL)
                children = []
                if children_match:
                    children_block = children_match.group(1)
                    child_refs = re.findall(r'fileID: (\d+)', children_block)
                    children = [ref for ref in child_refs]

                # 提取尺寸
                size_match = re.search(r'm_SizeDelta: \{x: ([^,]+), y: ([^}]+)\}', rect_block)
                if size_match and go_id in gameobjects:
                    x, y = size_match.groups()
                    gameobjects[go_id]['size'] = f"{float(x):.1f}×{float(y):.1f}"

                if go_id in gameobjects:
                    gameobjects[go_id]['parent'] = parent_id
                    gameobjects[go_id]['children'] = children

            # 提取Image组件（脚本GUID: fe87c0e1cc204ed48ad3b37840f39efc）
            image_pattern = r'--- !u!114 &(\d+)\nMonoBehaviour:(.*?)(?=\n--- !u!|\Z)'

            for match in re.finditer(image_pattern, content, re.DOTALL):
                comp_id = match.group(1)
                comp_block = match.group(2)

                # 检查是否是Image脚本
                if 'guid: fe87c0e1cc204ed48ad3b37840f39efc' not in comp_block:
                    continue

                go_match = re.search(r'm_GameObject: \{fileID: (\d+)\}', comp_block)
                if not go_match:
                    continue

                go_id = go_match.group(1)

                # 提取m_Sprite
                sprite_match = re.search(
                    r'm_Sprite: \{fileID: ([^,}]*), guid: ([^,}]*), type: ([^}]*)\}',
                    comp_block
                )

                if sprite_match and go_id in gameobjects:
                    file_id, guid, sprite_type = sprite_match.groups()
                    guid = guid.strip()
                    asset_name = self.get_asset_name_by_guid(guid)

                    gameobjects[go_id]['sprite'] = {
                        'fileID': file_id.strip(),
                        'guid': guid,
                        'type': sprite_type.strip(),
                        'asset_name': asset_name
                    }
                    gameobjects[go_id]['components'].append(('Image', asset_name))

            # 提取RawImage组件（脚本GUID: 1344c3c82d62a2a41a3576d8abb8e3ea）
            for match in re.finditer(image_pattern, content, re.DOTALL):
                comp_id = match.group(1)
                comp_block = match.group(2)

                # 检查是否是RawImage脚本
                if 'guid: 1344c3c82d62a2a41a3576d8abb8e3ea' not in comp_block:
                    continue

                go_match = re.search(r'm_GameObject: \{fileID: (\d+)\}', comp_block)
                if not go_match:
                    continue

                go_id = go_match.group(1)

                # 提取m_Texture（RawImage使用m_Texture而不是m_Sprite）
                texture_match = re.search(
                    r'm_Texture: \{fileID: ([^,}]*), guid: ([^,}]*), type: ([^}]*)\}',
                    comp_block
                )

                if texture_match and go_id in gameobjects:
                    file_id, guid, tex_type = texture_match.groups()
                    guid = guid.strip()
                    asset_name = self.get_asset_name_by_guid(guid)

                    gameobjects[go_id]['texture'] = {
                        'fileID': file_id.strip(),
                        'guid': guid,
                        'type': tex_type.strip(),
                        'asset_name': asset_name
                    }
                    gameobjects[go_id]['components'].append(('RawImage', asset_name))

            # 构建完整路径
            def get_full_path(go_id, gameobjects, visited=None):
                if visited is None:
                    visited = set()
                if go_id in visited:
                    return gameobjects[go_id]['name']
                visited.add(go_id)

                parent_id = gameobjects.get(go_id, {}).get('parent')
                if parent_id and parent_id != '0' and parent_id in gameobjects:
                    parent_path = get_full_path(parent_id, gameobjects, visited)
                    return f"{parent_path}/{gameobjects[go_id]['name']}"
                else:
                    return gameobjects[go_id]['name']

            for go_id in gameobjects:
                gameobjects[go_id]['path'] = get_full_path(go_id, gameobjects)

            return gameobjects

        except Exception as e:
            print(f"Error: {e}")
            return None

    def generate_markdown(self, prefab_path, gameobjects):
        """生成最终版Markdown笔记"""
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_path = os.path.relpath(prefab_path, PREFABS_DIR).replace('\\', '/')

        image_gos = [g for g in gameobjects.values() if g.get('sprite')]
        rawimage_gos = [g for g in gameobjects.values() if g.get('texture')]

        md = f"""# {prefab_name}

**路径**: `{rel_path}`
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 统计信息

| 指标 | 数值 |
|------|------|
| GameObject总数 | {len(gameobjects)} |
| Image组件数 | {len(image_gos)} |
| RawImage组件数 | {len(rawimage_gos)} |

---

## 📋 Image资源详细清单

**Image组件使用的精灵资源**

"""

        if image_gos:
            md += "| 完整路径 | 尺寸 | 资源名称 | FileID | GUID |\n"
            md += "|--------|------|--------|--------|------|\n"

            for go in sorted(image_gos, key=lambda x: x['path']):
                path = go['path']
                size = go.get('size', '-')
                sprite = go['sprite']
                asset_name = sprite.get('asset_name') or '[Unknown]'
                md += f"| `{path}` | {size} | **{asset_name}** | `{sprite['fileID']}` | `{sprite['guid']}` |\n"
        else:
            md += "*无Image组件*\n"

        md += "\n---\n\n"
        md += "## 📦 RawImage资源详细清单\n\n"
        md += "**RawImage组件使用的纹理资源**\n\n"

        if rawimage_gos:
            md += "| 完整路径 | 尺寸 | 资源名称 | FileID | GUID |\n"
            md += "|--------|------|--------|--------|------|\n"

            for go in sorted(rawimage_gos, key=lambda x: x['path']):
                path = go['path']
                size = go.get('size', '-')
                texture = go['texture']
                asset_name = texture.get('asset_name') or '[Unknown]'
                md += f"| `{path}` | {size} | **{asset_name}** | `{texture['fileID']}` | `{texture['guid']}` |\n"
        else:
            md += "*无RawImage组件*\n"

        md += "\n---\n\n"
        md += "## 🔍 资源GUID索引\n\n"
        md += "**按资源GUID分组，显示哪些GameObject使用了相同的资源**\n\n"

        # 按GUID分组
        guid_groups = {}
        for go_id, go in gameobjects.items():
            if go.get('sprite'):
                guid = go['sprite']['guid']
                asset_name = go['sprite'].get('asset_name') or '[Unknown]'
                if guid not in guid_groups:
                    guid_groups[guid] = {'type': 'Image', 'asset_name': asset_name, 'gos': []}
                guid_groups[guid]['gos'].append(go)
            if go.get('texture'):
                guid = go['texture']['guid']
                asset_name = go['texture'].get('asset_name') or '[Unknown]'
                if guid not in guid_groups:
                    guid_groups[guid] = {'type': 'RawImage', 'asset_name': asset_name, 'gos': []}
                guid_groups[guid]['gos'].append(go)

        for guid in sorted(guid_groups.keys()):
            info = guid_groups[guid]
            gos = info['gos']
            asset_name = info['asset_name']
            comp_type = info['type']

            md += f"### {asset_name} ({comp_type})\n\n"
            md += f"GUID: `{guid}`\n\n"
            md += f"使用该资源的GameObject ({len(gos)}个):\n\n"

            for go in sorted(gos, key=lambda x: x['path']):
                size = go.get('size', '-')
                if comp_type == 'Image':
                    file_id = go['sprite']['fileID']
                else:
                    file_id = go['texture']['fileID']
                md += f"- `{go['path']}` ({size}) [FileID: {file_id}]\n"
            md += "\n"

        return md

    def process(self, prefab_path):
        """处理单个预制体"""
        gameobjects = self.analyze_prefab(prefab_path)

        if gameobjects is None:
            return False

        markdown = self.generate_markdown(prefab_path, gameobjects)

        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_dir = os.path.dirname(os.path.relpath(prefab_path, PREFABS_DIR))

        output_dir = os.path.join(OUTPUT_DIR, rel_dir)
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"{prefab_name}_final.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        return True


def main():
    analyzer = FinalAnalyzer()

    # 处理示例
    test_prefabs = [
        "Chat/UI_Chat.prefab",
        "Block/UI_BlockBattleMap.prefab",
        "ActApexPvp/UI_ActApexPvp.prefab"
    ]

    print("Processing prefabs for final analysis...")

    for prefab_rel in test_prefabs:
        prefab_path = os.path.join(PREFABS_DIR, prefab_rel)

        if not os.path.exists(prefab_path):
            print(f"Not found: {prefab_rel}")
            continue

        print(f"Processing: {prefab_rel}")

        if analyzer.process(prefab_path):
            print(f"  OK")
        else:
            print(f"  FAILED")

    print(f"\nResults saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

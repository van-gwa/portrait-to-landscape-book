#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量处理所有预制体 - 最终版本
使用新的基础路径，遍历所有预制体并生成最终分析笔记
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', write_through=True)

# 使用新的基础路径
PREFABS_DIR = r"D:\CursorProject\Dadian - 副本\Arts\Assets\ArtResources\UIs\Prefabs"
ASSETS_DIR = r"D:\CursorProject\Dadian - 副本\Arts\Assets"
VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"
OUTPUT_DIR = os.path.join(VAULT_DIR, "prefab_final_analysis")
os.makedirs(OUTPUT_DIR, exist_ok=True)

class FinalAnalyzer:
    def __init__(self):
        self.guid_cache = {}
        self.load_guid_mapping()

    def load_guid_mapping(self):
        """从项目的.meta文件中提取GUID到资源名称的映射"""
        print("[Info] Loading GUID to asset name mapping...")

        count = 0
        for root, dirs, files in os.walk(ASSETS_DIR):
            for file in files:
                if file.endswith('.meta'):
                    meta_path = os.path.join(root, file)
                    asset_name = file[:-5]
                    asset_rel_path = os.path.relpath(os.path.join(root, asset_name), ASSETS_DIR)

                    try:
                        with open(meta_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                        guid_match = re.search(r'guid: ([a-f0-9]+)', content)
                        if guid_match:
                            guid = guid_match.group(1)
                            self.guid_cache[guid] = asset_rel_path
                            count += 1
                    except:
                        pass

        print(f"[Info] Loaded {count} GUID mappings")

    def get_asset_name_by_guid(self, guid):
        """根据GUID获取资源名称"""
        if guid in self.guid_cache:
            asset_path = self.guid_cache[guid]
            return os.path.basename(asset_path)
        return None

    def analyze_prefab(self, prefab_path):
        """完整分析单个预制体"""
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
                    'sprite': None,
                    'texture': None,
                    'path': name,
                    'components': []
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

                parent_match = re.search(r'm_Father: \{fileID: (\d+)\}', rect_block)
                parent_id = parent_match.group(1) if parent_match else '0'

                children_match = re.search(r'm_Children:(.*?)(?:\n  m_|\Z)', rect_block, re.DOTALL)
                children = []
                if children_match:
                    children_block = children_match.group(1)
                    child_refs = re.findall(r'fileID: (\d+)', children_block)
                    children = [ref for ref in child_refs]

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

                if 'guid: fe87c0e1cc204ed48ad3b37840f39efc' not in comp_block:
                    continue

                go_match = re.search(r'm_GameObject: \{fileID: (\d+)\}', comp_block)
                if not go_match:
                    continue

                go_id = go_match.group(1)

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

                if 'guid: 1344c3c82d62a2a41a3576d8abb8e3ea' not in comp_block:
                    continue

                go_match = re.search(r'm_GameObject: \{fileID: (\d+)\}', comp_block)
                if not go_match:
                    continue

                go_id = go_match.group(1)

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

        return md

    def process(self, prefab_path):
        """处理单个预制体"""
        gameobjects = self.analyze_prefab(prefab_path)

        if gameobjects is None:
            return False

        markdown = self.generate_markdown(prefab_path, gameobjects)

        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]

        # 保存到以预制体名称命名的笔记
        output_path = os.path.join(OUTPUT_DIR, f"{prefab_name}.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        return True


def find_all_prefabs(base_path):
    """找出基础路径下所有的预制体"""
    prefabs = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.prefab'):
                prefab_path = os.path.join(root, file)
                prefabs.append(prefab_path)
    return sorted(prefabs)


def batch_process(limit=None, module_filter=None):
    """批量处理预制体"""
    prefabs = find_all_prefabs(PREFABS_DIR)

    print(f"[Info] Found {len(prefabs)} prefabs in {PREFABS_DIR}")

    # 过滤模块
    if module_filter:
        prefabs = [p for p in prefabs if module_filter in p]
        print(f"[Filter] Keeping {len(prefabs)} prefabs from module '{module_filter}'")

    # 限制数量
    if limit:
        prefabs = prefabs[:limit]

    print(f"[Info] Processing {len(prefabs)} prefabs...")
    print(f"[Info] Estimated time: {len(prefabs) * 0.5 / 60:.1f} minutes")

    analyzer = FinalAnalyzer()
    success = 0
    failed = 0

    start_time = datetime.now()

    for i, prefab_path in enumerate(prefabs, 1):
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_path = os.path.relpath(prefab_path, PREFABS_DIR)

        # 每50个打印一次进度
        if i % 50 == 1 or i == len(prefabs):
            elapsed = (datetime.now() - start_time).total_seconds()
            rate = elapsed / max(i-1, 1)
            remaining = rate * (len(prefabs) - i)
            print(f"[Progress] [{i:4d}/{len(prefabs)}] Elapsed: {elapsed:.0f}s, Remaining: {remaining:.0f}s")

        try:
            if analyzer.process(prefab_path):
                success += 1
            else:
                failed += 1
        except Exception as e:
            print(f"[Error] {rel_path}: {str(e)[:50]}")
            failed += 1

    # 统计
    total_time = (datetime.now() - start_time).total_seconds()

    print("")
    print("=" * 60)
    print("COMPLETED")
    print(f"  Success: {success}/{len(prefabs)}")
    print(f"  Failed: {failed}/{len(prefabs)}")
    print(f"  Total time: {total_time:.0f}s ({total_time/60:.1f} min)")
    print(f"  Average: {total_time/max(len(prefabs), 1):.2f}s per prefab")
    print("=" * 60)
    print(f"Results saved to: {OUTPUT_DIR}")
    print("=" * 60)

    return success, failed


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Batch process all prefabs for final analysis"
    )

    parser.add_argument('--limit', type=int, help='Max prefabs to process')
    parser.add_argument('--module', help='Only process specific module')

    args = parser.parse_args()

    batch_process(limit=args.limit, module_filter=args.module)


if __name__ == "__main__":
    main()

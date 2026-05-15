#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版预制体分析 - 完整信息关联
显示Image资源与GUID的对应关系、完整路径等
"""

import os
import sys
import re
from datetime import datetime

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', write_through=True)

PREFABS_DIR = r"D:\CursorProject\Dadian\Arts\Assets\ArtResources\UIs\Prefabs"
VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"
OUTPUT_DIR = os.path.join(VAULT_DIR, "prefab_enhanced_analysis")
os.makedirs(OUTPUT_DIR, exist_ok=True)

class EnhancedAnalyzer:
    def analyze_prefab(self, prefab_path):
        """完整分析单个预制体，提取Image资源关联"""
        try:
            with open(prefab_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # 提取所有GameObject及其信息
            gameobjects = {}

            # 匹配GameObject定义
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
                    'path': name  # 完整路径
                }

            # 提取RectTransform中的层级关系和精灵信息
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
                size_str = ""
                if size_match and go_id in gameobjects:
                    x, y = size_match.groups()
                    size_str = f"{float(x):.1f}×{float(y):.1f}"
                    gameobjects[go_id]['size'] = size_str

                if go_id in gameobjects:
                    gameobjects[go_id]['parent'] = parent_id
                    gameobjects[go_id]['children'] = children

            # 提取所有MonoBehaviour中的Image组件和它们的Sprite
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
                    gameobjects[go_id]['sprite'] = {
                        'fileID': file_id.strip(),
                        'guid': guid.strip(),
                        'type': sprite_type.strip()
                    }

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
        """生成增强版Markdown笔记"""
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_path = os.path.relpath(prefab_path, PREFABS_DIR).replace('\\', '/')

        md = f"""# {prefab_name}

**路径**: `{rel_path}`
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 统计信息

| 指标 | 数值 |
|------|------|
| GameObject总数 | {len(gameobjects)} |
| 使用Image组件的GO | {len([g for g in gameobjects.values() if g.get('sprite')])} |
| 唯一GUID数 | {len(set(g['sprite']['guid'] for g in gameobjects.values() if g.get('sprite')))} |

---

## 📋 Image资源详细清单

**按完整路径显示每个使用Image的GameObject及其资源**

"""

        # 收集所有使用sprite的gameobjects
        sprite_gos = [(go_id, go) for go_id, go in gameobjects.items() if go.get('sprite')]
        sprite_gos.sort(key=lambda x: x[1]['path'])

        if sprite_gos:
            md += "| 完整路径 | 尺寸 | FileID | GUID |\n"
            md += "|--------|------|--------|------|\n"

            for go_id, go in sprite_gos:
                path = go['path']
                size = go.get('size', '-')
                sprite = go['sprite']
                md += f"| `{path}` | {size} | `{sprite['fileID']}` | `{sprite['guid']}` |\n"
        else:
            md += "*无使用Image资源的GameObject*\n"

        md += "\n---\n\n"
        md += "## 🔍 资源GUID索引\n\n"
        md += "**按GUID分组，显示哪些GameObject使用了相同的资源**\n\n"

        # 按GUID分组
        guid_groups = {}
        for go_id, go in gameobjects.items():
            if go.get('sprite'):
                guid = go['sprite']['guid']
                if guid not in guid_groups:
                    guid_groups[guid] = []
                guid_groups[guid].append(go)

        for guid in sorted(guid_groups.keys()):
            gos = guid_groups[guid]
            md += f"### {guid}\n\n"
            md += f"使用该资源的GameObject ({len(gos)}个):\n\n"
            for go in sorted(gos, key=lambda x: x['path']):
                size = go.get('size', '-')
                file_id = go['sprite']['fileID']
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

        output_path = os.path.join(output_dir, f"{prefab_name}_enhanced.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        return True


def main():
    analyzer = EnhancedAnalyzer()

    # 处理几个示例
    test_prefabs = [
        "Chat/UI_Chat.prefab",
        "Block/UI_BlockBattleMap.prefab",
        "ActApexPvp/UI_ActApexPvp.prefab"
    ]

    print("Processing prefabs for enhanced analysis...")

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

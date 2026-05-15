#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复版 - 完整解析预制体GameObject树和资源
直接从.prefab YAML中提取完整的层级信息
"""

import os
import sys
import re
from datetime import datetime

# 设置stdout编码为UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PREFABS_DIR = r"D:\CursorProject\Dadian\Arts\Assets\ArtResources\UIs\Prefabs"
VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"
OUTPUT_DIR = os.path.join(VAULT_DIR, "prefab_complete_analysis")
os.makedirs(OUTPUT_DIR, exist_ok=True)

class CompleteAnalyzer:
    def analyze_prefab(self, prefab_path):
        """完整分析单个预制体"""
        try:
            with open(prefab_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # 提取所有GameObject
            # 格式: --- !u!1 &123456789\nGameObject:\n  m_ObjectHideFlags: 0\n  ...\n  m_Name: GoName\n
            gameobject_matches = re.finditer(
                r'--- !u!1 &(\d+)\nGameObject:(.*?)(?=\n--- !u!|\Z)',
                content,
                re.DOTALL
            )

            gameobjects = {}
            for match in gameobject_matches:
                go_id = match.group(1)
                go_block = match.group(2)

                # 提取m_Name
                name_match = re.search(r'm_Name: (.+?)(?:\n|$)', go_block)
                name = name_match.group(1).strip() if name_match else f"[GO_{go_id}]"

                # 提取layer (m_Layer)
                layer_match = re.search(r'm_Layer: (\d+)', go_block)
                layer = int(layer_match.group(1)) if layer_match else 0

                gameobjects[go_id] = {
                    'name': name,
                    'layer': layer,
                    'children': [],
                    'parent': None,
                    'components': []
                }

            # 提取RectTransform来确定父子关系
            rect_transform_pattern = r'--- !u!224 &(\d+)\nRectTransform:(.*?)(?=\n--- !u!|\Z)'

            hierarchy = {}  # rect_id -> parent_id
            for match in re.finditer(rect_transform_pattern, content, re.DOTALL):
                rect_id = match.group(1)
                rect_block = match.group(2)

                # 找对应的GameObject
                go_match = re.search(r'm_GameObject: \{fileID: (\d+)\}', rect_block)
                if not go_match:
                    continue

                go_id = go_match.group(1)

                # 提取父节点
                parent_match = re.search(r'm_Father: \{fileID: (\d+)\}', rect_block)
                parent_id = parent_match.group(1) if parent_match else '0'

                # 提取子节点
                children_match = re.search(r'm_Children:(.*?)(?:\n  m_\w+:|\n  \w+:|\Z)', rect_block, re.DOTALL)
                children = []
                if children_match:
                    children_block = children_match.group(1)
                    child_refs = re.findall(r'fileID: (\d+)', children_block)
                    children = [ref for ref in child_refs]

                if go_id in gameobjects:
                    gameobjects[go_id]['parent'] = parent_id
                    gameobjects[go_id]['children'] = children

            # 提取RectTransform的尺寸
            for match in re.finditer(rect_transform_pattern, content, re.DOTALL):
                rect_id = match.group(1)
                rect_block = match.group(2)

                go_match = re.search(r'm_GameObject: \{fileID: (\d+)\}', rect_block)
                if not go_match:
                    continue

                go_id = go_match.group(1)

                # 提取m_SizeDelta
                size_match = re.search(r'm_SizeDelta: \{x: ([^,]+), y: ([^}]+)\}', rect_block)
                if size_match and go_id in gameobjects:
                    x, y = size_match.groups()
                    gameobjects[go_id]['size'] = f"{float(x):.1f}×{float(y):.1f}"

            # 提取所有Image组件使用的Sprite
            image_pattern = r'--- !u!114 &(\d+)\nMonoBehaviour:(.*?)(?=\n--- !u!|\Z)'
            sprites_used = {}  # go_id -> sprite_info

            for match in re.finditer(image_pattern, content, re.DOTALL):
                comp_id = match.group(1)
                comp_block = match.group(2)

                # 检查是否是Image脚本 (guid: fe87c0e1cc204ed48ad3b37840f39efc)
                if 'guid: fe87c0e1cc204ed48ad3b37840f39efc' not in comp_block:
                    continue

                # 找对应的GameObject
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
                    sprites_used[go_id] = {
                        'fileID': file_id.strip(),
                        'guid': guid.strip(),
                        'type': sprite_type.strip()
                    }
                    gameobjects[go_id]['sprite'] = sprites_used[go_id]

            return gameobjects, sprites_used

        except Exception as e:
            print(f"❌ 分析失败: {e}")
            return None, None

    def build_tree_string(self, go_id, gameobjects, depth=0, visited=None):
        """构建GameObject树的字符串表示"""
        if visited is None:
            visited = set()

        if go_id in visited or go_id not in gameobjects:
            return ""

        visited.add(go_id)

        go = gameobjects[go_id]
        name = go['name']
        size_info = f" {go.get('size', '')}" if 'size' in go else ""

        # 判断是否有Sprite
        sprite_info = ""
        if 'sprite' in go:
            sprite = go['sprite']
            sprite_info = f" [Sprite: {sprite['guid'][:8]}...]"

        indent = "  " * depth
        line = f"{indent}├─ {name}{size_info}{sprite_info}\n"

        # 递归添加子节点
        for child_id in go.get('children', []):
            child_go = gameobjects.get(child_id)
            if child_go and child_id not in visited:
                line += self.build_tree_string(child_id, gameobjects, depth + 1, visited)

        return line

    def generate_markdown(self, prefab_path, gameobjects, sprites_used):
        """生成Markdown笔记"""
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_path = os.path.relpath(prefab_path, PREFABS_DIR).replace('\\', '/')

        md = f"""# {prefab_name}

**路径**: `{rel_path}`
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 统计信息

| 指标 | 数值 |
|------|------|
| GameObject数量 | {len(gameobjects)} |
| 使用精灵的GO | {len(sprites_used)} |
| 唯一精灵GUID | {len(set(s['guid'] for s in sprites_used.values()))} |

---

## 🎮 GameObject 树（完整结构）

\`\`\`
"""

        # 找根节点（parent为'0'的）
        root_ids = [go_id for go_id, go in gameobjects.items() if go.get('parent') == '0']

        for root_id in root_ids:
            md += self.build_tree_string(root_id, gameobjects)

        md += """```

---

## 🎨 精灵资源清单

"""

        if sprites_used:
            md += "| GameObject | 尺寸 | FileID | GUID | \n"
            md += "|------------|------|--------|------|\n"

            for go_id, sprite in sorted(sprites_used.items()):
                go_name = gameobjects[go_id].get('name', f'[{go_id}]')
                size = gameobjects[go_id].get('size', '-')
                md += f"| {go_name} | {size} | `{sprite['fileID']}` | `{sprite['guid']}` |\n"
        else:
            md += "*无使用精灵的GameObject*\n"

        return md

    def process(self, prefab_path):
        """处理单个预制体"""
        gameobjects, sprites_used = self.analyze_prefab(prefab_path)

        if gameobjects is None:
            return False

        # 生成Markdown
        markdown = self.generate_markdown(prefab_path, gameobjects, sprites_used)

        # 保存文件
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_dir = os.path.dirname(os.path.relpath(prefab_path, PREFABS_DIR))

        output_dir = os.path.join(OUTPUT_DIR, rel_dir)
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"{prefab_name}_complete.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        return True


def main():
    analyzer = CompleteAnalyzer()

    # 处理几个示例
    test_prefabs = [
        "ActApexPvp/UI_ActApexPvp.prefab",
        "Beauty/UI_BeautyBookGet.prefab",
        "Chat/UI_Chat.prefab"
    ]

    print("📂 开始完整分析...")

    for prefab_rel in test_prefabs:
        prefab_path = os.path.join(PREFABS_DIR, prefab_rel)

        if not os.path.exists(prefab_path):
            print(f"❌ 未找到: {prefab_rel}")
            continue

        print(f"✅ 处理: {prefab_rel}")

        if analyzer.process(prefab_path):
            print(f"   ✓ 成功生成完整分析")
        else:
            print(f"   ✗ 失败")

    print(f"\n✅ 完成！结果保存在: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

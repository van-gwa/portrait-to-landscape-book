#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
改进版预制体分析 - 提取完整的GameObject树和资源名称
"""

import os
import sys
import json
import re
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

# 设置stdout编码为UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PREFABS_DIR = r"D:\CursorProject\Dadian\Arts\Assets\ArtResources\UIs\Prefabs"
VAULT_DIR = r"D:\obsidianProject\portrait-to-landscape\Unity横转竖"
ENHANCED_NOTES_DIR = os.path.join(VAULT_DIR, "prefab_analysis_enhanced")
os.makedirs(ENHANCED_NOTES_DIR, exist_ok=True)

class EnhancedPrefabExtractor:
    def __init__(self):
        self.prefab_data = {}

    def parse_prefab_yaml(self, prefab_path: str) -> Dict[str, Any]:
        """使用YAML解析器完整解析预制体"""
        try:
            with open(prefab_path, 'r', encoding='utf-8', errors='ignore') as f:
                # 读取raw内容
                content = f.read()

            # 使用正则表达式分段解析YAML
            gameobject_pattern = r'--- !u!1 &(\d+)\nGameObject:.*?\n  m_Name: (.+?)(?:\n|$)'
            image_pattern = r'--- !u!114 &(\d+)\nMonoBehaviour:.*?m_Script: \{fileID: 11500000, guid: fe87c0e1cc204ed48ad3b37840f39efc'

            # 提取GameObject和它们的ID
            gameobjects = {}
            for match in re.finditer(gameobject_pattern, content):
                go_id, name = match.groups()
                name = name.strip()
                gameobjects[go_id] = {'name': name, 'children': []}

            # 提取RectTransform中的m_Children引用
            rect_pattern = r'm_Children:\n  - \{fileID: (\d+)\}'

            # 提取Image组件使用的Sprite
            sprite_pattern = r'm_Sprite: \{fileID: ([^,}]*),\s*guid: ([^,}]*)'

            # 提取GameObject的层级关系
            hierarchy = {}
            rect_transform_pattern = r'--- !u!224 &(\d+)\nRectTransform:.*?m_GameObject: \{fileID: (\d+)\}.*?m_Children:\n(.*?)\n  m_Father: \{fileID: (\d+)\}'

            for match in re.finditer(rect_transform_pattern, content, re.DOTALL):
                rect_id, go_id, children_str, father_id = match.groups()
                children = re.findall(r'\{fileID: (\d+)\}', children_str)

                go_id = go_id.strip()
                father_id = father_id.strip()

                if go_id in gameobjects:
                    gameobjects[go_id]['rect_id'] = rect_id
                    gameobjects[go_id]['children_ids'] = children
                    gameobjects[go_id]['parent_id'] = father_id

            # 提取所有Image组件使用的精灵
            sprites_used = []
            for match in re.finditer(sprite_pattern, content):
                file_id, guid = match.groups()
                sprites_used.append({
                    'fileID': file_id.strip(),
                    'guid': guid.strip()
                })

            return {
                'gameobjects': gameobjects,
                'sprites': sprites_used,
                'raw_content': content
            }

        except Exception as e:
            print(f"❌ 解析失败 {prefab_path}: {e}")
            return None

    def build_hierarchy_tree(self, gameobjects: Dict, root_name: str = "Root") -> str:
        """构建完整的GameObject树"""
        # 找到根节点（没有父节点的GameObject）
        root_ids = []
        for go_id, data in gameobjects.items():
            if data.get('parent_id') == '0':
                root_ids.append(go_id)

        tree_lines = []

        def traverse(go_id, depth=0):
            if go_id not in gameobjects:
                return

            data = gameobjects[go_id]
            indent = "  " * depth
            name = data.get('name', 'Unknown')

            # 尝试从内容中提取Size信息
            size_info = ""

            tree_lines.append(f"{indent}├─ {name}{size_info}")

            # 递归处理子节点
            for child_id in data.get('children_ids', []):
                traverse(child_id, depth + 1)

        # 从所有根节点开始遍历
        for root_id in root_ids:
            traverse(root_id)

        return "\n".join(tree_lines)

    def generate_enhanced_markdown(self, prefab_path: str, extracted_data: Dict) -> str:
        """生成增强版笔记，包含完整树结构"""
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
        rel_path = os.path.relpath(prefab_path, PREFABS_DIR).replace('\\', '/')

        md = f"""# {prefab_name}

**预制体路径**: `{rel_path}`
**完整路径**: `{prefab_path}`
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 基本统计

| 指标 | 数值 |
|------|------|
| GameObject数量 | {len(extracted_data['gameobjects'])} |
| 使用的精灵资源 | {len(extracted_data['sprites'])} |

---

## 🎮 GameObject 树结构

\`\`\`
{self.build_hierarchy_tree(extracted_data['gameobjects'])}
\`\`\`

---

## 🎨 使用的精灵资源

| FileID | GUID | 说明 |
|--------|------|------|
"""

        for sprite in extracted_data['sprites']:
            md += f"| `{sprite['fileID']}` | `{sprite['guid']}` | Sprite资源 |\n"

        md += "\n---\n\n## 📋 详细信息\n\n"
        md += f"### GameObject 列表 ({len(extracted_data['gameobjects'])} 个)\n\n"
        md += "| ID | 名称 | 子节点数 |\n"
        md += "|-----|------|--------|\n"

        for go_id, data in sorted(extracted_data['gameobjects'].items()):
            children_count = len(data.get('children_ids', []))
            name = data.get('name', 'Unknown')
            md += f"| `{go_id}` | {name} | {children_count} |\n"

        return md

    def process_single_prefab(self, prefab_path: str) -> bool:
        """处理单个预制体"""
        prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]

        extracted = self.parse_prefab_yaml(prefab_path)
        if not extracted:
            return False

        # 生成Markdown
        markdown = self.generate_enhanced_markdown(prefab_path, extracted)

        # 保存笔记
        rel_dir = os.path.dirname(os.path.relpath(prefab_path, PREFABS_DIR))
        note_dir = os.path.join(ENHANCED_NOTES_DIR, rel_dir)
        os.makedirs(note_dir, exist_ok=True)

        note_path = os.path.join(note_dir, f"{prefab_name}_enhanced.md")
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        return True

    def process_all(self):
        """处理所有预制体"""
        prefabs = []
        for root, dirs, files in os.walk(PREFABS_DIR):
            for file in files:
                if file.endswith('.prefab'):
                    prefabs.append(os.path.join(root, file))

        prefabs = sorted(prefabs)
        success = 0

        print(f"📂 找到 {len(prefabs)} 个预制体，开始增强处理...")

        for i, prefab_path in enumerate(prefabs[:10], 1):  # 先处理前10个作为示例
            prefab_name = os.path.splitext(os.path.basename(prefab_path))[0]
            rel_path = os.path.relpath(prefab_path, PREFABS_DIR)

            print(f"\n[{i}/10] {rel_path}")

            if self.process_single_prefab(prefab_path):
                print(f"✅ 成功")
                success += 1
            else:
                print(f"❌ 失败")

        print(f"\n✅ 处理完成: {success}/10 成功")
        print(f"📂 增强笔记保存在: {ENHANCED_NOTES_DIR}")


if __name__ == "__main__":
    extractor = EnhancedPrefabExtractor()
    extractor.process_all()

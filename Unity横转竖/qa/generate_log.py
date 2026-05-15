#!/usr/bin/env python3
"""Generate comprehensive QA log for UI type analysis"""
import os, re
from collections import Counter
from PIL import Image
import numpy as np

wiki_map = {}
with open(r'D:/obsidianProject/portrait-to-landscape/Unity横转竖/qa/__ui_type_mapping.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('#'):
            continue
        parts = line.strip().split('\t')
        if len(parts) >= 3:
            wiki_map[parts[0]] = {'type': parts[1], 'group': parts[2]}

img_dir = r'D:/CursorProject/Dadian - 副本/Arts/Assets/Doc/UIImage'
prefab_dir = r'D:/obsidianProject/portrait-to-landscape/Unity横转竖/prefab_final_analysis'

results = []
for fname in sorted(os.listdir(img_dir)):
    if not fname.endswith('.png') or fname.startswith('__'):
        continue
    ui_name = fname.replace('.png', '')

    # Image features
    img_path = os.path.join(img_dir, fname)
    try:
        img = Image.open(img_path).convert('RGB')
        arr = np.array(img)
        h, w, _ = arr.shape
        gray = np.mean(arr, axis=2)

        overall_brightness = round(float(np.mean(gray)), 1)
        b = min(10, h//40)
        borders_dark = all([
            np.mean(gray[:b, :]) < 100,
            np.mean(gray[-b:, :]) < 100,
            np.mean(gray[:, :b]) < 100,
            np.mean(gray[:, -b:]) < 100
        ])
        center_brightness = round(float(np.mean(gray[int(h*0.15):int(h*0.85), int(w*0.15):int(w*0.85)])), 1)
        is_dark = overall_brightness < 40
        is_bright = overall_brightness > 200
        left_avg = float(np.mean(gray[:, :w//2]))
        right_avg = float(np.mean(gray[:, w//2:]))
        lr_diff = round(abs(left_avg - right_avg), 1)
    except:
        overall_brightness = 0
        borders_dark = False
        center_brightness = 0
        is_dark = False
        is_bright = False
        lr_diff = 0

    # Image type label
    if is_dark:
        img_type = "全屏深色界面"
    elif is_bright and not borders_dark:
        img_type = "亮色轻量界面" if lr_diff <= 30 else "亮色左右分栏"
    elif borders_dark:
        if center_brightness > 200:
            img_type = "浅色弹框+深色边框"
        elif lr_diff > 40:
            img_type = "深色边框+左右分栏"
        else:
            img_type = "标准深色边框面板"
    else:
        img_type = "左右分栏" if lr_diff > 30 else "中等亮度面板"

    # Wiki lookup
    wiki_info = wiki_map.get(ui_name, None)
    prefab_path = os.path.join(prefab_dir, f'{ui_name}.md')
    has_prefab = os.path.exists(prefab_path)

    if wiki_info:
        suggested_type = wiki_info['type']
        suggested_group = wiki_info['group']
        source = "WIKI"
    else:
        name_lower = ui_name.lower()
        if 'tip' in name_lower:
            suggested_type = 'tips'
            suggested_group = '基础控件'
        elif 'sign' in name_lower:
            suggested_type = '活动打脸弹窗'
            suggested_group = '弹框类'
        elif 'buy' in name_lower or 'shop' in name_lower or 'purchase' in name_lower:
            suggested_type = '使用弹框'
            suggested_group = '弹框类'
        elif 'reward' in name_lower or 'bonus' in name_lower or 'gift' in name_lower:
            suggested_type = '展示-横条-条内信息'
            suggested_group = '展示横条系列'
        elif 'skill' in name_lower:
            suggested_type = 'tips'
            suggested_group = '基础控件'
        elif 'chat' in name_lower or 'bubble' in name_lower or 'talk' in name_lower:
            suggested_type = '左-右'
            suggested_group = '左右布局'
        elif 'fly' in name_lower or 'float' in name_lower or 'marquee' in name_lower:
            suggested_type = 'tips'
            suggested_group = '基础控件'
        elif 'rank' in name_lower:
            suggested_type = '上标题-中竖列表-下信息'
            suggested_group = '上标题系列'
        elif 'main' in name_lower or 'lobby' in name_lower or 'root' in name_lower:
            suggested_type = 'mainUI'
            suggested_group = '基础控件'
        elif 'load' in name_lower or 'login' in name_lower or 'wait' in name_lower or 'net' in name_lower:
            suggested_type = '登录加载全屏'
            suggested_group = '全屏类'
        elif 'setting' in name_lower:
            suggested_type = '上标题-中横列表-下信息'
            suggested_group = '上标题系列'
        elif 'task' in name_lower:
            suggested_type = '上标题-中竖列表-下信息'
            suggested_group = '上标题系列'
        elif 'gm' in name_lower or 'debug' in name_lower:
            suggested_type = 'panel'
            suggested_group = '基础控件'
        elif 'msg' in name_lower or 'message' in name_lower or 'notice' in name_lower:
            suggested_type = '确认弹框'
            suggested_group = '弹框类'
        elif 'video' in name_lower:
            suggested_type = '功能开启&展示'
            suggested_group = '弹框类'
        elif 'scene' in name_lower:
            suggested_type = '全屏背景界面'
            suggested_group = '全屏类'
        elif 'bell' in name_lower:
            suggested_type = '展示-横条-条内信息'
            suggested_group = '展示横条系列'
        elif 'front' in name_lower:
            suggested_type = '展示-横条-左图-右信息'
            suggested_group = '展示横条系列'
        else:
            suggested_type = '待确认（新UI）'
            suggested_group = '待分类'
        source = "AI推测"

    results.append({
        'ui_name': ui_name,
        'suggested_type': suggested_type,
        'suggested_group': suggested_group,
        'source': source,
        'has_prefab': has_prefab,
        'brightness': overall_brightness,
        'borders_dark': borders_dark,
        'img_type': img_type,
    })

# Generate log
log_dir = r'D:/obsidianProject/portrait-to-landscape/Unity横转竖/qa/deepseek_cheek_ui_type_log'
os.makedirs(log_dir, exist_ok=True)

log_path = os.path.join(log_dir, 'ui_type_analysis.md')
with open(log_path, 'w', encoding='utf-8') as f:
    f.write("# UI Type Analysis Log\n\n")
    f.write("**Date**: 2026-05-14\n")
    f.write("**Source**: 976 screenshots from Dadian - Arts/Assets/Doc/UIImage/\n")
    f.write("**Wiki Reference**: llm_wiki (63 types, 891 mapped UIs)\n\n")

    wiki_count = sum(1 for r in results if r['source'] == 'WIKI')
    ai_count = sum(1 for r in results if r['source'] == 'AI推测')
    prefab_count = sum(1 for r in results if r['has_prefab'])

    f.write("## Summary\n\n")
    f.write(f"| Metric | Value |\n|--------|-------|\n")
    f.write(f"| Total Images | {len(results)} |\n")
    f.write(f"| With Wiki Entry | {wiki_count} |\n")
    f.write(f"| Without Wiki Entry | {ai_count} |\n")
    f.write(f"| With Prefab Analysis | {prefab_count} |\n\n")

    f.write("## Type Group Distribution\n\n")
    f.write("| Group | Count |\n|-------|-------|\n")
    group_count = Counter(r['suggested_group'] for r in results)
    for g, c in sorted(group_count.items(), key=lambda x: -x[1]):
        f.write(f"| {g} | {c} |\n")
    f.write("\n")

    f.write("## UIs Without Wiki Entry (85)\n\n")
    f.write("These UIs are NOT recorded in wiki layout types.\n\n")
    f.write("| UI Name | AI Inferred Type | Group | Has Prefab | Image Feature |\n")
    f.write("|---------|-----------------|-------|------------|--------------|\n")
    for r in results:
        if r['source'] == 'AI推测':
            f.write(f"| {r['ui_name']} | {r['suggested_type']} | {r['suggested_group']} | {'Y' if r['has_prefab'] else 'N'} | {r['img_type']} |\n")
    f.write("\n")

    f.write("## Wiki Type Distribution\n\n")
    f.write("| Wiki Type | Count | Group |\n|-----------|-------|-------|\n")
    wiki_types = Counter((r['suggested_type'], r['suggested_group']) for r in results if r['source'] == 'WIKI')
    for (t, g), c in sorted(wiki_types.items(), key=lambda x: -x[1]):
        f.write(f"| {t} | {c} | {g} |\n")
    f.write("\n")

    f.write("## Complete UI Inventory ({})\n\n".format(len(results)))
    f.write("| # | UI Name | Type | Group | Source |\n")
    f.write("|---|---------|------|-------|--------|\n")
    for i, r in enumerate(results, 1):
        f.write(f"| {i} | {r['ui_name']} | {r['suggested_type']} | {r['suggested_group']} | {r['source']} |\n")

print(f"Done! {len(results)} entries written to {log_path}")
print(f"Wiki: {wiki_count}, AI inferred: {ai_count}")

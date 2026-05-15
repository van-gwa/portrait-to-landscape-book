#!/usr/bin/env python3
"""UI Screenshot Analyzer: extract layout features and compare with wiki types"""

import os, re, json, glob
from PIL import Image
import numpy as np

# Paths
IMG_DIR = r'D:/CursorProject/Dadian - 副本/Arts/Assets/Doc/UIImage'
WIKI_MAP_FILE = r'D:/obsidianProject/portrait-to-landscape/Unity横转竖/qa/__ui_type_mapping.txt'
OUTPUT_DIR = r'D:/obsidianProject/portrait-to-landscape/Unity横转竖/qa'

def load_wiki_mapping():
    """Load UI-to-type mapping from wiki"""
    mapping = {}
    with open(WIKI_MAP_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                mapping[parts[0]] = {'type': parts[1], 'group': parts[2]}
    return mapping

def analyze_image(img_path):
    """Extract layout features from an image"""
    img = Image.open(img_path).convert('RGB')
    arr = np.array(img)
    h, w, _ = arr.shape
    gray = np.mean(arr, axis=2)

    # Border analysis - check if each side has a dark decorative border
    b = min(12, h//40, w//40)
    border = {
        'top': bool(np.mean(gray[:b, :]) < 90),
        'bottom': bool(np.mean(gray[-b:, :]) < 90),
        'left': bool(np.mean(gray[:, :b]) < 90),
        'right': bool(np.mean(gray[:, -b:]) < 90),
    }
    all_four = border['top'] and border['bottom'] and border['left'] and border['right']

    # Check for 四边木栏 pattern: dark decorative borders on all 4 sides,
    # with a slightly lighter inner border (the wood frame)
    inner = min(30, h//15, w//15)
    border_inner = {
        'top': bool(np.mean(gray[b:inner, :]) > np.mean(gray[:b, :]) + 20),
        'bottom': bool(np.mean(gray[-inner:-b, :]) > np.mean(gray[-b:, :]) + 20),
    }

    # Region analysis - divide into 3x3 grid and check brightness
    regions = {}
    for row in range(3):
        for col in range(3):
            r_start = int(h * row / 3)
            r_end = int(h * (row + 1) / 3)
            c_start = int(w * col / 3)
            c_end = int(w * (col + 1) / 3)
            region = gray[r_start:r_end, c_start:c_end]
            regions[f'r{row}c{col}'] = float(np.mean(region))

    # Check for left-right split
    left_region = gray[int(h*0.1):int(h*0.9), :int(w*0.35)]
    right_region = gray[int(h*0.1):int(h*0.9), int(w*0.65):]
    center_region = gray[int(h*0.1):int(h*0.9), int(w*0.35):int(w*0.65)]

    lr_diff = abs(float(np.mean(left_region)) - float(np.mean(right_region)))
    left_is_dark = float(np.mean(left_region)) < 80

    # Horizontal projection - find distinct content bands
    h_proj = np.mean(gray, axis=1)
    h_smooth = np.convolve(h_proj, np.ones(7)/7, mode='valid')
    h_grad = np.abs(np.diff(h_smooth))

    # Count significant transitions
    threshold = np.mean(h_grad) + np.std(h_grad)
    significant = np.where(h_grad > threshold)[0]

    # Check for title area at top
    title_region = gray[:int(h*0.08), int(w*0.2):int(w*0.8)]
    has_title = float(np.std(title_region)) > 30

    # Check bottom button area
    btn_region = gray[-int(h*0.1):, int(w*0.2):int(w*0.8)]
    has_bottom_buttons = float(np.std(btn_region)) > 25

    # Overall brightness stats
    overall_avg = float(np.mean(gray))
    center_avg = float(np.mean(center_region))

    return {
        'size': f'{w}x{h}',
        'overall_brightness': round(overall_avg, 1),
        'center_brightness': round(center_avg, 1),
        'border_dark': border,
        'four_borders_dark': all_four,
        'lr_brightness_diff': round(lr_diff, 1),
        'left_is_dark': left_is_dark,
        'has_title_bar': has_title,
        'has_bottom_buttons': has_bottom_buttons,
        'horizontal_transitions': len(significant),
        'regions': regions,
    }

def classify_by_features(features):
    """Classify UI type based on image features"""
    f = features
    b = f['border_dark']
    four_dark = f['four_borders_dark']

    # Very dark overall -> fullscreen or dark themed
    if f['overall_brightness'] < 30:
        if f['horizontal_transitions'] > 15:
            return '全屏界面（深色复杂）'
        return '全屏背景界面'

    # Very bright overall -> simple page/loading
    if f['overall_brightness'] > 230:
        return 'mainUI/轻量页面'

    # Four dark borders -> likely a framed panel
    if four_dark and b['top'] and b['bottom']:
        # Check if left is significantly darker (has sidebar/nav)
        if f['left_is_dark']:
            return '四边木栏+左导航'
        # Bright center with content structure
        if f['horizontal_transitions'] > 12:
            return '四边木栏+列表'
        if f['has_title_bar'] and f['has_bottom_buttons']:
            return '四边木栏（蒸笼标签）底'
        return '四边木栏（常规）'

    # Dialog-like: dark edges, bright center
    if f['center_brightness'] > 150 and f['overall_brightness'] < 180:
        if f['lr_brightness_diff'] > 40:
            return '左-右（弹框）'
        if f['has_title_bar']:
            if f['has_bottom_buttons']:
                return '确认弹框'
            return '使用弹框'
        return '弹框类'

    # Left-right layout: significant difference between left and right
    if f['lr_brightness_diff'] > 30:
        if f['left_is_dark']:
            return '左-右（深色左区）'
        return '左-右'

    # Content-heavy with many horizontal divisions
    if f['horizontal_transitions'] > 10:
        if f['has_title_bar']:
            return '上标题+列表'
        return '列表式界面'

    # Bright center panel
    if f['center_brightness'] > 180:
        if f['has_title_bar']:
            return '上标题系列'
        return '展示横条系列'

    return '待确定'

def main():
    wiki_map = load_wiki_mapping()
    print(f"Loaded {len(wiki_map)} wiki mappings")

    # Get all image files
    all_images = sorted([f.replace('.png', '') for f in os.listdir(IMG_DIR)
                        if f.endswith('.png') and not f.startswith('__')])
    print(f"Total images: {len(all_images)}")

    # Process all images and compare
    results = []
    for ui_name in all_images:
        img_path = os.path.join(IMG_DIR, f'{ui_name}.png')
        if not os.path.exists(img_path):
            continue

        try:
            features = analyze_image(img_path)
            predicted = classify_by_features(features)
            wiki_info = wiki_map.get(ui_name, None)
            wiki_type = wiki_info['type'] if wiki_info else 'WIKI中无记录'
            wiki_group = wiki_info['group'] if wiki_info else ''

            match_status = '一致' if predicted == wiki_type else ('不一致' if wiki_info else '无WIKI')

            results.append({
                'ui_name': ui_name,
                'predicted': predicted,
                'wiki_type': wiki_type,
                'wiki_group': wiki_group,
                'match': match_status,
                'brightness': features['overall_brightness'],
            })
        except Exception as e:
            results.append({
                'ui_name': ui_name,
                'predicted': f'ERROR: {str(e)[:50]}',
                'wiki_type': wiki_map.get(ui_name, {}).get('type', ''),
                'wiki_group': '',
                'match': 'ERROR',
                'brightness': 0,
            })

    # Generate summary stats
    matched = sum(1 for r in results if r['match'] == '一致')
    mismatched = sum(1 for r in results if r['match'] == '不一致')
    no_wiki = sum(1 for r in results if r['match'] == '无WIKI')
    errors = sum(1 for r in results if r['match'] == 'ERROR')

    print(f"\n{'='*70}")
    print(f"Results Summary:")
    print(f"{'='*70}")
    print(f"  Total processed: {len(results)}")
    print(f"  ✓ Matched wiki:  {matched}")
    print(f"  ✗ Mismatched:    {mismatched}")
    print(f"  - No wiki entry: {no_wiki}")
    print(f"  ! Errors:        {errors}")

    # Write detailed log
    log_path = os.path.join(OUTPUT_DIR, 'deepseek_cheek_ui_type_log', 'analysis_log.md')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(f"# UI Type Analysis Log\n\n")
        f.write(f"**Total images**: {len(results)}  \n")
        f.write(f"**Matched**: {matched} | **Mismatched**: {mismatched} | **No wiki**: {no_wiki} | **Errors**: {errors}  \n")
        f.write(f"**Generated**: 2026-05-14  \n\n")

        f.write("## Mismatched Entries (Image Analysis ≠ Wiki)\n\n")
        f.write("| UI Name | Image Analysis | Wiki Type | Notes |\n")
        f.write("|---------|---------------|-----------|-------|\n")
        for r in results:
            if r['match'] == '✗ 不一致':
                f.write(f"| {r['ui_name']} | {r['predicted']} | {r['wiki_type']} | 需人工复核 |\n")

        f.write("\n## Full Results\n\n")
        f.write("| UI Name | Predicted Type | Wiki Type | Group | Match |\n")
        f.write("|---------|---------------|-----------|-------|-------|\n")
        for r in results:
            f.write(f"| {r['ui_name']} | {r['predicted']} | {r['wiki_type']} | {r['wiki_group']} | {r['match']} |\n")

    print(f"\nLog written to: {log_path}")

    # Print mismatches
    print(f"\n{'='*70}")
    print(f"Mismatched Entries:")
    print(f"{'='*70}")
    for r in results:
        if r['match'] == '✗ 不一致':
            print(f"  {r['ui_name']}: Image->{r['predicted']} vs Wiki->{r['wiki_type']}")

if __name__ == '__main__':
    main()

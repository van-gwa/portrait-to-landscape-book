#!/usr/bin/env python3
"""Generate final QA log and learning notes"""
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
log_dir = r'D:/obsidianProject/portrait-to-landscape/Unity横转竖/qa/deepseek_cheek_ui_type_log'
os.makedirs(log_dir, exist_ok=True)

# Improved name-based classification for unknown UIs
def classify_by_name(ui_name):
    n = ui_name.lower()
    checks = [
        ('root', 'mainUI', '基础控件'),
        ('timeline', 'mainUI', '基础控件'),
        ('comment', '左-右', '左右布局'),
        ('getsign', '活动打脸弹窗', '弹框类'),
        ('signtip', 'tips', '基础控件'),
        ('notify', '确认弹框', '弹框类'),
        ('earningup', 'tips', '基础控件'),
        ('battleup', 'tips', '基础控件'),
        ('getting', '功能开启&展示', '弹框类'),
        ('promotesucc', '展示-横条-条内信息', '展示横条系列'),
        ('recuittip', 'tips', '基础控件'),
        ('upquality', '使用弹框', '弹框类'),
        ('fashionactive', '活动打脸弹窗', '弹框类'),
        ('getskin', '展示-横条-条内信息', '展示横条系列'),
        ('activeskill', 'tips', '基础控件'),
        ('coatingskill', 'tips', '基础控件'),
        ('common', '使用弹框', '弹框类'),
        ('cyberillusionskill', 'tips', '基础控件'),
        ('cyberillusionsource', '上标题-中竖列表-下信息', '上标题系列'),
        ('daily', 'tips', '基础控件'),
        ('aisle', '上标题-中竖列表-下信息', '上标题系列'),
        ('flyitem', 'tips', '基础控件'),
        ('gm', 'panel', '基础控件'),
        ('beautydispatch', '展示-横条-条内信息', '展示横条系列'),
        ('bell', '展示-横条-条内信息', '展示横条系列'),
        ('bestsell', '展示-横条-条内信息', '展示横条系列'),
        ('ingredents', '展示-横条-条内信息', '展示横条系列'),
        ('beautyskill', '展示-横条-条内信息', '展示横条系列'),
        ('coolingskill', '展示-横条-条内信息', '展示横条系列'),
        ('employertip', '展示-横条-条内信息', '展示横条系列'),
        ('hptip', '展示-横条-条内信息', '展示横条系列'),
        ('supportsucc', '展示-横条-条内信息', '展示横条系列'),
        ('marquee', 'tips', '基础控件'),
        ('mountattr', 'tips', '基础控件'),
        ('npcbubble', 'tips', '基础控件'),
        ('npc', 'tips', '基础控件'),
        ('likability', '展示-横条-条内信息', '展示横条系列'),
        ('propscard', '使用弹框', '弹框类'),
        ('buff', 'tips', '基础控件'),
        ('chat', '左-右', '左右布局'),
        ('skill', 'tips', '基础控件'),
        ('marrysucc', '展示-横条-条内信息', '展示横条系列'),
        ('player', '左-右', '左右布局'),
        ('missionscore', '展示-横条-条内信息', '展示横条系列'),
        ('opening', '功能开启&展示', '弹框类'),
        ('starlevel', 'tips', '基础控件'),
        ('treasure', '展示-横条-条内信息', '展示横条系列'),
        ('bubbl', 'tips', '基础控件'),
        ('target', '上标题-中竖列表-下信息', '上标题系列'),
        ('finish', '展示-横条-条内信息', '展示横条系列'),
        ('main', '上标题-中竖列表-下信息', '上标题系列'),
        ('exam', '上标题-中竖列表-下信息', '上标题系列'),
        ('technoinfo', '上标题-中竖列表-下信息', '上标题系列'),
        ('technostudy', '上标题-中竖列表-下信息', '上标题系列'),
        ('timeline', '左标签+右竖列表', '左标签系列'),
        ('trial', '上标题-中竖列表-下信息', '上标题系列'),
        ('video', '功能开启&展示', '弹框类'),
        ('wait', '登录加载全屏', '全屏类'),
        ('aside', 'tips', '基础控件'),
        ('cp', '活动打脸弹窗', '弹框类'),
        ('newship', '功能开启&展示', '弹框类'),
        ('strengthen', '使用弹框', '弹框类'),
        ('digit', 'tips', '基础控件'),
    ]
    for keyword, type_name, group in checks:
        if keyword in n:
            return type_name, group
    return '待确认（新UI）', '待分类'

# Also load prefab data for additional classification hints
def get_prefab_info(name):
    path = os.path.join(prefab_dir, f'{name}.md')
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'GameObject总数.*?(\d+)', content)
    go_count = int(m.group(1)) if m else 0
    has_wood = 'atlas_common_static' in content
    return {'go_count': go_count, 'has_wood': has_wood}

# Process all images
results = []
for fname in sorted(os.listdir(img_dir)):
    if not fname.endswith('.png') or fname.startswith('__'):
        continue
    ui_name = fname.replace('.png', '')

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
        center = float(np.mean(gray[int(h*0.15):int(h*0.85), int(w*0.15):int(w*0.85)]))
        is_dark = overall_brightness < 40
        lr_diff = round(abs(float(np.mean(gray[:, :w//2])) - float(np.mean(gray[:, w//2:]))), 1)
    except:
        overall_brightness = 0
        borders_dark = False
        center = 0
        is_dark = False
        lr_diff = 0

    if is_dark:
        img_type = "全屏深色"
    elif borders_dark:
        img_type = "有边框面板"
    elif lr_diff > 30:
        img_type = "左右分栏"
    else:
        img_type = "常规面板"

    wiki_info = wiki_map.get(ui_name, None)
    prefab_info = get_prefab_info(ui_name)

    if wiki_info:
        stype = wiki_info['type']
        sgroup = wiki_info['group']
        source = "WIKI"
    else:
        stype, sgroup = classify_by_name(ui_name)
        source = "AI推测"

    results.append({
        'name': ui_name, 'type': stype, 'group': sgroup,
        'source': source, 'prefab': 'Y' if prefab_info else 'N',
        'brightness': overall_brightness, 'img_type': img_type,
        'go_count': prefab_info['go_count'] if prefab_info else 0,
    })

# Write final QA log
log_path = os.path.join(log_dir, 'ui_type_analysis.md')
with open(log_path, 'w', encoding='utf-8') as f:
    f.write("# UI Type Analysis Log\n\n")
    f.write("**Date**: 2026-05-14\n")
    f.write("**Total Images**: {} ({} with wiki entry, {} without)\n\n".format(
        len(results), sum(1 for r in results if r['source']=='WIKI'),
        sum(1 for r in results if r['source']=='AI推测')))

    f.write("## Summary\n\n")
    f.write("| Group | Count | WIKI | AI推测 |\n|-------|-------|------|--------|\n")
    group_data = {}
    for r in results:
        g = r['group']
        if g not in group_data:
            group_data[g] = {'total': 0, 'wiki': 0, 'ai': 0}
        group_data[g]['total'] += 1
        if r['source'] == 'WIKI':
            group_data[g]['wiki'] += 1
        else:
            group_data[g]['ai'] += 1
    for g, d in sorted(group_data.items(), key=lambda x: -x[1]['total']):
        f.write(f"| {g} | {d['total']} | {d['wiki']} | {d['ai']} |\n")
    f.write("\n")

    f.write("## UIs Without Wiki Entry\n\n")
    f.write("| UI Name | Inferred Type | Group | Prefab | GO Count |\n")
    f.write("|---------|--------------|-------|--------|---------|\n")
    for r in results:
        if r['source'] == 'AI推测':
            f.write(f"| {r['name']} | {r['type']} | {r['group']} | {r['prefab']} | {r['go_count']} |\n")
    f.write("\n")

    f.write("## Full Inventory\n\n")
    f.write("| # | UI Name | Type | Group | Source |\n")
    f.write("|---|---------|------|-------|--------|\n")
    for i, r in enumerate(results, 1):
        f.write(f"| {i} | {r['name']} | {r['type']} | {r['group']} | {r['source']} |\n")

print(f"Log: {log_path}")

# Write learning notes
notes_path = os.path.join(log_dir, 'classification_notes.md')
with open(notes_path, 'w', encoding='utf-8') as f:
    f.write("# UI Type Classification Learning Notes\n\n")
    f.write("**Purpose**: Improve accuracy of UI type classification from screenshots\n\n")

    # Collect all WIKI types
    wiki_types = Counter((r['type'], r['group']) for r in results if r['source'] == 'WIKI')

    f.write("## Known Layout Types (from Wiki)\n\n")
    f.write("| # | Type Name | Group | UI Count |\n")
    f.write("|---|-----------|-------|----------|\n")
    for i, ((t, g), c) in enumerate(sorted(wiki_types.items(), key=lambda x: -x[1]), 1):
        f.write(f"| {i} | {t} | {g} | {c} |\n")
    f.write("\n")

    f.write("## Classification Rules by Type\n\n")

    # Group-specific classification rules
    rules = {
        "上标题系列": [
            "特征：顶部有标题栏，中部为列表（竖排或横排），底部有信息/操作区",
            "上标题-中竖列表-下信息：中部列表纵向排列，适合多行条目（92个UI，数量最多）",
            "上标题-中横列表-下信息：中部列表横向排列/网格排列（57个UI）",
            "上标题-中上标签-中竖列表-下信息：标题下方还有标签栏再进行分类（11个UI）",
            "上标题+下横列表：标题+底部横向列表，信息区融合在列表中（2个UI）",
        ],
        "弹框类": [
            "特征：居中弹窗，有遮罩层，内容集中在中央区域",
            "确认弹框：有确认/取消按钮，信息展示+确认操作（87个UI，第二大类型）",
            "活动打脸弹窗：半透明遮罩+中央特殊造型弹框，常用于活动入口/购买（30个UI）",
            "使用弹框：有数量选择/调整功能+使用按钮（24个UI）",
            "功能开启&展示：特效展示型，常含大图/动画预览（14个UI）",
        ],
        "展示横条系列": [
            "特征：横向条状内容单元竖向堆叠排列",
            "展示-横条-条内信息：横条内包含图标+文字+数值等信息（63个UI）",
            "展示-横条-左图-右信息：横条左侧为图片右侧为文字信息（15个UI）",
            "展示-横条-左右对比：横条左右两部分形成对比（11个UI）",
            "展示-横条-横列表：横条横向可滚动排列（7个UI）",
        ],
        "基础控件": [
            "tips：小型提示框，信息简洁（100个UI）",
            "panel：面板式界面，承载功能模块（26个UI）",
            "panel+入口：面板+功能入口链接（13个UI）",
            "mainUI：主界面/主场景UI（8个UI）",
        ],
        "左右布局": [
            "特征：界面左右分区，各自承载不同内容",
            "左-右：左右各约50%的对等分区（36个UI）",
            "左广告图-右列表：左侧大图/立绘，右侧信息列表（13个UI）",
            "左右对比：左右形成视觉/数据对比（8个UI）",
        ],
        "T型布局": [
            "特征：上部标题横跨，下部左右分栏",
            "T型-上标题-左标签-右竖列表：上标题横贯，左标签页导航，右竖向列表（28个UI）",
            "T型-上标题-左-右：上标题横贯，下部左右对等分区（26个UI）",
        ],
        "四边木栏系列": [
            "特征：四边有完整的木栏装饰边框（atlas_common_static.png）",
            "识别要点：检查UI四角是否有木纹理边框",
            "四边木栏（蒸笼标签）底：标签在底部的木栏面板（6个UI）",
            "四边木栏（蒸笼标签）+入口：底部标签+入口链接（2个UI）",
        ],
        "全屏类": [
            "特征：全屏展示，无弹窗效果",
            "全屏背景界面：全屏背景+内容层（12个UI）",
            "登录加载全屏：登录/加载过程中的全屏画面（3个UI）",
            "全屏获得新奖励：全屏展示获得新物品（3个UI）",
        ],
    }

    for group, group_rules in rules.items():
        f.write(f"### {group}\n\n")
        for rule in group_rules:
            f.write(f"- {rule}\n")
        # Count how many in this group
        count = sum(1 for r in results if r['group'] == group)
        f.write(f"\n*本组共 {count} 个UI*\n\n")

    f.write("## Image Feature Patterns\n\n")
    f.write("| Feature | Meaning |\n")
    f.write("|---------|--------|\n")
    f.write("| `four_borders_dark` | 四边都有深色边缘 → 可能是有边框面板 |\n")
    f.write("| `overall_brightness < 40` | 整体很暗 → 全屏界面或深色主题 |\n")
    f.write("| `overall_brightness > 200` | 整体很亮 → 轻量页面/弹窗 |\n")
    f.write("| `lr_diff > 30` | 左右亮度差异大 → 左右分栏布局 |\n")
    f.write("| `center_brightness > 150` | 中心区域亮 → 弹框/面板 |\n\n")

    f.write("## Caution: Known Limitations\n\n")
    f.write("1. 截图无法反映Unity prefab结构细节（如ScrollRect、LayoutGroup等组件）\n")
    f.write("2. 视觉特征分析只能给出粗略分类，不能完全替代prefab结构分析\n")
    f.write("3. 游戏UI普遍使用深色背景+装饰边框，导致\"四边木栏\"误检率高\n")
    f.write("4. 同一UI在不同状态下（有数据/无数据）视觉差异大\n")
    f.write("5. 部分UI类型仅能从功能上区分，视觉结构高度相似\n\n")

    f.write("## Recommended Classification Workflow\n\n")
    f.write("1. **prefab结构分析**（最准确）：检查Image组件的atlas引用、节点层级结构\n")
    f.write("2. **截图视觉分析**（辅助）：看整体布局、分区方式、装饰元素\n")
    f.write("3. **命名约定**：UI功能名通常暗示其类型（Tip→tips, Buy→使用弹框, Rank→列表）\n")
    f.write("4. **交叉验证**：结构+视觉+命名三者交叉，不一致时以prefab结构为准\n")

print(f"Notes: {notes_path}")

---
type: source
source_file: ui_layout_analysis.json
vault_path: D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_layout_analysis.json
size: ~200KB
last_updated: 2026-05-04
created: 2026-05-04
tags: [source, layout-analysis, json]
consumed_by:
  - [[llm_wiki/wiki/concepts/UI_Layout]]
  - [[llm_wiki/wiki/indexes/Index_Layout_Types]]
  - [[llm_wiki/wiki/indexes/Index_Layout_Groups]]
related_sources:
  - [[llm_wiki/sources/all_ui_features]]
  - [[llm_wiki/sources/ui_list]]
---

# Source: ui_layout_analysis.json

## 文件信息

| 属性 | 值 |
|------|-----|
| **路径** | `D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_layout_analysis.json` |
| **大小** | ~200KB |
| **最后更新** | 2026-05-04 |
| **数据类型** | JSON |

## 数据结构

```json
{
  "ui_info": {
    "UI_Achievement": {...},
    "UI_ActArena": {...},
    ...
  },
  "layout_groups": {
    "1280x720": [...]
  },
  "size_stats": {
    "1280x720": 910
  }
}
```

## 主要字段

| 字段 | 说明 |
|------|------|
| `ui_info` | 键为 UI 名称，值为该 UI 的布局信息 |
| `layout_groups` | 按分辨率分组的布局统计 |
| `size_stats` | 各分辨率下的 UI 数量 |

## 被哪些 Wiki 页面消费

- [[llm_wiki/wiki/concepts/UI_Layout]] — UI 布局概念
- [[llm_wiki/wiki/indexes/Index_Layout_Types]] — 布局类型索引
- [[llm_wiki/wiki/indexes/Index_Layout_Groups]] — 布局分组索引

## 使用场景

- 查询某个 UI 的布局分类
- 按分辨率统计 UI 分布
- 布局分组聚合分析

## 最后验证
- **日期**: 2026-05-09
- **状态**: ✅ 有效

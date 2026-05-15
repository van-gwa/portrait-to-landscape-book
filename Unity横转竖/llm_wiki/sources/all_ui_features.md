---
type: source
source_file: all_ui_features.json
vault_path: D:\obsidianProject\portrait-to-landscape\Unity横转竖\all_ui_features.json
size: ~1MB
last_updated: 2026-04-29
created: 2026-05-04
tags: [source, ui-features, json]
consumed_by:
  - [[llm_wiki/wiki/entities/UI_Database]]
related_sources:
  - [[llm_wiki/sources/ui_list]]
  - [[llm_wiki/sources/ui_layout_analysis]]
---

# Source: all_ui_features.json

## 文件信息

| 属性 | 值 |
|------|-----|
| **路径** | `D:\obsidianProject\portrait-to-landscape\Unity横转竖\all_ui_features.json` |
| **大小** | ~1MB |
| **最后更新** | 2026-04-29 |
| **数据类型** | JSON |

## 数据结构

```json
{
  "summary": {
    "total_uis": 1401,
    "feature_stats": {...}
  },
  "all_uis": [
    {
      "ui_name": "UI_ActApexPvp",
      "total_nodes": 68,
      "width": 1379.9,
      "height": 551.7,
      "aspect_ratio": 2.5,
      "x_distribution": "left-center-right",
      "y_distribution": "top:3 mid:55 bot:10",
      "module": "ActApexPvp",
      "path": "D:\\CursorProject\\Dadian - 副本\\..."
    }
  ]
}
```

## 主要字段

| 字段 | 说明 |
|------|------|
| `ui_name` | UI 预制体名称（如 `UI_ActApexPvp`） |
| `total_nodes` | 节点数量 |
| `width` / `height` | 宽高尺寸 |
| `aspect_ratio` | 宽高比 |
| `x_distribution` | X轴分布类型（left-center-right 等） |
| `y_distribution` | Y轴分布（top:3 mid:55 bot:10） |
| `module` | 所属模块 |
| `path` | Unity 预制体文件路径 |

## 被哪些 Wiki 页面消费

- [[llm_wiki/wiki/entities/UI_Database]] — UI 数据库总览
- [[llm_wiki/wiki/concepts/UI_Layout]] — 布局分析
- [[llm_wiki/wiki/guides/UI_Layout_Quick_Judge]] — 快速判断布局类型

## 使用场景

- 按宽高比筛选 UI
- 按节点数量分析复杂度
- 按模块分组统计
- 追溯 UI 的 Unity 路径

## 最后验证
- **日期**: 2026-05-09
- **状态**: ✅ 有效

---
type: concept
created: 2026-05-04
updated: 2026-05-04
tags: [concept, layout-type, layout]
related: [[[llm_wiki/wiki/concepts/UI_Layout]], [[llm_wiki/wiki/concepts/layout-groups/基础控件]], [[llm_wiki/wiki/indexes/Index_Layout_Types]]]
ui_count: 8
group: 基础控件
---

# mainUI

## 定义

该布局通过**mainUI**的空间组织方式，实现内容的有效展示和交互。

## 布局结构

```
┌──────────────────────┐
│    布局内容区      │
│    [item 1]       │
│    [item 2]       │ ↕ 可滚动
│    [item 3]       │
└──────────────────────┘
```

## 主要特征

- 清晰的空间分区方式
- 合理的内容排列逻辑
- 基础控件类型的特征表现

## 包含的 UI（共 8 个）

- [[prefab_final_analysis/UI_TradingPort|UI_TradingPort]]
- [[prefab_final_analysis/UI_VisitMain|UI_VisitMain]]
- [[prefab_final_analysis/UI_StarWorks|UI_StarWorks]]
- [[prefab_final_analysis/UI_MuseumMain|UI_MuseumMain]]
- [[prefab_final_analysis/UI_Market|UI_Market]]
- [[prefab_final_analysis/UI_Main|UI_Main]]
- [[prefab_final_analysis/UI_CombineMain|UI_CombineMain]]
- [[prefab_final_analysis/UI_MountMain|UI_MountMain]]


## 横竖屏适配要点

- 布局在横竖屏转换时需要调整各区域的宽高比
- 关键信息应优先保证可见性
- 可根据屏幕方向调整内容的流向方式

## 所属大类

[[llm_wiki/wiki/concepts/layout-groups/基础控件]]

## 相关资源

- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局总览]]
- [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型完整索引]]

---
type: concept
created: 2026-05-04
updated: 2026-05-04
tags: [concept, layout-type, layout]
related: [[[llm_wiki/wiki/concepts/UI_Layout]], [[llm_wiki/wiki/concepts/layout-groups/特殊玩法]], [[llm_wiki/wiki/indexes/Index_Layout_Types]]]
ui_count: 5
group: 特殊玩法
---

# 横条-VS

## 定义

该布局通过**横条-VS**的空间组织方式，实现内容的有效展示和交互。

## 布局结构

```
┌──────────────────────┐
│  横条展示区        │
│  [Item 内容]       │ ↕ 可竖向滚动
│  ...              │
└──────────────────────┘
```

## 主要特征

- 清晰的空间分区方式
- 合理的内容排列逻辑
- 特殊玩法类型的特征表现

## 包含的 UI（共 5 个）

- [[prefab_final_analysis/UI_TopLeagueReady|UI_TopLeagueReady]]
- [[prefab_final_analysis/UI_InvestmentBidding|UI_InvestmentBidding]]
- [[prefab_final_analysis/UI_MarketWarReady|UI_MarketWarReady]]
- [[prefab_final_analysis/UI_ActApexPvpReady|UI_ActApexPvpReady]]
- [[prefab_final_analysis/UI_BattleBaseStart|UI_BattleBaseStart]]


## 横竖屏适配要点

- 布局在横竖屏转换时需要调整各区域的宽高比
- 关键信息应优先保证可见性
- 可根据屏幕方向调整内容的流向方式

## 所属大类

[[llm_wiki/wiki/concepts/layout-groups/特殊玩法]]

## 相关资源

- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局总览]]
- [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型完整索引]]

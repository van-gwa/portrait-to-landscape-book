---
type: concept
created: 2026-05-04
updated: 2026-05-04
tags: [concept, layout-type, layout]
related: [[[llm_wiki/wiki/concepts/UI_Layout]], [[llm_wiki/wiki/concepts/layout-groups/基础控件]], [[llm_wiki/wiki/indexes/Index_Layout_Types]]]
ui_count: 26
group: 基础控件
---

# panel

## 定义

该布局通过**panel**的空间组织方式，实现内容的有效展示和交互。

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

## 包含的 UI（共 26 个）

- [[prefab_final_analysis/UI_GuildHonorUnLock|UI_GuildHonorUnLock]]
- [[prefab_final_analysis/UI_GuildMemberManager|UI_GuildMemberManager]]
- [[prefab_final_analysis/UI_FirstChargeBonus|UI_FirstChargeBonus]]
- [[prefab_final_analysis/UI_Achievement|UI_Achievement]]
- [[prefab_final_analysis/UI_DailyGift|UI_DailyGift]]
- [[prefab_final_analysis/UI_DailySystem|UI_DailySystem]]
- [[prefab_final_analysis/UI_ExpandAisleMap|UI_ExpandAisleMap]]
- [[prefab_final_analysis/UI_GachaMain|UI_GachaMain]]
- [[prefab_final_analysis/UI_GuildDungeonsList|UI_GuildDungeonsList]]
- [[prefab_final_analysis/UI_GuildLobby|UI_GuildLobby]]
- [[prefab_final_analysis/UI_GuildMsgs|UI_GuildMsgs]]
- [[prefab_final_analysis/UI_GuildManager|UI_GuildManager]]
- [[prefab_final_analysis/UI_GuildHallOfHonor|UI_GuildHallOfHonor]]
- [[prefab_final_analysis/UI_GuildPosition|UI_GuildPosition]]
- [[prefab_final_analysis/UI_GuildParty|UI_GuildParty]]
- [[prefab_final_analysis/UI_GuildWarStreet|UI_GuildWarStreet]]
- [[prefab_final_analysis/UI_GuildGroupBuyNew|UI_GuildGroupBuyNew]]
- [[prefab_final_analysis/UI_MulDayRechargeGift|UI_MulDayRechargeGift]]
- [[prefab_final_analysis/UI_PrivilegeDayCard|UI_PrivilegeDayCard]]
- [[prefab_final_analysis/UI_RechargeGift|UI_RechargeGift]]
- [[prefab_final_analysis/UI_SilkroadRankServerRank|UI_SilkroadRankServerRank]]
- [[prefab_final_analysis/UI_MuseumExhibition|UI_MuseumExhibition]]
- [[prefab_final_analysis/UI_SilkroadBuffEvent|UI_SilkroadBuffEvent]]
- [[prefab_final_analysis/UI_RelayRaceInfo|UI_RelayRaceInfo]]
- [[prefab_final_analysis/UI_AcitveAd|UI_AcitveAd]]
- [[prefab_final_analysis/UI_TrialSpacetime|UI_TrialSpacetime]]


## 横竖屏适配要点

- 布局在横竖屏转换时需要调整各区域的宽高比
- 关键信息应优先保证可见性
- 可根据屏幕方向调整内容的流向方式

## 所属大类

[[llm_wiki/wiki/concepts/layout-groups/基础控件]]

## 相关资源

- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局总览]]
- [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型完整索引]]

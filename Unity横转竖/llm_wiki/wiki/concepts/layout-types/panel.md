---
type: concept
created: 2026-05-04
updated: 2026-05-15
tags: [concept, layout-type, layout, 判断方法]
related: [[llm_wiki/wiki/concepts/UI_Layout]], [[llm_wiki/wiki/concepts/layout-groups/基础控件]], [[llm_wiki/wiki/indexes/Index_Layout_Types]]
ui_count: 26
group: 基础控件
---

# panel

## 定义

panel 是**基础控件中功能面板的统称**——形态多样的功能承载容器，涵盖全屏面板、大半屏面板、居中弹窗面板等。与其他类型的关键区别：panel 是**功能目的明确的功能界面**，非单次弹窗（区别于弹框类），非最小提示（区别于tips）。

## 布局结构

panel 形态多样，主要有三种：

```
【全屏面板型】               【居中弹窗面板型】         【左右分栏面板型】
┌─────────────────┐        ┌─────────────────┐       ┌─────────────────┐
│ 标题栏          │        │  全屏遮罩       │       │ 标题            │
├─────────────────┤        │  ┌───────────┐  │       ├──────┬──────────┤
│                 │        │  │ 标题      │  │       │ 左区 │ 右区     │
│  功能内容区     │        │  │           │  │       │ (列  │ (详情/   │
│                 │        │  │ 功能内容  │  │       │  表/ │  操作)   │
│                 │        │  │           │  │       │  展  │          │
│       [按钮]   │        │  │ [按钮]    │  │       │  示) │          │
└─────────────────┘        │  └───────────┘  │       └──────┴──────────┘
                            └─────────────────┘
```

## 三步判断法（8样本+2验证，盲测2/2通过）

### 第1步：是不是功能面板而非弹窗？

panel 的**存在感比弹窗更持久**——它不是临时弹出的确认/使用/通知，而是用户可以停留操作的**功能页面**。

- 功能面板（可停留操作）→ 可能是 panel
- 一次性弹窗（确认/使用/通知后关闭）→ 考虑弹框类或tips

### 第2步：规模是否大于 tips？

- panel 承载**多项内容**（列表/属性/多按钮/多区域）→ 可能是 panel
- 单一信息焦点 → tips

### 第3步：排除其他特定类型

- 有明确的上中下三段（上标题-中竖列表-下信息）→ 不是 panel
- 有明确的T型标题+左右分栏 → 不是 panel
- 有四边木栏 → 不是 panel
- 排除后剩余的功能面板 → **panel** ✓

---

## 三种形态

### A. 全屏/大半屏面板型（约40%）

直接替换或覆盖主场景的功能界面，通常无遮罩或有轻遮罩。

**典型UI**：UI_GuildLobby、UI_MuseumExhibition、UI_GuildWarStreet、UI_ExpandAisleMap、UI_GachaMain

### B. 居中弹窗面板型（约35%）

带有全屏遮罩的功能弹窗，但内容比弹框类更丰富。

**典型UI**：UI_GuildHonorUnLock、UI_Achievement、UI_PrivilegeDayCard、UI_RechargeGift、UI_DailyGift

### C. 左右分栏面板型（约25%）

左右两栏的功能面板，左侧展示/列表，右侧详情/操作。

**典型UI**：UI_GuildHallOfHonor、UI_GuildMsgs、UI_GuildManager、UI_GuildPosition

---

## 常见混淆类型及区分

### vs tips

| 特征 | panel | tips |
|------|-------|------|
| 规模 | 中大型，多功能 | 极小，单焦点 |
| 交互 | 多按钮/多区域 | 单按钮或无 |
| 停留感 | 可长期停留操作 | 看完就关 |

### vs 确认弹框

| 特征 | panel | 确认弹框 |
|------|-------|---------|
| 目的 | 功能操作 | 二次确认 |
| 按钮 | 多种操作按钮 | 确认+取消/单确认 |

### vs 左-右

| 特征 | panel | 左-右 |
|------|-------|-------|
| 形态 | 多样 | 固定左右两栏 |
| 遮罩 | 不一定 | 多数有 |

---

## 判断口诀

> **功能面板可停留，多项内容聚一框。非弹非tip非T型，基础控件panel当。**

---

## 26个UI分类速查

### A. 全屏/大半屏面板

| # | UI名称 | 内容特征 |
|---|--------|---------|
| 1 | UI_GuildLobby | 商会管理：左信息+右成员列表+底导航 |
| 2 | UI_MuseumExhibition | 博物馆展厅：陈列位+参展要求+按钮 |
| 3 | UI_GuildWarStreet | 城镇地图：等轴街区分佈+底信息栏 |
| 4 | UI_ExpandAisleMap | 关卡选择：左关卡卡+右分类筛选 |
| 5 | UI_GachaMain | 抽卡主界面 |
| 6 | UI_GuildDungeonsList | 商会副本列表 |
| 7 | UI_GuildParty | 商会聚会 |
| 8 | UI_GuildGroupBuyNew | 商会团购 |
| 9 | UI_MulDayRechargeGift | 多日充值礼 |
| 10 | UI_TrialSpacetime | 时空试炼 |

### B. 居中弹窗面板

| # | UI名称 | 内容特征 |
|---|--------|---------|
| 11 | UI_GuildHonorUnLock | 左右分栏：左预览+右属性+确定按钮 |
| 12 | UI_Achievement | 任务达成：图标+进度条+一键领取 |
| 13 | UI_PrivilegeDayCard | 红颜日卡：Banner+奖励详情+领取 |
| 14 | UI_RechargeGift | 每日充值领豪礼：进度+奖励+已领取 |
| 15 | UI_DailyGift | 每日礼包 |
| 16 | UI_FirstChargeBonus | 首充奖励 |
| 17 | UI_SilkroadBuffEvent | 丝路Buff事件 |
| 18 | UI_RelayRaceInfo | 接力赛信息 |

### C. 左右分栏面板

| # | UI名称 | 内容特征 |
|---|--------|---------|
| 19 | UI_GuildHallOfHonor | 左旗帜荣誉室+右组件分类+属性 |
| 20 | UI_GuildMsgs | 商会消息 |
| 21 | UI_GuildManager | 商会管理 |
| 22 | UI_GuildPosition | 商会职位 |
| 23 | UI_GuildMemberManager | 商会成员管理 |
| 24 | UI_SilkroadRankServerRank | 丝路服务器排名 |
| 25 | UI_AcitveAd | 活跃广告 |
| 26 | UI_DailySystem | 日常任务：进度75+任务列表+一键领取 |

---

## 主要特征

- 形态多样（全屏/弹窗/分栏），功能面板的统称
- 内容比 tips 丰富，比弹框类更持久
- 通过排除法判断（非T型/非左-右/非弹框类/非tips）
- 应用场景：商会管理、日常任务、成就系统、充值活动等

## 所属大类

[[llm_wiki/wiki/concepts/layout-groups/基础控件]]

## 相关资源

- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局总览]]
- [[llm_wiki/wiki/concepts/layout-types/tips|tips]]
- [[llm_wiki/wiki/concepts/layout-types/确认弹框|确认弹框]]

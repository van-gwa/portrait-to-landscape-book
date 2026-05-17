---
type: concept
created: 2026-05-04
updated: 2026-05-15
tags: [concept, layout-type, layout, 判断方法]
related: [[llm_wiki/wiki/concepts/UI_Layout]], [[llm_wiki/wiki/concepts/layout-groups/T型布局]], [[llm_wiki/wiki/indexes/Index_Layout_Types]]
ui_count: 26
group: T型布局
---

# T型-上标题-左-右

## 定义

该布局通过**T型结构**：顶部贯穿全宽的标题栏（T的横杠）+ 下方左右两列分区（T的竖杠），实现内容展示与操作。属T型布局大类，共 26 个 UI。

**与「T型-上标题-左标签-右竖列表」的核心区别**：本类型左侧是**通用内容/展示区**（非竖向标签导航），右侧是**通用内容/操作区**（非竖列表）。

## 布局结构

```
┌──────────────────────────────┐
│        标题（贯穿全宽）      │  ← T的横杠：全局水平分割线
├──────────┬───────────────────┤
│          │                   │
│  左区    │      右区         │
│ (展示/   │    (详情/操作)    │
│  选择)   │                   │
│          │                   │
└──────────┴───────────────────┘
```

## 三步判断法（基于8样本+2验证，盲测2/2通过）

### 第1步：顶部有没有贯穿全宽的标题栏？

- 标题**贯穿左右全宽**，形成T字横杠 → 继续
- 标题只在某侧/居中不贯穿 → 不是T型

这是T型最关键的特征，与「左-右」的核心区别。

### 第2步：下面是不是左右两列？

- 左+右两列分区 → 继续
- 三列或单列 → 考虑其他类型

### 第3步：排除左侧标签导航类型

- 左侧是**标签导航**（竖向排列的Tab按钮）→ T型-上标题-左标签-右竖列表
- 左侧是**通用内容**（插画/列表/物品展示）→ **T型-上标题-左-右** ✓

---

## 三种常见子类型

### A. 左展示-右详情（约50%）

左侧展示插画/物品，右侧为文字描述+属性+按钮。
**典型UI**：UI_MuseumAntiqueHistory、UI_MarketLightInfo、UI_CombineAccounting、UI_FuncPreview

### B. 左列表-右操作（约30%）

左侧为可选项列表，右侧为操作区。
**典型UI**：UI_CombinePersonnel、UI_TradingPortDecorateResolve、UI_RouteTradeDispatch

### C. 左信息-右信息（约20%）

左右各展示不同维度信息。
**典型UI**：UI_StarWorksChoiceUp、UI_CombinePublicity、UI_RankActGuildMemberRank

---

## 常见混淆类型及区分

### vs T型-上标题-左标签-右竖列表（最重要！）

| 特征 | T型-上标题-左-右 | T型-上标题-左标签-右竖列表 |
|------|-----------------|--------------------------|
| 左区 | 通用展示/内容 | **竖向标签导航**（Tab按钮） |
| 右区 | 通用详情/操作 | **竖列表**（条目上下滚动） |
| 关键判据 | 左区不切换内容 | 左侧标签点击切换右侧列表 |

### vs 左-右

| 特征 | T型-上标题-左-右 | 左-右 |
|------|-----------------|------|
| 顶部标题 | **贯穿全宽**的T型标题栏 | 可选，通常不贯穿 |

---

## 判断口诀

> **一横贯穿顶全宽，两竖分栏左右看。左非标签右非列，T型左右即此般。**

---

## 26个UI分类速查

| # | UI名称 | 标题 | 左区 | 右区 |
|---|--------|------|------|------|
| 1 | UI_CombineAccounting | 财务部：未开设 | 占位矩形 | 淡墨山水背景 |
| 2 | UI_CombineLeader | (领导部) | — | — |
| 3 | UI_CombineManager | (管理部) | — | — |
| 4 | UI_CombinePersonnel | 部门状态 | 门客招募位+属性 | 升级效果+按钮 |
| 5 | UI_CombinePublicity | 财务部 | 展示区 | 数值说明文字 |
| 6 | UI_CombineTactic | (策略部) | — | — |
| 7 | UI_TradingPortDecorateResolve | 设备分解 | 待选设备网格 | 分解预览+注意事项 |
| 8 | UI_GuildSearchInfo | (商会查找) | — | — |
| 9 | UI_GuildSetFlags | (旗帜设置) | — | — |
| 10 | UI_MarketLightInfo | 业务的名字 | 道具+插画+加成 | 说明+条件+已满级按钮 |
| 11 | UI_MountQueryAttr | (座驾属性) | — | — |
| 12 | UI_MountResolve | (座驾分解) | — | — |
| 13 | UI_MuseumAntiqueHistory | 文物历史 | 青铜大鼎插图+编号 | 文字简介 |
| 14 | UI_TradingPortDeCombine | (贸易港分解) | — | — |
| 15 | UI_RankAct | (榜单活动) | — | — |
| 16 | UI_RouteTradeDispatch | 选择派遣船只 | 船只选择(勾选) | 收益预览+确认派遣 |
| 17 | UI_TechnoCupShow | (技术杯展示) | — | — |
| 18 | UI_TradeWarAddVit | (商战加体力) | — | — |
| 19 | UI_StarWorksChoiceUp | 红颜提升 | 医美提升(容貌值) | 上课提升(涵养值) |
| 20 | UI_StarWorksLevelInfo | (明星等级信息) | — | — |
| 21 | UI_TradingPortDecorateBag | (装饰背包) | — | — |
| 22 | UI_RankActGuildMemberRank | 商会成员排行 | 商会徽章+编号+会长 | 成员排行榜 |
| 23 | UI_FuncPreview | 功能预告 | 风云阁插画 | 解锁条件+简介+产出+按钮 |
| 24 | UI_MarketSurvey | (市场调查) | — | — |
| 25 | UI_GachaLimitWish | (限时许愿) | — | — |
| 26 | UI_ChildSpecifiedPropose | (指定提亲) | — | — |

---

## 主要特征

- T型结构的全局标题栏贯穿全宽
- 下方左右两列分区，无标签导航
- 与T型-上标题-左标签-右竖列表的区别：左侧无Tab标签

## 所属大类

[[llm_wiki/wiki/concepts/layout-groups/T型布局]]

## 相关资源

- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局总览]]
- [[llm_wiki/wiki/concepts/layout-types/T型-上标题-左标签-右竖列表|T型-上标题-左标签-右竖列表]]
- [[llm_wiki/wiki/concepts/layout-types/左-右|左-右]]

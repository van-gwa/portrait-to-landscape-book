---
type: concept
created: 2026-05-04
updated: 2026-05-15
tags: [concept, layout-type, layout, 判断方法]
related: [[llm_wiki/wiki/concepts/UI_Layout]], [[llm_wiki/wiki/concepts/layout-groups/基础控件]], [[llm_wiki/wiki/indexes/Index_Layout_Types]]
ui_count: 13
group: 基础控件
---

# panel+入口

## 定义

「panel+入口」是**信息展示面板 + 核心操作入口按钮**的组合型功能界面——上半部展示状态/数据/信息，右下角有醒目的战斗/挑战/进入入口按钮。属基础控件大类，共13个UI。

**核心判据**：信息面板（数据/状态）+ 明显操作入口（挑战/出战/开战按钮）。

## 布局结构

```
┌──────────────────────────────┐
│  [返回]    标题/进度         │
│                              │
│  ┌────────────────────────┐  │
│  │  信息展示区            │  │
│  │  · 关卡/Boss信息      │  │
│  │  · 战力/属性对比      │  │
│  │  · 角色/部队状态      │  │
│  └────────────────────────┘  │
│                              │
│               ●              │
│          [挑战/出战]         │  ← 核心入口按钮
└──────────────────────────────┘
```

## 三步判断法（5样本+2验证，盲测2/2通过）

### 第1步：是否有信息展示面板？

- 界面主体展示关卡/对手/状态等信息 → 继续
- 纯操作弹窗 → 不是本类型

### 第2步：是否有核心操作入口按钮？

- 右下角或底部有醒目的操作按钮（挑战/出战/开战/匹配）→ 继续

### 第3步：用途是否为"战斗准备/活动入场"？

- 展示信息是为了让玩家决策是否进入战斗/活动 → **panel+入口** ✓

---

## 判断口诀

> **面板展实力数据，右下入口待出击。挑战出战开战键，panel入口即此意。**

## 13个UI速查

| # | UI名称 | 面板内容 | 入口按钮 |
|---|--------|---------|---------|
| 1 | UI_TradeWarBoss | 关卡+攻击力 | 挑战/自动挑战 |
| 2 | UI_TrialSpacetimeTradeWar | 时空商战 | 进入/挑战 |
| 3 | UI_TradePvp | VS+积分+体力 | 匹配对手 |
| 4 | UI_SilkroadMap | 丝路地图+图标 | 活动商店等 |
| 5 | UI_RelayRaceMapUI | 接力赛地图 | 进入 |
| 6 | UI_RankActSpecifyAd | 榜单活动广告 | 前往 |
| 7 | UI_GuildDungeonBattle | 副本信息 | 挑战 |
| 8 | UI_GuildDungeonChallenge | 副本挑战 | 挑战 |
| 9 | UI_GuildDungeonEliteBattle | 精英副本 | 挑战 |
| 10 | UI_ExpandBattle | 对战信息 | 开战 |
| 11 | UI_GuildWarBaseInfo | 商会战信息 | 进入 |
| 12 | UI_Expand | 游历挂机主界面 | 自动游历等 |
| 13 | UI_MarketWarTarget | 店铺实力+角色 | 出战 |

## 所属大类

[[llm_wiki/wiki/concepts/layout-groups/基础控件]]

## 相关资源

- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局总览]]
- [[llm_wiki/wiki/concepts/layout-types/panel|panel]]

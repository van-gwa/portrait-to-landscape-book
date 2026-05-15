---
type: concept
created: 2026-05-04
updated: 2026-05-15
tags: [concept, layout-type, layout, 判断方法]
related: [[llm_wiki/wiki/concepts/UI_Layout]], [[llm_wiki/wiki/concepts/layout-groups/基础控件]], [[llm_wiki/wiki/indexes/Index_Layout_Types]]
ui_count: 100
group: 基础控件
---

# tips

## 定义

tips 是最小粒度的 UI 基础控件——**在纯黑/暗色背景上的轻量级信息提示单元**。它是数量最多的布局类型（100个），涵盖飘字特效、居中卡片提示、系统通知、属性弹窗等多种形态。属基础控件大类。

**命名含义**：tips = 提示/贴士，最小的信息展示单元，"轻、小、简"是其核心特征。

## 布局结构

tips 没有固定的多区域结构，而是**单焦点、单信息块**：

```
┌──────────────────────────┐
│      纯黑/暗色背景      │
│                          │
│    ┌──────────────┐      │
│    │ 图标/文字     │      │  ← 单一信息焦点
│    │ 简短信息      │      │
│    └──────────────┘      │
│                          │
└──────────────────────────┘
```

## 三步判断法（基于100个UI图片分析）

### 第1步：背景是不是纯黑/暗色？

主体内容是否浮在**纯黑或半透明暗色背景**之上？
- 是 → 继续（几乎所有 tips 类 UI 满足）
- 否 → 不是 tips

这是 tips 最显著的视觉特征——它们**不是全屏页面，也不是半屏弹窗**，而是浮在黑暗中的独立信息块。

### 第2步：内容是不是单一焦点？

UI 是否围绕**一个核心信息**展开（一件物品、一条通知、一条规则、一个数值）？
- 只有一个焦点 → 继续
- 有多个并列区域（如列表、多标签页） → 考虑其他类型

### 第3步：是否是极简交互？

交互是否极简（通常只有"确认/关闭"，或完全无交互）？
- 是（纯展示或单一按钮） → **tips** ✓
- 有复杂交互（多按钮、输入、选择） → 考虑确认弹框/使用弹框

---

## 六种子类型

### A. 飘字特效型（约25%，纯黑图）

**命名特征**：Fly（飞行）、Float（飘浮）类
**典型UI**：UI_FlyItem、UI_FlyItem1、UI_FlyItem2、UI_FloatCoinTips、UI_FloatMoneyTips、UI_FloatStrTip
**特征**：运行时的动画特效（金币飘出、经验飘字），截图中显示为纯黑/空白。
**判断**：UI名含 Fly/Float/Coin/Money → 飘字特效型 tips

### B. 居中卡片提示型（约30%，最常见可截图类）

**特征**：黑底中央显示一张浅黄/羊皮纸质感的信息卡片，内容为单一物品详情/属性/获取途径。
**典型UI**：UI_ItemTip、UI_ExpandSidInfo、UI_MultiAwardItemTips、UI_GuestPath、UI_GetPaths2、UI_GetPaths3
**典型内容**：物品图标+名称+数量+属性描述

### C. 系统通知型（约15%）

**特征**：系统层面的通知/提示，如每日刷新、事件完成、错误提示。
**典型UI**：UI_DailyRefreshTips（代办已发布）、UI_HistoryStageTip（主线事件完成）、UI_NetError（网络错误）、UI_FuncUnlock（功能解锁）

### D. 成就/收集展示型（约10%）

**特征**：单件物品/奖杯的仪式感展示，通常有装饰性边框或横幅。
**典型UI**：UI_CupGetting（小当家奖杯）、UI_CupInfo、UI_GoodsActive、UI_BattlePassUpgradeAni（通行证升级动画）

### E. 属性/详情弹窗型（约10%）

**特征**：黑底上的属性/数据详情面板，展示数值/加成等。
**典型UI**：UI_MainPowerDetail（赚速详情）、UI_GuestAttrUpTip、UI_MarketStrength、UI_BeautyTalentSkillTips

### F. 引导/规则说明型（约10%）

**特征**：黑底上展示规则/引导文字，古风纸质面板。
**典型UI**：UI_RuleTip、UI_Guide、UI_SilkroadRetreatRuleTip（援兵规则）、UI_AgreementDesc（权限说明）、UI_PreviewAwards（奖励预览）

---

## 常见混淆类型及区分

### vs 确认弹框

| 特征 | tips | 确认弹框 |
|------|------|---------|
| 交互 | 极简（关闭/确认，或零交互） | 双按钮（确认+取消） |
| 背景 | 纯黑 | 可能有半透明遮罩 |
| 焦点 | 单一信息块 | 问题+选项 |

### vs 展示-横条-条内信息

| 特征 | tips | 展示-横条-条内信息 |
|------|------|-------------------|
| 规模 | 最小（原子级） | 中等（弹窗级） |
| 装饰 | 无/极少 | 艺术字标题+丝带飘带 |
| 内容量 | 极简（单条消息） | 多条信息（奖励列表+说明） |
| 背景 | 纯黑 | 半透明场景遮罩 |

**一句话区分**：tips 是"暗室中的小灯泡"，展示-横条-条内信息是"舞台上的横幅"。

### vs 活动打脸弹窗

| 特征 | tips | 活动打脸弹窗 |
|------|------|-------------|
| 目的 | 信息通知 | 营销转化 |
| 元素 | 简单 | 立绘+倒计时+折扣+¥购买按钮 |
| 尺寸 | 小 | 大 |

### vs panel

| 特征 | tips | panel |
|------|------|-------|
| 背景 | 纯黑 | 可能有游戏场景 |
| 用途 | 临时提示 | 常驻面板/组件 |

---

## 判断口诀

> **黑底浮窗单焦点，图标文字极简言。无框无栏无多区，轻量提示即 tips。**

---

## 100个UI分类速查

### A. 飘字特效型（纯黑截图）

| # | UI名称 | 判断依据 |
|---|--------|---------|
| 1 | UI_FlyItem | 飘物特效 |
| 2 | UI_FlyItem1 | 飘物特效 |
| 3 | UI_FlyItem2 | 飘物特效 |
| 4 | UI_FloatCoinTips | 飘币提示 |
| 5 | UI_FloatMoneyTips | 飘钱提示 |
| 6 | UI_FloatStrTip | 飘字提示 |
| 7 | UI_FullSceneTips | 全场景提示 |
| 8 | UI_GoodsActive | 物品激活特效 |
| 9 | UI_GuestPromoteItem | 门客提升物品特效 |
| 10 | UI_RoleUpTip | 角色升级提示特效 |
| 11 | UI_PrivilegeMonthlyCard2 | 月卡特效 |
| 12 | UI_BattlePassUpgradeAni | 通行证升级动画 |
| 13 | UI_StarWorksUpAni | 明星作品升级动画 |
| 14 | UI_FashionShopEff | 时装商店特效 |
| 15 | UI_FundGuestInfo | 基金门客信息浮层 |
| 16 | UI_FundBeautyInfo | 基金红颜信息浮层 |
| 17 | UI_RelayTrainRwd | 接力训练奖励飘字 |
| 18 | UI_ResAddition | 资源加成提示 |
| 19 | UI_ShopUnlockTips | 商店解锁提示 |
| 20 | UI_GachaLuckTips | 抽卡幸运提示 |
| 21 | UI_MarketWarTea | 商战茶话 |
| 22 | UI_GuestRareTip | 门客稀有提示 |
| 23 | UI_DivineTip | 占卜提示 |
| 24 | UI_TradeWarItem | 商战物品提示 |
| 25 | UI_RankActAddTip | 榜单活动附加提示 |

### B. 居中卡片提示型

| # | UI名称 | 内容 |
|---|--------|------|
| 26 | UI_ItemTip | 物品详情卡片（图标+名称+数量） |
| 27 | UI_ExpandSidInfo | 探索支线信息 |
| 28 | UI_MultiAwardItemTips | 多奖励物品详情 |
| 29 | UI_GuestPath | 门客提升攻略卡片 |
| 30 | UI_GetPaths2 | 获取途径卡片 |
| 31 | UI_GetPaths3 | 获取途径卡片 |
| 32 | UI_GuestATKUpPath | 门客攻击提升途径 |
| 33 | UI_GuestSupplyPath | 门客补给途径 |
| 34 | UI_GuestSupplyRecords | 门客补给记录 |
| 35 | UI_ExpandEventTip | 探索事件提示 |
| 36 | UI_RecruitTips | 招募提示（庖丁角色+数字） |
| 37 | UI_RecruitProgressTips | 招募进度提示（纳贤目标完成） |
| 38 | UI_StreetFightAttrTip | 街头战斗属性提示 |
| 39 | UI_TechnoCourseTip | 技术课程提示 |
| 40 | UI_TechnoTips | 技术提示 |
| 41 | UI_BeautyTalentSkillTips | 红颜天赋技能提示 |
| 42 | UI_TitleTips | 称号提示 |
| 43 | UI_MarketFacilityTip | 商铺设施提示 |
| 44 | UI_CyberIllusionEquipMessage | 赛博幻境装备信息 |
| 45 | UI_ChildCultivateVit | 子嗣培养体力提示 |
| 46 | UI_CommonSkin | 通用皮肤 |
| 47 | UI_BeautyTravelTip | 红颜同游提示 |
| 48 | UI_TaskProgressTip | 任务进度提示 |
| 49 | UI_SeaEvidenceTip | 海域证据提示 |
| 50 | UI_MarketRepresentAdd | 商铺代表加成 |
| 51 | UI_GuildWarProtactTips | 商会战保护提示 |
| 52 | UI_InvestmentSkillAddition | 投资技能加成 |
| 53 | UI_TopLeagueDesc | 顶级联赛说明 |
| 54 | UI_ActApexPvpDesc | 尖峰PVP说明 |
| 55 | UI_BanquetAddTips | 宴会加成提示 |

### C. 系统通知型

| # | UI名称 | 内容 |
|---|--------|------|
| 56 | UI_DailyRefreshTips | 新代办已发布（卡通猫通知） |
| 57 | UI_HistoryStageTip | 主线事件完成 |
| 58 | UI_NetError | 网络错误提示+卡通图 |
| 59 | UI_FuncUnlock | 功能解锁提示 |
| 60 | UI_AgeTips | 时代提示 |
| 61 | UI_HistoryStageLock | 历史阶段锁定提示 |
| 62 | UI_YardDispachResult | 宅院派遣结果 |
| 63 | UI_SilkroadBuffEventResult | 丝路Buff事件结果 |
| 64 | UI_SilkroadQucikTeleport | 丝路快速传送提示 |
| 65 | UI_ExpandMapNewTip | 发现神秘商道 |
| 66 | UI_ExpandNameTip | 外贸区场景标签 |
| 67 | UI_GuildDunExpReward | 商会副本经验奖励 |
| 68 | UI_GuildEliteAttackUp | 商会精英攻击提升 |
| 69 | UI_GuildPartyPreview | 商会聚会预览 |
| 70 | UI_VisitPlayerTitle | 访问玩家称号 |

### D. 成就/收集展示型

| # | UI名称 | 内容 |
|---|--------|------|
| 71 | UI_CupGetting | 小当家全美食指南奖杯 |
| 72 | UI_CupInfo | 奖杯信息 |
| 73 | UI_RedPacketOpen | 红包开启展示 |
| 74 | UI_RedPacketSetting | 红包设置 |
| 75 | UI_RouteTradeItem | 航线贸易物品展示 |
| 76 | UI_MarketWarTactic | 商战策略等级（传奇图标） |
| 77 | UI_MarketChild | 商铺子嗣 |
| 78 | UI_PlayerSkinPreview | 门客皮肤预览（坊间采风） |
| 79 | UI_TalkReview | 对话回顾（膳祖） |

### E. 属性/详情弹窗型

| # | UI名称 | 内容 |
|---|--------|------|
| 80 | UI_MainPowerDetail | 赚速详情（3360万/10.5亿） |
| 81 | UI_GuestAttrUpTip | 装备属性（腐蚀概率99.99万） |
| 82 | UI_MarketStrength | 商铺实力详情 |
| 83 | UI_MarketActiveAdvanced | 商铺激活高级详情 |
| 84 | UI_InvestmentRecord | 投资记录 |
| 85 | UI_InvestmentUnlock | 投资解锁详情 |
| 86 | UI_FundPreview | 基金预览 |
| 87 | UI_GuildColorCodeDesc | 商会颜色码说明 |
| 88 | UI_TradingPortSupplyLvUnlock | 贸易港补给等级解锁 |

### F. 引导/规则说明型

| # | UI名称 | 内容 |
|---|--------|------|
| 89 | UI_RuleTip | 规则说明空白界面 |
| 90 | UI_Guide | 对话引导文字 |
| 91 | UI_SilkroadRetreatRuleTip | 援兵规则（官宴自动开启） |
| 92 | UI_AgreementDesc | 权限说明古风框 |
| 93 | UI_PreviewAwards | 奖励预览（时空助力银两） |
| 94 | UI_BeautyEditor | 语音随机播放设置 |
| 95 | UI_GuildSetting | 商会旗帜设置（天） |
| 96 | UI_RelayRaceTab | 接力赛Tab |
| 97 | UI_RelayTrainUpPath | 接力训练提升途径 |
| 98 | UI_StreetTreasureList | 街头宝藏列表 |
| 99 | UI_MarketSkinLook | 商铺皮肤查看 |
| 100 | UI_PirateEvent | 海盗事件提示 |

---

## 主要特征

- 最小粒度的 UI 单元（原子级控件）
- 99% 在纯黑/暗色背景上
- 单一信息焦点，极简交互
- 涵盖：飘字特效、居中卡片、系统通知、成就展示、属性详情、规则引导
- 与弹框类的区别：更轻、更小、更临时

## 所属大类

[[llm_wiki/wiki/concepts/layout-groups/基础控件]]

## 相关资源

- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局总览]]
- [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型完整索引]]
- [[llm_wiki/wiki/concepts/layout-types/panel|panel]]
- [[llm_wiki/wiki/concepts/layout-types/确认弹框|确认弹框]]

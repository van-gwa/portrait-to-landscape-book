# 背景图分析总结

**分析时间**: 2026-05-01  
**数据来源**: background_image_list.md  
**筛选条件**: 宽度 >= 700px + UI_开头的预制体  
**保留界面数**: 716 个

---

## 📊 核心数据

| 指标 | 数值 |
|------|------|
| 总独特的 (图片, 尺寸) 组合 | 564 |
| 被多次使用的组合数 | 80 |
| 不同尺寸规格 | 470+ |

---

## 🔥 Top 10 最常复用的背景图

这些背景图和尺寸组合被多个界面共用，是最值得关注的复用机会。

### 1. **ui_common_bg_0018.png** (1040.0×604.0)
- **使用次数**: 20次
- **使用界面**:
  - [[UI_Bag]], [[UI_Beauty]], [[UI_BeautyInfo]], [[UI_BeautyShow]]
  - [[UI_ChildFamily]], [[UI_ChildInfo]], [[UI_ChildSchool]]
  - [[UI_GrowSystem]], [[UI_Guest]], [[UI_GuestInfo]], [[UI_GuestNotActive]]
  - [[UI_InvestmentMain]], [[UI_MountBuildInfo]], [[UI_MountInfo]]
  - [[UI_MuseumGachaShop]], [[UI_OtherRoleGuest]]
  - [[UI_StarWorksChoiceBeauty]], [[UI_TradeWar]], [[UI_TradeWarBattle]]
  - [[UI_TradingPortDock]]

### 2. **ui_common_bg_0018.png** (1048.1×600.2)
- **使用次数**: 11次
- **使用界面**:
  - [[UI_BanquetMain]], [[UI_GachaCoinShop]], [[UI_GuildDungeonsNew]]
  - [[UI_GuildList]], [[UI_GuildMain]], [[UI_MuseumAntiqueList]]
  - [[UI_RankGobal]], [[UI_RankLocal]], [[UI_RoleBeautyTip]]
  - [[UI_RoleGuestsTip]], [[UI_TradingPortFleet]]

### 3. **atlas_common_static.png** (1112.0×615.0)
- **使用次数**: 10次
- **使用界面**:
  - [[UI_ActApexPvpBattle]], [[UI_ActKingOfSnowBattle]], [[UI_GuildMemberBattle]]
  - [[UI_GuildWarBattle]], [[UI_InvestmentBattle]], [[UI_MarketWarBattle]]
  - [[UI_MarketWarBeautySkill]], [[UI_PirateFightBattle]]
  - [[UI_StreetFightBattle]], [[UI_TopLeagueBattle]]

### 4. **ui_common_bg_0052.png** (803.0×544.0)
- **使用次数**: 8次
- **使用界面**:
  - [[UI_BagComposeTips]], [[UI_DailySignBadInfo]], [[UI_GuestSupplyRecords]]
  - [[UI_GuildApply]], [[UI_GuildSameNameSetting]], [[UI_TradingPortSupplyInfo]]
  - [[UI_TradingPortSupplyRecords]], [[UI_YardRankTips]]

### 5. **ui_common_bg_0052.png** (880.1×623.2)
- **使用次数**: 5次
- **使用界面**:
  - [[UI_ActApexPvpReward]], [[UI_ActivityRank]], [[UI_RankActReward]]
  - [[UI_RelayRankDetail]], [[UI_TopLeagueReward]]

### 6. **ui_zs_dit19.png** (1028.0×578.0)
- **使用次数**: 5次
- **使用界面**:
  - [[UI_ChildPublicPropose]], [[UI_ChildSpecialSuitors]], [[UI_ChildSpecifiedPropose]]
  - [[UI_ChildSuitors]], [[UI_ChildWaitPropose]]

### 7. **ui_common_bg_0052.png** (967.1×525.5)
- **使用次数**: 4次
- **使用界面**:
  - [[UI_ActApexPvpRank]], [[UI_PurchaseBattleRank]], [[UI_RankActRewardGuild]]
  - [[UI_TopLeagueBetRank]]

### 8. **ui_common_hdbg_0093_1.png** (1124.0×375.0)
- **使用次数**: 4次
- **使用界面**:
  - [[UI_ActSnowWheelResult]], [[UI_BanquetFinish]], [[UI_CommonGetItems]]
  - [[UI_GuestStarSucc]]

### 9. **ui_syj_bg_1.png** (1271.0×621.0)
- **使用次数**: 4次
- **使用界面**:
  - [[UI_CyberPve]], [[UI_PirateServerBoss]], [[UI_StreetFight]]
  - [[UI_WorldWonders]]

### 10. **ui_common_hdbg_0093_1.png** (1024.0×302.6)
- **使用次数**: 3次
- **使用界面**:
  - [[UI_ActApexPvpResult]], [[UI_GuildPartyResult]], [[UI_TopLeagueResult]]

---

## 📐 尺寸标准化分析

### 最常见的尺寸标准

**尺寸 1040.0×604.0 (最常用)**
- 20张同尺寸背景
- 主要用于通用主界面背景
- 高度复用率

**尺寸 1048.1×600.2**
- 11张同尺寸背景  
- 与上述尺寸接近，用于相似功能

**尺寸 1112.0×615.0**
- 10张同尺寸背景
- 用于战斗界面、排行榜等内容展示

**其他常见尺寸**
- 803.0×544.0 - 8次使用
- 880.1×623.2 - 5次使用
- 1028.0×578.0 - 5次使用

---

## 💡 关键发现

1. **集中度高**: Top 10的背景图组合包含了所有多次使用组合中的大部分
2. **常用背景趋势**:
   - `ui_common_bg_0018.png`: 通用主界面背景（两个略微不同的尺寸，共31次）
   - `ui_common_bg_0052.png`: 通用弹窗/信息框背景（多种尺寸）
   - `atlas_common_static.png`: 通用UI组件背景（10次）
3. **横屏化建议**:
   - 优先处理被多次使用的背景（复用率高）
   - 按尺寸标准化分组处理
   - 关注 Top 3 的背景图对整体收益最大

---

## 🎯 后续建议

1. **优先级处理**:
   - 第一优先: ui_common_bg_0018.png 系列（共31次） → 收益最大
   - 第二优先: ui_common_bg_0052.png 系列（多种尺寸，多次使用）
   - 第三优先: atlas_common_static.png（10次）

2. **测试重点**:
   - 验证 Top 3 背景图的横屏转竖版效果
   - 检查多个尺寸版本的适配性
   - 对比竖屏原版和横屏转竖版的视觉效果

3. **数据维护**:
   - 当前文件已过滤掉所有宽度<700的界面
   - 已移除所有非UI_开头的预制体
   - 保留716个有效UI界面用于横屏转竖版

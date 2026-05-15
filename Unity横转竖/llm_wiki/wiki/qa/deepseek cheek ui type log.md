# DeepSeek UI 类型检查日志

> 创建时间: 2026-05-14
> 数据来源: D:\CursorProject\Dadian - 副本\Arts\Assets\Doc\UIImage\__filelist.txt (974 张图片)
> Wiki 类型来源: llm_wiki/wiki/concepts/layout-types/ (892 个 UI, 62 种布局类型)
> 特征数据来源: all_ui_features.json (1401 个 UI 的 prefab 节点结构数据)
> 分析方法: 基于 prefab 结构特征（节点数/宽高/XY分布）进行统计异常检测 (z-score > 2.5)
> 注意: 当前模型不支持直接图片视觉分析，分析基于 prefab 导出的结构数据。标记为异常的需要人工通过截图复核。

---

## 统计总览

| 指标 | 数值 |
|------|------|
| 文件清单总数 | 974 |
| 有效对比总数 | 973 |
| 有 Wiki 类型 | 891 |
| 无 Wiki 类型（仅图片） | 82 |
| 无特征数据 | 1 |
| 统计异常 (z>2.5) | 81 |
| Wiki 类型数 | 62 |

---

## 各 Wiki 类型的特征画像

以下是每种 wiki 类型的结构特征画像（均值 ± 标准差），用于判断新 UI 是否符合该类型：

| 类型 | 数量 | 宽 | 高 | 节点数 | Left | Center | Right | Top | Mid | Bot | List% | Bg% |
|------|------|-----|-----|--------|------|--------|-------|-----|-----|-----|-------|-----|
| tips | 99 | 349.2 ± 231.6 | 266.9 ± 165.2 | 14.4 ± 10.2 | 1.9 ± 1.4 | 10.7 ± 9.5 | 1.9 ± 1.5 | 1.9 ± 1.2 | 10.5 ± 9 | 2.1 ± 1.4 | 42% | 11% |
| 上标题-中竖列表-下信息 | 92 | 742.7 ± 366.1 | 392.6 ± 136.4 | 25.7 ± 8.5 | 3 ± 1.7 | 19.7 ± 7.2 | 3.1 ± 1.7 | 2.5 ± 1.3 | 21.4 ± 7.6 | 1.9 ± 1.4 | 96% | 16% |
| 确认弹框 | 87 | 348.7 ± 193.6 | 322.8 ± 94 | 17.1 ± 7 | 1.5 ± 1.1 | 13.6 ± 6.2 | 2 ± 1.4 | 1.9 ± 1 | 12.9 ± 5.8 | 2.3 ± 1.1 | 28% | 16% |
| 展示-横条-条内信息 | 63 | 590.5 ± 215.2 | 455.9 ± 141.7 | 24 ± 10.7 | 2.4 ± 1.3 | 18.8 ± 8.9 | 2.8 ± 1.9 | 2.6 ± 1.6 | 18.9 ± 9.5 | 2.6 ± 1.6 | 60% | 59% |
| 上标题-中横列表-下信息 | 57 | 568 ± 275.1 | 409.1 ± 101.3 | 29.6 ± 14.2 | 1.9 ± 1.2 | 25.7 ± 12.5 | 2.1 ± 1.8 | 3.1 ± 1.8 | 22.8 ± 11.4 | 3.7 ± 2.5 | 96% | 12% |
| 左-右 | 36 | 738.2 ± 264.1 | 471.9 ± 167.3 | 39.9 ± 18.7 | 4.5 ± 2.6 | 30.7 ± 17.4 | 4.6 ± 2.4 | 3.7 ± 2.5 | 32 ± 16.2 | 4.2 ± 2.7 | 78% | 33% |
| 活动打脸弹窗 | 30 | 697.8 ± 259.3 | 459.8 ± 170.6 | 30.6 ± 19 | 2.3 ± 1.9 | 25.3 ± 16.6 | 2.9 ± 1.7 | 2.8 ± 1.8 | 23.9 ± 17.8 | 3.8 ± 1.9 | 53% | 23% |
| T型-上标题-左标签-右竖列表 | 28 | 876.2 ± 195.4 | 426 ± 120.5 | 40.2 ± 12.2 | 3.4 ± 2.4 | 33.2 ± 10.3 | 3.6 ± 2 | 3 ± 2 | 35 ± 10.8 | 2.2 ± 1.4 | 96% | 18% |
| panel | 26 | 836.8 ± 196.7 | 484.1 ± 128.7 | 35.2 ± 17.7 | 3.5 ± 2.8 | 28.1 ± 14 | 3.7 ± 2.9 | 3.8 ± 3.1 | 27.5 ± 14.2 | 3.9 ± 2.4 | 85% | 23% |
| T型-上标题-左-右 | 26 | 635.8 ± 138.2 | 426.6 ± 70.5 | 34.2 ± 10.7 | 3.7 ± 2.4 | 25.7 ± 10.1 | 4.8 ± 2.3 | 4.1 ± 1.9 | 26.2 ± 9.3 | 3.8 ± 2.1 | 81% | 8% |
| 使用弹框 | 24 | 499 ± 47.4 | 404 ± 96.8 | 24 ± 5.2 | 2.4 ± 1.3 | 19 ± 4 | 2.7 ± 1.2 | 2.5 ± 1 | 19 ± 4.8 | 2.5 ± 1.7 | 42% | 0% |
| 一体框 | 22 | 731.7 ± 251.1 | 458.3 ± 141.6 | 39.1 ± 35 | 3.3 ± 2.1 | 32.5 ± 32.3 | 3.3 ± 3.1 | 3.4 ± 2.2 | 32.4 ± 31.9 | 3.3 ± 2.2 | 64% | 36% |
| 展示-横条-左图-右信息 | 15 | 825.2 ± 214.7 | 569.4 ± 221.3 | 28.3 ± 12.1 | 4.3 ± 1.9 | 20.8 ± 10.4 | 3.2 ± 1.2 | 2.7 ± 1 | 21.9 ± 11.4 | 3.6 ± 1.3 | 67% | 67% |
| 红框方形玩法入口 | 15 | 1031.4 ± 364 | 657.4 ± 238.2 | 54.7 ± 21.4 | 3.6 ± 1.9 | 46.5 ± 19.2 | 4.5 ± 2.2 | 5.3 ± 2.4 | 44.9 ± 21.1 | 4.4 ± 2 | 60% | 60% |
| 功能开启&展示 | 14 | 385.1 ± 242.8 | 328.8 ± 127.8 | 10.6 ± 3.5 | 1.2 ± 1 | 7.9 ± 3.5 | 1.5 ± 0.7 | 1.3 ± 0.5 | 7.5 ± 3.8 | 1.8 ± 0.8 | 14% | 14% |
| 左艺术设计+左-右 | 14 | 913.6 ± 147.7 | 496.9 ± 159.7 | 43.1 ± 18.4 | 3.1 ± 1.8 | 35.6 ± 15.5 | 4.4 ± 2.8 | 3.4 ± 1.9 | 34.9 ± 15.6 | 4.8 ± 2.2 | 86% | 0% |
| 左标签+右竖列表 | 14 | 980.7 ± 421.7 | 417 ± 109.9 | 45 ± 18.3 | 3.9 ± 2.6 | 36.9 ± 16 | 4.3 ± 2.7 | 4.4 ± 2.6 | 36.4 ± 14.7 | 4.2 ± 2.6 | 100% | 36% |
| 横列表 | 13 | 656.5 ± 477.4 | 515.4 ± 111 | 30.2 ± 16.1 | 2.4 ± 1.5 | 25.6 ± 15.2 | 2.2 ± 1.7 | 2.3 ± 1 | 25.1 ± 15.9 | 2.8 ± 1.2 | 92% | 8% |
| 左广告图-右列表 | 13 | 784.7 ± 215.5 | 439.2 ± 106.7 | 33.4 ± 13.6 | 4.5 ± 3.4 | 25.6 ± 11.6 | 3.2 ± 1.6 | 3.6 ± 1.7 | 25.5 ± 10.7 | 4.3 ± 3.4 | 92% | 15% |
| panel+入口 | 13 | 1268.9 ± 683.1 | 590.4 ± 70.6 | 60.8 ± 24.9 | 5.1 ± 2.9 | 50.5 ± 28.6 | 5.2 ± 3.8 | 5.8 ± 2.8 | 48.2 ± 25.4 | 6.8 ± 2.6 | 62% | 15% |
| 全屏背景界面 | 12 | 788.7 ± 350.1 | 503 ± 183.9 | 35.9 ± 37.3 | 2.1 ± 2.3 | 30.9 ± 32.5 | 2.9 ± 3.4 | 3.6 ± 4.3 | 28.2 ± 28.5 | 4.2 ± 4.9 | 50% | 17% |
| 上标题-中上标签-中竖列表-下信息 | 11 | 753.9 ± 310.6 | 399.3 ± 94.2 | 38.2 ± 13.1 | 4.6 ± 2 | 29.6 ± 10.6 | 3.9 ± 2.7 | 3.5 ± 1.4 | 32.3 ± 11.2 | 2.4 ± 1.4 | 100% | 0% |
| 四边木栏（蒸笼标签）+左中右 | 11 | 1020.5 ± 109 | 543.1 ± 62.9 | 87.7 ± 47.2 | 6.7 ± 3.6 | 69.6 ± 36.4 | 11.4 ± 8.9 | 10.5 ± 6.2 | 67.1 ± 34.7 | 10.2 ± 7.3 | 100% | 27% |
| 展示-横条-左右对比 | 11 | 639.3 ± 206.1 | 482.5 ± 111.5 | 20.1 ± 4 | 2.2 ± 1 | 16 ± 3.8 | 1.9 ± 1.2 | 2.4 ± 1.4 | 15.5 ± 3.9 | 2.3 ± 0.6 | 27% | 64% |
| 四边木栏（蒸笼标签）+横列表 | 9 | 954.6 ± 227.8 | 512.7 ± 100.6 | 36.2 ± 16.8 | 3.8 ± 1.2 | 29.1 ± 13.9 | 3.3 ± 2.4 | 4.8 ± 1.6 | 26.2 ± 12.8 | 5.2 ± 3.6 | 100% | 0% |
| 战斗 | 9 | 1151.7 ± 138 | 713.5 ± 183.3 | 86 ± 10.3 | 2.7 ± 2.1 | 78.3 ± 6.7 | 5 ± 2.2 | 6.1 ± 1.9 | 74 ± 11.2 | 5.9 ± 3 | 100% | 0% |
| 左右对比 | 8 | 582.9 ± 202.9 | 472.3 ± 92.9 | 27.6 ± 9.5 | 3 ± 1.2 | 20.9 ± 7.5 | 3.8 ± 1.9 | 3.2 ± 1.1 | 20.9 ± 9 | 3.5 ± 0.7 | 62% | 12% |
| mainUI | 8 | 930.9 ± 292.9 | 337 ± 138.2 | 46.9 ± 38.3 | 3.2 ± 1.4 | 41.4 ± 38 | 2.2 ± 1.7 | 3.4 ± 2.6 | 40.8 ± 35 | 2.8 ± 2.2 | 50% | 0% |
| 待确认 | 8 | 691.5 ± 366.6 | 438.8 ± 223.2 | 44.1 ± 46.8 | 3.6 ± 4 | 37.2 ± 41 | 3.2 ± 2.9 | 4.6 ± 6.1 | 36.5 ± 38.5 | 3 ± 3.2 | 75% | 50% |
| 展示-横条-横列表 | 7 | 631 ± 220.3 | 489.4 ± 141.3 | 23.3 ± 9.3 | 1.7 ± 0.9 | 19.7 ± 8.3 | 1.9 ± 0.8 | 1.9 ± 1.5 | 19.1 ± 10.6 | 2.3 ± 1 | 100% | 57% |
| 左标签页-右框内-上标题-中竖列表-下信息 | 7 | 961.1 ± 187.9 | 484.6 ± 52.2 | 42.1 ± 17.6 | 4.6 ± 2.3 | 34.1 ± 14.1 | 3.4 ± 1.9 | 4.6 ± 1.8 | 34.1 ± 16.8 | 3.4 ± 1.4 | 100% | 14% |
| 大背景-展示 | 7 | 652.9 ± 218.5 | 478.8 ± 79 | 25.3 ± 9.1 | 2.1 ± 0.8 | 20.3 ± 7.9 | 2.9 ± 2 | 2.1 ± 1 | 18.4 ± 6.3 | 4.7 ± 2.8 | 14% | 14% |
| 左标签+中图+右信息 | 6 | 875.6 ± 119.5 | 515 ± 42.7 | 37.7 ± 10.5 | 3.7 ± 1.8 | 29.3 ± 8.3 | 4.7 ± 2.4 | 4 ± 1.3 | 28.8 ± 9.9 | 4.8 ± 0.9 | 83% | 50% |
| 四边木栏（蒸笼标签）底 | 6 | 898.2 ± 202.3 | 499.4 ± 109.8 | 38.2 ± 15 | 3.8 ± 0.9 | 30.2 ± 13.4 | 4.2 ± 3.2 | 4.7 ± 1.5 | 28.3 ± 11.4 | 5.2 ± 2.8 | 50% | 33% |
| 左标签-右信息 | 5 | 1014 ± 493.6 | 471.7 ± 190.7 | 55.8 ± 33.8 | 4.4 ± 2.8 | 47 ± 30.3 | 4.4 ± 2.3 | 5.6 ± 2.7 | 46.2 ± 31.9 | 4 ± 2.4 | 80% | 40% |
| 横条-VS | 5 | 453.2 ± 128 | 239.9 ± 142 | 15.2 ± 3.1 | 3.4 ± 0.8 | 9.8 ± 1.5 | 2 ± 1.5 | 2.2 ± 1.9 | 11 ± 1.8 | 2 ± 1.1 | 0% | 20% |
| 左-中-右 | 5 | 1023 ± 249.2 | 533.4 ± 79.4 | 58 ± 23.3 | 4.4 ± 3.1 | 46.8 ± 19.2 | 6.8 ± 3.2 | 5.8 ± 2.1 | 46 ± 20.3 | 6.2 ± 2.1 | 100% | 0% |
| 地图底 | 5 | 1544.8 ± 1075.1 | 961.1 ± 394.1 | 49.2 ± 27.9 | 5 ± 1.8 | 41.2 ± 25.9 | 3 ± 1.8 | 3.2 ± 3.7 | 43 ± 27.8 | 3 ± 2.5 | 60% | 40% |
| 左右艺术设计+一体 | 4 | 818.6 ± 269.1 | 453.4 ± 59.5 | 33 ± 15 | 4.2 ± 2.2 | 25.5 ± 12.9 | 3.2 ± 1.6 | 2.2 ± 0.8 | 23.5 ± 11.2 | 7.2 ± 4.3 | 75% | 25% |
| 全屏获得新奖励 | 3 | 826.2 ± 350.6 | 530.3 ± 180.7 | 26.7 ± 13.2 | 3.7 ± 1.2 | 20 ± 12 | 3 ± 0 | 3 ± 0.8 | 20.3 ± 12 | 3.3 ± 1.9 | 0% | 100% |
| 登录加载全屏 | 3 | 655.2 ± 89.8 | 359 ± 56.7 | 15.7 ± 6.9 | 1.7 ± 0.9 | 12.3 ± 5.4 | 1.7 ± 0.9 | 2.7 ± 0.9 | 9.3 ± 6.6 | 3.7 ± 0.5 | 0% | 33% |
| 左右艺术设计+竖列表 | 3 | 858.6 ± 219.3 | 487.9 ± 80.8 | 19.7 ± 0.9 | 1.7 ± 0.5 | 14.7 ± 2.4 | 3.3 ± 0.9 | 1.3 ± 0.5 | 17.3 ± 1.2 | 1 ± 0 | 100% | 0% |
| 墙+小旗+横列表 | 3 | 986.3 ± 223 | 514.6 ± 3.3 | 59.3 ± 11 | 4.7 ± 0.5 | 53.7 ± 10.5 | 1 ± 0.8 | 5 ± 1.4 | 51.3 ± 13.8 | 3 ± 1.4 | 100% | 0% |
| 赛程 | 3 | 1356.6 ± 33 | 607.3 ± 63.3 | 57.7 ± 20.5 | 2.7 ± 1.7 | 51.3 ± 17.8 | 3.7 ± 1.9 | 3 ± 1.6 | 46.7 ± 15.5 | 8 ± 3.6 | 67% | 0% |
| 木屏风+横列表 | 3 | 695.1 ± 192.1 | 485.7 ± 100.6 | 37.3 ± 7.6 | 5.7 ± 2.6 | 30.3 ± 6.8 | 1.3 ± 1.9 | 6.3 ± 1.2 | 25.7 ± 9.3 | 5.3 ± 0.5 | 100% | 0% |
| 左右艺术设计+横列表 | 3 | 685.5 ± 252.7 | 502.5 ± 58.3 | 30 ± 2.2 | 3 ± 0 | 25.7 ± 2.9 | 1.3 ± 0.9 | 2.7 ± 0.5 | 24 ± 2.8 | 3.3 ± 1.2 | 100% | 0% |

---

## 统计异常 UI 清单 (z-score > 2.5) — 需要人工复核

以下 81 个 UI 在其分配的 wiki 类型中特征显著异常，可能存在分类错误：

| # | UI名称 | Wiki类型 | Z值 | 异常特征 | 实际值 | 类型均值±标准差 | WxH | 节点 | L/C/R | T/M/B |
|---|--------|---------|-----|---------|--------|---------------|-----|------|-------|-------|
| 1 | UI_GuildWarAtkSum | 上标题-中竖列表-下信息 | 7.3 | width | 3412.0 | 742.7±366.1 | 3412x526 | 29 | 0/28/1 | 1/27/1 |
| 2 | UI_CommonSkin | tips | 6.7 | center_count | 74 | 10.7±9.5 | 1128x717 | 78 | 1/74/3 | 4/68/6 |
| 3 | UI_RelayRaceResult | 展示-横条-条内信息 | 5.2 | bottom_count | 11 | 2.6±1.6 | 851x567 | 50 | 6/36/8 | 8/31/11 |
| 4 | UI_CombineRemouldTips | 确认弹框 | 4.9 | top_count | 7 | 1.9±1 | 439x286 | 42 | 4/35/3 | 7/32/3 |
| 5 | UI_GuildApplyList | 上标题-中竖列表-下信息 | 4.4 | bottom_count | 8 | 1.9±1.4 | 941x475 | 31 | 6/21/4 | 2/21/8 |
| 6 | UI_Chat | 一体框 | 4.4 | middle_count | 172 | 32.4±31.9 | 1635x919 | 191 | 2/173/16 | 9/172/10 |
| 7 | UI_CoatingActiveTips | 确认弹框 | 4.4 | height | 739.4 | 322.8±94 | 570x739 | 16 | 0/15/1 | 2/11/3 |
| 8 | UI_TradeWarPetition | 确认弹框 | 4.3 | bottom_count | 7 | 2.3±1.1 | 577x302 | 44 | 3/35/6 | 4/33/7 |
| 9 | UI_FlyItem | tips | 4.2 | right_count | 8 | 1.9±1.5 | 1x21 | 11 | 3/0/8 | 1/9/1 |
| 10 | UI_MarketStarActive | 上标题-中竖列表-下信息 | 4.1 | left_count | 10 | 3±1.7 | 728x489 | 37 | 10/24/3 | 4/29/4 |
| 11 | UI_BeautyCompMap | 左-右 | 4.1 | height | 1157.8 | 471.9±167.3 | 1416x1158 | 58 | 2/55/1 | 1/54/3 |
| 12 | UI_TeamInfo | 上标题-中横列表-下信息 | 4 | center_count | 76 | 25.7±12.5 | 935x529 | 85 | 3/76/6 | 9/65/11 |
| 13 | UI_StarWorksUpResult | 展示-横条-条内信息 | 3.8 | right_count | 10 | 2.8±1.9 | 502x482 | 42 | 4/28/10 | 3/34/5 |
| 14 | UI_FundGuestInfo | tips | 3.8 | total_nodes | 53 | 14.4±10.2 | 649x585 | 53 | 5/42/6 | 5/43/5 |
| 15 | UI_GuildGroupBuyNew | panel | 3.7 | bottom_count | 13 | 3.9±2.4 | 799x431 | 59 | 6/41/12 | 6/40/13 |
| 16 | UI_ItemUseTip | 使用弹框 | 3.6 | middle_count | 36 | 19±4.8 | 554x351 | 42 | 4/31/7 | 4/36/2 |
| 17 | UI_PirateInvasion | 红框方形玩法入口 | 3.5 | width | 2310.9 | 1031.4±364 | 2311x723 | 63 | 0/62/1 | 5/52/6 |
| 18 | UI_LimitLotteryGift | 上标题-中竖列表-下信息 | 3.5 | right_count | 9 | 3.1±1.7 | 589x594 | 36 | 3/24/9 | 3/32/1 |
| 19 | UI_CoatingResolveTips | 使用弹框 | 3.5 | height | 739.4 | 404±96.8 | 570x739 | 17 | 0/16/1 | 2/12/3 |
| 20 | UI_SeaEvidenceAdd | 使用弹框 | 3.5 | top_count | 6 | 2.5±1 | 527x467 | 29 | 5/19/5 | 6/16/7 |
| 21 | UI_RouteTrade | 上标题-中竖列表-下信息 | 3.5 | right_count | 9 | 3.1±1.7 | 1266x644 | 45 | 7/29/9 | 5/39/1 |
| 22 | UI_PirateEvent | tips | 3.4 | bottom_count | 7 | 2.1±1.4 | 552x628 | 43 | 2/39/2 | 5/31/7 |
| 23 | UI_CombineRemould | 上标题-中横列表-下信息 | 3.4 | left_count | 6 | 1.9±1.2 | 828x528 | 47 | 6/38/3 | 3/38/6 |
| 24 | UI_AssistantGuildSetting | 使用弹框 | 3.4 | width | 657.9 | 499±47.4 | 658x511 | 28 | 3/22/3 | 1/24/3 |
| 25 | UI_TradeWarGuests | 上标题-中横列表-下信息 | 3.3 | right_count | 8 | 2.1±1.8 | 1207x530 | 55 | 2/45/8 | 5/40/10 |
| 26 | UI_SkyscraperActivity | 红框方形玩法入口 | 3.3 | height | 1442.0 | 657.4±238.2 | 1029x1442 | 85 | 8/70/7 | 2/83/0 |
| 27 | UI_InvestmentDetail | 上标题-中横列表-下信息 | 3.3 | right_count | 8 | 2.1±1.8 | 908x503 | 66 | 3/55/8 | 6/52/8 |
| 28 | UI_RankActAd | 活动打脸弹窗 | 3.2 | middle_count | 80 | 23.9±17.8 | 811x843 | 89 | 8/74/7 | 3/80/6 |
| 29 | UI_SilkroadGains | T型-上标题-左标签-右竖列表 | 3.2 | middle_count | 70 | 35±10.8 | 695x468 | 76 | 8/61/7 | 1/70/5 |
| 30 | UI_AuthTips | 确认弹框 | 3.2 | left_count | 5 | 1.5±1.1 | 622x243 | 25 | 5/17/3 | 2/19/4 |
| 31 | UI_RankAct | T型-上标题-左-右 | 3.2 | top_count | 10 | 4.1±1.9 | 803x631 | 65 | 7/48/10 | 10/47/8 |
| 32 | UI_TradingPortCompose | 使用弹框 | 3.2 | bottom_count | 8 | 2.5±1.7 | 486x384 | 28 | 3/22/3 | 3/17/8 |
| 33 | UI_GuildWarStreet | panel | 3.2 | height | 891.0 | 484.1±128.7 | 1320x891 | 46 | 2/43/1 | 1/44/1 |
| 34 | UI_MarketWarSupport | 确认弹框 | 3.2 | left_count | 5 | 1.5±1.1 | 466x336 | 20 | 5/10/5 | 3/14/3 |
| 35 | UI_GuildNoticTemplate | 上标题-中竖列表-下信息 | 3.1 | height | 810.9 | 392.6±136.4 | 802x811 | 13 | 1/11/1 | 1/11/1 |
| 36 | UI_MarketWarResult | 展示-横条-条内信息 | 3.1 | center_count | 46 | 18.8±8.9 | 633x605 | 53 | 2/46/5 | 3/46/4 |
| 37 | UI_MarketCommodity | 左-右 | 3.1 | right_count | 12 | 4.6±2.4 | 719x438 | 42 | 5/25/12 | 5/28/9 |
| 38 | UI_RelayCommonFleet | 横列表 | 3.1 | width | 2128.0 | 656.5±477.4 | 2128x544 | 71 | 1/66/4 | 2/65/4 |
| 39 | UI_SilkroadMap | panel+入口 | 3.0 | width | 3319.7 | 1268.9±683.1 | 3320x666 | 99 | 1/96/2 | 6/82/11 |
| 40 | UI_TitleTips | tips | 3 | left_count | 6 | 1.9±1.4 | 264x302 | 11 | 6/1/4 | 1/8/2 |
| 41 | UI_FashionShopEff | tips | 3 | left_count | 6 | 1.9±1.4 | 334x341 | 32 | 6/21/5 | 3/25/4 |
| 42 | UI_RankActPreview | 活动打脸弹窗 | 3 | middle_count | 78 | 23.9±17.8 | 800x843 | 86 | 7/72/7 | 3/78/5 |
| 43 | UI_MarketBaseInfo | T型-上标题-左标签-右竖列表 | 3 | top_count | 9 | 3±2 | 918x501 | 66 | 8/50/8 | 9/52/5 |
| 44 | UI_GuildActivity | 左标签+右竖列表 | 2.9 | right_count | 12 | 4.3±2.7 | 942x572 | 70 | 3/55/12 | 11/53/6 |
| 45 | UI_GuildLobby | panel | 2.9 | top_count | 13 | 3.8±3.1 | 681x510 | 75 | 11/52/12 | 13/56/6 |
| 46 | UI_Role | 全屏背景界面 | 2.9 | top_count | 16 | 3.6±4.3 | 1236x720 | 138 | 7/123/8 | 16/104/18 |
| 47 | UI_SilkroadOasisOverview | 上标题-中竖列表-下信息 | 2.9 | right_count | 8 | 3.1±1.7 | 868x506 | 35 | 4/23/8 | 4/29/2 |
| 48 | UI_ActivityRank | 上标题-中竖列表-下信息 | 2.9 | center_count | 41 | 19.7±7.2 | 760x379 | 49 | 5/41/3 | 4/40/5 |
| 49 | UI_ExpandAkfReward | 确认弹框 | 2.9 | height | 592.6 | 322.8±94 | 291x593 | 26 | 2/21/3 | 2/20/4 |
| 50 | UI_PrivilegeMonthlyCard2 | tips | 2.8 | right_count | 6 | 1.9±1.5 | 448x301 | 21 | 3/12/6 | 3/14/4 |
| 51 | UI_SilkroadMission | 左广告图-右列表 | 2.8 | bottom_count | 14 | 4.3±3.4 | 1134x552 | 63 | 11/47/5 | 6/43/14 |
| 52 | UI_MountInfo | 四边木栏（蒸笼标签）+左中右 | 2.8 | width | 718.0 | 1020.5±109 | 718x393 | 32 | 1/29/2 | 5/25/2 |
| 53 | UI_BeautyCompUpgrade | 功能开启&展示 | 2.8 | left_count | 4 | 1.2±1 | 574x346 | 15 | 4/10/1 | 1/12/2 |
| 54 | UI_BanquetOfFamilyOpen | 确认弹框 | 2.8 | total_nodes | 37 | 17.1±7 | 645x403 | 37 | 2/30/5 | 4/28/5 |
| 55 | UI_RelayRaceInfo | panel | 2.7 | left_count | 11 | 3.5±2.8 | 899x502 | 73 | 11/55/7 | 7/61/5 |
| 56 | UI_TechnoCourseTip | tips | 2.7 | bottom_count | 6 | 2.1±1.4 | 382x200 | 16 | 4/9/3 | 2/8/6 |
| 57 | UI_ChildMarryFailTip | 展示-横条-条内信息 | 2.7 | width | 7.0 | 590.5±215.2 | 7x85 | 5 | 1/3/1 | 1/3/1 |
| 58 | UI_CyberIllusionMain | 全屏背景界面 | 2.7 | right_count | 12 | 2.9±3.4 | 865x611 | 91 | 6/73/12 | 9/71/11 |
| 59 | UI_GuildWarRstMult | 展示-横条-条内信息 | 2.7 | left_count | 6 | 2.4±1.3 | 949x612 | 33 | 6/21/6 | 6/25/2 |
| 60 | UI_GoodsActive | tips | 2.7 | height | 721.2 | 266.9±165.2 | 785x721 | 18 | 3/12/3 | 3/12/3 |
| 61 | UI_Setting | 一体框 | 2.7 | left_count | 9 | 3.3±2.1 | 860x435 | 39 | 9/26/4 | 6/26/7 |
| 62 | UI_TradeWarPveResult | 展示-横条-条内信息 | 2.7 | right_count | 8 | 2.8±1.9 | 886x369 | 50 | 4/38/8 | 0/44/6 |
| 63 | UI_TradeWarFind | 上标题-中上标签-中竖列表-下信息 | 2.7 | left_count | 10 | 4.6±2 | 870x405 | 61 | 10/43/8 | 7/50/4 |
| 64 | UI_ExpandEventNew | 展示-横条-条内信息 | 2.7 | width | 18.7 | 590.5±215.2 | 19x96 | 3 | 1/1/1 | 1/1/1 |
| 65 | UI_GuildWarPlan | 上标题-中竖列表-下信息 | 2.6 | height | 744.0 | 392.6±136.4 | 857x744 | 35 | 4/28/3 | 2/29/4 |
| 66 | UI_MarketWarRank | 上标题-中竖列表-下信息 | 2.6 | top_count | 6 | 2.5±1.3 | 1039x520 | 30 | 2/26/2 | 6/21/3 |
| 67 | UI_GuildDungeonEliteBattle | panel+入口 | 2.6 | top_count | 13 | 5.8±2.7 | 944x564 | 49 | 10/28/11 | 13/26/10 |
| 68 | UI_StreetFightBattle | 战斗 | 2.6 | left_count | 8 | 2.7±2.1 | 840x729 | 108 | 8/90/10 | 9/90/9 |
| 69 | UI_BeautyTalk | 功能开启&展示 | 2.6 | center_count | 17 | 7.9±3.5 | 579x446 | 18 | 0/17/1 | 1/14/3 |
| 70 | UI_ActArena | 左-右 | 2.6 | bottom_count | 11 | 4.2±2.7 | 1032x612 | 65 | 5/52/8 | 10/44/11 |
| 71 | UI_BeautyBook | 功能开启&展示 | 2.6 | height | 667.0 | 328.8±127.8 | 326x667 | 13 | 1/9/3 | 1/9/3 |
| 72 | UI_PrivilegeMain | 左标签+右竖列表 | 2.6 | height | 133.3 | 417±109.9 | 484x133 | 9 | 2/6/1 | 1/8/0 |
| 73 | UI_ActArenaSoloMarket | 上标题-中竖列表-下信息 | 2.6 | middle_count | 41 | 21.4±7.6 | 1141x522 | 45 | 5/34/6 | 3/41/1 |
| 74 | UI_PurchaseBattleGuildRank | 上标题-中竖列表-下信息 | 2.6 | top_count | 6 | 2.5±1.3 | 1019x426 | 32 | 5/24/3 | 6/23/3 |
| 75 | UI_MarketWarCapture | 上标题-中竖列表-下信息 | 2.6 | total_nodes | 48 | 25.7±8.5 | 1160x576 | 48 | 6/38/4 | 5/39/4 |
| 76 | UI_Billionaires | 左-右 | 2.5 | top_count | 10 | 3.7±2.5 | 1133x594 | 79 | 6/67/6 | 10/61/8 |
| 77 | UI_Main | mainUI | 2.5 | top_count | 10 | 3.4±2.6 | 1162x483 | 131 | 5/125/1 | 10/114/7 |
| 78 | UI_GuestInfo | 四边木栏（蒸笼标签）+左中右 | 2.5 | total_nodes | 206 | 87.7±47.2 | 1077x620 | 206 | 13/160/33 | 26/153/27 |
| 79 | UI_FundBeautyInfo | tips | 2.5 | top_count | 5 | 1.9±1.2 | 506x537 | 25 | 4/16/5 | 5/17/3 |
| 80 | UI_RoleUpTip | tips | 2.5 | middle_count | 33 | 10.5±9 | 810x423 | 38 | 2/33/3 | 2/33/3 |
| 81 | UI_MainPowerDetail | tips | 2.5 | top_count | 5 | 1.9±1.2 | 683x515 | 14 | 3/7/4 | 5/5/4 |

---

## 异常模式分析

### 异常类别分布

| 异常类型 | 数量 | 说明 |
|---------|------|------|
| 节点数异常 | 4 | UI 的 GameObject 节点数远超同类型均值 |
| 宽度异常 | 5 | UI 宽度远超同类型均值 |
| 高度异常 | 10 | UI 高度远超同类型均值 |
| XY分布异常 | 58 | 节点在 X/Y 轴分布与同类型差异大 |

### 常见异常模式

1. **小浮窗被标为其他类型**: 一些实际上的弹框/提示类 UI 尺寸小但节点多或分布异常，被 wiki 分到了面板类。例如 UI_TitleTips、UI_FashionShopEff 等小尺寸(200-350宽)但 left_count 比例高。

2. **超大面板**: 部分 UI 宽度远超同类（如 UI_GuildWarAtkSum 宽 3412、UI_RelayCommonFleet 宽 2128），可能是特殊布局的全宽列表。

3. **复杂UI被简化分类**: 如 UI_CommonSkin (1128x717, 78节点)被标为 tips 但实际是复杂皮肤预览界面。UI_Chat (1635x919, 191节点)被标为一体框但实际是大型聊天界面。

4. **装饰性UI特征缺失**: 四边木栏、艺术设计等装饰类型的识别需要视觉分析，仅从结构数据无法区分。如 UI_BeautyTravel (四边木栏+格子排 vs T型-上标题-左标签-右竖列表)。

---

## 无 Wiki 类型的 UI（仅图片，需分配类型）

以下 82 个 UI 在 wiki 布局类型中没有记录：

- **UI_ActApexPvpComment**: W=666 H=320 N=6 L/C/R=1/4/1 List=True
- **UI_ActApexPvpGetSign**: W=903 H=327 N=16 L/C/R=1/14/1 List=False
- **UI_ActApexPvpSignTip**: W=317 H=238 N=6 L/C/R=1/4/1 List=False
- **UI_AsideText**: W=0 H=150 N=2 L/C/R=0/2/0 List=False
- **UI_BanquetNotifyForJoin**: W=143 H=126 N=7 L/C/R=1/5/1 List=False
- **UI_BattleEarningUpTip**: W=472 H=192 N=8 L/C/R=1/6/1 List=False
- **UI_BattlePassBigRewardPreview**: W=324 H=272 N=20 L/C/R=1/19/0 List=True
- **UI_BattlePassRewardOverview**: W=373 H=414 N=20 L/C/R=1/19/0 List=True
- **UI_BattleUpTip**: W=372 H=66 N=8 L/C/R=2/5/1 List=False
- **UI_BeautyGetting**: W=1008 H=525 N=52 L/C/R=6/42/4 List=True
- **UI_BeautyPromoteSucc**: W=823 H=501 N=35 L/C/R=5/26/4 List=True
- **UI_BeautyRecuitTip**: W=297 H=527 N=8 L/C/R=2/4/2 List=False
- **UI_BeautyUpQuality**: W=1362 H=724 N=52 L/C/R=2/47/3 List=True
- **UI_BuffTips**: W=110 H=147 N=5 L/C/R=0/4/1 List=True
- **UI_ChatSmall**: W=422 H=79 N=17 L/C/R=1/11/5 List=False
- **UI_ChildMarrySuccTip**: W=630 H=235 N=16 L/C/R=2/12/2 List=False
- **UI_CoatingSkillDescTips**: W=107 H=178 N=3 L/C/R=2/0/1 List=False
- **UI_CommonDigit**: W=270 H=176 N=17 L/C/R=3/11/3 List=False
- **UI_CPPopBtns**: W=487 H=248 N=7 L/C/R=0/6/1 List=False
- **UI_CyberIllusionSkillTip**: W=288 H=248 N=11 L/C/R=2/7/2 List=False
- **UI_CyberIllusionSource**: W=250 H=247 N=10 L/C/R=0/8/2 List=True
- **UI_DailyTips**: W=185 H=124 N=5 L/C/R=1/2/2 List=False
- **UI_ExpandAisleTaskProUp**: W=92 H=196 N=8 L/C/R=1/5/2 List=False
- **UI_FashionShopBuySucc**: W=913 H=466 N=20 L/C/R=4/14/2 List=False
- **UI_FlyItem4**: W=76 H=65 N=9 L/C/R=1/7/1 List=False
- **UI_FlyItem5**: W=549 H=313 N=4 L/C/R=1/2/1 List=True
- **UI_GM**: W=1181 H=539 N=103 L/C/R=19/63/21 List=True
- **UI_GuestActiveSkill**: W=529 H=535 N=21 L/C/R=1/19/1 List=False
- **UI_GuestFashionActive**: W=950 H=397 N=23 L/C/R=2/19/2 List=True
- **UI_GuestGetSkinItem**: W=665 H=206 N=8 L/C/R=1/6/1 List=False
- **UI_GuestPromoteSucc**: W=745 H=391 N=36 L/C/R=4/28/4 List=False
- **UI_GuestUpQuality**: W=1299 H=535 N=40 L/C/R=1/37/2 List=True
- **UI_GuildWarScene**: W=4916 H=2744 N=153 L/C/R=2/139/12 List=True
- **UI_ItemAddTip**: W=132 H=210 N=5 L/C/R=1/3/1 List=False
- **UI_ItemAddTips2**: W=441 H=318 N=9 L/C/R=5/1/3 List=False
- **UI_LotterySkinItem**: W=798 H=517 N=34 L/C/R=2/29/3 List=True
- **UI_MainMoneyTalentBuffTips**: W=413 H=195 N=6 L/C/R=1/4/1 List=False
- **UI_MainVisitBuffTips**: W=413 H=196 N=5 L/C/R=1/3/1 List=False
- **UI_MarketBeautyDispatchSucc**: W=1056 H=483 N=32 L/C/R=1/30/1 List=True
- **UI_MarketBellProgress**: W=1095 H=358 N=18 L/C/R=3/11/4 List=False
- **UI_MarketBestSell**: W=281 H=386 N=12 L/C/R=2/8/2 List=False
- **UI_MarketIngredentsInfo**: W=387 H=482 N=19 L/C/R=3/13/3 List=True
- **UI_MarketWarBeautySkill**: W=681 H=446 N=14 L/C/R=3/6/5 List=False
- **UI_MarketWarBuff**: W=360 H=150 N=8 L/C/R=1/5/2 List=False
- **UI_MarketWarCoolingSkill**: W=451 H=210 N=5 L/C/R=1/3/1 List=False
- **UI_MarketWarEmployerTip**: W=748 H=406 N=12 L/C/R=4/7/1 List=False
- **UI_MarketWarHpTip**: W=135 H=103 N=10 L/C/R=1/7/2 List=False
- **UI_MarketWarSupportSucc**: W=516 H=462 N=4 L/C/R=1/2/1 List=False
- **UI_MarqueeMsg**: W=11 H=205 N=5 L/C/R=1/4/0 List=False
- **UI_MarqueeSpineMsg**: W=306 H=201 N=6 L/C/R=1/5/0 List=False
- **UI_MountAttrInfo**: W=293 H=49 N=7 L/C/R=3/3/1 List=True
- **UI_NpcBubble**: W=240 H=159 N=17 L/C/R=0/16/1 List=False
- **UI_NpcTimeBubble**: W=461 H=142 N=7 L/C/R=1/6/0 List=False
- **UI_PirateLikabilityAnim**: W=509 H=310 N=7 L/C/R=2/0/5 List=False
- **UI_PrivilegePropsCard**: W=591 H=200 N=17 L/C/R=1/14/2 List=True
- **UI_RankPlayerVoteReward**: W=665 H=351 N=11 L/C/R=1/8/2 List=False
- **UI_SilkroadMissionScoreAdd**: W=553 H=235 N=4 L/C/R=1/3/0 List=False
- **UI_SilkroadOpening**: W=966 H=470 N=8 L/C/R=2/4/2 List=False
- **UI_SkillDescTips**: W=298 H=203 N=22 L/C/R=4/15/3 List=False
- **UI_StarLevelTip**: W=121 H=116 N=5 L/C/R=1/2/2 List=False
- **UI_StreetTreasureTip**: W=186 H=117 N=9 L/C/R=3/2/4 List=False
- **UI_TalkBubbleList**: W=263 H=159 N=6 L/C/R=1/5/0 List=True
- **UI_TargetPro**: W=98 H=227 N=4 L/C/R=2/1/1 List=False
- **UI_TaskFinishTip**: W=151 H=368 N=9 L/C/R=1/6/2 List=False
- **UI_TaskMainTip**: W=256 H=1189 N=9 L/C/R=1/6/2 List=False
- **UI_TeamGuestTrial**: W=1969 H=888 N=55 L/C/R=3/50/2 List=True
- **UI_TechnoExamResult**: W=271 H=218 N=7 L/C/R=1/5/1 List=False
- **UI_TechnoInfo**: W=999 H=702 N=31 L/C/R=2/24/5 List=True
- **UI_TechnoStudy**: W=846 H=538 N=24 L/C/R=3/18/3 List=False
- **UI_TechnoStudyCourse**: W=314 H=731 N=16 L/C/R=1/12/3 List=False
- **UI_TimeLineOption**: W=4 H=2 N=4 L/C/R=0/3/1 List=False
- **UI_TopLeagueComment**: W=666 H=320 N=6 L/C/R=1/4/1 List=True
- **UI_TopLeagueGetSign**: W=903 H=327 N=16 L/C/R=1/14/1 List=False
- **UI_TopLeagueSignTip**: W=834 H=580 N=10 L/C/R=1/8/1 List=False
- **UI_TotalStrengthTip**: W=330 H=148 N=10 L/C/R=1/7/2 List=False
- **UI_TradingPortNewShip**: W=848 H=360 N=28 L/C/R=1/24/3 List=False
- **UI_TradingPortStrengthen**: W=704 H=580 N=39 L/C/R=1/29/9 List=True
- **UI_TrialSpacetimeDrop**: W=634 H=348 N=43 L/C/R=3/36/4 List=True
- **UI_TrialSpacetimeMsgs**: W=340 H=371 N=7 L/C/R=1/5/1 List=True
- **UI_VideoPlayer**: W=767 H=288 N=7 L/C/R=1/5/1 List=False
- **UI_VisitOptTips**: W=263 H=129 N=16 L/C/R=2/10/4 List=False
- **UI_WaitNet**: W=0 H=16 N=2 L/C/R=0/2/0 List=False

---

## 无特征数据的 UI（仅 wiki 记录）

- **UI_FullSceneTips**: Wiki类型=tips

---

## 完整对比清单

| # | UI名称 | Wiki类型 | 宽 | 高 | 节点 | L/C/R | T/M/B | List | Bg | 异常标记 |
|---|--------|---------|-----|-----|------|-------|-------|------|-----|---------|
| 1 | UI_ALiFirstVisit | 活动打脸弹窗 | 450 | 295 | 19 | 0/17/2 | 1/15/3 | Y | N |  |
| 2 | UI_ALiPCLogIn | 活动打脸弹窗 | 489 | 398 | 22 | 0/20/2 | 1/18/3 | Y | N |  |
| 3 | UI_Achievement | panel | 935 | 484 | 38 | 4/30/4 | 1/35/2 | Y | Y |  |
| 4 | UI_AcitveAd | panel | 1005 | 470 | 19 | 2/14/3 | 1/16/2 | N | N |  |
| 5 | UI_ActApexPvp | 赛程 | 1380 | 552 | 68 | 5/58/5 | 3/55/10 | Y | N |  |
| 6 | UI_ActApexPvpBattle | 战斗 | 1130 | 968 | 95 | 3/86/6 | 4/89/2 | Y | N |  |
| 7 | UI_ActApexPvpComment | N/A | 666 | 320 | 6 | 1/4/1 | 0/5/1 | Y | N |  |
| 8 | UI_ActApexPvpDesc | tips | 604 | 375 | 15 | 2/12/1 | 3/9/3 | N | N |  |
| 9 | UI_ActApexPvpEvent | T型-上标题-左标签-右竖列表 | 1261 | 603 | 46 | 1/39/6 | 4/41/1 | Y | N |  |
| 10 | UI_ActApexPvpGetSign | N/A | 903 | 327 | 16 | 1/14/1 | 1/12/3 | N | N |  |
| 11 | UI_ActApexPvpMarket | 左右对比 | 548 | 424 | 43 | 5/32/6 | 5/35/3 | Y | N |  |
| 12 | UI_ActApexPvpPreview | 左-右 | 1168 | 581 | 41 | 3/35/3 | 5/31/5 | Y | N |  |
| 13 | UI_ActApexPvpProgress | 四边木栏（蒸笼标签）+横列表 | 476 | 326 | 18 | 2/16/0 | 2/14/2 | Y | N |  |
| 14 | UI_ActApexPvpRank | 左标签+右竖列表 | 740 | 434 | 43 | 5/35/3 | 2/35/6 | Y | Y |  |
| 15 | UI_ActApexPvpReady | 横条-VS | 494 | 410 | 14 | 4/9/1 | 1/12/1 | N | N |  |
| 16 | UI_ActApexPvpRecord | 上标题-中竖列表-下信息 | 1112 | 318 | 28 | 1/23/4 | 2/25/1 | Y | N |  |
| 17 | UI_ActApexPvpResult | 展示-横条-条内信息 | 788 | 395 | 28 | 4/22/2 | 5/20/3 | N | Y |  |
| 18 | UI_ActApexPvpReward | 上标题-中竖列表-下信息 | 470 | 460 | 23 | 1/20/2 | 1/19/3 | Y | Y |  |
| 19 | UI_ActApexPvpShop | 上标题-中横列表-下信息 | 635 | 359 | 22 | 1/20/1 | 1/20/1 | Y | N |  |
| 20 | UI_ActApexPvpSignTip | N/A | 317 | 238 | 6 | 1/4/1 | 1/5/0 | N | N |  |
| 21 | UI_ActApexPvpWager | 使用弹框 | 476 | 350 | 24 | 2/18/4 | 2/20/2 | N | N |  |
| 22 | UI_ActArena | 左-右 | 1032 | 612 | 65 | 5/52/8 | 10/44/11 | Y | Y | ⚠ z=2.6 on bottom_count |
| 23 | UI_ActArenaOtherMarket | 上标题-中竖列表-下信息 | 474 | 419 | 24 | 1/21/2 | 5/16/3 | Y | Y |  |
| 24 | UI_ActArenaOtherMarketInfo | 上标题-中横列表-下信息 | 338 | 383 | 25 | 2/22/1 | 1/23/1 | Y | N |  |
| 25 | UI_ActArenaRank | 左标签页-右框内-上标题-中竖列表-下信息 | 1229 | 410 | 35 | 2/29/4 | 4/27/4 | Y | N |  |
| 26 | UI_ActArenaResult | 展示-横条-条内信息 | 792 | 472 | 36 | 3/28/5 | 2/29/5 | Y | N |  |
| 27 | UI_ActArenaSolo | 上标题-中横列表-下信息 | 566 | 491 | 37 | 2/31/4 | 6/27/4 | Y | Y |  |
| 28 | UI_ActArenaSoloMarket | 上标题-中竖列表-下信息 | 1141 | 522 | 45 | 5/34/6 | 3/41/1 | Y | N | ⚠ z=2.6 on middle_count |
| 29 | UI_ActArenaTarget | 上标题-中横列表-下信息 | 325 | 440 | 25 | 2/21/2 | 4/17/4 | Y | N |  |
| 30 | UI_ActCumulativeRecharge | 左艺术设计+左-右 | 964 | 522 | 40 | 4/34/2 | 4/30/6 | Y | N |  |
| 31 | UI_ActKingOfSnowBattle | 战斗 | 1183 | 553 | 79 | 2/73/4 | 7/64/8 | Y | N |  |
| 32 | UI_ActKingOfSnowBattleResult | 展示-横条-条内信息 | 790 | 630 | 34 | 4/26/4 | 4/27/3 | Y | Y |  |
| 33 | UI_ActKingOfSnowLevel | 上标题-中竖列表-下信息 | 362 | 542 | 28 | 3/24/1 | 2/25/1 | Y | N |  |
| 34 | UI_ActKingOfSnowMain | 红框方形玩法入口 | 925 | 560 | 36 | 4/26/6 | 9/20/7 | N | N |  |
| 35 | UI_ActKingOfSnowTask | 上标题-中竖列表-下信息 | 624 | 291 | 31 | 3/24/4 | 2/28/1 | Y | N |  |
| 36 | UI_ActMoonSpurt | T型-上标题-左标签-右竖列表 | 1111 | 276 | 40 | 2/35/3 | 2/36/2 | Y | N |  |
| 37 | UI_ActSnowCityRedRain | 红框方形玩法入口 | 612 | 595 | 18 | 1/15/2 | 4/12/2 | N | N |  |
| 38 | UI_ActSnowCityRedRainReward | 上标题-中横列表-下信息 | 218 | 277 | 10 | 1/9/0 | 2/7/1 | Y | N |  |
| 39 | UI_ActSnowMain | 全屏入口 | 624 | 536 | 45 | 1/42/2 | 5/35/5 | Y | Y |  |
| 40 | UI_ActSnowMan | 红框方形玩法入口 | 1030 | 534 | 40 | 4/30/6 | 4/32/4 | Y | N |  |
| 41 | UI_ActSnowManPreview | 上标题-中横列表-下信息 | 332 | 389 | 21 | 0/19/2 | 1/18/2 | Y | N |  |
| 42 | UI_ActSnowManTask | 上标题-中竖列表-下信息 | 624 | 453 | 34 | 3/26/5 | 4/30/0 | Y | N |  |
| 43 | UI_ActSnowWheel | 红框方形玩法入口 | 856 | 551 | 43 | 3/37/3 | 3/36/4 | Y | Y |  |
| 44 | UI_ActSnowWheelLimitAward | 上标题-中横列表-下信息 | 152 | 315 | 16 | 1/14/1 | 3/10/3 | Y | N |  |
| 45 | UI_ActSnowWheelPreview | 上标题-中横列表-下信息 | 186 | 389 | 21 | 1/16/4 | 1/18/2 | Y | N |  |
| 46 | UI_ActSnowWheelResult | 展示-横条-条内信息 | 532 | 562 | 30 | 3/25/2 | 3/25/2 | Y | Y |  |
| 47 | UI_ActSpurtGift | 上标题-中竖列表-下信息 | 543 | 248 | 17 | 1/12/4 | 1/16/0 | Y | Y |  |
| 48 | UI_ActStreet | 左-右 | 954 | 588 | 45 | 4/36/5 | 4/33/8 | Y | N |  |
| 49 | UI_ActStrengthSpurt | T型-上标题-左标签-右竖列表 | 773 | 294 | 35 | 2/30/3 | 1/32/2 | Y | N |  |
| 50 | UI_ActivityBuyGuest | 活动打脸弹窗 | 970 | 536 | 41 | 2/37/2 | 4/34/3 | N | N |  |
| 51 | UI_ActivityBuyGuest2 | 活动打脸弹窗 | 842 | 548 | 25 | 1/23/1 | 3/20/2 | N | N |  |
| 52 | UI_ActivityCalender | 左艺术设计+左-右 | 993 | 486 | 32 | 2/29/1 | 5/23/4 | Y | N |  |
| 53 | UI_ActivityLobby | 左标签-右信息 | 1069 | 791 | 102 | 5/90/7 | 6/93/3 | Y | N |  |
| 54 | UI_ActivityRank | 上标题-中竖列表-下信息 | 760 | 379 | 49 | 5/41/3 | 4/40/5 | Y | N | ⚠ z=2.9 on center_count |
| 55 | UI_ActivityReward | T型-上标题-左标签-右竖列表 | 751 | 512 | 40 | 2/35/3 | 3/36/1 | Y | N |  |
| 56 | UI_ActivityShop | 上标题-中横列表-下信息 | 635 | 315 | 26 | 2/22/2 | 3/22/1 | Y | N |  |
| 57 | UI_ActivitySubScribe | 上标题-中横列表-下信息 | 223 | 586 | 21 | 1/19/1 | 1/15/5 | Y | N |  |
| 58 | UI_ActivityUpRedTip | 活动打脸弹窗 | 1108 | 396 | 36 | 5/28/3 | 5/29/2 | N | N |  |
| 59 | UI_AddShortCut | 活动打脸弹窗 | 450 | 295 | 19 | 0/17/2 | 1/15/3 | Y | N |  |
| 60 | UI_AgeTips | tips | 14 | 265 | 6 | 1/5/0 | 2/2/2 | Y | N |  |
| 61 | UI_AgreementDesc | tips | 15 | 412 | 9 | 2/5/2 | 3/4/2 | N | N |  |
| 62 | UI_AgreementTips | 确认弹框 | 407 | 296 | 15 | 1/13/1 | 2/12/1 | N | N |  |
| 63 | UI_AirRoutePrivilege | 活动打脸弹窗 | 500 | 210 | 11 | 1/7/3 | 1/7/3 | Y | N |  |
| 64 | UI_AliMinGameClub | T型-上标题-左标签-右竖列表 | 675 | 445 | 32 | 2/27/3 | 1/29/2 | Y | Y |  |
| 65 | UI_AliRepetitionVisit | 活动打脸弹窗 | 441 | 413 | 19 | 0/17/2 | 1/15/3 | Y | N |  |
| 66 | UI_AsideText | N/A | 0 | 150 | 2 | 0/2/0 | 1/0/1 | N | N |  |
| 67 | UI_AssistantGuildSetting | 使用弹框 | 658 | 511 | 28 | 3/22/3 | 1/24/3 | Y | N | ⚠ z=3.4 on width |
| 68 | UI_AssistantPanel | 左艺术设计+左-右 | 800 | 346 | 24 | 3/18/3 | 1/21/2 | Y | N |  |
| 69 | UI_AssistantReward | 展示-横条-条内信息 | 434 | 448 | 20 | 0/17/3 | 1/18/1 | Y | Y |  |
| 70 | UI_AssistantRouteTrade | 上标题-中竖列表-下信息 | 564 | 578 | 27 | 4/19/4 | 2/21/4 | Y | N |  |
| 71 | UI_AssistantShop | 墙+小旗+横列表 | 1144 | 517 | 65 | 4/59/2 | 4/59/2 | Y | N |  |
| 72 | UI_AssistantShopPurchase | 使用弹框 | 476 | 452 | 25 | 1/22/2 | 2/20/3 | N | N |  |
| 73 | UI_AuthSelect | 上标题-中竖列表-下信息 | 548 | 439 | 21 | 1/17/3 | 2/17/2 | Y | N |  |
| 74 | UI_AuthTips | 确认弹框 | 622 | 243 | 25 | 5/17/3 | 2/19/4 | N | Y | ⚠ z=3.2 on left_count |
| 75 | UI_Bag | 四边木栏（蒸笼标签）+左中右 | 1101 | 548 | 82 | 3/78/1 | 3/68/11 | Y | Y |  |
| 76 | UI_BagComposeTips | 确认弹框 | 274 | 346 | 16 | 2/13/1 | 1/13/2 | N | N |  |
| 77 | UI_BanquetAddTips | tips | 442 | 306 | 15 | 2/12/1 | 1/12/2 | N | Y |  |
| 78 | UI_BanquetAdvancedList | 灯笼标签+彩带+全屏 | 629 | 224 | 9 | 3/0/6 | 2/6/1 | N | N |  |
| 79 | UI_BanquetFinish | 展示-横条-条内信息 | 522 | 571 | 19 | 1/16/2 | 3/13/3 | Y | N |  |
| 80 | UI_BanquetGiftSelect | 上标题+下横列表 | 628 | 424 | 23 | 2/18/3 | 4/16/3 | N | N |  |
| 81 | UI_BanquetGuest | 上标题-中竖列表-下信息 | 604 | 263 | 18 | 2/13/3 | 1/16/1 | Y | N |  |
| 82 | UI_BanquetJoinSetting | 上标题+下横列表 | 628 | 424 | 24 | 2/19/3 | 3/18/3 | N | N |  |
| 83 | UI_BanquetJoinSucc | 展示-横条-条内信息 | 502 | 438 | 19 | 1/16/2 | 3/14/2 | Y | N |  |
| 84 | UI_BanquetMain | 四边木栏（蒸笼标签）+格子排 | 914 | 582 | 39 | 3/31/5 | 3/34/2 | Y | N |  |
| 85 | UI_BanquetNormalList | 灯笼标签+彩带+全屏 | 1101 | 357 | 28 | 3/22/3 | 4/21/3 | Y | N |  |
| 86 | UI_BanquetNotifyForJoin | N/A | 143 | 126 | 7 | 1/5/1 | 1/5/1 | N | N |  |
| 87 | UI_BanquetObtainingTimes | 左艺术设计+左-右 | 706 | 502 | 15 | 2/11/2 | 2/11/2 | N | N |  |
| 88 | UI_BanquetOfBaiFuDetail | 左艺术设计+左-右 | 1086 | 562 | 37 | 2/32/3 | 1/33/3 | Y | N |  |
| 89 | UI_BanquetOfBaiFuList | 左右艺术设计+竖列表 | 724 | 480 | 19 | 2/13/4 | 2/16/1 | Y | N |  |
| 90 | UI_BanquetOfBaiFuSelectV2 | 左标签+中图+右信息 | 768 | 544 | 26 | 3/20/3 | 3/19/4 | Y | Y |  |
| 91 | UI_BanquetOfFamilyDetail | 左艺术设计+左-右 | 1086 | 582 | 53 | 6/44/3 | 5/40/8 | Y | N |  |
| 92 | UI_BanquetOfFamilyLimit | 确认弹框 | 155 | 311 | 11 | 1/7/3 | 1/9/1 | N | N |  |
| 93 | UI_BanquetOfFamilyOpen | 确认弹框 | 645 | 403 | 37 | 2/30/5 | 4/28/5 | N | N | ⚠ z=2.8 on total_nodes |
| 94 | UI_BanquetOfFamilySelect | 左标签+中图+右信息 | 768 | 552 | 52 | 3/39/10 | 6/42/4 | Y | Y |  |
| 95 | UI_BanquetOfOfficialDetail | 左艺术设计+左-右 | 1086 | 787 | 39 | 2/34/3 | 2/32/5 | Y | N |  |
| 96 | UI_BanquetOfOfficialList | 左右艺术设计+竖列表 | 684 | 393 | 19 | 2/13/4 | 1/17/1 | Y | N |  |
| 97 | UI_BanquetOfOfficialSelect | 左标签+中图+右信息 | 768 | 544 | 22 | 2/16/4 | 4/13/5 | Y | Y |  |
| 98 | UI_BanquetOpenSucc | 功能开启&展示 | 33 | 239 | 8 | 2/5/1 | 1/6/1 | N | N |  |
| 99 | UI_BanquetPopularityReward | 上标题-中竖列表-下信息 | 533 | 350 | 27 | 2/22/3 | 4/22/1 | Y | N |  |
| 100 | UI_BanquetRank | 上标题-中竖列表-下信息 | 617 | 403 | 23 | 4/17/2 | 2/18/3 | Y | N |  |
| 101 | UI_BanquetRecord | 上标题-中竖列表-下信息 | 623 | 356 | 15 | 2/11/2 | 1/12/2 | Y | N |  |
| 102 | UI_BattleBaseStart | 横条-VS | 602 | 81 | 20 | 4/11/5 | 6/10/4 | N | Y |  |
| 103 | UI_BattleEarningUpTip | N/A | 472 | 192 | 8 | 1/6/1 | 1/7/0 | N | N |  |
| 104 | UI_BattlePass | 左-右 | 1179 | 664 | 66 | 5/53/8 | 9/48/9 | Y | N |  |
| 105 | UI_BattlePassBigRewardPreview | N/A | 324 | 272 | 20 | 1/19/0 | 2/17/1 | Y | N |  |
| 106 | UI_BattlePassBuyExp | 上标题-中横列表-下信息 | 846 | 546 | 33 | 4/25/4 | 3/24/6 | Y | N |  |
| 107 | UI_BattlePassBuyLicense | 活动打脸弹窗 | 383 | 339 | 22 | 3/19/0 | 2/17/3 | Y | N |  |
| 108 | UI_BattlePassRewardOverview | N/A | 373 | 414 | 20 | 1/19/0 | 1/18/1 | Y | N |  |
| 109 | UI_BattlePassTask | T型-上标题-左标签-右竖列表 | 789 | 416 | 31 | 3/27/1 | 3/26/2 | Y | N |  |
| 110 | UI_BattlePassUpgradeAni | tips | 190 | 145 | 7 | 0/6/1 | 4/1/2 | N | N |  |
| 111 | UI_BattleUpTip | N/A | 372 | 66 | 8 | 2/5/1 | 1/5/2 | N | N |  |
| 112 | UI_Beauty | 四边木栏（蒸笼标签）+横列表 | 1112 | 592 | 71 | 6/58/7 | 6/53/12 | Y | N |  |
| 113 | UI_BeautyBook | 功能开启&展示 | 326 | 667 | 13 | 1/9/3 | 1/9/3 | Y | N | ⚠ z=2.6 on height |
| 114 | UI_BeautyBookGet | 功能开启&展示 | 26 | 276 | 5 | 1/3/1 | 2/0/3 | N | N |  |
| 115 | UI_BeautyBookInfo | 待确认 | 369 | 234 | 19 | 1/13/5 | 0/16/3 | Y | Y |  |
| 116 | UI_BeautyCompAwardPreview | 上标题-中竖列表-下信息 | 851 | 443 | 25 | 3/19/3 | 2/22/1 | Y | N |  |
| 117 | UI_BeautyCompBuy | 使用弹框 | 472 | 275 | 19 | 2/14/3 | 2/15/2 | N | N |  |
| 118 | UI_BeautyCompEnter | 左-右 | 863 | 558 | 58 | 4/52/2 | 5/43/10 | Y | N |  |
| 119 | UI_BeautyCompMap | 左-右 | 1416 | 1158 | 58 | 2/55/1 | 1/54/3 | Y | Y | ⚠ z=4.1 on height |
| 120 | UI_BeautyCompRank | 上标题-中竖列表-下信息 | 802 | 387 | 37 | 3/30/4 | 4/30/3 | Y | N |  |
| 121 | UI_BeautyCompRecord | 左标签页-右框内-上标题-中竖列表-下信息 | 797 | 475 | 49 | 4/43/2 | 6/37/6 | Y | N |  |
| 122 | UI_BeautyCompResult | 展示-横条-条内信息 | 622 | 617 | 44 | 3/38/3 | 3/38/3 | Y | N |  |
| 123 | UI_BeautyCompRewardTips | 确认弹框 | 644 | 511 | 16 | 0/15/1 | 1/13/2 | N | N |  |
| 124 | UI_BeautyCompTitleChange | 展示-横条-左右对比 | 566 | 506 | 19 | 2/16/1 | 2/16/1 | Y | Y |  |
| 125 | UI_BeautyCompUpgrade | 功能开启&展示 | 574 | 346 | 15 | 4/10/1 | 1/12/2 | N | N | ⚠ z=2.8 on left_count |
| 126 | UI_BeautyCompView | 上标题-中横列表-下信息 | 361 | 399 | 11 | 1/10/0 | 2/8/1 | Y | N |  |
| 127 | UI_BeautyEditor | tips | 637 | 47 | 10 | 1/7/2 | 1/9/0 | Y | N |  |
| 128 | UI_BeautyFame | 一体框 | 786 | 400 | 49 | 1/42/6 | 1/44/4 | Y | Y |  |
| 129 | UI_BeautyFameUpSuc | 展示-横条-左右对比 | 891 | 369 | 26 | 1/22/3 | 0/24/2 | Y | N |  |
| 130 | UI_BeautyGetting | N/A | 1008 | 525 | 52 | 6/42/4 | 3/43/6 | Y | N |  |
| 131 | UI_BeautyInfo | 四边木栏（蒸笼标签）+左中右 | 1072 | 592 | 135 | 12/105/18 | 13/103/19 | Y | Y |  |
| 132 | UI_BeautyOutings | 左-右 | 582 | 534 | 17 | 1/15/1 | 2/12/3 | N | N |  |
| 133 | UI_BeautyPromoteSucc | N/A | 823 | 501 | 35 | 5/26/4 | 4/30/1 | Y | Y |  |
| 134 | UI_BeautyPropsUseSucc | 展示-横条-横列表 | 132 | 276 | 14 | 0/12/2 | 1/10/3 | Y | N |  |
| 135 | UI_BeautyRecuitTip | N/A | 297 | 527 | 8 | 2/4/2 | 0/7/1 | N | N |  |
| 136 | UI_BeautySelect | 上标题-中横列表-下信息 | 419 | 462 | 21 | 2/17/2 | 2/17/2 | Y | N |  |
| 137 | UI_BeautyShow | 四边木栏（蒸笼标签）+左中右 | 1074 | 608 | 64 | 5/47/12 | 6/54/4 | Y | N |  |
| 138 | UI_BeautyTalentSkillTips | tips | 6 | 317 | 14 | 2/12/0 | 1/11/2 | Y | N |  |
| 139 | UI_BeautyTalk | 功能开启&展示 | 579 | 446 | 18 | 0/17/1 | 1/14/3 | N | N | ⚠ z=2.6 on center_count |
| 140 | UI_BeautyTalkMore | 横列表 | 582 | 631 | 20 | 2/15/3 | 4/13/3 | Y | N |  |
| 141 | UI_BeautyTalkTip | 确认弹框 | 224 | 144 | 9 | 1/7/1 | 2/5/2 | N | N |  |
| 142 | UI_BeautyTransform | 左右对比 | 605 | 437 | 24 | 3/19/2 | 3/18/3 | N | N |  |
| 143 | UI_BeautyTransformPreview | 左右对比 | 355 | 524 | 22 | 3/13/6 | 2/16/4 | N | N |  |
| 144 | UI_BeautyTransformResult | 展示-横条-左右对比 | 637 | 684 | 22 | 2/17/3 | 4/15/3 | N | Y |  |
| 145 | UI_BeautyTravel | T型-上标题-左标签-右竖列表 | 981 | 567 | 37 | 2/31/4 | 3/33/1 | Y | N |  |
| 146 | UI_BeautyTravelSharedGift | 上标题-中竖列表-下信息 | 434 | 296 | 20 | 1/16/3 | 2/17/1 | Y | Y |  |
| 147 | UI_BeautyTravelTip | tips | 523 | 289 | 15 | 2/12/1 | 2/10/3 | N | N |  |
| 148 | UI_BeautyUpQuality | N/A | 1362 | 724 | 52 | 2/47/3 | 1/49/2 | Y | N |  |
| 149 | UI_BeautyUpSkillSucc | 展示-横条-条内信息 | 788 | 390 | 25 | 4/16/5 | 1/22/2 | Y | Y |  |
| 150 | UI_Billionaires | 左-右 | 1133 | 594 | 79 | 6/67/6 | 10/61/8 | Y | Y | ⚠ z=2.5 on top_count |
| 151 | UI_BillionairesRank | 左-右 | 488 | 252 | 18 | 3/14/1 | 2/15/1 | Y | N |  |
| 152 | UI_Black | 待确认 | 458 | 311 | 15 | 1/14/0 | 1/13/1 | N | N |  |
| 153 | UI_BlockBattleActFinish | 展示-横条-条内信息 | 664 | 402 | 25 | 4/18/3 | 3/18/4 | N | Y |  |
| 154 | UI_BlockBattleMap | 地图底 | 1421 | 1449 | 95 | 8/83/4 | 0/94/1 | Y | N |  |
| 155 | UI_BlockBattleMinMap | 地图底 | 1317 | 1411 | 21 | 6/13/2 | 1/19/1 | N | N |  |
| 156 | UI_BlockBattleRecord | 上标题-中竖列表-下信息 | 849 | 310 | 29 | 4/21/4 | 4/22/3 | Y | N |  |
| 157 | UI_BlockBattleResult | 展示-横条-左图-右信息 | 1060 | 836 | 32 | 7/21/4 | 3/24/5 | N | Y |  |
| 158 | UI_BlockBattleTarget | 上标题-中横列表-下信息 | 953 | 430 | 36 | 1/34/1 | 7/22/7 | Y | N |  |
| 159 | UI_BlockBattleTask | 左标签+右竖列表 | 1083 | 529 | 54 | 3/48/3 | 4/49/1 | Y | N |  |
| 160 | UI_BossRedPacket | 确认弹框 | 577 | 420 | 17 | 1/14/2 | 4/10/3 | N | N |  |
| 161 | UI_BossRedPacketGetReward | 活动打脸弹窗 | 610 | 312 | 15 | 1/12/2 | 7/1/7 | N | N |  |
| 162 | UI_BuffTips | N/A | 110 | 147 | 5 | 0/4/1 | 2/2/1 | Y | Y |  |
| 163 | UI_CPPopBtns | N/A | 487 | 248 | 7 | 0/6/1 | 1/5/1 | N | N |  |
| 164 | UI_Chat | 一体框 | 1635 | 919 | 191 | 2/173/16 | 9/172/10 | Y | Y | ⚠ z=4.4 on middle_count |
| 165 | UI_ChatSmall | N/A | 422 | 79 | 17 | 1/11/5 | 5/10/2 | N | N |  |
| 166 | UI_ChildBeauty | 左右艺术设计+横列表 | 400 | 507 | 27 | 3/22/2 | 2/20/5 | Y | N |  |
| 167 | UI_ChildCultivateVit | tips | 173 | 208 | 9 | 0/7/2 | 2/6/1 | Y | N |  |
| 168 | UI_ChildFamily | 四边木栏（蒸笼标签）+左中右 | 1071 | 592 | 51 | 5/39/7 | 5/37/9 | Y | N |  |
| 169 | UI_ChildGetTip | 大背景-展示 | 450 | 504 | 19 | 3/13/3 | 2/14/3 | N | N |  |
| 170 | UI_ChildGraduateTip | 大背景-展示 | 691 | 522 | 34 | 1/30/3 | 3/27/4 | N | N |  |
| 171 | UI_ChildInfo | 四边木栏（蒸笼标签）+左标签+中图+右信息 | 1081 | 626 | 145 | 10/113/22 | 14/118/13 | Y | N |  |
| 172 | UI_ChildMail | 确认弹框 | 681 | 332 | 13 | 1/10/2 | 2/8/3 | N | N |  |
| 173 | UI_ChildMarry | 左艺术设计+左-右 | 1020 | 553 | 83 | 7/65/11 | 7/67/9 | Y | N |  |
| 174 | UI_ChildMarryFailTip | 展示-横条-条内信息 | 7 | 85 | 5 | 1/3/1 | 1/3/1 | N | Y | ⚠ z=2.7 on width |
| 175 | UI_ChildMarrySuccTip | N/A | 630 | 235 | 16 | 2/12/2 | 2/9/5 | N | N |  |
| 176 | UI_ChildMessageTip | 确认弹框 | 256 | 197 | 10 | 1/7/2 | 2/5/3 | N | N |  |
| 177 | UI_ChildPublicPropose | 上标题-中竖列表-下信息 | 652 | 392 | 11 | 2/8/1 | 1/9/1 | N | N |  |
| 178 | UI_ChildRecoverVit | 使用弹框 | 496 | 409 | 22 | 4/16/2 | 2/17/3 | N | N |  |
| 179 | UI_ChildRecoverVitSucc | 展示-横条-横列表 | 740 | 586 | 19 | 2/16/1 | 2/13/4 | Y | Y |  |
| 180 | UI_ChildRenameSuccTip | 展示-横条-横列表 | 740 | 461 | 14 | 1/12/1 | 1/10/3 | Y | N |  |
| 181 | UI_ChildRenameTip | 确认弹框 | 239 | 262 | 20 | 0/18/2 | 2/17/1 | N | Y |  |
| 182 | UI_ChildResume | 左广告图-右列表 | 618 | 332 | 16 | 3/9/4 | 1/11/4 | Y | N |  |
| 183 | UI_ChildSchool | 四边木栏（蒸笼标签）+左中右 | 1105 | 530 | 63 | 6/54/3 | 8/48/7 | Y | N |  |
| 184 | UI_ChildSchoolUp | 展示-横条-上图-下信息 | 895 | 598 | 13 | 2/8/3 | 2/9/2 | N | Y |  |
| 185 | UI_ChildSpecialSuitors | 左标签+右竖列表 | 911 | 358 | 30 | 2/22/6 | 2/25/3 | Y | N |  |
| 186 | UI_ChildSpecifiedPropose | T型-上标题-左-右 | 706 | 421 | 32 | 5/25/2 | 5/25/2 | Y | N |  |
| 187 | UI_ChildSuitorInfo | 左广告图-右列表 | 740 | 337 | 23 | 2/18/3 | 1/20/2 | Y | N |  |
| 188 | UI_ChildSuitors | 左标签+右竖列表 | 892 | 253 | 27 | 1/21/5 | 3/23/1 | Y | N |  |
| 189 | UI_ChildTravelApply | 左右艺术设计+一体 | 416 | 371 | 18 | 4/11/3 | 3/11/4 | N | N |  |
| 190 | UI_ChildTravelFailTip | 左右艺术设计+一体 | 731 | 456 | 18 | 1/15/2 | 1/14/3 | Y | N |  |
| 191 | UI_ChildTravelList | 上标题-中横列表-下信息 | 837 | 457 | 36 | 4/28/4 | 3/26/7 | Y | N |  |
| 192 | UI_ChildTravelSuccTip | 大背景-展示 | 562 | 450 | 14 | 3/9/2 | 1/10/3 | N | N |  |
| 193 | UI_ChildTravelTip | 大背景-展示 | 511 | 444 | 19 | 2/15/2 | 2/14/3 | N | N |  |
| 194 | UI_ChildUpSchoolTip | 展示-横条-上图-下信息 | 787 | 661 | 20 | 3/14/3 | 5/12/3 | N | Y |  |
| 195 | UI_ChildUpgradeSuccTip | 展示-横条-横列表 | 747 | 732 | 22 | 2/17/3 | 4/16/2 | Y | Y |  |
| 196 | UI_ChildWaitPropose | 左-右 | 393 | 389 | 22 | 5/12/5 | 1/19/2 | N | N |  |
| 197 | UI_ChoosingCar | 多列 | 896 | 788 | 182 | 12/155/15 | 10/157/15 | Y | Y |  |
| 198 | UI_CoatingActiveTips | 确认弹框 | 570 | 739 | 16 | 0/15/1 | 2/11/3 | N | N | ⚠ z=4.4 on height |
| 199 | UI_CoatingInfo | 上标题-中横列表-下信息 | 933 | 568 | 43 | 4/36/3 | 3/34/6 | Y | N |  |
| 200 | UI_CoatingMain | 大背景-展示 | 986 | 639 | 41 | 3/31/7 | 4/28/9 | N | N |  |
| 201 | UI_CoatingPreview2 | 上标题-中横列表-下信息 | 696 | 421 | 27 | 1/25/1 | 2/23/2 | Y | N |  |
| 202 | UI_CoatingResolveTips | 使用弹框 | 570 | 739 | 17 | 0/16/1 | 2/12/3 | Y | N | ⚠ z=3.5 on height |
| 203 | UI_CoatingSelectUpLevelMat | 上标题-中横列表-下信息 | 639 | 281 | 31 | 3/26/2 | 3/22/6 | Y | N |  |
| 204 | UI_CoatingSelectUpStarMat | 上标题-中横列表-下信息 | 152 | 280 | 26 | 2/23/1 | 2/20/4 | Y | N |  |
| 205 | UI_CoatingSkillDescTips | N/A | 107 | 178 | 3 | 2/0/1 | 2/0/1 | N | Y |  |
| 206 | UI_CoatingTask | 上标题-中竖列表-下信息 | 568 | 93 | 24 | 4/17/3 | 2/19/3 | Y | N |  |
| 207 | UI_CoatingUpgrade | 左右对比 | 468 | 526 | 29 | 2/24/3 | 2/24/3 | Y | N |  |
| 208 | UI_CombineAccounting | T型-上标题-左-右 | 678 | 487 | 40 | 1/36/3 | 6/30/4 | Y | N |  |
| 209 | UI_CombineLeader | T型-上标题-左-右 | 669 | 466 | 44 | 1/36/7 | 4/35/5 | Y | N |  |
| 210 | UI_CombineMain | mainUI | 953 | 184 | 21 | 2/18/1 | 2/17/2 | N | N |  |
| 211 | UI_CombineManager | T型-上标题-左-右 | 501 | 465 | 33 | 3/22/8 | 4/27/2 | Y | N |  |
| 212 | UI_CombineManagerStar | 上标题-中横列表-下信息 | 117 | 302 | 20 | 0/18/2 | 3/14/3 | Y | N |  |
| 213 | UI_CombinePersonnel | T型-上标题-左-右 | 592 | 504 | 54 | 1/48/5 | 5/45/4 | Y | N |  |
| 214 | UI_CombinePersonnelGuest | 左-右 | 502 | 342 | 30 | 1/25/4 | 4/23/3 | Y | N |  |
| 215 | UI_CombinePublicity | T型-上标题-左-右 | 528 | 473 | 34 | 1/28/5 | 5/25/4 | N | N |  |
| 216 | UI_CombinePublicityCup | T型-上标题-左标签-右竖列表 | 406 | 472 | 23 | 1/22/0 | 4/17/2 | Y | N |  |
| 217 | UI_CombineRemould | 上标题-中横列表-下信息 | 828 | 528 | 47 | 6/38/3 | 3/38/6 | Y | Y | ⚠ z=3.4 on left_count |
| 218 | UI_CombineRemouldSucc | 展示-横条-左右对比 | 487 | 415 | 14 | 1/12/1 | 1/11/2 | N | Y |  |
| 219 | UI_CombineRemouldTips | 确认弹框 | 439 | 286 | 42 | 4/35/3 | 7/32/3 | Y | Y | ⚠ z=4.9 on top_count |
| 220 | UI_CombineTactic | T型-上标题-左-右 | 639 | 486 | 33 | 1/26/6 | 2/29/2 | N | N |  |
| 221 | UI_CombineTacticInfo | 一体框 | 740 | 435 | 33 | 5/27/1 | 3/27/3 | Y | N |  |
| 222 | UI_CombineUpSucc | 展示-横条-左图-右信息 | 789 | 638 | 36 | 5/28/3 | 4/29/3 | Y | Y |  |
| 223 | UI_CombineUpgradeCond | 上标题-中竖列表-下信息 | 482 | 234 | 17 | 2/13/2 | 3/13/1 | N | N |  |
| 224 | UI_CommandMonitor | 测试界面 | 1626 | 698 | 59 | 1/56/2 | 12/44/3 | Y | Y |  |
| 225 | UI_CommonComposite | 使用弹框 | 475 | 361 | 21 | 2/17/2 | 2/18/1 | Y | N |  |
| 226 | UI_CommonDigit | N/A | 270 | 176 | 17 | 3/11/3 | 4/9/4 | N | Y |  |
| 227 | UI_CommonGetItems | 展示-横条-横列表 | 532 | 370 | 23 | 2/20/1 | 4/17/2 | Y | Y |  |
| 228 | UI_CommonPurchase | 使用弹框 | 449 | 383 | 23 | 1/20/2 | 2/18/3 | N | N |  |
| 229 | UI_CommonRoleInfo | 一体框 | 988 | 439 | 36 | 3/29/4 | 6/26/4 | N | Y |  |
| 230 | UI_CommonSkin | tips | 1128 | 717 | 78 | 1/74/3 | 4/68/6 | Y | N | ⚠ z=6.7 on center_count |
| 231 | UI_CommonUseSucc | 展示-横条-条内信息 | 740 | 448 | 18 | 2/14/2 | 3/12/3 | Y | Y |  |
| 232 | UI_ContinueRechargeAct | 左标签+中图+右信息 | 1052 | 450 | 44 | 7/33/4 | 4/36/4 | N | N |  |
| 233 | UI_CreateRole | 全屏背景界面 | 1340 | 599 | 16 | 3/11/2 | 1/12/3 | N | Y |  |
| 234 | UI_CupGetting | tips | 2 | 327 | 6 | 1/4/1 | 1/3/2 | N | N |  |
| 235 | UI_CupInfo | tips | 300 | 274 | 13 | 2/7/4 | 1/11/1 | Y | N |  |
| 236 | UI_CyberIllusionAuto | 确认弹框 | 532 | 304 | 14 | 1/8/5 | 2/11/1 | N | N |  |
| 237 | UI_CyberIllusionBreakThrough | 展示-横条-左右对比 | 1132 | 705 | 24 | 3/17/4 | 3/18/3 | Y | Y |  |
| 238 | UI_CyberIllusionEquip | 左右对比 | 462 | 362 | 24 | 2/21/1 | 3/16/5 | Y | N |  |
| 239 | UI_CyberIllusionEquipMessage | tips | 449 | 238 | 12 | 1/10/1 | 3/7/2 | Y | N |  |
| 240 | UI_CyberIllusionMain | 全屏背景界面 | 865 | 611 | 91 | 6/73/12 | 9/71/11 | Y | Y | ⚠ z=2.7 on right_count |
| 241 | UI_CyberIllusionRemouldSucc | 展示-横条-左图-右信息 | 587 | 328 | 12 | 1/10/1 | 3/6/3 | Y | Y |  |
| 242 | UI_CyberIllusionRoleUp | 左右对比 | 1079 | 675 | 20 | 2/15/3 | 3/14/3 | Y | Y |  |
| 243 | UI_CyberIllusionSelectMarket | 左广告图-右列表 | 588 | 391 | 25 | 6/17/2 | 3/21/1 | N | N |  |
| 244 | UI_CyberIllusionSkill | 左标签+中图+右信息 | 1016 | 460 | 43 | 5/35/3 | 5/32/6 | Y | N |  |
| 245 | UI_CyberIllusionSkillTip | N/A | 288 | 248 | 11 | 2/7/2 | 1/9/1 | N | N |  |
| 246 | UI_CyberIllusionSource | N/A | 250 | 247 | 10 | 0/8/2 | 3/3/4 | Y | N |  |
| 247 | UI_CyberIllusionUpSucc | 展示-横条-左图-右信息 | 536 | 497 | 16 | 1/13/2 | 3/11/2 | Y | Y |  |
| 248 | UI_CyberPve | 左-中-右 | 870 | 466 | 57 | 3/44/10 | 7/45/5 | Y | N |  |
| 249 | UI_CyberPveResult | 展示-横条-左图-右信息 | 1227 | 882 | 35 | 4/28/3 | 2/29/4 | Y | Y |  |
| 250 | UI_DailyGift | panel | 1086 | 302 | 28 | 3/23/2 | 4/22/2 | Y | Y |  |
| 251 | UI_DailyRefreshTips | tips | 226 | 67 | 6 | 3/1/2 | 2/1/3 | N | N |  |
| 252 | UI_DailySign | 左-右 | 766 | 499 | 58 | 3/50/5 | 6/50/2 | Y | Y |  |
| 253 | UI_DailySignBadInfo | 确认弹框 | 235 | 447 | 16 | 1/14/1 | 3/11/2 | N | Y |  |
| 254 | UI_DailySystem | panel | 903 | 644 | 45 | 4/39/2 | 4/38/3 | Y | N |  |
| 255 | UI_DailyTips | N/A | 185 | 124 | 5 | 1/2/2 | 1/3/1 | N | N |  |
| 256 | UI_DebugLogPanel | 确认弹框 | 501 | 358 | 16 | 1/13/2 | 1/12/3 | Y | N |  |
| 257 | UI_DivineTip | tips | 276 | 100 | 6 | 2/3/1 | 1/4/1 | N | N |  |
| 258 | UI_ExpGetPath | 左-右 | 520 | 236 | 28 | 11/12/5 | 5/18/5 | Y | N |  |
| 259 | UI_Expand | panel+入口 | 2149 | 705 | 114 | 1/112/1 | 5/103/6 | Y | N |  |
| 260 | UI_ExpandAgentResult | 展示-横条-横列表 | 699 | 426 | 43 | 2/38/3 | 0/42/1 | Y | N |  |
| 261 | UI_ExpandAgentStart | 确认弹框 | 54 | 310 | 10 | 0/9/1 | 1/8/1 | N | N |  |
| 262 | UI_ExpandAgentStop | 确认弹框 | 402 | 310 | 10 | 1/8/1 | 2/6/2 | N | N |  |
| 263 | UI_ExpandAisleMap | panel | 829 | 614 | 30 | 3/25/2 | 6/19/5 | Y | N |  |
| 264 | UI_ExpandAisleResult | 展示-横条-条内信息 | 697 | 636 | 30 | 4/20/6 | 4/22/4 | Y | Y |  |
| 265 | UI_ExpandAisleTaskProUp | N/A | 92 | 196 | 8 | 1/5/2 | 1/7/0 | N | N |  |
| 266 | UI_ExpandAkfPreview | T型-上标题-左标签-右竖列表 | 1066 | 291 | 40 | 1/35/4 | 5/35/0 | N | Y |  |
| 267 | UI_ExpandAkfReward | 确认弹框 | 291 | 593 | 26 | 2/21/3 | 2/20/4 | N | N | ⚠ z=2.9 on height |
| 268 | UI_ExpandAkfSpeed | 确认弹框 | 44 | 376 | 19 | 2/16/1 | 3/14/2 | N | N |  |
| 269 | UI_ExpandAutoResult | 展示-横条-横列表 | 828 | 574 | 28 | 3/23/2 | 1/26/1 | Y | Y |  |
| 270 | UI_ExpandAutoTip | 确认弹框 | 240 | 250 | 12 | 3/8/1 | 1/10/1 | N | N |  |
| 271 | UI_ExpandBattle | panel+入口 | 989 | 576 | 31 | 4/25/2 | 3/22/6 | Y | N |  |
| 272 | UI_ExpandBuffResult | 展示-横条-条内信息 | 57 | 250 | 11 | 0/10/1 | 1/8/2 | Y | N |  |
| 273 | UI_ExpandDispatch | 上标题-中横列表-下信息 | 791 | 564 | 33 | 0/32/1 | 3/25/5 | Y | N |  |
| 274 | UI_ExpandDispatchList | 确认弹框 | 418 | 432 | 17 | 1/13/3 | 1/14/2 | Y | N |  |
| 275 | UI_ExpandEventNew | 展示-横条-条内信息 | 19 | 96 | 3 | 1/1/1 | 1/1/1 | N | N | ⚠ z=2.7 on width |
| 276 | UI_ExpandEventResult | 展示-横条-条内信息 | 640 | 504 | 35 | 3/31/1 | 1/33/1 | Y | N |  |
| 277 | UI_ExpandEventSelect | 展示-横条-条内信息 | 642 | 356 | 12 | 2/9/1 | 2/9/1 | N | N |  |
| 278 | UI_ExpandEventTip | tips | 13 | 104 | 6 | 1/4/1 | 2/1/3 | N | N |  |
| 279 | UI_ExpandFogMap | 上标题-中竖列表-下信息 | 913 | 550 | 23 | 6/13/4 | 2/20/1 | Y | N |  |
| 280 | UI_ExpandFogResult | 展示-横条-条内信息 | 789 | 632 | 31 | 3/24/4 | 3/24/4 | Y | Y |  |
| 281 | UI_ExpandMap | 左标签+框内整图 | 1049 | 601 | 125 | 10/101/14 | 10/102/13 | Y | Y |  |
| 282 | UI_ExpandMapNewTip | tips | 9 | 90 | 8 | 5/0/3 | 2/5/1 | N | N |  |
| 283 | UI_ExpandNameTip | tips | 1 | 14 | 6 | 0/5/1 | 3/0/3 | N | N |  |
| 284 | UI_ExpandRank | 左-右 | 706 | 477 | 29 | 4/20/5 | 2/25/2 | Y | N |  |
| 285 | UI_ExpandResult | 展示-横条-条内信息 | 779 | 426 | 35 | 2/31/2 | 0/34/1 | Y | Y |  |
| 286 | UI_ExpandResultFail | 展示-横条-条内信息 | 512 | 313 | 17 | 2/14/1 | 1/15/1 | N | Y |  |
| 287 | UI_ExpandRoll | 确认弹框 | 407 | 386 | 11 | 1/9/1 | 3/7/1 | Y | N |  |
| 288 | UI_ExpandSeaFailResult | 展示-横条-条内信息 | 510 | 323 | 19 | 1/16/2 | 1/17/1 | N | Y |  |
| 289 | UI_ExpandSeaResult | 展示-横条-条内信息 | 790 | 456 | 34 | 1/29/4 | 1/32/1 | Y | N |  |
| 290 | UI_ExpandSidInfo | tips | 364 | 262 | 27 | 1/24/2 | 2/24/1 | N | N |  |
| 291 | UI_FashionShop | 左-中-右 | 1117 | 642 | 38 | 5/27/6 | 7/25/6 | Y | N |  |
| 292 | UI_FashionShopBuySucc | N/A | 913 | 466 | 20 | 4/14/2 | 1/18/1 | N | N |  |
| 293 | UI_FashionShopEff | tips | 334 | 341 | 32 | 6/21/5 | 3/25/4 | Y | N | ⚠ z=3 on left_count |
| 294 | UI_FirstChargeBonus | panel | 620 | 450 | 30 | 1/26/3 | 3/25/2 | Y | N |  |
| 295 | UI_FirstStarTips | 展示-横条-左右对比 | 438 | 455 | 19 | 3/15/1 | 2/15/2 | N | N |  |
| 296 | UI_FloatCoinTips | tips | 0 | 0 | 2 | 0/2/0 | 0/2/0 | Y | N |  |
| 297 | UI_FloatMoneyTips | tips | 150 | 17 | 4 | 1/2/1 | 1/2/1 | N | N |  |
| 298 | UI_FloatStrTip | tips | 516 | 648 | 11 | 2/8/1 | 1/9/1 | N | N |  |
| 299 | UI_FlyItem | tips | 1 | 21 | 11 | 3/0/8 | 1/9/1 | N | N | ⚠ z=4.2 on right_count |
| 300 | UI_FlyItem1 | tips | 0 | 0 | 3 | 0/3/0 | 0/3/0 | N | N |  |
| 301 | UI_FlyItem2 | tips | 33 | 69 | 10 | 0/9/1 | 1/8/1 | N | N |  |
| 302 | UI_FlyItem4 | N/A | 76 | 65 | 9 | 1/7/1 | 0/8/1 | N | N |  |
| 303 | UI_FlyItem5 | N/A | 549 | 313 | 4 | 1/2/1 | 1/2/1 | Y | N |  |
| 304 | UI_FriendsMain | 左艺术设计+左-右 | 861 | 482 | 52 | 5/41/6 | 5/44/3 | Y | N |  |
| 305 | UI_FuLiDaTingWeiXin | 左标签+右竖列表 | 815 | 441 | 53 | 5/44/4 | 3/46/4 | Y | Y |  |
| 306 | UI_FullSceneTips | tips | - | - | - | - | - | - | - |  |
| 307 | UI_FuncOpen | 功能开启&展示 | 4 | 191 | 4 | 1/1/2 | 2/0/2 | N | N |  |
| 308 | UI_FuncOpenTip2 | 功能开启&展示 | 690 | 482 | 12 | 1/10/1 | 1/9/2 | N | N |  |
| 309 | UI_FuncPreview | T型-上标题-左-右 | 968 | 441 | 31 | 1/28/2 | 3/23/5 | Y | N |  |
| 310 | UI_FuncUnlock | tips | 507 | 128 | 16 | 2/11/3 | 4/10/2 | Y | N |  |
| 311 | UI_Fund | 左-右 | 768 | 626 | 73 | 4/64/5 | 5/62/6 | Y | Y |  |
| 312 | UI_FundBeautyInfo | tips | 506 | 537 | 25 | 4/16/5 | 5/17/3 | Y | N | ⚠ z=2.5 on top_count |
| 313 | UI_FundGuestInfo | tips | 649 | 585 | 53 | 5/42/6 | 5/43/5 | Y | N | ⚠ z=3.8 on total_nodes |
| 314 | UI_FundPreview | tips | 271 | 362 | 21 | 2/19/0 | 0/19/2 | Y | N |  |
| 315 | UI_GM | N/A | 1181 | 539 | 103 | 19/63/21 | 15/84/4 | Y | Y |  |
| 316 | UI_GachaAutoTypeSelect | 上标题-中竖列表-下信息 | 747 | 209 | 22 | 2/17/3 | 2/19/1 | Y | N |  |
| 317 | UI_GachaCoinShop | 四边木栏+左右-宽列表 | 620 | 536 | 49 | 5/44/0 | 2/45/2 | Y | N |  |
| 318 | UI_GachaExchange | 墙+小旗+横列表 | 671 | 510 | 44 | 5/39/0 | 7/32/5 | Y | N |  |
| 319 | UI_GachaExchangeConfirm | 确认弹框 | 445 | 288 | 23 | 2/18/3 | 2/19/2 | N | Y |  |
| 320 | UI_GachaJackpot | 全屏获得新奖励 | 645 | 379 | 12 | 2/7/3 | 3/7/2 | N | Y |  |
| 321 | UI_GachaLimitWish | T型-上标题-左-右 | 642 | 413 | 47 | 5/37/5 | 5/37/5 | Y | N |  |
| 322 | UI_GachaLuckTips | tips | 236 | 287 | 12 | 1/11/0 | 1/9/2 | N | N |  |
| 323 | UI_GachaMain | panel | 835 | 637 | 45 | 2/38/5 | 5/36/4 | N | N |  |
| 324 | UI_GachaPreview | 上标题-中竖列表-下信息 | 752 | 396 | 43 | 5/35/3 | 3/38/2 | Y | N |  |
| 325 | UI_GachaResult | 展示-横条-条内信息 | 564 | 624 | 33 | 3/27/3 | 5/24/4 | Y | Y |  |
| 326 | UI_GachaSwitchBeautyPool | 横列表 | 447 | 477 | 17 | 1/15/1 | 2/12/3 | Y | N |  |
| 327 | UI_GachaSwitchPool | 横列表 | 447 | 337 | 17 | 1/15/1 | 1/13/3 | Y | N |  |
| 328 | UI_GetPaths | 左-右 | 501 | 262 | 34 | 4/24/6 | 1/30/3 | Y | N |  |
| 329 | UI_GetPaths2 | tips | 477 | 395 | 14 | 1/9/4 | 2/10/2 | N | N |  |
| 330 | UI_GetPaths3 | tips | 556 | 316 | 13 | 3/9/1 | 3/9/1 | Y | N |  |
| 331 | UI_GoGuestTip | 确认弹框 | 38 | 157 | 9 | 1/8/0 | 3/4/2 | N | N |  |
| 332 | UI_GoodsActive | tips | 785 | 721 | 18 | 3/12/3 | 3/12/3 | N | Y | ⚠ z=2.7 on height |
| 333 | UI_GrowSystem | 四边木栏（蒸笼标签）底 | 1069 | 594 | 23 | 5/17/1 | 3/15/5 | N | N |  |
| 334 | UI_Guest | 四边木栏（蒸笼标签）+横列表 | 950 | 634 | 44 | 3/35/6 | 7/30/7 | Y | N |  |
| 335 | UI_GuestATKUpPath | tips | 73 | 136 | 12 | 0/10/2 | 1/10/1 | Y | N |  |
| 336 | UI_GuestActive | 全屏获得新奖励 | 1316 | 784 | 44 | 5/36/3 | 2/36/6 | N | Y |  |
| 337 | UI_GuestActiveSkill | N/A | 529 | 535 | 21 | 1/19/1 | 2/17/2 | N | N |  |
| 338 | UI_GuestAttrUpTip | tips | 502 | 133 | 7 | 1/5/1 | 2/1/4 | N | N |  |
| 339 | UI_GuestAureole | 活动打脸弹窗 | 1044 | 547 | 27 | 1/23/3 | 2/21/4 | N | N |  |
| 340 | UI_GuestAureoleSkillSucc | 展示-横条-条内信息 | 391 | 271 | 12 | 2/7/3 | 2/8/2 | N | Y |  |
| 341 | UI_GuestAureoleTips | 一体框 | 591 | 306 | 30 | 3/25/2 | 5/23/2 | N | N |  |
| 342 | UI_GuestBuy | 活动打脸弹窗 | 954 | 618 | 40 | 3/33/4 | 5/31/4 | N | N |  |
| 343 | UI_GuestCollect | 左右艺术设计+横列表 | 642 | 572 | 32 | 3/29/0 | 3/26/3 | Y | N |  |
| 344 | UI_GuestDivine | 左艺术设计+左-右 | 663 | 439 | 49 | 5/37/7 | 3/39/7 | N | N |  |
| 345 | UI_GuestDivineTips | 一体框 | 610 | 311 | 12 | 2/8/2 | 0/11/1 | Y | N |  |
| 346 | UI_GuestEquipMount | 左-右 | 588 | 523 | 72 | 6/59/7 | 2/67/3 | Y | N |  |
| 347 | UI_GuestFashionActive | N/A | 950 | 397 | 23 | 2/19/2 | 2/19/2 | Y | N |  |
| 348 | UI_GuestFetterAdd | 确认弹框 | 62 | 353 | 17 | 1/15/1 | 1/15/1 | Y | N |  |
| 349 | UI_GuestGetPath | 上标题-中竖列表-下信息 | 668 | 284 | 25 | 2/19/4 | 4/20/1 | Y | N |  |
| 350 | UI_GuestGetSkinItem | N/A | 665 | 206 | 8 | 1/6/1 | 1/6/1 | N | Y |  |
| 351 | UI_GuestInfo | 四边木栏（蒸笼标签）+左中右 | 1077 | 620 | 206 | 13/160/33 | 26/153/27 | Y | Y | ⚠ z=2.5 on total_nodes |
| 352 | UI_GuestManagerSkinBuy | 活动打脸弹窗 | 947 | 627 | 31 | 2/25/4 | 1/25/5 | Y | N |  |
| 353 | UI_GuestNotActive | 四边木栏（蒸笼标签）+左中右 | 905 | 502 | 60 | 7/42/11 | 9/46/5 | Y | N |  |
| 354 | UI_GuestPath | tips | 184 | 226 | 11 | 0/10/1 | 3/7/1 | Y | N |  |
| 355 | UI_GuestPromote | 活动打脸弹窗 | 986 | 614 | 57 | 4/49/4 | 3/49/5 | N | N |  |
| 356 | UI_GuestPromoteItem | tips | 294 | 131 | 6 | 1/4/1 | 1/5/0 | N | Y |  |
| 357 | UI_GuestPromoteSucc | N/A | 745 | 391 | 36 | 4/28/4 | 1/34/1 | N | N |  |
| 358 | UI_GuestQueryAttr | T型-上标题-左标签-右竖列表 | 810 | 561 | 46 | 9/29/8 | 2/39/5 | Y | Y |  |
| 359 | UI_GuestRareTip | tips | 400 | 34 | 14 | 2/11/1 | 0/12/2 | Y | N |  |
| 360 | UI_GuestRechargeBuy | 活动打脸弹窗 | 853 | 593 | 39 | 4/30/5 | 3/29/7 | N | Y |  |
| 361 | UI_GuestSelectCard | 确认弹框 | 509 | 319 | 18 | 1/16/1 | 1/13/4 | Y | N |  |
| 362 | UI_GuestSetInfo | 活动打脸弹窗 | 1088 | 582 | 53 | 2/49/2 | 7/38/8 | Y | N |  |
| 363 | UI_GuestSetMain | 横列表 | 571 | 413 | 16 | 2/14/0 | 3/9/4 | Y | N |  |
| 364 | UI_GuestStarPreview | 上标题-中竖列表-下信息 | 790 | 427 | 29 | 3/24/2 | 1/27/1 | Y | N |  |
| 365 | UI_GuestStarSucc | 展示-横条-条内信息 | 415 | 412 | 23 | 4/17/2 | 3/19/1 | N | Y |  |
| 366 | UI_GuestSupplyInfo | 确认弹框 | 439 | 266 | 14 | 3/9/2 | 1/11/2 | Y | N |  |
| 367 | UI_GuestSupplyPath | tips | 637 | 249 | 18 | 4/12/2 | 4/13/1 | Y | N |  |
| 368 | UI_GuestSupplyRecords | tips | 538 | 281 | 19 | 2/15/2 | 1/16/2 | Y | N |  |
| 369 | UI_GuestTalentSkill | 展示-横条-条内信息 | 704 | 408 | 18 | 2/14/2 | 2/14/2 | N | Y |  |
| 370 | UI_GuestUp | 上标题-中横列表-下信息 | 285 | 258 | 19 | 3/14/2 | 1/18/0 | Y | N |  |
| 371 | UI_GuestUpQuality | N/A | 1299 | 535 | 40 | 1/37/2 | 0/36/4 | Y | N |  |
| 372 | UI_GuestUseItem | 使用弹框 | 472 | 346 | 21 | 2/17/2 | 2/18/1 | N | N |  |
| 373 | UI_Guide | tips | 440 | 84 | 9 | 1/8/0 | 1/7/1 | N | N |  |
| 374 | UI_GuildActivity | 左标签+右竖列表 | 942 | 572 | 70 | 3/55/12 | 11/53/6 | Y | N | ⚠ z=2.9 on right_count |
| 375 | UI_GuildApply | 确认弹框 | 395 | 265 | 15 | 4/6/5 | 2/10/3 | N | Y |  |
| 376 | UI_GuildApplyList | 上标题-中竖列表-下信息 | 941 | 475 | 31 | 6/21/4 | 2/21/8 | Y | N | ⚠ z=4.4 on bottom_count |
| 377 | UI_GuildBuild | 上标题-中横列表-下信息 | 559 | 465 | 33 | 3/29/1 | 5/23/5 | Y | N |  |
| 378 | UI_GuildChallangeLevel | 上标题-中竖列表-下信息 | 360 | 519 | 28 | 2/26/0 | 2/24/2 | Y | N |  |
| 379 | UI_GuildChallengeContrib | T型-上标题-左标签-右竖列表 | 646 | 393 | 34 | 5/26/3 | 2/30/2 | Y | N |  |
| 380 | UI_GuildColorCodeDesc | tips | 449 | 183 | 11 | 3/6/2 | 4/3/4 | N | Y |  |
| 381 | UI_GuildCreate | 左艺术设计+左-右 | 656 | 400 | 33 | 2/24/7 | 4/23/6 | Y | N |  |
| 382 | UI_GuildDunChallengeRecord | 待确认 | 902 | 127 | 11 | 1/9/1 | 1/10/0 | Y | N |  |
| 383 | UI_GuildDunExpReward | tips | 368 | 102 | 12 | 1/9/2 | 1/9/2 | Y | N |  |
| 384 | UI_GuildDunGroupRankAndReward | 上标题-中上标签-中竖列表-下信息 | 531 | 462 | 29 | 4/24/1 | 3/24/2 | Y | N |  |
| 385 | UI_GuildDunLineUp | 上标题-中横列表-下信息 | 104 | 464 | 15 | 3/11/1 | 3/8/4 | Y | N |  |
| 386 | UI_GuildDunRankAndReward | 上标题-中上标签-中竖列表-下信息 | 531 | 462 | 30 | 4/25/1 | 2/25/3 | Y | N |  |
| 387 | UI_GuildDungeonBattle | panel+入口 | 1058 | 525 | 27 | 7/13/7 | 4/15/8 | N | N |  |
| 388 | UI_GuildDungeonBattlePhase | 展示-横条-条内信息 | 413 | 264 | 16 | 1/13/2 | 1/13/2 | Y | N |  |
| 389 | UI_GuildDungeonBattleResult | 展示-横条-条内信息 | 306 | 182 | 14 | 2/11/1 | 1/10/3 | Y | N |  |
| 390 | UI_GuildDungeonBattleSucc | 展示-横条-条内信息 | 413 | 395 | 16 | 1/13/2 | 1/13/2 | Y | N |  |
| 391 | UI_GuildDungeonBattleTail | 展示-横条-条内信息 | 454 | 356 | 18 | 2/12/4 | 2/13/3 | Y | N |  |
| 392 | UI_GuildDungeonChallenge | panel+入口 | 946 | 522 | 52 | 11/28/13 | 9/34/9 | N | N |  |
| 393 | UI_GuildDungeonEliteBattle | panel+入口 | 944 | 564 | 49 | 10/28/11 | 13/26/10 | N | N | ⚠ z=2.6 on top_count |
| 394 | UI_GuildDungeonsList | panel | 945 | 558 | 29 | 3/24/2 | 4/20/5 | Y | N |  |
| 395 | UI_GuildDungeonsNew | 四边木栏（蒸笼标签）底 | 620 | 357 | 21 | 3/18/0 | 3/17/1 | N | Y |  |
| 396 | UI_GuildEliteAttackUp | tips | 429 | 269 | 14 | 2/11/1 | 2/11/1 | Y | N |  |
| 397 | UI_GuildGroupBuyNew | panel | 799 | 431 | 59 | 6/41/12 | 6/40/13 | Y | N | ⚠ z=3.7 on bottom_count |
| 398 | UI_GuildHaggleRank | 上标题-中竖列表-下信息 | 662 | 360 | 19 | 4/10/5 | 1/15/3 | Y | N |  |
| 399 | UI_GuildHallOfHonor | panel | 681 | 493 | 29 | 6/19/4 | 2/24/3 | Y | N |  |
| 400 | UI_GuildHallOfHonorTips | 确认弹框 | 356 | 264 | 12 | 1/10/1 | 2/8/2 | N | N |  |
| 401 | UI_GuildHonorRecord | 上标题-中竖列表-下信息 | 340 | 139 | 10 | 6/2/2 | 0/9/1 | Y | N |  |
| 402 | UI_GuildHonorUnLock | panel | 482 | 381 | 15 | 3/7/5 | 2/10/3 | N | N |  |
| 403 | UI_GuildList | 四边木栏（蒸笼标签）底 | 937 | 515 | 50 | 4/36/10 | 7/36/7 | Y | N |  |
| 404 | UI_GuildLobby | panel | 681 | 510 | 75 | 11/52/12 | 13/56/6 | Y | N | ⚠ z=2.9 on top_count |
| 405 | UI_GuildMain | 四边木栏（蒸笼标签）底 | 620 | 342 | 26 | 5/17/4 | 4/20/2 | N | Y |  |
| 406 | UI_GuildManager | panel | 430 | 535 | 10 | 2/8/0 | 1/7/2 | Y | N |  |
| 407 | UI_GuildMemberBattle | 战斗 | 1270 | 554 | 72 | 1/68/3 | 5/58/9 | Y | N |  |
| 408 | UI_GuildMemberBattleResult | 待确认 | 289 | 563 | 13 | 1/12/0 | 1/11/1 | N | Y |  |
| 409 | UI_GuildMemberBattleTarget | 上标题-中横列表-下信息 | 942 | 535 | 39 | 2/36/1 | 5/27/7 | Y | N |  |
| 410 | UI_GuildMemberManager | panel | 758 | 462 | 30 | 7/19/4 | 1/26/3 | Y | N |  |
| 411 | UI_GuildMsgs | panel | 860 | 429 | 17 | 1/14/2 | 2/14/1 | Y | N |  |
| 412 | UI_GuildNotic | 一体框 | 540 | 549 | 23 | 5/16/2 | 2/19/2 | Y | Y |  |
| 413 | UI_GuildNoticEditor | 一体框 | 611 | 412 | 20 | 2/14/4 | 1/17/2 | N | Y |  |
| 414 | UI_GuildNoticPreview | 确认弹框 | 5 | 334 | 12 | 0/9/3 | 1/10/1 | Y | Y |  |
| 415 | UI_GuildNoticTemplate | 上标题-中竖列表-下信息 | 802 | 811 | 13 | 1/11/1 | 1/11/1 | Y | Y | ⚠ z=3.1 on height |
| 416 | UI_GuildOpenDungenon | 确认弹框 | 80 | 295 | 16 | 1/12/3 | 1/13/2 | N | N |  |
| 417 | UI_GuildOptPopup | 确认弹框 | 417 | 248 | 18 | 1/15/2 | 3/11/4 | N | N |  |
| 418 | UI_GuildParty | panel | 1126 | 519 | 43 | 1/37/5 | 10/27/6 | Y | N |  |
| 419 | UI_GuildPartyPreview | tips | 368 | 347 | 21 | 4/17/0 | 2/18/1 | N | N |  |
| 420 | UI_GuildPartyResult | 展示-横条-条内信息 | 530 | 286 | 22 | 1/19/2 | 3/17/2 | Y | Y |  |
| 421 | UI_GuildPhaseReward | 上标题-中上标签-中竖列表-下信息 | 554 | 484 | 27 | 4/22/1 | 2/24/1 | Y | N |  |
| 422 | UI_GuildPosition | panel | 812 | 474 | 41 | 1/38/2 | 2/35/4 | Y | N |  |
| 423 | UI_GuildPositionDesc | 上标题-中竖列表-下信息 | 497 | 227 | 15 | 3/10/2 | 2/12/1 | Y | N |  |
| 424 | UI_GuildSameNameSetting | 确认弹框 | 177 | 300 | 11 | 1/7/3 | 2/6/3 | N | Y |  |
| 425 | UI_GuildSearch | 左-右 | 810 | 509 | 41 | 8/25/8 | 4/33/4 | Y | Y |  |
| 426 | UI_GuildSearchInfo | T型-上标题-左-右 | 629 | 365 | 35 | 9/21/5 | 6/28/1 | Y | Y |  |
| 427 | UI_GuildSetFlags | T型-上标题-左-右 | 590 | 340 | 26 | 5/17/4 | 5/20/1 | Y | N |  |
| 428 | UI_GuildSetting | tips | 653 | 323 | 27 | 5/19/3 | 4/19/4 | N | N |  |
| 429 | UI_GuildUpgradeTips | 功能开启&展示 | 136 | 346 | 9 | 0/8/1 | 1/7/1 | Y | N |  |
| 430 | UI_GuildWarAlliance | T型-上标题-左标签-右竖列表 | 707 | 526 | 40 | 8/29/3 | 6/32/2 | Y | N |  |
| 431 | UI_GuildWarAppoint | 上标题-中竖列表-下信息 | 439 | 420 | 20 | 3/13/4 | 4/15/1 | Y | N |  |
| 432 | UI_GuildWarAtkRandTip | 确认弹框 | 57 | 262 | 15 | 1/13/1 | 1/13/1 | N | N |  |
| 433 | UI_GuildWarAtkSum | 上标题-中竖列表-下信息 | 3412 | 526 | 29 | 0/28/1 | 1/27/1 | Y | N | ⚠ z=7.3 on width |
| 434 | UI_GuildWarAuthorize | 上标题-中竖列表-下信息 | 439 | 400 | 22 | 3/14/5 | 4/17/1 | Y | N |  |
| 435 | UI_GuildWarBaseInfo | panel+入口 | 581 | 644 | 69 | 5/54/10 | 7/56/6 | N | N |  |
| 436 | UI_GuildWarBattle | 战斗 | 1121 | 959 | 93 | 3/84/6 | 5/85/3 | Y | N |  |
| 437 | UI_GuildWarCommander | 上标题-中竖列表-下信息 | 463 | 578 | 18 | 3/13/2 | 3/13/2 | Y | N |  |
| 438 | UI_GuildWarGroup | 上标题-中竖列表-下信息 | 1270 | 399 | 18 | 3/12/3 | 2/15/1 | Y | N |  |
| 439 | UI_GuildWarMain | 红框方形玩法入口 | 1069 | 623 | 60 | 4/52/4 | 7/49/4 | Y | Y |  |
| 440 | UI_GuildWarOpTips | 上标题-中竖列表-下信息 | 407 | 331 | 12 | 1/9/2 | 1/10/1 | N | N |  |
| 441 | UI_GuildWarPlan | 上标题-中竖列表-下信息 | 857 | 744 | 35 | 4/28/3 | 2/29/4 | Y | N | ⚠ z=2.6 on height |
| 442 | UI_GuildWarProtactTips | tips | 25 | 292 | 6 | 2/3/1 | 2/3/1 | N | N |  |
| 443 | UI_GuildWarRank | T型-上标题-左标签-右竖列表 | 695 | 584 | 33 | 3/27/3 | 2/30/1 | Y | N |  |
| 444 | UI_GuildWarRecord | T型-上标题-左标签-右竖列表 | 894 | 354 | 40 | 6/33/1 | 4/35/1 | Y | N |  |
| 445 | UI_GuildWarRstFail | 展示-横条-左图-右信息 | 636 | 481 | 26 | 4/18/4 | 5/16/5 | N | N |  |
| 446 | UI_GuildWarRstMult | 展示-横条-条内信息 | 949 | 612 | 33 | 6/21/6 | 6/25/2 | Y | N | ⚠ z=2.7 on left_count |
| 447 | UI_GuildWarRstWin | 展示-横条-条内信息 | 646 | 517 | 40 | 4/32/4 | 6/30/4 | N | N |  |
| 448 | UI_GuildWarScene | N/A | 4916 | 2744 | 153 | 2/139/12 | 1/140/12 | Y | Y |  |
| 449 | UI_GuildWarSchedule | 横列表 | 667 | 408 | 31 | 2/26/3 | 3/27/1 | Y | N |  |
| 450 | UI_GuildWarStreet | panel | 1320 | 891 | 46 | 2/43/1 | 1/44/1 | Y | N | ⚠ z=3.2 on height |
| 451 | UI_GuildWarTask | T型-上标题-左标签-右竖列表 | 727 | 190 | 27 | 1/24/2 | 1/25/1 | Y | N |  |
| 452 | UI_HistoryEvent | 多列 | 1072 | 400 | 47 | 2/43/2 | 3/36/8 | Y | N |  |
| 453 | UI_HistoryEventGet | 左-右 | 1074 | 510 | 28 | 3/22/3 | 2/25/1 | Y | Y |  |
| 454 | UI_HistoryEventTip | 左-右 | 489 | 397 | 23 | 1/17/5 | 1/20/2 | Y | Y |  |
| 455 | UI_HistoryStageLock | tips | 463 | 245 | 11 | 1/9/1 | 1/9/1 | N | N |  |
| 456 | UI_HistoryStageTip | tips | 131 | 149 | 9 | 2/5/2 | 0/8/1 | N | N |  |
| 457 | UI_InvestMarketUp | 上标题-中横列表-下信息 | 858 | 482 | 32 | 1/29/2 | 2/25/5 | Y | Y |  |
| 458 | UI_InvestmentBattle | 战斗 | 1392 | 544 | 84 | 2/79/3 | 7/67/10 | Y | N |  |
| 459 | UI_InvestmentBidding | 横条-VS | 216 | 129 | 17 | 3/12/2 | 2/13/2 | N | N |  |
| 460 | UI_InvestmentBiddingResult | 展示-横条-条内信息 | 786 | 686 | 24 | 4/17/3 | 3/18/3 | N | Y |  |
| 461 | UI_InvestmentCancel | 展示-横条-条内信息 | 669 | 582 | 19 | 2/16/1 | 1/17/1 | Y | Y |  |
| 462 | UI_InvestmentCreateSucc | 展示-横条-条内信息 | 669 | 582 | 23 | 3/17/3 | 3/17/3 | N | Y |  |
| 463 | UI_InvestmentDetail | 上标题-中横列表-下信息 | 908 | 503 | 66 | 3/55/8 | 6/52/8 | Y | Y | ⚠ z=3.3 on right_count |
| 464 | UI_InvestmentFightTips | 确认弹框 | 545 | 355 | 18 | 2/15/1 | 3/12/3 | N | N |  |
| 465 | UI_InvestmentJoinAddTips | 使用弹框 | 472 | 359 | 18 | 2/14/2 | 2/14/2 | N | N |  |
| 466 | UI_InvestmentMain | 四边木栏（蒸笼标签）+左标签+中图+右信息 | 1044 | 552 | 56 | 5/49/2 | 7/44/5 | Y | N |  |
| 467 | UI_InvestmentPropStop | 确认弹框 | 214 | 219 | 13 | 2/8/3 | 3/8/2 | N | N |  |
| 468 | UI_InvestmentPropsUse | 使用弹框 | 472 | 302 | 22 | 3/17/2 | 4/17/1 | N | N |  |
| 469 | UI_InvestmentRecord | tips | 686 | 295 | 17 | 4/11/2 | 2/14/1 | Y | N |  |
| 470 | UI_InvestmentResult | 展示-横条-条内信息 | 786 | 686 | 24 | 3/18/3 | 2/19/3 | Y | Y |  |
| 471 | UI_InvestmentSkill | T型-上标题-左标签-右竖列表 | 1104 | 557 | 32 | 2/29/1 | 2/26/4 | Y | N |  |
| 472 | UI_InvestmentSkillAddition | tips | 228 | 343 | 11 | 1/10/0 | 2/8/1 | Y | N |  |
| 473 | UI_InvestmentSkillUpgrade | 确认弹框 | 411 | 392 | 30 | 3/23/4 | 3/24/3 | Y | N |  |
| 474 | UI_InvestmentUnlock | tips | 503 | 139 | 12 | 2/8/2 | 1/10/1 | N | N |  |
| 475 | UI_ItemAddTip | N/A | 132 | 210 | 5 | 1/3/1 | 1/3/1 | N | N |  |
| 476 | UI_ItemAddTips2 | N/A | 441 | 318 | 9 | 5/1/3 | 3/0/6 | N | N |  |
| 477 | UI_ItemTip | tips | 330 | 378 | 19 | 2/14/3 | 0/17/2 | N | N |  |
| 478 | UI_ItemUseTip | 使用弹框 | 554 | 351 | 42 | 4/31/7 | 4/36/2 | Y | N | ⚠ z=3.6 on middle_count |
| 479 | UI_LimitActRechargeGift | 上标题-中竖列表-下信息 | 935 | 303 | 26 | 1/23/2 | 3/22/1 | Y | Y |  |
| 480 | UI_LimitActivity | 红框方形玩法入口 | 823 | 513 | 49 | 5/39/5 | 8/35/6 | N | Y |  |
| 481 | UI_LimitActivityPreview | 上标题-中横列表-下信息 | 353 | 295 | 23 | 3/20/0 | 3/18/2 | N | N |  |
| 482 | UI_LimitExchange | 木屏风+横列表 | 563 | 557 | 45 | 8/37/0 | 5/35/5 | Y | N |  |
| 483 | UI_LimitLottery | 红框方形玩法入口 | 838 | 532 | 63 | 6/53/4 | 7/50/6 | N | Y |  |
| 484 | UI_LimitLotteryGift | 上标题-中竖列表-下信息 | 589 | 594 | 36 | 3/24/9 | 3/32/1 | Y | Y | ⚠ z=3.5 on right_count |
| 485 | UI_LimitLotteryTask | T型-上标题-左标签-右竖列表 | 1083 | 529 | 54 | 3/48/3 | 5/48/1 | Y | N |  |
| 486 | UI_LimitWish | 左-右 | 659 | 645 | 44 | 6/34/4 | 2/40/2 | N | N |  |
| 487 | UI_LimitWishTip | 确认弹框 | 405 | 137 | 7 | 1/6/0 | 1/5/1 | N | N |  |
| 488 | UI_Loading | 登录加载全屏 | 782 | 376 | 7 | 1/5/1 | 2/2/3 | N | Y |  |
| 489 | UI_Login | 登录加载全屏 | 593 | 418 | 24 | 3/18/3 | 2/18/4 | N | N |  |
| 490 | UI_LotteryBigReward | 功能开启&展示 | 484 | 312 | 10 | 1/8/1 | 2/7/1 | N | N |  |
| 491 | UI_LotterySkinItem | N/A | 798 | 517 | 34 | 2/29/3 | 2/30/2 | Y | Y |  |
| 492 | UI_Mail | 左标签-框内左+右 | 711 | 476 | 35 | 5/26/4 | 4/27/4 | Y | Y |  |
| 493 | UI_Main | mainUI | 1162 | 483 | 131 | 5/125/1 | 10/114/7 | Y | N | ⚠ z=2.5 on top_count |
| 494 | UI_MainMoneyTalentBuffTips | N/A | 413 | 195 | 6 | 1/4/1 | 1/4/1 | N | N |  |
| 495 | UI_MainPowerDetail | tips | 683 | 515 | 14 | 3/7/4 | 5/5/4 | N | N | ⚠ z=2.5 on top_count |
| 496 | UI_MainVisitBuffTips | N/A | 413 | 196 | 5 | 1/3/1 | 1/3/1 | N | N |  |
| 497 | UI_Market | mainUI | 1373 | 539 | 87 | 3/82/2 | 3/83/1 | N | N |  |
| 498 | UI_MarketActive | 左-右 | 397 | 299 | 31 | 4/21/6 | 3/26/2 | N | Y |  |
| 499 | UI_MarketActiveAdvanced | tips | 526 | 122 | 9 | 4/3/2 | 2/7/0 | N | Y |  |
| 500 | UI_MarketActiveFloor | 上标题-中竖列表-下信息 | 787 | 608 | 33 | 6/23/4 | 4/24/5 | Y | Y |  |
| 501 | UI_MarketAdvanced | T型-上标题-左标签-右竖列表 | 913 | 393 | 28 | 6/18/4 | 1/24/3 | Y | N |  |
| 502 | UI_MarketAllBell | 功能开启&展示 | 446 | 213 | 9 | 0/8/1 | 2/6/1 | N | Y |  |
| 503 | UI_MarketAllBellResult | 功能开启&展示 | 735 | 196 | 12 | 2/7/3 | 1/10/1 | N | N |  |
| 504 | UI_MarketAureoleTips | 左标签-右信息 | 905 | 517 | 81 | 9/65/7 | 9/67/5 | Y | N |  |
| 505 | UI_MarketAutoTip | 确认弹框 | 181 | 268 | 11 | 1/9/1 | 1/9/1 | N | N |  |
| 506 | UI_MarketBaseInfo | T型-上标题-左标签-右竖列表 | 918 | 501 | 66 | 8/50/8 | 9/52/5 | Y | N | ⚠ z=3 on top_count |
| 507 | UI_MarketBeauty | 上标题-中竖列表-下信息 | 755 | 490 | 32 | 3/25/4 | 2/29/1 | Y | N |  |
| 508 | UI_MarketBeautyAdd | 上标题-中竖列表-下信息 | 703 | 546 | 24 | 3/20/1 | 3/20/1 | Y | N |  |
| 509 | UI_MarketBeautyBest | 上标题-中竖列表-下信息 | 949 | 546 | 36 | 4/26/6 | 5/29/2 | Y | N |  |
| 510 | UI_MarketBeautyDispatchSucc | N/A | 1056 | 483 | 32 | 1/30/1 | 2/28/2 | Y | N |  |
| 511 | UI_MarketBellProgress | N/A | 1095 | 358 | 18 | 3/11/4 | 5/4/9 | N | N |  |
| 512 | UI_MarketBestSell | N/A | 281 | 386 | 12 | 2/8/2 | 2/8/2 | N | Y |  |
| 513 | UI_MarketChild | tips | 713 | 514 | 21 | 2/16/3 | 3/15/3 | Y | N |  |
| 514 | UI_MarketCommodity | 左-右 | 719 | 438 | 42 | 5/25/12 | 5/28/9 | Y | N | ⚠ z=3.1 on right_count |
| 515 | UI_MarketFacilityTip | tips | 362 | 199 | 13 | 2/10/1 | 2/10/1 | Y | Y |  |
| 516 | UI_MarketGetSkinItem | 展示-横条-左图-右信息 | 724 | 305 | 11 | 2/8/1 | 2/7/2 | N | N |  |
| 517 | UI_MarketGuest | 抽屉 | 1004 | 548 | 51 | 1/47/3 | 7/42/2 | Y | N |  |
| 518 | UI_MarketHarvest | 一体框 | 834 | 384 | 20 | 2/16/2 | 3/15/2 | N | N |  |
| 519 | UI_MarketIngredentsInfo | N/A | 387 | 482 | 19 | 3/13/3 | 1/16/2 | Y | N |  |
| 520 | UI_MarketLightInfo | T型-上标题-左-右 | 364 | 429 | 23 | 3/14/6 | 2/15/6 | Y | N |  |
| 521 | UI_MarketList | 待确认 | 976 | 906 | 118 | 13/97/8 | 17/98/3 | Y | Y |  |
| 522 | UI_MarketOffer | 上标题-中横列表-下信息 | 589 | 515 | 40 | 4/34/2 | 5/31/4 | Y | N |  |
| 523 | UI_MarketQuality | 一体框 | 704 | 470 | 28 | 4/22/2 | 3/24/1 | Y | N |  |
| 524 | UI_MarketRateTips | 上标题-中竖列表-下信息 | 666 | 257 | 21 | 2/15/4 | 4/16/1 | Y | Y |  |
| 525 | UI_MarketRecommend | 一体框 | 657 | 663 | 19 | 0/18/1 | 1/17/1 | N | N |  |
| 526 | UI_MarketRepresentAdd | tips | 384 | 244 | 11 | 4/5/2 | 1/9/1 | Y | N |  |
| 527 | UI_MarketRevenue | 上标题-中竖列表-下信息 | 713 | 431 | 26 | 3/19/4 | 2/22/2 | Y | N |  |
| 528 | UI_MarketRobotInfo | 左-右 | 457 | 266 | 12 | 4/6/2 | 2/7/3 | N | N |  |
| 529 | UI_MarketSkin | 上标题-中横列表-下信息 | 138 | 406 | 19 | 2/17/0 | 2/14/3 | Y | N |  |
| 530 | UI_MarketSkinLook | tips | 652 | 468 | 15 | 1/13/1 | 1/12/2 | Y | N |  |
| 531 | UI_MarketSlotAdd | 一体框 | 898 | 318 | 25 | 5/18/2 | 1/20/4 | Y | N |  |
| 532 | UI_MarketStarActive | 上标题-中竖列表-下信息 | 728 | 489 | 37 | 10/24/3 | 4/29/4 | Y | N | ⚠ z=4.1 on left_count |
| 533 | UI_MarketStrategyActive | 功能开启&展示 | 361 | 216 | 12 | 1/9/2 | 1/10/1 | N | N |  |
| 534 | UI_MarketStrength | tips | 456 | 133 | 7 | 1/5/1 | 2/1/4 | N | N |  |
| 535 | UI_MarketSuggest | 上标题-中竖列表-下信息 | 765 | 404 | 28 | 5/19/4 | 3/23/2 | Y | N |  |
| 536 | UI_MarketSurvey | T型-上标题-左-右 | 846 | 257 | 38 | 5/31/2 | 4/33/1 | Y | N |  |
| 537 | UI_MarketTransfer | 左右对比 | 597 | 407 | 16 | 2/11/3 | 3/9/4 | N | N |  |
| 538 | UI_MarketWarAddVit | 确认弹框 | 342 | 315 | 11 | 4/5/2 | 1/8/2 | Y | N |  |
| 539 | UI_MarketWarAgentResult | 展示-横条-条内信息 | 690 | 401 | 30 | 2/24/4 | 0/29/1 | Y | N |  |
| 540 | UI_MarketWarAgentTip | 确认弹框 | 302 | 378 | 14 | 1/11/2 | 2/10/2 | N | N |  |
| 541 | UI_MarketWarBattle | 战斗 | 1155 | 504 | 77 | 1/73/3 | 9/63/5 | Y | N |  |
| 542 | UI_MarketWarBeautySkill | N/A | 681 | 446 | 14 | 3/6/5 | 0/11/3 | N | N |  |
| 543 | UI_MarketWarBuff | N/A | 360 | 150 | 8 | 1/5/2 | 2/4/2 | N | N |  |
| 544 | UI_MarketWarCapture | 上标题-中竖列表-下信息 | 1160 | 576 | 48 | 6/38/4 | 5/39/4 | Y | N | ⚠ z=2.6 on total_nodes |
| 545 | UI_MarketWarCaptureNew | 确认弹框 | 550 | 335 | 14 | 1/12/1 | 2/9/3 | N | N |  |
| 546 | UI_MarketWarCoolingSkill | N/A | 451 | 210 | 5 | 1/3/1 | 1/3/1 | N | N |  |
| 547 | UI_MarketWarEmployer | 左广告图-右列表 | 931 | 408 | 36 | 6/28/2 | 4/27/5 | Y | N |  |
| 548 | UI_MarketWarEmployerTip | N/A | 748 | 406 | 12 | 4/7/1 | 1/10/1 | N | N |  |
| 549 | UI_MarketWarHpTip | N/A | 135 | 103 | 10 | 1/7/2 | 1/6/3 | N | N |  |
| 550 | UI_MarketWarRank | 上标题-中竖列表-下信息 | 1039 | 520 | 30 | 2/26/2 | 6/21/3 | Y | N | ⚠ z=2.6 on top_count |
| 551 | UI_MarketWarRankReward | 一体框 | 723 | 528 | 36 | 3/28/5 | 4/28/4 | Y | Y |  |
| 552 | UI_MarketWarReady | 横条-VS | 460 | 168 | 11 | 2/8/1 | 1/8/2 | N | N |  |
| 553 | UI_MarketWarReport | 上标题-中上标签-中竖列表-下信息 | 1224 | 221 | 25 | 2/19/4 | 2/21/2 | Y | N |  |
| 554 | UI_MarketWarRescure | 确认弹框 | 695 | 289 | 21 | 2/14/5 | 1/18/2 | N | N |  |
| 555 | UI_MarketWarResult | 展示-横条-条内信息 | 633 | 605 | 53 | 2/46/5 | 3/46/4 | Y | Y | ⚠ z=3.1 on center_count |
| 556 | UI_MarketWarSupport | 确认弹框 | 466 | 336 | 20 | 5/10/5 | 3/14/3 | N | N | ⚠ z=3.2 on left_count |
| 557 | UI_MarketWarSupportSucc | N/A | 516 | 462 | 4 | 1/2/1 | 1/2/1 | N | N |  |
| 558 | UI_MarketWarTactic | tips | 523 | 278 | 17 | 1/13/3 | 0/15/2 | N | N |  |
| 559 | UI_MarketWarTacticUse | 待确认 | 434 | 395 | 16 | 2/13/1 | 3/10/3 | Y | Y |  |
| 560 | UI_MarketWarTarget | panel+入口 | 1255 | 676 | 60 | 4/50/6 | 4/53/3 | Y | N |  |
| 561 | UI_MarketWarTask | 上标题-中竖列表-下信息 | 716 | 483 | 25 | 1/22/2 | 2/22/1 | Y | N |  |
| 562 | UI_MarketWarTea | tips | 269 | 422 | 19 | 2/17/0 | 4/12/3 | N | N |  |
| 563 | UI_MarketWarUseItem | 确认弹框 | 498 | 376 | 14 | 1/11/2 | 1/10/3 | N | N |  |
| 564 | UI_MarqueeMsg | N/A | 11 | 205 | 5 | 1/4/0 | 0/4/1 | N | N |  |
| 565 | UI_MarqueeSpineMsg | N/A | 306 | 201 | 6 | 1/5/0 | 1/5/0 | N | N |  |
| 566 | UI_MessageTip1 | 确认弹框 | 57 | 404 | 16 | 2/13/1 | 2/12/2 | N | N |  |
| 567 | UI_MessageTip2 | 确认弹框 | 161 | 408 | 16 | 0/15/1 | 2/12/2 | N | N |  |
| 568 | UI_MountActive | 活动打脸弹窗 | 420 | 577 | 21 | 1/19/1 | 2/17/2 | N | N |  |
| 569 | UI_MountAttrInfo | N/A | 293 | 49 | 7 | 3/3/1 | 1/5/1 | Y | N |  |
| 570 | UI_MountAureole | 上标题-中竖列表-下信息 | 278 | 235 | 12 | 2/9/1 | 1/11/0 | Y | N |  |
| 571 | UI_MountBuildInfo | 待确认 | 1441 | 528 | 131 | 7/118/6 | 13/107/11 | Y | N |  |
| 572 | UI_MountBuildSpeedUpTips | 确认弹框 | 284 | 304 | 14 | 2/11/1 | 2/9/3 | N | N |  |
| 573 | UI_MountCharactersActive | 展示-横条-条内信息 | 464 | 244 | 11 | 3/6/2 | 2/8/1 | N | Y |  |
| 574 | UI_MountInfo | 四边木栏（蒸笼标签）+左中右 | 718 | 393 | 32 | 1/29/2 | 5/25/2 | Y | N | ⚠ z=2.8 on width |
| 575 | UI_MountLevelUp | 确认弹框 | 560 | 388 | 32 | 1/28/3 | 3/25/4 | N | Y |  |
| 576 | UI_MountMain | mainUI | 1004 | 428 | 40 | 4/33/3 | 1/37/2 | Y | N |  |
| 577 | UI_MountOneKeyUpdateTips | 确认弹框 | 57 | 367 | 12 | 1/10/1 | 1/9/2 | N | N |  |
| 578 | UI_MountPartRemake | 一体框 | 740 | 378 | 62 | 7/52/3 | 6/51/5 | Y | N |  |
| 579 | UI_MountPartRemakeTip | 确认弹框 | 125 | 251 | 12 | 1/10/1 | 1/10/1 | N | N |  |
| 580 | UI_MountPreviewInfo | 一体框 | 500 | 567 | 23 | 4/17/2 | 3/17/3 | Y | N |  |
| 581 | UI_MountQualityUpgrade | 展示-横条-条内信息 | 603 | 464 | 16 | 4/10/2 | 3/12/1 | Y | Y |  |
| 582 | UI_MountQueryAttr | T型-上标题-左-右 | 691 | 361 | 26 | 5/19/2 | 2/23/1 | Y | Y |  |
| 583 | UI_MountResolve | T型-上标题-左-右 | 909 | 389 | 46 | 5/38/3 | 4/33/9 | Y | N |  |
| 584 | UI_MountResolveTips | 确认弹框 | 662 | 496 | 16 | 0/15/1 | 2/12/2 | N | N |  |
| 585 | UI_MountSelectUpStarMat | 上标题-中横列表-下信息 | 668 | 287 | 25 | 0/21/4 | 2/20/3 | Y | N |  |
| 586 | UI_MountStarPreview | 上标题-中竖列表-下信息 | 790 | 427 | 27 | 4/20/3 | 2/24/1 | Y | N |  |
| 587 | UI_MountUpgradeResult | 上标题-中横列表-下信息 | 469 | 432 | 38 | 1/36/1 | 2/35/1 | Y | N |  |
| 588 | UI_MulDayRechargeGift | panel | 723 | 298 | 21 | 2/18/1 | 2/17/2 | Y | Y |  |
| 589 | UI_MultiAwardItemTips | tips | 255 | 309 | 16 | 1/12/3 | 1/13/2 | Y | Y |  |
| 590 | UI_MultiAwardItemUse | 使用弹框 | 475 | 368 | 22 | 2/18/2 | 3/18/1 | Y | N |  |
| 591 | UI_MuseumAntiqueHistory | T型-上标题-左-右 | 587 | 445 | 20 | 7/9/4 | 3/11/6 | Y | N |  |
| 592 | UI_MuseumAntiqueList | 四边木栏（蒸笼标签）+左中右 | 1041 | 514 | 71 | 4/56/11 | 11/56/4 | Y | N |  |
| 593 | UI_MuseumAntiquePut | 上标题-中横列表-下信息 | 484 | 481 | 26 | 2/23/1 | 3/21/2 | Y | N |  |
| 594 | UI_MuseumCollectionSucc | 展示-横条-左图-右信息 | 532 | 318 | 16 | 5/7/4 | 3/11/2 | Y | N |  |
| 595 | UI_MuseumExhibition | panel | 858 | 539 | 25 | 2/21/2 | 1/20/4 | Y | Y |  |
| 596 | UI_MuseumExhibitionList | 左标签+框内横列表 | 612 | 463 | 28 | 3/25/0 | 6/19/3 | Y | N |  |
| 597 | UI_MuseumExhibitionSucc | 展示-横条-左右对比 | 526 | 463 | 23 | 3/19/1 | 3/17/3 | N | Y |  |
| 598 | UI_MuseumGacha | 大背景-展示 | 959 | 400 | 30 | 2/25/3 | 2/19/9 | N | N |  |
| 599 | UI_MuseumGachaResult | 展示-横条-条内信息 | 587 | 624 | 36 | 3/31/2 | 5/26/5 | Y | N |  |
| 600 | UI_MuseumGachaShop | 四边木栏（蒸笼标签）+横列表 | 1001 | 404 | 35 | 3/28/4 | 5/28/2 | Y | N |  |
| 601 | UI_MuseumJackpot | 全屏获得新奖励 | 517 | 428 | 24 | 4/17/3 | 4/18/2 | N | Y |  |
| 602 | UI_MuseumMain | mainUI | 948 | 259 | 18 | 4/11/3 | 2/14/2 | Y | N |  |
| 603 | UI_MuseumMedalInfo | 上标题-中竖列表-下信息 | 812 | 499 | 19 | 2/15/2 | 3/15/1 | Y | N |  |
| 604 | UI_MuseumMedalWall | 上标题-中横列表-下信息 | 456 | 317 | 18 | 1/17/0 | 2/14/2 | Y | N |  |
| 605 | UI_MuseumStarUpSucc | 展示-横条-左图-右信息 | 748 | 284 | 24 | 5/15/4 | 3/17/4 | Y | N |  |
| 606 | UI_NetError | tips | 8 | 260 | 8 | 2/5/1 | 2/5/1 | N | N |  |
| 607 | UI_Notice | 左-右 | 423 | 328 | 14 | 3/9/2 | 3/10/1 | Y | Y |  |
| 608 | UI_NpcBubble | N/A | 240 | 159 | 17 | 0/16/1 | 3/12/2 | N | N |  |
| 609 | UI_NpcTimeBubble | N/A | 461 | 142 | 7 | 1/6/0 | 2/4/1 | N | N |  |
| 610 | UI_OpenCustomBox | 使用弹框 | 476 | 494 | 29 | 1/26/2 | 3/24/2 | Y | N |  |
| 611 | UI_OpenCustomSkin | 横列表 | 374 | 569 | 26 | 1/25/0 | 2/20/4 | Y | N |  |
| 612 | UI_OtherRoleBattleAttr | 上标题-中竖列表-下信息 | 1414 | 296 | 33 | 2/31/0 | 4/29/0 | Y | N |  |
| 613 | UI_OtherRoleGuest | 四边木栏（蒸笼标签）+左中右 | 1021 | 496 | 76 | 8/60/8 | 13/55/8 | Y | N |  |
| 614 | UI_OtherRoleMarket | 左-右 | 1199 | 464 | 72 | 11/59/2 | 2/67/3 | Y | N |  |
| 615 | UI_OtherTechnoCup | 全屏背景界面 | 610 | 526 | 13 | 0/12/1 | 1/11/1 | N | N |  |
| 616 | UI_PanelGuideBtn | 待确认 | 663 | 446 | 30 | 3/22/5 | 1/27/2 | Y | N |  |
| 617 | UI_PirateChallengeResult | 展示-横条-条内信息 | 280 | 352 | 20 | 3/17/0 | 3/15/2 | N | Y |  |
| 618 | UI_PirateEvent | tips | 552 | 628 | 43 | 2/39/2 | 5/31/7 | Y | Y | ⚠ z=3.4 on bottom_count |
| 619 | UI_PirateFightBattle | 战斗 | 1139 | 671 | 82 | 1/77/4 | 4/73/5 | Y | N |  |
| 620 | UI_PirateIntelStation | 上标题-中上标签-中竖列表-下信息 | 460 | 266 | 30 | 6/20/4 | 4/24/2 | Y | N |  |
| 621 | UI_PirateInvasion | 红框方形玩法入口 | 2311 | 723 | 63 | 0/62/1 | 5/52/6 | N | Y | ⚠ z=3.5 on width |
| 622 | UI_PirateInvasionMain | 红框方形玩法入口 | 1008 | 591 | 52 | 3/46/3 | 5/43/4 | Y | Y |  |
| 623 | UI_PirateLikabilityAnim | N/A | 509 | 310 | 7 | 2/0/5 | 5/0/2 | N | N |  |
| 624 | UI_PirateLottery | 活动打脸弹窗 | 842 | 612 | 27 | 2/21/4 | 4/16/7 | N | N |  |
| 625 | UI_PiratePreview | 上标题-中横列表-下信息 | 343 | 332 | 22 | 3/19/0 | 2/17/3 | N | N |  |
| 626 | UI_PirateResultFail | 展示-横条-条内信息 | 71 | 261 | 14 | 0/12/2 | 1/12/1 | N | N |  |
| 627 | UI_PirateServerBoss | 左-中-右 | 1385 | 571 | 65 | 3/59/3 | 5/52/8 | Y | N |  |
| 628 | UI_PirateTask | 左广告图-右列表 | 1134 | 544 | 43 | 9/32/2 | 5/32/6 | Y | N |  |
| 629 | UI_PirateTips | 确认弹框 | 441 | 309 | 16 | 1/14/1 | 2/12/2 | N | N |  |
| 630 | UI_PlayerSkinPreview | tips | 473 | 606 | 15 | 3/11/1 | 3/7/5 | N | N |  |
| 631 | UI_PreviewAwards | tips | 77 | 67 | 13 | 1/11/1 | 1/7/5 | N | Y |  |
| 632 | UI_PrivilegeCardInfo | 活动打脸弹窗 | 549 | 250 | 11 | 1/7/3 | 1/8/2 | N | Y |  |
| 633 | UI_PrivilegeDayCard | panel | 782 | 284 | 26 | 3/19/4 | 3/20/3 | Y | Y |  |
| 634 | UI_PrivilegeMain | 左标签+右竖列表 | 484 | 133 | 9 | 2/6/1 | 1/8/0 | Y | N | ⚠ z=2.6 on height |
| 635 | UI_PrivilegeMonthlyCard | 活动打脸弹窗 | 541 | 296 | 26 | 3/18/5 | 6/15/5 | Y | Y |  |
| 636 | UI_PrivilegeMonthlyCard2 | tips | 448 | 301 | 21 | 3/12/6 | 3/14/4 | Y | N | ⚠ z=2.8 on right_count |
| 637 | UI_PrivilegePropsCard | N/A | 591 | 200 | 17 | 1/14/2 | 3/11/3 | Y | N |  |
| 638 | UI_PurchaseBattleActivity | 红框方形玩法入口 | 896 | 555 | 48 | 2/40/6 | 8/35/5 | Y | N |  |
| 639 | UI_PurchaseBattleExchange | 使用弹框 | 476 | 317 | 19 | 2/15/2 | 3/13/3 | N | N |  |
| 640 | UI_PurchaseBattleGuildRank | 上标题-中竖列表-下信息 | 1019 | 426 | 32 | 5/24/3 | 6/23/3 | Y | N | ⚠ z=2.6 on top_count |
| 641 | UI_PurchaseBattleInject | 确认弹框 | 476 | 317 | 19 | 2/15/2 | 2/15/2 | N | N |  |
| 642 | UI_PurchaseBattleMain | 左标签页-右框内-上标题-中竖列表-下信息 | 1265 | 537 | 78 | 9/62/7 | 5/70/3 | Y | Y |  |
| 643 | UI_PurchaseBattleRank | 左标签+右竖列表 | 1907 | 389 | 32 | 1/28/3 | 4/22/6 | Y | N |  |
| 644 | UI_PurchaseBattleReward | 左标签+右竖列表 | 655 | 437 | 44 | 8/33/3 | 6/34/4 | Y | N |  |
| 645 | UI_PurchaseBattleSchedule | 上标题-中横列表-下信息 | 590 | 222 | 18 | 2/14/2 | 1/16/1 | Y | N |  |
| 646 | UI_RankAct | T型-上标题-左-右 | 803 | 631 | 65 | 7/48/10 | 10/47/8 | Y | N | ⚠ z=3.2 on top_count |
| 647 | UI_RankActAd | 活动打脸弹窗 | 811 | 843 | 89 | 8/74/7 | 3/80/6 | Y | Y | ⚠ z=3.2 on middle_count |
| 648 | UI_RankActAddTip | tips | 77 | 178 | 5 | 0/4/1 | 1/3/1 | N | N |  |
| 649 | UI_RankActEntrance | 左标签+右竖列表 | 1228 | 552 | 84 | 7/69/8 | 7/68/9 | Y | Y |  |
| 650 | UI_RankActGift | T型-上标题-左标签-右竖列表 | 1052 | 316 | 47 | 2/41/4 | 3/42/2 | Y | Y |  |
| 651 | UI_RankActGuildMemberRank | T型-上标题-左-右 | 640 | 439 | 31 | 9/17/5 | 7/20/4 | Y | N |  |
| 652 | UI_RankActItem | 左标签+右竖列表 | 751 | 438 | 35 | 2/30/3 | 3/31/1 | Y | N |  |
| 653 | UI_RankActPath | 上标题-中横列表-下信息 | 487 | 226 | 13 | 2/10/1 | 2/10/1 | Y | N |  |
| 654 | UI_RankActPreview | 活动打脸弹窗 | 800 | 843 | 86 | 7/72/7 | 3/78/5 | Y | Y | ⚠ z=3 on middle_count |
| 655 | UI_RankActReward | 左标签页-右框内-上标题-中竖列表-下信息 | 768 | 460 | 28 | 3/24/1 | 2/22/4 | Y | N |  |
| 656 | UI_RankActRewardGuild | 左标签+右竖列表 | 1925 | 431 | 62 | 1/58/3 | 7/48/7 | Y | N |  |
| 657 | UI_RankActServerRank | 上标题-中竖列表-下信息 | 826 | 368 | 18 | 2/14/2 | 3/12/3 | Y | N |  |
| 658 | UI_RankActSingleServerRank | 上标题-中竖列表-下信息 | 901 | 371 | 21 | 3/15/3 | 4/13/4 | Y | Y |  |
| 659 | UI_RankActSpecifyAd | panel+入口 | 946 | 575 | 66 | 4/58/4 | 4/53/9 | Y | N |  |
| 660 | UI_RankActSprint | T型-上标题-左标签-右竖列表 | 1051 | 414 | 62 | 2/56/4 | 6/51/5 | Y | Y |  |
| 661 | UI_RankActTask | T型-上标题-左标签-右竖列表 | 976 | 314 | 43 | 3/35/5 | 4/37/2 | Y | N |  |
| 662 | UI_RankActTaskMemberRank | 上标题-中竖列表-下信息 | 615 | 373 | 23 | 5/15/3 | 4/14/5 | Y | Y |  |
| 663 | UI_RankActTwo | 左-右 | 816 | 628 | 58 | 9/40/9 | 8/44/6 | Y | N |  |
| 664 | UI_RankEntry | 横列表 | 77 | 607 | 22 | 4/12/6 | 1/18/3 | Y | N |  |
| 665 | UI_RankGobal | 四边木栏（蒸笼标签）底 | 1071 | 595 | 52 | 3/44/5 | 6/38/8 | Y | N |  |
| 666 | UI_RankGuildVoteReward | 展示-横条-条内信息 | 414 | 370 | 12 | 1/11/0 | 1/8/3 | Y | N |  |
| 667 | UI_RankLocal | 四边木栏（蒸笼标签）底 | 1071 | 595 | 57 | 3/49/5 | 5/44/8 | Y | N |  |
| 668 | UI_RankPlayerVoteReward | N/A | 665 | 351 | 11 | 1/8/2 | 1/9/1 | N | N |  |
| 669 | UI_RechargeGift | panel | 779 | 301 | 29 | 1/27/1 | 3/22/4 | Y | Y |  |
| 670 | UI_RechargeMain | 木屏风+横列表 | 967 | 343 | 27 | 2/21/4 | 8/13/6 | Y | N |  |
| 671 | UI_RechargeTokens | 横列表 | 456 | 428 | 21 | 1/18/2 | 3/17/1 | Y | N |  |
| 672 | UI_RecruitConfirm | 确认弹框 | 454 | 450 | 21 | 1/19/1 | 2/17/2 | Y | Y |  |
| 673 | UI_RecruitMain | 活动打脸弹窗 | 732 | 399 | 32 | 2/28/2 | 5/23/4 | Y | Y |  |
| 674 | UI_RecruitProgressTips | tips | 250 | 122 | 5 | 1/2/2 | 1/3/1 | N | N |  |
| 675 | UI_RecruitTips | tips | 441 | 632 | 17 | 2/12/3 | 0/16/1 | N | N |  |
| 676 | UI_RedPacketInfo | 左广告图-右列表 | 789 | 378 | 29 | 1/23/5 | 4/24/1 | Y | N |  |
| 677 | UI_RedPacketOpen | tips | 447 | 396 | 21 | 2/17/2 | 3/15/3 | N | N |  |
| 678 | UI_RedPacketSetting | tips | 469 | 354 | 18 | 2/15/1 | 2/15/1 | N | N |  |
| 679 | UI_RelayAddCar | 左-右 | 779 | 419 | 40 | 4/31/5 | 2/33/5 | Y | N |  |
| 680 | UI_RelayCommonEquip | 上标题-中横列表-下信息 | 824 | 480 | 50 | 3/43/4 | 2/43/5 | Y | N |  |
| 681 | UI_RelayCommonFleet | 横列表 | 2128 | 544 | 71 | 1/66/4 | 2/65/4 | Y | N | ⚠ z=3.1 on width |
| 682 | UI_RelayRaceInfo | panel | 899 | 502 | 73 | 11/55/7 | 7/61/5 | Y | N | ⚠ z=2.7 on left_count |
| 683 | UI_RelayRaceMain | 红框方形玩法入口 | 974 | 686 | 77 | 4/68/5 | 3/66/8 | Y | N |  |
| 684 | UI_RelayRaceMap | 地图底 | 3561 | 812 | 58 | 4/52/2 | 10/41/7 | N | Y |  |
| 685 | UI_RelayRaceMapUI | panel+入口 | 1063 | 664 | 87 | 3/83/1 | 5/80/2 | Y | N |  |
| 686 | UI_RelayRaceNpc | 左广告图-右列表 | 802 | 556 | 47 | 3/41/3 | 6/39/2 | Y | Y |  |
| 687 | UI_RelayRacePeakGraph | 赛程 | 1310 | 696 | 29 | 1/27/1 | 1/25/3 | N | N |  |
| 688 | UI_RelayRacePlayers | 上标题-中竖列表-下信息 | 627 | 509 | 24 | 3/19/2 | 2/19/3 | Y | N |  |
| 689 | UI_RelayRacePlayersMult | 左标签页-右框内-上标题-中竖列表-下信息 | 854 | 553 | 28 | 4/22/2 | 3/22/3 | Y | N |  |
| 690 | UI_RelayRacePlayersRank | 左标签页-右框内-上标题-中竖列表-下信息 | 935 | 531 | 25 | 3/19/3 | 4/18/3 | Y | N |  |
| 691 | UI_RelayRacePvpRank | 上标题-中上标签-中竖列表-下信息 | 1282 | 443 | 52 | 3/40/9 | 4/47/1 | Y | N |  |
| 692 | UI_RelayRaceRecordRank | 上标题-中竖列表-下信息 | 754 | 494 | 21 | 3/14/4 | 2/16/3 | Y | N |  |
| 693 | UI_RelayRaceResult | 展示-横条-条内信息 | 851 | 567 | 50 | 6/36/8 | 8/31/11 | Y | N | ⚠ z=5.2 on bottom_count |
| 694 | UI_RelayRaceRwds | 上标题-中竖列表-下信息 | 787 | 448 | 23 | 2/19/2 | 2/20/1 | Y | Y |  |
| 695 | UI_RelayRaceTab | tips | 561 | 187 | 10 | 2/8/0 | 1/9/0 | N | N |  |
| 696 | UI_RelayRankDetail | 左标签页-右框内-上标题-中竖列表-下信息 | 879 | 428 | 52 | 7/40/5 | 8/43/1 | Y | N |  |
| 697 | UI_RelayTrainFightTips | 确认弹框 | 589 | 336 | 15 | 2/12/1 | 1/12/2 | N | N |  |
| 698 | UI_RelayTrainFleetUp | 上标题-中横列表-下信息 | 456 | 455 | 18 | 2/14/2 | 3/13/2 | Y | N |  |
| 699 | UI_RelayTrainGradeUp | 横列表 | 653 | 449 | 20 | 4/15/1 | 4/14/2 | N | N |  |
| 700 | UI_RelayTrainGradeUpSucc | 展示-横条-条内信息 | 787 | 597 | 17 | 3/11/3 | 5/8/4 | N | Y |  |
| 701 | UI_RelayTrainMain | 左标签+框内整图 | 1067 | 528 | 69 | 5/57/7 | 6/56/7 | Y | N |  |
| 702 | UI_RelayTrainRstFail | 展示-横条-条内信息 | 802 | 393 | 21 | 1/18/2 | 2/18/1 | N | N |  |
| 703 | UI_RelayTrainRstWin | 展示-横条-条内信息 | 681 | 628 | 27 | 4/20/3 | 5/20/2 | Y | N |  |
| 704 | UI_RelayTrainRwd | tips | 680 | 530 | 13 | 0/12/1 | 1/11/1 | Y | N |  |
| 705 | UI_RelayTrainTask | 上标题-中竖列表-下信息 | 568 | 271 | 24 | 4/18/2 | 1/23/0 | Y | N |  |
| 706 | UI_RelayTrainUpPath | tips | 146 | 99 | 9 | 2/5/2 | 2/5/2 | Y | N |  |
| 707 | UI_RelayUpgradePath | 上标题-中横列表-下信息 | 257 | 236 | 12 | 0/9/3 | 3/8/1 | Y | N |  |
| 708 | UI_ResAddition | tips | 201 | 236 | 14 | 1/13/0 | 3/9/2 | Y | N |  |
| 709 | UI_ResRetrieve | 上标题-中竖列表-下信息 | 1294 | 563 | 39 | 3/34/2 | 3/35/1 | Y | N |  |
| 710 | UI_ResUpdateTip | 确认弹框 | 323 | 233 | 12 | 1/11/0 | 2/9/1 | N | Y |  |
| 711 | UI_Role | 全屏背景界面 | 1236 | 720 | 138 | 7/123/8 | 16/104/18 | Y | N | ⚠ z=2.9 on top_count |
| 712 | UI_RoleBeautyTip | 四边木栏（蒸笼标签）+横列表 | 821 | 579 | 22 | 5/16/1 | 4/13/5 | Y | N |  |
| 713 | UI_RoleEvalEquipTips | 展示-横条-左图-右信息 | 665 | 271 | 16 | 2/10/4 | 1/13/2 | N | N |  |
| 714 | UI_RoleEvaluate | 全屏背景界面 | 686 | 622 | 32 | 2/28/2 | 2/28/2 | Y | N |  |
| 715 | UI_RoleEvaluateSucc | 全屏背景界面 | 568 | 520 | 25 | 0/24/1 | 2/19/4 | Y | N |  |
| 716 | UI_RoleGuestsTip | 四边木栏（蒸笼标签）+横列表 | 812 | 512 | 19 | 4/14/1 | 4/11/4 | Y | N |  |
| 717 | UI_RoleHeadTip | 左-右 | 504 | 325 | 37 | 10/25/2 | 5/27/5 | Y | Y |  |
| 718 | UI_RoleObtainingTitleTips | 展示-横条-条内信息 | 380 | 449 | 11 | 1/10/0 | 2/6/3 | N | Y |  |
| 719 | UI_RoleOthter | 全屏背景界面 | 1222 | 698 | 26 | 1/24/1 | 2/21/3 | Y | N |  |
| 720 | UI_RoleRenameTip | 确认弹框 | 265 | 268 | 11 | 1/10/0 | 1/8/2 | N | Y |  |
| 721 | UI_RoleSkinTip | 活动打脸弹窗 | 633 | 573 | 17 | 3/13/1 | 2/9/6 | N | N |  |
| 722 | UI_RoleStageTip | 一体框 | 935 | 254 | 34 | 1/32/1 | 6/24/4 | Y | Y |  |
| 723 | UI_RoleUpTip | tips | 810 | 423 | 38 | 2/33/3 | 2/33/3 | Y | Y | ⚠ z=2.5 on middle_count |
| 724 | UI_RouteTrade | 上标题-中竖列表-下信息 | 1266 | 644 | 45 | 7/29/9 | 5/39/1 | Y | Y | ⚠ z=3.5 on right_count |
| 725 | UI_RouteTradeAccelerate | 确认弹框 | 466 | 305 | 31 | 0/28/3 | 4/24/3 | Y | Y |  |
| 726 | UI_RouteTradeAddition | 上标题-中竖列表-下信息 | 571 | 404 | 19 | 4/11/4 | 1/17/1 | Y | N |  |
| 727 | UI_RouteTradeBoss | 左-右 | 789 | 444 | 25 | 5/16/4 | 3/16/6 | Y | N |  |
| 728 | UI_RouteTradeBossResult | 展示-横条-条内信息 | 789 | 458 | 22 | 1/19/2 | 2/18/2 | Y | N |  |
| 729 | UI_RouteTradeDispatch | T型-上标题-左-右 | 534 | 455 | 31 | 1/26/4 | 2/25/4 | Y | N |  |
| 730 | UI_RouteTradeDispatchSucc | 展示-横条-左右对比 | 543 | 352 | 18 | 4/10/4 | 5/11/2 | N | N |  |
| 731 | UI_RouteTradeItem | tips | 48 | 86 | 17 | 0/14/3 | 2/12/3 | Y | N |  |
| 732 | UI_RouteTradeTip | 确认弹框 | 291 | 293 | 16 | 2/14/0 | 2/13/1 | N | N |  |
| 733 | UI_RuleTip | tips | 624 | 184 | 10 | 1/8/1 | 2/7/1 | Y | N |  |
| 734 | UI_SDKLogin | 登录加载全屏 | 590 | 282 | 16 | 1/14/1 | 4/8/4 | N | N |  |
| 735 | UI_SeaEvidence | 地图底 | 1074 | 529 | 53 | 4/43/6 | 4/44/5 | Y | Y |  |
| 736 | UI_SeaEvidenceAdd | 使用弹框 | 527 | 467 | 29 | 5/19/5 | 6/16/7 | Y | N | ⚠ z=3.5 on top_count |
| 737 | UI_SeaEvidenceAddSucc | 展示-横条-条内信息 | 789 | 475 | 20 | 2/16/2 | 3/15/2 | N | N |  |
| 738 | UI_SeaEvidenceArea | 确认弹框 | 520 | 374 | 22 | 1/17/4 | 3/17/2 | Y | N |  |
| 739 | UI_SeaEvidenceTip | tips | 407 | 224 | 11 | 1/7/3 | 2/8/1 | N | N |  |
| 740 | UI_ServerList | 左艺术设计+左-右 | 941 | 118 | 21 | 1/19/1 | 1/18/2 | Y | N |  |
| 741 | UI_Setting | 一体框 | 860 | 435 | 39 | 9/26/4 | 6/26/7 | N | N | ⚠ z=2.7 on left_count |
| 742 | UI_SettingPush | 上标题-中横列表-下信息 | 954 | 260 | 16 | 1/14/1 | 2/13/1 | Y | N |  |
| 743 | UI_Shop | 墙+小旗+横列表 | 1144 | 517 | 69 | 5/63/1 | 4/63/2 | Y | N |  |
| 744 | UI_ShopCommonActShop | 上标题-中横列表-下信息 | 713 | 377 | 33 | 2/28/3 | 6/25/2 | Y | Y |  |
| 745 | UI_ShopGiftPurchase | 确认弹框 | 208 | 403 | 21 | 1/20/0 | 4/15/2 | Y | N |  |
| 746 | UI_ShopPurchase | 使用弹框 | 476 | 367 | 23 | 1/20/2 | 2/19/2 | N | N |  |
| 747 | UI_ShopUnlockTips | tips | 364 | 174 | 16 | 1/13/2 | 1/13/2 | N | N |  |
| 748 | UI_Sidebar | 确认弹框 | 594 | 375 | 21 | 1/15/5 | 3/15/3 | N | N |  |
| 749 | UI_SilkCaravan | 活动打脸弹窗 | 975 | 285 | 25 | 2/21/2 | 4/18/3 | Y | N |  |
| 750 | UI_SilkroadAccelerate | 活动打脸弹窗 | 209 | 276 | 15 | 2/8/5 | 1/12/2 | N | N |  |
| 751 | UI_SilkroadActGift | 上标题-中竖列表-下信息 | 795 | 413 | 39 | 2/34/3 | 3/34/2 | Y | N |  |
| 752 | UI_SilkroadAppraisal | 活动打脸弹窗 | 835 | 541 | 31 | 3/24/4 | 3/26/2 | Y | N |  |
| 753 | UI_SilkroadAppraisalPreview | 一体框 | 696 | 374 | 24 | 1/20/3 | 5/17/2 | Y | N |  |
| 754 | UI_SilkroadAppraisalReward | 展示-横条-条内信息 | 568 | 366 | 15 | 2/12/1 | 3/10/2 | Y | N |  |
| 755 | UI_SilkroadAssistant | 左广告图-右列表 | 598 | 395 | 26 | 6/13/7 | 2/16/8 | Y | N |  |
| 756 | UI_SilkroadBattleTailReward | 大背景-展示 | 411 | 394 | 20 | 1/19/0 | 1/17/2 | Y | Y |  |
| 757 | UI_SilkroadBox | 确认弹框 | 680 | 294 | 27 | 2/24/1 | 1/22/4 | Y | N |  |
| 758 | UI_SilkroadBuffEvent | panel | 554 | 400 | 23 | 1/21/1 | 2/17/4 | N | N |  |
| 759 | UI_SilkroadBuffEventResult | tips | 279 | 311 | 16 | 1/14/1 | 1/12/3 | N | N |  |
| 760 | UI_SilkroadCashGift | 确认弹框 | 229 | 329 | 25 | 2/18/5 | 3/18/4 | Y | N |  |
| 761 | UI_SilkroadDamageRank | 上标题-中上标签-中竖列表-下信息 | 531 | 426 | 31 | 5/25/1 | 4/26/1 | Y | N |  |
| 762 | UI_SilkroadEncourageReward | 上标题-中竖列表-下信息 | 604 | 241 | 24 | 2/20/2 | 4/19/1 | Y | N |  |
| 763 | UI_SilkroadFightSelectGuest | 上标题-中横列表-下信息 | 618 | 609 | 44 | 4/38/2 | 1/41/2 | Y | N |  |
| 764 | UI_SilkroadGains | T型-上标题-左标签-右竖列表 | 695 | 468 | 76 | 8/61/7 | 1/70/5 | Y | N | ⚠ z=3.2 on middle_count |
| 765 | UI_SilkroadGuestInfo | 左-右 | 550 | 442 | 24 | 4/14/6 | 3/18/3 | N | N |  |
| 766 | UI_SilkroadInspire | 上标题-中横列表-下信息 | 360 | 312 | 22 | 1/20/1 | 2/17/3 | Y | N |  |
| 767 | UI_SilkroadMain | 红框方形玩法入口 | 1043 | 480 | 54 | 3/45/6 | 6/45/3 | Y | Y |  |
| 768 | UI_SilkroadManuals | 上标题-中上标签-中竖列表-下信息 | 399 | 266 | 28 | 5/19/4 | 3/24/1 | Y | N |  |
| 769 | UI_SilkroadMap | panel+入口 | 3320 | 666 | 99 | 1/96/2 | 6/82/11 | Y | Y | ⚠ z=3.0 on width |
| 770 | UI_SilkroadMeetEvent | 左广告图-右列表 | 384 | 302 | 23 | 1/18/4 | 2/19/2 | Y | N |  |
| 771 | UI_SilkroadMemberSelect | 上标题-中竖列表-下信息 | 875 | 465 | 24 | 5/16/3 | 3/19/2 | Y | N |  |
| 772 | UI_SilkroadMission | 左广告图-右列表 | 1134 | 552 | 63 | 11/47/5 | 6/43/14 | Y | Y | ⚠ z=2.8 on bottom_count |
| 773 | UI_SilkroadMissionScoreAdd | N/A | 553 | 235 | 4 | 1/3/0 | 0/3/1 | N | N |  |
| 774 | UI_SilkroadMonsterFight | 红框方形玩法入口 | 1148 | 954 | 104 | 5/90/9 | 8/91/5 | Y | Y |  |
| 775 | UI_SilkroadMonsterSwitch | 上标题-中竖列表-下信息 | 448 | 351 | 17 | 2/14/1 | 1/15/1 | Y | N |  |
| 776 | UI_SilkroadOasisOverview | 上标题-中竖列表-下信息 | 868 | 506 | 35 | 4/23/8 | 4/29/2 | Y | N | ⚠ z=2.9 on right_count |
| 777 | UI_SilkroadOpening | N/A | 966 | 470 | 8 | 2/4/2 | 1/6/1 | N | N |  |
| 778 | UI_SilkroadQucikTeleport | tips | 2 | 85 | 6 | 1/4/1 | 3/1/2 | N | N |  |
| 779 | UI_SilkroadQuickBuffResult | 展示-横条-条内信息 | 385 | 615 | 16 | 3/12/1 | 2/13/1 | Y | N |  |
| 780 | UI_SilkroadRank | 上标题-中竖列表-下信息 | 672 | 334 | 33 | 4/26/3 | 5/27/1 | Y | N |  |
| 781 | UI_SilkroadRankReward | 上标题-中竖列表-下信息 | 609 | 428 | 28 | 4/22/2 | 3/22/3 | Y | N |  |
| 782 | UI_SilkroadRankServerRank | panel | 1044 | 391 | 17 | 2/12/3 | 2/11/4 | Y | N |  |
| 783 | UI_SilkroadRetreatRuleTip | tips | 26 | 181 | 8 | 4/0/4 | 3/4/1 | Y | N |  |
| 784 | UI_SilkroadTeleport | 确认弹框 | 224 | 141 | 12 | 1/10/1 | 2/7/3 | N | N |  |
| 785 | UI_SilkroadTeleportReward | 展示-横条-条内信息 | 409 | 446 | 22 | 2/20/0 | 2/18/2 | Y | Y |  |
| 786 | UI_SilkroadTrade | 确认弹框 | 384 | 314 | 17 | 2/13/2 | 1/13/3 | Y | N |  |
| 787 | UI_SilkroadTradeConfirm | 确认弹框 | 227 | 169 | 12 | 1/10/1 | 1/8/3 | N | N |  |
| 788 | UI_SilkroadTreasure | 左-中-右 | 646 | 420 | 32 | 1/27/4 | 2/27/3 | Y | N |  |
| 789 | UI_SingleMarketOut | 上标题-中横列表-下信息 | 953 | 422 | 29 | 1/27/1 | 5/17/7 | Y | N |  |
| 790 | UI_SkillDescTips | N/A | 298 | 203 | 22 | 4/15/3 | 3/15/4 | N | N |  |
| 791 | UI_SkyscraperActivity | 红框方形玩法入口 | 1029 | 1442 | 85 | 8/70/7 | 2/83/0 | Y | N | ⚠ z=3.3 on height |
| 792 | UI_SkyscraperRank | 左标签+右竖列表 | 655 | 437 | 44 | 9/32/3 | 6/33/5 | Y | Y |  |
| 793 | UI_SkyscraperReco | 上标题-中竖列表-下信息 | 247 | 233 | 11 | 2/9/0 | 1/10/0 | Y | N |  |
| 794 | UI_SkyscraperRedPacket | 左广告图-右列表 | 806 | 607 | 27 | 2/23/2 | 3/21/3 | Y | N |  |
| 795 | UI_SkyscraperRedPacketTip | 功能开启&展示 | 628 | 299 | 10 | 1/8/1 | 1/7/2 | N | Y |  |
| 796 | UI_SoloMarket | 上标题-中上标签-中竖列表-下信息 | 1136 | 479 | 58 | 3/50/5 | 5/49/4 | Y | N |  |
| 797 | UI_SpaceHonor | 全屏背景界面 | 80 | 56 | 6 | 0/5/1 | 4/0/2 | N | N |  |
| 798 | UI_SpaceInfo | 全屏背景界面 | 441 | 353 | 13 | 1/11/1 | 1/10/2 | Y | N |  |
| 799 | UI_SpaceRank | 上标题-中竖列表-下信息 | 826 | 470 | 39 | 6/29/4 | 1/36/2 | Y | N |  |
| 800 | UI_SpaceTop | 全屏背景界面 | 884 | 257 | 23 | 2/20/1 | 1/20/2 | N | N |  |
| 801 | UI_StarLevelTip | N/A | 121 | 116 | 5 | 1/2/2 | 1/3/1 | N | N |  |
| 802 | UI_StarWorks | mainUI | 489 | 108 | 15 | 1/14/0 | 3/11/1 | N | N |  |
| 803 | UI_StarWorksChoiceBeauty | 四边木栏（蒸笼标签）+横列表 | 995 | 629 | 53 | 5/43/5 | 5/38/10 | Y | N |  |
| 804 | UI_StarWorksChoiceUp | T型-上标题-左-右 | 485 | 330 | 17 | 3/11/3 | 5/9/3 | N | N |  |
| 805 | UI_StarWorksEndorse | 上标题-中横列表-下信息 | 283 | 353 | 19 | 1/16/2 | 5/10/4 | Y | N |  |
| 806 | UI_StarWorksLevelInfo | T型-上标题-左-右 | 459 | 399 | 27 | 5/17/5 | 4/17/6 | N | N |  |
| 807 | UI_StarWorksLevelUp | 展示-横条-条内信息 | 377 | 495 | 19 | 2/12/5 | 3/13/3 | N | Y |  |
| 808 | UI_StarWorksUpAni | tips | 362 | 320 | 10 | 1/8/1 | 1/7/2 | N | N |  |
| 809 | UI_StarWorksUpResult | 展示-横条-条内信息 | 502 | 482 | 42 | 4/28/10 | 3/34/5 | N | Y | ⚠ z=3.8 on right_count |
| 810 | UI_StreetFight | 左-中-右 | 1097 | 568 | 98 | 10/77/11 | 8/81/9 | Y | N |  |
| 811 | UI_StreetFightAddVit | 使用弹框 | 554 | 466 | 29 | 4/22/3 | 3/22/4 | Y | N |  |
| 812 | UI_StreetFightAttrTip | tips | 30 | 126 | 5 | 1/2/2 | 1/3/1 | N | Y |  |
| 813 | UI_StreetFightBattle | 战斗 | 840 | 729 | 108 | 8/90/10 | 9/90/9 | Y | N | ⚠ z=2.6 on left_count |
| 814 | UI_StreetFightJumpResult | 展示-横条-左图-右信息 | 879 | 596 | 32 | 5/25/2 | 2/27/3 | Y | Y |  |
| 815 | UI_StreetFightMarket | 上标题-中竖列表-下信息 | 1150 | 495 | 39 | 4/30/5 | 2/36/1 | Y | N |  |
| 816 | UI_StreetFightResult | 展示-横条-左图-右信息 | 813 | 680 | 54 | 6/43/5 | 1/47/6 | Y | Y |  |
| 817 | UI_StreetFightSolo | 上标题-中横列表-下信息 | 769 | 492 | 56 | 2/49/5 | 7/42/7 | Y | Y |  |
| 818 | UI_StreetFightSweep | 使用弹框 | 475 | 527 | 29 | 3/23/3 | 2/25/2 | Y | N |  |
| 819 | UI_StreetFightSweepResult | 展示-横条-条内信息 | 839 | 690 | 28 | 2/22/4 | 2/24/2 | Y | Y |  |
| 820 | UI_StreetFightTarget | 上标题-中横列表-下信息 | 948 | 488 | 33 | 2/30/1 | 5/25/3 | Y | N |  |
| 821 | UI_StreetFightTask | T型-上标题-左标签-右竖列表 | 864 | 501 | 30 | 4/24/2 | 1/28/1 | Y | N |  |
| 822 | UI_StreetFightTip | 确认弹框 | 252 | 237 | 25 | 1/22/2 | 2/18/5 | Y | N |  |
| 823 | UI_StreetFightWait | 功能开启&展示 | 371 | 374 | 11 | 2/7/2 | 1/8/2 | N | N |  |
| 824 | UI_StreetTreasureDetail | 上标题-中竖列表-下信息 | 363 | 224 | 17 | 0/15/2 | 1/15/1 | Y | N |  |
| 825 | UI_StreetTreasureFind | 确认弹框 | 787 | 336 | 21 | 4/13/4 | 2/17/2 | Y | Y |  |
| 826 | UI_StreetTreasureList | tips | 115 | 48 | 10 | 1/8/1 | 0/9/1 | Y | N |  |
| 827 | UI_StreetTreasureTip | N/A | 186 | 117 | 9 | 3/2/4 | 4/3/2 | N | N |  |
| 828 | UI_SurpriseGift | 活动打脸弹窗 | 804 | 348 | 29 | 2/25/2 | 2/25/2 | Y | Y |  |
| 829 | UI_SurpriseSeriesGift | 横列表 | 1016 | 530 | 34 | 2/31/1 | 1/32/1 | Y | N |  |
| 830 | UI_TalkBubbleList | N/A | 263 | 159 | 6 | 1/5/0 | 2/2/2 | Y | N |  |
| 831 | UI_TalkReview | tips | 467 | 274 | 8 | 0/7/1 | 1/7/0 | Y | N |  |
| 832 | UI_TalkSelect | 确认弹框 | 483 | 335 | 31 | 2/27/2 | 3/26/2 | N | N |  |
| 833 | UI_TargetPro | N/A | 98 | 227 | 4 | 2/1/1 | 1/2/1 | N | N |  |
| 834 | UI_Task | 左艺术设计+左-右 | 998 | 764 | 73 | 2/66/5 | 6/63/4 | Y | N |  |
| 835 | UI_TaskChapter | 左右艺术设计+横列表 | 1014 | 429 | 31 | 3/26/2 | 3/26/2 | Y | N |  |
| 836 | UI_TaskChapterTip | 左-右 | 705 | 510 | 15 | 2/10/3 | 2/12/1 | Y | Y |  |
| 837 | UI_TaskFinishTip | N/A | 151 | 368 | 9 | 1/6/2 | 1/8/0 | N | N |  |
| 838 | UI_TaskGroupReward | 上标题-中竖列表-下信息 | 662 | 94 | 29 | 1/21/7 | 2/22/5 | Y | N |  |
| 839 | UI_TaskMainTip | N/A | 256 | 1189 | 9 | 1/6/2 | 1/7/1 | N | N |  |
| 840 | UI_TaskProgressTip | tips | 356 | 477 | 19 | 1/17/1 | 2/12/5 | N | N |  |
| 841 | UI_TaskSprint | T型-上标题-左标签-右竖列表 | 784 | 316 | 37 | 2/33/2 | 4/30/3 | Y | N |  |
| 842 | UI_TaskTalk | 一体框 | 729 | 618 | 43 | 3/38/2 | 3/34/6 | Y | Y |  |
| 843 | UI_TeamApplyList | 上标题-中竖列表-下信息 | 964 | 171 | 23 | 3/16/4 | 3/17/3 | Y | N |  |
| 844 | UI_TeamEnterFail | 确认弹框 | 258 | 328 | 19 | 2/14/3 | 1/16/2 | Y | N |  |
| 845 | UI_TeamFriend | 上标题-中横列表-下信息 | 859 | 345 | 50 | 1/44/5 | 5/42/3 | Y | N |  |
| 846 | UI_TeamGuestTrial | N/A | 1969 | 888 | 55 | 3/50/2 | 0/53/2 | Y | N |  |
| 847 | UI_TeamInfo | 上标题-中横列表-下信息 | 935 | 529 | 85 | 3/76/6 | 9/65/11 | Y | Y | ⚠ z=4 on center_count |
| 848 | UI_TeamInviteList | 上标题-中竖列表-下信息 | 677 | 265 | 26 | 3/19/4 | 0/25/1 | Y | N |  |
| 849 | UI_TeamList | T型-上标题-左标签-右竖列表 | 772 | 341 | 39 | 5/29/5 | 0/36/3 | Y | N |  |
| 850 | UI_TeamMarket | 上标题-中上标签-中竖列表-下信息 | 775 | 479 | 49 | 5/39/5 | 3/41/5 | Y | N |  |
| 851 | UI_TeamTip | 确认弹框 | 13 | 269 | 12 | 1/11/0 | 2/9/1 | N | N |  |
| 852 | UI_Techno | 全屏背景界面 | 922 | 547 | 35 | 3/28/4 | 3/31/1 | N | N |  |
| 853 | UI_TechnoCourse | 上标题-中横列表-下信息 | 817 | 517 | 41 | 2/37/2 | 3/31/7 | Y | N |  |
| 854 | UI_TechnoCourseTip | tips | 382 | 200 | 16 | 4/9/3 | 2/8/6 | N | N | ⚠ z=2.7 on bottom_count |
| 855 | UI_TechnoCup | 全屏背景界面 | 610 | 526 | 13 | 0/12/1 | 1/11/1 | N | N |  |
| 856 | UI_TechnoCupAchi | 一体框 | 459 | 429 | 44 | 2/39/3 | 2/40/2 | N | N |  |
| 857 | UI_TechnoCupInfo | 左-右 | 651 | 344 | 34 | 2/29/3 | 0/31/3 | Y | N |  |
| 858 | UI_TechnoCupShow | T型-上标题-左-右 | 566 | 439 | 29 | 3/20/6 | 2/22/5 | Y | N |  |
| 859 | UI_TechnoExam | 打开书页 | 1063 | 613 | 33 | 6/23/4 | 6/21/6 | N | N |  |
| 860 | UI_TechnoExamResult | N/A | 271 | 218 | 7 | 1/5/1 | 2/3/2 | N | N |  |
| 861 | UI_TechnoInfo | N/A | 999 | 702 | 31 | 2/24/5 | 3/21/7 | Y | N |  |
| 862 | UI_TechnoStudy | N/A | 846 | 538 | 24 | 3/18/3 | 7/11/6 | N | Y |  |
| 863 | UI_TechnoStudyCourse | N/A | 314 | 731 | 16 | 1/12/3 | 2/12/2 | N | Y |  |
| 864 | UI_TechnoTips | tips | 452 | 306 | 15 | 2/11/2 | 3/9/3 | Y | N |  |
| 865 | UI_TestServer | 测试界面 | 956 | 364 | 13 | 2/9/2 | 5/2/6 | Y | N |  |
| 866 | UI_TimeLineOption | N/A | 4 | 2 | 4 | 0/3/1 | 0/3/1 | N | N |  |
| 867 | UI_TimerTravel | 地图底 | 351 | 604 | 19 | 3/15/1 | 1/17/1 | Y | N |  |
| 868 | UI_TimerTravelInfo | 左右艺术设计+一体 | 1066 | 448 | 47 | 7/34/6 | 2/37/8 | Y | Y |  |
| 869 | UI_TitleTips | tips | 264 | 302 | 11 | 6/1/4 | 1/8/2 | N | N | ⚠ z=3 on left_count |
| 870 | UI_TokensError | 确认弹框 | 124 | 287 | 8 | 1/6/1 | 1/6/1 | N | N |  |
| 871 | UI_TokensLimit | 确认弹框 | 62 | 183 | 10 | 4/4/2 | 2/5/3 | N | N |  |
| 872 | UI_TopLeague | 赛程 | 1380 | 574 | 76 | 2/69/5 | 5/60/11 | Y | N |  |
| 873 | UI_TopLeagueBattle | 战斗 | 1135 | 940 | 84 | 3/75/6 | 5/77/2 | Y | N |  |
| 874 | UI_TopLeagueBetRank | 左标签+右竖列表 | 740 | 434 | 43 | 5/35/3 | 2/35/6 | Y | Y |  |
| 875 | UI_TopLeagueComment | N/A | 666 | 320 | 6 | 1/4/1 | 0/5/1 | Y | N |  |
| 876 | UI_TopLeagueDesc | tips | 604 | 375 | 20 | 2/14/4 | 3/14/3 | N | N |  |
| 877 | UI_TopLeagueEvent | T型-上标题-左标签-右竖列表 | 1261 | 603 | 46 | 1/39/6 | 4/41/1 | Y | N |  |
| 878 | UI_TopLeagueGetSign | N/A | 903 | 327 | 16 | 1/14/1 | 1/12/3 | N | N |  |
| 879 | UI_TopLeagueMarket | 左右对比 | 548 | 424 | 43 | 5/32/6 | 5/35/3 | Y | N |  |
| 880 | UI_TopLeagueProgress | 上标题-中横列表-下信息 | 476 | 326 | 18 | 2/16/0 | 2/14/2 | Y | N |  |
| 881 | UI_TopLeagueRank | 左图-右竖列表 | 1168 | 606 | 43 | 3/36/4 | 6/32/5 | Y | N |  |
| 882 | UI_TopLeagueReady | 横条-VS | 494 | 410 | 14 | 4/9/1 | 1/12/1 | N | N |  |
| 883 | UI_TopLeagueRecord | 上标题-中竖列表-下信息 | 1112 | 318 | 28 | 1/23/4 | 2/25/1 | Y | N |  |
| 884 | UI_TopLeagueResult | 展示-横条-条内信息 | 788 | 395 | 28 | 4/21/3 | 5/20/3 | N | Y |  |
| 885 | UI_TopLeagueReward | 上标题-中竖列表-下信息 | 470 | 460 | 23 | 1/20/2 | 1/19/3 | Y | Y |  |
| 886 | UI_TopLeagueShop | 上标题-中横列表-下信息 | 635 | 359 | 22 | 1/20/1 | 1/20/1 | Y | N |  |
| 887 | UI_TopLeagueSignTip | N/A | 834 | 580 | 10 | 1/8/1 | 1/7/2 | N | N |  |
| 888 | UI_TopLeagueWager | 使用弹框 | 476 | 350 | 24 | 2/18/4 | 2/20/2 | N | N |  |
| 889 | UI_TotalStrengthTip | N/A | 330 | 148 | 10 | 1/7/2 | 1/8/1 | N | N |  |
| 890 | UI_TradePvp | panel+入口 | 1220 | 578 | 45 | 4/39/2 | 2/39/4 | N | N |  |
| 891 | UI_TradeWar | 四边木栏（蒸笼标签）+入口 | 1096 | 578 | 105 | 12/83/10 | 12/76/17 | Y | Y |  |
| 892 | UI_TradeWarAddVit | T型-上标题-左-右 | 500 | 334 | 18 | 2/14/2 | 5/11/2 | N | N |  |
| 893 | UI_TradeWarAnnounce | 左右艺术设计+竖列表 | 1168 | 590 | 21 | 1/18/2 | 1/19/1 | Y | N |  |
| 894 | UI_TradeWarBattle | 四边木栏（蒸笼标签）+入口 | 2453 | 592 | 80 | 1/79/0 | 9/59/12 | Y | Y |  |
| 895 | UI_TradeWarBatttleSet | 确认弹框 | 312 | 255 | 14 | 2/9/3 | 1/11/2 | N | N |  |
| 896 | UI_TradeWarBoss | panel+入口 | 1000 | 490 | 43 | 6/33/4 | 6/29/8 | Y | N |  |
| 897 | UI_TradeWarBossJump | 确认弹框 | 253 | 299 | 16 | 1/14/1 | 2/12/2 | Y | N |  |
| 898 | UI_TradeWarConsume | 上标题-中竖列表-下信息 | 557 | 89 | 18 | 0/14/4 | 2/15/1 | Y | N |  |
| 899 | UI_TradeWarFind | 上标题-中上标签-中竖列表-下信息 | 870 | 405 | 61 | 10/43/8 | 7/50/4 | Y | N | ⚠ z=2.7 on left_count |
| 900 | UI_TradeWarFloor | T型-上标题-左标签-右竖列表 | 768 | 191 | 22 | 1/18/3 | 1/18/3 | Y | N |  |
| 901 | UI_TradeWarGuests | 上标题-中横列表-下信息 | 1207 | 530 | 55 | 2/45/8 | 5/40/10 | Y | N | ⚠ z=3.3 on right_count |
| 902 | UI_TradeWarItem | tips | 297 | 274 | 8 | 3/1/4 | 1/5/2 | N | N |  |
| 903 | UI_TradeWarMarket | 左广告图-右列表 | 654 | 326 | 22 | 0/20/2 | 5/13/4 | Y | N |  |
| 904 | UI_TradeWarPetition | 确认弹框 | 577 | 302 | 44 | 3/35/6 | 4/33/7 | Y | N | ⚠ z=4.3 on bottom_count |
| 905 | UI_TradeWarPetitionUp | 上标题-中竖列表-下信息 | 606 | 234 | 23 | 2/18/3 | 3/17/3 | Y | N |  |
| 906 | UI_TradeWarPveResult | 展示-横条-条内信息 | 886 | 369 | 50 | 4/38/8 | 0/44/6 | Y | Y | ⚠ z=2.7 on right_count |
| 907 | UI_TradeWarReport | 上标题-中竖列表-下信息 | 840 | 240 | 25 | 3/17/5 | 1/23/1 | Y | N |  |
| 908 | UI_TradeWarResult | 展示-横条-条内信息 | 786 | 637 | 37 | 2/32/3 | 3/32/2 | Y | Y |  |
| 909 | UI_TradeWarSetting | 确认弹框 | 336 | 256 | 16 | 2/12/2 | 1/14/1 | N | N |  |
| 910 | UI_TradeWarTech | 左标签+中图+右信息 | 882 | 539 | 39 | 2/33/4 | 2/31/6 | Y | N |  |
| 911 | UI_TradeWarTechGet | 展示-横条-条内信息 | 785 | 538 | 16 | 3/10/3 | 5/7/4 | N | Y |  |
| 912 | UI_TradeWarTechTip | 横列表 | 342 | 774 | 54 | 4/46/4 | 2/47/5 | Y | N |  |
| 913 | UI_TradingPort | mainUI | 1056 | 334 | 31 | 2/27/2 | 4/26/1 | Y | N |  |
| 914 | UI_TradingPortChangeShip | 左-右 | 971 | 419 | 48 | 2/41/5 | 6/38/4 | Y | N |  |
| 915 | UI_TradingPortCompose | 使用弹框 | 486 | 384 | 28 | 3/22/3 | 3/17/8 | Y | N | ⚠ z=3.2 on bottom_count |
| 916 | UI_TradingPortComposeQuick | 确认弹框 | 358 | 470 | 21 | 1/20/0 | 1/18/2 | Y | N |  |
| 917 | UI_TradingPortDeCombine | T型-上标题-左-右 | 656 | 405 | 35 | 2/29/4 | 2/31/2 | Y | N |  |
| 918 | UI_TradingPortDecorateBag | T型-上标题-左-右 | 560 | 456 | 34 | 2/22/10 | 2/28/4 | Y | N |  |
| 919 | UI_TradingPortDecorateResolve | T型-上标题-左-右 | 789 | 461 | 39 | 3/28/8 | 3/32/4 | Y | N |  |
| 920 | UI_TradingPortDock | 四边木栏（蒸笼标签）+左中右 | 1041 | 578 | 125 | 10/96/19 | 16/93/16 | Y | N |  |
| 921 | UI_TradingPortDockUnlock | 确认弹框 | 214 | 312 | 10 | 2/7/1 | 1/8/1 | N | N |  |
| 922 | UI_TradingPortFactory | 一体框 | 468 | 482 | 34 | 2/27/5 | 2/29/3 | Y | N |  |
| 923 | UI_TradingPortFleet | 四边木栏（蒸笼标签）+横列表 | 1073 | 440 | 24 | 3/20/1 | 3/20/1 | Y | N |  |
| 924 | UI_TradingPortNewShip | N/A | 848 | 360 | 28 | 1/24/3 | 5/20/3 | N | N |  |
| 925 | UI_TradingPortQueryAttr | 左标签-右信息 | 760 | 258 | 30 | 5/22/3 | 2/28/0 | Y | Y |  |
| 926 | UI_TradingPortShipPosUnlock | 上标题-中竖列表-下信息 | 574 | 393 | 15 | 2/11/2 | 1/11/3 | N | N |  |
| 927 | UI_TradingPortStrengthen | N/A | 704 | 580 | 39 | 1/29/9 | 4/28/7 | Y | N |  |
| 928 | UI_TradingPortSupplyInfo | 确认弹框 | 410 | 347 | 12 | 2/9/1 | 1/9/2 | N | N |  |
| 929 | UI_TradingPortSupplyLvUnlock | tips | 534 | 268 | 16 | 4/9/3 | 2/11/3 | Y | N |  |
| 930 | UI_TradingPortSupplyRecords | 上标题-中竖列表-下信息 | 538 | 281 | 19 | 2/15/2 | 1/16/2 | Y | N |  |
| 931 | UI_TradingPortUpPreview | 展示-横条-左右对比 | 786 | 523 | 22 | 1/20/1 | 3/16/3 | N | N |  |
| 932 | UI_TradingPorttUseItem | 使用弹框 | 472 | 346 | 21 | 2/17/2 | 2/18/1 | N | N |  |
| 933 | UI_TrialSpacetime | panel | 1010 | 588 | 72 | 6/60/6 | 10/54/8 | Y | N |  |
| 934 | UI_TrialSpacetimeBoss | 左广告图-右列表 | 1022 | 582 | 54 | 9/44/1 | 5/45/4 | Y | N |  |
| 935 | UI_TrialSpacetimeDrop | N/A | 634 | 348 | 43 | 3/36/4 | 2/37/4 | Y | N |  |
| 936 | UI_TrialSpacetimeHighResult | 展示-横条-左图-右信息 | 1060 | 818 | 39 | 6/29/4 | 3/32/4 | Y | Y |  |
| 937 | UI_TrialSpacetimeMiddleResult | 展示-横条-左图-右信息 | 1060 | 772 | 44 | 4/37/3 | 3/37/4 | Y | Y |  |
| 938 | UI_TrialSpacetimeMsgs | N/A | 340 | 371 | 7 | 1/5/1 | 1/5/1 | Y | N |  |
| 939 | UI_TrialSpacetimeRecord | 左标签-右信息 | 430 | 294 | 8 | 2/5/1 | 3/0/5 | N | Y |  |
| 940 | UI_TrialSpacetimeRewardPreview | 上标题-中竖列表-下信息 | 574 | 269 | 24 | 1/22/1 | 2/22/0 | Y | N |  |
| 941 | UI_TrialSpacetimeSnatchResult | 展示-横条-左图-右信息 | 1060 | 836 | 31 | 7/20/4 | 3/23/5 | N | Y |  |
| 942 | UI_TrialSpacetimeTradeWar | panel+入口 | 1025 | 491 | 48 | 6/37/5 | 7/34/7 | Y | Y |  |
| 943 | UI_UpgradeCoatingSucc | 展示-横条-左右对比 | 603 | 407 | 12 | 1/10/1 | 1/9/2 | N | Y |  |
| 944 | UI_UseMultItem | 使用弹框 | 472 | 454 | 21 | 2/17/2 | 2/17/2 | N | N |  |
| 945 | UI_UseViceCurrency | 确认弹框 | 124 | 287 | 11 | 1/7/3 | 1/8/2 | N | N |  |
| 946 | UI_VWo12 | 活动打脸弹窗 | 541 | 451 | 26 | 1/23/2 | 2/22/2 | Y | N |  |
| 947 | UI_VideoPlayer | N/A | 767 | 288 | 7 | 1/5/1 | 0/6/1 | N | N |  |
| 948 | UI_VipGift | 左艺术设计+左-右 | 931 | 413 | 53 | 1/45/7 | 2/45/6 | Y | N |  |
| 949 | UI_VisitMain | mainUI | 462 | 361 | 32 | 5/21/6 | 2/24/6 | N | N |  |
| 950 | UI_VisitOptTips | N/A | 263 | 129 | 16 | 2/10/4 | 8/1/7 | N | N |  |
| 951 | UI_VisitPlayerTitle | tips | 299 | 408 | 20 | 2/17/1 | 1/15/4 | Y | N |  |
| 952 | UI_VisitRecord | 上标题-中竖列表-下信息 | 526 | 352 | 28 | 3/21/4 | 3/23/2 | Y | N |  |
| 953 | UI_VisitUsePropsConfirm | 确认弹框 | 284 | 325 | 19 | 1/14/4 | 1/15/3 | N | N |  |
| 954 | UI_WaitNet | N/A | 0 | 16 | 2 | 0/2/0 | 1/0/1 | N | N |  |
| 955 | UI_WishMakingExchange | 木屏风+横列表 | 555 | 557 | 40 | 7/33/0 | 6/29/5 | Y | N |  |
| 956 | UI_WishMakingGift | 左标签-右信息 | 1907 | 497 | 58 | 1/53/4 | 8/43/7 | Y | N |  |
| 957 | UI_WishMakingGiftTips | 使用弹框 | 569 | 317 | 21 | 5/14/2 | 2/18/1 | N | N |  |
| 958 | UI_WishMakingLotteryTips | 确认弹框 | 60 | 231 | 15 | 2/11/2 | 2/12/1 | N | N |  |
| 959 | UI_WishMakingMain | 红框方形玩法入口 | 910 | 522 | 28 | 2/25/1 | 1/25/2 | N | Y |  |
| 960 | UI_WishMakingPreview | 一体框 | 391 | 412 | 35 | 6/29/0 | 2/32/1 | N | N |  |
| 961 | UI_WishMakingResetTips | 确认弹框 | 708 | 492 | 19 | 1/17/1 | 1/16/2 | Y | N |  |
| 962 | UI_WishMakingSelectReward | 上标题-中横列表-下信息 | 267 | 352 | 21 | 1/20/0 | 1/18/2 | Y | N |  |
| 963 | UI_WorldBuild | 左-右 | 604 | 368 | 34 | 7/22/5 | 4/26/4 | N | N |  |
| 964 | UI_WorldBuildFinish | 左-右 | 419 | 340 | 21 | 2/15/4 | 3/16/2 | N | N |  |
| 965 | UI_WorldWonderBuildSucc | 展示-横条-左右对比 | 423 | 428 | 22 | 3/18/1 | 2/18/2 | N | Y |  |
| 966 | UI_WorldWonders | 左右艺术设计+一体 | 1061 | 539 | 49 | 5/42/2 | 3/32/14 | Y | N |  |
| 967 | UI_XiaoZhuShou | 活动打脸弹窗 | 127 | 180 | 6 | 3/1/2 | 0/5/1 | N | N |  |
| 968 | UI_YardDispach | 上标题-中横列表-下信息 | 632 | 477 | 31 | 1/28/2 | 6/19/6 | Y | N |  |
| 969 | UI_YardDispachResult | tips | 94 | 259 | 17 | 4/12/1 | 1/15/1 | N | N |  |
| 970 | UI_YardMeet | 四边木栏（蒸笼标签）+横列表 | 1351 | 499 | 40 | 3/32/5 | 7/29/4 | Y | N |  |
| 971 | UI_YardMentInfo | 横列表 | 774 | 532 | 44 | 6/35/3 | 2/39/3 | Y | Y |  |
| 972 | UI_YardRankTips | 上标题-中竖列表-下信息 | 748 | 257 | 14 | 3/9/2 | 1/12/1 | Y | Y |  |
| 973 | UI_YardResultTips | 展示-横条-条内信息 | 740 | 483 | 17 | 1/14/2 | 2/12/3 | N | Y |  |

---

## 结论与建议

1. **81 个统计异常 UI 需要人工截图复核**，确认 wiki 类型是否准确
2. **82 个无类型的 UI** 需要分配 wiki 布局类型
3. **特征分析的局限性**: 当前仅基于 prefab 节点的数量和位置分布，无法识别：
   - 视觉装饰元素（木栏框、艺术设计、灯笼等）
   - 节点的语义角色（哪个是标题、哪个是列表、哪个是按钮）
   - T型布局的上标题是否贯穿全宽
4. **改进建议**: 需要增加视觉分析能力（截图识别）或更细粒度的 prefab 结构分析（如识别 Image/Sprite/Button 组件的语义角色）


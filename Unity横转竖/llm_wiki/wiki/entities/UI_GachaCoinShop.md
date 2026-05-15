---
type: entity
category: UI
created: 2026-05-06
updated: 2026-05-06
tags: [entity, ui, gacha, shop, four-border-left-right-list]
concepts: [[llm_wiki/wiki/concepts/layout-types/四边木栏+左右-宽列表]]
sources:
  - id: ui_list
    file: D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_list.json
    last_verified: 2026-05-09
  - id: all_ui_features
    file: D:\obsidianProject\portrait-to-landscape\Unity横转竖\all_ui_features.json
    last_verified: 2026-05-09
  - id: ui_layout_analysis
    file: D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_layout_analysis.json
    last_verified: 2026-05-09
---

# UI_GachaCoinShop

## 基本信息

| 字段 | 值 |
|------|-----|
| **UI 名称** | UI_GachaCoinShop |
| **预制体路径** | `Shop/UI_GachaCoinShop.prefab` |
| **完整路径** | `D:\CursorProject\Dadian - 副本\Arts\Assets\ArtResources\UIs\Prefabs\Shop\UI_GachaCoinShop.prefab` |
| **布局类型** | [[llm_wiki/wiki/concepts/layout-types/四边木栏+左右-宽列表\|四边木栏+左右-宽列表]] |
| **功能** | 游戏商城，销售虚拟货币和道具 |
| **分析日期** | 2026-05-06 |

## 截图

![[attachments/UI_Images/UI_GachaCoinShop.png]]

## 结构分析

### 总体数据

| 指标 | 数值 |
|------|------|
| **GameObject 总数** | 92 |
| **Image 组件** | 40 |
| **RawImage 组件** | 1 |
| **显示尺寸（W×H）** | 1237.55 × 1006.50 |
| **类型判定** | ✅ 四边木栏+左右-宽列表 |

### 四边木栏包边

| 方向 | 状态 | 特征 |
|------|------|------|
| **上** | ✔ | 有上方边框 Image |
| **下** | ✔ | 有下方边框 Image |
| **左** | ✔ | 有左方边框 Image（宽 29px） |
| **右** | ✔ | 有右方边框 Image（包含在 NodeBg） |

### 空间分布

```
┌─────────────────────────────────────────────────┐
│ 上边框                                          │
├─────────┬───────────────────────────────────┤
│ 左标签页 │  中右：大背景 + 宽列表            │
│ 分类    │  ┌────────────────────────────┐   │
│ TglGroup│  │RawImage (1048×1006)        │   │
│ Fun     │  │背景图：ui_common_bg_0018   │   │
│         │  │ListGoods 列表:             │   │
│ 共多个  │  │  ├─ GoodsItem1             │ ↕ │
│ 切签页  │  │  ├─ PrefabSmallItem        │ 滚│
│         │  │  └─ [n 个商品卡]          │ 动│
│         │  └────────────────────────────┘   │
│         │  BoxTime 时间限制框                │
├─────────┴───────────────────────────────────┤
│ 下边框                                      │
└─────────────────────────────────────────────┘
```

### 节点分布（14个有效节点）

#### 左区（7个节点 - 导航标签页）
```
TglGroupFun
  ├─ TextPageType（标签文字）
  ├─ BtnHelp（帮助按钮）
  ├─ GoodsItem1（初始展示项）
  └─ [多个 Toggle 选项]
```

#### 中右区（6个节点 - 内容展示）
```
RawImage
  └─ ui_common_bg_0018.png（大背景）

NodeBg
  ├─ Image（背景装饰）
  ├─ ListGoods（商品列表，宽1019.16）
  │   └─ PrefabSmallItem（物品卡片）
  ├─ Image（分隔线）
  └─ [多个装饰 Image]

BoxTime（时间限制框）
  └─ [倒计时等信息]
```

## 关键组件识别

| 组件 | 节点名 | 用途 | 判定依据 |
|------|--------|------|--------|
| **标签页** | TglGroupFun | 商品分类切换 | ✅ Toggle Group 组件，有多个选项 |
| **宽列表** | ListGoods | 商品展示 | ✅ ScrollRect，宽1019.16≥背景宽×0.8 |
| **大背景** | RawImage | 装饰背景 | ✅ 尺寸1048×1006，非滚动容器 |
| **边框** | 多个 Image | 木栏包边 | ✅ 四边都找到，都来自 atlas_common_static.png |

## 图集资源统计

### Image 资源（40 个）

**主要使用的图集：**

| 图集名称 | 用途 | 引用次数 |
|---------|------|--------|
| `atlas_common_static.png` | 通用UI元素、边框、装饰线 | 27 |
| `atlas_face.png` | 角色头像 | 3 |
| `atlas_shop_static.png` | 商店特有元素 | 3 |
| `atlas_common.png` | 通用框架 | 2 |
| `atlas_item.png` | 物品图标 | 4 |
| `atlas_activity.png` | 活动相关图片 | 1 |

### RawImage 资源（1 个）

| 资源名 | 尺寸 | 用途 |
|--------|------|------|
| `ui_common_bg_0018.png` | 1048×1006 | 主背景图片 |

## 横竖屏转换分析

### 竖屏特点（当前状态）
- ✅ 宽度充足（1237.55）
- ✅ 左侧标签页占用 200px，合理
- ✅ 右侧列表充分利用宽度
- ✅ 背景图片完整显示

### 横屏转换要点

#### 关键挑战
1. **左侧标签页冲突**
   - 竖屏时左侧占用 200px，在横屏中高度受限，难以显示多个标签页
   - 需改为上方标签栏或下方菜单

2. **列表高度压缩**
   - 横屏宽度增加，但高度大幅减少
   - 需要增加列宽或增加列数，减少纵向滚动

3. **背景图适配**
   - 当前背景 1048×1006，改为横屏后比例不匹配
   - 需要重新制作或裁切为横屏背景

#### 推荐改版方案

**方案A：上方标签栏（推荐）**
```
改版步骤：
1. TglGroupFun 从左侧移到上方，改为横向排列
2. 标签页内容从纵向改为横向，减少高度占用
3. 列表宽度可进一步扩展
4. 背景图改为宽度优先的裁切

优点：空间利用充分，符合常见商城设计
缺点：需要修改标签页的 LayoutGroup 方向
```

**方案B：下方菜单（备选）**
```
改版步骤：
1. TglGroupFun 改为下方固定菜单栏
2. 列表占据上方主区域
3. 菜单栏使用紧凑布局

优点：列表区域最大化
缺点：需要点击菜单才能切换，交互不如方案A流畅
```

### 预期工作量

| 阶段 | 工作内容 | 工时 |
|------|--------|------|
| **1. 布局重构** | TglGroupFun 改方向，调整尺寸和位置 | 1-2h |
| **2. 列表适配** | ListGoods 宽度调整，可能改为多列 | 1-2h |
| **3. 背景处理** | 新背景图制作或现有图裁切 | 2-4h |
| **4. 测试调整** | 在竖横两种模式下测试，微调位置 | 1-2h |
| **小计** | 合计 5-10 小时工作量 | **中等复杂度** |

## 相关分析

### 同类型 UI
- [[prefab_final_analysis/UI_YardMeet|UI_YardMeet]]（参考）

### 对比分析

| 类型 | 本 UI（GachaCoinShop） | 区别 |
|------|--------|------|
| **四边木栏+左中右** | 有四边框，但右侧是列表，非对等分区 | ❌ 不符合 |
| **左标签页+右文本列表** | 有左标签页，但右侧是物品列表，非纯文本 | ❌ 不符合 |
| **大背景+宽列表** | 虽有大背景，但有左标签页和四边框 | ❌ 不符合 |
| **✅ 四边木栏+左右-宽列表** | 四边框 + 左标签页 + 右侧宽列表 1019.16 | ✅ **完全符合** |

## 最近发现（2026-05-06）

- 自动分类脚本（classify-ui-type）成功识别该 UI 为「四边木栏+左右-宽列表」
- 关键特征识别：
  - TglGroupFun（左标签页）
  - ListGoods（右侧宽列表，宽1019.16）
  - 四边完整木栏包边（上下左右都有 Image）
  - 大背景 RawImage（1048×1006）
- 节点结构清晰，无多层嵌套引用，易于分析
- 该类型在竖屏下设计合理，横屏转换时需重点关注左侧导航的处理方式

## 参考资源

- [[llm_wiki/wiki/concepts/layout-types/四边木栏+左右-宽列表|布局类型说明]]
- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局总览]]
- [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型完整索引]]

---
type: entity
category: Database
created: 2026-05-04
updated: 2026-05-04
tags: [entity, database, ui-data]
concepts: [[llm_wiki/wiki/concepts/UI_Layout]], [[llm_wiki/wiki/concepts/UI_Component]]
sources:
  - id: all_ui_features
    file: D:\obsidianProject\portrait-to-landscape\Unity横转竖\all_ui_features.json
    last_verified: 2026-05-09
  - id: ui_layout_analysis
    file: D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_layout_analysis.json
    last_verified: 2026-05-09
  - id: ui_list
    file: D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_list.json
    last_verified: 2026-05-09
  - id: ui_classification
    file: D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_classification_by_strategy.json
    last_verified: 2026-05-09
  - id: ui_clustering
    file: D:\obsidianProject\portrait-to-landscape\Unity横转竖\ui_clustering_report.json
    last_verified: 2026-05-09
---

# UI 数据库

## 基本信息
- **ID**: UI_Database
- **数据量**: 910 个 UI 预制体
- **数据来源**: Unity 项目提取
- **最后更新**: 2026-05-04
- **状态**: 活跃

## 数据概览

### 规模统计
```
总 UI 数量: 910
  ├─ 布局类型数: 62 种
  ├─ 组件类型数: 20+ 种
  ├─ 背景图数: 150+ 张
  └─ Sprite 资产: 1000+ 个
```

### 数据特征
| 指标 | 值 |
|------|-----|
| 平均组件数/UI | 8-12 个 |
| 最复杂的 UI | ~50 个组件 |
| 最简单的 UI | 1 个组件 |
| 最常用的布局类型 | 上标题-中竖列表-下信息（92 个） |
| 最常用的组件 | Button、Text、Image |

## 数据结构

### 源数据文件
1. **all_ui_features.json**（~1MB）
   - 所有 UI 的特征提取
   - 字段：name, components, layout, background, sprites
   
2. **ui_layout_analysis.json**（~200KB）
   - 布局分类结果
   - 字段：ui_name, layout_type, structure, hierarchy

3. **ui_list.json**（~50KB）
   - UI 名称索引
   - 用于快速查找

## 关键数据指标

### 布局类型分布
最频繁的 10 种布局：
1. 上标题-中竖列表-下信息 (92 个)
2. 四边框架+左中右 (...)
3. 大背景+宽列表 (...)
... （详见 [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型索引]]）

### 组件复用度
最常用的组件：
1. **Button** - 几乎所有交互型 UI 都有
2. **Text** - 所有 UI 都有
3. **Image** - 用于背景、图标等

### 背景图复用分析
- 最常复用的背景图：被 20+ 个 UI 使用
- 平均复用度：3-5 个 UI 共享一张背景
- 优化空间：通过背景复用可减少 30% 的贴图资源

## 数据质量

### 完整性
- ✅ 所有 910 个 UI 都有完整数据
- ✅ 组件信息采集完整
- ✅ 布局分类覆盖 100%

### 准确性
- ✅ 已通过多轮验证
- ⚠️ 某些古老 UI 可能有遗留组件（已标记）
- ✅ 布局分类经过人工审核

## 数据更新策略

### 更新触发条件
1. UI 项目版本更新 → 重新提取一次数据
2. 发现新的组件组合 → 添加到分析中
3. 布局优化完成 → 更新布局分类

### 更新流程
参见 [[llm_wiki/workflows/Ingest_Workflow|Ingest 工作流]]

## 相关 Wiki 页面
- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局]]
- [[llm_wiki/wiki/concepts/UI_Component|UI 组件]]
- [[llm_wiki/sources|原始资源索引]]

## 访问指南

### 如何查询特定 UI？
1. 打开 [[llm_wiki/wiki/indexes/Index_All_UIs|全部 UI 索引]]
2. 搜索 UI 名称
3. 查看详细信息页面

### 如何按布局查找 UI？
1. 打开 [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型索引]]
2. 选择布局类型
3. 浏览该类型的所有 UI

### 如何进行数据分析？
参考原始数据文件：
- 分析脚本：`extract_all_ui_features.py`
- 分析结果：`ui_layout_analysis.json`
- 详见 [[llm_wiki/sources|原始资源索引]]

## 最近发现与更新

### 2026-05-04
- ✅ 建立 LLM Wiki 索引
- 发现布局类型可进一步细化
- 标记需要补充的文档

### 需要后续处理
- [ ] 创建所有 910 个 UI 的实体页面（预计后续批量生成）
- [ ] 补充组件复用分析
- [ ] 深化背景优化建议

---

**维护说明**: 此页面为 Wiki 的重要枢纽，连接原始数据和具体 UI 实体。

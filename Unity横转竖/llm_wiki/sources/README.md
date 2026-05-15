# 原始资源索引

## 📄 说明
这个目录包含所有原始的、不可变的源文档和数据。
LLM 从这些源中提取信息，但不修改这些源文件。

## 📚 当前资源清单

### UI 相关数据源

#### 1. UI 预制体数据
- **文件**: `all_ui_features.json`
- **来源**: Unity 项目提取
- **大小**: ~1MB
- **内容**: 所有 910 个 UI 预制体的特征数据
- **更新频率**: 按项目版本更新
- **相关 Wiki 页面**: [[llm_wiki/wiki/entities/UI_Database|UI 数据库]]

#### 2. UI 布局分析
- **文件**: `ui_layout_analysis.json`
- **来源**: Claude Code 分析生成
- **内容**: 910 个 UI 的布局分类和结构分析
- **相关 Wiki 页面**: [[llm_wiki/wiki/concepts/UI_Layout|UI 布局]]

#### 3. UI 列表
- **文件**: `ui_list.json`
- **来源**: 项目数据导出
- **内容**: 完整的 UI 名称列表
- **相关 Wiki 页面**: [[llm_wiki/wiki/indexes/Index_All_UIs|全部 UI 索引]]

#### 4. Sprite 预制体索引
- **文件**: `prefab_sprites_index.json`
- **来源**: Unity 资源提取
- **大小**: ~5MB
- **内容**: 所有预制体中使用的 Sprite 图片索引
- **相关 Wiki 页面**: [[llm_wiki/wiki/concepts/Sprite_Asset|Sprite 资产]]

---

### 背景图像数据源

#### 1. 背景图像列表
- **文件**: `background_image_list.md`
- **来源**: UI 分析结果
- **内容**: 所有背景图像及其使用频率
- **相关 Wiki 页面**: [[llm_wiki/wiki/concepts/Background_Images|背景图像]]

#### 2. 背景分析报告
- **文件**: `background_analysis_summary.md`
- **来源**: Claude Code 生成的分析报告
- **内容**: 背景复用情况、优化建议
- **相关 Wiki 页面**: [[llm_wiki/wiki/guides/Background_Optimization|背景优化指南]]

---

### 布局分类数据源

#### 1. 布局分类报告
- **文件**: `prefab_similarity_report.md`
- **来源**: 相似度分析脚本
- **内容**: 布局相似性分析和聚类结果
- **相关 Wiki 页面**: [[llm_wiki/wiki/concepts/Layout_Similarity|布局相似性]]

#### 2. UI 布局分析数据
- **文件**: `ui_layout_analysis.json`
- **来源**: 结构化分析
- **内容**: 详细的布局特征和分类
- **相关 Wiki 页面**: [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型索引]]

---

### 提取日志和报告

#### 1. 预制体提取日志
- **文件**: `prefab_extraction.log`
- **来源**: 自动提取工具
- **大小**: ~300KB
- **内容**: 完整的数据提取过程记录
- **用途**: 调试和验证数据完整性

#### 2. 预制体分析报告
- **文件**: `prefab_analysis_report.md`
- **来源**: 初期分析结果
- **内容**: 预制体特征分析概览
- **相关 Wiki 页面**: [[llm_wiki/wiki/entities/Prefab_Database|预制体数据库]]

---

### 脚本和工具源代码

#### 1. 特征提取脚本
- **文件**: `extract_all_ui_features.py`
- **来源**: 开发脚本
- **用途**: 从 Unity 项目提取 UI 特征数据
- **相关 Wiki 页面**: [[llm_wiki/wiki/guides/Data_Extraction_Guide|数据提取指南]]

#### 2. UI 分类脚本
- **文件**: `classify_by_strategy.py`, `cluster_uis.py`
- **来源**: 分析工具集
- **用途**: 进行 UI 分类和聚类

---

## 🔄 资源管理规则

### ✅ 允许的操作
- 阅读源文件以提取信息
- 创建 Wiki 页面总结源文件内容
- 建立源文件与 Wiki 页面的映射关系
- 在 Wiki 中引用源文件（通过链接或脚注）

### ❌ 禁止的操作
- **不修改** 源文件内容
- **不删除** 源文件
- **不重命名** 源文件
- 源文件是不可变的记录

### 如何处理过时源文件
1. 标记页面为 `#deprecated`
2. 在 Wiki 中记录为什么过时
3. 链接到新的源文件
4. 保留原始文件用于历史追踪

---

## 📊 数据统计

| 类别 | 数量 | 大小 |
|------|------|------|
| UI 预制体 | 910 | - |
| JSON 数据文件 | 5 | ~6MB |
| 日志文件 | 1 | ~300KB |
| 分析报告 | 5+ | ~50KB |
| 脚本文件 | 3 | ~50KB |
| **总计** | **914+** | **~6.5MB** |

---

## 🔗 索引映射

此索引链接到相应的 Wiki 概念和实体页面：
- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局概念]]
- [[llm_wiki/wiki/entities/UI_Database|UI 数据库实体]]
- [[llm_wiki/wiki/indexes/Index_All_UIs|全部 UI 索引]]
- [[llm_wiki/wiki/guides/Data_Extraction_Guide|数据提取指南]]

---

**最后更新**: 2026-05-04  
**维护者**: Claude LLM Wiki System

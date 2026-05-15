---
type: qa
created: 2026-05-06
updated: 2026-05-06
tags: [qa, ui-classification, automation, daily-check]
related: [[llm_wiki/wiki/guides/UI_Classification_Quick_Guide]], [[llm_wiki/wiki/indexes/Index_Layout_Types]]
---

# UI 分类一致性检查日志

## 说明

本页面由自动化定时任务自动生成和更新。每 3 分钟随机选择一张 UI 图片，进行以下检查：

1. **图片分析**：使用 Claude 分析图片内容，判断 UI 类型
2. **数据库查询**：在 llm_wiki 中搜索该 UI 的现有分类
3. **结果对比**：检查分析结果与已有分类是否一致
4. **问题记录**：如果发现不一致，记录问题和建议处理方案

---

## 最近检查结果

### 日期统计

| 日期 | 检查次数 | 通过数 | 问题数 | 通过率 |
|------|--------|--------|--------|--------|
| 2026-05-06 | 0 | 0 | 0 | - |

### 问题记录

*暂无问题记录*

---

## 检查流程说明

### Step 1：选择随机图片
```
从 D:\CursorProject\Dadian - 副本\Arts\Assets\Doc\UIImage\ 
随机选择一张 UI_*.png 图片
```

### Step 2：分析图片
```
Claude 阅读图片内容，根据以下维度判断 UI 类型：
- 四边框的有无
- 左侧结构（导航、信息、立绘）
- 右侧结构（列表、信息、立绘）
- 其他特殊元素（标题、标签页、抽屉）
```

### Step 3：查询已有分类
```
在 llm_wiki/wiki/entities/ 中搜索该 UI 的页面
提取页面中的布局类型信息
```

### Step 4：对比结果
```
判断分析结果与已有分类是否一致：
- 完全相同 → ✅ 通过
- 不同但属于同一大类 → ✅ 通过
- 完全不同 → ⚠️ 需要处理
```

### Step 5：记录问题
```
如果发现不一致：
1. 分析不一致的原因
2. 判断正确的分类
3. 更新相关文档
4. 同步到 llm_wiki
```

---

## 已检查的 UI 列表

| 检查时间 | UI 名称 | 分析结果 | 已有分类 | 结果 | 备注 |
|---------|--------|--------|--------|------|------|
| 暂无数据 | - | - | - | - | - |

---

## 问题修复跟踪

### 待处理问题

*暂无待处理问题*

### 已修复问题

*暂无修复记录*

---

## 系统配置

| 项目 | 值 |
|------|-----|
| 检查频率 | 每 3 分钟 |
| 图片源目录 | D:\CursorProject\Dadian - 副本\Arts\Assets\Doc\UIImage\ |
| 分类数据库 | llm_wiki/wiki/entities/ |
| QA 记录目录 | llm_wiki/wiki/qa/ |
| 脚本文件 | C:\Users\guowe\.openclaw\workspace-code\ui_classification_verify.ps1 |

---

## 相关资源

- [[llm_wiki/wiki/guides/UI_Classification_Quick_Guide|快速识别指南]]
- [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型索引]]
- [[llm_wiki/DASHBOARD|Wiki 仪表板]]

---

**自动更新时间**：每次检查完成后立即更新本页面  
**最后更新**：2026-05-06 08:30（创建时间）  
**系统状态**：✅ 已启用，等待首次检查

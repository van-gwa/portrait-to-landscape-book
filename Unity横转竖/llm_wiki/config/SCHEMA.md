---
type: meta
created: 2026-05-04
updated: 2026-05-09
tags: [meta, schema]
---

# LLM Wiki 结构定义（Schema）

## 📋 版本信息
- **版本**: 1.0
- **创建日期**: 2026-05-04
- **最后修改**: 2026-05-04
- **维护者**: Claude

---

## 1. 整体架构

```
llm_wiki/
├── sources/           # 📄 原始资源层（不可变）
├── wiki/              # 📚 Wiki 知识库层
│   ├── concepts/      # 概念页面
│   ├── entities/      # 实体页面
│   ├── guides/        # 指南文档
│   └── indexes/       # 索引和导航
├── config/            # ⚙️ 配置层
└── workflows/         # 🔄 工作流指南
```

---

## 2. Wiki 页面类型与规范

### 2.1 概念页面（Concepts）
**目的**：解释核心概念和原理

**文件名**：`[concept-name].md`
**路径**：`llm_wiki/wiki/concepts/`

**必须字段**（frontmatter）：
```yaml
---
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
related: [[related-page1]], [[related-page2]]
---
```

**页面结构**：
```
# 概念名称

## 定义
简洁的概念定义

## 核心原理
深入解释

## 相关概念
- [[related-concept-1]]
- [[related-concept-2]]

## 应用场景
用在什么地方

## 参考资源
原始来源或延伸阅读
```

**示例**：
- [[llm_wiki/wiki/concepts/UI_Layout|UI布局]]
- [[llm_wiki/wiki/concepts/UI_Component|UI组件]]

---

### 2.2 实体页面（Entities）
**目的**：记录特定的 UI、配置或对象

**文件名**：`[entity-name].md`
**路径**：`llm_wiki/wiki/entities/`

**必须字段**（frontmatter）：
```yaml
---
type: entity
category: UI | Configuration | Pattern
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
concepts: [[concept1]], [[concept2]]
sources: [[source-file]]
---
```

**页面结构**：
```
# 实体名称

## 基本信息
- **ID**: 
- **分类**: 
- **状态**: 

## 描述
详细描述

## 属性
- 属性1: 值
- 属性2: 值

## 关联关系
- 属于概念：[[concept]]
- 相关实体：[[entity1]], [[entity2]]
- 源文件：[[source]]

## 最近发现
记录最新的分析发现
```

**示例**：
- [[llm_wiki/wiki/entities/UI_Bag|UI_Bag界面]]
- [[llm_wiki/wiki/entities/FrameScrollRect|Frame滚动组件]]

---

### 2.3 指南页面（Guides）
**目的**：提供工作流指南和最佳实践

**文件名**：`[guide-name].md`
**路径**：`llm_wiki/wiki/guides/`

**必须字段**（frontmatter）：
```yaml
---
type: guide
status: draft | published | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
related: [[related-guide1]]
---
```

**示例**：
- [[llm_wiki/wiki/guides/UI_Conversion_Guide|UI转换指南]]
- [[llm_wiki/wiki/guides/Component_Analysis_Guide|组件分析指南]]

---

### 2.4 索引页面（Indexes）
**目的**：提供导航和汇总

**文件名**：`Index_[topic].md`
**路径**：`llm_wiki/wiki/indexes/`

**特点**：
- 聚合相关页面的链接
- 使用 Dataview 生成动态索引（可选）
- 用于分类浏览和快速导航

**示例**：
- [[llm_wiki/wiki/indexes/Index_UI_Layouts|布局类型索引]]
- [[llm_wiki/wiki/indexes/Index_Components|组件索引]]

---

## 3. Frontmatter 字段说明

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| type | enum | ✓ | concept/entity/guide/index |
| created | date | ✓ | 创建日期 YYYY-MM-DD |
| updated | date | ✓ | 最后更新日期 |
| tags | array | ✓ | 分类标签 |
| related | array | ✗ | 相关页面链接 |
| category | enum | 条件 | entity 类型需要 |
| status | enum | 条件 | guide 类型需要 |
| concepts | array | 条件 | entity 类型可选 |
| sources | array | 条件 | entity/guide 类型可选 |

---

## 4. 标签规范（Tagging Convention）

### 按内容类型
- `#concept` - 概念页面
- `#entity` - 实体页面
- `#guide` - 指南页面

### 按 UI 分类
- `#layout-type-[name]` - 布局类型（如 `#layout-type-four-border`）
- `#component-[type]` - 组件类型（如 `#component-button`）
- `#pattern-[name]` - 设计模式（如 `#pattern-portrait-landscape`）

### 按优先级
- `#high-priority` - 高优先级（影响大）
- `#medium-priority` - 中等优先级
- `#low-priority` - 低优先级

### 按状态
- `#needs-update` - 需要更新
- `#needs-verification` - 需要验证
- `#incomplete` - 不完整

---

## 5. 链接约定

### Wiki 内链接
```markdown
[[page-name]] 或 [[folder/page-name]]
```

### 外部链接
```markdown
[描述](URL)
```

### 反向链接用途
- 概念页面：通过反向链接发现所有使用该概念的实体
- 实体页面：通过反向链接追踪所有涉及该实体的分析

---

## 6. 版本控制

每个页面都应该维护：
- **created**: 创建时间（不变）
- **updated**: 最后更新时间（每次修改时更新）
- **status**: 页面状态（draft/published/archived）

---

## 7. 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 概念页面 | 小写+连字符 | `ui-layout`, `scroll-behavior` |
| 实体页面 | 保留原名 | `UI_Bag`, `FrameScrollRect` |
| 指南页面 | Title Case | `UI_Conversion_Guide` |
| 索引页面 | `Index_[Topic]` | `Index_UI_Layouts` |
| 文件夹 | 小写+下划线 | `concepts`, `entities` |

---

## 8. 质量指标

### 页面完整性检查清单
- [ ] 有正确的 frontmatter 字段
- [ ] 至少有 3 个相关链接
- [ ] 标签数量在 2-5 个之间
- [ ] 没有断裂的 Wiki 链接
- [ ] 最后更新日期在 1 个月内

### Wiki 整体健康度
- **孤立页面**：无任何传入或传出链接的页面
- **断裂链接**：指向不存在页面的链接
- **未分类内容**：缺少标签的页面
- **过期信息**：超过 3 个月未更新的页面

---

## 9. 更新日志

| 日期 | 变更 | 说明 |
|------|------|------|
| 2026-05-04 | 初始版本 | 创建基础 Schema 框架 |

---

## 相关文档
- [[llm_wiki/workflows/Ingest_Workflow|Ingest 工作流]]
- [[llm_wiki/workflows/Query_Workflow|Query 工作流]]
- [[llm_wiki/workflows/Lint_Workflow|Lint 工作流]]

---
type: guide
status: published
created: 2026-05-04
updated: 2026-05-04
tags: [guide, getting-started, wiki-management]
related: [[llm_wiki/workflows/Ingest_Workflow]], [[llm_wiki/workflows/Query_Workflow]], [[llm_wiki/workflows/Lint_Workflow]]
---

# LLM Wiki 快速开始

## 🎯 5 分钟快速上手

这是为 Unity 横竖屏项目建立的 **LLM 知识库系统**。按照本指南快速理解结构和使用方式。

---

## 📁 项目结构一览

```
llm_wiki/
├── config/
│   └── SCHEMA.md          ← 📋 Wiki 规范和定义（重要！）
├── sources/
│   └── README.md          ← 📄 原始资源索引
├── wiki/
│   ├── concepts/          ← 📚 概念页面（如"UI布局"、"组件"）
│   ├── entities/          ← 🔹 实体页面（如具体的UI）
│   ├── guides/            ← 📖 指南和最佳实践
│   └── indexes/           ← 🗂️ 索引和导航
└── workflows/
    ├── Ingest_Workflow.md  ← ➕ 处理新数据
    ├── Query_Workflow.md   ← 🔍 查询和合成
    └── Lint_Workflow.md    ← 🧹 清理和维护
```

---

## 🚀 三大核心操作

### 1️⃣ Ingest（摄入）- 处理新源文档
**何时用**：你获得了新的数据、分析结果或项目更新

**做什么**：
- 阅读新文档
- 将信息分解为 Wiki 页面
- 创建或更新相关页面
- 建立交叉引用

**指南**：[[llm_wiki/workflows/Ingest_Workflow|完整 Ingest 工作流]]
**预计时间**：1-2 小时（小规模内容）

---

### 2️⃣ Query（查询）- 回答问题并充实 Wiki
**何时用**：有人提问，你需要找答案

**做什么**：
- 搜索 Wiki 找相关页面
- 综合信息生成答案
- 发现 Wiki 的缺陷或不足
- 创建新页面补充知识库

**指南**：[[llm_wiki/workflows/Query_Workflow|完整 Query 工作流]]
**预计时间**：25-75 分钟

---

### 3️⃣ Lint（清理）- 定期维护 Wiki 健康
**何时用**：定期维护（每周或每月）

**做什么**：
- 发现断裂的链接
- 清理孤立页面
- 发现并调和矛盾信息
- 更新过期内容
- 生成健康报告

**指南**：[[llm_wiki/workflows/Lint_Workflow|完整 Lint 工作流]]
**预计时间**：15-30 分钟（轻量）/ 2-4 小时（完整）

---

## 📖 页面类型速记

### 概念页面（Concepts）
**用途**：解释核心概念和原理
**例如**：
- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局]]
- [[llm_wiki/wiki/concepts/UI_Component|UI 组件]]

**特点**：
- 相对稳定（不常改）
- 被很多其他页面引用
- 提供背景知识和定义

---

### 实体页面（Entities）
**用途**：记录具体的对象、UI、配置

**例如**：
- [[llm_wiki/wiki/entities/UI_Database|UI 数据库]]
- （将来的）[[llm_wiki/wiki/entities/UI_Bag|UI_Bag 界面]]

**特点**：
- 经常更新（随项目变化）
- 链接到概念页面
- 链接到源数据

---

### 指南页面（Guides）
**用途**：提供操作指南和最佳实践

**例如**：
- [[llm_wiki/workflows/Ingest_Workflow|Ingest 工作流]]
- [[llm_wiki/workflows/Query_Workflow|Query 工作流]]

**特点**：
- 关于"如何做"
- 包含步骤、检查清单、示例
- 从实践经验总结

---

### 索引页面（Indexes）
**用途**：导航和聚合

**例如**：
- [[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型索引]]（将创建）
- [[llm_wiki/wiki/indexes/Index_All_UIs|全部 UI 索引]]（将创建）

**特点**：
- 聚合相关页面的链接
- 经常被用来浏览
- 可使用 Dataview 动态生成

---

## 🎨 页面示例模板

### 新建概念页面
```markdown
---
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [concept, topic-name]
related: [[related-page1]], [[related-page2]]
---

# [概念名称]

## 定义
[简洁的定义]

## 核心原理
[深入解释]

## 相关概念
- [[related-concept-1]]
- [[related-concept-2]]

## 应用场景
[用在什么地方]

## 参考资源
[来源]
```

### 新建实体页面
```markdown
---
type: entity
category: UI | Configuration | Pattern
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [entity, category, specific-type]
concepts: [[concept1]], [[concept2]]
sources: [[source-file]]
---

# [实体名称]

## 基本信息
- **ID**: [id]
- **分类**: [category]

## 描述
[详细描述]

## 属性
[属性列表]

## 关联关系
- 属于概念：[[concept]]
- 相关实体：[[entity1]]

## 最近发现
[最新更新]
```

---

## 🔗 常用链接速记

| 需要... | 打开... |
|--------|---------|
| 查看 Wiki 规范 | [[llm_wiki/config/SCHEMA]] |
| 了解原始数据 | [[llm_wiki/sources]] |
| 处理新数据 | [[llm_wiki/workflows/Ingest_Workflow]] |
| 回答问题 | [[llm_wiki/workflows/Query_Workflow]] |
| 维护 Wiki | [[llm_wiki/workflows/Lint_Workflow]] |
| 查找概念 | [[llm_wiki/wiki/concepts/UI_Layout]] 等 |
| 查找实体 | [[llm_wiki/wiki/entities/UI_Database]] 等 |

---

## ✅ 核心规范要点

### Frontmatter（页面头部）
```yaml
---
type: concept | entity | guide | index  # 必需
created: YYYY-MM-DD                     # 必需
updated: YYYY-MM-DD                     # 必需
tags: [tag1, tag2]                      # 必需（2-5个）
related: [[page1]], [[page2]]           # 可选
---
```

### 标签规范
- `#concept` - 概念页面
- `#entity` - 实体页面
- `#guide` - 指南页面
- `#layout-type-[name]` - 布局类型
- `#component-[type]` - 组件类型
- `#needs-update` - 需要更新
- `#needs-verification` - 需要验证

### 命名规范
- **概念**：小写+连字符（ui-layout）
- **实体**：保留原名（UI_Bag）
- **指南**：Title Case（UI_Conversion_Guide）
- **索引**：Index_[Topic]（Index_Layout_Types）

---

## 🎓 学习路径

### 第一次使用
1. ✅ 已读：本快速开始指南
2. 👉 接下来：打开 [[llm_wiki/config/SCHEMA]] 理解完整规范
3. 👉 然后：浏览现有的示例页面（[[llm_wiki/wiki/concepts/UI_Layout]] 等）

### 准备做第一次 Ingest
1. 阅读：[[llm_wiki/workflows/Ingest_Workflow]]
2. 准备：新的源文档或数据
3. 执行：按工作流 5 个步骤操作
4. 完成：创建 3-10 个新 Wiki 页面

### 准备做第一次 Query
1. 阅读：[[llm_wiki/workflows/Query_Workflow]]
2. 有：一个需要回答的问题
3. 执行：搜索 Wiki、综合答案、更新知识库
4. 完成：给出回答，改进 2-3 个页面

### 准备做第一次 Lint
1. 阅读：[[llm_wiki/workflows/Lint_Workflow]]
2. 条件：Wiki 中已有 20+ 页
3. 执行：按工作流 6 个步骤扫描和修复
4. 完成：生成健康报告，修复问题

---

## ❓ 常见问题

**Q：我需要现在就创建所有 910 个 UI 的实体页面吗？**
A：不需要！这些页面可以按需创建。你可以先创建核心的概念和指南页面，然后在 Query 和 Ingest 过程中逐步添加具体 UI 实体。

**Q：什么时候应该创建新页面 vs 更新现有页面？**
A：概念完全新颖或需要独立详细说明时→创建新页面。信息补充、修正或增加示例时→更新现有页面。

**Q：如何确保 Wiki 不会变成混乱？**
A：通过定期 Lint（每周或每月）。Lint 工作流会帮你发现断裂链接、孤立页面、信息矛盾。

**Q：可以用 Dataview 动态生成索引吗？**
A：可以！但不是必须。简单的 Wiki 链接列表也完全够用。

---

## 📞 需要帮助？

- **理解规范**：看 [[llm_wiki/config/SCHEMA]]
- **了解工作流**：看 [[llm_wiki/workflows/Ingest_Workflow|Ingest]]、[[llm_wiki/workflows/Query_Workflow|Query]]、[[llm_wiki/workflows/Lint_Workflow|Lint]]
- **找页面模板**：本页面下面有

---

## 🎯 下一步

**现在就可以开始：**
1. ✅ 浏览现有的概念页面（[[llm_wiki/wiki/concepts/UI_Layout]]）
2. 👉 查看实体页面示例（[[llm_wiki/wiki/entities/UI_Database]]）
3. 👉 阅读一个工作流指南（推荐：[[llm_wiki/workflows/Query_Workflow]]）
4. 👉 考虑你的第一个操作：Ingest 新数据还是 Query 一个问题？

---

**建立时间**: 2026-05-04  
**维护者**: Claude LLM Wiki System  
**状态**: 🟢 活跃

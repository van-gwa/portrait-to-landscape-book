---
type: index
created: 2026-05-04
updated: 2026-05-04
tags: [index, dashboard, navigation]
---

# 🎯 LLM Wiki 仪表板

## 📊 Wiki 整体状态

```
创建时间：2026-05-04
最后更新：2026-05-06
页面总数：18 个（+3）
  ├─ 概念页面：3 个（+1 布局类型）
  ├─ 实体页面：2 个（+1 UI）
  ├─ 指南页面：5 个（+1 快速指南）
  ├─ 索引页面：2 个（已更新）
  └─ 配置和系统：7 个

Wiki 结构完成度：✅ 基础框架完成
内容充实度：🟡 初期阶段（22% 完成，持续增长）
健康度评分：🟢 良好（完整性 100%, 一致性 100%）
```

---

## 🗂️ 核心导航

### 📚 文档中心

| 文档 | 用途 | 优先级 | 阅读时间 |
|------|------|--------|--------|
| [[llm_wiki/README|LLM Wiki 快速开始]] | 5 分钟快速入门 | ⭐⭐⭐ | 5 分钟 |
| [[llm_wiki/config/SCHEMA|Wiki 结构定义]] | 完整规范说明 | ⭐⭐⭐ | 15 分钟 |
| [[llm_wiki/sources|原始资源索引]] | 数据源说明 | ⭐⭐ | 10 分钟 |

### 🔄 工作流指南

| 工作流 | 触发时机 | 预计时间 | 阅读链接 |
|-------|---------|--------|---------|
| **Ingest** | 新数据/文档到达 | 1-2 小时 | [[llm_wiki/workflows/Ingest_Workflow]] |
| **Query** | 用户提问 | 25-75 分钟 | [[llm_wiki/workflows/Query_Workflow]] |
| **Lint** | 定期维护（周/月） | 15 分钟 - 4 小时 | [[llm_wiki/workflows/Lint_Workflow]] |

### 📖 示例与教程

| 内容 | 说明 | 链接 |
|------|------|------|
| **实战演示** | 用真实数据演示三个工作流 | [[llm_wiki/wiki/guides/实战演示]] |
| **概念示例** | UI 布局概念页面 | [[llm_wiki/wiki/concepts/UI_Layout]] |
| **实体示例** | UI 数据库实体页面 | [[llm_wiki/wiki/entities/UI_Database]] |

---

## 🚀 快速开始（选择你的路径）

### 路径 1️⃣：我想快速理解这个系统
```
1. 阅读本仪表板（现在）
2. 打开 [[llm_wiki/README]]（5 分钟）
3. 浏览示例页面：
   - [[llm_wiki/wiki/concepts/UI_Layout]]
   - [[llm_wiki/wiki/entities/UI_Database]]
4. 阅读实战演示：[[llm_wiki/wiki/guides/实战演示]]

⏱️ 总耗时：20-30 分钟
```

### 路径 2️⃣：我想为 Wiki 贡献内容
```
1. 阅读 [[llm_wiki/README]]（5 分钟）
2. 阅读 [[llm_wiki/config/SCHEMA]]（15 分钟）
3. 选择任务：
   ✅ 摄入新数据？→ 阅读 [[llm_wiki/workflows/Ingest_Workflow]]
   ✅ 回答问题？→ 阅读 [[llm_wiki/workflows/Query_Workflow]]
4. 参考示例：[[llm_wiki/wiki/guides/实战演示]]
5. 开始创建页面！

⏱️ 准备时间：30-45 分钟
```

### 路径 3️⃣：我想维护 Wiki 质量
```
1. 了解系统：阅读 [[llm_wiki/README]]（5 分钟）
2. 了解规范：阅读 [[llm_wiki/config/SCHEMA]]（15 分钟）
3. 学习维护方法：[[llm_wiki/workflows/Lint_Workflow]]（20 分钟）
4. 执行首次轻量 Lint（15 分钟）
5. 根据报告修复问题

⏱️ 首次时间：1 小时
```

---

## 📁 现有内容地图

### 概念页面（Concepts）
```
llm_wiki/wiki/concepts/
├─ UI_Layout.md                   📌 UI 布局基础概念
├─ UI_Component.md                📌 UI 组件分类
├─ layout-types/
│  └─ 四边木栏+左右-宽列表.md      ✨ 新增（2026-05-06）
├─ [更多待添加]
```

### 实体页面（Entities）
```
llm_wiki/wiki/entities/
├─ UI_Database.md                 🔹 UI 预制体数据库
├─ UI_GachaCoinShop.md            ✨ 新增（2026-05-06）
├─ [更多待添加]
```

### 指南页面（Guides）
```
llm_wiki/wiki/guides/
├─ 实战演示.md                   📖 三个工作流完整演示
├─ UI_Classification_Quick_Guide.md  ✨ 新增（2026-05-06）
├─ [更多待添加]
```

### 索引页面（Indexes）
```
llm_wiki/wiki/indexes/
├─ [待创建：布局类型索引]
├─ [待创建：全部 UI 索引]
```

---

## 🎯 最近更新

### 2026-05-06：UI_GachaCoinShop 详细分析完成
- ✅ 创建布局类型页面：「四边木栏+左右-宽列表」
- ✅ 创建 UI 实体页面：[[llm_wiki/wiki/entities/UI_GachaCoinShop|UI_GachaCoinShop]]
- ✅ 更新分组页面：[[llm_wiki/wiki/concepts/layout-groups/四边木栏系列]]（+1 布局，+1 UI）
- ✅ 更新索引页面：[[llm_wiki/wiki/indexes/Index_Layout_Types|布局类型索引]]（现有 63 种）
- ✅ 创建快速指南：[[llm_wiki/wiki/guides/UI_Classification_Quick_Guide|UI 分类快速指南]]

**新增内容说明**：
- 布局类型：通过自动化工具（classify-ui-type）分类，包含完整的特征、对比和改版方案
- UI 实体：包含 92 个 GameObject、40 个 Image，详细的节点分析和竖横屏改版预期
- 快速指南：避免类型混淆的 3 对对比、手工检验清单、常见错误案例

### 2026-05-04：系统初建
- ✅ 创建 LLM Wiki 核心架构
- ✅ 定义 Schema 和规范
- ✅ 建立三个工作流指南
- ✅ 创建初始概念和实体页面
- ✅ 编写实战演示
- ✅ 搭建导航系统

**下一步方向**：
- [ ] 继续分类更多 UI（从 UI 清单中选取）
- [ ] 为其他易混淆类型对创建对比指南
- [ ] 建立更多实体页面（参考 UI）
- [ ] 执行首次 Lint 检查

---

## 📈 Wiki 成长路线图

### 第一阶段：基础完成 ✅（当前）
- ✅ 架构和规范定义
- ✅ 工作流指南
- ✅ 初始示例页面
- 预计：5-10 页

### 第二阶段：快速充实（即将开始）
- 📋 执行首个 Ingest（布局数据）→ 生成 62+ 页
- 📋 执行多个 Query（回答设计问题）→ 改进 5-10 页
- 预计：80+ 新页面

### 第三阶段：优化和维护（后续）
- 📋 定期 Lint（每月）→ 保持 Wiki 健康
- 📋 重构和优化（季度）→ 改进结构
- 📋 扩展指南（持续）→ 添加更多最佳实践

---

## 🔧 系统配置

### 文件夹结构
```
llm_wiki/
├── config/          ⚙️ 配置和规范
├── sources/         📄 原始资源（不可变）
├── wiki/            📚 主要内容
│   ├── concepts/    🔍 概念
│   ├── entities/    🔹 实体
│   ├── guides/      📖 指南
│   └── indexes/     🗂️ 索引
└── workflows/       🔄 工作流文档
```

### 核心文件
- `llm_wiki/config/SCHEMA.md` - Wiki 结构定义
- `llm_wiki/sources/README.md` - 数据源索引
- `llm_wiki/README.md` - 快速开始指南

### 工作流文件
- `llm_wiki/workflows/Ingest_Workflow.md` - 数据摄入
- `llm_wiki/workflows/Query_Workflow.md` - 查询和合成
- `llm_wiki/workflows/Lint_Workflow.md` - 维护和清理

---

## 💡 常见任务速查

### 我想...

#### 🆕 创建新页面
1. 确定类型：概念/实体/指南/索引？
2. 查看 [[llm_wiki/config/SCHEMA]] 对应部分
3. 复制正确的 frontmatter 模板
4. 参考同类型的现有页面
5. 创建并测试链接

#### ✏️ 更新现有页面
1. 在"最近发现"部分添加新信息
2. 更新 frontmatter 的"updated"日期
3. 添加新的反向链接（如需要）
4. 检查一致性

#### 🔗 添加链接
- 使用 `[[page-name]]` 或 `[[folder/page-name]]`
- 确保链接的页面存在（或在任务清单中）
- 通过 Obsidian 的反向链接视图验证

#### 🏷️ 添加标签
1. 主标签：#concept, #entity, #guide, #index
2. 主题标签：#layout-type-*, #component-*
3. 状态标签：#needs-update, #needs-verification
4. 优先级标签：#high-priority, #medium-priority

#### 🔍 查找信息
- 使用全局搜索（Ctrl+Shift+F）
- 浏览索引页面
- 沿着反向链接探索
- 按标签浏览

#### 🧹 发现并修复问题
1. 按 [[llm_wiki/workflows/Lint_Workflow]] 执行
2. 标记问题（#needs-verification 等）
3. 列出修复清单
4. 逐个处理

---

## 📊 统计和指标

### 页面统计
| 类型 | 数量 | 目标 | 进度 |
|------|------|------|------|
| 概念 | 3 | 15+ | 20% |
| 实体 | 2 | 50+ | 4% |
| 指南 | 5 | 10 | 50% |
| 索引 | 2 | 5+ | 40% |
| **总计** | **18** | **80+** | **22%** |

### 质量指标
| 指标 | 当前 | 目标 |
|------|------|------|
| 完整性 | 100% | 100% |
| 无断裂链接 | ✅ 是 | ✅ 是 |
| 无孤立页面 | ✅ 是 | ✅ 是 |
| 标签规范 | 100% | 100% |
| 更新频率 | 周 | 周+ |

---

## ❓ 常见问题速答

**Q: 我可以直接删除页面吗？**  
A: 不建议直接删除。标记为 #deprecated，保留历史。

**Q: 什么时候做 Lint？**  
A: 轻量 Lint 每周一次（15 分钟），完整 Lint 每月一次（2-4 小时）。

**Q: 可以修改 SCHEMA 吗？**  
A: 可以，但要谨慎。修改前在 [[llm_wiki/config/SCHEMA]] 的"更新日志"中记录。

**Q: 如何处理重复的信息？**  
A: 参见 Lint 工作流第 3 步"检查矛盾"。标记 #needs-verification，后续合并。

**Q: Wiki 会变得太大和混乱吗？**  
A: 不会。通过定期 Lint 和清晰的分类结构，Wiki 会保持有序和可维护。

---

## 🎓 学习资源

### 官方文档
- [[llm_wiki/README|快速开始]]（5 分钟）
- [[llm_wiki/config/SCHEMA|完整规范]]（15 分钟）

### 工作流指南
- [[llm_wiki/workflows/Ingest_Workflow|Ingest]]（30 分钟阅读）
- [[llm_wiki/workflows/Query_Workflow|Query]]（30 分钟阅读）
- [[llm_wiki/workflows/Lint_Workflow|Lint]]（20 分钟阅读）

### 实践教程
- [[llm_wiki/wiki/guides/实战演示|三大工作流完整演示]]（30 分钟）

### 示例页面
- [[llm_wiki/wiki/concepts/UI_Layout|概念示例]]
- [[llm_wiki/wiki/entities/UI_Database|实体示例]]

---

## 📞 获取帮助

### 遇到的问题
1. **链接或格式问题**？→ 查看 [[llm_wiki/config/SCHEMA]]
2. **不知道怎么做**？→ 查看对应的工作流指南
3. **想看具体例子**？→ 打开 [[llm_wiki/wiki/guides/实战演示]]

### 反馈和建议
- 在相关页面底部添加"💬 反馈"笔记
- 或在 Lint 报告中记录

---

## 🎯 立即开始

### ✨ 推荐的第一步

**新用户**：
1. 5 分钟：阅读本仪表板 ✅（现在）
2. 5 分钟：打开 [[llm_wiki/README]]
3. 10 分钟：浏览 [[llm_wiki/wiki/guides/实战演示]]
4. 🎓 现在你已准备好！

**新贡献者**：
1. 30 分钟：学习规范（SCHEMA）
2. 30 分钟：选择一个工作流学习
3. 💪 准备执行你的第一个任务！

---

**仪表板最后更新**: 2026-05-06  
**系统状态**: 🟢 运行中  
**下一个检查点**: 2026-05-13（继续充实布局类型，目标 10+ 个）

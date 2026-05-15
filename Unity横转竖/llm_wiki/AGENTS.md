---
type: meta
created: 2026-05-09
updated: 2026-05-09
tags: [meta, agents, entry-point]
---

# AGENTS.md — AI 助手入口

这是 LLM Wiki 的入口引导文件。AI 助手首次访问时，应先阅读此文件了解 Wiki 结构、工作流和触发关键词。

---

## 📂 Vault 路径

```
D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\
```

## 🏗️ 三层架构

```
Raw Sources（原始数据）
   ↓ Ingest
Wiki（知识库页面）
   ↓ Query
Schema（结构化规范）
```

## 📁 目录结构

```
llm_wiki/
├── wiki/
│   ├── concepts/          # 概念定义（UI_Layout, 组件类型等）
│   │   ├── layout-types/  # 63 种布局类型
│   │   └── layout-groups/ # 15 个布局分组
│   ├── entities/          # UI 实体页面（910 个 UI）
│   ├── guides/            # 操作指南
│   └── indexes/           # 导航索引
│       ├── Index_All_UIs        # 全部 910 个 UI 索引
│       ├── Index_Layout_Types   # 63 种布局类型索引
│       └── Index_Layout_Groups  # 15 个布局分组索引
├── sources/               # 原始数据索引（Immutable）
│   ├── all_ui_features.json.md
│   ├── ui_layout_analysis.json.md
│   └── ui_list.json.md
├── workflows/             # 三大工作流
│   ├── Ingest_Workflow.md
│   ├── Query_Workflow.md
│   └── Lint_Workflow.md
├── scripts/              # Lint 自动化脚本
│   ├── find_broken_links.ps1
│   ├── find_orphan_pages.ps1
│   └── lint_report.ps1
└── qa/
    └── lint_reports/      # 健康报告输出目录
```

## 🔑 核心触发词

### Ingest（消化新数据）
触发条件：发现新的 UI 数据、布局分析报告、组件统计
```
请 Ingest 这个新数据 → 执行 Ingest 工作流
```
步骤：Read → Map → Create/Update → Cross-reference → Validate

### Query（查询知识库）
触发条件：用户提问、需要查找 UI、分析布局模式
```
帮我查一下哪些 UI 使用了 XXX 布局
这个 UI 属于什么布局类型？
```
步骤：Understand → Search → Synthesize → Answer → Update Wiki

### Lint（健康检查）
触发条件：定期检查、修改页面后验证
```
跑一下 Lint 检查
```
运行：`llm_wiki\scripts\lint_report.ps1`

## 🔗 常用链接

| 需要找 | 去哪里 |
|--------|--------|
| 某个 UI 实体 | [[llm_wiki/wiki/indexes/Index_All_UIs]] |
| 按布局类型查 UI | [[llm_wiki/wiki/indexes/Index_Layout_Types]] |
| 某个布局类型定义 | [[llm_wiki/wiki/concepts/layout-types/xxx]] |
| UI 数据库总览 | [[llm_wiki/wiki/entities/UI_Database]] |
| 原始数据 | [[llm_wiki/sources]] |

## 📋 数据规模

- **UI 实体**: 910 个
- **布局类型**: 63 种
- **布局分组**: 15 个
- **原始数据**: 5 个 JSON 文件（总计 ~6.5MB）

## ⚠️ 规范

- Sources 目录下的文件是**不可变**的，只读不修改
- Wiki 页面修改后运行 `lint_report.ps1` 验证
- 每次 Query 完成后在 `qa/execution_logs/` 记录执行摘要
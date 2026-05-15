---
type: guide
status: published
created: 2026-05-06
updated: 2026-05-06
tags: [guide, automation, qa, setup]
related: [[llm_wiki/wiki/qa/UI_Classification_Daily_Check]], [[llm_wiki/wiki/qa/UI_Classification_Issues]]
---

# UI 分类一致性自动检查系统 — 设置指南

## 概述

**UI 分类一致性自动检查系统**是一个完全自动化的 Wiki 质量保证机制，每 3 分钟执行一次：

1. 随机选择一张 UI 图片
2. 分析其布局类型
3. 查询已有的分类记录
4. 对比结果并记录问题
5. 自动同步到 llm_wiki

---

## 系统架构

```
┌─────────────────────────────────────────────────────┐
│          openCLaw 定时任务系统                       │
│  (C:\Users\guowe\.openclaw\cron\jobs.json)           │
└────────────────┬────────────────────────────────────┘
                 │
                 ├─ 每 3 分钟触发事件
                 │
                 ↓
┌─────────────────────────────────────────────────────┐
│        Claude Code 会话                             │
│  接收 "UIClassificationVerify" 系统事件              │
└────────────────┬────────────────────────────────────┘
                 │
                 ├─ 执行 /clear（清理上下文）
                 ├─ 选择随机 UI 图片
                 ├─ 分析图片并判断类型
                 ├─ 查询 llm_wiki 中的分类
                 ├─ 对比结果
                 └─ 记录和同步到 Wiki
                 │
                 ↓
┌─────────────────────────────────────────────────────┐
│          llm_wiki 更新                              │
│  llm_wiki/wiki/qa/UI_Classification_Daily_Check.md  │
│  llm_wiki/wiki/qa/UI_Classification_Issues.md       │
└─────────────────────────────────────────────────────┘
```

---

## 已安装的文件

### 1. PowerShell 脚本
**文件**: `C:\Users\guowe\.openclaw\workspace-code\ui_classification_verify.ps1`

**功能**:
- 获取随机 UI 图片
- 查询已有分类
- 生成检查报告
- 记录日志

**权限**: 已配置

---

### 2. openCLaw 定时任务配置
**文件**: `C:\Users\guowe\.openclaw\cron\jobs.json`

**配置内容**:
```json
{
  "id": "ui-classification-verify-3min",
  "agentId": "code",
  "name": "UI分类一致性检查-定时任务",
  "schedule": {
    "kind": "every",
    "everyMs": 180000  // 每 3 分钟 = 180000 毫秒
  },
  "payload": {
    "kind": "systemEvent",
    "text": "UIClassificationVerify"
  },
  "enabled": true
}
```

**状态**: ✅ 已启用

---

### 3. Claude 处理指令
**文件**: `D:\obsidianProject\portrait-to-landscape\Unity横转竖\.claude\instructions\ui-classification-verify.md`

**功能**: 定义 Claude 的处理流程和输出格式

**包含内容**:
- 详细的 6 步处理流程
- 输出格式模板
- 问题识别标准
- 数据同步规则

---

### 4. Wiki QA 页面
**文件**: `llm_wiki/wiki/qa/UI_Classification_Daily_Check.md`

**功能**: 记录所有检查结果的汇总

**内容**:
- 检查统计信息
- 已检查 UI 列表
- 问题修复跟踪
- 系统配置说明

---

### 5. 问题记录页面
**文件**: `llm_wiki/wiki/qa/UI_Classification_Issues.md`

**功能**: 记录发现的具体问题

**内容**:
- 待处理问题
- 已修复问题
- 问题管理流程

---

### 6. 工作流定义（可选）
**文件**: `D:\obsidianProject\portrait-to-landscape\Unity横转竖\.claude\workflows\ui-classification-verify.yml`

**功能**: 定义完整的检查工作流（高级用法）

---

## 工作流程详解

### 第 1 分钟：任务触发

```
openCLaw 定时器触发
  ↓
发送系统事件："UIClassificationVerify"
  ↓
Claude Code 接收事件
```

### 第 2-3 分钟：检查执行

```
1. /clear                      (清理上下文)
   ↓
2. 选择随机 UI 图片
   - 扫描 UIImage 目录
   - 列出所有 UI_*.png
   - 随机选择一张
   ↓
3. 分析图片
   - 阅读图片内容
   - 根据特征判断类型
   - 记录置信度
   ↓
4. 查询分类
   - 在 llm_wiki 搜索
   - 提取已有分类
   - 记录查询结果
   ↓
5. 对比结果
   - 判断一致性
   - 分析差异原因
   - 生成结论
   ↓
6. 记录和同步
   - 更新 Daily Check 页面
   - 如有问题，更新 Issues 页面
   - 完成检查
```

---

## 配置参数

### 时间相关

| 参数 | 值 | 说明 |
|------|-----|------|
| 检查频率 | 3 分钟 | 时间间隔（可调整） |
| 超时时间 | 2 分钟 | 单次检查最长耗时 |
| 并发数 | 1 | 同时运行的检查数 |

### 路径相关

| 参数 | 值 | 说明 |
|------|-----|------|
| 图片源 | D:\CursorProject\Dadian - 副本\Arts\Assets\Doc\UIImage\ | UI 图片目录 |
| Wiki 路径 | D:\obsidianProject\portrait-to-landscape\Unity横转竖\ | Vault 根目录 |
| 分类数据库 | llm_wiki/wiki/entities/ | 已分类 UI 的存储位置 |
| QA 记录 | llm_wiki/wiki/qa/ | 检查结果的存储位置 |
| 日志位置 | .claude/cron_logs/ | 执行日志 |

### 检查相关

| 参数 | 值 | 说明 |
|------|-----|------|
| 选择方式 | 随机 | 每次随机选择（避免偏差） |
| 一致标准 | 完全或同大类 | 判断标准 |
| 问题级别 | 高/中/低 | 优先级分类 |

---

## 如何使用

### 查看检查结果

1. **最新检查日志**
   ```
   打开：llm_wiki/wiki/qa/UI_Classification_Daily_Check.md
   查看：已检查的 UI 列表和统计信息
   ```

2. **问题清单**
   ```
   打开：llm_wiki/wiki/qa/UI_Classification_Issues.md
   查看：待处理和已修复的问题
   ```

### 手动触发检查

```bash
# 在 openCLaw 中手动运行一次检查
# 可以通过 openCLaw CLI 或 API 手动触发
```

### 修改检查频率

**从 3 分钟改为 5 分钟**：

1. 编辑 `C:\Users\guowe\.openclaw\cron\jobs.json`
2. 找到 `"ui-classification-verify-3min"` 任务
3. 修改 `"everyMs": 180000` → `"everyMs": 300000`
4. 保存文件
5. openCLaw 会自动重新加载配置

### 禁用或启用

**禁用检查**：
```json
"enabled": false
```

**启用检查**：
```json
"enabled": true
```

---

## 输出示例

### 日志消息格式

```
💡 [2026-05-06 09:15:23] === UI Classification Verification Task Started ===

📸 [2026-05-06 09:15:24] Selected image: UI_GachaCoinShop.png

🔍 [2026-05-06 09:15:25] Processing: UI_GachaCoinShop

✅ [2026-05-06 09:15:26] Existing classification found: Four-border + Left-Right List

📊 [2026-05-06 09:15:27] UI analysis queued for Claude processing

✔️ [2026-05-06 09:15:30] === UI Classification Verification Task Completed ===
```

### Wiki 更新示例

**Daily Check 页面**中的表格行：
```
| 2026-05-06 09:15:27 | UI_GachaCoinShop | 四边木栏+左右-宽列表 | 四边木栏+左右-宽列表 | ✅ 通过 | 完全一致 |
```

**Issues 页面**（如果发现问题）：
```
### ⚠️ 2026-05-06 09:15:27 - UI_SomeName

| 项目 | 内容 |
|------|------|
| UI 名称 | UI_SomeName |
| 分析结果 | 四边木栏+左中右 |
| 已有分类 | 弹框类 |
| 问题类型 | 分类错误 |
| 问题描述 | 分析结果与已有分类完全不同，需要人工验证 |
| 建议处理 | 检查 UI_SomeName.png 图片，确认正确分类 |
| 发现时间 | 2026-05-06 09:15:27 |
```

---

## 故障排除

### 问题 1：定时任务未执行

**症状**: 3 分钟过去了，但未见检查日志

**检查步骤**:
1. 确认 openCLaw 正在运行
2. 检查 jobs.json 配置是否正确
3. 查看 openCLaw 的控制台输出
4. 确认 Claude Code 会话是活跃的

### 问题 2：图片目录不存在或为空

**症状**: 日志显示"No UI_*.png files found"

**解决方案**:
1. 检查路径是否正确
2. 确保目录中有 UI_*.png 文件
3. 检查文件权限

### 问题 3：分析结果不准确

**症状**: 频繁出现明显的误判

**改进措施**:
1. 检查图片质量（是否清晰）
2. 改进识别指南
3. 调整 Claude 的提示词
4. 手动标记几个参考案例

### 问题 4：Wiki 同步失败

**症状**: 日志显示更新成功，但 Wiki 无变化

**检查步骤**:
1. 确认文件写入权限
2. 检查文件格式是否正确（YAML frontmatter）
3. 验证文件路径
4. 查看 Obsidian 是否需要刷新

---

## 后续改进

### 短期（1 周内）

- [ ] 观察首次运行结果
- [ ] 调整识别准确度
- [ ] 改进问题记录格式

### 中期（2-4 周）

- [ ] 建立问题分类标准
- [ ] 创建自动修复规则
- [ ] 生成周报告

### 长期（1 个月+）

- [ ] 统计分类准确率
- [ ] 识别系统性问题
- [ ] 优化分类体系

---

## 常见问题 (FAQ)

**Q: 为什么选择 3 分钟的频率？**

A: 平衡检查覆盖度和系统负担。3 分钟可以在一天内完成 480 次检查，覆盖大部分 UI 样本，同时不会对系统造成压力。

**Q: 如果检查发现问题，谁负责修复？**

A: 系统自动记录问题，但修复需要人工判断。问题被标记到 Issues 页面，可以由团队成员逐个处理。

**Q: 可以同时运行多个检查吗？**

A: 目前配置为单个任务顺序执行，避免并发问题。如需并行，需要修改配置。

**Q: 检查结果会覆盖已有分类吗？**

A: 不会。系统只记录和对比，不修改已有分类。任何修改都需要人工确认。

---

## 支持和反馈

如遇问题或有改进建议，请：

1. 查看本指南的"故障排除"部分
2. 检查 llm_wiki 的相关页面
3. 查看执行日志：`.claude/cron_logs/ui_classification_check.log`

---

**系统启动时间**: 2026-05-06 08:30  
**首次检查**: 等待中  
**状态**: ✅ 已配置，已启用，等待首次运行

**下一步**: 观察首次检查结果，根据需要调整参数

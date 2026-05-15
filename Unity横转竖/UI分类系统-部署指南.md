---
type: system-guide
created: 2026-05-06
updated: 2026-05-06
tags: [system, deployment, ui-classification]
---

# UI 分类系统 - 部署指南

## 🎯 系统目标

每 3 分钟自动执行一次 UI 分类检查：
1. 随机选择一张 UI 截图
2. 用 Claude Vision API 分析其布局类型
3. 对比 Wiki 中的真实分类
4. 记录结果到日志文件

## 📋 系统状态

| 项目 | 状态 | 说明 |
|------|------|------|
| 主分析脚本 | ✅ | `ui-classification-with-claude.ps1` |
| 密钥配置脚本 | ✅ | `setup-api-from-cursor-permanent.ps1` |
| Task Scheduler 任务 | ✅ | `UIClassificationCheck` 已配置 |
| API 密钥环境变量 | ❌ | 需要配置 |
| 系统运行状态 | ⏳ | 等待 API 密钥 |

## 🚀 快速启动（3个步骤）

### 第 1 步：配置 API 密钥

打开 PowerShell（**管理员模式**），执行：

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\guowe\.openclaw\scripts\setup-api-from-cursor-permanent.ps1"
```

**脚本功能：**
- ✓ 从 Cursor 的设置中自动提取 Claude API 密钥
- ✓ 设置为系统用户级环境变量 `CLAUDE_API_KEY`
- ✓ 验证配置成功
- ✓ 显示日志位置

### 第 2 步：重启 PowerShell

关闭所有 PowerShell 窗口，重新打开 PowerShell（或重启系统）

**验证：**
```powershell
echo $env:CLAUDE_API_KEY
# 应该显示：sk-ant-xxxxx...（密钥的前缀）
```

### 第 3 步：等待自动执行

Task Scheduler 会在下一个 3 分钟周期自动运行任务。

**验证执行：**
- 查看系统日志：`C:\Users\guowe\.openclaw\logs\ui-classification-results.log`
- 查看每日日志：`llm_wiki/wiki/qa/execution_logs/2026-05-06.md`

## 📊 系统架构

```
Task Scheduler (每 3 分钟)
    ↓
ui-classification-with-claude.ps1
    ├─ 选择随机 UI 图片
    │   └─ D:\CursorProject\Dadian - 副本\Arts\Assets\Doc\UIImage\
    │
    ├─ 转换为 Base64 编码
    │
    ├─ 调用 Claude Vision API
    │   └─ 分析 UI 布局结构
    │   └─ 返回中文分类类型
    │
    ├─ 搜索 Wiki 分类
    │   └─ llm_wiki/wiki/concepts/layout-types/
    │
    ├─ 对比结果
    │   ├─ ✅ 一致
    │   ├─ ⚠️ 不一致
    │   └─ ❌ 未分类
    │
    └─ 记录到日志
        ├─ 系统日志: C:\Users\guowe\.openclaw\logs\
        └─ 每日日志: llm_wiki/wiki/qa/execution_logs/YYYY-MM-DD.md
```

## 📁 关键文件

### 脚本
| 文件 | 位置 | 作用 |
|------|------|------|
| `setup-api-from-cursor-permanent.ps1` | `C:\Users\guowe\.openclaw\scripts\` | 配置 API 密钥 |
| `ui-classification-with-claude.ps1` | `C:\Users\guowe\.openclaw\scripts\` | 主执行脚本 |

### 日志
| 文件 | 位置 | 内容 |
|------|------|------|
| 系统日志 | `C:\Users\guowe\.openclaw\logs\ui-classification-results.log` | 执行详情和错误 |
| 每日日志 | `llm_wiki/wiki/qa/execution_logs/YYYY-MM-DD.md` | 分类结果表格 |

### 配置
| 项目 | 值 |
|------|-----|
| Task Scheduler 任务名 | `UIClassificationCheck` |
| 执行间隔 | 每 3 分钟 |
| 执行脚本 | `ui-classification-with-claude.ps1` |

## 🔍 日志格式

### 系统日志示例
```
[2026-05-06 10:37:48] [INFO] 开始 UI 分类检查
[2026-05-06 10:37:48] [INFO] 选中UI: UI_RoleObtainingTitleTips
[2026-05-06 10:37:49] [SUCCESS] Claude API 调用成功
[2026-05-06 10:37:49] [INFO] 初判类型: T型-上标题-左-右
[2026-05-06 10:37:49] [INFO] 在Wiki中找到分类: T型-上标题-左-右
[2026-05-06 10:37:49] [SUCCESS] 记录已追加到日志
```

### 每日日志格式
```markdown
| 时间 | UI名称 | 初判类型 | 实际类型 | 结果 | 备注 |
|------|--------|--------|----------|------|------|
| 10:37:48 | UI_RoleObtainingTitleTips | T型-上标题-左-右 | T型-上标题-左-右 | ✅ | 分类一致 |
| 10:40:47 | UI_GuildWarAppoint | 上标题+下横列表 | 上标题-中竖列表-下信息 | ⚠️ | 分类不一致，需确认 |
```

## ❌ 故障排除

### 问题：脚本执行失败

**检查清单：**
1. API 密钥是否已设置？
   ```powershell
   echo $env:CLAUDE_API_KEY
   # 应该返回密钥，不是空白
   ```

2. PowerShell 是否已重启？
   - 关闭并重新打开 PowerShell
   - 或重启系统

3. Cursor 设置中是否有 API 密钥？
   - 打开 Cursor → Settings
   - 搜索 "Claude" 或 "CLAUDE_API_KEY"
   - 确认已配置

### 问题：Task Scheduler 任务不运行

```powershell
# 检查任务状态
Get-ScheduledTask -TaskName "UIClassificationCheck" | Select-Object State, Enabled

# 查看任务历史
Get-ScheduledTaskInfo -TaskName "UIClassificationCheck"

# 手动触发任务（测试）
Start-ScheduledTask -TaskName "UIClassificationCheck"
```

### 问题：日志文件乱码

这通常表示编码问题。系统会自动修复，但如果问题持续：
1. 删除日志文件
2. 重新运行脚本
3. 脚本会创建新的 UTF-8 编码日志

## 📈 性能指标

| 指标 | 值 |
|------|-----|
| 执行频率 | 每 3 分钟（20 次/小时） |
| 单次执行时间 | 约 10-15 秒 |
| 日志增长 | 约 20-30 KB/天 |
| 平均 Token 使用 | 约 1.5K/call |
| 月度 Token 量 | 约 900K tokens |

## ✨ 成功标志

系统正常运行的迹象：
- [ ] `CLAUDE_API_KEY` 已设置为系统环境变量
- [ ] 日志文件每 3 分钟更新一次
- [ ] 记录包含中文的 UI 类型分类
- [ ] 结果显示 ✅/⚠️/❌ 之一
- [ ] 没有 "环境变量未设置" 的错误
- [ ] Task Scheduler 显示任务已运行

## 🆘 获取帮助

**系统日志：** `C:\Users\guowe\.openclaw\logs\ui-classification-results.log`

**API 状态：** https://console.anthropic.com/status

**常见错误代码：**
- Exit 1: CLAUDE_API_KEY 未设置
- Exit 1: UI 图片目录不存在或为空
- Exit 1: Claude API 调用失败

## 📞 相关文档

- [[QUICK-REFERENCE.md]] - 快速参考指南
- [[IMPLEMENTATION-SUMMARY.md]] - 系统实现总结
- [[README-UI-Classification.md]] - 架构说明

---

**最后更新：** 2026-05-06 10:37
**系统版本：** 1.2
**状态：** ⏳ 等待 API 密钥配置

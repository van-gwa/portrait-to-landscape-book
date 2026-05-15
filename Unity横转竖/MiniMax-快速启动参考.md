---
type: quick-reference
created: 2026-05-06
updated: 2026-05-06
tags: [minimax, quick-start]
---

# MiniMax 快速启动参考

## 🎯 一句话总结

用你提供的 MiniMax 参数替换 Claude，启动自动化 UI 分类系统。

## ⚡ 快速命令

### 1️⃣ 配置 MiniMax API 密钥

```powershell
# PowerShell 管理员权限运行
powershell -ExecutionPolicy Bypass -File "C:\Users\guowe\.openclaw\scripts\setup-minimax-api.ps1"
```

### 2️⃣ 重启 PowerShell 激活环境变量

```powershell
# 关闭并重新打开 PowerShell

# 验证环境变量
echo $env:MINIMAX_API_KEY
# 输出应该是：sk-cp-xxx...
```

### 3️⃣ 更新 Task Scheduler（使用 MiniMax）

```powershell
$newAction = New-ScheduledTaskAction -Execute "powershell.exe" `
  -Argument '-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\Users\guowe\.openclaw\scripts\ui-classification-with-minimax.ps1"'

Set-ScheduledTask -TaskName "UIClassificationCheck" -Action $newAction

Write-Host "✅ Task Scheduler 已更新为 MiniMax"
```

## 📋 MiniMax 参数配置

| 参数 | 值 |
|------|-----|
| Base URL | `https://api.minimaxi.com/v1` |
| Model | `MiniMax-M2.7` |
| API Key | `sk-cp-hs_EcrRDXFh8...` |
| 认证方式 | `Bearer Token` |

## 🔧 脚本说明

### 主脚本：ui-classification-with-minimax.ps1
- 自动化 UI 分类
- 每 3 分钟执行一次（由 Task Scheduler 调用）
- 内置 MiniMax API 调用
- 支持中文分类类型

### 配置脚本：setup-minimax-api.ps1
- 交互式输入 API 密钥
- 设置系统环境变量 `MINIMAX_API_KEY`
- 验证配置成功

## 📊 日志位置

| 日志 | 位置 |
|------|------|
| 系统日志 | `C:\Users\guowe\.openclaw\logs\ui-classification-results.log` |
| 每日日志 | `llm_wiki/wiki/qa/execution_logs/YYYY-MM-DD.md` |
| 配置日志 | `C:\Users\guowe\.openclaw\logs\minimax-setup.log` |

## ✅ 验证成功

运行成功的标志：

```
日志中出现：
✓ [SUCCESS] MiniMax API 调用成功
✓ [INFO] 初判类型: T型-上标题-左-右  （中文）
✓ [SUCCESS] 记录已追加到日志
✓ 每 3 分钟自动新增一条记录
```

## 🔄 切换回其他 LLM

### 改回 Claude
```powershell
$newAction = New-ScheduledTaskAction -Execute "powershell.exe" `
  -Argument '-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\Users\guowe\.openclaw\scripts\ui-classification-with-claude.ps1"'
  
Set-ScheduledTask -TaskName "UIClassificationCheck" -Action $newAction
```

### 改为 OpenAI
```powershell
$newAction = New-ScheduledTaskAction -Execute "powershell.exe" `
  -Argument '-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\Users\guowe\.openclaw\scripts\ui-classification-with-openai.ps1"'
  
Set-ScheduledTask -TaskName "UIClassificationCheck" -Action $newAction
```

## 📝 可选配置

### 改为 MiniMax 高速版本

编辑 `ui-classification-with-minimax.ps1`：

```powershell
# 找到这一行：
$MiniMaxModel = "MiniMax-M2.7"

# 改为：
$MiniMaxModel = "MiniMax-M2.7-highspeed"
```

## 📚 详细文档

- [[MiniMax-Vision-API-集成指南.md]] - 完整集成指南
- [[LLM-完整对比分析.md]] - LLM 对比分析
- [[UI分类系统-部署指南.md]] - 系统部署指南

## ⏰ 时间线

```
现在：
  ↓
运行配置脚本（1-2 分钟）
  ↓
重启 PowerShell（1 分钟）
  ↓
更新 Task Scheduler（1-2 分钟）
  ↓
系统启动！每 3 分钟自动执行
```

**总耗时：5-10 分钟**

## 🆘 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| "MINIMAX_API_KEY 未设置" | 环境变量未激活 | 重启 PowerShell |
| "API 调用失败：401" | API 密钥无效 | 重新运行配置脚本 |
| "无权限执行脚本" | 缺少管理员权限 | 用管理员权限运行 |

## 📞 需要帮助？

1. 查看系统日志：`C:\Users\guowe\.openclaw\logs\ui-classification-results.log`
2. 查看配置日志：`C:\Users\guowe\.openclaw\logs\minimax-setup.log`
3. 查看完整文档：[[MiniMax-Vision-API-集成指南.md]]

---

**状态：✅ 就绪，等待启动**

**下一步：运行配置脚本**

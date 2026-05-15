---
type: guide
created: 2026-05-06
updated: 2026-05-06
tags: [system, minimax, api, integration]
---

# MiniMax Vision API 集成指南

## 🎯 MiniMax 介绍

**MiniMax** 是中国领先的 AI 公司，提供高性能 Vision API。

### 主要特点
- ✅ 支持图像理解和分析
- ✅ 支持中文 prompt
- ✅ API 响应速度快
- ✅ 成本相对合理
- ✅ 国内访问稳定

## 📋 MiniMax 配置信息

| 项目 | 值 |
|------|-----|
| **Base URL** | `https://api.minimaxi.com/v1` |
| **模型** | `MiniMax-M2.7` 或 `MiniMax-M2.7-highspeed` |
| **API 密钥格式** | `sk-cp-xxx...` |
| **端点** | `/messages` |
| **认证方式** | Bearer Token |

### 获取 API 密钥
访问：https://console.minimaxi.com/

## 🚀 快速启动（3步）

### 第 1 步：配置 API 密钥

打开 PowerShell（**管理员权限**），执行：

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\guowe\.openclaw\scripts\setup-minimax-api.ps1"
```

脚本会：
- 请求输入你的 MiniMax API 密钥
- 设置为系统环境变量 `MINIMAX_API_KEY`
- 验证配置成功

### 第 2 步：重启 PowerShell

- 关闭当前 PowerShell 窗口
- 打开新的 PowerShell 窗口
- 验证环境变量：
  ```powershell
  echo $env:MINIMAX_API_KEY
  # 应该显示：sk-cp-xxx...
  ```

### 第 3 步：更新 Task Scheduler

修改现有任务执行脚本：

```powershell
# 获取任务
$task = Get-ScheduledTask -TaskName "UIClassificationCheck"

# 获取现有操作
$action = $task.Actions[0]

# 更改脚本路径
$newAction = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument '-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\Users\guowe\.openclaw\scripts\ui-classification-with-minimax.ps1"'

# 更新任务
Set-ScheduledTask -TaskName "UIClassificationCheck" -Action $newAction

Write-Host "✅ Task Scheduler 已更新为 MiniMax 版本"
```

或者用 Task Scheduler GUI：
1. 打开 Task Scheduler
2. 找到 `UIClassificationCheck` 任务
3. 编辑 → 操作
4. 改 PowerShell 参数中的脚本路径

## 📊 MiniMax API 详细说明

### API 端点

```
POST https://api.minimaxi.com/v1/messages
```

### 请求格式

```json
{
  "model": "MiniMax-M2.7",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "image",
          "image": "data:image/png;base64,xxx..."
        },
        {
          "type": "text",
          "text": "请分析这个UI..."
        }
      ]
    }
  ],
  "stream": false,
  "max_tokens": 1024
}
```

### 响应格式

MiniMax API 返回格式：

```json
{
  "reply": [
    {
      "content": "Claude分析的结果..."
    }
  ]
}
```

或兼容 OpenAI 格式：

```json
{
  "choices": [
    {
      "message": {
        "content": "分类结果..."
      }
    }
  ]
}
```

### 认证方式

```
Authorization: Bearer sk-cp-xxx...
```

## 🔧 脚本说明

### ui-classification-with-minimax.ps1

**主执行脚本，功能：**
- 读取随机 UI 图片
- 将图片转换为 Base64
- 调用 MiniMax Vision API
- 分析 UI 布局类型
- 搜索 Wiki 中的实际分类
- 对比并记录结果

**关键配置：**
```powershell
$MiniMaxBaseUrl = "https://api.minimaxi.com/v1"
$MiniMaxModel = "MiniMax-M2.7"
```

**可改为高速版：**
```powershell
$MiniMaxModel = "MiniMax-M2.7-highspeed"
```

### setup-minimax-api.ps1

**配置脚本，功能：**
- 交互式输入 API 密钥
- 验证密钥格式
- 设置系统环境变量
- 当前会话激活

## ⚙️ 模型选择

### MiniMax-M2.7（标准）
- 更准确
- 更好的中文理解
- 稍慢（1-2秒）
- 推荐用于精确分类

### MiniMax-M2.7-highspeed（高速）
- 更快（500ms-1s）
- 略低的准确度
- 适合实时应用
- 如果对响应时间敏感可用

**建议：** 使用标准版本 `MiniMax-M2.7`

## 📈 成本估计

基于每月 480 次执行（每 3 分钟一次）：

```
平均 token 消耗：1.5K tokens/call
月度总消耗：720K tokens/月

MiniMax 定价（需查询最新价格）：
  输入：$ 约 0.002-0.005/1K tokens
  输出：$ 约 0.004-0.01/1K tokens
  
月度成本估计：$15-40/月（国内最优）
```

## ✅ 成功验证

脚本正常运行时：

- [ ] 日志文件每 3 分钟更新一次
- [ ] 包含中文的 UI 分类类型
- [ ] 结果显示 ✅/⚠️/❌ 之一
- [ ] 没有 "环境变量未设置" 错误
- [ ] 日志中显示 "MiniMax API 调用成功"

## ❌ 常见问题

### 问题：API 调用失败，显示 401

**原因：** API 密钥无效或过期

**解决方案：**
1. 检查 API 密钥是否正确
2. 检查是否有权限使用 Vision API
3. 重新获取新的 API 密钥
4. 重新运行 `setup-minimax-api.ps1`

### 问题：返回格式异常

**原因：** MiniMax API 响应格式可能有变化

**解决方案：**
1. 查看日志中的完整响应
2. 检查 MiniMax 官方文档是否有更新
3. 可能需要调整脚本的响应解析部分

### 问题：Task Scheduler 更新失败

**解决方案：** 使用 GUI 更新
1. 打开 Task Scheduler（开始菜单搜索）
2. 找到 `UIClassificationCheck` 任务
3. 右键 → 编辑
4. 点击 "操作" 标签页
5. 编辑现有操作
6. 修改参数中的脚本路径

## 📋 切换回其他 LLM

如果需要切换回 Claude 或 OpenAI：

```powershell
# 恢复 Claude
Set-ScheduledTask -TaskName "UIClassificationCheck" `
  -Action (New-ScheduledTaskAction -Execute "powershell.exe" `
  -Argument '-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\Users\guowe\.openclaw\scripts\ui-classification-with-claude.ps1"')

# 恢复 OpenAI
Set-ScheduledTask -TaskName "UIClassificationCheck" `
  -Action (New-ScheduledTaskAction -Execute "powershell.exe" `
  -Argument '-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\Users\guowe\.openclaw\scripts\ui-classification-with-openai.ps1"')
```

## 📚 相关文档

- [[LLM-完整对比分析.md]] - LLM 成本和能力对比
- [[LLM-API-切换指南.md]] - 其他 LLM 的切换方案
- [[UI分类系统-部署指南.md]] - 完整系统部署指南

## 🔗 链接

- [MiniMax 官方网站](https://www.minimaxi.com/)
- [MiniMax 控制台](https://console.minimaxi.com/)
- [MiniMax API 文档](https://docs.minimaxi.com/)

---

**当前配置：** MiniMax-M2.7

**下一步：** 运行配置脚本，系统即可自动运行

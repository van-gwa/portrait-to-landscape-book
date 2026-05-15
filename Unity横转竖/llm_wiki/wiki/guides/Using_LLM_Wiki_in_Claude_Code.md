---
type: guide
created: 2026-05-06
updated: 2026-05-06
tags: [guide, llm-wiki, setup, windows, claude-code]
related: [[llm_wiki/README]], [[llm_wiki/DASHBOARD]]
---

# LLM Wiki - Windows PowerShell 和 Claude Code 使用指南

**目的**：教你如何在 Windows PowerShell 中访问和使用 llm_wiki 的所有资源

**适用场景**：
- 在 Claude Code 中读取 Wiki 内容
- 用 PowerShell 搜索和分析 Wiki
- 集成 Wiki 知识到其他工具中

---

## 📍 LLM Wiki 的位置

### 完整路径（Windows）

```powershell
D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki
```

### 相对于 Vault 根目录

```
llm_wiki/
├── config/
├── sources/
├── wiki/
├── workflows/
└── [各个顶级页面]
```

### 快速导航表

| 内容 | 路径 | 用途 |
|-----|------|------|
| 快速开始 | `llm_wiki/README.md` | 入门指南 |
| 仪表板 | `llm_wiki/DASHBOARD.md` | 导航和状态 |
| Wiki规范 | `llm_wiki/config/SCHEMA.md` | 规范定义 |
| 快速判断 | `llm_wiki/wiki/guides/UI_Layout_Quick_Judge.md` | 日常工具 |
| 完整指南 | `llm_wiki/wiki/guides/UI_Layout_Classification_Guide.md` | 深入学习 |
| 错误分析 | `llm_wiki/wiki/guides/Avoiding_Classification_Mistakes.md` | 学习错误 |
| 62个类型 | `llm_wiki/wiki/concepts/layout-types/` | 具体类型 |
| 15个分组 | `llm_wiki/wiki/concepts/layout-groups/` | 类型分组 |

---

## 💻 方式1：在 PowerShell 中使用

### 1.1 设置 Wiki 根路径

```powershell
# 方式A：使用完整路径变量
$wikiRoot = "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki"

# 方式B：从当前位置计算相对路径（假设你在vault根目录）
$wikiRoot = (Get-Location).Path + "\llm_wiki"

# 方式C：使用环境变量（持久化）
[Environment]::SetEnvironmentVariable("LLMWIKI", "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki", "User")
$wikiRoot = $env:LLMWIKI
```

### 1.2 常用 PowerShell 命令

#### 列出所有 Wiki 页面

```powershell
# 列出所有 .md 文件及其路径
Get-ChildItem -Path $wikiRoot -Recurse -Filter "*.md" | 
  Select-Object -Property FullName, Name, LastWriteTime |
  Format-Table -AutoSize

# 统计 Wiki 页面总数
(Get-ChildItem -Path $wikiRoot -Recurse -Filter "*.md").Count
```

#### 读取某个页面内容

```powershell
# 读取单个页面
$content = Get-Content -Path "$wikiRoot\wiki\guides\UI_Layout_Quick_Judge.md" -Encoding UTF8
Write-Output $content

# 读取指定行数（前100行）
$content = Get-Content -Path "$wikiRoot\wiki\guides\UI_Layout_Quick_Judge.md" -Encoding UTF8 -TotalCount 100
$content
```

#### 搜索特定关键词

```powershell
# 搜索包含"布局分类"的所有页面
Get-ChildItem -Path $wikiRoot -Recurse -Filter "*.md" | 
  Where-Object { (Get-Content $_.FullName -Encoding UTF8) -match "布局分类" } |
  Select-Object Name, FullName

# 搜索包含特定词的行
Get-ChildItem -Path $wikiRoot -Recurse -Filter "*.md" -ErrorAction SilentlyContinue |
  ForEach-Object {
    $content = Get-Content $_.FullName -Encoding UTF8
    if ($content -match "T型") {
      Write-Output "文件: $($_.Name)"
      $content | Select-String -Pattern "T型"
    }
  }
```

#### 按类型分类列出

```powershell
# 列出所有指南页面
Get-ChildItem -Path "$wikiRoot\wiki\guides" -Filter "*.md" |
  Select-Object Name

# 列出所有概念页面
Get-ChildItem -Path "$wikiRoot\wiki\concepts" -Recurse -Filter "*.md" |
  Select-Object Name, Directory
```

#### 统计和分析

```powershell
# 统计每个目录下有多少个 .md 文件
Get-ChildItem -Path $wikiRoot -Directory | 
  ForEach-Object {
    $count = (Get-ChildItem -Path $_.FullName -Recurse -Filter "*.md").Count
    [PSCustomObject]@{
      Directory = $_.Name
      FileCount = $count
    }
  } |
  Format-Table -AutoSize

# 找出最大和最小的文件
Get-ChildItem -Path $wikiRoot -Recurse -Filter "*.md" |
  Sort-Object Length -Descending |
  Select-Object -First 5, -Last 5 |
  Select-Object Name, @{Name="Size(KB)"; Expression={[math]::Round($_.Length/1KB, 2)}}
```

---

## 🔧 方式2：在 Claude Code 的工具中使用

### 2.1 在 Read 工具中使用

#### 使用相对路径（推荐）

```
文件路径：llm_wiki/wiki/guides/UI_Layout_Quick_Judge.md
```

Claude Code 会自动根据 vault 根目录解析相对路径。

#### 使用绝对路径

```
文件路径：D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\wiki\guides\UI_Layout_Quick_Judge.md
```

### 2.2 在 Bash 工具中使用

```bash
# 读取文件内容
cat ./llm_wiki/wiki/guides/UI_Layout_Quick_Judge.md

# 查找某个关键词
grep -r "布局分类" ./llm_wiki/wiki/guides/

# 列出所有 markdown 文件
find ./llm_wiki -name "*.md" -type f

# 统计文件数
find ./llm_wiki -name "*.md" | wc -l

# 显示目录树结构
tree ./llm_wiki -L 3
```

### 2.3 在 PowerShell 工具中使用

```powershell
# 定义 wiki 路径
$wikiRoot = "llm_wiki"

# 列出快速判断指南的行数
(Get-Content "$wikiRoot\wiki\guides\UI_Layout_Quick_Judge.md" -Encoding UTF8 | Measure-Object -Line).Lines

# 搜索特定内容
$files = Get-ChildItem -Path $wikiRoot -Recurse -Filter "*.md"
foreach ($file in $files) {
  $content = Get-Content $file.FullName -Encoding UTF8
  if ($content -match "错误") {
    Write-Output "找到: $($file.Name)"
  }
}
```

---

## 📚 方式3：作为知识库引用

### 3.1 在 Claude Code 中直接引用

当你需要 Wiki 中的信息时，可以这样做：

```
1. 我需要查看 UI 布局快速判断流程
   → 打开 [[llm_wiki/wiki/guides/UI_Layout_Quick_Judge]]
   
2. 我想了解 4 层分类维度
   → 打开 [[llm_wiki/wiki/concepts/UI_Layout_Classification_Dimensions]]
   
3. 我要学习常见错误
   → 打开 [[llm_wiki/wiki/guides/Avoiding_Classification_Mistakes]]
```

### 3.2 在代码或笔记中引用

```markdown
根据[[llm_wiki/wiki/guides/UI_Layout_Quick_Judge]]中的快速判断法：
1. 看窗口大小
2. 看内容分割
3. 检查装饰元素

详细说明参考：[[llm_wiki/wiki/guides/UI_Layout_Classification_Guide]]
```

---

## 🎯 常见任务和解决方案

### 任务1：我想快速找到某个布局类型的说明

```powershell
# PowerShell 方式
$wikiRoot = "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki"
$layoutType = "T型-上标题-左标签-右竖列表"
$file = Get-ChildItem -Path "$wikiRoot\wiki\concepts\layout-types" -Filter "*$layoutType*"
Get-Content -Path $file.FullName -Encoding UTF8
```

### 任务2：我要统计所有布局类型有多少个

```powershell
$layoutTypesPath = "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\wiki\concepts\layout-types"
(Get-ChildItem -Path $layoutTypesPath -Filter "*.md").Count
```

### 任务3：我要在 Claude Code 中读取某个错误分析

在 Claude Code 中使用 Read 工具：
```
文件路径：llm_wiki/wiki/guides/Avoiding_Classification_Mistakes.md
```

### 任务4：我想查看 Wiki 的完整目录结构

```powershell
# 使用 tree 命令（需要装 tree 工具）
tree "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki" /F

# 或使用 PowerShell
function Show-Tree {
  param([string]$Path, [int]$Indent = 0)
  Get-ChildItem -Path $Path | ForEach-Object {
    "  " * $Indent + $_.Name
    if ($_.PSIsContainer) {
      Show-Tree -Path $_.FullName -Indent ($Indent + 1)
    }
  }
}
Show-Tree "D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki"
```

---

## 🚀 最佳实践

### ✅ 推荐做法

1. **使用相对路径**
   - 在 Claude Code 中：`llm_wiki/wiki/guides/UI_Layout_Quick_Judge.md`
   - 这样更灵活，不依赖绝对路径

2. **创建 Wiki 根变量**
   ```powershell
   $wikiRoot = (Get-Location).Path + "\llm_wiki"
   ```
   - 这样可以快速访问所有 Wiki 文件

3. **使用 UTF8 编码**
   ```powershell
   Get-Content -Encoding UTF8  # 确保中文显示正确
   ```

4. **定期更新路径变量**
   - 如果 Wiki 位置变更，更新变量定义

### ❌ 避免做法

1. **不要硬编码长路径**
   - 不好：`"D:\obsidianProject\portrait-to-landscape\Unity横转竖\llm_wiki\wiki\guides\UI_Layout_Quick_Judge.md"`
   - 好：使用变量或相对路径

2. **不要使用错误的编码**
   - 不好：`Get-Content -Path $file`（默认编码）
   - 好：`Get-Content -Path $file -Encoding UTF8`

3. **不要忽视路径中的中文字符**
   - 某些工具可能对中文路径有问题
   - 在 Claude Code 中最好使用相对路径

---

## 📖 快速参考

### 最常用的 5 个命令

```powershell
# 1. 读取快速判断流程
Get-Content "llm_wiki\wiki\guides\UI_Layout_Quick_Judge.md" -Encoding UTF8

# 2. 列出所有指南
Get-ChildItem "llm_wiki\wiki\guides" -Filter "*.md"

# 3. 搜索特定主题
Get-ChildItem "llm_wiki" -Recurse -Filter "*.md" | 
  Where-Object { (Get-Content $_.FullName -Encoding UTF8) -match "你的关键词" }

# 4. 统计总页数
(Get-ChildItem "llm_wiki" -Recurse -Filter "*.md").Count

# 5. 查看某个布局类型
Get-Content "llm_wiki\wiki\concepts\layout-types\[你要的类型].md" -Encoding UTF8
```

---

## 💡 进阶用法

### 创建 Wiki 查询脚本

```powershell
# 保存为 wiki-search.ps1
param(
  [string]$SearchTerm,
  [string]$Path = ".\llm_wiki"
)

Write-Output "搜索: $SearchTerm`n"
Get-ChildItem -Path $Path -Recurse -Filter "*.md" |
  Where-Object {
    $content = Get-Content $_.FullName -Encoding UTF8
    $content -match $SearchTerm
  } |
  ForEach-Object {
    Write-Output "文件: $($_.Name)"
    Write-Output "路径: $($_.FullName)"
    Write-Output "---"
  }
```

使用方式：
```powershell
.\wiki-search.ps1 -SearchTerm "布局分类"
```

---

## ⚠️ 常见问题

**Q: 路径中有中文，Read 工具是否支持？**
A: 支持，但推荐使用相对路径：`llm_wiki/wiki/guides/...`

**Q: 如何在 Claude Code 中更新 Wiki 内容？**
A: 使用 Edit 或 Write 工具，指定相对路径即可

**Q: 如何确保 Wiki 内容不被意外修改？**
A: 可以在 vault 中设置这些文件为只读，或在 Claude Code 中使用 Read-Only 模式

**Q: Wiki 位置变了怎么办？**
A: 更新所有路径变量和引用，相对路径自动适应

---

## 🔗 相关资源

- [[llm_wiki/README]] - Wiki 快速开始
- [[llm_wiki/DASHBOARD]] - Wiki 仪表板和导航
- [[llm_wiki/config/SCHEMA]] - Wiki 规范
- [[llm_wiki/workflows/Ingest_Workflow]] - 数据摄入工作流

---

**指南创建**：2026-05-06  
**适用环境**：Windows PowerShell + Claude Code  
**最后更新**：2026-05-06

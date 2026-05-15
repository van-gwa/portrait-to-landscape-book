# 🚀 快速开始指南

## 在你的项目中使用预制体分析数据

---

## 📋 5分钟快速上手

### 步骤1：查看全局报告

```bash
# 打开这个文件了解全局统计
D:\obsidianProject\portrait-to-landscape\Unity横转竖\similarity_analysis\global_similarity_analysis.md
```

**你会看到**:
- TOP 20最常用的资源
- 预制体复杂度分布
- 精灵数TOP 20的预制体

---

### 步骤2：查找具体预制体

**在Obsidian中**:
1. 打开 `prefab_analysis/` 文件夹
2. Ctrl+P 快速打开，输入预制体名称（如 `UI_Chat`）
3. 查看该预制体使用的所有资源

**或在命令行**:
```bash
cd "D:\obsidianProject\portrait-to-landscape\Unity横转竖"
python3 scripts/quick_query.py "UI_Chat"
```

---

### 步骤3：找相似的界面

```bash
# 找与UI_Chat相似的所有预制体
python3 scripts/quick_query.py --similar "UI_Chat" --similarity 0.3
```

输出示例:
```
🔎 与 'UI_Chat' 相似的预制体 (相似度 >= 30%):
============================================================
相似度       共享资源        预制体
----------------------------------------------------------------------
81.0%      17         UI_GuestInfo
62.5%      10         UI_SilkroadMap
50.0%       8         UI_Main
...
```

---

### 步骤4：按条件筛选

```bash
# 找精灵数超过100的所有预制体
python3 scripts/quick_query.py --sprite-count 100

# 找精灵数在50-100之间的预制体
python3 scripts/quick_query.py --sprite-count 50 --max 100

# 找使用特定资源的所有预制体
python3 scripts/quick_query.py --guid "f3cd0b87d165167408ec7bd72e5c8056"
```

---

## 💻 常用命令参考

### 查询预制体信息

```bash
# 查看UI_Chat的所有资源
python3 scripts/quick_query.py "UI_Chat"

# 结果包含:
# - 路径和基本信息
# - 使用的所有GUID列表
# - 精灵数和文件引用数
```

### 按资源查询

```bash
# 查找使用特定资源的预制体
python3 scripts/quick_query.py --guid "0043689f31ec8dc4a95674a1144d7078"

# 结果显示:
# - 使用该资源的所有预制体列表
# - 按名称排序
```

### 按相似度查询

```bash
# 严格匹配（相似度 >= 70%）
python3 scripts/quick_query.py --similar "UI_Chat" --similarity 0.7 --limit 20

# 宽松匹配（相似度 >= 20%）
python3 scripts/quick_query.py --similar "UI_Chat" --similarity 0.2 --limit 50
```

### 按复杂度查询

```bash
# 简单界面 (< 50精灵)
python3 scripts/quick_query.py --sprite-count 0 --max 49

# 中等复杂 (50-100精灵)
python3 scripts/quick_query.py --sprite-count 50 --max 100

# 复杂界面 (> 150精灵)
python3 scripts/quick_query.py --sprite-count 150
```

---

## 📊 典型使用场景

### 场景1：我想找所有"列表类"界面

**思路**: 找精灵数较多（50+）且相互相似的预制体

```bash
# 1. 找精灵数50-150的预制体
python3 scripts/quick_query.py --sprite-count 50 --max 150

# 2. 选一个代表（如UI_MarketList），查看它的相似体
python3 scripts/quick_query.py --similar "UI_MarketList" --similarity 0.3
```

---

### 场景2：我想了解某个资源被哪些界面使用

**思路**: 查找使用该资源的所有预制体

```bash
# 查找使用资源f3cd0b87d165167408ec7bd72e5c8056的预制体
python3 scripts/quick_query.py --guid "f3cd0b87d165167408ec7bd72e5c8056"

# 结果会列出使用该资源的所有预制体
# 这些预制体可能有类似的视觉风格
```

---

### 场景3：我要处理UI转换，需要找"相同风格"的界面

**思路**: 找使用相同资源组合的预制体

```bash
# 1. 选一个代表预制体（如UI_Main）
# 2. 找与它相似的所有预制体
python3 scripts/quick_query.py --similar "UI_Main" --similarity 0.5

# 这些相似预制体可以用相同的转换策略处理
```

---

### 场景4：我想批量处理最复杂的界面

**思路**: 先处理高精灵数的复杂界面

```bash
# 找精灵数最多的预制体
python3 scripts/quick_query.py --sprite-count 100

# 结果会按精灵数从多到少排列
# 优先处理TOP 10可以解决最复杂的10个界面
```

---

## 🔍 在Obsidian中使用索引

### 全文搜索GUID

1. 打开Obsidian
2. 按 `Ctrl+Shift+F` 打开全文搜索
3. 输入GUID（如 `f3cd0b87d165167408ec7bd72e5c8056`）
4. 所有使用该资源的笔记都会显示

### 查看预制体笔记

1. 按 `Ctrl+P` 快速打开
2. 输入预制体名称（如 `UI_Chat`）
3. 选择 `prefab_analysis/Chat/UI_Chat.md`
4. 查看笔记中的所有资源信息

### 使用关系图

1. 打开任何笔记
2. 查看右侧的"反向链接"（若已配置）
3. 了解哪些其他预制体使用了相同资源

---

## 📁 文件位置速查

| 用途 | 文件路径 |
|------|---------|
| 全局统计 | `similarity_analysis/global_similarity_analysis.md` |
| 索引文件 | `prefab_sprites_index.json` |
| 预制体笔记 | `prefab_analysis/[模块]/[预制体].md` |
| 快速查询 | `scripts/quick_query.py` |
| 相似分析 | `scripts/analyze_similarity.py` |
| 项目总结 | `PROJECT_SUMMARY.md` |

---

## ⚙️ 常见问题

### Q: 如何导出查询结果为CSV？

编辑 `scripts/quick_query.py`，在main()末尾添加：

```python
# 导出为CSV
import csv

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['名称', '路径', '精灵数'])
    for prefab_path, data in query.index.items():
        writer.writerow([data['prefab_name'], prefab_path, data['sprite_count']])
```

---

### Q: 如何找到完全不使用任何资源的预制体？

```python
from scripts.query_prefab_resources import PrefabResourceQuery

query = PrefabResourceQuery()
empty_prefabs = [p for p, d in query.index.items() if len(d['guids']) == 0]
print(f"找到 {len(empty_prefabs)} 个空预制体")
```

---

### Q: 相似度0.3是什么意思？

**Jaccard相似度** = 共享资源 / 总资源

- 0.0 = 完全不同
- 0.3 = 共享30%的资源
- 0.5 = 共享50%的资源
- 1.0 = 完全相同

**建议阈值**:
- `--similarity 0.1`: 非常宽松（包含远距离相似）
- `--similarity 0.3`: 一般相似
- `--similarity 0.5`: 高度相似
- `--similarity 0.7`: 非常相似

---

### Q: 为什么有些预制体的GUID数和精灵数不同？

因为：
- **精灵数**: 该预制体中实际使用的精灵总数（有重复）
- **GUID数**: 该预制体引用的唯一资源种类数（去重）

例如：一个预制体可能引用同一张图片100次，但GUID数只有1。

---

## 🎯 下一步建议

### 建议1：按相似度聚类预制体

```python
# 创建一个脚本，将所有预制体按相似度分组
# 相似的预制体可以用同样的转换策略
```

### 建议2：分析UI设计模式

```python
# 找出最常见的资源组合
# 了解项目的UI设计规范
```

### 建议3：优化处理顺序

```python
# 按以下顺序处理:
# 1. 影响最大的高频资源
# 2. 高复杂度的预制体
# 3. 高相似度的预制体组
```

---

## 💬 需要帮助？

1. **查看详细报告**: 打开 `PROJECT_SUMMARY.md`
2. **查看技术细节**: 打开 `prefab_analysis_report.md`
3. **查看脚本源码**: 查看 `scripts/` 目录中的注释
4. **运行帮助命令**: `python3 scripts/quick_query.py --help`

---

**祝你使用愉快！如有问题，检查脚本的日志输出或项目文档。** 🎉

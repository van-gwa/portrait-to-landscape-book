# 🚀 批量处理预制体指南

## 快速命令参考

### 1. 处理前N个预制体（快速测试）

```bash
cd "D:\obsidianProject\portrait-to-landscape\Unity横转竖"

# 处理前50个
python3 scripts/batch_final_analysis.py --limit 50

# 处理前100个
python3 scripts/batch_final_analysis.py --limit 100

# 处理前500个
python3 scripts/batch_final_analysis.py --limit 500
```

### 2. 处理特定模块的预制体

```bash
# 只处理Chat模块
python3 scripts/batch_final_analysis.py --module Chat

# 只处理Activity模块
python3 scripts/batch_final_analysis.py --module Activity

# 只处理ActApexPvp模块
python3 scripts/batch_final_analysis.py --module ActApexPvp
```

### 3. 处理所有预制体（完整处理）

```bash
# 处理所有预制体（耗时较长，预计30-60分钟）
python3 scripts/batch_final_analysis.py
```

---

## 预期的处理时间

| 数量 | 处理速度 | 预计时间 |
|------|--------|--------|
| 50个 | 0.5秒/个 | ~25秒 |
| 100个 | 0.5秒/个 | ~50秒 |
| 500个 | 0.5秒/个 | ~4-5分钟 |
| 全部(1400+) | 0.5秒/个 | ~12-15分钟 |

---

## 生成的笔记位置

```
D:\obsidianProject\portrait-to-landscape\Unity横转竖\prefab_final_analysis\
├── UI_ActApexPvp.md
├── UI_ActApexPvpBattle.md
├── UI_Chat.md
├── UI_BlockBattleMap.md
├── ...
└── (所有预制体都会生成同名的.md文件)
```

**每个笔记包含**:
- ✅ GameObject的完整树结构
- ✅ 每个GameObject的名称和尺寸
- ✅ Image组件使用的资源名称、FileID和GUID
- ✅ RawImage组件使用的资源名称、FileID和GUID

---

## 笔记内容示例

打开任何生成的笔记（如 `UI_Chat.md`），你会看到：

### Image资源部分
```
| 完整路径 | 尺寸 | 资源名称 | FileID | GUID |
|--------|------|--------|--------|------|
| `BtnAdd` | 36.3×40.0 | **atlas_chat_static.png** | `1008801711` | `08ccf81ac676f764191f62d6b9fe6cee` |
| `Image` | 88.0×86.0 | **atlas_common_static.png** | `-1803286378` | `f3cd0b87d165167408ec7bd72e5c8056` |
| ... | ... | ... | ... | ... |
```

### RawImage资源部分
```
| 完整路径 | 尺寸 | 资源名称 | FileID | GUID |
|--------|------|--------|--------|------|
| `RawImage` | 167.6×720.0 | **ui_lt_bg_0002.png** | `2800000` | `67de4419e6ddc4145a1cadd089dbd367` |
| `ImageBg` | 424.2×653.7 | **ui_common_bg_0052.png** | `2800000` | `a03bfc7dc4e0b8b4e8c3086842f6e0ec` |
| ... | ... | ... | ... | ... |
```

---

## 在Obsidian中查看

1. 打开Obsidian库
2. 进入 `prefab_final_analysis` 文件夹
3. 按预制体名称搜索（如 `UI_Chat`）
4. 打开笔记查看完整信息

---

## 脚本信息

- **脚本位置**: `scripts/batch_final_analysis.py`
- **基础路径**: `D:\CursorProject\Dadian - 副本\Arts\Assets\ArtResources\UIs\Prefabs`
- **输出路径**: `prefab_final_analysis/`
- **GUID映射**: 自动扫描Assets目录下的所有.meta文件（需要时间）

---

## 注意事项

1. **首次运行**: 第一次运行时会加载GUID映射，可能需要30-60秒
2. **后续运行**: 脚本会重新加载映射，确保资源名称最新
3. **中断处理**: 可以随时Ctrl+C中断，已处理的笔记会保存
4. **重复处理**: 如果重复运行，会覆盖已有的笔记

---

## 常见问题

**Q: 为什么第一次运行这么慢？**
A: 脚本需要加载所有.meta文件建立GUID映射，需要30-60秒。后续运行同样需要。

**Q: 可以只处理某个模块吗？**
A: 可以，使用 `--module ModuleName` 参数，如 `--module Chat`

**Q: 全部1400+个预制体需要多长时间？**
A: 大约12-15分钟（包括GUID加载时间）

**Q: 生成的笔记太多会不会影响Obsidian性能？**
A: 不会有明显影响。Obsidian可以轻松处理1000+个笔记。

---

## 下一步

建议处理顺序：
1. ✅ 已完成：前3个预制体（测试）
2. ⏳ 现在：前100个预制体
3. 后续：处理全部预制体

建议使用：
```bash
python3 scripts/batch_final_analysis.py
```

这会自动处理所有预制体。

---
type: concept
created: 2026-05-04
updated: 2026-05-04
tags: [concept, ui-design, component]
related: [[llm_wiki/wiki/concepts/UI_Layout]], [[llm_wiki/wiki/entities/UI_Database]]
---

# UI 组件

## 定义
**UI 组件**是 Unity 游戏项目中可复用的用户界面元素单元。每个组件都有特定的功能和视觉表现，可以组合使用来构建完整的界面。

## 核心组件类型

### 1. 文本组件
- **标题文本**（Title）：界面名称或主要信息
- **正文文本**（Body Text）：内容详情
- **标签文本**（Label）：字段说明

### 2. 输入组件
- **按钮**（Button）：触发操作
- **输入框**（InputField）：接收用户输入
- **滑块**（Slider）：数值选择
- **开关**（Toggle）：二进制选择

### 3. 显示组件
- **图像**（Image）：显示贴图和图片
- **进度条**（ProgressBar）：显示进度
- **列表项**（ListItem）：列表中的单项

### 4. 布局组件
- **滚动视图**（ScrollRect）：可滚动内容
- **网格布局**（GridLayout）：网格排列
- **竖直布局**（VerticalLayout）：竖向排列
- **横向布局**（HorizontalLayout）：横向排列

### 5. 特殊组件
- **遮罩**（Mask）：裁剪显示区域
- **按钮组**（ButtonGroup）：多个按钮集合
- **标签页**（Tabs）：多页签切换

## 组件属性

### 通用属性
```yaml
组件类型: [type]
尺寸: [width × height]
位置: [x, y]
缩放: [scaleX, scaleY]
旋转: [rotation]
颜色: [color]
透明度: [alpha]
启用状态: [active]
```

### 交互属性
```yaml
可交互: [true/false]
响应事件: [click/hover/drag/...]
禁用时表现: [grayed/hidden/...]
```

## 常见组件组合

### 列表项组合
```
ListItem
├─ Image（图标/头像）
├─ Text（名称）
├─ Text（描述）
└─ Text（数值）
```

### 按钮组合
```
Button
├─ Image（背景）
├─ Text（标签）
└─ Outline（边框）
```

### 卡片组合
```
Card
├─ Image（背景或头图）
├─ VerticalLayout
│  ├─ Text（标题）
│  ├─ Text（描述）
│  └─ HorizontalLayout
│     ├─ Button
│     └─ Button
```

## 相关概念
- [[llm_wiki/wiki/concepts/UI_Layout|UI 布局]]
- [[llm_wiki/wiki/concepts/Component_Hierarchy|组件树结构]]

## 应用数据
- 项目中共使用的组件类型：20+ 种
- 最常用的组件：Button、Text、Image
- 最复杂的组件：ScrollRect（经常嵌套）

## 参考资源
- [[llm_wiki/wiki/guides/Component_Analysis_Guide|组件分析指南]]

# AI 文档处理工具箱

> 基于 DeepSeek API 的 AI 文档工具——浏览器端可视化 + 命令行两种方式

## 快速开始

### 方式一：浏览器端

双击 `index.html`，设置 API Key，选择模式，粘贴文档，点击生成。

### 方式二：命令行

```bash
# 文档摘要
python ai-cli.py summary < 输入文件.txt

# 需求整理
python ai-cli.py requirements 需求描述.txt

# 会议纪要
python ai-cli.py minutes 会议记录.txt
```

## 四种处理模式

| 模式 | 用途 |
|------|------|
| 文档摘要 | 长文 → 一句话概括 + 核心要点 + 数据 |
| 需求整理 | 客户原话 → 结构化需求文档 |
| 会议纪要 | 会议内容 → 标准化纪要 + 待办清单 |
| 智能识别 | AI 自动判断内容类型 |

## 导出格式（浏览器端）

📋 复制 / 📝 Markdown / 📄 TXT / 🖨️ PDF

## 项目文件

```
├── index.html          # 浏览器端工具
├── ai-cli.py           # 命令行工具
├── README.md
├── 需求整理助手.txt     # Prompt 模板
├── 文档摘要助手.txt     # Prompt 模板
└── 演示材料.pdf        # 效果演示
```

## 技术栈

- 浏览器端：纯 HTML/CSS/JS（零依赖，单文件）
- 命令行：Python + DeepSeek API（纯标准库，零第三方依赖）
- API：DeepSeek Chat API
- 存储：API Key 仅存在本地

## 为什么做这个

我是计算机网络专业学生，对 AI 工具在实际办公场景的应用有浓厚兴趣。课余搭建过 AI 开发环境（DeepSeek + Claude Code），也独立开发了这个文档处理工具箱——同时提供浏览器端和命令行两种交互方式。项目助理日常大量时间花在"整理信息"上，这个工具要解决的就是这个问题。

## 后续计划

- [ ] 支持流式输出
- [ ] 新增竞品分析模板
- [ ] 接入 Dify/Coze 工作流
- [ ] 批量文件处理

---

*作者：黄世游 | 2026.06*

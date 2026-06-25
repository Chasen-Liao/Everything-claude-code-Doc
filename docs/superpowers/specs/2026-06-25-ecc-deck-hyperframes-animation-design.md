# ECC 导读幻灯片 HyperFrames 动画设计

## 目标

把现有 `docs/deck.html` 的 10 页 ECC 导读幻灯片改编为一个可预览、可渲染为 MP4 的 HyperFrames 动画视频。现有网页幻灯片保持不变；动画视频作为独立项目新增。

## 输出形态

- 新增目录：`hyperframes-ecc-deck/`
- 视频比例：16:9 横屏
- 分辨率：1920x1080
- 时长：约 70 秒
- 内容来源：复用 `docs/deck.html` 的 10 页结构、文案和视觉主题
- 交付方式：HyperFrames 项目，可通过 `npx hyperframes preview` 预览，并可通过 `npx hyperframes render` 导出 MP4

## 视觉风格

沿用现有 notebook tabs 主题：

- 深灰外底：`#2d2d2d`
- 奶油纸张：`#f8f6f1`
- 主文本：`#1a1a1a`
- 次级文本：`#6b6358`
- 标签色：薄荷绿、薰衣草紫、粉色、浅蓝、浅黄
- 字体：标题使用 Bodoni Moda / Didot 风格，正文使用 DM Sans / Helvetica Neue 风格

新增 HyperFrames 项目需要包含 `DESIGN.md`，记录上述颜色、字体、动效约束，满足 HyperFrames 的视觉身份要求。

## 内容结构

视频按原幻灯片逐页改编：

1. 封面：Everything Claude Code 与核心规模数字
2. 目录：三段主线
3. 章节页：ECC 是什么
4. 概念页：Agentic Coding harness
5. 基石页：Agent / Skill / Command / Rule / Hook
6. 章节页：命令
7. 命令速查：6 个高频入口
8. 章节页：工作流
9. 工作流页：端到端任务流水线
10. 结束页：系统而非命令集合，附站点入口

## 动画设计

每页使用相同的基础舞台：深灰背景、纸张卡片、装订孔、左侧红线、右侧彩色标签页。

单页动效：

- 纸张轻微缩放或上移进入
- 页眉先入场
- 标题、说明、列表、卡片按视觉层级 stagger 出现
- 数字页使用描边大数字滑入
- 命令表按行依次出现
- 工作流卡片按 2x2 节奏出现

页间转场：

- 不使用硬切
- outgoing page 在转场开始时保持完整可见
- 使用纸张覆盖、轻微位移、透明度交叠和标签页高亮切换完成场景转换
- 末页允许淡出到结束状态

## 技术方案

- 使用 HyperFrames HTML composition，而不是录屏现有网页。
- 根文件为 `hyperframes-ecc-deck/index.html`。
- 所有场景在一个 composition 内按时间线编排，降低跨文件复杂度。
- 使用 GSAP 时间线，所有 timeline 同步注册到 `window.__timelines`。
- 不使用随机数、异步构建 timeline、无限 repeat、媒体 play/pause 调用。
- 不编辑 `everything-claude-code/`。
- 不修改现有 `docs/deck.html`，除非后续用户明确要求把动画入口接入站点。

## 验证标准

完成后至少运行：

```bash
npx hyperframes lint
npx hyperframes validate
npx hyperframes inspect
```

如果本地环境支持渲染，再运行：

```bash
npx hyperframes render --quality draft
```

成功标准：

- HyperFrames lint 无错误
- validate 无必须修复的结构错误
- inspect 无文本溢出或画面越界问题
- 视频能从第一页按时间自动播放到结束页
- 现有 MkDocs 站点不被破坏

## 明确不做

- 不把动画直接嵌入 GitHub Pages
- 不生成配音或字幕
- 不重写教程内容
- 不把 `docs/deck.html` 改造成 HyperFrames 源文件
- 不创建新的 CI workflow

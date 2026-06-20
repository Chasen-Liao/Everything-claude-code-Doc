<div class="hero-container">
  <h1 class="hero-title">Everything Claude Code <span class="gradient-text">中文教程</span></h1>
  <p class="hero-subtitle">ECC (Everything Claude Code) 的中文导读、最佳实践与能力检索手册</p>
  <div class="hero-actions">
    <a href="getting-started/what-is-ecc/" class="hero-btn primary-btn">快速开始 →</a>
    <a href="commands/" class="hero-btn secondary-btn">命令速查</a>
  </div>
  <p style="font-size: 0.85rem; margin: 0; opacity: 0.75; line-height: 1.6;">
    💡 这是 <a href="https://github.com/affaan-m/ECC" target="_blank">affaan-m/Everything Claude Code</a> 的中文导读镜像。上游为权威源，本站重在导读与串联。
  </p>
</div>

## 这是什么

`affaan-m/Everything Claude Code`(简称 **ECC**)是一份面向 Claude Code 用户的"能力清单 + 最佳实践"集合,围绕 **Agent / Skill / Command / Hook / Rule** 五个核心概念组织,覆盖从个人工作流到团队协作的多类场景。

本教程站点把上游的入口拆成可按需检索的多页结构,帮助你:

- **5 分钟**:理解 ECC 的能力边界与适用人群
- **15 分钟**:定位到自己语言 / 场景下需要的命令族
- **按需深入**:回到上游仓库查原始定义与示例

## 怎么开始

<div class="grid cards" markdown>

-   :material-rocket-launch: __新手上路__

    ---

    第一次接触 ECC?从这一篇开始,5 分钟建立整体认知。

    [:octicons-arrow-right-24: ECC 是什么](getting-started/what-is-ecc.md)

-   :material-map: __按场景 / 语言读__

    ---

    已经知道 ECC 是什么,想找"我现在能用上的"命令族与工作流。

    [:octicons-arrow-right-24: 命令速查](commands/index.md)

-   :material-book-open-variant: __阅读路线__

    ---

    不知道从哪开始?按"角色 × 目标"给出 3 条推荐阅读路径。

    [:octicons-arrow-right-24: 阅读路线](routes/index.md)

-   :material-source-branch: __维护本仓库__

    ---

    贡献者视角:如何与上游同步、刷新中文文档、保持计数对齐。

    [:octicons-arrow-right-24: 与上游同步](maintenance/sync-upstream.md)

</div>

## 上游状态

<div class="stats-container">
  <div class="stats-card">
    <div class="stats-number">67</div>
    <div class="stats-label">Agents 智能体</div>
  </div>
  <div class="stats-card">
    <div class="stats-number">271</div>
    <div class="stats-label">Skills 技能数</div>
  </div>
  <div class="stats-card">
    <div class="stats-number">59 + 92</div>
    <div class="stats-label">Commands 命令数</div>
  </div>
</div>
<div class="sync-info">
  📌 <strong>镜像 SHA:</strong> <code>34faa39b</code> (上游 <code>2.0.0</code>) | ⏰ <strong>最后同步:</strong> 2026-06-21
</div>

!!! tip "回到上游"
    本教程层只解释、串联；<strong>所有权威定义、命令原文、配置示例，请回 <a href="https://github.com/affaan-m/ECC" target="_blank">affaan-m/ECC</a> 仓库阅读。</strong>
    站内"上游副本导航"分组的 <a href="upstream-navigation/by-directory/">upstream-navigation/by-directory/</a> 提供了完整目录索引。

## 读者分流

<div class="routing-container">
  <div class="routing-card routing-card-new">
    <div class="routing-badge badge-new">新手</div>
    <h3>第一次听说 ECC</h3>
    <p>快速建立概念认知，了解它的能力边界与适用人群，轻松开启第一步。</p>
    <a href="getting-started/what-is-ecc/">ECC 是什么 →</a>
  </div>
  <div class="routing-card routing-card-concept">
    <div class="routing-badge badge-concept">核心</div>
    <h3>概念分不清楚</h3>
    <p>搞不懂 Agent、Skill 与 Command 的区别与协同关系？这里有最透彻的拆解。</p>
    <a href="concepts/overview/">核心概念总览 →</a>
  </div>
  <div class="routing-card routing-card-cmd">
    <div class="routing-badge badge-cmd">速查</div>
    <h3>只想查某条命令</h3>
    <p>按场景、按语言、最常用或完整工作流，提供多种维度的检索导航。</p>
    <a href="commands/">命令速查总览 →</a>
  </div>
  <div class="routing-card routing-card-dev">
    <div class="routing-badge badge-dev">贡献</div>
    <h3>要维护本仓库</h3>
    <p>贡献者视角：如何与上游保持同步、合并最新改动、刷新并保持计数一致。</p>
    <a href="maintenance/sync-upstream/">与上游同步 →</a>
  </div>
</div>

## 仓库结构

本仓库分两层,各自承担不同职责:

- **教程层(本仓库维护)**:`docs/` 下的中文教程,由 GitHub Pages 渲染成当前站点。`README.md`、`ECC-COMMANDS-ZH.md`、`ECC-NAVIGATION-ZH.md` 三份顶层文档只是入口门牌,权威解释都在站点里。
- **上游同步层(上游维护)**:[`everything-claude-code/`](https://github.com/affaan-m/ECC/tree/main/) 是上游 ECC 的本地 gitlink 副本,目录名、文件内容、版本号都由上游决定,本仓库只做 fast-forward 同步,不直接编辑。

简单记法:**教程层负责讲清楚,同步层负责给原文。**

## 常见问题

- ECC 和官方 Claude Code 文档是什么关系? —— 见 [FAQ](faq.md)
- 上游变了,本教程会同步吗? —— 会,由 [`sync-upstream-zh-docs`](maintenance/sync-upstream.md) 技能驱动

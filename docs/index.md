# Everything Claude Code 中文教程

> [!info] 关于本教程
> 这是 [`affaan-m/Everything Claude Code`](https://github.com/affaan-m/ECC) 的**中文导读镜像**。
> 上游仓库才是权威源——本教程只做解释、串联、阅读路径,不承担"翻译并替代原文"的角色。

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

!!! note "权威计数(随上游更新)"
    - Agents: **63** · Skills: **249** · Commands: **59** slash + 79 legacy shims
    - 镜像 SHA: pinned at `64cd1ba2`(上游 `2.0.0-rc.1`)
    - 最后同步:<!--SYNC_DATE-->请运行 sync-upstream-zh-docs 技能后回填<!--END-->

!!! tip "回到上游"
    本教程层只解释、串联;**所有权威定义、命令原文、配置示例,请回 [`affaan-m/ECC`](https://github.com/affaan-m/ECC) 仓库阅读。**
    站内"上游副本导航"分组的 [`upstream-navigation/by-directory.md`](upstream-navigation/by-directory.md) 提供了完整目录索引。

## 常见问题

- ECC 和官方 Claude Code 文档是什么关系? —— 见 [FAQ](faq.md)
- 上游变了,本教程会同步吗? —— 会,由 [`sync-upstream-zh-docs`](maintenance/sync-upstream.md) 技能驱动

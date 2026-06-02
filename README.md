# Everything Claude Code 中文教程仓库

这是 [`affaan-m/ECC`](https://github.com/affaan-m/ECC) 的中文教程镜像仓库，主要内容已经搬到结构化的 GitHub Pages 站点。

## 中文教程站点

完整中文教程：**<https://Chasen-Liao.github.io/Everything-claude-code-Doc/>**

站点把上游的概念、命令、推荐阅读路线、上游副本导航等拆成可按需检索的多页结构，并保留与上游链接的双向跳转。本仓库根目录只做"门牌 + 入口"，权威解释都在站点里。

## 这份仓库是什么

仓库由两层组成：

- **教程层**：`docs/` 下的中文教程（由 GitHub Pages 渲染），三份顶层 .md（本 README、`ECC-COMMANDS-ZH.md`、`ECC-NAVIGATION-ZH.md`）只是门牌。
- **上游同步层**：[`everything-claude-code/`](everything-claude-code/) 是上游 ECC 的本地 gitlink 副本，由上游维护，本仓库只 fast-forward 同步。

如果你只想读教程，去 Pages 站点。如果你要核对上游真实文件内容，进入 `everything-claude-code/` 或上游官方仓库。

## 快速开始

1. 打开教程站点：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/>
2. 第一次接触 ECC：从"入门 / ECC 是什么"开始读。
3. 只想查命令：直接进"命令速查"。

## 上游官方入口

- 上游仓库主页：<https://github.com/affaan-m/ECC>
- 上游英文 README：<https://github.com/affaan-m/ECC/blob/main/README.md>
- 上游中文 README：<https://github.com/affaan-m/ECC/blob/main/README.zh-CN.md>
- 上游命令速查：<https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md>
- 上游长文指南：<https://github.com/affaan-m/ECC/blob/main/the-longform-guide.md>
- 上游短文指南：<https://github.com/affaan-m/ECC/blob/main/the-shortform-guide.md>
- 上游安全指南：<https://github.com/affaan-m/ECC/blob/main/the-security-guide.md>
- 上游故障排查：<https://github.com/affaan-m/ECC/blob/main/docs/TROUBLESHOOTING.md>

## 维护本仓库

- 同步上游 / 刷新中文文档的工作流见根目录 `CLAUDE.md` 与 [`.claude/skills/sync-upstream-zh-docs/`](.claude/skills/sync-upstream-zh-docs/)。
- 站点构建与发布走 `.github/workflows/deploy-pages.yml`。
- 站点配置见 `mkdocs.yml`，源在 `docs/`。

## License

见 [LICENSE](LICENSE)。

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库定位

这是 `affaan-m/Everything Claude Code (ECC)` 的**中文教程镜像仓库**，分两层：

- **顶层教程层（本仓库维护）**：`README.md`、`ECC-COMMANDS-ZH.md`、`ECC-NAVIGATION-ZH.md` 三份中文文档，负责解释、串联、给出阅读路径。
- **上游同步层**：`everything-claude-code/`，是上游 ECC 的嵌入式 gitlink 克隆（当前 pinned 在上游 SHA `34faa39b`，上游版本 `2.0.0`），其内容由上游管，本仓库只做同步。

权威定义始终以上游为准；本仓库的"教程层"只翻译/梳理/对齐计数，不复制完整原始文档。

## 关键的非显然事实

### `everything-claude-code/` 是 gitlink，不是普通子目录

在主仓库的 git index 里它是 mode 160000 的 gitlink，且**没有 `.gitmodules` 映射**——是一个独立 clone 套在主仓库的子目录里。

- 子目录里的工作树推进，**不会**自动反映到主仓库的 gitlink 记录。
- 主仓库要写回新 SHA，必须 `git add everything-claude-code` 然后再 commit。
- 推进方式只能 fast-forward，不要 rebase 或非 ff merge——重写历史会让与上游的 diff 变得不可读。

### `59` 和 `92` 是两个不同的数

- `everything-claude-code/commands/` 目录下是 **92 个命令文件**（含 `legacy-command-shims/` 的兼容别名）。
- `everything-claude-code/COMMANDS-QUICK-REF.md` 列的是 **59 个全局 slash commands**。
- 两者不可互换；上层中文文档提到"59"时不要改成"92"，反之亦然。

### 上游 README 公开承诺的同步面

`agents / skills / commands / rules` 数量与 `everything-claude-code/README.md` 里的 "67 agents, 271 skills, 92 legacy command shims" 对齐。`README.md` 第 442、1529、1531 行是这几组数字的权威来源。

## 维护工作流（最常用命令）

```bash
# 1. 在子仓库里推进上游
cd everything-claude-code
git fetch origin
git rev-list --left-right --count HEAD...origin/main
git merge --ff-only origin/main

# 2. 量化变化、对齐权威计数
for d in agents skills commands rules; do echo -n "$d: "; ls $d | wc -l; done
grep -nE "67 agents|271 skills|92 legacy|59 slash" README.md

# 3. 回到主仓库写回新 SHA 并按需刷新顶层中文文档
cd ..
git add everything-claude-code
```

子仓库 diff 里出现的 `CRLF` 警告是 `core.autocrlf` 在 Windows 上的正常表现，不要去改文件换行。

## 边界

**不要直接编辑或重写**：

- `everything-claude-code/` 下任何文件（除 gitlink 元数据外）——所有改动通过 fast-forward 同步自上游。
- `everything-claude-code/README.zh-CN.md`——那是上游的中文 README，由上游维护。
- `LICENSE`——保留上游许可原文。

**只编辑**：

- 顶层三份中文教程（数量、表格、新语言轨道、新命令族）。
- 顶层 `.claude/skills/` 下的项目级技能。

## 仓库自带技能

`.claude/skills/sync-upstream-zh-docs/SKILL.md` 把"同步上游 → 量化变化 → 扫描顶层中文文档过期项 → 精准修改"整条链路编码成了单一 skill。

当用户说"同步上游 / 刷新中文文档 / 维护教程"，或观察到上游 `VERSION` 变化、agents/skills/commands 计数漂移时，**先调用该 skill**，再按它的指引执行。它内部已包含易错点（gitlink 写回、59 vs 79、CRLF 警告等）。

## Pages 站点维护

本仓库的中文教程通过 GitHub Pages + MkDocs Material 发布。关键事实：

- 站点 URL：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/>
- 源目录：`docs/`，MkDocs 配置 `mkdocs.yml`。
- 上游 gitlink `everything-claude-code/` 通过 `exclude_docs` 排除，**不进 build**。
- CI 工作流：`.github/workflows/deploy-pages.yml`，仅在 `docs/**`、`mkdocs.yml`、`requirements.txt` 变更时触发。
- 一次性迁移脚本 `scripts/migrate_docs.py` 已完成首版迁移，**默认不重跑**——后续编辑直接修 `docs/` 下文件即可。
- 顶层 `README.md`、`ECC-COMMANDS-ZH.md`、`ECC-NAVIGATION-ZH.md` 是 Pages 站点的门牌，不再是权威正文。改它们不会触发 Pages 重建。
- 本地预览：`python -m mkdocs serve`，严格构建：`python -m mkdocs build --strict`。

注意：编辑 `docs/` 下文件时，链接形态要遵守站内相对路径或 `https://github.com/affaan-m/ECC/...` 上游 URL 二选一，**禁止再引入 `everything-claude-code/...` 形态的相对路径**。

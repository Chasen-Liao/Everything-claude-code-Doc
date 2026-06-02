---
name: sync-upstream-zh-docs
description: Sync the embedded affaan-m/ECC clone under everything-claude-code/ to upstream, then refresh the top-level Chinese tutorial docs (README.md, ECC-COMMANDS-ZH.md, ECC-NAVIGATION-ZH.md) for any stale counts, new language tracks, or new commands. Use when the user asks to "同步上游", "刷新中文文档", "维护教程", or after noticing the upstream VERSION / count drift.
origin: ECC
---

# Sync Upstream and Refresh Chinese Docs

This repo mirrors upstream `affaan-m/ECC` as an embedded clone at `everything-claude-code/`, with a thin layer of Chinese tutorial docs at the top. This skill encodes the full maintenance loop.

## 触发场景

- 用户要求"同步上游"、"刷新中文文档"、"维护教程"
- 上游 `VERSION` 变化或 agents / skills / commands 数量可见变化
- 周期维护（建议每次上游 release 后跑一次）

## 工作流

### 1. 同步子仓库

```bash
cd everything-claude-code
git fetch origin
git rev-list --left-right --count HEAD...origin/main
```

落后时 fast-forward：

```bash
git merge --ff-only origin/main
```

读 `VERSION`。若版本号变化，预期有比常规刷新更大的改动（如新增语言轨道、命令族重构）。

### 2. 量化变化

```bash
# 当前数量
for d in agents skills commands rules; do
  echo -n "$d: "; ls $d | wc -l
done

# 关键文件 diff
git diff --name-status <old-sha>..HEAD -- agents/ skills/ commands/ rules/
git diff --stat <old-sha>..HEAD -- README.md README.zh-CN.md COMMANDS-QUICK-REF.md VERSION

# 上游 README 自己声明的权威数量
grep -nE "63 agents|249 skills|79 legacy|59 slash" README.md
```

把 `agents / skills / commands / rules` 数量与上游 README 头部声明的 "63 agents, 249 skills, 79 legacy command shims" 对齐——这是上游自己公开承诺的同步面。

### 3. 扫描顶层中文文档中的过期项

```bash
grep -rnE "60 个|232 个|75 个|60 |232 |75 " README.md ECC-COMMANDS-ZH.md ECC-NAVIGATION-ZH.md docs/
grep -rnE "react|React" README.md docs/
grep -rnE "go-reviewer|python-reviewer|java-reviewer|typescript-reviewer" README.md docs/
```

最容易过期的几类：

- 核心概念表的 agents / skills / commands 数量
- 文中对命令数量的复述（如"75 个命令文件" → "79 个命令文件"）
- 代理表 / 命令表的"语言专项"行（新增语言轨道时遗漏）
- 规则章节的"各语言目录"示例（新增语言目录时遗漏）
- 快速参考表的"语言/任务 → 常见专项入口"表

注意：`COMMANDS-QUICK-REF.md` 头部仍写 "59 slash commands installed globally"——这是**全局安装面**，不是命令文件数（`commands/` 目录下 79 个文件，差异在 `legacy-command-shims/` 与命名空间）。**59 不要改**。

### 4. 精准修改

用 `Edit` 工具逐处修改，每个修改独立验证。原则：

- 只改事实过期部分；不重构、不重写、不重新组织表格
- 不补充"营销 / 前端"等已隐含覆盖的内容（已写在 skill 族 5 或快速参考表）
- 不自动 commit；改完先向用户汇报

每次修改后用 grep 反向验证：

```bash
# 应为空
grep -rnE "60 个代理|232 个技能|75 个命令文件" README.md docs/
# 59 应保留
grep -rnE "59 个" README.md ECC-COMMANDS-ZH.md docs/
# React 应至少出现 4 处（含 docs/ 站点页）
grep -crE "react|React" README.md docs/
```

### 5. 汇报

向用户说明：

- 旧 SHA → 新 SHA、版本号是否变化
- agents / skills / commands 数量变化
- 改动的文件清单与具体位置
- 主动没改的内容和原因
- 询问是否 commit / push

## 易错点

- `everything-claude-code` 在主仓库是 **gitlink**（mode 160000）。子目录工作树推进不会自动反映到主仓库的 gitlink，需在主仓库 `git add everything-claude-code`，主仓库 commit 时才会把新 SHA 记录下来。
- **文件数 ≠ 全局命令数**。`commands/` 目录共 79 个 `.md` 文件，`COMMANDS-QUICK-REF.md` 列 59 个全局 slash command。
- **仅 fast-forward**。除非用户明确要求，不要 rebase 或非 ff merge——`everything-claude-code` 是嵌入式 clone，重写历史会让与上游的 diff 变得不可读。
- **Windows CRLF 警告**是 `core.autocrlf` 的正常提示，不要去改文件换行。
- **不替换 README.zh-CN.md**：那是上游的中文 README，由上游维护；本仓库只维护顶层的 `README.md` 等三份教程。
- **Pages 站点拆分页里的同步计数也要一起改**。`docs/` 下的章节同样含有 59 / 79 / 63 / 249 这类计数。刷新顶层三份 .md 时，必须把 `docs/**/*.md` 的同步计数一起改。否则会出现"顶层 README 已更新但 Pages 站点显示旧数"的不一致。

## 相关参考

- `everything-claude-code/COMMANDS-QUICK-REF.md` —— 命令权威清单
- `everything-claude-code/README.md` —— 数量权威来源（"63 agents, 249 skills, 79 legacy command shims"）
- `everything-claude-code/CHANGELOG.md` —— 上游版本历史
- `everything-claude-code/VERSION` —— 当前上游版本
- `README.md`（本仓库）—— 核心概念表、"现在的 ECC 和早期版本有什么不同"两节是过期高发区

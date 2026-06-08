# 与上游同步

本页面向**人**——任何协作者照着做都能成功把本仓库的 `everything-claude-code/` 嵌入式副本与上游 `affaan-m/Everything Claude Code` 对齐，并按需刷新顶层中文教程与 Pages 站点。

如果你在用 AI 助手维护这个仓库，请让它直接调用仓库自带的 [`.claude/skills/sync-upstream-zh-docs`](https://github.com/Chasen-Liao/Everything-claude-code-Doc/tree/main/.claude/skills/sync-upstream-zh-docs) skill；那一份是给 AI 看的。

## 什么时候看这页

- 上游 `affaan-m/ECC` 发了新 release，或 `everything-claude-code/VERSION` 文件值变了。
- 本仓库核心概念页 [核心概念](../concepts/overview.md) 里的 64/261/84/59 数字与上游对不上。
- 顶层 `README.md` / `ECC-COMMANDS-ZH.md` / `ECC-NAVIGATION-ZH.md` 提到的命令数、代理数、专项语言行明显落后。
- GitHub Pages 构建失败，或站点上某条命令的链接 404。

## 30 秒 TL;DR

整个同步是"在子仓库里 fast-forward，再回到主仓库写回新 SHA"的两步操作。常用版本：

```bash
cd everything-claude-code
git fetch origin
git rev-list --left-right --count HEAD...origin/main   # 看看落后多少
git merge --ff-only origin/main                        # 落后就拉平
cd ..
git add everything-claude-code                          # 把新 SHA 写回主仓库
git status                                             # 仅这个 gitlink 变化就算成功
```

需要的话再去刷顶层三份中文文档和 `docs/` 下的同步计数；刷完跑 `python -m mkdocs build --strict` 自检，然后 commit + push。

## 完整步骤

### 步骤 1：同步子仓库

进入嵌入式 clone，先看落后多少，再决定要不要拉平。`--ff-only` 是底线——`everything-claude-code` 是嵌入式 git clone，重写历史会让以后与上游的 diff 变得不可读。

```bash
cd everything-claude-code
git fetch origin
git rev-list --left-right --count HEAD...origin/main
```

`0	0` 表示已对齐；`0	N`（N>0）表示落后 N 个提交，需要 fast-forward：

```bash
git merge --ff-only origin/main
cat VERSION   # 看看版本号有没有跳
```

版本号跳变（例如从 `2.0.0-rc.1` 到 `2.0.0`）通常意味着新增语言轨道、命令族重构、或 docs/ 结构变动——比常规刷新要更仔细地扫一遍过期项。

### 步骤 2：量化变化

用四个目录的文件数对照上游自己公开的同步面。当前权威数字（已与 `docs/concepts/overview.md` 对齐）：**64 agents、261 skills、84 command shims、59 global slash commands**。

```bash
# 本仓库当前数量
for d in agents skills commands rules; do
  echo -n "$d: "; ls $d | wc -l
done

# 上游 README 头部声明的权威数量
cd everything-claude-code
grep -nE "64 agents|261 skills|84 legacy|59 slash" README.md
```

如果本地 `ls | wc -l` 与上游 README 数字对不上，说明上游可能刚改了表头；先看上游 diff，确认是否也要调整本仓库的引用。

### 步骤 3：扫描过期项

最容易过期的几类内容：

- 核心概念表的 64/261/84/59 数字（参考 [`docs/concepts/overview.md`](../concepts/overview.md)）。
- 顶层 `README.md` 中对命令、代理、技能数量的复述段落。
- "代理表 / 命令表 / 规则章节"里"语言专项"行——上游新增语言轨道时，本仓库最容易漏改。
- 快速参考表的"语言/任务 → 常见专项入口"表。
- Pages 站点 `docs/**/*.md` 里的同步计数——和顶层三份 `.md` 是两套内容，改顶层不会自动改站点。

精确扫描可以用：

```bash
grep -rnE "63 个|249 个|79 个|60 个|232 个|75 个" README.md ECC-COMMANDS-ZH.md docs/
grep -rnE "60 |232 |75 " README.md docs/
```

凡是命中这些过期数字的位置都要改。注意：**59 不要碰**——它指的是全局安装的 slash command 数，不是 `commands/` 下的文件数。

### 步骤 4：精准修改

只改事实过期部分，不重构、不重写、不重新组织表格。具体原则：

- 用 `Edit` 工具逐处改，每处改完独立验证。
- 不补"营销 / 前端"等已隐含覆盖的内容（它们已经在 skill 族 5 或快速参考表里）。
- 不自动 commit；改完先在本地构建验证、列改动清单。
- 同时改 `docs/` 下相关站点页，保持"顶层 README 与 Pages 站点计数一致"。

改完反向验证：

```bash
# 过期数字应为空
grep -rnE "63 个|249 个|79 个|60 个|232 个|75 个" README.md docs/
# 59 应保留
grep -rnE "59 个" README.md ECC-COMMANDS-ZH.md docs/
```

### 步骤 5：写回 gitlink 并提交

子目录里的工作树推进不会自动反映到主仓库的 gitlink 记录。必须在主仓库显式 `git add everything-claude-code`，让主仓库 commit 把新 SHA 记录下来。

```bash
cd ..
git add everything-claude-code
git status   # 应当只看到 everything-claude-code 这一项变更（gitlink 模式 160000）
```

如果 `git status` 列出了一堆 `everything-claude-code/` 下的具体文件，说明你忘了在子仓库里 commit 就回了主目录——回去 `git status` 看看。

提交时建议把"上游 SHA 旧→新 + 顶层/站点文档改动"分开写进 message：

```bash
git commit -m "chore(sync): fast-forward everything-claude-code to <new-sha>"
```

推送后，CI 会按 `.github/workflows/deploy-pages.yml` 的 `paths` 过滤决定是否重建 Pages——只改了 `everything-claude-code/` 不会触发 Pages 构建，只改了 `docs/**` 才会。

## 关键事实

!!! warning "易错点"

    - **`everything-claude-code/` 是 gitlink，不是普通子目录。** 主仓库的 git index 里它是 mode 160000 的 gitlink，且**没有 `.gitmodules` 映射**。子目录里工作树推进不会自动写回主仓库，必须在主仓库 `git add everything-claude-code`。
    - **84 与 59 是两个不同的数。** `commands/` 目录是 84 个命令文件（含 `legacy-command-shims/` 兼容别名）；`COMMANDS-QUICK-REF.md` 头部声明的是 59 个全局 slash commands。两者不可互换，看到"59"时不要改成"84"。
    - **只 fast-forward，不要 rebase 或 non-ff merge。** 重写历史会让以后与上游的 diff 不可读。
    - **Windows CRLF 警告是 `core.autocrlf` 的正常表现。** 子仓库 diff 里偶尔会出现这种警告，不要去改文件换行。
    - **不要修改 `everything-claude-code/README.zh-CN.md`。** 那是上游的中文 README，由上游维护；本仓库只维护顶层 `README.md` 和 `docs/` 下的教程。
    - **Pages 站点页 (`docs/**/*.md`) 与顶层三份 .md 是两套内容。** 改顶层不会自动同步站点；改站点也不会回写顶层。两者都要分别刷。

!!! danger "破坏性操作"

    - 永远不要在 `everything-claude-code/` 里 rebase、reset --hard、force push 到 main。
    - 不要在主仓库用 `git add -A` 一次性把 `everything-claude-code/` 下的具体文件带进来——那意味着把嵌入式 clone 当普通子目录用了，会污染主仓库历史。
    - 不要直接编辑 `LICENSE`、`everything-claude-code/README.zh-CN.md`、以及上游 README 里的事实声明。

## 故障排查

!!! tip "常见 case"

    - **`git fetch` 失败 / 网络超时**：在子仓库里 `git remote -v` 确认 `origin` 指向 `https://github.com/affaan-m/everything-claude-code.git`；必要时配代理或改用 SSH。
    - **子仓库 detached HEAD / 不在 main 分支**：`cd everything-claude-code && git checkout main && git status`；嵌入式 clone 一般应当稳定在 `main`。
    - **`git merge --ff-only` 报 "Not possible to fast-forward"**：上游历史被重写过。**停下来**，不要 force 同步；去上游仓库看是否发了带 force-push 的 release 通告，必要时手动调整。
    - **CI Pages 构建失败**：先本地 `python -m mkdocs build --strict` 复现；常见原因是 `docs/` 里新加的页忘了进 `mkdocs.yml` 的 `nav`。
    - **Pages 站点没更新**：检查 push 触发的 workflow run，确认 `paths` 过滤命中（`docs/**`、`mkdocs.yml`、`requirements.txt` 三者之一变化才会触发）。
    - **数字和上游对不上**：先 `cat everything-claude-code/VERSION` 和 `grep -nE "64 agents|261 skills|84 legacy" everything-claude-code/README.md`；权威数以上游 README 公开声明为准，本仓库的所有引用都要跟着它走。

## 相关参考

- [核心概念](../concepts/overview.md) —— 64/261/84/59 这几个数字的当前引用面。
- 仓库根目录 [`CLAUDE.md`](https://github.com/Chasen-Liao/Everything-claude-code-Doc/blob/main/CLAUDE.md) —— 仓库 AI 指南，包含 gitlink 与同步面说明。
- [`everything-claude-code/README.md`](https://github.com/affaan-m/everything-claude-code/blob/main/README.md) —— 数量权威来源。
- [`everything-claude-code/CHANGELOG.md`](https://github.com/affaan-m/everything-claude-code/blob/main/CHANGELOG.md) —— 上游版本历史。
- [`everything-claude-code/VERSION`](https://github.com/affaan-m/everything-claude-code/blob/main/VERSION) —— 当前上游版本号。
- [`everything-claude-code/COMMANDS-QUICK-REF.md`](https://github.com/affaan-m/everything-claude-code/blob/main/COMMANDS-QUICK-REF.md) —— 59 个全局 slash commands 的权威清单。

## 附录：手动验证命令清单

每条独立可粘贴，按需挑用：

```bash
# 子仓库落后量
cd everything-claude-code
git rev-list --left-right --count HEAD...origin/main

# 当前四个目录的文件数
for d in agents skills commands rules; do echo -n "$d: "; ls $d | wc -l; done

# 上游 README 公开声明的权威数
grep -nE "64 agents|261 skills|84 legacy|59 slash" README.md

# 当前上游版本
cat VERSION

# 顶层中文文档里的过期数字扫描
cd ..
grep -rnE "63 个|249 个|79 个|60 个|232 个|75 个" README.md ECC-COMMANDS-ZH.md docs/

# 保留 59 的反向验证
grep -rnE "59 个" README.md ECC-COMMANDS-ZH.md docs/

# 看主仓库 gitlink 是否记录了上游新 SHA
git ls-files --stage everything-claude-code

# 严格构建 MkDocs（Pages 本地等价物）
python -m mkdocs build --strict
```

# 阅读路线

按读者类型和时间预算挑一条路。每条路径都给了明确的画像、为什么选这条路，以及走到哪一步算结束。读完这条页面再切到其他教程入口会省不少时间。

## 路径 1：10 分钟新手指引

**读者画像**：完全没碰过 ECC，只想知道"这东西是什么、值不值得我花时间"。**时间预算**：10 分钟。**适用场景**：你刚 fork 这个仓库或点进站点，准备判断 ECC 是不是你要找的那类工作系统。

1. 读 [适合谁看](../getting-started/who-is-this-for.md)，看 ECC 是不是落在你的使用场景里。
2. 读 [ECC 是什么](../getting-started/what-is-ecc.md)，弄清本仓库（中文教程层）和 `everything-claude-code/`（上游同步层）各自负责什么。
3. 浏览 [核心概念](../concepts/overview.md) 表格：扫一眼 agents / skills / commands / rules / hooks 各自的数量与定位即可，不必细读。
4. 翻 [常见误解](../concepts/misconceptions.md) 4 条，对照自己脑子里"它就是命令包"那种直觉，把它先校准掉。
5. 想看真实目录就跳 [上游副本导航](../upstream-navigation/index.md) 第一组入口；想立刻看命令面就跳 [命令速查](../commands/index.md)。

**结束于**：本节 5 步走完你应该已经能向别人讲清"ECC 是什么 / 不什么 / 我用不用得上"。**接下来**：如果答案是"想用"，跳路径 2 或路径 3。

## 路径 2：30 分钟概念入门

**读者画像**：ECC 已经装好（或者你能照 `install.sh` / `install.ps1` 跑通），但分不清 agent、skill、command、rule、hook 各自做什么。**时间预算**：30 分钟。**适用场景**：你准备真正开始用 ECC，但不想一上来就被命令速查里几十个 `/xxx` 淹没。

1. 先用 10 分钟读 [核心概念 · 总览](../concepts/overview.md)，把那张组件表读透：64 agents / 261 skills / 84 commands / 59 global slash commands 是怎么对上的。
2. 用 10 分钟读 [Agent / Skill / Command 等组件](../concepts/agent-vs-skill-vs-command.md)，重点看"使用代理的方式"和"Skill 和 Slash Command 的关系"两节，这两个是最容易混淆的点。
3. 用 5 分钟过 [常见误解](../concepts/misconceptions.md)，把"skill 和 slash command 是一回事吗"这种典型误解清掉。
4. 用 5 分钟在 [按目录读上游副本](../upstream-navigation/by-directory.md) 里挑 3 个目录点开看真东西：建议先看 `agents/`、`skills/`、`commands/`，体会每个目录的"粒度感"。

**结束于**：你现在应该能用一句话说清"agent 是角色、skill 是工作流、command 是入口、rule 是约束、hook 是事件"之间的差别。**接下来**：去路径 3，把概念落到真实命令流上。

## 路径 3：60 分钟上手命令流

**读者画像**：概念已经清楚，想用 ECC 跑一个真实任务（新功能、bug 修复、代码审查、跨天继续等）。**时间预算**：60 分钟。**适用场景**：你今天就要拿 ECC 在自己项目上做一次完整开发循环。

1. 先用 10 分钟读 [实际工作流示例](../commands/workflow-examples.md) 六个例子：新功能 / 构建修复 / 质量把关 / 多代理并行 / 跨天继续 / 边做边沉淀。这六个例子的命令链就是你接下来要照搬的模板。
2. 用 10 分钟对照 [按场景选命令](../commands/by-scenario.md) 和 [最常用命令](../commands/most-used.md)，把示例里出现的命令锚到速查表上，记牢 `/plan` `/tdd` `/code-review` `/verify` `/build-fix` 这五个最小集合。
3. 如果你做的任务带语言偏好（Go / Python / TS / Rust / React …），花 10 分钟翻 [按语言选命令](../commands/by-language.md)，把通用命令换成本地语言专项版（例如 `/go-build` 代替 `/build-fix`、`/python-review` 代替 `/code-review`）。
4. 用 20 分钟自己挑一个真实小需求跑一遍上面的命令链：**先 `/plan`、再 `/tdd`、完成后 `/verify`、必要时 `/code-review`**。这是把纸面理解固化下来的唯一方式。
5. 收尾时跑 `/update-docs` 或回头看 [实际工作流示例](../commands/workflow-examples.md) 第 5、6 个例子，把"会话沉淀"和"跨天继续"两条链路也走通。

**结束于**：你已经完成过一次完整 ECC 循环（plan → tdd → verify → review），并且知道 `/save-session` `/resume-session` `/learn` 这类治理命令大致在什么时机用。**接下来**：去 [FAQ](../faq.md) 翻你今天踩过的具体问题；想把经验借给别的项目，参考路径 4 里的 [按目录读上游副本](../upstream-navigation/by-directory.md) 抄取规则与示例。

## 路径 4：维护者路线

**读者画像**：要更新这个中文镜像、修顶层三份中文文档、跟进上游版本变化，或者排查构建/链接问题。**时间预算**：90 分钟。**适用场景**：你被指派（或自愿）维护这个仓库，需要在不动上游 gitlink 内容的前提下把教程层和上游同步层对齐。

1. 先用 15 分钟读仓库根目录的 [`CLAUDE.md`](https://github.com/Chasen-Liao/Everything-claude-code-Doc/blob/main/CLAUDE.md)，把"`everything-claude-code/` 是 gitlink 而不是普通子目录"、"59 和 79 不要混用"、"只编辑顶层三份中文文档"这几条非显然事实记牢。
2. 用 20 分钟读 [与上游同步](../maintenance/sync-upstream.md)，按里面给的 fast-forward 流程跑一次：子仓库 `git fetch origin` → `git merge --ff-only origin/main` → 主仓库 `git add everything-claude-code`。先确认你能把上游推进并写回新 SHA。
3. 用 15 分钟读 [上游 CHANGELOG](https://github.com/affaan-m/ECC/blob/main/CHANGELOG.md)，看本次同步里 agents / skills / commands / rules 数量是否有变；如果变了，回到 [核心概念 · 总览](../concepts/overview.md) 和 [命令速查 · 总览](../commands/index.md) 对齐数字（64 / 261 / 84 / 59 是权威来源，不要改）。
4. 用 20 分钟做一次全站巡检：跑 `mkdocs build --strict`，按警告去修内部链接、缺失引用、路径形式。编辑 `docs/` 时只允许"站内相对路径"或"上游 GitHub URL"两种形态，禁止 `everything-claude-code/...` 形态的相对路径（这条在 `CLAUDE.md` 的 Pages 站点维护一节写明）。
5. 用 20 分钟做发布前复核：检查 [FAQ](../faq.md)、[快速开始](../getting-started/quickstart.md)、[阅读路线](../routes/index.md)（即本页）三处是否还有与上游漂移的措辞或死链，再决定是否发版。

**结束于**：你完成了一次上游同步 + 教程层对齐 + `mkdocs build --strict` 干净通过，并知道下次维护时该从仓库 `CLAUDE.md` + [与上游同步](../maintenance/sync-upstream.md) 这两处开始。**接下来**：把这次发现写进 commit message；如果上游引入了新语言轨道或新命令族，按 `CLAUDE.md` 的"边界"一节只改顶层中文文档、不动 gitlink 内任何文件。

---

## 选不出来了？

按下面这个简单规则二选一：

- 你目前只想判断"要不要用 ECC" → 走路径 1。
- 你已经决定要用 ECC → 跳过路径 1，直接看路径 2 或路径 3（看你是要补概念还是要跑命令）。
- 你被叫去维护这个仓库 → 不管前面，走路径 4。

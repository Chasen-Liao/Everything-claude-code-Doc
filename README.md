# Everything Claude Code 中文教程仓库

> 这是一个面向 **Everything Claude Code / ECC** 的中文教程型 GitHub 仓库，用来帮助你更快理解它的能力边界、目录结构、典型工作流和使用入口。
> 上游项目当前仓库名：<https://github.com/affaan-m/ECC>
> 历史仓库名 / 旧链接来源：`everything-claude-code`

---

## 这份仓库是什么 / 不是什么

这是一个**中文教程型仓库**，目标不是完整复制上游说明，而是把 ECC 这套体系讲清楚，方便中文用户快速建立整体认知，并按教程路线逐步上手。

它**不是**上游项目的完整官方文档站，也不是只包含少量配置片段的示例仓库。当前这个仓库主要包含四部分：

- 顶层的这份 [`README.md`](README.md)：中文总教程与导读入口。
- [`ECC-COMMANDS-ZH.md`](ECC-COMMANDS-ZH.md)：中文命令速查。
- [`ECC-NAVIGATION-ZH.md`](ECC-NAVIGATION-ZH.md)：本地上游副本导航索引。
- 本地同步的上游副本：[`everything-claude-code/`](everything-claude-code/)。

如果你要快速理解 ECC 的设计思路，看这套中文文档就够了；如果你要核对原始定义、目录细节、脚本实现、实际 skill/agent 内容，再进入上游仓库或本地同步副本。

---

## 快速开始

如果你是第一次接触 ECC，建议按下面顺序阅读：

1. 先看下文的“核心概念”，理解 **Agent / Skill / Command / Rule / Hook / Harness** 这些层次分别是什么。
2. 再看下文的“推荐教程路线”，按你的目标选择阅读顺序。
3. 然后看 [`ECC-COMMANDS-ZH.md`](ECC-COMMANDS-ZH.md) 和 [`ECC-NAVIGATION-ZH.md`](ECC-NAVIGATION-ZH.md) 建立命令与目录的整体地图。
4. 最后根据需要进入上游同步副本 [`everything-claude-code/`](everything-claude-code/) 核对原始定义和实现细节。

如果你更习惯直接读原文，可以从这些入口开始：

- 上游项目主页：<https://github.com/affaan-m/ECC>
- 上游英文 README：<https://github.com/affaan-m/ECC/blob/main/README.md>
- 上游中文 README：<https://github.com/affaan-m/ECC/blob/main/README.zh-CN.md>
- 上游命令速查：<https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md>
- 上游长文指南：<https://github.com/affaan-m/ECC/blob/main/the-longform-guide.md>
- 上游短文指南：<https://github.com/affaan-m/ECC/blob/main/the-shortform-guide.md>
- 上游安全指南：<https://github.com/affaan-m/ECC/blob/main/the-security-guide.md>
- 上游故障排查：<https://github.com/affaan-m/ECC/blob/main/docs/TROUBLESHOOTING.md>

---

## 适合谁看

这份仓库尤其适合下面几类读者：

- 想快速理解 ECC 是什么、但不想一开始就扎进上游大仓库的人。
- 已经在用 Claude Code、Cursor、Codex 或其他 agent harness，想参考 ECC 工作流设计的人。
- 想把 agents、skills、rules、hooks 这一整套方法借到自己项目里的人。
- 想先看中文教程，再决定是否深入上游原始文档的人。

如果你只是想看上游最权威定义，或者要逐文件核对实现细节，那就应该直接进入 [`everything-claude-code/`](everything-claude-code/) 或上游官方仓库。

---

## 你会在这里得到什么

读完这份仓库，你通常会得到三样东西：

1. 对 ECC 整体结构的中文理解，而不是零散命令列表。
2. 一条更省时间的阅读路径，知道应该先看哪几个入口文件。
3. 一套把 ECC 拆成 agent、skill、command、rule、hook、harness 来理解的方法。

如果你想进一步对照原始定义，可以把本仓库和 [`everything-claude-code/`](everything-claude-code/) 一起看：前者负责讲清楚，后者负责给原文和实现。

---

## 常见误解

### 1. ECC 只是 Claude Code 的命令包吗？

不是。现在的 ECC 更接近一套完整的 **agent harness performance system**，除了命令，还包括 agents、skills、rules、hooks、上下文管理、学习沉淀和跨平台适配。

### 2. skill 和 slash command 是一回事吗？

不是。skill 是能力定义或工作流定义，slash command 是触发入口。某个 skill 存在，并不等于一定有同名全局命令。

### 3. 这个仓库是上游官方文档吗？

不是。本仓库是中文教程和导读层，方便快速理解；权威定义仍以上游仓库和本地同步副本为准。

### 4. 我是不是必须把整个 ECC 全量照搬？

不一定。很多人更适合按需吸收，例如只借 rules、只借 commands、或者只参考 agents / hooks 的组织方式。

---

## 和上游仓库的关系

你可以把这两个部分理解成不同层级：

- [README.md](README.md)：中文教程层，负责解释、串联、给出阅读路径。
- [`everything-claude-code/`](everything-claude-code/)：上游同步层，负责提供原始文档、真实目录和实现细节。

如果你想快速学会怎么用，优先看本仓库顶层中文文档；如果你想核对最新定义、逐项确认命令、查看真实 skill 或 hook 内容，再进入 [`everything-claude-code/`](everything-claude-code/)。

---

## FAQ

### 我应该先看哪个文件？

如果你是第一次接触 ECC，先看本页，再看 [ECC-COMMANDS-ZH.md](ECC-COMMANDS-ZH.md)，然后看 [ECC-NAVIGATION-ZH.md](ECC-NAVIGATION-ZH.md)。

### 我只想知道有哪些命令怎么办？

先看 [ECC-COMMANDS-ZH.md](ECC-COMMANDS-ZH.md)，再按需要对照 [`everything-claude-code/COMMANDS-QUICK-REF.md`](everything-claude-code/COMMANDS-QUICK-REF.md)。

### 我只想知道上游副本里该从哪里读起？

直接看 [ECC-NAVIGATION-ZH.md](ECC-NAVIGATION-ZH.md)，它就是为这个目的准备的。

### 我想把 ECC 的一部分抄到自己的项目里？

优先看本页的“推荐教程路线”里的“路线 4”，再进入 [`everything-claude-code/examples/`](everything-claude-code/examples/) 和 [`everything-claude-code/rules/README.md`](everything-claude-code/rules/README.md)。

---

## 仓库状态与原始来源

为了便于对照，这里说明一下当前仓库与上游的关系：

- **本仓库**：中文教程、中文整理、适合快速上手和建立整体认知。
- **本地同步副本**：[`everything-claude-code/`](everything-claude-code/)，用于在本地直接查上游真实内容。
- **上游官方仓库**：`affaan-m/ECC`，这是判断最新结构与最新能力的权威来源。

当前本地同步副本已成功同步到上游仓库，可直接查看：[`everything-claude-code/`](everything-claude-code/)。

---

## 目录

1. 这份仓库是什么 / 不是什么
2. 快速开始
3. 仓库状态与原始来源
4. 核心概念
5. 现在的 ECC 和早期版本有什么不同
6. 推荐教程路线
7. 推荐阅读入口
8. 代理（Agents）
9. 技能（Skills）
10. 命令（Commands）
11. 规则（Rules）
12. 钩子（Hooks）
13. 实际工作流示例
14. 快速参考表

---

## 核心概念

ECC 现在已经不只是“Claude Code 的一套配置”，更接近一个**AI agent harness performance system**：它把代理、技能、命令、规则、钩子、安装清单和跨平台适配整合成一套可复用工作系统。

> 说明：下面的数量与描述基于当前已同步的上游 `affaan-m/ECC` 本地副本，以及上游 README 中公开说明的当前表面。版本继续演进时，数量可能变化。

| 组件 | 当前规模 | 作用 |
| ------ | ------ | ------ |
| **代理（Agents）** | 60 个代理文件 | 把复杂任务委派给专门角色，例如规划、审查、构建修复、文档更新 |
| **技能（Skills）** | 232 个技能目录 | 封装领域知识、工作流和可复用模式 |
| **命令（Commands）** | 75 个命令文件 | 作为 slash command 或命令入口调用工作流 |
| **全局 slash commands** | 59 个 | 当前安装表面里最常用的全局命令集合 |
| **规则（Rules）** | 多语言规则体系 | 约束编码风格、测试、安全和项目行为 |
| **钩子（Hooks）** | hooks 清单与运行时组件 | 在工具调用前后、会话开始结束等时机自动执行 |
| **跨平台适配** | 多个 harness / IDE 目录 | 让同一套体系能在 Claude Code、Codex、Cursor、OpenCode、Gemini 等环境中复用 |

### 这些概念如何区分

- **Agent**：子代理，适合复杂、专业化、需要独立上下文的任务。
- **Skill**：能力定义或工作流定义，本质是可复用经验包。
- **Command**：触发入口，通常对应 `/plan`、`/tdd` 这类命令。
- **Rule**：始终生效的行为约束，例如安全要求、测试要求、编码习惯。
- **Hook**：自动化脚本，在特定事件时触发。
- **Harness**：Claude Code、Codex、Cursor、OpenCode、Gemini 等“承载 AI agent 的运行环境”。ECC 现在强调的是**跨 harness 复用**，而不是只服务单一工具。

---

## 现在的 ECC 和早期版本有什么不同

如果你以前看过 `everything-claude-code` 时期的介绍，最容易混淆的是：**ECC 现在的范围大了很多**。

早期常见理解是：

- 面向 Claude Code 的配置集合。
- 重点是 agents、skills、commands、rules、hooks。
- 常见命令数量较少，语言覆盖较集中。

当前 ECC 的变化主要有这些：

1. **仓库定位升级**
   - 不再只是配置集合，而是“agent harness performance system”。
   - 不只关注提示词和命令，还覆盖上下文优化、会话恢复、持续学习、安全审计、评估与编排。

2. **跨平台支持明显增强**
   - 不再局限于 Claude Code。
   - 现在仓库里可以直接看到 `.cursor/`、`.codex/`、`.opencode/`、`.gemini/`、`.zed/`、`.kiro/`、`.trae/` 等目录或适配层。

3. **命令面显著扩大**
   - 已确认存在 75 个命令文件。
   - 上游命令速查中明确写了 **59 个全局 slash commands**。
   - 新增了质量门禁、上下文预算、循环执行、多模型协作、文档查询、harness 审计等能力。

4. **文档体系更完整**
   - 除主 README 外，还有长文指南、短文指南、安全指南、故障排查、架构说明、安装设计、Hermes 相关文档等。

5. **ECC 2.0 / Hermes 方向出现**
   - 上游文档里已经出现 `ecc2/`、Hermes setup、operator workflow 等新方向。
   - 这说明 ECC 不再只是“命令包”，而是在往更完整的操作层与控制层演进。

---

## 推荐教程路线

如果你希望这个仓库更像一套教程来读，而不是一篇长说明，建议按目标选择：

### 路线 1：第一次接触 ECC

1. 先看本页的“核心概念”。
2. 再看 [`ECC-COMMANDS-ZH.md`](ECC-COMMANDS-ZH.md) 了解最常用命令。
3. 再看 [`ECC-NAVIGATION-ZH.md`](ECC-NAVIGATION-ZH.md) 建立整个上游副本的目录地图。
4. 最后进入 [`everything-claude-code/README.md`](everything-claude-code/README.md) 对照原始定义。

### 路线 2：想尽快学会怎么用

1. [`ECC-COMMANDS-ZH.md`](ECC-COMMANDS-ZH.md)
2. 本页的“实际工作流示例”
3. [`everything-claude-code/COMMANDS-QUICK-REF.md`](everything-claude-code/COMMANDS-QUICK-REF.md)
4. [`everything-claude-code/the-shortform-guide.md`](everything-claude-code/the-shortform-guide.md)

### 路线 3：想研究完整系统

1. [`everything-claude-code/README.md`](everything-claude-code/README.md)
2. [`everything-claude-code/the-longform-guide.md`](everything-claude-code/the-longform-guide.md)
3. [`everything-claude-code/agents/`](everything-claude-code/agents/)
4. [`everything-claude-code/skills/`](everything-claude-code/skills/)
5. [`everything-claude-code/rules/`](everything-claude-code/rules/)
6. [`everything-claude-code/hooks/`](everything-claude-code/hooks/)

### 路线 4：想抄一套到自己的项目里

1. [`everything-claude-code/examples/`](everything-claude-code/examples/)
2. [`everything-claude-code/rules/README.md`](everything-claude-code/rules/README.md)
3. [`everything-claude-code/install.sh`](everything-claude-code/install.sh)
4. [`everything-claude-code/install.ps1`](everything-claude-code/install.ps1)
5. [`everything-claude-code/docs/SELECTIVE-INSTALL-ARCHITECTURE.md`](everything-claude-code/docs/SELECTIVE-INSTALL-ARCHITECTURE.md)

---

## 推荐阅读入口

按“你想解决什么问题”来选入口，通常会更高效。

### 1. 想先知道 ECC 是什么

- 上游英文 README：<https://github.com/affaan-m/ECC/blob/main/README.md>
- 上游中文 README：<https://github.com/affaan-m/ECC/blob/main/README.zh-CN.md>
- 本地同步副本入口：[`everything-claude-code/README.md`](everything-claude-code/README.md)

### 2. 想快速知道有哪些命令

- 命令速查：<https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md>
- 本地同步副本：[`everything-claude-code/COMMANDS-QUICK-REF.md`](everything-claude-code/COMMANDS-QUICK-REF.md)
- 命令目录：<https://github.com/affaan-m/ECC/tree/main/commands>

### 3. 想理解背后的方法论

- 长文指南：<https://github.com/affaan-m/ECC/blob/main/the-longform-guide.md>
- 短文指南：<https://github.com/affaan-m/ECC/blob/main/the-shortform-guide.md>
- 安全指南：<https://github.com/affaan-m/ECC/blob/main/the-security-guide.md>

### 4. 想解决安装或使用问题

- 故障排查：<https://github.com/affaan-m/ECC/blob/main/docs/TROUBLESHOOTING.md>
- 选择性安装设计：<https://github.com/affaan-m/ECC/blob/main/docs/SELECTIVE-INSTALL-ARCHITECTURE.md>
- Hermes 安装：<https://github.com/affaan-m/ECC/blob/main/docs/HERMES-SETUP.md>

### 5. 想查原始定义

- Agents：<https://github.com/affaan-m/ECC/tree/main/agents>
- Skills：<https://github.com/affaan-m/ECC/tree/main/skills>
- Rules：<https://github.com/affaan-m/ECC/tree/main/rules>
- Hooks：<https://github.com/affaan-m/ECC/tree/main/hooks>
- Docs：<https://github.com/affaan-m/ECC/tree/main/docs>

---

## 代理（Agents）

代理是专业化子代理，用来把复杂任务拆给更擅长某一领域的角色。你可以把它理解为“带专长的协作同事”。

原始目录：<https://github.com/affaan-m/ECC/tree/main/agents>

### 典型代理类型

以下是当前 ECC 中很有代表性的一组代理：

| 代理名称 | 作用 |
| ---------- | ---------- |
| `planner` | 分析需求、识别风险、输出实施计划 |
| `architect` | 做架构设计、边界划分和权衡 |
| `tdd-guide` | 强制以测试优先的方式推进开发 |
| `code-reviewer` | 通用代码质量、安全与可维护性审查 |
| `security-reviewer` | 从漏洞和风险角度审查改动 |
| `build-error-resolver` | 定位并修复构建或类型错误 |
| `e2e-runner` | 生成并执行 E2E 测试 |
| `doc-updater` | 更新文档、校正文档与实现的一致性 |
| `docs-lookup` | 查文档、API、配置说明 |
| `go-reviewer` / `python-reviewer` / `java-reviewer` / `typescript-reviewer` | 语言专项代码审查 |
| `go-build-resolver` / `cpp-build-resolver` / `java-build-resolver` / `kotlin-build-resolver` | 语言专项构建修复 |
| `loop-operator` | 循环式任务执行与持续操作 |
| `harness-optimizer` | 优化 agent harness 的配置与使用方式 |

### 使用代理的方式

代理既可以被系统自动调度，也可以作为明确的子代理调用。常见理解方式是：

```text
用户目标很大
→ 先交给 planner / architect 明确路线
→ 开发中交给 tdd-guide / build resolver / reviewer
→ 完成前交给 code-reviewer / security-reviewer / doc-updater
```

如果你以前只把 ECC 当成“slash command 集合”，这里是一个重要升级点：**现在的 ECC 很强调子代理协作，而不是单条命令孤立执行。**

---

## 技能（Skills）

技能是工作流定义和领域知识的集合。和 agent 相比，skill 更像“可复用方法论”或“某类任务的标准操作手册”。

原始目录：<https://github.com/affaan-m/ECC/tree/main/skills>

### 常见技能族

ECC 的 skill 已经很多，不适合在一篇导读里完整罗列。更好的理解方式是按技能族来看：

#### 1. 测试与验证

- `tdd-workflow`
- `golang-testing`
- `django-tdd`
- `springboot-tdd`
- `e2e-testing`
- `test-coverage` 相关能力

这类技能负责把“先写失败测试、再实现、再验证覆盖率”的流程标准化。

#### 2. 语言与框架模式

- `golang-patterns`
- `python-patterns`
- `frontend-patterns`
- `backend-patterns`
- `django-patterns`
- `springboot-patterns`
- `postgres-patterns`
- `jpa-patterns`
- `nestjs-patterns`

这类技能更像“某语言 / 某框架下的经验模板”。

#### 3. 安全与审计

- `security-review`
- `security-scan`
- 框架安全类 skill，例如 `django-security`、`springboot-security`

这类技能帮助你从输入校验、配置暴露、认证授权、依赖风险等角度审视项目。

#### 4. 学习与沉淀

- `continuous-learning-v2`
- `iterative-retrieval`
- `strategic-compact`
- `skill-create`

这部分是 ECC 比较有代表性的特色：它不只想“帮你写完一次”，还想把会话中的模式沉淀成以后能复用的能力。

#### 5. 运营 / 文档 / 研究型能力

随着 ECC 扩展，skills 已经不局限于编码本身，还出现了：

- 文档查询与更新
- 市场研究与内容生产
- 运营类工作流
- 视频与发布内容生成
- workspace / social / billing / project flow 等扩展面

这也是为什么现在更适合把 ECC 理解成“工作系统”而不是“代码助手配置包”。

### Skill 和 Slash Command 的关系

这里要特别区分两件事：

- **Skill**：能力定义，本质上是可复用工作流或知识块。
- **Slash Command**：命令入口，是否存在、是否全局安装、是否带命名空间，取决于你的安装方式和当前 harness。

也就是说，不是每个 skill 都会天然对应一个 `/xxx` 命令。你看到某个 skill 存在，并不等于一定能直接用同名命令调用。

---

## 命令（Commands）

命令是最常见的使用入口。当前上游已确认存在 **75 个命令文件**，其中命令速查中明确列出 **59 个全局 slash commands**。

原始目录：<https://github.com/affaan-m/ECC/tree/main/commands>

### 最核心的一组命令

| 命令 | 作用 |
| ------ | ------ |
| `/plan` | 先澄清需求、识别风险、给出实现计划 |
| `/tdd` | 启动测试驱动开发流程 |
| `/code-review` | 做完整代码审查 |
| `/build-fix` | 修复构建错误 |
| `/verify` | 跑验证循环：构建、测试、类型检查等 |
| `/e2e` | 生成并执行端到端测试 |
| `/quality-gate` | 用项目标准做一次质量闸门检查 |

### 现在新增或更值得关注的命令族

#### 1. 测试与覆盖率

- `/test-coverage`
- `/go-test`
- `/kotlin-test`
- `/rust-test`
- `/cpp-test`

#### 2. 语言专项审查与构建修复

- `/python-review`
- `/go-review`
- `/kotlin-review`
- `/rust-review`
- `/cpp-review`
- `/go-build`
- `/kotlin-build`
- `/rust-build`
- `/cpp-build`
- `/gradle-build`

#### 3. 多模型 / 多代理协作

- `/multi-plan`
- `/multi-execute`
- `/multi-workflow`
- `/multi-backend`
- `/multi-frontend`
- `/orchestrate`
- `/devfleet`

#### 4. 会话管理与上下文控制

- `/save-session`
- `/resume-session`
- `/sessions`
- `/checkpoint`
- `/aside`
- `/context-budget`

#### 5. 学习、规则与治理

- `/learn`
- `/learn-eval`
- `/evolve`
- `/promote`
- `/instinct-status`
- `/instinct-export`
- `/instinct-import`
- `/skill-create`
- `/skill-health`
- `/rules-distill`

#### 6. 文档、研究与基础设施

- `/docs`
- `/update-docs`
- `/update-codemaps`
- `/projects`
- `/harness-audit`
- `/eval`
- `/model-route`
- `/loop-start`
- `/loop-status`
- `/claw`
- `/pm2`
- `/setup-pm`

### 如何理解命令的演进

旧版介绍通常把命令理解为“快捷方式”。这个说法没错，但已经不够了。现在的 ECC 命令更像：

- 某个 skill 的入口；
- 某组 agent 编排的入口；
- 某个跨会话 / 跨模型流程的入口；
- 某类工程治理动作的入口。

所以 `/plan`、`/verify`、`/harness-audit` 这类命令，背后不只是单次执行动作，而是完整工作流。

---

## 规则（Rules）

规则是始终遵循的编码与工作约束，用来把“项目偏好”和“最低安全线”固化下来。

原始目录：<https://github.com/affaan-m/ECC/tree/main/rules>

### 规则体系怎么理解

ECC 的规则不再只是单文件集合，而是**多语言、可选择安装、按主题拆分**的体系。你通常会看到：

- `common/`：通用规则
- 各语言目录：例如 TypeScript、Python、Go、Rust、Java、C++ 等
- 每种语言下再拆成 coding style、testing、patterns、security、hooks 等主题

### 规则重点通常包括

1. **编码风格**
   - 倾向清晰、可维护、不过度抽象。
   - 让生成代码更贴近项目约定。

2. **测试要求**
   - 强调 TDD、覆盖率、验证循环。
   - 不是“代码写完后再补一点测试”，而是把测试前移到开发流程中。

3. **安全要求**
   - 防止 secrets 泄露。
   - 校验用户输入。
   - 避免 SQL 注入、XSS、认证配置错误等问题。

4. **Hook 约束**
   - 控制何时自动运行格式化、类型检查、会话持久化、学习提取等行为。

5. **项目工作流**
   - 规范提交、审查、验证和文档更新方式。

如果你只想“借用 ECC 的一部分能力”，rules 往往是最适合按需摘取的部分之一。

---

## 钩子（Hooks）

钩子是基于事件触发的自动化脚本，是 ECC 很重要的一层，因为很多“会自己发生的行为”其实都来自 hooks。

原始目录：<https://github.com/affaan-m/ECC/tree/main/hooks>

### 常见触发时机

| 触发器 | 执行时机 |
| -------- | ---------- |
| `PreToolUse` | 工具执行前 |
| `PostToolUse` | 工具执行后 |
| `PreCompact` | 上下文压缩前 |
| `SessionStart` | 会话开始时 |
| `SessionEnd` | 会话结束时 |
| `Stop` | 会话停止或中止时 |

### 钩子主要解决什么问题

- 自动格式化或检查改动
- 提醒上下文预算与压缩时机
- 保存 / 恢复会话信息
- 从当前会话提取可复用模式
- 对高风险命令做额外检查
- 让不同 harness 的行为尽量一致

### 当前 ECC 的 hook 特点

较新的 ECC 版本更强调：

- 脚本化 hook，而不是脆弱的一行命令；
- 通过运行时参数控制启用级别；
- 兼容不同平台与不同 harness；
- 把记忆持久化、学习提取和流程提醒纳入自动化链路。

---

## 实际工作流示例

### 1. 新功能开发

```text
用户请求：实现一个用户认证系统

1. /plan
   → 先澄清需求、识别风险、生成实施路线

2. /tdd
   → 先写失败测试，再实现功能，再通过测试

3. /code-review
   → 检查可维护性、安全性与回归风险

4. /verify
   → 跑完整验证循环

5. /update-docs
   → 如果改动影响用户使用方式或项目结构，同步文档
```

### 2. 修复构建或类型错误

```text
项目突然无法构建

/build-fix
→ 自动识别语言与问题类型
→ 如有需要再切到 /go-build、/rust-build、/gradle-build 等专项命令
→ 修完后用 /verify 做收尾
```

### 3. 需要更严格的代码质量把关

```text
功能已经能跑，但你担心质量与风险

/code-review
/security-review 或 /security-scan
/quality-gate
```

这三类入口组合起来，比较接近“提交前 final pass”。

### 4. 多模型 / 多代理并行协作

```text
需求较大、任务面很多

/multi-plan
→ 从多个模型或多个视角拆方案

/multi-execute 或 /multi-workflow
→ 并行推进不同部分

/orchestrate 或 /devfleet
→ 在更复杂的场景下统一协调多个 agent
```

### 5. 会话跨天继续

```text
今天先做到这里
/save-session
/checkpoint

明天继续
/resume-session
```

### 6. 边做边沉淀经验

```text
/learn
/learn-eval
/evolve
```

这个链路体现了 ECC 的一个核心思路：把一次成功会话里的模式，逐步转化为以后能复用的能力资产。

---

## 快速参考表

### 场景 → 推荐入口

| 场景 | 推荐命令 / 文档 |
| ------ | -------------- |
| 开始新功能 | `/plan` |
| 按测试优先推进开发 | `/tdd` |
| E2E 测试 | `/e2e` |
| 代码审查 | `/code-review` |
| 安全检查 | `/security-scan`、`/security-review` |
| 修构建错误 | `/build-fix` |
| 语言专项修构建 | `/go-build`、`/rust-build`、`/cpp-build`、`/gradle-build` |
| 看覆盖率缺口 | `/test-coverage` |
| 发布前做质量闸门 | `/quality-gate` |
| 保存 / 恢复会话 | `/save-session`、`/resume-session` |
| 控制上下文预算 | `/context-budget` |
| 学习与沉淀模式 | `/learn-eval`、`/evolve` |
| 多代理并行 | `/multi-plan`、`/multi-execute`、`/orchestrate` |
| 查当前库/API 文档 | `/docs` |
| 更新项目文档 | `/update-docs` |
| 查故障排查 | `docs/TROUBLESHOOTING.md` |
| 理解整体方法论 | `the-shortform-guide.md`、`the-longform-guide.md` |

### 语言 / 任务 → 常见专项入口

| 方向 | 典型入口 |
| ------ | ------ |
| Python | `/python-review`、`python-patterns` |
| Go | `/go-review`、`/go-test`、`/go-build` |
| Kotlin | `/kotlin-review`、`/kotlin-test`、`/kotlin-build` |
| Rust | `/rust-review`、`/rust-test`、`/rust-build` |
| C++ | `/cpp-review`、`/cpp-test`、`/cpp-build` |
| Django | `django-patterns`、`django-tdd`、`django-security`、`django-verification` |
| Spring Boot | `springboot-patterns`、`springboot-tdd`、`springboot-security`、`springboot-verification` |
| 数据库 | `postgres-patterns`、`database-reviewer` |
| 前端 | `frontend-patterns`、`/e2e` |

---

## 关键原则

1. **先澄清再动手**：复杂需求先 `/plan`，不要一上来就改代码。
2. **测试优先**：能走 TDD 就优先 `/tdd`。
3. **验证闭环**：开发完成后不要只看“能跑”，还要 `/verify` 或 `/quality-gate`。
4. **安全前置**：任何涉及用户输入、认证、依赖、配置的改动，都应该经过安全视角检查。
5. **把经验沉淀下来**：ECC 的特色不只是帮你完成任务，而是把成功模式转成可复用资产。
6. **把它理解为系统，不只是命令包**：Agent、Skill、Command、Rule、Hook、Harness 之间是联动的。

---

## 更多信息

- 上游项目 GitHub：<https://github.com/affaan-m/ECC>
- 当前说明仓库：<https://github.com/Chasen-Liao/Everything-claude-code-Doc>
- 当前同步到本地的上游副本：[`everything-claude-code/`](everything-claude-code/)
- 上游英文 README：<https://github.com/affaan-m/ECC/blob/main/README.md>
- 上游中文 README：<https://github.com/affaan-m/ECC/blob/main/README.zh-CN.md>
- Agents 原始目录：<https://github.com/affaan-m/ECC/tree/main/agents>
- Skills 原始目录：<https://github.com/affaan-m/ECC/tree/main/skills>
- Rules 原始目录：<https://github.com/affaan-m/ECC/tree/main/rules>
- Hooks 原始目录：<https://github.com/affaan-m/ECC/tree/main/hooks>
- Commands 原始目录：<https://github.com/affaan-m/ECC/tree/main/commands>
- 命令速查：<https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md>
- 长文指南：<https://github.com/affaan-m/ECC/blob/main/the-longform-guide.md>
- 短文指南：<https://github.com/affaan-m/ECC/blob/main/the-shortform-guide.md>
- 安全指南：<https://github.com/affaan-m/ECC/blob/main/the-security-guide.md>
- 故障排查：<https://github.com/affaan-m/ECC/blob/main/docs/TROUBLESHOOTING.md>
- Hermes 安装：<https://github.com/affaan-m/ECC/blob/main/docs/HERMES-SETUP.md>

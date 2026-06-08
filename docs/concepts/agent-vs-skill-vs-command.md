# Agent / Skill / Command 等组件

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
| `go-reviewer` / `python-reviewer` / `java-reviewer` / `typescript-reviewer` / `react-reviewer` | 语言专项代码审查 |
| `go-build-resolver` / `cpp-build-resolver` / `java-build-resolver` / `kotlin-build-resolver` / `react-build-resolver` | 语言专项构建修复 |
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

命令是最常见的使用入口。当前上游已确认存在 **84 个命令文件**（其中包括 `legacy-command-shims/` 下的兼容别名），命令速查中明确列出 **59 个全局 slash commands**。

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
- `/react-test`

#### 2. 语言专项审查与构建修复

- `/python-review`
- `/go-review`
- `/kotlin-review`
- `/rust-review`
- `/cpp-review`
- `/react-review`
- `/go-build`
- `/kotlin-build`
- `/rust-build`
- `/cpp-build`
- `/gradle-build`
- `/react-build`

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
- 各语言目录：例如 TypeScript、Python、Go、Rust、Java、C++、React、Angular、Kotlin、Dart、Swift、Ruby、PHP、Perl、C#、F# 等
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

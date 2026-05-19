# ECC 本地副本导航索引

> 这个索引帮助你快速理解本仓库中的上游同步副本 [`everything-claude-code/`](everything-claude-code/) 应该从哪里读起。
> 如果你不想先在巨大的目录里到处找，这份索引会更高效。

---

## 先看哪里

### 我只想先知道 ECC 是什么

先看这几个：

- [`everything-claude-code/README.md`](everything-claude-code/README.md)
- [`everything-claude-code/README.zh-CN.md`](everything-claude-code/README.zh-CN.md)
- [`README.md`](README.md)

### 我只想知道有哪些命令

- [`everything-claude-code/COMMANDS-QUICK-REF.md`](everything-claude-code/COMMANDS-QUICK-REF.md)
- [`ECC-COMMANDS-ZH.md`](ECC-COMMANDS-ZH.md)
- [`everything-claude-code/commands/`](everything-claude-code/commands/)
- [`everything-claude-code/legacy-command-shims/`](everything-claude-code/legacy-command-shims/)

### 我只想知道有哪些 agents / skills

- [`everything-claude-code/agents/`](everything-claude-code/agents/)
- [`everything-claude-code/skills/`](everything-claude-code/skills/)
- [`everything-claude-code/AGENTS.md`](everything-claude-code/AGENTS.md)

### 我想解决安装或使用问题

- [`everything-claude-code/docs/TROUBLESHOOTING.md`](everything-claude-code/docs/TROUBLESHOOTING.md)
- [`everything-claude-code/docs/HERMES-SETUP.md`](everything-claude-code/docs/HERMES-SETUP.md)
- [`everything-claude-code/install.sh`](everything-claude-code/install.sh)
- [`everything-claude-code/install.ps1`](everything-claude-code/install.ps1)

### 我想理解方法论和设计思路

- [`everything-claude-code/the-shortform-guide.md`](everything-claude-code/the-shortform-guide.md)
- [`everything-claude-code/the-longform-guide.md`](everything-claude-code/the-longform-guide.md)
- [`everything-claude-code/the-security-guide.md`](everything-claude-code/the-security-guide.md)
- [`everything-claude-code/docs/architecture/`](everything-claude-code/docs/architecture/)

---

## 按目录理解这个上游副本

### 核心入口

| 路径 | 用途 |
| ------ | ------ |
| [`everything-claude-code/README.md`](everything-claude-code/README.md) | 上游英文主入口 |
| [`everything-claude-code/README.zh-CN.md`](everything-claude-code/README.zh-CN.md) | 上游中文主入口 |
| [`everything-claude-code/CHANGELOG.md`](everything-claude-code/CHANGELOG.md) | 版本更新记录 |
| [`everything-claude-code/COMMANDS-QUICK-REF.md`](everything-claude-code/COMMANDS-QUICK-REF.md) | 命令速查 |
| [`everything-claude-code/TROUBLESHOOTING.md`](everything-claude-code/TROUBLESHOOTING.md) | 顶层故障排查入口 |
| [`everything-claude-code/SECURITY.md`](everything-claude-code/SECURITY.md) | 安全相关说明 |
| [`everything-claude-code/RULES.md`](everything-claude-code/RULES.md) | 规则体系总览 |
| [`everything-claude-code/AGENTS.md`](everything-claude-code/AGENTS.md) | agent 目录总览 |

### 核心能力目录

| 路径 | 看什么 |
| ------ | ------ |
| [`everything-claude-code/agents/`](everything-claude-code/agents/) | 子代理定义 |
| [`everything-claude-code/skills/`](everything-claude-code/skills/) | skills / 工作流定义 |
| [`everything-claude-code/commands/`](everything-claude-code/commands/) | 维护中的命令入口 |
| [`everything-claude-code/legacy-command-shims/`](everything-claude-code/legacy-command-shims/) | 兼容旧命令的 shim |
| [`everything-claude-code/rules/`](everything-claude-code/rules/) | 通用规则与语言规则 |
| [`everything-claude-code/hooks/`](everything-claude-code/hooks/) | hooks 配置与说明 |
| [`everything-claude-code/scripts/`](everything-claude-code/scripts/) | 跨平台脚本与 hooks 实现 |
| [`everything-claude-code/tests/`](everything-claude-code/tests/) | 脚本与 hooks 的测试 |

### 支撑性目录

| 路径 | 看什么 |
| ------ | ------ |
| [`everything-claude-code/docs/`](everything-claude-code/docs/) | 补充文档、架构说明、安装设计、平台指南 |
| [`everything-claude-code/examples/`](everything-claude-code/examples/) | 示例 CLAUDE.md 和项目样板 |
| [`everything-claude-code/contexts/`](everything-claude-code/contexts/) | 注入式上下文模板 |
| [`everything-claude-code/mcp-configs/`](everything-claude-code/mcp-configs/) | MCP 服务器配置 |
| [`everything-claude-code/manifests/`](everything-claude-code/manifests/) | 安装与组件清单 |
| [`everything-claude-code/plugins/`](everything-claude-code/plugins/) | 插件相关内容 |
| [`everything-claude-code/schemas/`](everything-claude-code/schemas/) | 配置或数据结构 schema |
| [`everything-claude-code/src/`](everything-claude-code/src/) | 程序源码与控制层实现 |
| [`everything-claude-code/ecc2/`](everything-claude-code/ecc2/) | ECC 2.0 / 控制层相关原型 |

### 跨 harness / 平台适配目录

这些目录的存在说明 ECC 不再只服务 Claude Code：

- [`everything-claude-code/.claude/`](everything-claude-code/.claude/)
- [`everything-claude-code/.claude-plugin/`](everything-claude-code/.claude-plugin/)
- [`everything-claude-code/.cursor/`](everything-claude-code/.cursor/)
- [`everything-claude-code/.codex/`](everything-claude-code/.codex/)
- [`everything-claude-code/.codex-plugin/`](everything-claude-code/.codex-plugin/)
- [`everything-claude-code/.opencode/`](everything-claude-code/.opencode/)
- [`everything-claude-code/.gemini/`](everything-claude-code/.gemini/)
- [`everything-claude-code/.zed/`](everything-claude-code/.zed/)
- [`everything-claude-code/.kiro/`](everything-claude-code/.kiro/)
- [`everything-claude-code/.trae/`](everything-claude-code/.trae/)
- [`everything-claude-code/.qwen/`](everything-claude-code/.qwen/)

---

## 按目标选阅读路线

### 路线 1：只想学会怎么用

建议顺序：

1. [`README.md`](README.md)
2. [`ECC-COMMANDS-ZH.md`](ECC-COMMANDS-ZH.md)
3. [`everything-claude-code/COMMANDS-QUICK-REF.md`](everything-claude-code/COMMANDS-QUICK-REF.md)
4. [`everything-claude-code/the-shortform-guide.md`](everything-claude-code/the-shortform-guide.md)

### 路线 2：想看完整工作系统

建议顺序：

1. [`everything-claude-code/README.md`](everything-claude-code/README.md)
2. [`everything-claude-code/the-longform-guide.md`](everything-claude-code/the-longform-guide.md)
3. [`everything-claude-code/agents/`](everything-claude-code/agents/)
4. [`everything-claude-code/skills/`](everything-claude-code/skills/)
5. [`everything-claude-code/rules/`](everything-claude-code/rules/)
6. [`everything-claude-code/hooks/`](everything-claude-code/hooks/)

### 路线 3：想抄一套到自己的项目里

建议顺序：

1. [`everything-claude-code/examples/`](everything-claude-code/examples/)
2. [`everything-claude-code/rules/README.md`](everything-claude-code/rules/README.md)
3. [`everything-claude-code/install.sh`](everything-claude-code/install.sh)
4. [`everything-claude-code/install.ps1`](everything-claude-code/install.ps1)
5. [`everything-claude-code/docs/SELECTIVE-INSTALL-ARCHITECTURE.md`](everything-claude-code/docs/SELECTIVE-INSTALL-ARCHITECTURE.md)

### 路线 4：只想研究某类能力

- 看 agents：去 [`everything-claude-code/agents/`](everything-claude-code/agents/)
- 看 skills：去 [`everything-claude-code/skills/`](everything-claude-code/skills/)
- 看 rules：去 [`everything-claude-code/rules/`](everything-claude-code/rules/)
- 看 hooks：去 [`everything-claude-code/hooks/`](everything-claude-code/hooks/)
- 看平台适配：去各个点目录，如 [`.cursor/`](everything-claude-code/.cursor/) 或 [`.codex/`](everything-claude-code/.codex/)

---

## 和本仓库其余文件的关系

- [`README.md`](README.md)：中文总导读。
- [`ECC-COMMANDS-ZH.md`](ECC-COMMANDS-ZH.md)：中文命令速查。
- [`ECC-NAVIGATION-ZH.md`](ECC-NAVIGATION-ZH.md)：你现在正在看的本地副本导航索引。
- [`everything-claude-code/`](everything-claude-code/)：上游同步副本本体。

如果你平时只是想“快速找入口”，优先看这三份中文文件；如果你要核对定义和细节，再进入上游同步副本。

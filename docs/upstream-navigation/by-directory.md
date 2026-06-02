# 按目录读上游副本

## 按目录理解这个上游副本

### 核心入口

| 路径 | 用途 |
| ------ | ------ |
| [`everything-claude-code/README.md`](https://github.com/affaan-m/ECC/blob/main/README.md) | 上游英文主入口 |
| [`everything-claude-code/README.zh-CN.md`](https://github.com/affaan-m/ECC/blob/main/README.zh-CN.md) | 上游中文主入口 |
| [`everything-claude-code/CHANGELOG.md`](https://github.com/affaan-m/ECC/blob/main/CHANGELOG.md) | 版本更新记录 |
| [`everything-claude-code/COMMANDS-QUICK-REF.md`](https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md) | 命令速查 |
| [`everything-claude-code/TROUBLESHOOTING.md`](https://github.com/affaan-m/ECC/blob/main/TROUBLESHOOTING.md) | 顶层故障排查入口 |
| [`everything-claude-code/SECURITY.md`](https://github.com/affaan-m/ECC/blob/main/SECURITY.md) | 安全相关说明 |
| [`everything-claude-code/RULES.md`](https://github.com/affaan-m/ECC/blob/main/RULES.md) | 规则体系总览 |
| [`everything-claude-code/AGENTS.md`](https://github.com/affaan-m/ECC/blob/main/AGENTS.md) | agent 目录总览 |

### 核心能力目录

| 路径 | 看什么 |
| ------ | ------ |
| [`everything-claude-code/agents/`](https://github.com/affaan-m/ECC/tree/main/agents/) | 子代理定义 |
| [`everything-claude-code/skills/`](https://github.com/affaan-m/ECC/tree/main/skills/) | skills / 工作流定义 |
| [`everything-claude-code/commands/`](https://github.com/affaan-m/ECC/tree/main/commands/) | 维护中的命令入口 |
| [`everything-claude-code/legacy-command-shims/`](https://github.com/affaan-m/ECC/tree/main/legacy-command-shims/) | 兼容旧命令的 shim |
| [`everything-claude-code/rules/`](https://github.com/affaan-m/ECC/tree/main/rules/) | 通用规则与语言规则 |
| [`everything-claude-code/hooks/`](https://github.com/affaan-m/ECC/tree/main/hooks/) | hooks 配置与说明 |
| [`everything-claude-code/scripts/`](https://github.com/affaan-m/ECC/tree/main/scripts/) | 跨平台脚本与 hooks 实现 |
| [`everything-claude-code/tests/`](https://github.com/affaan-m/ECC/tree/main/tests/) | 脚本与 hooks 的测试 |

### 支撑性目录

| 路径 | 看什么 |
| ------ | ------ |
| [`everything-claude-code/docs/`](https://github.com/affaan-m/ECC/tree/main/docs/) | 补充文档、架构说明、安装设计、平台指南 |
| [`everything-claude-code/examples/`](https://github.com/affaan-m/ECC/tree/main/examples/) | 示例 CLAUDE.md 和项目样板 |
| [`everything-claude-code/contexts/`](https://github.com/affaan-m/ECC/tree/main/contexts/) | 注入式上下文模板 |
| [`everything-claude-code/mcp-configs/`](https://github.com/affaan-m/ECC/tree/main/mcp-configs/) | MCP 服务器配置 |
| [`everything-claude-code/manifests/`](https://github.com/affaan-m/ECC/tree/main/manifests/) | 安装与组件清单 |
| [`everything-claude-code/plugins/`](https://github.com/affaan-m/ECC/tree/main/plugins/) | 插件相关内容 |
| [`everything-claude-code/schemas/`](https://github.com/affaan-m/ECC/tree/main/schemas/) | 配置或数据结构 schema |
| [`everything-claude-code/src/`](https://github.com/affaan-m/ECC/tree/main/src/) | 程序源码与控制层实现 |
| [`everything-claude-code/ecc2/`](https://github.com/affaan-m/ECC/tree/main/ecc2/) | ECC 2.0 / 控制层相关原型 |

### 跨 harness / 平台适配目录

这些目录的存在说明 ECC 不再只服务 Claude Code：

- [`everything-claude-code/.claude/`](https://github.com/affaan-m/ECC/tree/main/.claude/)
- [`everything-claude-code/.claude-plugin/`](https://github.com/affaan-m/ECC/tree/main/.claude-plugin/)
- [`everything-claude-code/.cursor/`](https://github.com/affaan-m/ECC/tree/main/.cursor/)
- [`everything-claude-code/.codex/`](https://github.com/affaan-m/ECC/tree/main/.codex/)
- [`everything-claude-code/.codex-plugin/`](https://github.com/affaan-m/ECC/tree/main/.codex-plugin/)
- [`everything-claude-code/.opencode/`](https://github.com/affaan-m/ECC/tree/main/.opencode/)
- [`everything-claude-code/.gemini/`](https://github.com/affaan-m/ECC/tree/main/.gemini/)
- [`everything-claude-code/.zed/`](https://github.com/affaan-m/ECC/tree/main/.zed/)
- [`everything-claude-code/.kiro/`](https://github.com/affaan-m/ECC/tree/main/.kiro/)
- [`everything-claude-code/.trae/`](https://github.com/affaan-m/ECC/tree/main/.trae/)
- [`everything-claude-code/.qwen/`](https://github.com/affaan-m/ECC/tree/main/.qwen/)

---

## 按目标选阅读路线

### 路线 1：只想学会怎么用

建议顺序：

1. [`README.md`](../index.md)
2. [`ECC-COMMANDS-ZH.md`](../commands/index.md)
3. [`everything-claude-code/COMMANDS-QUICK-REF.md`](https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md)
4. [`everything-claude-code/the-shortform-guide.md`](https://github.com/affaan-m/ECC/blob/main/the-shortform-guide.md)

### 路线 2：想看完整工作系统

建议顺序：

1. [`everything-claude-code/README.md`](https://github.com/affaan-m/ECC/blob/main/README.md)
2. [`everything-claude-code/the-longform-guide.md`](https://github.com/affaan-m/ECC/blob/main/the-longform-guide.md)
3. [`everything-claude-code/agents/`](https://github.com/affaan-m/ECC/tree/main/agents/)
4. [`everything-claude-code/skills/`](https://github.com/affaan-m/ECC/tree/main/skills/)
5. [`everything-claude-code/rules/`](https://github.com/affaan-m/ECC/tree/main/rules/)
6. [`everything-claude-code/hooks/`](https://github.com/affaan-m/ECC/tree/main/hooks/)

### 路线 3：想抄一套到自己的项目里

建议顺序：

1. [`everything-claude-code/examples/`](https://github.com/affaan-m/ECC/tree/main/examples/)
2. [`everything-claude-code/rules/README.md`](https://github.com/affaan-m/ECC/blob/main/rules/README.md)
3. [`everything-claude-code/install.sh`](https://github.com/affaan-m/ECC/blob/main/install.sh)
4. [`everything-claude-code/install.ps1`](https://github.com/affaan-m/ECC/blob/main/install.ps1)
5. [`everything-claude-code/docs/SELECTIVE-INSTALL-ARCHITECTURE.md`](https://github.com/affaan-m/ECC/blob/main/docs/SELECTIVE-INSTALL-ARCHITECTURE.md)

### 路线 4：只想研究某类能力

- 看 agents：去 [`everything-claude-code/agents/`](https://github.com/affaan-m/ECC/tree/main/agents/)
- 看 skills：去 [`everything-claude-code/skills/`](https://github.com/affaan-m/ECC/tree/main/skills/)
- 看 rules：去 [`everything-claude-code/rules/`](https://github.com/affaan-m/ECC/tree/main/rules/)
- 看 hooks：去 [`everything-claude-code/hooks/`](https://github.com/affaan-m/ECC/tree/main/hooks/)
- 看平台适配：去各个点目录，如 [`.cursor/`](https://github.com/affaan-m/ECC/tree/main/.cursor/) 或 [`.codex/`](https://github.com/affaan-m/ECC/tree/main/.codex/)

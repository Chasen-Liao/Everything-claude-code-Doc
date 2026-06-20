# 核心概念

## 核心概念

ECC 现在已经不只是“Claude Code 的一套配置”，更接近一个**AI agent harness performance system**：它把代理、技能、命令、规则、钩子、安装清单和跨平台适配整合成一套可复用工作系统。

> 说明：下面的数量与描述基于当前已同步的上游 `affaan-m/ECC` 本地副本，以及上游 README 中公开说明的当前表面。版本继续演进时，数量可能变化。

| 组件 | 当前规模 | 作用 |
| ------ | ------ | ------ |
| **代理（Agents）** | 67 个代理文件 | 把复杂任务委派给专门角色，例如规划、审查、构建修复、文档更新 |
| **技能（Skills）** | 271 个技能目录 | 封装领域知识、工作流和可复用模式 |
| **命令（Commands）** | 92 个命令文件 | 作为 slash command 或命令入口调用工作流（上游也称之为 legacy command shims） |
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
   - 已确认存在 92 个命令文件（上游也称之为 legacy command shims）。
   - 上游命令速查中明确写了 **59 个全局 slash commands**。
   - 新增了质量门禁、上下文预算、循环执行、多模型协作、文档查询、harness 审计等能力。

4. **文档体系更完整**
   - 除主 README 外，还有长文指南、短文指南、安全指南、故障排查、架构说明、安装设计、Hermes 相关文档等。

5. **ECC 2.0 / Hermes 方向出现**
   - 上游文档里已经出现 `ecc2/`、Hermes setup、operator workflow 等新方向。
   - 这说明 ECC 不再只是“命令包”，而是在往更完整的操作层与控制层演进。

---

## 关键原则

1. **先澄清再动手**：复杂需求先 `/plan`，不要一上来就改代码。
2. **测试优先**：能走 TDD 就优先 `/tdd`。
3. **验证闭环**：开发完成后不要只看“能跑”，还要 `/verify` 或 `/quality-gate`。
4. **安全前置**：任何涉及用户输入、认证、依赖、配置的改动，都应该经过安全视角检查。
5. **把经验沉淀下来**：ECC 的特色不只是帮你完成任务，而是把成功模式转成可复用资产。
6. **把它理解为系统，不只是命令包**：Agent、Skill、Command、Rule、Hook、Harness 之间是联动的。

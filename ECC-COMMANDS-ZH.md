# ECC 命令中文速查

> 基于上游 [`COMMANDS-QUICK-REF.md`](everything-claude-code/COMMANDS-QUICK-REF.md) 整理。
> 当前上游公开说明为 **59 个全局 slash commands**。

---

## 最常用的一组

| 命令 | 什么时候用 | 作用 |
| ------ | ------ | ------ |
| `/plan` | 需求还不清晰、任务较大 | 先澄清需求、识别风险、生成实施计划 |
| `/tdd` | 想按测试优先推进 | 先写失败测试，再实现，再验证覆盖率 |
| `/code-review` | 代码写完后需要审查 | 检查质量、安全、可维护性 |
| `/build-fix` | 构建、类型检查、编译挂了 | 自动识别语言并修复常见构建问题 |
| `/verify` | 改动准备收尾 | 跑完整验证循环：build、lint、test、type-check |
| `/quality-gate` | 想做一次提交前质量闸门 | 按项目标准检查是否达到交付门槛 |

---

## 按场景找命令

### 1. 新功能开发

推荐顺序：

```text
/plan → /tdd → /code-review → /verify
```

如果功能涉及 UI 或用户流，再补：

```text
/e2e
```

### 2. 测试与覆盖率

| 命令 | 作用 |
| ------ | ------ |
| `/tdd` | 通用 TDD 工作流 |
| `/e2e` | 生成并运行 Playwright E2E 测试 |
| `/test-coverage` | 查看覆盖率与测试缺口 |
| `/go-test` | Go 的 TDD 与覆盖率工作流 |
| `/kotlin-test` | Kotlin 的 TDD 工作流 |
| `/rust-test` | Rust 的 TDD 工作流 |
| `/cpp-test` | C++ 的 TDD 工作流 |

### 3. 代码审查

| 命令 | 作用 |
| ------ | ------ |
| `/code-review` | 通用代码审查 |
| `/python-review` | Python 审查：PEP 8、类型提示、安全 |
| `/go-review` | Go 审查：惯用法、并发安全、错误处理 |
| `/kotlin-review` | Kotlin 审查：空安全、协程、架构 |
| `/rust-review` | Rust 审查：所有权、生命周期、unsafe |
| `/cpp-review` | C++ 审查：内存安全、现代写法、并发 |

### 4. 构建问题修复

| 命令 | 作用 |
| ------ | ------ |
| `/build-fix` | 自动识别语言并修复构建错误 |
| `/go-build` | 修复 Go build / go vet 问题 |
| `/kotlin-build` | 修复 Kotlin / Gradle 编译问题 |
| `/rust-build` | 修复 Rust 编译与 borrow checker 问题 |
| `/cpp-build` | 修复 C++ CMake / linker 问题 |
| `/gradle-build` | 修复 Android / KMP / Gradle 错误 |

### 5. 规划、多代理、多模型协作

| 命令 | 作用 |
| ------ | ------ |
| `/plan` | 单任务实现计划 |
| `/multi-plan` | 多模型协作规划 |
| `/multi-workflow` | 多模型协作开发 |
| `/multi-backend` | 偏后端的多模型流程 |
| `/multi-frontend` | 偏前端的多模型流程 |
| `/multi-execute` | 多模型协同执行 |
| `/orchestrate` | 指导 tmux / worktree 多代理编排 |
| `/devfleet` | 通过 DevFleet 并行调度 Claude Code agents |

### 6. 会话管理与上下文控制

| 命令 | 作用 |
| ------ | ------ |
| `/save-session` | 保存当前会话状态 |
| `/resume-session` | 恢复最近一次保存的会话 |
| `/sessions` | 浏览和管理会话历史 |
| `/checkpoint` | 在当前会话中打一个检查点 |
| `/aside` | 临时处理旁支问题，不丢主任务上下文 |
| `/context-budget` | 分析上下文占用并优化 |

### 7. 学习、沉淀与规则治理

| 命令 | 作用 |
| ------ | ------ |
| `/learn` | 从当前会话中提取模式 |
| `/learn-eval` | 提取模式并先做质量自评 |
| `/evolve` | 把已学习模式聚合成更稳定的技能结构 |
| `/promote` | 把项目级 instinct 提升到全局 |
| `/instinct-status` | 查看已学习 instinct 及置信度 |
| `/instinct-export` | 导出 instinct |
| `/instinct-import` | 导入 instinct |
| `/skill-create` | 从本地 git 历史生成 skill |
| `/skill-health` | 查看技能资产健康度 |
| `/rules-distill` | 从 skills 中抽取共性规则 |

### 8. 文档、研究与基础设施

| 命令 | 作用 |
| ------ | ------ |
| `/docs` | 通过 Context7 查询当前库 / API 文档 |
| `/update-docs` | 更新项目文档 |
| `/update-codemaps` | 重建代码地图 |
| `/projects` | 查看已知项目与 instinct 统计 |
| `/harness-audit` | 审计 agent harness 配置的稳定性与成本 |
| `/eval` | 跑评估 harness |
| `/model-route` | 给任务选择更合适的模型 |
| `/pm2` | 初始化或管理 PM2 |
| `/setup-pm` | 配置 npm / pnpm / yarn / bun |

### 9. 自动化与循环执行

| 命令 | 作用 |
| ------ | ------ |
| `/loop-start` | 启动定时循环 agent |
| `/loop-status` | 查看循环任务状态 |
| `/claw` | 启动 NanoClaw v2 持久 REPL |

---

## 最简决策表

```text
开始一个新功能？           → /plan，然后 /tdd
代码刚写完？               → /code-review
构建挂了？                 → /build-fix
需要当前库/API文档？       → /docs <library>
今天要收尾？               → /save-session 或 /learn-eval
明天继续？                 → /resume-session
上下文太重？               → /context-budget，然后 /checkpoint
想把经验沉淀下来？         → /learn-eval，然后 /evolve
要做重复自动化？           → /loop-start
```

---

## 补充说明

1. 这里是**中文速查**，不是完整权威定义。精确定义以上游命令文件与上游速查为准。
2. 并不是每个 skill 都一定有同名 slash command；不同 harness、不同安装方式，命令暴露面可能不同。
3. 某些命令在 ECC 中背后并不只是“执行一个动作”，而是会联动 skill、agent、rules 和 hooks，最好把它理解成工作流入口。

---

## 原始来源

- 上游命令速查：<https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md>
- 本地同步副本：[`everything-claude-code/COMMANDS-QUICK-REF.md`](everything-claude-code/COMMANDS-QUICK-REF.md)
- 上游命令目录：<https://github.com/affaan-m/ECC/tree/main/commands>

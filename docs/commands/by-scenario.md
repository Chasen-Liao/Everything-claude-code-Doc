# 按场景查命令

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

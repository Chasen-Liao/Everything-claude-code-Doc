# Everything Claude Code 使用指南

> 这是一个功能极其强大的 Claude Code 配置集合，包含代理、技能、命令、规则和自动化钩子。经过 10 多个月的密集日常使用和真实产品开发不断演化，是生产级别的开发工具。

---

## 目录

1. [核心概念](#核心概念)
2. [代理（Agents）](#代理-agents)
3. [技能（Skills）](#技能-skills)
4. [命令（Commands）](#命令-commands)
5. [规则（Rules）](#规则-rules)
6. [钩子（Hooks）](#钩子-hooks)
7. [实际工作流示例](#实际工作流示例)
8. [快速参考表](#快速参考表)

---

## 核心概念

Everything Claude Code 由以下核心组件构成：

| 组件 | 数量 | 功能 |
|------|------|------|
| **代理（Agents）** | 13个 | 专业化子代理，处理特定任务 |
| **技能（Skills）** | 37个 | 领域知识和工作流定义 |
| **命令（Commands）** | 31个 | 斜杠命令，快速触发功能 |
| **规则（Rules）** | 31条 | 始终遵循的编码指南 |
| **钩子（Hooks）** | 多个 | 基于触发事件的自动化 |

---

## 代理（Agents）

代理是专业化的子代理，可以处理特定领域的复杂任务。当遇到复杂任务时，Claude Code 会自动或根据指令调用这些代理。

### 代理列表与功能

| 代理名称 | 文件位置 | 功能描述 |
|----------|----------|----------|
| `planner` | `agents/planner.md` | 分析需求，创建详细实现计划 |
| `tdd-guide` | `agents/tdd-guide.md` | 强制测试驱动开发方法论，80%+ 覆盖率 |
| `code-reviewer` | `agents/code-reviewer.md` | 通用代码质量与安全审查 |
| `security-reviewer` | `agents/security-reviewer.md` | 安全漏洞检测与分析 |
| `build-error-resolver` | `agents/build-error-resolver.md` | 修复构建错误和类型错误 |
| `e2e-runner` | `agents/e2e-runner.md` | Playwright 端到端测试 |
| `refactor-cleaner` | `agents/refactor-cleaner.md` | 死代码清理与重构 |
| `doc-updater` | `agents/doc-updater.md` | 文档同步更新 |
| `go-reviewer` | `agents/go-reviewer.md` | Go 代码审查（惯用语、并发安全） |
| `go-build-resolver` | `agents/go-build-resolver.md` | Go 构建错误解决 |
| `python-reviewer` | `agents/python-reviewer.md` | Python 代码审查（PEP 8、类型提示） |
| `database-reviewer` | `agents/database-reviewer.md` | PostgreSQL/Supabase 数据库审查 |
| `architect` | `agents/architect.md` | 系统设计决策与架构规划 |

### 使用代理的方式

代理可以自动触发，也可以手动调用：

```
# 自动触发示例
User: "实现一个用户认证系统"
→ 系统自动调用 planner → 创建实施计划
→ 系统自动调用 tdd-guide → 开始 TDD 工作流

# 手动调用代理
使用 Task 工具指定 subagent_type
```

---

## 技能（Skills）

技能是工作流定义和领域知识的集合，包含特定领域的最佳实践和模式。

### 技能分类

#### 1. 测试驱动开发（TDD）

| 技能 | 路径 | 描述 |
|------|------|------|
| `tdd-workflow` | `skills/tdd-workflow/` | 通用 TDD 方法论，强制 80%+ 覆盖率 |
| `tdd-java` | `skills/tdd-java/` | Java TDD 模式 |
| `django-tdd` | `skills/django-tdd/` | Django 测试策略（pytest-django） |
| `springboot-tdd` | `skills/springboot-tdd/` | Spring Boot TDD（JUnit 5, Mockito） |
| `golang-testing` | `skills/golang-testing/` | Go 测试模式（表驱动测试、基准测试） |

#### 2. 编程语言模式

| 技能 | 路径 | 描述 |
|------|------|------|
| `golang-patterns` | `skills/golang-patterns/` | Go 惯用语和最佳实践 |
| `python-patterns` | `skills/python-patterns/` | Pythonic 惯用语、PEP 8 |
| `java-coding-standards` | `skills/java-coding-standards/` | Java 编码标准 |
| `jpa-patterns` | `skills/jpa-patterns/` | JPA/Hibernate 模式 |
| `cpp-testing` | `skills/cpp-testing/` | C++ 测试（GoogleTest） |

#### 3. Web 框架

| 技能 | 路径 | 描述 |
|------|------|------|
| `django-patterns` | `skills/django-patterns/` | Django 架构模式 |
| `django-security` | `skills/django-security/` | Django 安全最佳实践 |
| `django-verification` | `skills/django-verification/` | Django 验证循环 |
| `springboot-patterns` | `skills/springboot-patterns/` | Spring Boot 架构模式 |
| `springboot-security` | `skills/springboot-security/` | Spring Security |
| `springboot-verification` | `skills/springboot-verification/` | Spring Boot 验证循环 |

#### 4. 数据库

| 技能 | 路径 | 描述 |
|------|------|------|
| `postgres-patterns` | `skills/postgres-patterns/` | PostgreSQL 查询优化、索引设计 |
| `clickhouse-io` | `skills/clickhouse-io/` | ClickHouse 分析数据库 |
| `database-migrations` | `skills/database-migrations/` | 数据库迁移最佳实践 |

#### 5. 前端开发

| 技能 | 路径 | 描述 |
|------|------|------|
| `frontend-patterns` | `skills/frontend-patterns/` | React、Next.js、状态管理 |
| `e2e-testing` | `skills/e2e-testing/` | Playwright E2E 测试模式 |

#### 6. DevOps 与部署

| 技能 | 路径 | 描述 |
|------|------|------|
| `deployment-patterns` | `skills/deployment-patterns/` | CI/CD 管道、Docker、部署策略 |
| `docker-patterns` | `skills/docker-patterns/` | Docker Compose 开发环境 |

#### 7. API 设计

| 技能 | 路径 | 描述 |
|------|------|------|
| `api-design` | `skills/api-design/` | REST API 设计模式 |
| `backend-patterns` | `skills/backend-patterns/` | 后端架构模式 |

#### 8. 安全

| 技能 | 路径 | 描述 |
|------|------|------|
| `security-review` | `skills/security-review/` | 综合安全检查清单 |
| `security-scan` | `skills/security-scan/` | Claude Code 配置安全审计 |

#### 9. 高级功能

| 技能 | 路径 | 描述 |
|------|------|------|
| `continuous-learning-v2` | `skills/continuous-learning-v2/` | 基于直觉的学习系统 |
| `iterative-retrieval` | `skills/iterative-retrieval/` | 子代理上下文细化 |
| `strategic-compact` | `skills/strategic-compact/` | 手动上下文压缩建议 |
| `skill-create` | `skills/skill-create/` | 从 git 历史生成技能 |

### 技能调用方式

使用 Skill 工具调用：

```bash
# 调用 TDD 工作流
/skill tdd-workflow

# 调用 Python 代码审查
/skill python-review

# 调用安全审查
/skill security-review
```

或使用斜杠命令（如有配置）：

```bash
/tdd           # TDD 工作流
/e2e           # E2E 测试
/code-review   # 代码审查
```

---

## 命令（Commands）

斜杠命令是快速触发特定功能的快捷方式。

### 常用命令列表

#### 规划与执行

| 命令 | 功能 |
|------|------|
| `/plan` | 创建实现计划（调用 planner 代理） |
| `/multi-plan` | 多代理任务分解 |
| `/multi-execute` | 编排多代理工作流 |

#### 测试驱动开发

| 命令 | 功能 |
|------|------|
| `/tdd` | 启动 TDD 工作流 |
| `/e2e` | 生成端到端测试 |
| `/go-test` | Go TDD 工作流 |

#### 代码审查

| 命令 | 功能 |
|------|------|
| `/code-review` | 通用代码审查 |
| `/go-review` | Go 代码审查 |
| `/python-review` | Python 代码审查 |
| `/build-fix` | 修复构建错误 |
| `/go-build` | 修复 Go 构建错误 |

#### 重构与清理

| 命令 | 功能 |
|------|------|
| `/refactor-clean` | 移除死代码和未使用的导入 |
| `/verify` | 运行验证循环 |

#### 学习系统

| 命令 | 功能 |
|------|------|
| `/learn` | 从当前会话提取模式 |
| `/instinct-status` | 显示学习的直觉及置信度 |
| `/instinct-export` | 导出直觉供团队共享 |
| `/instinct-import` | 从他人导入直觉 |
| `/evolve` | 将相关直觉聚类到技能 |
| `/skill-create` | 从 git 历史生成技能文件 |

#### 开发工具

| 命令 | 功能 |
|------|------|
| `/setup-pm` | 配置包管理器（npm/pnpm/yarn/bun） |
| `/pm2` | PM2 服务生命周期管理 |
| `/sessions` | 会话历史管理 |

---

## 规则（Rules）

规则是始终遵循的编码指南，影响 Claude Code 的行为。

### 规则结构

```
rules/
├── common/                    # 语言无关原则（必须安装）
│   ├── coding-style.md       # 编码风格（不可变性、文件组织）
│   ├── git-workflow.md       # Git 工作流
│   ├── testing.md            # 测试要求（TDD、80% 覆盖率）
│   ├── performance.md        # 性能优化
│   ├── patterns.md           # 设计模式
│   ├── hooks.md              # Hook 架构
│   ├── agents.md             # 代理使用指南
│   └── security.md           # 安全检查
├── typescript/                # TypeScript 特定规则
│   ├── coding-style.md
│   ├── testing.md
│   ├── patterns.md
│   ├── hooks.md
│   └── security.md
├── python/                    # Python 特定规则
│   ├── coding-style.md
│   ├── testing.md
│   ├── patterns.md
│   ├── hooks.md
│   └── security.md
└── golang/                    # Go 特定规则
    ├── coding-style.md
    ├── testing.md
    ├── patterns.md
    ├── hooks.md
    └── security.md
```

### 核心规则要点

#### 1. 编码风格（coding-style.md）

- **不可变性**：始终创建新对象，永不修改现有对象
  - ❌ `modify(original, field, value)` - 原地修改
  - ✅ `update(original, field, value)` - 返回新副本
- **文件组织**：多小文件 > 少大文件；高内聚、低耦合
- **文件大小**：典型 200-400 行，最多 800 行

#### 2. 测试（testing.md）

- 强制 TDD 方法论
- 单元测试 + 集成测试 + E2E 测试
- 最低 80% 覆盖率要求

#### 3. 安全（security.md）

每次提交前必须检查：
- [ ] 无硬编码 secrets（API keys、passwords、tokens）
- [ ] 所有用户输入已验证
- [ ] SQL 注入防护（参数化查询）
- [ ] XSS 防护（HTML 净化）
- [ ] CSRF 防护已启用
- [ ] 认证/授权已验证
- [ ] 所有端点有速率限制
- [ ] 错误消息不泄露敏感数据

#### 4. Git 工作流（git-workflow.md）

- 提交信息格式：类型(范围): 描述
- 保持小而专注的提交
- 使用功能分支工作流

---

## 钩子（Hooks）

钩子是基于事件触发的自动化脚本。

### 钩子类型

| 触发器 | 执行时机 |
|--------|----------|
| `PreToolUse` | 工具执行前 |
| `PostToolUse` | 工具执行后 |
| `PreCompact` | 上下文压缩前 |
| `SessionStart` | 会话开始时 |
| `SessionEnd` | 会话结束时 |
| `Stop` | 停止时 |

### 功能性钩子

| 钩子 | 功能 |
|------|------|
| `post-edit-format.js` | 编辑后自动格式化（Prettier） |
| `post-edit-typecheck.js` | TypeScript 类型检查 |
| `post-edit-console-warn.js` | 警告 console.log 使用 |
| `check-console-log.js` | 检查控制台日志泄露 |
| `session-start.js` | 加载会话上下文 |
| `session-end.js` | 保存会话状态 |
| `suggest-compact.js` | 建议手动上下文压缩 |
| `evaluate-session.js` | 从会话中提取模式 |

---

## 实际工作流示例

### 1. 新功能开发

```
# 用户请求
实现一个用户认证系统

# 自动触发的工作流
1. /plan "添加用户认证"
   → planner 分析需求，创建详细的实施计划
   → 识别依赖：数据库表、JWT 机制、密码加密
   → 等待用户确认

2. 用户确认后
   /tdd
   → tdd-guide 强制测试优先
   → 编写用户旅程测试 → 测试失败 → 实现代码 → 测试通过 → 重构

3. 开发过程中
   → code-reviewer 自动审查代码质量

4. 完成前
   /e2e
   → e2e-runner 生成关键用户流的 E2E 测试

5. 部署前
   /security-scan
   → security-reviewer 安全审计
```

### 2. Bug 修复

```
# 用户请求
修复登录页面无法提交表单的问题

# 工作流
/tdd
→ tdd-guide: 编写一个复现 bug 的失败测试
→ 实现修复
→ 验证测试通过

→ code-reviewer: 捕获可能的回归
```

### 3. 代码审查

```
# 通用审查
/code-review

# Go 项目
/go-review

# Python 项目
/python-review

# 数据库相关
/database-review
```

### 4. 死代码清理

```
/refactor-clean
→ refactor-cleaner: 分析死代码、孤独导出、未使用导入
→ 执行清理，保持功能完整
```

### 5. 学习与知识积累

```
# 查看当前学习到的直觉
/instinct-status

# 将会话中的模式提取为可重用技能
/evolve

# 导出技能供团队使用
/instinct-export

# 从团队成员导入技能
/instinct-import
```

### 6. Go 项目开发

```
# 创建新功能
/plan "添加支付功能"
→ planner 分析并创建计划

# 开发
/go-test
→ golang-testing: TDD 工作流，带表驱动测试

# 审查
/go-review
→ go-reviewer: 检查惯用语、并发安全、错误处理

# 修复构建错误
/go-build
→ go-build-resolver: 最小改动修复构建问题
```

### 7. Python/Django 项目

```
# Django 项目
/django-patterns    # 查看 Django 最佳实践
/django-tdd         # Django TDD 工作流
/django-verification # 验证：迁移、lint、测试、覆盖率

# Python 通用
/python-patterns    # Pythonic 惯用语
/python-review      # PEP 8 审查
```

---

## 快速参考表

### 场景 → 动作映射

| 场景 | 推荐命令/技能 |
|------|--------------|
| 开始新功能 | `/plan` |
| 修复 Bug | `/tdd` |
| 写测试 | `/tdd` |
| E2E 测试 | `/e2e` |
| 代码审查 | `/code-review` |
| 安全检查 | `/security-scan` 或 `/security-review` |
| 清理死代码 | `/refactor-clean` |
| 修复构建错误 | `/build-fix` |
| 部署前验证 | `/verify` |
| 学习代码库 | 使用 Explore agent |
| Go 开发 | `/go-review`, `/go-test`, `/go-build` |
| Python 开发 | `/python-review`, `python-patterns` |
| Django 开发 | `django-patterns`, `django-tdd` |
| Spring Boot | `springboot-patterns`, `springboot-tdd` |
| 数据库优化 | `postgres-patterns`, `database-review` |
| 学习会话模式 | `/evolve`, `/instinct-status` |

### 语言 → 专用代理/技能

| 语言 | 代理 | 技能 |
|------|------|------|
| TypeScript | `code-reviewer` | `frontend-patterns` |
| Python | `python-reviewer` | `python-patterns`, `python-testing` |
| Go | `go-reviewer`, `go-build-resolver` | `golang-patterns`, `golang-testing` |
| Java | - | `java-coding-standards`, `jpa-patterns` |
| C++ | - | `cpp-testing` |
| Django | - | `django-patterns`, `django-tdd`, `django-security` |
| Spring Boot | - | `springboot-patterns`, `springboot-tdd`, `springboot-security` |

---

## 关键原则

1. **测试优先**：使用 `/tdd` 启动任何新功能开发
2. **安全第一**：所有涉及用户输入、认证、API 的功能使用 `/security-review`
3. **代码质量**：完成功能后使用 `/code-review` 或对应语言审查
4. **持续学习**：使用 `/evolve` 从成功的工作流中创建可重用技能
5. **验证检查**：生产部署前运行 `/verify`

---

## 更多信息

- 项目 GitHub: https://github.com/affaan-m/everything-claude-code
- 配置目录: `everything-claude-code/`
- 规则目录: `rules/`
- 技能目录: `skills/`
- 代理目录: `agents/`
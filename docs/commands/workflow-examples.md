# 实际工作流示例

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

这三类入口组合起来，比较接近"提交前 final pass"。

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

# 命令速查

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
- 本地同步副本：[`everything-claude-code/COMMANDS-QUICK-REF.md`](https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md)
- 上游命令目录：<https://github.com/affaan-m/ECC/tree/main/commands>

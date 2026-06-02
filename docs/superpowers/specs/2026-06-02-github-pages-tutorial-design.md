# GitHub Pages 中文教程站点设计

- 日期：2026-06-02
- 状态：已与用户对齐，待写实施计划
- 适用仓库：`Everything-claude-code-Doc`

## 背景

本仓库当前是 `affaan-m/ECC (Everything Claude Code)` 的中文教程镜像，分两层：

- 顶层教程层：`README.md`（738 行）、`ECC-COMMANDS-ZH.md`（162 行）、`ECC-NAVIGATION-ZH.md`（156 行），三份合计约 1056 行中文 Markdown。
- 上游同步层：`everything-claude-code/` 是嵌入式 gitlink，pinned 在上游 SHA `64cd1ba2`、版本 `2.0.0-rc.1`，由上游维护，本仓库只 fast-forward。

目标是把顶层教程层做成 GitHub Pages 站点，让中文读者能在浏览器里按结构化、可搜索的方式阅读这套教程，并保持与上游同步流程兼容。

## 目标 / 非目标

### 目标

- 站点首版包含现有 1056 行中文内容的全部信息，不丢失章节。
- 中文搜索、深浅色切换、代码块复制等阅读体验完整。
- 推进上游 / 修改文档时，Pages 站点能通过 CI 自动重建并发布。
- 现有 `sync-upstream-zh-docs` skill 在扩展之后能继续守住"数量计数"这条易错点。

### 首版范围说明

用户选定的内容范围是"完整教程书：重组 + 新增"。本设计文档对应**首版**，只完成"重组"这一半：

- 现有 1056 行中文内容按信息架构拆分到 `docs/` 对应路径，不改写语义。
- 信息架构里的"新增页"（典型如 `docs/maintenance/sync-upstream.md`）首版**只建立骨架文件**（含标题与一两句导读），正文留待后续迭代分批补全。
- 不在本首版引入入门视频、与上游对照表、可点击命令索引等额外新增内容。这些新增内容在站点上线、迁移稳定后，作为后续 PR 单独立项。

### 非目标（YAGNI）

- 站内中英双语切换。
- 自定义域名 / CNAME。
- PR Preview 站点。
- 评论系统（Giscus / Utterances）。
- Analytics。
- Algolia DocSearch（内置搜索已够用）。
- mermaid / 视频 / 截图（首版纯文本 + 表格 + 代码块）。
- 上游链接巡检调度。

## 整体架构

仓库内分两条独立链路：

```
教程层（站点源）        上游同步层
docs/                  everything-claude-code/   (gitlink)
mkdocs.yml             ↑ 由 sync-upstream-zh-docs skill 推进
        │
        └─→ GitHub Actions: mkdocs build --strict
                          → actions/deploy-pages
                          → <owner>.github.io/Everything-claude-code-Doc/
```

- 教程层以 `docs/` 为 MkDocs 单一源目录，`mkdocs.yml` 在仓库根。
- 上游同步层的 `everything-claude-code/` 通过 `mkdocs.yml` 的 `exclude_docs` 显式排除，**不进 build**。
- 顶层三份 .md 文件保留在仓库根，但内容做减法，仅作为 GitHub 仓库首页的"门牌 + 入口"，权威内容下沉到 `docs/`。

## 仓库目录结构

```
Everything-claude-code-Doc/
├── .github/workflows/deploy-pages.yml      新增
├── .claude/skills/sync-upstream-zh-docs/   已有，需扩展
├── docs/                                    新增（MkDocs 源）
│   ├── index.md                             首页
│   ├── getting-started/
│   │   ├── what-is-ecc.md
│   │   ├── who-is-this-for.md
│   │   └── quickstart.md
│   ├── concepts/
│   │   ├── overview.md
│   │   ├── agent-vs-skill-vs-command.md
│   │   └── misconceptions.md
│   ├── routes/
│   │   ├── index.md
│   │   ├── route-1-quick.md
│   │   ├── route-2-workflow.md
│   │   ├── route-3-multimodel.md
│   │   └── route-4-borrow.md
│   ├── commands/
│   │   ├── index.md
│   │   ├── most-used.md
│   │   ├── by-scenario.md
│   │   └── by-language.md
│   ├── upstream-navigation/
│   │   ├── index.md
│   │   └── by-directory.md
│   ├── maintenance/
│   │   └── sync-upstream.md
│   ├── faq.md
│   ├── assets/extra.css
│   ├── overrides/                           主题覆盖，首版留空
│   └── superpowers/specs/                   本设计文档所在位置（exclude_docs 排除）
├── everything-claude-code/                  已有 gitlink
├── scripts/migrate-docs.py                  新增：一次性迁移脚本
├── mkdocs.yml                                新增
├── requirements.txt                          新增
├── CLAUDE.md                                 已有，补一节"Pages 维护"
├── README.md                                 已有，做减法
├── ECC-COMMANDS-ZH.md                        已有，做减法
├── ECC-NAVIGATION-ZH.md                      已有，做减法
└── LICENSE
```

## 信息架构（侧边栏）

按"读者今天想干什么"组织一级目录：

1. 首页（`index.md`，对应原 README 的导读总览）
2. 入门
   - ECC 是什么 / 适合谁看 / 快速开始
3. 核心概念
   - Agent / Skill / Command / Rule / Hook / Harness 的层次解释
   - 常见误解
4. 推荐阅读路线（四条路线一页各一）
5. 命令速查
   - 最常用 / 按场景 / 按语言
6. 上游副本导航（对应原 NAVIGATION，外链全部跳上游 GitHub）
7. 维护：与上游同步（给本仓库维护者看）
8. FAQ

## 内容映射与链接重写

### 顶层三份 .md 的处置

原则：`docs/` 是权威，顶层文件减薄为门牌。

- 顶层 `README.md` 保留约 60–80 行：项目定位 + Pages 站链接 + 最小化"快速开始 3 步" + 上游链接列表。其余 600+ 行的细节内容下沉到 `docs/` 对应章节。
- 顶层 `ECC-COMMANDS-ZH.md` / `ECC-NAVIGATION-ZH.md` 减薄成单页导引，正文指向 `docs/commands/` 与 `docs/upstream-navigation/` 的 Pages URL。
- 内容**只做拆分与链接重写，不改写语义**。

### 链接重写规则

| 当前链接形态 | `docs/` 内改写为 |
| ------ | ------ |
| `[X](everything-claude-code/foo/bar.md)` | `[X](https://github.com/affaan-m/ECC/blob/main/foo/bar.md)` |
| `[X](everything-claude-code/foo/)` | `[X](https://github.com/affaan-m/ECC/tree/main/foo/)` |
| `[X](ECC-COMMANDS-ZH.md)` | `[X](../commands/index.md)` |
| `[X](ECC-NAVIGATION-ZH.md)` | `[X](../upstream-navigation/index.md)` |
| `[X](README.md#锚点)` | 解析到对应拆分页后改写为 `../concepts/...md#锚点` 等 |
| 已是 `https://...` 的 URL | 保持原样 |

所有外链统一加 Material 的 `:material-open-in-new:` 图标，提示读者离开本站。

### 一次性迁移脚本

写一个 `scripts/migrate-docs.py`：

- 输入：顶层三份 .md。
- 行为：按上面规则做正则重写 + 按章节切分，输出到 `docs/` 对应路径。
- 支持 `--dry-run` 打印将要写入的文件列表与重写计数，不落盘。
- 完成首版迁移后保留脚本，未来重大改动时复用。

迁移完成后，**首次上线前必须执行的人工校对**：

- 每个 `docs/**` 页面里 `everything-claude-code/` 字面量出现次数应为 0。
- 每个外链至少抽 1 条点击验证，目标在上游确实存在（最少抽检 10 条）。
- 站内相对链接由 `mkdocs build --strict` 自动验证，无需人工。

人工校对未通过则不进入 Pages 部署，先修后部。

## MkDocs 配置

### `mkdocs.yml`

关键字段：

```yaml
site_name: Everything Claude Code 中文教程
site_url: https://<owner>.github.io/Everything-claude-code-Doc/
repo_url: https://github.com/<owner>/Everything-claude-code-Doc
repo_name: Everything-claude-code-Doc
edit_uri: edit/main/docs/

docs_dir: docs
exclude_docs: |
  superpowers/**
  everything-claude-code/**

theme:
  name: material
  language: zh
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.code.annotate
    - content.action.edit
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle: { icon: material/weather-sunny, name: 切换到深色 }
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle: { icon: material/weather-night, name: 切换到浅色 }
  font:
    text: Noto Sans SC
    code: JetBrains Mono

plugins:
  - search:
      lang: [zh, en]
  - tags

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed: { alternate_style: true }
  - pymdownx.highlight: { anchor_linenums: true }
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - attr_list
  - md_in_html
  - toc: { permalink: true }

extra_css:
  - assets/extra.css

nav:
  # 与信息架构一节一一对应，迁移后补全
```

关键点：

- `language: zh` + `plugins.search.lang: [zh, en]`：中文界面与中文搜索分词。
- `exclude_docs` 同时排除 `superpowers/**`（本设计文档目录）与 `everything-claude-code/**`（上游 gitlink）。
- `edit_uri` 让每页顶部有 "Edit this page" 按钮直跳 GitHub。

### `requirements.txt`

```text
mkdocs-material>=9.5
mkdocs-material-extensions>=1.3
```

只列必需，版本不锁死。

## CI 与部署

### `.github/workflows/deploy-pages.yml`

```yaml
name: Deploy MkDocs to Pages

on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'mkdocs.yml'
      - 'requirements.txt'
      - '.github/workflows/deploy-pages.yml'
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: pip
      - run: pip install -r requirements.txt
      - run: mkdocs build --strict
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

要点：

- `paths` 触发器只对站点相关变化生效。`everything-claude-code/` 推进、根 README 减薄、`scripts/` 变更都不会触发 Pages 重建（必要时用 `workflow_dispatch` 手动触发）。
- `mkdocs build --strict` 把链接断裂 / 锚点找不到提升为错误。
- 用官方 Pages 部署 action，不写 `gh-pages` 分支。

### 一次性手动设置

仓库 Settings → Pages → Build and deployment → Source 设为 **GitHub Actions**（不是 "Deploy from branch"）。此操作只需做一次。

## 与 sync-upstream-zh-docs skill 的衔接

现有 skill 会在上游 `VERSION` 或计数（59 / 79 / 63 / 249 等）变化时，扫描顶层三份 .md 并刷新数字。Pages 加入后需要扩展：

- 扫描范围：旧的"顶层 3 份" → 新的"顶层 3 份 + `docs/**/*.md`"。
- 易错点清单新增一条：Pages 站点的拆分页里也散落了同样的计数，必须一起改。
- skill 内部命令（`for d in agents skills commands rules; do ls $d | wc -l; done` 等）保持不变。

skill 的扩展工作在实施计划阶段单独列任务。

## 错误处理与失败模式

| 失败模式 | 处理 |
| ------ | ------ |
| 内部链接 / 锚点损坏 | `mkdocs build --strict` 在 CI 失败，deploy 步骤不会跑，线上版本不动 |
| 外链上游 URL 失效（上游改名 / 文件搬迁） | 构建时不拦截。首次迁移后做一次人工抽检；后续若发现可临时手改并提 issue，不引入巡检调度 |
| Pages 缓存陈旧 | Material 内置 `navigation.instant` + 资源哈希；用户 Ctrl+F5 刷新即可 |
| 字体 CDN 在国内访问慢 | 首版接受；若后续抱怨多，再把 `theme.font` 改为系统字体回退栈，放进 `assets/extra.css` |

## 验收标准

满足全部下列条件视为首版完成：

1. `<owner>.github.io/Everything-claude-code-Doc/` 可访问，中文不乱码，深浅色可切换。
2. 现有 1056 行中文内容**全部**可在站点找到对应章节，无丢失。
3. 任意页面的"上游链接"点击后落到 `github.com/affaan-m/ECC/...` 的有效路径，人工抽检 10 条全部通过。
4. `mkdocs build --strict` 在本地与 CI 均通过。
5. `sync-upstream-zh-docs` skill 升级后，模拟一次"上游计数变化"，skill 能扫到并改写 `docs/**` 里的同步计数。

## 关键约束

- 不动 `everything-claude-code/` 下任何文件——它是上游 gitlink，所有变更走 fast-forward 同步。
- 不重写中文文档语义，迁移阶段只做"拆分 + 链接重写"。
- 顶层 README 减薄要保留三件套：项目定位、Pages 入口、上游链接列表，不可清空。
- `mkdocs.yml` 的 `exclude_docs` 必须同时排除 `superpowers/**` 与 `everything-claude-code/**`，否则 spec 文档与上游副本会被意外纳入站点。

## 待解决 / 后续

- 实施计划：由 `superpowers:writing-plans` 产出，覆盖迁移脚本、`docs/` 落盘、`mkdocs.yml`、Actions、skill 扩展、顶层文件减薄、本地构建验证、Pages 上线核验等步骤。
- skill 扩展的具体内部实现：写在实施计划里。
- `docs/maintenance/sync-upstream.md` 的正文：拆分迁移之后补全。

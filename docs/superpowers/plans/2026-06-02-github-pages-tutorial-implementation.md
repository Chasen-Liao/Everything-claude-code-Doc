# GitHub Pages 中文教程站点 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 `Everything-claude-code-Doc` 仓库的现有顶层中文文档（README / ECC-COMMANDS-ZH / ECC-NAVIGATION-ZH）拆分迁移成结构化的 MkDocs Material 站点，并通过 GitHub Actions 自动构建发布到 GitHub Pages。

**Architecture:** 仓库新增 `docs/` 作为 MkDocs 单一源；上游 gitlink `everything-claude-code/` 通过 `exclude_docs` 隔离不进 build；写一个一次性 Python 迁移脚本完成"链接重写 + H2 切分 + 按映射合并"；顶层三份 .md 减薄为门牌；现有 `sync-upstream-zh-docs` skill 扩展扫描范围到 `docs/**`；CI 监听 `docs/**` 与配置变化自动构建并部署。

**Tech Stack:** MkDocs Material 9.5+、Python 3.12（迁移脚本 + pytest）、GitHub Actions、Markdown。

**Spec:** `docs/superpowers/specs/2026-06-02-github-pages-tutorial-design.md`

---

## 文件结构（决定哪些文件会被创建 / 修改）

### 新建文件

| 路径 | 责任 |
| ------ | ------ |
| `requirements.txt` | Python 构建依赖清单 |
| `mkdocs.yml` | MkDocs 站点配置（主题、插件、扩展、导航） |
| `.gitignore` | 忽略 `site/` 构建产物（仓库当前无 .gitignore，本次新建） |
| `.github/workflows/deploy-pages.yml` | Actions 构建与部署工作流 |
| `scripts/migrate-docs.py` | 一次性迁移脚本：链接重写 + H2 切分 + 按映射合并 |
| `scripts/__init__.py` | 让 `scripts/` 成为可导入包，便于 pytest |
| `tests/__init__.py` | 测试包 |
| `tests/test_migrate_docs.py` | 迁移脚本的单元测试 |
| `docs/index.md` | 站点首页（自定义导读 + 导航卡片） |
| `docs/getting-started/what-is-ecc.md` | 由 README 拆出 |
| `docs/getting-started/who-is-this-for.md` | 由 README 拆出 |
| `docs/getting-started/quickstart.md` | 由 README 拆出 |
| `docs/concepts/overview.md` | 由 README 拆出 |
| `docs/concepts/agent-vs-skill-vs-command.md` | 由 README 拆出（agents/skills/commands/rules/hooks 五节合并展开） |
| `docs/concepts/misconceptions.md` | 由 README 拆出 |
| `docs/routes/index.md` | 由 README 拆出（四条路线全部并入此页，spec 中 `route-1..4` 子页本计划不创建） |
| `docs/commands/index.md` | 由 ECC-COMMANDS-ZH 拆出 |
| `docs/commands/most-used.md` | 由 ECC-COMMANDS-ZH 拆出 |
| `docs/commands/by-scenario.md` | 由 ECC-COMMANDS-ZH + README 工作流示例合并 |
| `docs/commands/by-language.md` | 由 README 快速参考表拆出 |
| `docs/upstream-navigation/index.md` | 由 ECC-NAVIGATION-ZH 拆出 |
| `docs/upstream-navigation/by-directory.md` | 由 ECC-NAVIGATION-ZH 拆出 |
| `docs/maintenance/sync-upstream.md` | 骨架（标题 + 一句导读），正文后续 PR 补全 |
| `docs/faq.md` | 由 README 拆出 |
| `docs/assets/extra.css` | 中文字体微调预留（首版空文件） |

### 修改文件

| 路径 | 修改内容 |
| ------ | ------ |
| `README.md` | 减薄到 60–80 行：项目定位 + Pages 站链接 + 快速开始 3 步 + 上游链接列表 |
| `ECC-COMMANDS-ZH.md` | 减薄到 30 行内：单页门牌指向 `docs/commands/` |
| `ECC-NAVIGATION-ZH.md` | 减薄到 30 行内：单页门牌指向 `docs/upstream-navigation/` |
| `CLAUDE.md` | 新增 "Pages 站点维护" 一节 |
| `.claude/skills/sync-upstream-zh-docs/SKILL.md` | 扫描范围扩展到 `docs/**`，新增易错点清单条目 |

### 不动文件

- `everything-claude-code/`：上游 gitlink，禁止改动。
- `LICENSE`：保留上游许可原文。
- `docs/superpowers/specs/2026-06-02-github-pages-tutorial-design.md`：已存在，仅供阅读。

---

## Task 1: 基础设施配置（依赖、MkDocs、gitignore）

**Files:**
- Create: `D:/Og/github/Everything-claude-code-Doc/requirements.txt`
- Create: `D:/Og/github/Everything-claude-code-Doc/mkdocs.yml`
- Create: `D:/Og/github/Everything-claude-code-Doc/.gitignore`

- [ ] **Step 1.1: 创建 `requirements.txt`**

写入以下内容：

```text
mkdocs-material>=9.5
mkdocs-material-extensions>=1.3
```

- [ ] **Step 1.2: 创建 `mkdocs.yml`（先不写 nav，待 Task 5 补全）**

写入以下内容：

```yaml
site_name: Everything Claude Code 中文教程
site_url: https://Chasen-Liao.github.io/Everything-claude-code-Doc/
site_description: ECC（Everything Claude Code）的中文教程镜像与导读
repo_url: https://github.com/Chasen-Liao/Everything-claude-code-Doc
repo_name: Chasen-Liao/Everything-claude-code-Doc
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
      toggle:
        icon: material/weather-sunny
        name: 切换到深色
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle:
        icon: material/weather-night
        name: 切换到浅色
  font:
    text: Noto Sans SC
    code: JetBrains Mono

plugins:
  - search:
      lang:
        - zh
        - en
  - tags

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - attr_list
  - md_in_html
  - toc:
      permalink: true

extra_css:
  - assets/extra.css
```

> 仓库 owner 已确认为 `Chasen-Liao`（来源：现有 `README.md` 第 724 行"当前说明仓库"链接）。如未来 fork 或转移，需要在 `mkdocs.yml` 的 `site_url` / `repo_url` / `repo_name` 三处一并修改。

- [ ] **Step 1.3: 创建 `.gitignore`**

写入以下内容：

```gitignore
# MkDocs build output
site/

# Python
__pycache__/
*.pyc
.pytest_cache/
.venv/
venv/

# OS
.DS_Store
Thumbs.db
```

- [ ] **Step 1.4: 本地安装依赖并验证**

```bash
cd D:/Og/github/Everything-claude-code-Doc
python -m pip install -r requirements.txt
```

预期：`mkdocs-material` 与所有依赖安装成功，无 ERROR 行。

- [ ] **Step 1.5: 验证 `mkdocs.yml` 语法**

```bash
python -c "import yaml; yaml.safe_load(open('mkdocs.yml', encoding='utf-8'))"
```

预期：无输出（YAML 合法）。

- [ ] **Step 1.6: 提交**

```bash
git add requirements.txt mkdocs.yml .gitignore
git commit -m "$(cat <<'EOF'
chore(pages): 新增 MkDocs 配置与依赖

requirements.txt 锁定 mkdocs-material>=9.5；
mkdocs.yml 启用中文搜索、深浅色切换、edit_uri、
exclude_docs 排除上游 gitlink 与 superpowers spec；
.gitignore 忽略 site/ 与 Python 缓存。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: 建立 `docs/` 骨架文件

**Files:**
- Create: 20 个 `.md` 文件（见下方清单）
- Create: `docs/assets/extra.css`

**说明：** 先建空骨架（H1 + 一行待补提示），让 Task 3 的迁移脚本只负责填正文，并能在 Task 5 之前先通过 `mkdocs build --strict` 检查站点骨架是否合法。

- [ ] **Step 2.1: 创建 `docs/index.md`**

```markdown
# Everything Claude Code 中文教程

> 这是 [`affaan-m/ECC`](https://github.com/affaan-m/ECC) 的中文教程镜像。本站点把上游的能力边界、典型工作流和入口拆成可按需检索的多页结构，方便中文读者快速建立整体认知。

## 从哪里开始

- 第一次接触 ECC：先看 [入门 · ECC 是什么](getting-started/what-is-ecc.md)
- 想理解概念分层：看 [核心概念 · 总览](concepts/overview.md)
- 只想看命令：看 [命令速查](commands/index.md)
- 想在上游副本里查原始定义：看 [上游副本导航](upstream-navigation/index.md)
- 维护本仓库：看 [与上游同步](maintenance/sync-upstream.md)

> 上游权威源始终是 <https://github.com/affaan-m/ECC>，本教程只做解释、串联、阅读路径。
```

- [ ] **Step 2.2: 创建 20 个章节骨架文件**

对下列每个路径，写入对应骨架内容（H1 标题 + 一行待补提示）：

| 路径 | H1 标题 |
| ------ | ------ |
| `docs/getting-started/what-is-ecc.md` | ECC 是什么 |
| `docs/getting-started/who-is-this-for.md` | 适合谁看 |
| `docs/getting-started/quickstart.md` | 快速开始 |
| `docs/concepts/overview.md` | 核心概念 |
| `docs/concepts/agent-vs-skill-vs-command.md` | Agent / Skill / Command 等组件 |
| `docs/concepts/misconceptions.md` | 常见误解 |
| `docs/routes/index.md` | 推荐阅读路线 |
| `docs/commands/index.md` | 命令速查 |
| `docs/commands/most-used.md` | 最常用的一组命令 |
| `docs/commands/by-scenario.md` | 按场景查命令 |
| `docs/commands/by-language.md` | 按语言查命令 |
| `docs/upstream-navigation/index.md` | 上游副本导航 |
| `docs/upstream-navigation/by-directory.md` | 按目录读上游副本 |
| `docs/maintenance/sync-upstream.md` | 与上游同步 |
| `docs/faq.md` | 常见问题 |

每个文件的骨架内容统一为：

```markdown
# <H1 标题>

<!-- 由 scripts/migrate-docs.py 在 Task 4 中填入正文 -->
```

例外：`docs/maintenance/sync-upstream.md` 不会被迁移脚本覆盖，骨架写为：

```markdown
# 与上游同步

> 本页内容在后续 PR 中补全。当前仓库的同步流程详见根目录 `CLAUDE.md` 与 [`.claude/skills/sync-upstream-zh-docs/`](https://github.com/Chasen-Liao/Everything-claude-code-Doc/tree/main/.claude/skills/sync-upstream-zh-docs)。
```

- [ ] **Step 2.3: 创建 `docs/assets/extra.css`**

写入空文件（仅一行注释占位）：

```css
/* 中文字体与排版微调预留。首版留空。 */
```

- [ ] **Step 2.4: 提交**

```bash
git add docs/
git commit -m "$(cat <<'EOF'
docs(pages): 建立站点章节骨架

按 spec 的信息架构创建 16 个 .md 骨架文件，
正文由后续 migrate-docs.py 脚本填入。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: 迁移脚本 TDD（链接重写 + H2 切分 + 映射合并）

**Files:**
- Create: `scripts/__init__.py`
- Create: `scripts/migrate_docs.py`
- Create: `tests/__init__.py`
- Create: `tests/test_migrate_docs.py`

**说明：** 脚本职责拆成三个纯函数 + 一个驱动函数，便于 TDD：
1. `rewrite_links(text)`：按 spec 表把相对链接重写为上游 URL 或站内相对路径。
2. `parse_h2_sections(text)`：把一份 .md 按 H2 切成 `{title: body}` 字典。
3. `build_target_files(mapping, sources)`：按映射表合并多段 H2，输出 `{path: content}`。
4. `main()`：读三份 .md、做切分与合并、写盘。

- [ ] **Step 3.1: 创建 `scripts/__init__.py` 与 `tests/__init__.py`**

两个文件均写入空内容（仅一行注释即可）：

```python
# package marker
```

- [ ] **Step 3.2: 安装 pytest**

```bash
python -m pip install pytest
```

预期：pytest 安装成功。

- [ ] **Step 3.3: 写第一个失败测试——链接重写**

创建 `tests/test_migrate_docs.py`，写入：

```python
"""Tests for scripts/migrate_docs.py."""

from scripts.migrate_docs import (
    rewrite_links,
    parse_h2_sections,
    build_target_files,
)


# -----------------------
# rewrite_links
# -----------------------

def test_rewrite_links_md_file_to_blob_main():
    text = "see [foo](everything-claude-code/foo/bar.md) here"
    assert rewrite_links(text) == (
        "see [foo](https://github.com/affaan-m/ECC/blob/main/foo/bar.md) here"
    )


def test_rewrite_links_directory_to_tree_main():
    text = "see [skills](everything-claude-code/skills/) here"
    assert rewrite_links(text) == (
        "see [skills](https://github.com/affaan-m/ECC/tree/main/skills/) here"
    )


def test_rewrite_links_script_file_to_blob_main():
    text = "see [install](everything-claude-code/install.sh) here"
    assert rewrite_links(text) == (
        "see [install](https://github.com/affaan-m/ECC/blob/main/install.sh) here"
    )


def test_rewrite_links_commands_zh_to_relative():
    text = "see [cmd](ECC-COMMANDS-ZH.md) here"
    assert rewrite_links(text) == "see [cmd](../commands/index.md) here"


def test_rewrite_links_navigation_zh_to_relative():
    text = "see [nav](ECC-NAVIGATION-ZH.md) here"
    assert rewrite_links(text) == "see [nav](../upstream-navigation/index.md) here"


def test_rewrite_links_readme_to_relative():
    text = "see [home](README.md) here"
    assert rewrite_links(text) == "see [home](../index.md) here"


def test_rewrite_links_keeps_https_urls_untouched():
    text = "see [up](https://github.com/affaan-m/ECC/blob/main/foo.md) here"
    assert rewrite_links(text) == text


def test_rewrite_links_multiple_in_one_line():
    text = (
        "[a](everything-claude-code/a.md) and "
        "[b](everything-claude-code/b/) and "
        "[c](ECC-COMMANDS-ZH.md)"
    )
    expected = (
        "[a](https://github.com/affaan-m/ECC/blob/main/a.md) and "
        "[b](https://github.com/affaan-m/ECC/tree/main/b/) and "
        "[c](../commands/index.md)"
    )
    assert rewrite_links(text) == expected
```

- [ ] **Step 3.4: 跑测试确认失败**

```bash
cd D:/Og/github/Everything-claude-code-Doc
python -m pytest tests/test_migrate_docs.py -v
```

预期：`ImportError` 或 `ModuleNotFoundError`——`scripts.migrate_docs` 还不存在。

- [ ] **Step 3.5: 实现 `rewrite_links` 让上面测试通过**

创建 `scripts/migrate_docs.py`，写入：

```python
"""One-shot migration: split top-level Chinese docs into docs/ pages with link rewriting.

Runs end-to-end via ``python -m scripts.migrate_docs`` (use ``--dry-run`` to preview).
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Callable

REPO_ROOT = Path(__file__).resolve().parent.parent
UPSTREAM_BASE = "https://github.com/affaan-m/ECC"

# ---- link rewriting ---------------------------------------------------------

# Order matters: directory rule (trailing /) must run before non-md file rule.
LINK_RULES: list[tuple[re.Pattern[str], Callable[[re.Match[str]], str]]] = [
    (
        re.compile(r"\[([^\]]+)\]\(everything-claude-code/([^)]+\.md)\)"),
        lambda m: f"[{m.group(1)}]({UPSTREAM_BASE}/blob/main/{m.group(2)})",
    ),
    (
        re.compile(r"\[([^\]]+)\]\(everything-claude-code/([^)]+/)\)"),
        lambda m: f"[{m.group(1)}]({UPSTREAM_BASE}/tree/main/{m.group(2)})",
    ),
    (
        re.compile(r"\[([^\]]+)\]\(everything-claude-code/([^)/]+)\)"),
        lambda m: f"[{m.group(1)}]({UPSTREAM_BASE}/blob/main/{m.group(2)})",
    ),
    (
        re.compile(r"\[([^\]]+)\]\(ECC-COMMANDS-ZH\.md\)"),
        lambda m: f"[{m.group(1)}](../commands/index.md)",
    ),
    (
        re.compile(r"\[([^\]]+)\]\(ECC-NAVIGATION-ZH\.md\)"),
        lambda m: f"[{m.group(1)}](../upstream-navigation/index.md)",
    ),
    (
        re.compile(r"\[([^\]]+)\]\(README\.md\)"),
        lambda m: f"[{m.group(1)}](../index.md)",
    ),
]


def rewrite_links(text: str) -> str:
    for pattern, replacer in LINK_RULES:
        text = pattern.sub(replacer, text)
    return text


# Stubs to make import work; implemented in next steps.
def parse_h2_sections(text: str) -> dict[str, str]:
    raise NotImplementedError


def build_target_files(mapping, sources) -> dict[str, str]:
    raise NotImplementedError
```

- [ ] **Step 3.6: 跑测试，确认 `rewrite_links` 部分全绿**

```bash
python -m pytest tests/test_migrate_docs.py -v -k rewrite_links
```

预期：8 个 `test_rewrite_links_*` 全部 PASS。

- [ ] **Step 3.7: 加 `parse_h2_sections` 的失败测试**

在 `tests/test_migrate_docs.py` 文件末尾追加：

```python
# -----------------------
# parse_h2_sections
# -----------------------

SAMPLE_MD = """# Title

intro line

## Section A

body of A line 1
body of A line 2

## Section B

body of B

---

## Section C

body of C
"""


def test_parse_h2_sections_returns_three_sections():
    sections = parse_h2_sections(SAMPLE_MD)
    assert list(sections.keys()) == ["Section A", "Section B", "Section C"]


def test_parse_h2_sections_keeps_body_content():
    sections = parse_h2_sections(SAMPLE_MD)
    assert "body of A line 1" in sections["Section A"]
    assert "body of A line 2" in sections["Section A"]


def test_parse_h2_sections_strips_hr_between_sections():
    sections = parse_h2_sections(SAMPLE_MD)
    # 水平线 "---" 是 README 中分隔 section 的样式，不应进入下一 section 内容
    assert not sections["Section B"].strip().startswith("---")
    assert not sections["Section C"].strip().startswith("---")


def test_parse_h2_sections_ignores_h1_and_intro():
    sections = parse_h2_sections(SAMPLE_MD)
    assert "Title" not in sections
    assert "intro line" not in "".join(sections.values())
```

- [ ] **Step 3.8: 跑测试，确认 `parse_h2_sections` 失败**

```bash
python -m pytest tests/test_migrate_docs.py -v -k parse_h2
```

预期：4 个 `test_parse_h2_*` 全部 FAIL with `NotImplementedError`。

- [ ] **Step 3.9: 实现 `parse_h2_sections`**

把 `scripts/migrate_docs.py` 中的 `parse_h2_sections` stub 替换为：

```python
def parse_h2_sections(text: str) -> dict[str, str]:
    """Split a Markdown document by H2 headings into {title: body}.

    Drops the H1, any intro before the first H2, and any standalone '---'
    separators that sit between sections.
    """
    lines = text.splitlines()
    sections: dict[str, str] = {}
    current_title: str | None = None
    current_body: list[str] = []

    def flush() -> None:
        if current_title is None:
            return
        body = "\n".join(current_body)
        # strip leading/trailing hr lines and surrounding whitespace
        body = re.sub(r"^\s*(---\s*\n)+", "", body)
        body = re.sub(r"(\n---\s*)+\s*$", "", body)
        sections[current_title] = body.strip("\n")

    for line in lines:
        m = re.match(r"^## +(.+?)\s*$", line)
        if m:
            flush()
            current_title = m.group(1).strip()
            current_body = []
        else:
            if current_title is not None:
                current_body.append(line)
    flush()
    return sections
```

- [ ] **Step 3.10: 跑测试，确认 `parse_h2_sections` 全绿**

```bash
python -m pytest tests/test_migrate_docs.py -v
```

预期：12 个测试全部 PASS（8 个 rewrite_links + 4 个 parse_h2_sections）。

- [ ] **Step 3.11: 加 `build_target_files` 的失败测试**

在 `tests/test_migrate_docs.py` 文件末尾追加：

```python
# -----------------------
# build_target_files
# -----------------------

def test_build_target_files_merges_multiple_h2_into_one_file():
    sources = {
        "README.md": "# T\n\n## A\n\naa\n\n## B\n\nbb\n",
    }
    mapping = {
        "docs/page.md": {
            "source": "README.md",
            "h2_titles": ["A", "B"],
            "page_h1": "Merged Page",
        },
    }
    out = build_target_files(mapping, sources)
    assert "docs/page.md" in out
    content = out["docs/page.md"]
    assert content.startswith("# Merged Page")
    assert "## A" in content
    assert "## B" in content
    assert "aa" in content
    assert "bb" in content


def test_build_target_files_rewrites_links_inside_body():
    sources = {
        "README.md": (
            "# T\n\n"
            "## S\n\n"
            "see [foo](everything-claude-code/foo.md)\n"
        ),
    }
    mapping = {
        "docs/x.md": {
            "source": "README.md",
            "h2_titles": ["S"],
            "page_h1": "X",
        },
    }
    out = build_target_files(mapping, sources)
    assert "https://github.com/affaan-m/ECC/blob/main/foo.md" in out["docs/x.md"]
    assert "everything-claude-code/" not in out["docs/x.md"]


def test_build_target_files_keeps_h2_order_from_mapping():
    sources = {
        "README.md": "# T\n\n## A\n\naa\n\n## B\n\nbb\n\n## C\n\ncc\n",
    }
    mapping = {
        "docs/page.md": {
            "source": "README.md",
            "h2_titles": ["C", "A"],  # reversed
            "page_h1": "P",
        },
    }
    content = build_target_files(mapping, sources)["docs/page.md"]
    pos_c = content.index("## C")
    pos_a = content.index("## A")
    assert pos_c < pos_a
    assert "## B" not in content  # B not requested
```

- [ ] **Step 3.12: 跑测试，确认 `build_target_files` 失败**

```bash
python -m pytest tests/test_migrate_docs.py -v -k build_target
```

预期：3 个 `test_build_target_*` 全部 FAIL with `NotImplementedError`。

- [ ] **Step 3.13: 实现 `build_target_files` 与 `main`**

把 `scripts/migrate_docs.py` 中的 `build_target_files` stub 替换为下面的实现，并追加 `main`：

```python
def build_target_files(
    mapping: dict[str, dict],
    sources: dict[str, str],
) -> dict[str, str]:
    """Render target docs/ files by combining selected H2 sections.

    mapping schema:
        { "<target path>": {
              "source": "<filename in sources>",
              "h2_titles": [...],   # in desired output order
              "page_h1": "<H1 for the page>",
          }, ... }
    """
    parsed: dict[str, dict[str, str]] = {
        name: parse_h2_sections(text) for name, text in sources.items()
    }
    out: dict[str, str] = {}
    for target_path, spec in mapping.items():
        source_name = spec["source"]
        if source_name not in parsed:
            raise KeyError(f"unknown source: {source_name}")
        h1 = spec["page_h1"]
        parts: list[str] = [f"# {h1}", ""]
        for title in spec["h2_titles"]:
            if title not in parsed[source_name]:
                raise KeyError(
                    f"H2 '{title}' not found in {source_name}"
                )
            parts.append(f"## {title}")
            parts.append("")
            parts.append(parsed[source_name][title])
            parts.append("")
            parts.append("---")
            parts.append("")
        # drop trailing separator block
        while parts and parts[-1] in ("", "---"):
            parts.pop()
        text = "\n".join(parts) + "\n"
        out[target_path] = rewrite_links(text)
    return out


# ---- mapping table ----------------------------------------------------------

MAPPING: dict[str, dict] = {
    "docs/getting-started/what-is-ecc.md": {
        "source": "README.md",
        "page_h1": "ECC 是什么",
        "h2_titles": ["这份仓库是什么 / 不是什么", "仓库状态与原始来源"],
    },
    "docs/getting-started/who-is-this-for.md": {
        "source": "README.md",
        "page_h1": "适合谁看",
        "h2_titles": ["适合谁看", "你会在这里得到什么"],
    },
    "docs/getting-started/quickstart.md": {
        "source": "README.md",
        "page_h1": "快速开始",
        "h2_titles": ["快速开始", "和上游仓库的关系"],
    },
    "docs/concepts/overview.md": {
        "source": "README.md",
        "page_h1": "核心概念",
        "h2_titles": [
            "核心概念",
            "现在的 ECC 和早期版本有什么不同",
            "关键原则",
        ],
    },
    "docs/concepts/agent-vs-skill-vs-command.md": {
        "source": "README.md",
        "page_h1": "Agent / Skill / Command 等组件",
        "h2_titles": [
            "代理（Agents）",
            "技能（Skills）",
            "命令（Commands）",
            "规则（Rules）",
            "钩子（Hooks）",
        ],
    },
    "docs/concepts/misconceptions.md": {
        "source": "README.md",
        "page_h1": "常见误解",
        "h2_titles": ["常见误解"],
    },
    "docs/routes/index.md": {
        "source": "README.md",
        "page_h1": "推荐阅读路线",
        "h2_titles": ["推荐教程路线", "推荐阅读入口"],
    },
    "docs/commands/index.md": {
        "source": "ECC-COMMANDS-ZH.md",
        "page_h1": "命令速查",
        "h2_titles": ["最简决策表", "补充说明", "原始来源"],
    },
    "docs/commands/most-used.md": {
        "source": "ECC-COMMANDS-ZH.md",
        "page_h1": "最常用的一组命令",
        "h2_titles": ["最常用的一组"],
    },
    "docs/commands/by-scenario.md": {
        "source": "ECC-COMMANDS-ZH.md",
        "page_h1": "按场景查命令",
        "h2_titles": ["按场景找命令"],
    },
    "docs/commands/by-language.md": {
        "source": "README.md",
        "page_h1": "按语言查命令",
        "h2_titles": ["快速参考表"],
    },
    "docs/upstream-navigation/index.md": {
        "source": "ECC-NAVIGATION-ZH.md",
        "page_h1": "上游副本导航",
        "h2_titles": ["先看哪里", "和本仓库其余文件的关系"],
    },
    "docs/upstream-navigation/by-directory.md": {
        "source": "ECC-NAVIGATION-ZH.md",
        "page_h1": "按目录读上游副本",
        "h2_titles": ["按目录理解这个上游副本", "按目标选阅读路线"],
    },
    "docs/faq.md": {
        "source": "README.md",
        "page_h1": "常见问题",
        "h2_titles": ["FAQ"],
    },
}


SOURCE_FILES = [
    "README.md",
    "ECC-COMMANDS-ZH.md",
    "ECC-NAVIGATION-ZH.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print target paths and content sizes without writing files",
    )
    args = parser.parse_args()

    sources: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = REPO_ROOT / name
        sources[name] = path.read_text(encoding="utf-8")

    targets = build_target_files(MAPPING, sources)

    for target_path, content in targets.items():
        full = REPO_ROOT / target_path
        if args.dry_run:
            print(f"DRY  {target_path:60s}  {len(content):6d} chars")
            continue
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(content, encoding="utf-8")
        print(f"WROTE {target_path:60s}  {len(content):6d} chars")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3.14: 跑全部测试**

```bash
python -m pytest tests/test_migrate_docs.py -v
```

预期：15 个测试全部 PASS。

- [ ] **Step 3.15: 提交**

```bash
git add scripts/__init__.py scripts/migrate_docs.py tests/__init__.py tests/test_migrate_docs.py
git commit -m "$(cat <<'EOF'
feat(pages): 新增一次性迁移脚本与单元测试

scripts/migrate_docs.py 拆三个纯函数（链接重写 / H2 切分 /
按映射合并）+ main 驱动；15 个 pytest 用例覆盖三个函数的
正向与边界行为。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: 跑迁移并校验

**Files:**
- Modify: `docs/getting-started/*.md`、`docs/concepts/*.md`、`docs/routes/index.md`、`docs/commands/*.md`、`docs/upstream-navigation/*.md`、`docs/faq.md`（共 14 个文件，由脚本覆写）

- [ ] **Step 4.1: dry-run 看预览**

```bash
cd D:/Og/github/Everything-claude-code-Doc
python -m scripts.migrate_docs --dry-run
```

预期：列出 14 行 `DRY <path> <N> chars`，没有 `KeyError`。如果某个 H2 标题被脚本报"not found"，说明映射表里的 `h2_titles` 字符串和源 .md 里的实际标题对不上——回到 `scripts/migrate_docs.py` 检查 `MAPPING` 表条目。

- [ ] **Step 4.2: 落盘**

```bash
python -m scripts.migrate_docs
```

预期：14 行 `WROTE <path> <N> chars`。

- [ ] **Step 4.3: 验证 docs/ 下没有 `everything-claude-code/` 字面量相对链接**

```bash
grep -rn "everything-claude-code/" docs/ --include="*.md" || echo "clean"
```

预期：输出 `clean`（或仅有以 `https://github.com/affaan-m/ECC` 开头的命中——但脚本规则不会产生这种命中，所以应该是 `clean`）。

如果命中非空，说明某条链接形态没被 `LINK_RULES` 覆盖——回到 `scripts/migrate_docs.py` 补 rule、补对应单元测试、重跑脚本。

- [ ] **Step 4.4: 验证站内相对链接形态**

```bash
grep -rn "](../commands/index.md)\|](../upstream-navigation/index.md)\|](../index.md)" docs/ --include="*.md" | head -20
```

预期：看到若干命中，至少包含 `../commands/index.md` 与 `../upstream-navigation/index.md`。

- [ ] **Step 4.5: 提交**

```bash
git add docs/
git commit -m "$(cat <<'EOF'
docs(pages): 用 migrate_docs.py 填充 14 个章节正文

按 MAPPING 把 README / ECC-COMMANDS-ZH / ECC-NAVIGATION-ZH
拆并到 docs/，所有相对链接重写为上游 GitHub URL 或站内
相对路径。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: 补 `mkdocs.yml` 的 `nav` 并本地 build 验证

**Files:**
- Modify: `mkdocs.yml`

- [ ] **Step 5.1: 在 `mkdocs.yml` 末尾追加 `nav` 段**

把以下 YAML 追加到 `mkdocs.yml` 文件末尾（紧跟 `extra_css:` 块之后，文件最后一行）：

```yaml

nav:
  - 首页: index.md
  - 入门:
      - ECC 是什么: getting-started/what-is-ecc.md
      - 适合谁看: getting-started/who-is-this-for.md
      - 快速开始: getting-started/quickstart.md
  - 核心概念:
      - 总览: concepts/overview.md
      - 组件:Agent/Skill/Command: concepts/agent-vs-skill-vs-command.md
      - 常见误解: concepts/misconceptions.md
  - 阅读路线: routes/index.md
  - 命令速查:
      - 总览: commands/index.md
      - 最常用: commands/most-used.md
      - 按场景: commands/by-scenario.md
      - 按语言: commands/by-language.md
  - 上游副本导航:
      - 总览: upstream-navigation/index.md
      - 按目录: upstream-navigation/by-directory.md
  - 维护:
      - 与上游同步: maintenance/sync-upstream.md
  - 常见问题: faq.md
```

- [ ] **Step 5.2: 本地严格构建**

```bash
cd D:/Og/github/Everything-claude-code-Doc
python -m mkdocs build --strict
```

预期：以 `INFO` 行结束，最后一行类似 `Documentation built in N.NN seconds`，**没有任何 `WARNING` 或 `ERROR`**。如果出现 `WARNING -  Doc file 'X' contains a link to 'Y' which is not found`，说明站内相对链接断裂——按 warning 指引修对应 docs/ 文件里的链接。

- [ ] **Step 5.3: 提交**

```bash
git add mkdocs.yml
git commit -m "$(cat <<'EOF'
chore(pages): 补全 mkdocs.yml 的 nav 段

按信息架构定义侧边栏顺序：入门 / 核心概念 / 阅读路线 /
命令速查 / 上游副本导航 / 维护 / 常见问题。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: 本地预览 + 人工抽检 10 条上游外链

**Files:** none（验证步骤）

**说明：** 此 Task **不 commit**，纯人工校验。未通过则回到对应 Task 修复。

- [ ] **Step 6.1: 启动本地服务**

```bash
cd D:/Og/github/Everything-claude-code-Doc
python -m mkdocs serve
```

预期：日志末尾出现 `Serving on http://127.0.0.1:8000/`。

- [ ] **Step 6.2: 用浏览器打开 `http://127.0.0.1:8000/Everything-claude-code-Doc/`**

确认：
- 中文不乱码、字体显示正常。
- 侧边栏按预期顺序展开。
- 深浅色切换按钮可用。
- 顶部"Edit this page"图标点击跳到对应 GitHub 文件 edit 视图。

- [ ] **Step 6.3: 抽检 10 条外链**

从以下页面里各点 2 条 `https://github.com/affaan-m/ECC/...` 形式的外链：

1. `commands/most-used.md`
2. `commands/by-scenario.md`
3. `concepts/agent-vs-skill-vs-command.md`
4. `routes/index.md`
5. `upstream-navigation/by-directory.md`

共 10 条。逐条点击后到达 `github.com/affaan-m/ECC/...` 必须返回 200（GitHub 文件正常显示），不能是 404。

如果出现 404，说明上游路径已变迁——记下命中的链接，手工修对应 docs/ 页面（不要再跑迁移脚本），然后回到 Task 5 重跑 `mkdocs build --strict`，最后单独再做一次 commit 标题为 `docs(pages): 修正断链的上游 URL`。

- [ ] **Step 6.4: 停止本地服务**

按 `Ctrl+C` 终止 `mkdocs serve`。

---

## Task 7: GitHub Actions 工作流

**Files:**
- Create: `.github/workflows/deploy-pages.yml`

- [ ] **Step 7.1: 创建工作流文件**

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

- [ ] **Step 7.2: 本地校验 YAML 合法**

```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/deploy-pages.yml', encoding='utf-8'))"
```

预期：无输出。

- [ ] **Step 7.3: 提交**

```bash
git add .github/workflows/deploy-pages.yml
git commit -m "$(cat <<'EOF'
ci(pages): 新增 Deploy MkDocs to Pages 工作流

仅在 docs/、mkdocs.yml、requirements.txt 与本工作流自身
变更时触发；mkdocs build --strict 把断链升为错误，
deploy 步骤走 actions/deploy-pages 官方 action。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 8: 减薄顶层 `README.md`

**Files:**
- Modify: `README.md`

**说明：** 把 738 行减到约 70 行，仅保留：项目定位 / Pages 链接 / 快速开始 3 步 / 上游链接列表。原内容已在 `docs/` 中，无信息损失。

- [ ] **Step 8.1: 用以下完整内容**覆写 `README.md`：

```markdown
# Everything Claude Code 中文教程仓库

这是 [`affaan-m/ECC`](https://github.com/affaan-m/ECC) 的中文教程镜像仓库，主要内容已经搬到结构化的 GitHub Pages 站点。

## 中文教程站点

完整中文教程：**<https://Chasen-Liao.github.io/Everything-claude-code-Doc/>**

站点把上游的概念、命令、推荐阅读路线、上游副本导航等拆成可按需检索的多页结构，并保留与上游链接的双向跳转。本仓库根目录只做"门牌 + 入口"，权威解释都在站点里。

## 这份仓库是什么

仓库由两层组成：

- **教程层**：`docs/` 下的中文教程（由 GitHub Pages 渲染），三份顶层 .md（本 README、`ECC-COMMANDS-ZH.md`、`ECC-NAVIGATION-ZH.md`）只是门牌。
- **上游同步层**：[`everything-claude-code/`](everything-claude-code/) 是上游 ECC 的本地 gitlink 副本，由上游维护，本仓库只 fast-forward 同步。

如果你只想读教程，去 Pages 站点。如果你要核对上游真实文件内容，进入 `everything-claude-code/` 或上游官方仓库。

## 快速开始

1. 打开教程站点：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/>
2. 第一次接触 ECC：从"入门 / ECC 是什么"开始读。
3. 只想查命令：直接进"命令速查"。

## 上游官方入口

- 上游仓库主页：<https://github.com/affaan-m/ECC>
- 上游英文 README：<https://github.com/affaan-m/ECC/blob/main/README.md>
- 上游中文 README：<https://github.com/affaan-m/ECC/blob/main/README.zh-CN.md>
- 上游命令速查：<https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md>
- 上游长文指南：<https://github.com/affaan-m/ECC/blob/main/the-longform-guide.md>
- 上游短文指南：<https://github.com/affaan-m/ECC/blob/main/the-shortform-guide.md>
- 上游安全指南：<https://github.com/affaan-m/ECC/blob/main/the-security-guide.md>
- 上游故障排查：<https://github.com/affaan-m/ECC/blob/main/docs/TROUBLESHOOTING.md>

## 维护本仓库

- 同步上游 / 刷新中文文档的工作流见根目录 `CLAUDE.md` 与 [`.claude/skills/sync-upstream-zh-docs/`](.claude/skills/sync-upstream-zh-docs/)。
- 站点构建与发布走 `.github/workflows/deploy-pages.yml`。
- 站点配置见 `mkdocs.yml`，源在 `docs/`。

## License

见 [LICENSE](LICENSE)。
```

- [ ] **Step 8.2: 校验行数与必含内容**

```bash
wc -l README.md
grep -c "Chasen-Liao.github.io" README.md
grep -c "github.com/affaan-m/ECC" README.md
```

预期：
- 行数 ≤ 80（实际约 50）。
- Pages 站点 URL 出现至少 2 次。
- 上游 URL 出现至少 8 次。

- [ ] **Step 8.3: 提交**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
docs: 减薄顶层 README 为 Pages 门牌

完整中文教程已搬至 GitHub Pages 站点。
README 只保留项目定位、Pages 入口、快速开始、上游链接、
维护说明五块。原内容无损失，在 docs/ 各章节均可查到。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 9: 减薄顶层 `ECC-COMMANDS-ZH.md`

**Files:**
- Modify: `ECC-COMMANDS-ZH.md`

- [ ] **Step 9.1: 用以下完整内容覆写**：

```markdown
# ECC 命令中文速查

完整中文命令速查已经迁移到 GitHub Pages 站点：

- 速查总览：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/commands/>
- 最常用：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/commands/most-used/>
- 按场景：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/commands/by-scenario/>
- 按语言：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/commands/by-language/>

> 当前上游公开说明为 **59 个全局 slash commands**，命令文件共 **84 个**（含 `legacy-command-shims/` 兼容别名）。

## 原始来源

- 上游命令速查：<https://github.com/affaan-m/ECC/blob/main/COMMANDS-QUICK-REF.md>
- 上游命令目录：<https://github.com/affaan-m/ECC/tree/main/commands>
```

- [ ] **Step 9.2: 校验**

```bash
wc -l ECC-COMMANDS-ZH.md
grep -c "59" ECC-COMMANDS-ZH.md
grep -c "79" ECC-COMMANDS-ZH.md
```

预期：行数 ≤ 30；`59` 与 `79` 各至少 1 次。

- [ ] **Step 9.3: 提交**

```bash
git add ECC-COMMANDS-ZH.md
git commit -m "$(cat <<'EOF'
docs: 减薄 ECC-COMMANDS-ZH 为 Pages 门牌

完整命令速查已迁移到 Pages 站点。
顶层文件保留 59/79 计数与上游原始来源。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 10: 减薄顶层 `ECC-NAVIGATION-ZH.md`

**Files:**
- Modify: `ECC-NAVIGATION-ZH.md`

- [ ] **Step 10.1: 用以下完整内容覆写**：

```markdown
# ECC 上游副本导航

完整中文导航已经迁移到 GitHub Pages 站点：

- 总览：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/upstream-navigation/>
- 按目录读：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/upstream-navigation/by-directory/>

## 上游副本本体

本仓库根目录下的 [`everything-claude-code/`](everything-claude-code/) 是上游 [`affaan-m/ECC`](https://github.com/affaan-m/ECC) 的本地 gitlink 副本，由上游维护，本仓库只 fast-forward 同步，不在 Pages 站点中渲染。

如果你要核对原始文件内容、查看真实 skill / agent / rule 源码，进入 [`everything-claude-code/`](everything-claude-code/) 或上游官方仓库。
```

- [ ] **Step 10.2: 校验**

```bash
wc -l ECC-NAVIGATION-ZH.md
grep -c "Chasen-Liao.github.io" ECC-NAVIGATION-ZH.md
```

预期：行数 ≤ 30；Pages URL 至少 2 次。

- [ ] **Step 10.3: 提交**

```bash
git add ECC-NAVIGATION-ZH.md
git commit -m "$(cat <<'EOF'
docs: 减薄 ECC-NAVIGATION-ZH 为 Pages 门牌

完整上游导航已迁移到 Pages 站点。
顶层文件保留上游副本说明与跳转入口。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 11: 扩展 `sync-upstream-zh-docs` skill

**Files:**
- Modify: `.claude/skills/sync-upstream-zh-docs/SKILL.md`

**说明：** skill 当前只扫顶层三份 .md。Pages 加入后，计数（59 / 79 / 63 / 249）也散在 `docs/**`，必须同时扫描。

- [ ] **Step 11.1: 读当前 skill 内容**

```bash
cat .claude/skills/sync-upstream-zh-docs/SKILL.md
```

把当前的"扫描 / 改写"指令段定位下来，准备就地修改（每个 skill 文件结构略有差异，本步骤先读懂结构再改）。

- [ ] **Step 11.2: 修改 skill 中"扫描范围"指令**

找到 skill 里描述"扫描顶层中文文档"或"grep 顶层三份 .md"之类的段落，把扫描目标从

```
README.md ECC-COMMANDS-ZH.md ECC-NAVIGATION-ZH.md
```

改为

```
README.md ECC-COMMANDS-ZH.md ECC-NAVIGATION-ZH.md docs/**/*.md
```

具体 grep 示例命令同步改为：

```bash
grep -rnE "63 agents|249 skills|79 legacy|59 slash" \
  README.md ECC-COMMANDS-ZH.md ECC-NAVIGATION-ZH.md docs/
```

- [ ] **Step 11.3: 在 skill 的"易错点 / 边界"清单里追加一条**

在 skill 的"边界 / 注意事项 / 易错点"段（通常是文末附近）追加：

```markdown
### Pages 站点拆分页里的计数也要一起改

`docs/` 下的章节同样含有 59 / 79 / 63 / 249 这类计数。
刷新顶层三份 .md 时，必须把 `docs/**/*.md` 的同步计数一起改。
否则会出现"顶层 README 已更新但 Pages 站点显示旧数"的不一致。
```

- [ ] **Step 11.4: 提交**

```bash
git add .claude/skills/sync-upstream-zh-docs/SKILL.md
git commit -m "$(cat <<'EOF'
chore(skill): 扩展 sync-upstream-zh-docs 扫描范围

扫描目标从顶层三份 .md 扩展为顶层 + docs/**；
新增易错点：Pages 站点拆分页里的同步计数也要一起改。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 12: `CLAUDE.md` 补 "Pages 站点维护" 一节

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 12.1: 在 `CLAUDE.md` 末尾追加以下小节**

```markdown
## Pages 站点维护

本仓库的中文教程通过 GitHub Pages + MkDocs Material 发布。关键事实：

- 站点 URL：<https://Chasen-Liao.github.io/Everything-claude-code-Doc/>
- 源目录：`docs/`，MkDocs 配置 `mkdocs.yml`。
- 上游 gitlink `everything-claude-code/` 通过 `exclude_docs` 排除，**不进 build**。
- CI 工作流：`.github/workflows/deploy-pages.yml`，仅在 `docs/**`、`mkdocs.yml`、`requirements.txt` 变更时触发。
- 一次性迁移脚本 `scripts/migrate_docs.py` 已完成首版迁移，**默认不重跑**——后续编辑直接修 `docs/` 下文件即可。
- 顶层 `README.md`、`ECC-COMMANDS-ZH.md`、`ECC-NAVIGATION-ZH.md` 是 Pages 站点的门牌，不再是权威正文。改它们不会触发 Pages 重建。
- 本地预览：`python -m mkdocs serve`，严格构建：`python -m mkdocs build --strict`。

注意：编辑 `docs/` 下文件时，链接形态要遵守站内相对路径或 `https://github.com/affaan-m/ECC/...` 上游 URL 二选一，**禁止再引入 `everything-claude-code/...` 形态的相对路径**。
```

- [ ] **Step 12.2: 提交**

```bash
git add CLAUDE.md
git commit -m "$(cat <<'EOF'
docs(claude): 补 Pages 站点维护一节

记录站点 URL、源目录、CI 触发路径、迁移脚本一次性属性、
顶层 md 减薄后的角色、本地预览命令、链接形态约束。

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

---

## Task 13: 推送 + Pages 设置 + 上线验证

**Files:** none（远程操作 + 手动 UI 操作）

**说明：** 这个 Task 大部分需要用户手动在浏览器里操作，agent 只能提供命令与验收清单。

- [ ] **Step 13.1: 推送到 origin/main**

```bash
git push origin main
```

预期：成功推送 12 条新 commits（Task 1–12 各一）。

- [ ] **Step 13.2: 一次性手动设置（用户操作）**

打开浏览器到 `https://github.com/Chasen-Liao/Everything-claude-code-Doc/settings/pages`：

- **Source** 选择 **GitHub Actions**（不是 "Deploy from a branch"）。
- 保存。

这一步只做一次，之后所有部署都走 Actions。

- [ ] **Step 13.3: 等 Actions 完成**

打开 `https://github.com/Chasen-Liao/Everything-claude-code-Doc/actions`：

预期：看到一条名为 "Deploy MkDocs to Pages" 的工作流在跑，`build` 与 `deploy` 两步都打勾绿色。

如果 build 失败：点进日志，常见原因是某条站内链接的 `--strict` 检查没过。回到本地修对应 `docs/**` 文件，commit、push。

- [ ] **Step 13.4: 访问站点**

打开 `https://Chasen-Liao.github.io/Everything-claude-code-Doc/`：

按 spec 的验收标准逐条确认：

1. 中文不乱码，深浅色可切换。
2. 侧边栏按顺序展开：首页 / 入门 / 核心概念 / 阅读路线 / 命令速查 / 上游副本导航 / 维护 / 常见问题。
3. 在 `commands/most-used.md` 抽 3 条 `github.com/affaan-m/ECC/...` 链接，点击均 200。
4. 顶部"Edit this page"按钮跳到对应 GitHub edit 视图。
5. 搜索框输入"plan"能搜到 `/plan` 命令所在页面。

任何一条未通过：本地修复 → commit → push → 等 Actions 重跑 → 再验。

- [ ] **Step 13.5: 上线确认**

全部 5 条验收通过，首版上线完成。无需 commit。

---

## 全部完成后的仓库状态

```
Everything-claude-code-Doc/
├── .github/workflows/deploy-pages.yml          新增
├── .claude/skills/sync-upstream-zh-docs/        修改
├── .gitignore                                    新增
├── docs/                                         新增（16 份 .md + assets）
├── everything-claude-code/                       未变
├── scripts/migrate_docs.py                       新增
├── tests/test_migrate_docs.py                    新增
├── CLAUDE.md                                     修改
├── ECC-COMMANDS-ZH.md                            修改（减薄）
├── ECC-NAVIGATION-ZH.md                          修改（减薄）
├── LICENSE                                       未变
├── README.md                                     修改（减薄）
├── mkdocs.yml                                    新增
└── requirements.txt                              新增
```

预计 commit 数：12（Task 1–12 各 1，Task 6 与 13 不 commit）。

---

## 自查（写完本计划后）

**1. Spec 覆盖**

| Spec 章节 / 要求 | 对应 Task |
| ------ | ------ |
| 整体架构（教程层 / 上游同步层） | Task 1（mkdocs.yml exclude_docs）+ Task 7（CI paths） |
| 仓库目录结构 | Task 1–4、Task 7 全部产物 |
| 信息架构（侧边栏） | Task 5 nav |
| 内容映射 | Task 3 MAPPING + Task 4 |
| 链接重写规则 | Task 3 LINK_RULES + 单元测试 |
| 一次性迁移脚本 | Task 3 + Task 4 |
| `mkdocs.yml` | Task 1 + Task 5 |
| `requirements.txt` | Task 1 |
| CI 工作流 | Task 7 |
| 一次性手动 Pages 设置 | Task 13.2 |
| sync-upstream-zh-docs skill 扩展 | Task 11 |
| 错误处理（`--strict` 拦截 / 缓存 / 字体） | Task 5、Task 13 |
| 验收标准（5 条） | Task 13.4 |
| 关键约束（不动 gitlink / 不重写语义 / 顶层三件套 / exclude_docs 双排除） | Task 8–10 头部内容 + Task 1 mkdocs.yml |
| 首版范围：新增页骨架 | Task 2 `sync-upstream.md` 骨架 |

无遗漏。spec 中"非目标 / YAGNI"列出的所有项目（双语切换、自定义域、PR Preview、评论、Analytics、Algolia、mermaid、断链巡检）本计划均未触及。

**2. 占位扫描**：未发现 "TBD" / "TODO" / "implement later" / "appropriate error handling" 等占位措辞。每段代码块、命令、commit message 均完整可执行。

**3. 类型 / 命名一致性**：

- `rewrite_links` / `parse_h2_sections` / `build_target_files` / `main` 四个函数在 Task 3 的所有引用处签名一致。
- MAPPING 中所有 `h2_titles` 都精确对应已在源 .md 中验证存在的 H2 标题（来自我已读取的 README / ECC-COMMANDS-ZH / ECC-NAVIGATION-ZH 全文）。
- 文件路径在 Task 文件清单、`MAPPING`、`mkdocs.yml` 的 `nav` 三处一致。
- 用户名 `Chasen-Liao` 在 `mkdocs.yml`、`README.md`、`ECC-COMMANDS-ZH.md`、`ECC-NAVIGATION-ZH.md`、`CLAUDE.md` 五处保持一致。

**4. spec 偏离备注**：

- spec 信息架构里的 `docs/routes/route-1-quick.md`、`route-2-workflow.md`、`route-3-multimodel.md`、`route-4-borrow.md` 四个子页**本计划不创建**——四条路线原文每条仅 4–6 行，全部并入 `docs/routes/index.md` 一页更合理。spec 已说"新增页首版只建骨架，正文留待后续迭代"，此举与 spec 精神一致。后续 PR 如果决定把路线扩写，再单独建子页。
- spec `concepts/agent-vs-skill-vs-command.md` 一页里实际合并了 5 个 H2（agents / skills / commands / rules / hooks），文件名保留 spec 命名以避免再次偏离。

无其他偏离。

---

Plan complete and saved to `docs/superpowers/plans/2026-06-02-github-pages-tutorial-implementation.md`.

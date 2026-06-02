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
        re.compile(r"\[([^\]]+)\]\(everything-claude-code/(.*?)(/)?\)"),
        lambda m: (
            f"[{m.group(1)}]({UPSTREAM_BASE}/tree/main/{m.group(2)}{'/' if m.group(2) else ''})"
            if m.group(3) or not m.group(2)
            else f"[{m.group(1)}]({UPSTREAM_BASE}/blob/main/{m.group(2)})"
        ),
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

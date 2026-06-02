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
    assert not sections["Section B"].strip().startswith("---")
    assert not sections["Section C"].strip().startswith("---")


def test_parse_h2_sections_ignores_h1_and_intro():
    sections = parse_h2_sections(SAMPLE_MD)
    assert "Title" not in sections
    assert "intro line" not in "".join(sections.values())


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
            "h2_titles": ["C", "A"],
            "page_h1": "P",
        },
    }
    content = build_target_files(mapping, sources)["docs/page.md"]
    pos_c = content.index("## C")
    pos_a = content.index("## A")
    assert pos_c < pos_a
    assert "## B" not in content

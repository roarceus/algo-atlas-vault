"""Regenerate vault README.md with stats and topic index.

Standalone script meant to run in GitHub Actions without the algo_atlas
package installed.  Mirrors the logic in algo_atlas.utils.vault_readme.
"""

import re
import sys
from datetime import datetime
from pathlib import Path

STATS_START = "<!-- STATS:START -->"
STATS_END = "<!-- STATS:END -->"
TOPICS_START = "<!-- TOPICS:START -->"
TOPICS_END = "<!-- TOPICS:END -->"

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent


def count_problems(vault: Path) -> dict[str, int]:
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for difficulty in counts:
        d = vault / difficulty
        if d.exists():
            counts[difficulty] = sum(
                1 for f in d.iterdir() if f.is_dir() and re.match(r"^\d+\.", f.name)
            )
    return counts


def extract_topics(readme: Path) -> list[str]:
    try:
        content = readme.read_text(encoding="utf-8")
        m = re.search(r"\*\*Topics:\*\*\s*(.+?)(?:\n|$)", content)
        if m:
            return [t.strip() for t in m.group(1).split(",") if t.strip()]
    except OSError:
        pass
    return []


def scan_topics(vault: Path) -> dict[str, list[dict]]:
    index: dict[str, list[dict]] = {}
    for difficulty in ["Easy", "Medium", "Hard"]:
        d = vault / difficulty
        if not d.exists():
            continue
        for folder in d.iterdir():
            if not folder.is_dir():
                continue
            m = re.match(r"^(\d+)\.\s*(.+)$", folder.name)
            if not m:
                continue
            info = {
                "number": int(m.group(1)),
                "title": m.group(2),
                "difficulty": difficulty,
                "folder_name": folder.name,
            }
            for topic in extract_topics(folder / "README.md"):
                index.setdefault(topic, []).append(info)
    for problems in index.values():
        problems.sort(key=lambda p: p["number"])
    return index


def build_stats(counts: dict[str, int]) -> str:
    total = sum(counts.values())
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [
        STATS_START,
        "## Statistics",
        "",
        "| Difficulty | Count | Percentage |",
        "|------------|-------|------------|",
    ]
    for diff in ["Easy", "Medium", "Hard"]:
        c = counts.get(diff, 0)
        pct = round(c / total * 100) if total > 0 else 0
        lines.append(f"| {diff} | {c} | {pct}% |")
    lines.append(f"| **Total** | **{total}** | **100%** |")
    lines.append("")
    lines.append(f"*Last updated: {today}*")
    lines.append(STATS_END)
    return "\n".join(lines)


def build_topics(index: dict[str, list[dict]]) -> str:
    if not index:
        return ""
    lines = [TOPICS_START, "## Topics", ""]
    for topic in sorted(index):
        lines.append(f"### {topic}")
        lines.append("")
        for p in index[topic]:
            encoded = p["folder_name"].replace(" ", "%20")
            link = f"{p['difficulty']}/{encoded}/"
            lines.append(f"- [{p['number']}. {p['title']}]({link})")
        lines.append("")
    lines.append(TOPICS_END)
    return "\n".join(lines)


def update_section(content: str, section: str, start: str, end: str) -> str:
    if start in content and end in content:
        pattern = re.compile(rf"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL)
        return pattern.sub(section, content)
    return content.rstrip() + "\n\n" + section + "\n"


def main() -> None:
    readme = VAULT_ROOT / "README.md"
    if readme.exists():
        content = readme.read_text(encoding="utf-8")
    else:
        content = "# AlgoAtlas Vault\n\nMy documented LeetCode solutions.\n\n"

    counts = count_problems(VAULT_ROOT)
    content = update_section(content, build_stats(counts), STATS_START, STATS_END)

    topics = scan_topics(VAULT_ROOT)
    topics_md = build_topics(topics)
    if topics_md:
        content = update_section(content, topics_md, TOPICS_START, TOPICS_END)

    readme.write_text(content, encoding="utf-8")

    total = sum(counts.values())
    print(f"Updated vault README: {total} problems, {len(topics)} topics")


if __name__ == "__main__":
    main()

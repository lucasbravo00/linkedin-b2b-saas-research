#!/usr/bin/env python3
"""
collect_linkedin_posts.py
-------------------------
Organize collected LinkedIn posts into per-author markdown files under
research/linkedin-posts/<author-slug>/posts.md

WHY THIS IS A "COLLECT & ORGANIZE" SCRIPT, NOT A SCRAPER
--------------------------------------------------------
LinkedIn's Terms of Service restrict automated scraping of the feed. The robust,
ToS-respecting workflow is: you (a human) open each expert's "Recent activity →
Posts" page, copy the post text + URL + date into a CSV, and let this script turn
that into a clean, organized, annotated corpus. This is reliable, ethical, and
honestly faster than fighting anti-bot measures.

If you decide to use a licensed third-party posts API instead, you can adapt
`load_rows()` to pull from it — but that ToS decision is yours, and not the default.

Input CSV columns:  author_slug,date,url,post_text,note
  - author_slug : matches the folders/slugs used elsewhere (e.g. "anthony-pierri")
  - date        : ISO date of the post (YYYY-MM-DD) if known
  - url         : permalink to the post
  - post_text   : the post body (use quotes; newlines inside are fine in CSV)
  - note        : optional one-line annotation on why this post matters

A starter file with real post URLs lives at scripts/seeds/linkedin_posts.csv
(fill in post_text as you collect).

Usage:
  python scripts/collect_linkedin_posts.py --input scripts/seeds/linkedin_posts.csv
"""

import argparse
import csv
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "research" / "linkedin-posts"


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", (text or "")).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)[:80] or "unknown-author"


def load_rows(input_path: Path):
    with input_path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_author_file(author_slug, posts):
    folder = OUT_DIR / author_slug
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "posts.md"

    # sort newest first when dates are present
    def sort_key(p):
        return p.get("date") or "0000-00-00"

    posts = sorted(posts, key=sort_key, reverse=True)

    lines = [
        f"# LinkedIn posts — {author_slug}",
        "",
        f"- **Posts collected:** {len(posts)}",
        f"- **Last updated:** {date.today().isoformat()}",
        "",
        "> Collected for research/analysis. Text belongs to the original author; links point to source.",
        "",
        "---",
        "",
    ]
    for i, p in enumerate(posts, 1):
        d = (p.get("date") or "unknown date").strip()
        url = (p.get("url") or "").strip()
        note = (p.get("note") or "").strip()
        text = (p.get("post_text") or "").strip()
        lines.append(f"## Post {i} — {d}")
        if url:
            lines.append(f"**Source:** {url}")
        if note:
            lines.append(f"**Why it matters:** {note}")
        lines.append("")
        if text:
            # indent as a blockquote so it reads as quoted source material
            lines.extend("> " + ln if ln.strip() else ">" for ln in text.splitlines())
        else:
            lines.append("> _(post text not yet collected — paste it into the CSV)_")
        lines.append("")
        lines.append("---")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main():
    ap = argparse.ArgumentParser(description="Organize collected LinkedIn posts by author.")
    ap.add_argument("--input", required=True, help="CSV: author_slug,date,url,post_text,note")
    args = ap.parse_args()

    rows = load_rows(Path(args.input))
    by_author = defaultdict(list)
    for row in rows:
        slug = slugify(row.get("author_slug"))
        by_author[slug].append(row)

    total = 0
    for author, posts in sorted(by_author.items()):
        path = write_author_file(author, posts)
        filled = sum(1 for p in posts if (p.get("post_text") or "").strip())
        print(f"  ✓ {author}: {len(posts)} posts ({filled} with text) → {path.relative_to(REPO_ROOT)}")
        total += len(posts)

    print(f"\nDone. {total} posts across {len(by_author)} authors.")


if __name__ == "__main__":
    main()

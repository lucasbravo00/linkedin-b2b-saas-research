#!/usr/bin/env python3
"""
fetch_youtube_transcripts.py
----------------------------
Pull YouTube transcripts for the experts in this research project and save them
as annotated markdown under research/youtube-transcripts/<author-slug>/<video-id>.md

Primary method:  Supadata API  (free tier — https://supadata.ai, key in .env as SUPADATA_API_KEY)
Fallback method: youtube-transcript-api  (pip package, no key, but less robust to blocks)

Input: a CSV with columns:  author_slug,video_url,title,date
  (a starter file lives at scripts/seeds/youtube_videos.csv)

Usage:
  python scripts/fetch_youtube_transcripts.py --input scripts/seeds/youtube_videos.csv
  python scripts/fetch_youtube_transcripts.py --input scripts/seeds/youtube_videos.csv --method fallback
"""

import argparse
import csv
import os
import re
import sys
from datetime import date
from pathlib import Path

try:
    import requests
except ImportError:
    requests = None

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "research" / "youtube-transcripts"
SUPADATA_ENDPOINT = "https://api.supadata.ai/v1/youtube/transcript"


def load_env():
    """Minimal .env loader so we don't add a python-dotenv dependency."""
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())


def video_id_from_url(url: str) -> str:
    """Extract the 11-char YouTube id from common URL shapes."""
    patterns = [
        r"(?:v=|/embed/|youtu\.be/|/v/|/shorts/)([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    # last resort: a bare 11-char token
    m = re.search(r"([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else "unknown"


def fetch_supadata(url: str, api_key: str) -> str:
    """Return plain-text transcript via Supadata, or raise."""
    if requests is None:
        raise RuntimeError("requests not installed — run: pip install -r requirements.txt")
    resp = requests.get(
        SUPADATA_ENDPOINT,
        params={"url": url, "text": "true"},
        headers={"x-api-key": api_key},
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    content = data.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):  # list of {text, offset, ...} segments
        return " ".join(seg.get("text", "") for seg in content)
    raise RuntimeError(f"Unexpected Supadata response shape: {list(data.keys())}")


def fetch_fallback(url: str) -> str:
    """Free fallback using youtube-transcript-api."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        raise RuntimeError(
            "youtube-transcript-api not installed — run: pip install youtube-transcript-api"
        )
    vid = video_id_from_url(url)
    chunks = YouTubeTranscriptApi.get_transcript(vid)
    return " ".join(c["text"] for c in chunks)


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)[:80] or "untitled"


def write_transcript(author_slug, video_url, title, vid_date, transcript):
    vid = video_id_from_url(video_url)
    folder = OUT_DIR / author_slug
    folder.mkdir(parents=True, exist_ok=True)
    fname = f"{vid}-{slugify(title)}.md"
    path = folder / fname
    front = (
        f"# {title}\n\n"
        f"- **Author:** {author_slug}\n"
        f"- **Video:** {video_url}\n"
        f"- **Published:** {vid_date or 'unknown'}\n"
        f"- **Collected:** {date.today().isoformat()}\n"
        f"- **Words:** {len(transcript.split())}\n\n"
        f"> Transcript collected for research/analysis. Source belongs to the original creator.\n\n"
        f"---\n\n## Transcript\n\n"
    )
    path.write_text(front + transcript.strip() + "\n", encoding="utf-8")
    return path


def main():
    ap = argparse.ArgumentParser(description="Fetch YouTube transcripts for the research corpus.")
    ap.add_argument("--input", required=True, help="CSV: author_slug,video_url,title,date")
    ap.add_argument("--method", choices=["supadata", "fallback", "auto"], default="auto")
    args = ap.parse_args()

    load_env()
    api_key = os.environ.get("SUPADATA_API_KEY", "")

    rows = list(csv.DictReader(Path(args.input).open(encoding="utf-8")))
    if not rows:
        print("No rows in input CSV.")
        return

    ok, failed = 0, 0
    for row in rows:
        author = (row.get("author_slug") or "").strip()
        url = (row.get("video_url") or "").strip()
        title = (row.get("title") or "Untitled").strip()
        vdate = (row.get("date") or "").strip()
        if not author or not url:
            continue
        try:
            method = args.method
            if method == "auto":
                method = "supadata" if api_key else "fallback"
            transcript = (
                fetch_supadata(url, api_key) if method == "supadata" else fetch_fallback(url)
            )
            if not transcript.strip():
                raise RuntimeError("empty transcript")
            path = write_transcript(author, url, title, vdate, transcript)
            print(f"  ✓ {author}: {path.relative_to(REPO_ROOT)}")
            ok += 1
        except Exception as e:  # noqa: BLE001
            print(f"  ✗ {author}: {url}\n      {e}", file=sys.stderr)
            failed += 1

    print(f"\nDone. {ok} saved, {failed} failed.")
    if failed:
        print("Tip: try --method fallback, or add a SUPADATA_API_KEY to .env.")


if __name__ == "__main__":
    main()

# LinkedIn Organic Content Strategy for B2B SaaS — Research

A research project collecting recent, high-signal content from practitioners of **LinkedIn organic content strategy for B2B SaaS**, organized to support building a real playbook later.

> Chosen topic (from the brief): **#2 — LinkedIn organic content strategy for B2B SaaS.**
> Rationale: it's the most "meta" and directly executable option — the experts *are* LinkedIn creators, so collecting their content (the method the brief asks for) maps perfectly onto where they actually publish.

---

## What's in here

```
.
├── README.md                     ← you are here
├── research/
│   ├── sources.md                ← the 10 experts: links, dates, annotations, selection logic
│   ├── linkedin-posts/           ← posts organized by author (one folder each)
│   ├── youtube-transcripts/      ← transcripts organized by video
│   └── other/                    ← newsletters, podcasts, reports, screenshots
├── scripts/
│   ├── fetch_youtube_transcripts.py   ← pull transcripts via Supadata API (free tier) or fallback
│   ├── collect_linkedin_posts.py      ← turn collected posts into organized markdown
│   ├── seeds/                          ← starter input files (real URLs to begin from)
│   └── README.md                       ← how to run the scripts
├── docs/
│   └── git-workflow.md           ← commit-often workflow notes
├── requirements.txt
├── .env.example
└── .gitignore
```

## The 10 experts (and why)

Full annotations, links, and the coverage map are in [`research/sources.md`](research/sources.md). Short version:

| # | Expert | Project | Angle they cover |
|---|--------|---------|------------------|
| 1 | Dave Gerhardt | Exit Five | Strategy + community; LinkedIn as a brand channel |
| 2 | Anthony Pierri | Fletch PMM | Positioning + post/carousel craft |
| 3 | Finn Thormeier | Project 33 | Founder-led content *engine* (repeatable system) |
| 4 | Adam Robinson | RB2B / Retention.com | Build-in-public founder-led growth |
| 5 | Devin Reed | The Reeder | Content strategy (95:5), ex-Gong/Clari |
| 6 | Amelia Sordell | Klowt | Founder personal-branding craft |
| 7 | Sara Stella Lattanzio | advisor | Content-led GTM + distribution |
| 8 | Richard van der Blom | Just Connecting | Algorithm data / evidence base |
| 9 | Wes Kao | (ex-Maven) | Writing & communication craft |
| 10 | Emily Kramer | MKT1 | B2B SaaS marketing strategy + "LinkedIn flywheel" |

**Selection bar:** real practitioners (not commentators), specifically working in B2B SaaS, currently active (verified June 2026), and chosen so the set *together* covers strategy → engine → execution → craft → distribution → data. Names that fail the bar — including a deliberately excluded big name (Chris Walker, who exited his B2B agency in 2025) — are documented at the bottom of `sources.md` to show the list was filtered, not scraped.

## What was collected

- **`research/sources.md`** — the 10 experts with verified links, primary platforms, dates, and per-source "why chosen" annotations, plus a coverage map and an explicit "considered but excluded" section.
- **`research/linkedin-posts/<author>/`** — their recent LinkedIn posts (text + metadata), one folder per author. Seeded with real post URLs to start from (see `scripts/seeds/linkedin_posts.csv`).
- **`research/youtube-transcripts/<author>/`** — transcripts of relevant talks/podcasts/videos, fetched via the script. Seeded with real video URLs (see `scripts/seeds/youtube_videos.csv`).
- **`research/other/`** — newsletters, podcast notes, and reference reports (e.g., van der Blom's Algorithm Insights Report) that aren't LinkedIn posts or YouTube videos.

## How to use this repo

1. Install deps: `pip install -r requirements.txt`
2. Copy `.env.example` → `.env` and add your `SUPADATA_API_KEY` (free tier at supadata.ai).
3. Pull YouTube transcripts: `python scripts/fetch_youtube_transcripts.py --input scripts/seeds/youtube_videos.csv`
4. Collect LinkedIn posts (see `scripts/README.md` for the manual-collection workflow that respects LinkedIn's ToS), then `python scripts/collect_linkedin_posts.py --input scripts/seeds/linkedin_posts.csv`
5. Review, annotate, and commit in small batches (see [`docs/git-workflow.md`](docs/git-workflow.md)).

## Status

- [x] Topic chosen and justified
- [x] 10 experts found, vetted, and annotated (`sources.md`)
- [x] Repo structure + collection scripts in place
- [ ] LinkedIn posts collected per author
- [ ] YouTube transcripts pulled per video
- [ ] "Other" materials (reports, newsletters) gathered
- [ ] Playbook outline drafted from the corpus

## Notes on method & ethics

- LinkedIn's Terms of Service restrict automated scraping. The default LinkedIn workflow here is **manual/assisted collection** (you copy the post text + URL into a CSV; the script organizes it). If you choose to use a third-party posts API, that's your call to make against their ToS — it's not the default.
- Everything stored here is for **research/analysis**. Post text is kept for study; always attribute and link back to the original author.

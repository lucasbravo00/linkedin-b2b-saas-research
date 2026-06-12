# Scripts

Two small, dependency-light collectors. Both write into `research/`.

## Setup

```bash
pip install -r ../requirements.txt          # from repo root: pip install -r requirements.txt
cp ../.env.example ../.env                   # then add your SUPADATA_API_KEY
```

---

## 1. `fetch_youtube_transcripts.py`

Pulls transcripts and saves them to `research/youtube-transcripts/<author-slug>/<video-id>-<title>.md`.

```bash
# uses Supadata if SUPADATA_API_KEY is set, else falls back automatically
python scripts/fetch_youtube_transcripts.py --input scripts/seeds/youtube_videos.csv

# force the free fallback (youtube-transcript-api, no key)
python scripts/fetch_youtube_transcripts.py --input scripts/seeds/youtube_videos.csv --method fallback
```

**Input CSV:** `author_slug,video_url,title,date`

**Where to find more videos to add** (high-signal channels/shows for this corpus):
- Dave Gerhardt → Exit Five podcast on YouTube ("How to Master LinkedIn for B2B", etc.)
- Anthony Pierri → Fletch PMM talks + Exit Five guest episodes (two are seeded)
- Finn Thormeier → "The Founder-Led Marketing Show" (Project 33)
- Devin Reed → "Reed Between the Lines"
- Adam Robinson → GTMnow / SaaStock / podcast guest spots
- Richard van der Blom → his algorithm-report webinars

Add rows to `seeds/youtube_videos.csv` (or your own CSV) and re-run.

---

## 2. `collect_linkedin_posts.py`

Organizes collected posts into `research/linkedin-posts/<author-slug>/posts.md`, newest first.

```bash
python scripts/collect_linkedin_posts.py --input scripts/seeds/linkedin_posts.csv
```

**Input CSV:** `author_slug,date,url,post_text,note`

### The LinkedIn collection workflow (ToS-respecting)

LinkedIn restricts automated feed scraping, so the default here is **manual/assisted collection** — reliable and ethical:

1. Open the expert's profile → **Recent activity** → **Posts**.
2. For each post worth keeping, copy into a new row of your CSV:
   - the **URL** (click the post's "⋯" → Copy link to post),
   - the **date**,
   - the **post text** (wrap in quotes; line breaks inside quotes are fine),
   - a one-line **note** on why it matters (the annotation makes the corpus playbook-ready).
3. Run the script. Re-run any time you add rows — it rewrites each author's `posts.md`.

Aim for ~5–10 *strong* posts per author rather than everything. The brief rewards signal, not volume.

> If you'd rather use a licensed third-party LinkedIn posts API, adapt `load_rows()` in the script to read from it. That ToS decision is yours to make — it isn't the default here.

---

## Commit as you go

Don't batch everything into one giant commit. See [`../docs/git-workflow.md`](../docs/git-workflow.md). A good rhythm: one commit per author once their posts + transcripts are in.

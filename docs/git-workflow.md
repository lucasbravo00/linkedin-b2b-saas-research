# Git workflow — commit small, commit often

One of the explicit evaluation criteria is *"commit and push regularly (not one giant
commit at the end)."* This file is a suggested rhythm.

## First push

```bash
git init
git add README.md research/sources.md docs/ scripts/ requirements.txt .env.example .gitignore
git commit -m "Set up repo: topic, 10 vetted experts, structure, collection scripts"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## A commit rhythm that tells a story

Make each commit a meaningful unit of progress:

```bash
# after vetting/annotating sources
git commit -m "Add and annotate 10 experts in sources.md"

# one commit per author as you collect their material
git commit -m "Collect Anthony Pierri: 8 LinkedIn posts + 2 transcripts"
git commit -m "Collect Finn Thormeier: founder-led content engine posts"
git commit -m "Collect Devin Reed: 95:5 content-strategy posts + transcript"
# ...repeat per author...

# reference materials
git commit -m "Add other/: algorithm report notes + MKT1 LinkedIn flywheel summary"

# synthesis
git commit -m "Draft playbook outline from corpus"
```

## Tips

- Push after every 1–3 commits so progress is visible, not dumped at the end.
- Keep secrets out: `.env` is gitignored — never commit your API key.
- Empty folders don't track in git; the `.gitkeep` files keep the structure visible
  until real content lands (delete a `.gitkeep` once that folder has files).
- Write commit messages in the imperative ("Add…", "Collect…", "Fix…").

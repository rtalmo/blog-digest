# Blog Digest

A running, topic-classified digest of the Salesforce Developer and Admin blogs.
Each post gets a 3-5 bullet summary, topics, annotated links, suggested tasks, and
Read / Done checkboxes.

## Daily flow

`scripts/refresh.sh` runs: ingest (RSS) -> enrich links -> curate new posts with
headless Claude -> build `site/index.html`. Only new posts are sent to Claude.

Run it by hand: `scripts/refresh.sh`

## Scheduling (macOS launchd, runs daily at 7:00 if the Mac is awake, else on wake)

    cp scripts/com.rtalmo.blogdigest.plist ~/Library/LaunchAgents/
    launchctl load ~/Library/LaunchAgents/com.rtalmo.blogdigest.plist

Logs: `logs/refresh.log`. Unload with `launchctl unload ...`.

## Hosting (persistent URL)

`docs/` is a single static file. Easiest: GitHub Pages from a repo.

    git init && git add -A && git commit -m "Initial digest"
    gh repo create blog-digest --public --source=. --push
    # Settings -> Pages -> deploy from branch, folder /docs

`refresh.sh` commits and pushes after each run, so the hosted site updates daily.
The repo is public. `.gitignore` keeps `raw/`, `tasks/` and `logs/` out of it, so only
the site, scripts, and summaries are published.

## Read / Done state

Checkboxes are stored in the browser (localStorage), per device. Use
"Export progress" / "Import" in the site header to move state between devices.

## Layout

    raw/<source>/posts/*.json   ingested posts (full text + links)
    data/curation.json          summaries, topics, tasks
    data/link_meta.json         cached link titles/descriptions
    data/posts/<source>/*.md    per-post markdown
    tasks/backlog.md            suggested tasks by topic
    docs/index.html             the website (GitHub Pages serves this folder)

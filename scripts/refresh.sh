#!/bin/zsh
# Daily refresh: ingest new posts, enrich links, summarize/classify new ones, rebuild the site.
# Only posts not yet in data/curation.json are sent to Claude, so a normal day is 0-3 calls.
set -eu
ROOT="${0:A:h:h}"
SINCE="${SINCE:-$(date -v-90d +%Y-%m-%d)}"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/bin:/bin:$PATH"

echo "== $(date) refresh (since $SINCE)"
python3 -I "$ROOT/scripts/ingest.py" https://developer.salesforce.com/blogs/feed dev "$ROOT/raw/dev/posts" "$SINCE"
python3 -I "$ROOT/scripts/ingest.py" https://admin.salesforce.com/feed admin "$ROOT/raw/admin/posts" "$SINCE"
python3 -I "$ROOT/scripts/enrich_links.py" "$ROOT"
python3 -I "$ROOT/scripts/curate.py" "$ROOT" </dev/null
python3 -I "$ROOT/scripts/build.py" "$ROOT"

# Publish only if this folder is a git repo with a remote (see README).
# .gitignore keeps raw/, tasks/ and logs/ out of the commit.
if [ -d "$ROOT/.git" ] && git -C "$ROOT" remote | grep -q .; then
  git -C "$ROOT" add -A
  git -C "$ROOT" diff --cached --quiet || git -C "$ROOT" commit -qm "Daily refresh $(date +%F)

Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>"
  git -C "$ROOT" push -q
fi
echo "== done"

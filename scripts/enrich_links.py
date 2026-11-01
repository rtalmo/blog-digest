"""Fetch <title> and meta description for every useful link in the curated posts.

Results are cached in data/link_meta.json so reruns only fetch new URLs.

Usage: python3 -I enrich_links.py <project_root>
"""
import glob
import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser

root = sys.argv[1]
cache_path = f"{root}/data/link_meta.json"
cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}

NOISE = ("/blogs/author", "linkedin.com", "x.com/", "bsky.app", "developer.salesforce.com/blogs/tag")


class Meta(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title, self.desc, self._in_title = "", "", False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = (a.get("name") or a.get("property") or "").lower()
            if name in ("description", "og:description") and not self.desc:
                self.desc = a.get("content") or ""
            if name == "og:title" and not self.title:
                self.title = a.get("content") or ""

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title and not self.title:
            self.title = data


def fetch_meta(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 blog-digest/0.1"})
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read(300_000).decode("utf-8", "replace")
        m = Meta()
        m.feed(raw)
        return url, {"title": " ".join(m.title.split()), "desc": " ".join(m.desc.split())}
    except Exception as e:
        return url, {"title": "", "desc": "", "error": str(e)[:80]}


urls = set()
for f in glob.glob(f"{root}/raw/*/posts/*.json"):
    key = os.path.basename(f)[:-5]
    if key not in json.load(open(f"{root}/data/curation.json")):
        continue
    p = json.load(open(f))
    for l in p["links"]:
        if not any(n in l["url"] for n in NOISE) and not l["url"].startswith(p["url"]):
            urls.add(l["url"])

todo = [u for u in urls if u not in cache]
print(f"{len(urls)} links, {len(todo)} to fetch")
with ThreadPoolExecutor(8) as ex:
    for url, meta in ex.map(fetch_meta, todo):
        cache[url] = meta
json.dump(cache, open(cache_path, "w"), indent=1)
ok = sum(1 for u in urls if cache[u]["title"])
print(f"{ok}/{len(urls)} have a title")

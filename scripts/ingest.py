"""Fetch a WordPress blog feed (paginated) and write one JSON record per post.

Usage: python3 -I ingest.py <feed_url> <source> <out_dir> <since YYYY-MM-DD>
"""
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


class LinkParser(HTMLParser):
    """Collects link hrefs with anchor text and the sentence-ish context around each."""

    def __init__(self):
        super().__init__()
        self.links, self.text = [], []
        self._href, self._anchor, self._pos = None, [], 0

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href and href.startswith("http"):
                self._href, self._anchor = href, []
                self._pos = sum(len(t) for t in self.text)

    def handle_endtag(self, tag):
        if tag == "a" and self._href:
            self.links.append({"href": self._href, "anchor": " ".join("".join(self._anchor).split()),
                               "pos": self._pos})
            self._href = None

    def handle_data(self, data):
        self.text.append(data)
        if self._href:
            self._anchor.append(data)

    def context(self, pos, width=220):
        full = "".join(self.text)
        start = max(0, pos - width)
        snippet = full[start:pos + width]
        return " ".join(snippet.split())


def link_type(url):
    if "github.com" in url:
        return "repo"
    if "trailhead.salesforce.com" in url:
        return "trailhead"
    if "help.salesforce.com" in url or "developer.salesforce.com/docs" in url:
        return "docs"
    if "release-notes" in url or "releasenotes" in url:
        return "release-note"
    return "other"


class OgImage(HTMLParser):
    image = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and a.get("property") == "og:image" and not self.image:
            self.image = a.get("content")


def og_image(url):
    try:
        parser = OgImage()
        parser.feed(fetch(url)[:200_000].decode("utf-8", "replace"))
        return parser.image
    except Exception:
        return None


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "blog-digest/0.1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main(feed_url, source, out_dir, since):
    since_dt = datetime.fromisoformat(since).replace(tzinfo=timezone.utc)
    posts, page, done = [], 1, False
    while not done:
        try:
            root = ET.fromstring(fetch(f"{feed_url}?paged={page}"))
        except Exception as e:  # past the last page the feed 404s
            print(f"page {page}: stop ({e})")
            break
        items = root.findall("./channel/item")
        if not items:
            break
        for it in items:
            date = parsedate_to_datetime(it.findtext("pubDate"))
            if date < since_dt:
                done = True
                continue
            body = it.findtext("content:encoded", namespaces=NS) or ""
            p = LinkParser()
            p.feed(body)
            links, seen = [], set()
            for l in p.links:
                u = l["href"].split("#")[0]
                if u not in seen:
                    seen.add(u)
                    links.append({"url": u, "type": link_type(u), "anchor": l["anchor"],
                                  "context": p.context(l["pos"])})
            posts.append({
                "title": it.findtext("title"),
                "url": it.findtext("link"),
                "source": source,
                "date": date.date().isoformat(),
                "authors": [it.findtext("dc:creator", namespaces=NS)],
                "hero": (it.find("media:thumbnail", {"media": "http://search.yahoo.com/mrss/"}) is not None
                         and it.find("media:thumbnail", {"media": "http://search.yahoo.com/mrss/"}).get("url")),
                "feed_categories": [c.text for c in it.findall("category")],
                "links": links,
                "text": re.sub(r"\s+", " ", "".join(p.text)).strip(),
            })
        print(f"page {page}: {len(items)} items, total kept {len(posts)}")
        page += 1
    import os
    os.makedirs(out_dir, exist_ok=True)
    for post in posts:
        slug = post["url"].rstrip("/").rsplit("/", 1)[-1]
        path = f"{out_dir}/{post['date']}-{slug}.json"
        if not post["hero"]:
            # reuse a previously found image; otherwise read og:image from the post page
            old = json.load(open(path)).get("hero") if os.path.exists(path) else None
            post["hero"] = old or og_image(post["url"])
        with open(path, "w") as f:
            json.dump(post, f, indent=2)
    print(f"wrote {len(posts)} posts to {out_dir}")


if __name__ == "__main__":
    main(*sys.argv[1:5])

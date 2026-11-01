"""Merge raw posts + curation into markdown posts, index.json, backlog and site.

Usage: python3 -I build.py <project_root>
"""
import glob
import html
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone

root = sys.argv[1]
curation = json.load(open(f"{root}/data/curation.json"))
link_meta = json.load(open(f"{root}/data/link_meta.json")) if os.path.exists(f"{root}/data/link_meta.json") else {}
GENERIC = {"", "Salesforce Help", "Salesforce Developers"}
posts = []
for f in sorted(glob.glob(f"{root}/raw/*/posts/*.json"), reverse=True):
    key = os.path.basename(f)[:-5]
    if key not in curation:
        continue
    p = json.load(open(f))
    p.update(curation[key])
    p["key"] = f"{p['source']}/{key}"
    posts.append(p)
posts.sort(key=lambda p: p["date"], reverse=True)

NOISE = ("/blogs/author", "linkedin.com", "x.com/", "bsky.app", "twitter.com", "facebook.com",
         "developer.salesforce.com/blogs/tag", "admin.salesforce.com/blog/author")


def useful_links(p):
    out = []
    for l in p["links"]:
        if (any(n in l["url"] for n in NOISE) or l["url"].rstrip("/") in
                ("https://developer.salesforce.com/blogs", "https://admin.salesforce.com/blog")
                or l["url"].startswith(p["url"])):
            continue
        m = link_meta.get(l["url"], {})
        title = m.get("title", "")
        # page titles often end in "| Salesforce Developers"; keep the informative part
        title = title.split(" | ")[0] if title.split(" | ")[0] not in GENERIC else ""
        out.append({**l, "label": title or l["anchor"] or l["url"],
                    "desc": m.get("desc", ""), "mentioned_as": l["anchor"]})
    return out


# per-post markdown
for p in posts:
    d = f"{root}/data/posts/{p['source']}"
    os.makedirs(d, exist_ok=True)
    lines = ["---", f"title: {json.dumps(p['title'])}", f"url: {p['url']}", f"source: {p['source']}",
             f"date: {p['date']}", f"authors: {json.dumps([a for a in p['authors'] if a])}",
             f"topics: {json.dumps(p['topics'])}", "---", ""]
    lines += [f"- {b}" for b in p["summary"]]
    lines += ["", "## Links"]
    for l in useful_links(p):
        lines.append(f"- **{l['label']}** [{l['type']}]: {l['desc'] or 'no description available'}  ")
        if l["mentioned_as"] and l["mentioned_as"] != l["label"]:
            lines.append(f"  Mentioned as \"{l['mentioned_as']}\"  ")
        lines.append(f"  {l['url']}")
    lines += ["", "## Suggested tasks"]
    lines += [f"- [ ] {t['title']} ({t['effort']})" for t in p["tasks"]] or ["_none_"]
    open(f"{d}/{p['key'].split('/')[1]}.md", "w").write("\n".join(lines) + "\n")

# index
json.dump([{k: p[k] for k in ("key", "title", "url", "source", "date", "topics")} for p in posts],
          open(f"{root}/data/index.json", "w"), indent=2)

# backlog (suggestions only; the site tracks what you tick)
order = {"S": 0, "M": 1, "L": 2}
by_topic = defaultdict(list)
for p in posts:
    for t in p["tasks"]:
        by_topic[p["topics"][0]].append((t, p))
out = ["# Backlog", "", "## Accepted", "", "_(move suggestions here to accept them)_", "",
       "## Suggested", ""]
for topic in sorted(by_topic):
    out.append(f"### {topic}")
    for t, p in sorted(by_topic[topic], key=lambda x: order[x[0]["effort"]]):
        out.append(f"- [ ] **{t['title']}** ({t['effort']}), from [{p['title']}]({p['url']}) [{p['source']}, {p['date']}]")
    out.append("")
os.makedirs(f"{root}/tasks", exist_ok=True)
open(f"{root}/tasks/backlog.md", "w").write("\n".join(out))

# site
e = html.escape
topic_counts = defaultdict(int)
for p in posts:
    for t in p["topics"]:
        topic_counts[t] += 1

cards = []
for p in posts:
    ul = useful_links(p)
    links = "".join(
        f'<li><span class="lt">{e(l["type"])}</span><div><a href="{e(l["url"])}" target="_blank" rel="noopener">{e(l["label"])} ↗</a>'
        + (f'<div class="ld">{e(l["desc"])}</div>' if l["desc"] else "")
        + (f'<div class="lm">Mentioned as “{e(l["mentioned_as"])}”</div>' if l["mentioned_as"] and l["mentioned_as"] != l["label"] else "")
        + '</div></li>' for l in ul)
    hero = f'<img class="hero" src="{e(p["hero"])}" alt="" loading="lazy">' if p.get("hero") else ""
    tasks = "".join(
        f'<label class="task"><input type="checkbox" data-task="{e(p["key"])}#{i}"> <span>{e(t["title"])}</span> <em class="eff">{t["effort"]}</em></label>'
        for i, t in enumerate(p["tasks"]))
    authors = e(", ".join(a for a in p["authors"] if a))
    cards.append(f"""<article data-key="{e(p['key'])}" data-topics="{e('|'.join(p['topics']))}" data-source="{p['source']}">
{hero}<div class="meta"><span class="src {p['source']}">{'DEV' if p['source'] == 'dev' else 'ADMIN'}</span><span>{p['date']}</span>{f'<span>· {authors}</span>' if authors else ''}</div>
<h2><a href="{e(p['url'])}" target="_blank" rel="noopener">{e(p['title'])}</a></h2>
<div class="tags">{''.join(f'<span>{e(t)}</span>' for t in p['topics'])}</div>
<ul class="sum">{''.join(f'<li>{e(b)}</li>' for b in p['summary'])}</ul>
{f'<details class="links"><summary>{len(ul)} links</summary><ul>{links}</ul></details>' if ul else ''}
{f'<div class="tasks"><div class="th">Suggested tasks</div>{tasks}</div>' if tasks else ''}
<div class="status">
<label class="chk read"><input type="checkbox" data-read> Read</label>
<label class="chk done"><input type="checkbox" data-done> Done (work complete)</label>
</div>
</article>""")

nav = "".join(f'<a href="#" data-t="{e(t)}"><span>{e(t)}</span><b>{n}</b></a>'
              for t, n in sorted(topic_counts.items(), key=lambda x: -x[1]))
updated = datetime.now(timezone.utc).strftime("%b %d, %Y %H:%M UTC")

page = """<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Blog Digest</title>
<style>
:root{--bg:#f4f6f9;--card:#fff;--ink:#16202a;--mute:#5c6a78;--line:#e1e6ec;--brand:#0b5cab;--brand2:#032d60;--soft:#e8f2fd;--ok:#2e844a;--okbg:#e6f5ea}
@media(prefers-color-scheme:dark){:root{--bg:#10151a;--card:#1a2129;--ink:#e8ecf0;--mute:#9aa7b4;--line:#2a343e;--brand:#6db3f8;--brand2:#0a1a2e;--soft:#1f2c3a;--ok:#5cc47a;--okbg:#18291f}}
*{box-sizing:border-box}body{margin:0;font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif;color:var(--ink);background:var(--bg)}
header{position:sticky;top:0;z-index:5;background:var(--brand2);color:#fff;padding:10px 20px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
header h1{font-size:16px;margin:0;letter-spacing:.08em}header input[type=search]{flex:1;min-width:180px;max-width:360px;padding:7px 12px;border-radius:8px;border:0;font:inherit}
.prog{margin-left:auto;font-size:12px;opacity:.9;text-align:right}.bar{height:5px;background:#ffffff33;border-radius:3px;width:160px;margin-top:3px;overflow:hidden}.bar i{display:block;height:100%;background:#6ee7a0;width:0}
.wrap{display:flex;max-width:1180px;margin:0 auto}
aside{width:236px;flex:none;padding:18px 14px;position:sticky;top:52px;align-self:flex-start;max-height:calc(100vh - 52px);overflow:auto}
aside h3{font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--mute);margin:14px 8px 6px}
aside a{display:flex;justify-content:space-between;padding:6px 10px;color:var(--ink);text-decoration:none;border-radius:8px;font-size:14px}
aside a b{font-weight:500;color:var(--mute);font-size:12px}aside a:hover{background:var(--soft)}aside a.on{background:var(--soft);color:var(--brand);font-weight:600}
main{flex:1;min-width:0;padding:18px 20px 60px}
.updated{font-size:12px;color:var(--mute);margin-bottom:12px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.updated button{font:inherit;font-size:12px;background:none;border:1px solid var(--line);color:var(--mute);border-radius:6px;padding:2px 8px;cursor:pointer}
article{position:relative;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-bottom:14px;box-shadow:0 1px 2px #0000000a}
article.isread{opacity:.82}article.isdone{border-left:4px solid var(--ok)}article.isdone h2 a{text-decoration:line-through;text-decoration-color:#0004}
.hero{float:right;width:132px;height:88px;object-fit:cover;border-radius:8px;margin:0 0 8px 16px;border:1px solid var(--line)}
article::after{content:"";display:block;clear:both}
.meta{font-size:12px;color:var(--mute);display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.src{color:#fff;border-radius:4px;padding:1px 7px;font-weight:600;font-size:11px;letter-spacing:.04em}.src.dev{background:#0b5cab}.src.admin{background:#9050e9}
h2{font-size:18px;line-height:1.3;margin:6px 0 8px}h2 a{color:var(--ink);text-decoration:none}h2 a:hover{color:var(--brand)}
.tags span{font-size:12px;background:var(--soft);color:var(--brand);border-radius:99px;padding:2px 10px;margin-right:6px;display:inline-block}
.sum{margin:10px 0 4px;padding-left:20px}.sum li{margin:4px 0}
.links summary,.tasks .th{cursor:pointer;font-size:12px;font-weight:600;color:var(--mute);text-transform:uppercase;letter-spacing:.06em;margin-top:10px}
.links ul{list-style:none;padding:0;margin:8px 0 0}.links li{display:flex;gap:10px;margin:9px 0;font-size:13px}
.lt{flex:none;width:70px;font-size:10px;text-transform:uppercase;letter-spacing:.06em;color:var(--mute);padding-top:3px}
.links li a{color:var(--brand);font-weight:600;text-decoration:none}.links li a:hover{text-decoration:underline}
.ld{color:var(--mute)}.lm{font-size:12px;color:var(--mute);font-style:italic}
.tasks{background:var(--soft);border-radius:8px;padding:8px 12px;margin-top:12px}.tasks .th{margin:0 0 4px;cursor:default}
.task{display:flex;gap:8px;align-items:baseline;font-size:13.5px;margin:3px 0;cursor:pointer}.task input:checked+span{text-decoration:line-through;color:var(--mute)}
.eff{font-style:normal;font-size:10px;font-weight:700;border:1px solid var(--line);border-radius:4px;padding:0 5px;color:var(--mute);background:var(--card)}
.status{display:flex;gap:18px;margin-top:12px;padding-top:10px;border-top:1px solid var(--line)}
.chk{font-size:13px;font-weight:600;cursor:pointer;display:flex;gap:6px;align-items:center;color:var(--mute)}.chk:has(input:checked){color:var(--ok)}
input[type=checkbox]{accent-color:var(--ok);width:16px;height:16px;margin:0}
.empty{text-align:center;color:var(--mute);padding:40px}
@media(max-width:760px){aside{display:none}.hero{width:96px;height:64px}.prog{display:none}}
</style>
<header><h1>BLOG DIGEST</h1><input type="search" id="q" placeholder="Search posts, links, tasks…">
<div class="prog"><span id="progtxt"></span><div class="bar"><i id="progbar"></i></div></div></header>
<div class="wrap"><aside>
<h3>Status</h3><div id="statusnav">
<a href="#" data-s="all" class="on"><span>All</span><b id="n-all"></b></a>
<a href="#" data-s="unread"><span>Unread</span><b id="n-unread"></b></a>
<a href="#" data-s="read"><span>Read, not done</span><b id="n-read"></b></a>
<a href="#" data-s="done"><span>Done</span><b id="n-done"></b></a>
</div>
<h3>Source</h3><div id="srcnav">
<a href="#" data-src="" class="on"><span>Dev + Admin</span></a>
<a href="#" data-src="dev"><span>Developer blog</span></a>
<a href="#" data-src="admin"><span>Admin blog</span></a>
</div>
<h3>Topics</h3><div id="topicnav"><a href="#" data-t="" class="on"><span>All topics</span><b>__N__</b></a>__NAV__</div>
</aside>
<main><div class="updated"><span>Updated __UPDATED__</span><button id="export">Export progress</button><button id="import">Import</button><span id="count"></span></div>
__CARDS__
<div class="empty" id="empty" hidden>No posts match these filters.</div>
</main></div>
<script>
const KEY="blog-digest-state-v1";
let st=JSON.parse(localStorage.getItem(KEY)||'{"read":{},"done":{},"task":{}}');
const save=()=>localStorage.setItem(KEY,JSON.stringify(st));
let topic="",status="all",src="";
const q=document.getElementById("q"),arts=[...document.querySelectorAll("article")];
function paint(){
  arts.forEach(a=>{const k=a.dataset.key,d=!!st.done[k],r=d||!!st.read[k];
    a.classList.toggle("isdone",d);a.classList.toggle("isread",r&&!d);
    a.querySelector("[data-read]").checked=r;a.querySelector("[data-done]").checked=d;
    a.querySelectorAll("[data-task]").forEach(c=>c.checked=!!st.task[c.dataset.task])});
  filter();
}
function filter(){
  let n=0,c={all:0,unread:0,read:0,done:0};
  arts.forEach(a=>{const k=a.dataset.key,d=!!st.done[k],r=!!st.read[k]&&!d,u=!d&&!r;
    const s=d?"done":r?"read":"unread";
    const ok=(!topic||a.dataset.topics.split("|").includes(topic))&&(!src||a.dataset.source===src)&&a.textContent.toLowerCase().includes(q.value.toLowerCase());
    if(ok){c.all++;c[s]++}
    const show=ok&&(status==="all"||status===s);a.hidden=!show;n+=show});
  for(const k in c)document.getElementById("n-"+k).textContent=c[k];
  document.getElementById("count").textContent=n+" shown";
  document.getElementById("empty").hidden=n>0;
  const tot=arts.length,dn=arts.filter(a=>st.done[a.dataset.key]).length,rd=arts.filter(a=>st.read[a.dataset.key]||st.done[a.dataset.key]).length;
  document.getElementById("progtxt").textContent=rd+" of "+tot+" read · "+dn+" done";
  document.getElementById("progbar").style.width=(tot?100*rd/tot:0)+"%";
}
arts.forEach(a=>{const k=a.dataset.key;
  a.querySelector("[data-read]").onchange=e=>{st.read[k]=e.target.checked;if(!e.target.checked)delete st.done[k];save();paint()};
  a.querySelector("[data-done]").onchange=e=>{if(e.target.checked){st.done[k]=1;st.read[k]=1}else delete st.done[k];save();paint()};
  a.querySelectorAll("[data-task]").forEach(c=>c.onchange=()=>{st.task[c.dataset.task]=c.checked;save()});
});
function nav(sel,attr,set){document.querySelectorAll(sel+" a").forEach(l=>l.onclick=ev=>{ev.preventDefault();set(l.dataset[attr]);
  document.querySelectorAll(sel+" a").forEach(x=>x.classList.toggle("on",x===l));filter()})}
nav("#statusnav","s",v=>status=v);nav("#srcnav","src",v=>src=v);nav("#topicnav","t",v=>topic=v);
q.oninput=filter;
document.getElementById("export").onclick=()=>{const a=document.createElement("a");a.href=URL.createObjectURL(new Blob([JSON.stringify(st,null,1)],{type:"application/json"}));a.download="blog-digest-progress.json";a.click()};
document.getElementById("import").onclick=()=>{const i=document.createElement("input");i.type="file";i.accept=".json";i.onchange=async()=>{try{st=JSON.parse(await i.files[0].text());save();paint()}catch(x){alert("Not a valid progress file")}};i.click()};
paint();
</script></html>"""
page = (page.replace("__N__", str(len(posts))).replace("__NAV__", nav)
        .replace("__UPDATED__", updated).replace("__CARDS__", "\n".join(cards)))
os.makedirs(f"{root}/docs", exist_ok=True)
open(f"{root}/docs/index.html", "w").write(page)
print(f"built {len(posts)} posts")

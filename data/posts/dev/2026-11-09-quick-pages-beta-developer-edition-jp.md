---
title: "Quick Pages (Beta) \u3092 Developer Edition \u3067\u8a66\u3059 : \u6709\u52b9\u5316\u304b\u3089\u30da\u30fc\u30b8\u306e\u4f5c\u6210\u307e\u3067"
url: https://developer.salesforce.com/blogs/2026/11/quick-pages-beta-developer-edition-jp
source: dev
date: 2026-11-09
authors: ["Hiroyuki Inaba"]
topics: ["LWC / UI", "Agentforce & AI", "Releases"]
---

- Quick Pages (Beta, Winter '27) lets users describe a page in natural language and an agent builds a React-based single-page app with live preview, using live org data (including custom objects and fields) with tiles, charts, tables and tabs.
- It works on Lightning Experience Enterprise/Performance/Unlimited/Developer Edition orgs with Foundations on Hyperforce, and requires Multi-Framework Apps domain enabled, Salesforce Edge Network on, and Einstein turned on.
- Setup is to toggle Quick Pages on in Setup, then assign the 'Create and View Quick Pages (Beta)' permission set to creators or 'View Quick Pages (Beta)' to viewers; no admin rights are needed to build pages.
- Pages can be refined via chat or suggested 'NEXT' prompts (e.g. sorting, a phase filter dropdown), then saved and shared with individuals, public groups or the whole org, and viewers only see data they already have access to.
- Beta caveats: pages are read-only (no create/update/delete), prompts over about 2 minutes time out, page names can't be changed after saving, Japanese IME Enter can send prematurely, there is no Apex/Connect REST/Data 360/external API access, and no packaging or data-export migration.

## Links
- **Introducing Quick Pages（Salesforce ブログ）** [other]: no description available  
  https://www.salesforce.com/blog/introducing-quick-pages-builder-tool/
- **Bring Custom UIs to Life with Quick Pages (Beta)（Winter ’27 リリースノート）** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_quick_pages_beta.htm&release=264&type=5
- **Considerations and Limitations for Quick Pages (Beta)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.quick_pages_considerations.htm&type=5
- **Set Up Quick Pages (Beta)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.quick_pages_setup.htm&type=5
- **Create and Share Quick Pages (Beta)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.quick_pages_create.htm&type=5

## Suggested tasks
- [ ] Enable Quick Pages in a fresh Developer Edition, assign the Create permission set, and build an opportunity dashboard (S)
- [ ] Run the sample-data Anonymous Apex script and iterate on the page with 3-4 chat refinements, noting timeouts and IME issues (S)
- [ ] Share a saved Quick Page with a user holding restricted permissions and verify they see only the data they can access (M)

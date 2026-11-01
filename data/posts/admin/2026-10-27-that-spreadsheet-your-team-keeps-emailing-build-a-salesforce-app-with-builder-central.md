---
title: "That Spreadsheet Your Team Keeps Emailing? Build a Salesforce App With Builder Central"
url: https://admin.salesforce.com/blog/2026/that-spreadsheet-your-team-keeps-emailing-build-a-salesforce-app-with-builder-central
source: admin
date: 2026-10-27
authors: ["mgerholdt@salesforce.com"]
topics: ["Flow & Automation", "Agentforce & AI", "Releases"]
---

- Builder Central is an AI-powered conversational workspace (currently in beta) where Admins plan, build, preview and deploy Salesforce solutions such as apps, agents, flows, custom objects, fields and permission sets using plain language.
- The author recreated an old Object Creator demo, a 'Bulk Delivery Management' app with a custom 'Bulk Delivery' object, from a single prompt, with no spreadsheet or Object Manager work, and it took about 12 minutes in real time.
- Builder Central first produces a project plan for review, then builds in a separate workspace where nothing reaches the org until you publish, and it can also assign the permission set and create list views on request.
- The generated record page was missing some fields, so the author fixed it in Lightning App Builder, which shows the conversational and declarative tools can be used together.
- The author recommends trying it in a sandbox first and reviewing the plan, permissions, automation and UX as usual, and notes that the beta has limitations to check; at general availability it is intended to become the single place to manage and configure sandbox and production orgs.

## Links
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20261026100852/Image-1-Spreadsheet.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20261026100852/Image-1-Spreadsheet.png
- **hands-on with Builder Central in a sandbox** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.builder_central_set_up.htm&type=5
- **limitations** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.builder_central_limitations.htm&type=5
- **Build apps by describing them: conversational app creator** [trailhead]: Builder Central lets admins and builders describe an app in plain language and get a full plan and preview. This conversational app creator generates objects, pages  
  Mentioned as "Get to Know Builder Central"  
  https://trailhead.salesforce.com/content/learn/modules/builder-central-quick-look/get-to-know-builder-central
- **Dreamforce 2026 Product Highlights for Admins - Salesforce Admins** [other]: Admin keynote at Dreamforce 2026: Build trusted AI, deliver trusted AI everywhere and govern AI  
  Mentioned as "Dreamforce Highlights for Admins"  
  https://admin.salesforce.com/blog/2026/dreamforce-2026-product-highlights-for-admins
- **Builder Central: The Ultimate Salesforce AI Development Hub** [other]: Introducing the all-in-one workspace to build, configure, and deploy agents, apps, and experiences on Salesforce.  
  Mentioned as "Introducing Builder Central"  
  https://www.salesforce.com/blog/builder-central-ai-development/
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Recreate a past app or business scenario in Builder Central in a sandbox, then review the project plan and generated components (M)
- [ ] Complete the Trailhead module 'Get to Know Builder Central' and note the beta limitations (S)

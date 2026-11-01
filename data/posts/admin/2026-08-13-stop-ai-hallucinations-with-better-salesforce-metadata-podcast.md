---
title: "Stop AI Hallucinations with Better Salesforce Metadata"
url: https://admin.salesforce.com/blog/2026/stop-ai-hallucinations-with-better-salesforce-metadata-podcast
source: admin
date: 2026-08-13
authors: []
topics: ["Agentforce & AI", "Security & Admin", "Community & Events"]
---

- Skye Tyler (Principal Solution Consultant, Beyond the Horizon Technology) argues that clean metadata is essential for reliable AI agents, comparing agents to an enthusiastic intern with short-term memory problems.
- Agents look at metadata (field labels, descriptions, help text) before reading field values, so ambiguous fields such as four similarly named date fields lead the agent to guess.
- Because LLMs are non-deterministic, a guess may be right many times and then wrong on a later run, and the wrong answer still sounds fluent and confident.
- Recommended approach is 'clean-as-you-go': whenever you update an object or build a new AI-enabled business process, review and update descriptions and help text for the related fields the agent can touch.
- The episode also covers Skye's career path from nonprofit arts, advice to share what you know in the Salesforce community, and a preview of a Dreamforce session on the topic.

## Links
- **Salesforce Admins Podcast - Podcast - Apple Podcasts** [other]: Listen to Mike Gerholdt's Salesforce Admins Podcast podcast on Apple Podcasts.  
  Mentioned as "subscribe"  
  https://itunes.apple.com/us/podcast/buttonclick-admin-podcast/id914088438?mt=2&ign-mpt=uo%3D4
- **Admins** [other]: Admins  
  Mentioned as "Salesforce Admins on the Trailhead Store"  
  https://trailheadstoreamer.com/category/salesforce-admins
- **How Should I Clean Metadata for Salesforce AI Agents? - Salesforce Admins** [other]: Learn why clean, consistent metadata is critical for Agentforce success—and how Admins can start small to make a big impact.  
  Mentioned as "How Should I Clean Metadata for Salesforce AI Agents?"  
  https://admin.salesforce.com/blog/2025/how-should-i-clean-metadata-for-salesforce-ai-agents-podcast
- **Use Metadata To Empower Salesforce Agents - Salesforce Admins** [other]: Agentforce relies on clean metadata. Learn why organizing your org is key to building helpful AI agents on the Salesforce platform.  
  Mentioned as "Use Metadata To Empower Salesforce Agents"  
  https://admin.salesforce.com/blog/2025/use-metadata-to-empower-salesforce-agents-podcast
- **Metadata Is Your Admin Blueprint for Building Better Agents - Salesforce Admins** [other]: Salesforce metadata is your admin secret weapon to supercharge Agentforce! Learn how descriptions & topics help AI understand your customizations. Read now!  
  Mentioned as "Metadata Is Your Admin Blueprint for Building Better Agents"  
  https://admin.salesforce.com/blog/2025/metadata-your-admin-blueprint-for-building-better-agents
- **Group Detail** [other]: no description available  
  Mentioned as "Admin Trailblazers Community Group"  
  https://sforce.co/4977GHH
- **Mike Gerholdt (@mikegerholdt) • Threads, Say more** [other]: 238 Followers • 280 Threads • Salesforce Admin Evangelist I live with @Gunnarthebasenji 🐶 These inspiring words are my own. See the latest conversations with @mikegerholdt.  
  Mentioned as "Mike on Threads"  
  https://www.threads.net/@mikegerholdt/
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Audit one Agentforce-relevant object in a sandbox for fields with empty descriptions/help text or confusingly similar labels, and fill them in (M)
- [ ] Test an agent prompt against an object with ambiguous date fields before and after adding field descriptions, and compare answer consistency over repeated runs (S)

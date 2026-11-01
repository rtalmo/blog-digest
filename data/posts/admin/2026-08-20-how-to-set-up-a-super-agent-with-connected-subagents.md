---
title: "How to Set Up a Super Agent with Connected Subagents"
url: https://admin.salesforce.com/blog/2026/how-to-set-up-a-super-agent-with-connected-subagents
source: admin
date: 2026-08-20
authors: []
topics: ["Agentforce & AI", "Flow & Automation", "Security & Admin"]
---

- A single do-everything agent gets hard to maintain because subagents (formerly topics) compete for the same requests and the reasoning engine makes surprising choices.
- The recommended pattern is a Super Agent that owns the user conversation and delegates to Connected Subagents, with each one decomposed by functional domain, workflow stage, or capability.
- Use a Connected Subagent where work hands off to a different team or system and the task has its own input and output plus enough reasoning and data access. If it's a single step with no real reasoning, make it an action instead.
- Keep the Super Agent's instructions focused on routing, and put cross-cutting concerns there: guardrails and compliance (e.g. GDPR opt-out), one-time user verification and context priming, disambiguation, and human handoff.
- In the author's Pronto Delivery Concierge build, description-based routing was right only about 80% of the time, so they added a deterministic Agent Script conditional (if @variables.order_status == "In Progress": invoke @actions.go_to_Logistics_Dispatch) after a Get Order Details flow action.

## Links
- **What Is Multi-Agent Orchestration, and When To Build a Super Agent or a Single Agent - Salesforce Admins** [other]: Learn when to use a single Salesforce agent vs. multi-agent orchestration and design scalable Agentforce architectures.  
  Mentioned as "Super Agent"  
  https://admin.salesforce.com/blog/2026/what-is-soma-and-when-to-build-a-super-agent-or-a-single-agent
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260819094439/Super-Agent-1.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260819094439/Super-Agent-1.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260819094656/Agent-Router.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260819094656/Agent-Router.png
- **Multi-Agent Orchestration (Beta)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.agent_multi_orch.htm&type=5
- **Salesforce+ A Blueprint for Single-Org, Multi-Agent Orchestration** [other]: Learn how to architect single-org, multi-agent (SOMA) solutions by designing agent hand-offs, sharing context, and applying Well-Architected patterns for scalable Agentforce orchestration.  
  Mentioned as "A Blueprint for Single-Org, Multi-Agent Orchestration"  
  https://www.salesforce.com/plus/experience/tdx_2026/series/architects_at_tdx_2026/episode/episode-s1e13
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Build a Super Agent in a sandbox with two Connected Subagents and add an order_status conditional that overrides description-based routing (L)
- [ ] Audit existing Agentforce subagent descriptions for vague or overlapping wording and apply the one-sentence 'no and' test (S)

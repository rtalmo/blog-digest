---
title: "100 Ready-to-Use AI Prompts for Salesforce Admins"
url: https://admin.salesforce.com/blog/2026/100-ready-to-use-ai-prompts-for-salesforce-admins
source: admin
date: 2026-11-19
authors: ["Joshua Birk"]
topics: ["Agentforce & AI", "Flow & Automation", "Security & Admin"]
---

- Salesforce Admins and Lay Durafe released the Agentforce Vibes Admin Accelerator Kit, a markdown file on GitHub with 100 ready-made prompts that you can read and copy in a browser without cloning anything.
- The prompts fall into four buckets (Understanding, Configuring, Troubleshooting, Documenting), each with five categories of five prompts, and angle-bracket placeholders like <Object> or <Flow_Name> are replaced with your org's API names.
- The prompts work with Agentforce Vibes and with other agents connected to a Salesforce org through MCP, and the post advises starting in a sandbox or Developer Edition org because Configuring prompts change metadata while Understanding and Documenting prompts mostly read it.
- Impact-analysis prompts such as 'If I change <Field_Name> from text to picklist, what is impacted?' help you check Apex, Flows, reports, layouts and permission sets before a change, and the agent generates Flow metadata that waits for your review, with deployment as a separate prompt.
- Troubleshooting prompts cover Flow faults, 'Insufficient Privileges' errors and conflicting automations that revert field values, and they work best when you paste the full fault email, record ID and user.

## Links
- **this blog post** [other]: no description available  
  https://admin.salesforce.com/blog/2026/8-lessons-for-writing-ai-prompts-as-a-salesforce-admin
- **Agentforce Vibes Admin Accelerator Kit** [repo]: no description available  
  https://github.com/L-AY/admin-afvibes-df26-promptpack
- **Get to Know Agentforce Vibes** [trailhead]: no description available  
  https://trailhead.salesforce.com/content/learn/modules/einstein-for-developers/get-to-know-einstein-for-developers
- **Prompt Fundamentals: Write Effective Prompts for AI** [trailhead]: Prompt Fundamentals teaches how to write effective prompts for generative AI, starting with the six components that make prompts clear and actionable  
  Mentioned as "Prompt Fundamentals"  
  https://trailhead.salesforce.com/content/learn/modules/prompt-fundamentals
- **Prompt Like a Pro: AI Prompt Writing for Salesforce Admins** [other]: no description available  
  https://admin.salesforce.com/blog/2025/prompt-like-a-pro-ai-prompt-writing-for-salesforce-admins
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Run three Understanding prompts from the Admin Accelerator Kit against a sandbox (e.g., list active Flows on Account and map a record lifecycle) (S)
- [ ] Connect an agent to a sandbox via MCP and try the field type-change impact analysis plus the 'Document why' prompt on an existing validation rule or Flow (M)

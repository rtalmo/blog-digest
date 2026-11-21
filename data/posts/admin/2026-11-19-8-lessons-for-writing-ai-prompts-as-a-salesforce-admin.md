---
title: "8 Lessons for Writing AI Prompts as a Salesforce Admin"
url: https://admin.salesforce.com/blog/2026/8-lessons-for-writing-ai-prompts-as-a-salesforce-admin
source: admin
date: 2026-11-19
authors: ["Joshua Birk"]
topics: ["Agentforce & AI", "Security & Admin", "Flow & Automation"]
---

- The post argues prompt writing is ordinary professional writing, not engineering, and that most admin requests need only three to six plain-language sentences.
- It gives eight lessons: know your audience, lead with the goal, be specific, give context and the reason, define the output format, show examples, use plain language, and set constraints.
- Being specific for admin work means naming exact API names, such as the Require_Close_Reason validation rule on Opportunity rather than 'the opportunity rule'.
- Guardrails belong in the prompt from the start, for example working in a sandbox only, not touching active Flows, not changing profiles, and not deploying yet.
- The worked example turns 'Make a validation rule for close reason' into a full prompt for Closed Lost opportunities with a blank Close_Reason__c. It specifies the naming pattern, an error message under 100 characters and output limited to the formula and message.

## Links
- **100 Ready-to-Use AI Prompts for Salesforce Admins - Salesforce Admins** [other]: Put 100 ready-made prompts to work in your Salesforce org. A walkthrough of the Agentforce Vibes Admin Accelerator Kit, from understanding your org to documenting changes.  
  Mentioned as "this post"  
  https://admin.salesforce.com/blog/2026/100-ready-to-use-ai-prompts-for-salesforce-admins
- **Prompt Fundamentals: Write Effective Prompts for AI** [trailhead]: Prompt Fundamentals teaches how to write effective prompts for generative AI, starting with the six components that make prompts clear and actionable  
  Mentioned as "Prompt Fundamentals"  
  https://trailhead.salesforce.com/content/learn/modules/prompt-fundamentals
- **Explore Agentforce Vibes: Enhancing Developer Productivity** [trailhead]: Discover the capabilities of Agentforce Vibes, designed to boost developer productivity through innovative AI tools. Learn how Salesforce protects customer data while  
  Mentioned as "Get to Know Agentforce Vibes"  
  https://trailhead.salesforce.com/content/learn/modules/einstein-for-developers/get-to-know-einstein-for-developers
- **Prompt Like a Pro: AI Prompt Writing for Salesforce Admins - Salesforce Admins** [other]: Learn Salesforce Prompt Builder best practices for admins, including effective AI prompts, security, and scaling. Feel empowered by no-code generative AI.  
  Mentioned as "Prompt Like a Pro: AI Prompt Writing for Salesforce Admins"  
  https://admin.salesforce.com/blog/2025/prompt-like-a-pro-ai-prompt-writing-for-salesforce-admins
- **GitHub - L-AY/admin-afvibes-df26-promptpack: Agentforce Vibes for Salesforce Admins — Reusable Prompt Library · GitHub** [repo]: Agentforce Vibes for Salesforce Admins — Reusable Prompt Library - L-AY/admin-afvibes-df26-promptpack  
  Mentioned as "Agentforce Vibes Admin Accelerator Kit"  
  https://github.com/L-AY/admin-afvibes-df26-promptpack
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Rewrite one of your usual one-line admin requests using the eight lessons and compare the agent's output before and after in a sandbox (S)
- [ ] Browse the Agentforce Vibes Admin Accelerator Kit on GitHub and try 2-3 of its prompts against a scratch org or sandbox (M)

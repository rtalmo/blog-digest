---
title: "How to Find Your First Agentforce Use Case"
url: https://admin.salesforce.com/blog/2026/how-to-find-your-first-agentforce-use-case
source: admin
date: 2026-09-01
authors: []
topics: ["Agentforce & AI", "Flow & Automation", "Security & Admin"]
---

- The post advises admins to pick a small first Agentforce use case: one recurring problem for one user group, with one clear job and a measurable outcome.
- Listen for friction signals such as "I can never find…" or "Can you summarize this for me?". Users who export Salesforce data into unapproved consumer AI tools are a strong sign of unmet need and a data-handling risk that a governed Agentforce experience could replace.
- Keep a friction log for at least a week, recording the goal, what slowed users down, the workaround, how often it happens, and what a better outcome looks like.
- First check whether Agentforce is the right tool, meaning the job needs natural-language interpretation, summarization, context, or next-step decisions. Otherwise use something like Flow. Then score the remaining criteria from 1 to 5: data readiness (weighted most heavily), business value, frequency, manageable risk, and measurable outcome.
- For implementation, use a standard action where one exists (for example Summarize Record, which uses a Record Summary prompt template). Otherwise build a custom action powered by a prompt template (tailored generative output) or by Flow (deterministic processes). Combining Agentforce for interpretation with Flow for approved steps often works best.

## Links
- **How Can Salesforce Admins Find Simple Agentforce Use Cases? - Salesforce Admins** [other]: Learn how Salesforce Admins can start small with Agentforce to solve user pain points and build secure AI wins that earn buy-in.  
  Mentioned as "conversation with Kacie Molina"  
  https://admin.salesforce.com/blog/2026/how-can-salesforce-admins-find-simple-agentforce-use-cases-podcast
- **4 Inspiring Agentforce Use Cases for Salesforce Admins - Salesforce Admins** [other]: Discover 4 inspiring Agentforce use cases from the Salesforce Hackathon. See how Salesforce Admins are leveraging AI to solve real-world challenges.  
  Mentioned as "4 Inspiring Agentforce Use Cases for Salesforce Admins"  
  https://admin.salesforce.com/blog/2025/inspiring-agentforce-use-cases-for-salesforce-admins
- **Community-Crafted Agentforce Use Cases To Customize for Your Org - Salesforce Admins** [other]: Discover innovative Agentforce solutions from TDX. Learn how Agentblazers automate processes, streamline operations & enhance CRM with real-time insights.  
  Mentioned as "Community-Crafted Agentforce Use Cases To Customize for Your Org"  
  https://admin.salesforce.com/blog/2025/community-crafted-agentforce-use-cases-to-customize-for-your-org
- **Finding Your First Agentforce Win as a Salesforce Admin - Salesforce Admins** [other]: As a Salesforce Admin, the potential of AI is huge, and Agentforce puts that power directly in your hands. But with so many possibilities, the biggest question is often the simplest: Where do I begin? If you’re exploring how Agentforce fits into your org, or even a specific project, you might find yourself wondering how […]  
  Mentioned as "Finding Your First Agentforce Win as a Salesforce Admin"  
  https://admin.salesforce.com/blog/2025/finding-your-first-agentforce-win-as-a-salesforce-admin
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Start a one-week friction log of user struggles in your org and score the top candidates with the data-readiness-first scorecard (M)
- [ ] Try the Summarize Record standard action with a Record Summary prompt template on related records in a scratch org or sandbox (M)

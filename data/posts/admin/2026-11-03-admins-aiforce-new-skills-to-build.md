---
title: "Admins & AIforce: New Skills to Build"
url: https://admin.salesforce.com/blog/2026/admins-aiforce-new-skills-to-build
source: admin
date: 2026-11-03
authors: ["Kate Lessard"]
topics: ["Agentforce & AI", "Security & Admin", "DevOps & Tooling"]
---

- The post introduces a new AI extensibility stack for admins under AIforce: MCPs (Model Context Protocol), Skills, and Plugins.
- MCP is a standardized layer over APIs that lets AI securely fetch live context or take action, such as querying CRM records, searching records, or triggering auto-launched flows. Skills define repeatable steps, rules, and formatting for a task. Plugins bundle MCP connectors, skills, and interfaces for one-click install.
- The post lists new admin skills: MCP management (including external client applications and Agentic Identity), agent skills and Super Agent orchestration with subagents, plugin lifecycle management mapped to user roles, Agentforce Coworker setup, and Agent Script.
- Agent Script uses hybrid reasoning to define guardrails, tone, required steps, and logic declaratively in Agentforce Studio. Builder Central and Agentforce Vibes provide AI-assisted building, but admins still need solid fundamentals like schema, layouts, and permissions.
- The suggested roadmap runs from the AI Trust, Security, and Governance trail (Agentblazer Champion), to Coworker and Studio (Innovator), to Builder Central, Vibes, and plugin packaging (Legend), then to change management.

## Links
- **package elements** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-unlocked-pkg-whats-a-package.html
- **Being able to create and orchestrate a Super Agent with connected Subagents** [other]: no description available  
  https://admin.salesforce.com/blog/2026/how-to-set-up-a-super-agent-with-connected-subagents
- **AI Trust, Security, and Governance for the Agentic Era** [trailhead]: no description available  
  https://trailhead.salesforce.com/content/learn/trails/ai-trust-security-governance
- **Agentblazer Champion** [trailhead]: no description available  
  https://trailhead.salesforce.com/content/learn/trails/become-an-agentblazer-champion-2026
- **Agentblazer Innovator** [trailhead]: no description available  
  https://trailhead.salesforce.com/content/learn/trails/become-an-agentblazer-innovator-2026
- **Update your Legacy Agents to Agentforce Studio** [other]: no description available  
  https://www.youtube.com/watch?v=e0w8TNA-hc0
- **Build a Super Agent Step-by-Step** [other]: no description available  
  https://www.youtube.com/watch?v=VWOdgy6oyls
- **Salesforce Dev, Architect & Admin Events** [other]: Join Salesforce experts for live AMAs, coding, and workshops. Register for technical sessions on Agentforce, Data 360, and the platform to build skills.  
  Mentioned as "AIforce Workshop"  
  https://developer.salesforce.com/events
- **Agentblazer Legend** [trailhead]: no description available  
  https://trailhead.salesforce.com/content/learn/trails/become-an-agentblazer-legend-2026
- **Human Skills and Change Management for the Agentic Era** [trailhead]: no description available  
  https://trailhead.salesforce.com/content/learn/trails/human-skills-and-change-management-for-the-agentic-era
- **Tour of the HXL Playground** [other]: no description available  
  https://www.youtube.com/watch?v=FxeiOs8YDSo
- **What Is MCP? A Simple Guide to Model Context Protocol for Salesforce Admins - Salesforce Admins** [other]: Model Context Protocol is a new standard that lets agents talk to each other. We break down what it is, how it works & what it means for Salesforce Admins.  
  Mentioned as "What is MCP? A Simple Guide to Model Context Protocol for Salesforce Admins"  
  https://admin.salesforce.com/blog/2025/what-is-mcp-a-simple-guide-to-model-context-protocol-for-salesforce-admins
- **Skills in Agentforce Vibes: A Guide for Admins** [other]: no description available  
  https://admin.salesforce.com/blog/2026/skills-in-agentforce-vibes-a-guide-for-admins
- **How AI Could Change the Way Admins Set Up Salesforce** [other]: no description available  
  https://admin.salesforce.com/blog/2026/how-ai-could-change-the-way-admins-set-up-salesforce-podcast
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Set up Agentforce Coworker in a sandbox and test which skills and MCPs surface in global search, Slack, and mobile (M)
- [ ] Document a central inventory of org-wide MCP connections and external client apps, with the permissions each one needs (S)

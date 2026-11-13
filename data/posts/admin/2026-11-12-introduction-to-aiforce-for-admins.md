---
title: "Introduction to AIforce for Admins"
url: https://admin.salesforce.com/blog/2026/introduction-to-aiforce-for-admins
source: admin
date: 2026-11-12
authors: ["Joshua Birk"]
topics: ["Agentforce & AI", "Security & Admin", "Integration & APIs"]
---

- Salesforce's AIforce strategy is a live interface layer on top of Data 360, Customer 360 and Agentforce. It lets Salesforce flows, data models and logic be used from any AI model, agent or interface, including Claude (Claudeforce), Slack (Slackforce) and Lightning (Agentforce Coworker).
- The Headless Toolkit (formerly Headless 360) bundles five tool types: MCP servers, APIs, Skills, Plugins and developer tools (Salesforce CLI, Agentforce Vibes, Agent Script). It is not a new product to buy, and it includes 60+ MCP tools, 4,000+ existing APIs and 220+ CLI commands.
- Once an agent is written in Agent Script, an admin can create a custom MCP server, add the agent to the Agentforce Asset Library and configure access. Salesforce in Claude ships 37 prebuilt sales skills across 8 categories.
- External developers can use the Headless Experience Layer (HXL) to render Salesforce workflows in Slack, WhatsApp, voice or mobile without custom rendering code. They can instead call APIs and MCP tools directly and build their own UI, which gives more control but is slower.
- Security (Salesforce Guardian) relies on the existing model: identity, sharing rules, field-level security, permission sets, validation rules, triggers and governor limits all apply to MCP and API calls, and Salesforce-hosted MCP traffic passes through the Trust Layer. Because an agent can do anything its user can, the post urges reviewing profiles and permission sets, and says Agentic Identity (separate agent credentials, individually revocable) is planned for the near future.

## Links
- **Salesforce Unveils the Future of Enterprise Software: AIforce - Salesforce** [other]: AIforce unlocks tremendous value by enabling agents anywhere to reason and take action across all the data, workflows, and logic inside Salesforce Instead  
  Mentioned as "announced"  
  https://www.salesforce.com/news/stories/aiforce-announcement/
- **Salesforce Expands Agentforce With New Agents - Salesforce** [other]: New job-ready agents help companies get to business outcomes faster across sales, service, commerce, and the workforce — driving revenue, reducing costs,  
  Mentioned as "check out our growing family of agents"  
  https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents/
- **Multi-Framework Support** [other]: Develop AI agents and applications natively on the Agentforce 360 Platform using industry-standard UI frameworks.  
  Mentioned as "Salesforce Multi-Framework"  
  https://www.salesforce.com/platform/multi-framework/
- **Unlock the Power of Headless 360 for Your Organization** [trailhead]: Explore how Headless 360 transforms organizational capabilities by making data accessible from any environment. Learn to leverage powerful AI tools and streamline  
  Mentioned as "Introduction to AIforce"  
  https://trailhead.salesforce.com/content/learn/modules/salesforce-headless-360-quick-look?trailmix_creator_id=teamtrailhead&trailmix_slug=get-started-with-aiforce-quest
- **Headless tools: MCP, APIs, CLIs, and agent skills** [trailhead]: Explore how MCP, APIs, CLIs, and agent skills enable a headless architecture for flexible, programmatic access to the platform. This page explains hosted MCP server  
  Mentioned as "Salesforce Headless Toolkit"  
  https://trailhead.salesforce.com/content/learn/modules/headless-tools-and-functionality?trailmix_creator_id=teamtrailhead&trailmix_slug=get-started-with-aiforce-quest
- **Unlock Headless Functionality for Enhanced Operations** [trailhead]: Explore how headless functionality transforms business operations across sectors. Learn to implement smart configurations without traditional setups  
  Mentioned as "Actionable Headless Use Cases"  
  https://trailhead.salesforce.com/content/learn/modules/headless-360-use-cases-in-action?trailmix_creator_id=teamtrailhead&trailmix_slug=get-started-with-aiforce-quest
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Audit profiles and permission sets for users likely to connect agents or MCP clients, and tighten overly broad access (M)
- [ ] Complete the Trailhead modules on AIforce and the Headless Toolkit, then try exposing an Agent Script agent through a custom MCP server in a sandbox or scratch org (M)

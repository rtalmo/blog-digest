---
title: "Metadata Grounding: Let Your Coding Agent Search Your Org by Intent"
url: https://developer.salesforce.com/blogs/2026/11/metadata-grounding-let-your-coding-agent-search-your-org-by-intent
source: dev
date: 2026-11-05
authors: ["Gonzalo Gambino"]
topics: ["Agentforce & AI", "DevOps & Tooling", "Integration & APIs"]
---

- The Metadata Grounding MCP Server (Beta) lets coding agents search a pre-indexed catalog of an org's metadata by natural-language intent, so they find existing components before building new ones.
- It exposes three read-only tools, describe_metadata, search_metadata and query_metadata, following a describe, search, then query pattern across 70+ metadata types such as objects, fields, LWCs, Apex classes, flows and permission sets.
- It is backed by Salesforce Catalog on Data 360, using a hybrid vector and keyword index. Incremental sync covers supported types, and a full refresh runs every 24 hours, so recent deployments can lag.
- Two Pronto examples show it in use: a vague menu-page bug led to MenuBrowserController and the c__menuBrowser LWC, and a review-summary request led to the existing AgentSummarizeReviewsActions class, which was extended instead of rebuilt.
- It returns metadata and properties, not source code, and it is not an exhaustive inventory. Agents must retrieve code via the CLI or Metadata API and should confirm a record with query_metadata before coding against it.

## Links
- **Metadata Grounding (Beta)** [docs]: Use the Metadata Grounding MCP Server to discover and reuse Salesforce metadata from a connected org such as standard and custom objects and fields, L  
  Mentioned as "Metadata Grounding MCP Server (Beta)"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/metadata-grounding.html
- **GitHub - trailheadapps/pronto: Pronto sample app that showcases the Headless Toolkit · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - trailheadapps/pronto  
  Mentioned as "Pronto"  
  https://github.com/trailheadapps/pronto
- **Welcome to Salesforce Headless Toolkit** [docs]: For years, using Salesforce meant opening a web browser and logging into the Lightning interface. The headless approach is a fundamental shift that de  
  Mentioned as "Headless Toolkit"  
  https://developer.salesforce.com/docs/platform/headless-get-started/guide/headless-get-started.html
- **Salesforce Catalog** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_salesforce_catalog.htm&type=5
- **sf-skills/skills/platform-metadata-grounding-get at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/skills/platform-metadata-grounding-get at main · forcedotcom/sf-skills  
  Mentioned as "platform-metadata-grounding-get"  
  https://github.com/forcedotcom/sf-skills/tree/main/skills/platform-metadata-grounding-get
- **sf-skills/skills/platform-metadata-discovery-get at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/skills/platform-metadata-discovery-get at main · forcedotcom/sf-skills  
  Mentioned as "platform-metadata-discovery-get"  
  https://github.com/forcedotcom/sf-skills/tree/main/skills/platform-metadata-discovery-get
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "public sf-skills repo"  
  https://github.com/forcedotcom/sf-skills
- **Salesforce Development Plugin** [docs]: Use Salesforce Development workflows, AI Skills, Salesforce CLI, and Model Context Protocol (MCP) tools to build, test, and deploy on the Salesforce P  
  Mentioned as "Salesforce Development Plugin for Claude Code"  
  https://developer.salesforce.com/docs/platform/salesforce-skills-plugins/overview
- **Metadata Grounding MCP Server** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_headless360_mcp_servers_metadata_grounding.htm&release=264&type=5
- **Set Up Your Org** [docs]: Before AI clients can connect to your Salesforce org through MCP, you need to configure authentication and access. This setup process is a one-time co  
  Mentioned as "Platform Hosted MCP Server setup guide"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/setup-overview.html
- **Billing Considerations for Salesforce Catalog** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_salesforce_catalog_billing_considerations.htm&type=5
- **[Early Access Interest] Metadata Grounding Capabilities** [other]: We're working on two additions to Metadata Grounding: AI-Generated Metadata Descriptions and the Metadata Graph. AI-Generated Descriptions are meant to make your org's metadata more meaningful to AI agents. The Metadata Graph is meant to let agents look up how your metadata connects, so you can see what uses a field or object and what could break before you change it. Both are still under development. Signing up does not guarantee a spot, and early-access features may require additional terms before you join. Early access would be in a Developer Edition or sandbox org, and we'll confirm the details when we reach out. If you're interested, tell us below and we'll be in touch when there's something to try.  
  Mentioned as "Sign up for early access."  
  https://docs.google.com/forms/d/e/1FAIpQLSc3X7ujzcjVViQQKAv7f5Bj19vz-cPfCqKvaMH80hB7bjkcEw/viewform
- **Metadata Grounding: Share Your Feedback** [other]: Your feedback helps shape Metadata Grounding. This takes about two minutes. Please don't include confidential or customer data in your answers. The Metadata Grounding product team will use your responses to improve the product.  
  Mentioned as "your feedback"  
  https://forms.gle/G3Xuto6tMAUfhA1K7
- **Developer Portal** [other]: Learn how to build mobile and enterprise applications and agents on Salesforce and deliver innovative experiences using the Agentforce 360 Platform.  
  Mentioned as "Salesforce Developers website"  
  https://developer.salesforce.com/
- **Ground Users and Agents in Your Metadata with Salesforce Catalog (Generally Available)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_cdp_2026_winter_salesforce_catalog_ga.htm&release=264&type=5
- **Announcing the Headless 360 MCP Server Beta** [other]: The Headless 360 MCP Server (Beta) is a new surface that empowers headless clients to quickly discover and execute complex Salesforce setup and integration operations.  
  https://developer.salesforce.com/blogs/2026/07/announcing-the-headless-360-mcp-server-beta

## Suggested tasks
- [ ] Enable Salesforce Catalog in a sandbox, activate the Metadata Grounding MCP Server, and connect it to your coding agent (e.g. Claude Code) (M)
- [ ] Add the 'check the org first' project rule, or install the platform-metadata-grounding-get skill from sf-skills, and test it with a ticket for a feature you suspect already exists (S)
- [ ] Audit descriptions on key Apex classes and LWCs in your org to improve search ranking (M)

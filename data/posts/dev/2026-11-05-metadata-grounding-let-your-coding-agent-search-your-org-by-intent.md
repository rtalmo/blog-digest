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
- **Metadata Grounding MCP Server (Beta)** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/metadata-grounding.html
- **GitHub - trailheadapps/pronto: Pronto sample app that showcases the Headless Toolkit · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - trailheadapps/pronto  
  Mentioned as "Pronto"  
  https://github.com/trailheadapps/pronto
- **Headless Toolkit** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/headless-get-started/guide/headless-get-started.html
- **Salesforce Catalog** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_salesforce_catalog.htm&type=5
- **platform-metadata-grounding-get** [repo]: no description available  
  https://github.com/forcedotcom/sf-skills/tree/main/skills/platform-metadata-grounding-get
- **platform-metadata-discovery-get** [repo]: no description available  
  https://github.com/forcedotcom/sf-skills/tree/main/skills/platform-metadata-discovery-get
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "public sf-skills repo"  
  https://github.com/forcedotcom/sf-skills
- **Salesforce Development Plugin for Claude Code** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/salesforce-skills-plugins/overview
- **Metadata Grounding MCP Server** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_headless360_mcp_servers_metadata_grounding.htm&release=264&type=5
- **Platform Hosted MCP Server setup guide** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/setup-overview.html
- **Billing Considerations for Salesforce Catalog** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_salesforce_catalog_billing_considerations.htm&type=5
- **Sign up for early access.** [other]: no description available  
  https://docs.google.com/forms/d/e/1FAIpQLSc3X7ujzcjVViQQKAv7f5Bj19vz-cPfCqKvaMH80hB7bjkcEw/viewform
- **your feedback** [other]: no description available  
  https://forms.gle/G3Xuto6tMAUfhA1K7
- **Developer Portal** [other]: Learn how to build mobile and enterprise applications and agents on Salesforce and deliver innovative experiences using the Agentforce 360 Platform.  
  Mentioned as "Salesforce Developers website"  
  https://developer.salesforce.com/
- **Ground Users and Agents in Your Metadata with Salesforce Catalog (Generally Available)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_cdp_2026_winter_salesforce_catalog_ga.htm&release=264&type=5
- **Announcing the Headless 360 MCP Server Beta** [other]: no description available  
  https://developer.salesforce.com/blogs/2026/07/announcing-the-headless-360-mcp-server-beta

## Suggested tasks
- [ ] Enable Salesforce Catalog in a sandbox, activate the Metadata Grounding MCP Server, and connect it to your coding agent (e.g. Claude Code) (M)
- [ ] Add the 'check the org first' project rule, or install the platform-metadata-grounding-get skill from sf-skills, and test it with a ticket for a feature you suspect already exists (S)
- [ ] Audit descriptions on key Apex classes and LWCs in your org to improve search ranking (M)

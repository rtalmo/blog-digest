---
title: "Explore the Headless Toolkit with the Pronto Sample App"
url: https://developer.salesforce.com/blogs/2026/10/explore-the-headless-toolkit-with-the-pronto-sample-app
source: dev
date: 2026-10-28
authors: ["Philippe Ozil"]
topics: ["Agentforce & AI", "Integration & APIs", "DevOps & Tooling"]
---

- Pronto is a new open-source sample app (fictional AI food-delivery platform) showing the Headless Toolkit: Salesforce in Claude, Slack, Agentforce Coworker and more.
- Ships two orchestrator agents and 16+ actions, with multi-agent orchestration: both reuse a connected 'storefront explorer' subagent without losing conversation context.
- Exposes business logic to external clients through Salesforce Hosted MCP Servers (invocable actions, REST resources, API catalog).
- Good source of reference patterns: agent files, MCP server definitions, action classes and an LWR site.

## Links
- **Salesforce Headless Toolkit** [other]: Salesforce Headless Toolkit  
  Mentioned as "Headless Toolkit"  
  https://developer.salesforce.com/developer-centers/headless
- **Agentforce Coworker** [docs]: Powered by Data 360, Agentforce Coworker is your AI-powered agent, connecting all your work tools into one conversational interface. Instead of juggli  
  https://developer.salesforce.com/docs/data/agentforce-coworker/guide/agentforce-coworker-a-home.html
- **GitHub - trailheadapps/pronto: Pronto sample app that showcases the Headless Toolkit · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - trailheadapps/pronto  
  Mentioned as "Pronto"  
  https://github.com/trailheadapps/pronto
- **GitHub - trailheadapps/agent-script-recipes: A collection of easy-to-digest Agent Script examples. · GitHub** [repo]: A collection of easy-to-digest Agent Script examples. - trailheadapps/agent-script-recipes  
  Mentioned as "Agentforce Recipes"  
  https://github.com/trailheadapps/agent-script-recipes
- **multi-agent orchestrations** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.agent_multi_orch.htm&type=5
- **pronto/src-base/main/default/aiAuthoringBundles/Storefront_Explorer_Assistant/Storefront_Explorer_Assistant.agent at main · trailheadapps/pronto · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - pronto/src-base/main/default/aiAuthoringBundles/Storefront_Explorer_Assistant/Storefront_Explorer_Assistant.agent at main · trailheadapps/pronto  
  Mentioned as "storefront explorer assistant"  
  https://github.com/trailheadapps/pronto/blob/main/src-base/main/default/aiAuthoringBundles/Storefront_Explorer_Assistant/Storefront_Explorer_Assistant.agent
- **pronto/src-base/main/default/aiAuthoringBundles/Employee_Assistant/Employee_Assistant.agent at main · trailheadapps/pronto · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - pronto/src-base/main/default/aiAuthoringBundles/Employee_Assistant/Employee_Assistant.agent at main · trailheadapps/pronto  
  Mentioned as "employee assistant"  
  https://github.com/trailheadapps/pronto/blob/main/src-base/main/default/aiAuthoringBundles/Employee_Assistant/Employee_Assistant.agent
- **pronto/src-base/main/default/aiAuthoringBundles/Customer_Service_Assistant/Customer_Service_Assistant.agent at main · trailheadapps/pronto · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - pronto/src-base/main/default/aiAuthoringBundles/Customer_Service_Assistant/Customer_Service_Assistant.agent at main · trailheadapps/pronto  
  Mentioned as "customer service assistant"  
  https://github.com/trailheadapps/pronto/blob/main/src-base/main/default/aiAuthoringBundles/Customer_Service_Assistant/Customer_Service_Assistant.agent
- **Salesforce Hosted MCP Servers** [docs]: Give AI agents a secure, governed way to interact with Salesforce data and automation using the Model Context Protocol (MCP). Any compatible AI client  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers
- **Pronto employee custom MCP server** [repo]: no description available  
  https://github.com/trailheadapps/pronto/blob/main/src-site/main/default/mcpServerDefinitions/ProntoEmployeeServer.mcpServerDefinition-meta.xml
- **Connect Claude with Salesforce Hosted MCP Servers** [other]: Stop logging into Lightning Experience for daily operations. Learn how to securely configure external tools like Claude Code to interact directly with the Salesforce Platform using standard and custom Hosted MCP Servers.  
  Mentioned as "such as Claude Code"  
  https://developer.salesforce.com/blogs/2026/05/connect-claude-with-salesforce-hosted-mcp-servers
- **Invocable Actions** [docs]: Apex Actions — also commonly known as Invocable Actions — can be exposed as custom MCP tools, giving agents access to business logic your team has alr  
  Mentioned as "Apex tools"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/invocable-actions.html
- **pronto/src-base/main/default/classes/actions/orders/CreateOrderAction.cls at main · trailheadapps/pronto · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - pronto/src-base/main/default/classes/actions/orders/CreateOrderAction.cls at main · trailheadapps/pronto  
  Mentioned as "create order"  
  https://github.com/trailheadapps/pronto/blob/main/src-base/main/default/classes/actions/orders/CreateOrderAction.cls
- **pronto/src-base/main/default/classes/actions/orders/GetOrderStatusAction.cls at main · trailheadapps/pronto · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - pronto/src-base/main/default/classes/actions/orders/GetOrderStatusAction.cls at main · trailheadapps/pronto  
  Mentioned as "get order status"  
  https://github.com/trailheadapps/pronto/blob/main/src-base/main/default/classes/actions/orders/GetOrderStatusAction.cls
- **API Catalog** [docs]: The Salesforce API Catalog is a curated registry of REST API endpoints that admins can map to custom MCP tools through the Setup UI. Rather than writi  
  Mentioned as "Apex REST tool"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/api-catalog.html
- **pronto/src-base/main/default/classes/rest/StorefrontRestResource.cls at main · trailheadapps/pronto · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - pronto/src-base/main/default/classes/rest/StorefrontRestResource.cls at main · trailheadapps/pronto  
  Mentioned as "searching storefronts"  
  https://github.com/trailheadapps/pronto/blob/main/src-base/main/default/classes/rest/StorefrontRestResource.cls
- **Agentforce** [docs]: Expose Agentforce agents and Prompt Builder templates as MCP tools to allow external AI assistants to invoke Salesforce's native AI capabilities as pa  
  Mentioned as "agent MCP tool"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/agentforce.html
- **LWR Sites for Experience Cloud** [docs]: Develop sites that load quickly and scale well using the  
  Mentioned as "LWR site built with Experience Cloud"  
  https://developer.salesforce.com/docs/atlas.en-us.exp_cloud_lwr.meta/exp_cloud_lwr/intro.htm
- **Get Started** [docs]: Headless Experience Layer (HXL) is a unified experience engine and platform designed to deliver consistent, portable, and rich user experiences across  
  Mentioned as "Headless Experience Layer"  
  https://developer.salesforce.com/docs/platform/hxl/guide
- **Connect MCP Clients** [docs]: Connecting a client to a Salesforce Hosted MCP Server is a process that involves both Salesforce Setup and your selected client application.  
  Mentioned as "documentation"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/client-connection-overview.html
- **Get Started** [docs]: Agentforce is the agent-driven layer of the Salesforce Platform, and it helps you deploy AI agents that work side-by-side with your employees to exten  
  Mentioned as "Agentforce Developer Guide"  
  https://developer.salesforce.com/docs/ai/agentforce/guide/get-started.html
- **HXL Playground** [other]: Explore the Headless Experience Layer — build surface-agnostic widgets with Mosaic, preview them across Agentforce, Slack, and ChatGPT.  
  https://www.headlessexperiencelayer.com/
- **pozil (Philippe Ozil) · GitHub** [repo]: Principal Developer Advocate at Salesforce. Full stack coder, DevOps expert, ex VR dev and robot master. - pozil  
  Mentioned as "GitHub projects"  
  https://github.com/pozil

## Suggested tasks
- [ ] Clone trailheadapps/pronto and deploy to a scratch org (M)
- [ ] Study the multi-agent orchestration .agent files and reuse the pattern (M)
- [ ] Expose one of my own Apex actions through a Hosted MCP Server (L)

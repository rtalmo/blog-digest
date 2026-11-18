---
title: "Expose HXL Widgets to Slackbot with a Custom MCP Server"
url: https://developer.salesforce.com/blogs/2026/11/expose-hxl-widgets-slackbot-custom-mcp-server
source: dev
date: 2026-11-17
authors: ["Akshata Sawant"]
topics: ["Agentforce & AI", "Integration & APIs", "Security & Admin"]
---

- Headless Experience Layer (HXL, beta) widgets that already render in Claude or ChatGPT render in Slackbot without changes to the widget, Apex action, or Custom Lightning Types; only Slack-side configuration is needed.
- Before connecting, verify the custom MCP server is Active, every <resources> entry has a <description>, each tool's <uiResource> matches a resourceName, read-only tools set readOnly=true and destructive=false, and descriptionOverride clearly states what the tool returns.
- Connecting requires mapping each Salesforce user's Federation ID to their Slack email, requesting the connection under Manage Salesforce Organizations, approving it in Setup > Manage Slack Connection (Salesforce Mapping Field = SAML Federation ID), then adding the server under Salesforce > MCP servers; a blank 'Date added' means setup is incomplete and the server must be removed and re-added.
- Slackbot allows up to five active MCP servers per user and enforces a 60-second tool timeout with stateless calls, so keep Apex actions light (avoid chained callouts and heavy aggregate SOQL) and return only the fields the widget needs.
- Slackbot may pick its own Salesforce search or an overlapping tool on another server and show a plain table instead of your card; fix by avoiding overlapping servers, writing specific tool descriptions, naming records in prompts, and starting a new DM, and use MCP Inspector or MCPJam to confirm whether the tool result includes a UI resource.

## Links
- **Headless Experience Layer** [other]: Headless Experience Layer (HXL) is Salesforce's agentic experience layer for securely deploying logic to any external app.  
  https://www.salesforce.com/headless/agentic-experience-layer/
- **Agentforce employee agents** [other]: no description available  
  https://www.salesforce.com/agentforce/agentforce-for-employees/employee-agents/
- **Building Interactive UI with Headless Experience Layer** [other]: Learn how the Headless Experience Layer (HXL) lets you build one interactive widget that renders in Agentforce and MCP clients like Claude and ChatGPT.  
  https://developer.salesforce.com/blogs/2026/10/building-interactive-ui-with-hxl
- **How HXL Widgets Render in Agentforce and MCP Clients** [other]: no description available  
  https://developer.salesforce.com/blogs/2026/11/how-hxl-widgets-render-in-agentforce-and-mcp-clients?utm_campaign=amer_sfld&utm_content=Salesforce+Developers__sprout-1794501428&utm_medium=organic_social&utm_source=linkedin
- **HXL Playground** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/hxl/guide/playground.html
- **GitHub - trailheadapps/pronto: Pronto sample app that showcases the Headless Toolkit · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - trailheadapps/pronto  
  Mentioned as "Pronto"  
  https://github.com/trailheadapps/pronto
- **Slackbot MCP client documentation** [other]: no description available  
  https://docs.slack.dev/ai/slackbot-mcp-client/
- **GitHub - modelcontextprotocol/inspector: Deterministic testing tools for MCP servers · GitHub** [repo]: Deterministic testing tools for MCP servers. Contribute to modelcontextprotocol/inspector development by creating an account on GitHub.  
  Mentioned as "MCP Inspector"  
  https://github.com/modelcontextprotocol/inspector
- **MCPJam** [repo]: no description available  
  https://github.com/MCPJam/inspector
- **Trailblazer Community** [other]: no description available  
  http://sforce.co/DevCommunity
- **Build a Rich UI for External Agents** [docs]: Some AI agents use MCP to interact with data in your org, such as Claude Desktop, Slackbot, and ChatGPT. HXL widgets are compatible with the  
  Mentioned as "Use HXL Widgets on MCP Channels"  
  https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-channels.html
- **Get Started** [docs]: Headless Experience Layer (HXL) is a unified experience engine and platform designed to deliver consistent, portable, and rich user experiences across  
  Mentioned as "Headless Experience Layer: Get Started"  
  https://developer.salesforce.com/docs/platform/hxl/guide/get-started.html
- **Blog: How HXL Widgets Render in Agentforce and MCP Clients** [other]: no description available  
  https://developer.salesforce.com/blogs/2026/11/how-hxl-widgets-render-in-agentforce-and-mcp-clients
- **AIforce Workshop: Give Agents UI with the Headless Experience Layer (HXL)** [other]: no description available  
  https://developer.salesforce.com/workshops/aiforce-workshop/give-agents-ui-with-the-headless-experience-layer-hxl/overview

## Suggested tasks
- [ ] Audit your custom MCP server definition for resource descriptions, uiResource/resourceName matches, and readOnly/destructive flags (S)
- [ ] Connect Slackbot to a sandbox org via the Salesforce org connection and test the Pronto Storefront Tools widget (M)
- [ ] Check your server's tool output with MCP Inspector or MCPJam and rewrite descriptionOverride text to avoid routing to overlapping tools (S)

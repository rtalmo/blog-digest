---
title: "Hosted MCP Server\u3092\u4f7f\u3063\u3066Salesforce\u306bSlack\u3092\u63a5\u7d9a\u3059\u308b"
url: https://developer.salesforce.com/blogs/2026/09/connect-slack-to-salesforce-with-hosted-mcp-servers-jp
source: dev
date: 2026-09-16
authors: ["Philippe Ozil"]
topics: ["Agentforce & AI", "Integration & APIs", "Security & Admin"]
---

- Slackbot, Slack's built-in AI teammate and MCP client, can connect to Salesforce Hosted MCP Servers (Headless 360) so users can query and act on Salesforce data from Slack conversations without opening Salesforce tabs.
- Salesforce ships standard Hosted MCP Servers for SObject All, Tableau and Data 360. You can also build custom MCP servers that expose Apex actions, Flows, Apex REST endpoints, API Catalog APIs, Prompt Builder templates and Agentforce agents without writing integration code.
- Setup is done in the Slack admin UI in three steps: open the MCP server settings (the path differs for Business+/Enterprise Select and Enterprise Grid/Enterprise+), add a Hosted MCP Server, then set access to everyone, specific groups or members, or no one yet.
- Prerequisites are a paid Slack plan (Business+, Enterprise Select, Enterprise Grid or Enterprise+), a Salesforce org already connected to Slack, Slack and Salesforce admin rights, and at least one active Hosted MCP Server. Users are authenticated through the existing Slack–Salesforce account mapping, so no separate login is needed.
- Every Slackbot MCP call follows the Salesforce security model (object permissions, field-level security, sharing rules) per user and per request, and Slack prompts the user to confirm before it runs a custom MCP tool.

## Links
- **How to work with Slackbot** [other]: Navigate your workday with help from Slackbot, your personal agent for work. Slackbot has the same context and access to information you do, so answers are always relevant and personalized. Start a...  
  Mentioned as "Slackbot"  
  https://slack.com/help/articles/202026038-How-to-use-Slackbot
- **Salesforce Hosted MCP Servers** [docs]: Give AI agents a secure, governed way to interact with Salesforce data and automation using the Model Context Protocol (MCP). Any compatible AI client  
  Mentioned as "Salesforce Hosted MCP Server"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/overview
- **Beyond the sandbox: connect Slackbot to your production data with MCP** [other]: Most teams don’t have a tooling problem. They have an access problem. You’ve likely already built internal APIs, dashboards, or scripts that solve real  
  Mentioned as "Slackbot MCPクライアント"  
  https://slack.dev/slackbot-mcp-client/
- **What is the Model Context Protocol (MCP)? - Model Context Protocol** [other]: no description available  
  Mentioned as "オープン標準"  
  https://modelcontextprotocol.io/
- **Reference** [docs]: Reference  
  Mentioned as "Salesforceオブジェクト"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/references/reference/servers-reference.html
- **Reference** [docs]: Reference  
  Mentioned as "Tableau"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/references/reference/tableau-next.html
- **Reference** [docs]: Reference  
  Mentioned as "Data 360"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/references/reference/data-cloud-sql.html
- **Build Custom MCP Servers** [docs]: Salesforce ships various standard MCP servers bundling out-of-box capabilities oriented around discrete product areas. To combine MCP tools from diffe  
  Mentioned as "カスタムMCPサーバー"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/custom-servers.html
- **Activate MCP Servers** [docs]: MCP servers are disabled in your org by default and must be enabled by an administrator before clients can connect. This is a security measure — capab  
  Mentioned as "有効なSalesforce Hosted MCP server"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/activate-mcp-servers.html
- **Connect Salesforce and Slack** [other]: To set up Slack features that integrate with Salesforce (like Slackbot, Salesforce channels, or Agentforce), configure a connection between Slack and Salesforce. When you connect Salesforce and Sla...  
  Mentioned as "SalesforceとSlackを連携させる"  
  https://slack.com/help/articles/30754346665747-Connect-Salesforce-and-Slack
- **こちらの手順** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=slack.slack_salesforce_setup.htm&type=5
- **Salesforce Data Security Model — Explained Visually** [other]: To provide a security model that satisfies numerous, unique real-world business cases, Salesforce provides a comprehensive and flexible data security model to secure data at different levels. Salesforce also provides sharing tools to open up and allow secure access to data based on business needs. In this post, I explain how security features work together by taking a real-world scenario and describing it using images and GIFs.  
  Mentioned as "Salesforceセキュリティモデル"  
  https://developer.salesforce.com/blogs/developer-relations/2017/04/salesforce-data-security-model-explained-visually
- **SObject All** [docs]: The  
  Mentioned as "SObject All MCP server"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/sobject-all.html
- **Hosted Tableau MCP** [other]: Tableau MCP is available as a managed service on every Tableau Cloud pod, accessible at a single URL//mcp.tableau.com. It is the fastest way to get an AI agent talking to your Tableau Cloud site — no servers to deploy, no credentials to manage, and no infrastructure to maintain.  
  Mentioned as "Tableau MCPサーバー"  
  https://tableau.github.io/tableau-mcp/docs/hosted-tableau-mcp
- **Connect Slackbot to Salesforce with MCP** [other]: Add and configure Salesforce Model Context Protocol (MCP) servers in Slack to connect Slackbot with Salesforce or Data 360. When you add an MCP server, members of your workspace or Enterprise organ...  
  Mentioned as "MCPサーバーでSlackbotをSalesforceに接続する"  
  https://slack.com/help/articles/52462858006675-Connect-Slackbot-to-Salesforce-with-MCP
- **pozil (Philippe Ozil) · GitHub** [repo]: Principal Developer Advocate at Salesforce. Full stack coder, DevOps expert, ex VR dev and robot master. - pozil  
  Mentioned as "GitHubのプロジェクト"  
  https://github.com/pozil

## Suggested tasks
- [ ] Enable a Hosted MCP Server (e.g. SObject All) in a sandbox org and connect it to Slackbot via the Slack admin MCP settings (M)
- [ ] Build a custom MCP server in a scratch or sandbox org that exposes a Flow, such as an account-health-score Flow, and test it from Slackbot (M)
- [ ] Review permission sets, field-level security and sharing rules for the users who would get Slackbot MCP access, and decide which groups to allow (S)

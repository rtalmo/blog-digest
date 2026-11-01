---
title: "Extending Agentforce with External MCP Tools via MuleSoft"
url: https://developer.salesforce.com/blogs/2026/08/extending-agentforce-with-external-mcp-tools-via-mulesoft
source: dev
date: 2026-08-11
authors: ["Alex Martinez"]
topics: ["Agentforce & AI", "Integration & APIs", "DevOps & Tooling"]
---

- The post shows how Agentforce agents can call external MCP (Model Context Protocol) tools over JSON-RPC via HTTP, with no custom Apex callouts or middleware.
- It deploys a stateless timezone MCP server on MuleSoft CloudHub (single JAR, 0.1 vCore Micro worker). The server uses DataWeave 2.0 and exposes four tools: get_current_time, convert_time, time_difference and list_timezones, covering 50+ cities mapped to IANA IDs.
- The server implements the MCP methods initialize, tools/list and tools/call. It validates a Bearer token (returning JSON-RPC error -32000 if the token is missing or invalid) and is secured with OAuth 2.0 client credentials through an Anypoint Connected App and an API Manager policy.
- To register it in Salesforce, go to Setup → API Catalog → MCP Server → Import External MCP Server and supply the /mcp URL and OAuth details. Salesforce then fetches a token, negotiates protocol version 2024-11-05, discovers tools via tools/list and creates GenAiFunction metadata. You must add the tools to the allowlist before using them.
- In Agent Studio you create an Agentforce Employee Agent with a subagent, add the MCP tools from the Asset Library, then commit and activate the version and test it in Preview (e.g. 'What is the current time in New Delhi?'). Salesforce handles token caching and refresh, retries and error handling.

## Links
- **GitHub - SalesforceLabs/mule-mcp-timezone · GitHub** [repo]: Contribute to SalesforceLabs/mule-mcp-timezone development by creating an account on GitHub.  
  Mentioned as "GitHub repo"  
  https://github.com/SalesforceLabs/mule-mcp-timezone
- **mule-mcp-timezone/README.md at main · SalesforceLabs/mule-mcp-timezone · GitHub** [repo]: Contribute to SalesforceLabs/mule-mcp-timezone development by creating an account on GitHub.  
  Mentioned as "README.md"  
  https://github.com/SalesforceLabs/mule-mcp-timezone/blob/main/README.md
- **What is the Model Context Protocol (MCP)? - Model Context Protocol** [other]: no description available  
  Mentioned as "Model Context Protocol (MCP)"  
  https://modelcontextprotocol.io/docs/getting-started/intro
- **MCP for Agentforce** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.agent_mcp.htm&type=5
- **Trailblazer** [other]: Trailblazer Profile  
  Mentioned as "Trailblazer Community"  
  https://www.salesforce.com/trailblazer/devalexmartinez

## Suggested tasks
- [ ] Clone the timezone MCP server repo, build it with ./build.sh and deploy it to CloudHub via Runtime Manager (M)
- [ ] In a scratch org or sandbox, register the MCP server under API Catalog, allowlist the tools and build a 'Time Zone Assistant' Agentforce Employee Agent to test it in Preview (M)
- [ ] Identify one existing Apex callout in your org that could be replaced by an MCP tool and sketch the server design (S)

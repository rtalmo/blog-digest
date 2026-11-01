---
title: "Build Custom Salesforce Connect Adapters Smarter with Salesforce Skills"
url: https://developer.salesforce.com/blogs/2026/09/build-custom-salesforce-connect-adapters-smarter-with-salesforce-skills
source: dev
date: 2026-09-14
authors: ["snakra"]
topics: ["Integration & APIs", "Agentforce & AI", "Apex & Code"]
---

- The new platform-salesforce-connect-adapter-generate skill (in the open-source sf-skills repo) gives coding agents the DataSource framework context needed to generate a custom Salesforce Connect Apex adapter from a plain-language API description.
- A custom adapter needs two Apex classes, DataSource.Provider (declares objects, query capabilities, and auth method) and DataSource.Connection (handles QueryContext, makes the callout, and returns a TableResult).
- The skill enforces required details that commonly break agent-written code: ExternalId and DisplayUrl columns on every table, a designated name column, correct DataSource.DataType mappings, and Named Credentials via the callout: prefix instead of hardcoded secrets.
- With the Salesforce Headless 360 MCP Server, the agent can register the external data source through the external-data-source-setup operation, leaving only the validate-and-sync step as one click in Setup.
- The demo uses the public iRail API (714 Belgian train stations), but the generated code is only a first pass: you must add error handling and a test class before deploying to production, and Winter '27 is planned to extend headless external data source lifecycle management (subject to change).

## Links
- **Salesforce Connect** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.platform_connect_about.htm&type=5
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "write the integration by hand"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_connector_start.htm
- **custom Salesforce Connect Apex adapter** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.apex_adapter_setup.htm&type=5
- **validate and sync** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.ext_data_sync_database.htm&type=5
- **Headless 360 (Beta)** [docs]: The  
  Mentioned as "Headless 360 MCP Server"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/headless-360-mcp.html
- **external data source** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_externaldatasource.htm
- **external object.** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_external_objects.htm
- **Apex Reference Guide** [docs]: Apex Reference Guide  
  Mentioned as "DataSource"  
  https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_namespace_DataSource.htm
- **Apex Reference Guide** [docs]: Apex Reference Guide  
  Mentioned as "DataSource.Provider"  
  https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_DataSource_Provider.htm
- **Apex Reference Guide** [docs]: Apex Reference Guide  
  Mentioned as "DataSource.Connection"  
  https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_DataSource_Connection.htm
- **Agent Skills & Plugins** [other]: Capture your expertise as reusable Agent Skills and Plugins that AI agents apply consistently – across Claude, Slack, Agentforce, and more.  
  Mentioned as "Salesforce skills"  
  https://www.salesforce.com/headless/agent-skills-plugins/
- **Named credential** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_about.htm&type=5
- **iRail API Docs** [other]: no description available  
  Mentioned as "iRail API"  
  https://docs.irail.be/
- **GitHub - shra1904/dreamforce-demo: Dreamforce 2026 — Build Custom Salesforce Connect Apex Adapter using Headless 360 MCP and a Coding Agent · GitHub** [repo]: Dreamforce 2026 — Build Custom Salesforce Connect Apex Adapter using Headless 360 MCP and a Coding Agent - shra1904/dreamforce-demo  
  Mentioned as "https://github.com/shra1904/dreamforce-demo"  
  http://github.com/shra1904/dreamforce-demo
- **GitHub - forcedotcom/mcp-hosted: Salesforce Hosted MCP Servers · GitHub** [repo]: Salesforce Hosted MCP Servers. Contribute to forcedotcom/mcp-hosted development by creating an account on GitHub.  
  Mentioned as "MCP tool:"  
  https://github.com/forcedotcom/mcp-hosted?tab=readme-ov-file
- **sf-skills/skills/platform-salesforce-connect-adapter-generate at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/skills/platform-salesforce-connect-adapter-generate at main · forcedotcom/sf-skills  
  Mentioned as "sf-skills"  
  https://github.com/forcedotcom/sf-skills/tree/main/skills/platform-salesforce-connect-adapter-generate
- **IdeaExchange** [other]: no description available  
  https://ideas.salesforce.com/s/search
- **Salesforce Connect Custom Apex Adapter documentation** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.salesforce_connect_apex.htm&type=5

## Suggested tasks
- [ ] Install the skill (npx skills add forcedotcom/sf-skills) and generate the iRail adapter in a scratch org with a Connect license (M)
- [ ] Connect the Headless 360 MCP Server to your coding agent and try registering an external data source via external-data-source-setup (M)
- [ ] Write a test class and error handling for a generated adapter, including a callout mock, to meet production deploy coverage (S)

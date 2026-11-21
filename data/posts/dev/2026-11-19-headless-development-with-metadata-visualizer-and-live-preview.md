---
title: "Headless Development with Metadata Visualizer and Live Preview"
url: https://developer.salesforce.com/blogs/2026/11/headless-development-with-metadata-visualizer-and-live-preview
source: dev
date: 2026-11-19
authors: ["Philippe Ozil"]
topics: ["DevOps & Tooling", "Agentforce & AI", "LWC / UI"]
---

- The Headless Toolkit combines agent skills, hosted MCP servers, and the Headless Experience Layer (HXL) so agents can work with Salesforce metadata and data without Setup menus.
- Agents can query and modify metadata such as permission sets locally from the terminal. This cuts out Setup clicks and the retrieve-after-change round trip, and operations can run in parallel.
- The Metadata Visualizer VS Code extension renders read-only views of Agents, Flows, Lightning pages (FlexiPage), Objects, and Permission sets. It ships in the Salesforce Extension Pack, and you open it with the Visualize button on a supported metadata file.
- With Agentforce Vibes, you can select elements in a visualizer to have the agent edit the metadata. Otherwise you apply changes by prompting an agent in VS Code.
- The Live Preview extension covers LWC and Multi-Framework UI bundles, which use live org data. It also covers HXL widgets, which use editable sample data on a Data tab, and you open them with 'SFDX: Open in Widget Preview'.

## Links
- **Metadata Visualizer - Visual Studio Marketplace** [other]: Extension for Visual Studio Code - VS Code Extension to visualize Salesforce metadata with interactive diagrams  
  Mentioned as "Metadata Visualizer"  
  https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-metadata-visualizer-vscode
- **Salesforce Live Preview - Visual Studio Marketplace** [other]: Extension for Visual Studio Code - Salesforce Live Preview for Lightning Web Components  
  Mentioned as "Live Preview"  
  https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-vscode-ui-preview
- **Welcome to Salesforce Headless Toolkit** [docs]: For years, using Salesforce meant opening a web browser and logging into the Lightning interface. The headless approach is a fundamental shift that de  
  Mentioned as "Headless Toolkit"  
  https://developer.salesforce.com/docs/platform/headless-get-started/guide/headless-get-started.html
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "agent skills"  
  https://github.com/forcedotcom/sf-skills
- **Reference** [docs]: Reference  
  Mentioned as "hosted Model Context Protocol (MCP) servers"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/references/reference/servers-reference.html
- **Get Started** [docs]: Headless Experience Layer (HXL) is a unified experience engine and platform designed to deliver consistent, portable, and rich user experiences across  
  Mentioned as "Headless Experience Layer"  
  https://developer.salesforce.com/docs/platform/hxl/guide
- **Salesforce CLI** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  https://developer.salesforce.com/tools/salesforcecli
- **Salesforce Extension Pack - Visual Studio Marketplace** [other]: Extension for Visual Studio Code - Extensions for developing on the Salesforce Platform  
  Mentioned as "Salesforce Extension Pack"  
  https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-vscode
- **Agentforce Vibes Overview** [docs]: Welcome to the next generation of AI-driven development! The all-new Agentforce Vibes is re-engineered from the ground up to bring you smarter, faster  
  Mentioned as "Agentforce Vibes"  
  https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-overview.html
- **Edit Metadata Through Visualizations** [docs]: When you visualize metadata such as a data model, an agent, a flow, or a permission set, you can select one or more elements on the canvas and use Age  
  Mentioned as "have the agent edit the metadata"  
  https://developer.salesforce.com/docs/platform/md-visualizer/guide/mdv-vibes-editing.html
- **Run a Live Component Preview** [docs]: :::note Live Preview VS Code Extension for React components is a pilot or beta service that is subject to the Beta Services Terms at  
  Mentioned as "Lightning web components"  
  https://developer.salesforce.com/docs/platform/lwc/guide/get-started-test-components.html
- **Preview and Run Your App Locally** [docs]: As you build a Multi-Framework app, you can run it locally and preview your changes without deploying to an org each time. You have two options: run t  
  Mentioned as "Multi-Framework UI bundles"  
  https://developer.salesforce.com/docs/platform/multiframework/guide/mfw-preview.html
- **MCP Apps - Model Context Protocol** [other]: Interactive UI applications that render inside MCP hosts like Claude Desktop  
  Mentioned as "MCP Apps"  
  https://modelcontextprotocol.io/extensions/apps/overview
- **Metadata Visualizer Extension** [docs]: The Metadata Visualizer VS Code extension streamlines the interpretation of complex metadata by converting raw files into clear, structured visual rep  
  Mentioned as "Metadata Visualizer extension docs"  
  https://developer.salesforce.com/docs/platform/md-visualizer/overview
- **pozil (Philippe Ozil) · GitHub** [repo]: Principal Developer Advocate at Salesforce. Full stack coder, DevOps expert, ex VR dev and robot master. - pozil  
  Mentioned as "GitHub projects"  
  https://github.com/pozil

## Suggested tasks
- [ ] Open a flow and a permission set in Metadata Visualizer in VS Code and try a prompt-driven edit with an agent (S)
- [ ] Preview an LWC with Live Preview against a scratch org and compare it to your current deploy-and-refresh loop (M)
- [ ] Build a small HXL widget, run SFDX: Open in Widget Preview, and generate realistic sample data from a real org record (M)

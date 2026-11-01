---
title: "Headless Development with Skills and a Claude Code Plugin"
url: https://developer.salesforce.com/blogs/2026/08/headless-development-with-skills-and-a-claude-code-plugin
source: dev
date: 2026-08-19
authors: ["Philippe Ozil"]
topics: ["DevOps & Tooling", "Agentforce & AI", "Apex & Code"]
---

- Headless development relies on three components: agent skills (SKILL.md folders loaded lazily by name and description), MCP servers (a standard way to connect agents to external systems), and agent plugins (installable bundles of skills, MCP servers and utilities).
- Plugins are currently AI-vendor-specific, unlike skills and MCP servers, which are standards.
- The open-source sf-skills library has over 100 Salesforce skills, installable in other agentic environments with `npx skills add forcedotcom/sf-skills`. It comes pre-installed in Agentforce Vibes.
- Skills were renamed under a defined taxonomy (e.g., DX > DevOps > Test > Failures Analyze) and now pass an automated gated verification pipeline. Each skill now has its own version and dependency metadata, including the minimum Salesforce API version.
- The first official plugin, `salesforce-development` for Claude Code, bundles about 40 core development skills. It also includes the salesforce-dev, architecture-review and ADLC agents, and three MCP servers (salesforce-api-context, salesforce-metadata-experts, salesforce-lsp with Apex/SOQL language servers). Hooks cover org detection, Agent Script validation and deployment validation, and commands include /setup, /discovery, /org, /login and /logout.

## Links
- **Agent Skills Overview - Agent Skills** [other]: A standardized way to give AI agents new capabilities and expertise.  
  Mentioned as "Agent skills"  
  https://agentskills.io/home
- **Specification - Agent Skills** [other]: The complete format specification for Agent Skills.  
  Mentioned as "specification"  
  https://agentskills.io/specification
- **What is the Model Context Protocol (MCP)? - Model Context Protocol** [other]: no description available  
  Mentioned as "Model Context Protocol"  
  https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "Salesforce skills library (sf-skills)"  
  https://github.com/forcedotcom/sf-skills
- **Agentforce Vibes Overview** [docs]: Welcome to the next generation of AI-driven development! The all-new Agentforce Vibes is re-engineered from the ground up to bring you smarter, faster  
  Mentioned as "Agentforce Vibes"  
  https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-overview.html
- **sf-skills/skills/dx-org-manage/SKILL.md at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/skills/dx-org-manage/SKILL.md at main · forcedotcom/sf-skills  
  Mentioned as "dx-org-manage skill"  
  https://github.com/forcedotcom/sf-skills/blob/main/skills/dx-org-manage/SKILL.md
- **Claude Code** [other]: A shared Claude Code session on claude.ai/code  
  https://claude.ai/code
- **How Salesforce Developer Experience (DX) Tooling Changes the Way You Work** [docs]: Salesforce DX tooling provides modern experience to manage and develop apps on the platform across their entire lifecycle. It brings together source-d  
  Mentioned as "Salesforce CLI"  
  https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_intro.htm
- **API Library** [docs]: Discover Salesforce APIs in the Salesforce Developers API Library to extend and integrate your applications.  
  Mentioned as "Salesforce APIs"  
  https://developer.salesforce.com/docs/apis
- **Homepage** [other]: Discover trusted architecture guidance from Salesforce. Explore the Well-Architected Framework, decision guides, and resources built for Salesforce architects.  
  Mentioned as "Well-Architected pillars"  
  https://architect.salesforce.com/docs/architect/well-architected/guide/overview.html
- **Salesforce Extensions for Visual Studio Code** [docs]: Salesforce Extensions for Visual Studio Code are a set of open-source extensions that come with rich tools for developing on the Salesforce platform.  
  Mentioned as "Salesforce Extensions for VS Code"  
  https://developer.salesforce.com/docs/platform/sfvscode-extensions/overview
- **Node.js — Run JavaScript Everywhere** [other]: Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.  
  Mentioned as "Node.js"  
  https://nodejs.org
- **Salesforce CLI** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  https://developer.salesforce.com/tools/salesforcecli
- **Download Python** [other]: The official home of the Python Programming Language  
  Mentioned as "Python 3.8 or above"  
  https://www.python.org/downloads/
- **sf-skills/plugins/builder/salesforce-development at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/plugins/builder/salesforce-development at main · forcedotcom/sf-skills  
  Mentioned as "official setup instructions"  
  https://github.com/forcedotcom/sf-skills/tree/main/plugins/builder/salesforce-development
- **Confirm Redirect** [other]: no description available  
  Mentioned as "Plugin homepage"  
  https://sfdc.co/sf-claude
- **Overview - Claude Code Docs** [other]: Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools. Available in your terminal, IDE, desktop app, and browser.  
  Mentioned as "Claude Code documentation"  
  https://code.claude.com/docs
- **Salesforce Hosted MCP Servers** [docs]: Give AI agents a secure, governed way to interact with Salesforce data and automation using the Model Context Protocol (MCP). Any compatible AI client  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers
- **Plugins overview - Claude Code Docs** [other]: Understand what a Claude Code plugin is, when you need one instead of a standalone skill or MCP server, and which page to read to install or create one.  
  Mentioned as "Plugin development guide"  
  https://code.claude.com/docs/en/plugins
- **pozil (Philippe Ozil) · GitHub** [repo]: Principal Developer Advocate at Salesforce. Full stack coder, DevOps expert, ex VR dev and robot master. - pozil  
  Mentioned as "GitHub projects"  
  https://github.com/pozil

## Suggested tasks
- [ ] Install the salesforce-development plugin in Claude Code against a scratch org and run /setup, then try prompts like creating an Apex service class and its test class (M)
- [ ] Run `npx skills add forcedotcom/sf-skills` in another agent (Cursor, Codex or OpenCode) and compare the results with the Claude plugin (S)
- [ ] Review the sf-skills repository's skill metadata (versions, dependencies) and the taxonomy naming, and note which skills would fit your team's workflows (S)

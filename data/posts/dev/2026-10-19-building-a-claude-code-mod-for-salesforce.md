---
title: "Building a Claude Code Mod for Salesforce"
url: https://developer.salesforce.com/blogs/2026/10/building-a-claude-code-mod-for-salesforce
source: dev
date: 2026-10-19
authors: ["Dave Norris"]
topics: ["DevOps & Tooling", "Agentforce & AI"]
---

- Walkthrough of building `sf-headless-band`, a Claude Code mod that shows your Salesforce default org above the prompt.
- Resolves the default org the way the CLI does (SF_TARGET_ORG, then project config, then global config) and shows alias, My Domain and org type; scratch orgs show days remaining, and production is red.
- Adds one line per Salesforce MCP server showing which org it reaches (DX MCP Server `--orgs` flag, or Hosted MCP Server).
- Explains what makes a mod different from settings hooks, skills and MCP servers: it runs inside Claude Code and can draw its own UI.

## Links
- **Mods overview - Claude Code Docs** [other]: Add panes, commands, and tool call rules to Claude Code with a mod. See what a mod can do, how to make or install one, and where mods run.  
  Mentioned as "mods"  
  https://code.claude.com/docs/en/plugins/mods/overview
- **GitHub - deejay-hub/sf-headless-band: A Claude Code mod for Salesforce showing which Orgs are connected · GitHub** [repo]: A Claude Code mod for Salesforce showing which Orgs are connected - deejay-hub/sf-headless-band  
  Mentioned as "GitHub"  
  https://github.com/deejay-hub/sf-headless-band
- **Create a mod - Claude Code Docs** [other]: Have Claude write a Claude Code mod from a description, or write one yourself that counts tool calls and adds a command. Learn the reload and validate loop.  
  Mentioned as "Create a Mod"  
  https://code.claude.com/docs/en/plugins/mods/create
- **Draw in the interface with a mod - Claude Code Docs** [other]: Draw panes, a band above the prompt, buttons, and text fields from a Claude Code mod, handle presses and input, and keep state between redraws and sessions.  
  Mentioned as "Draw in the Interface"  
  https://code.claude.com/docs/en/plugins/mods/interface
- **Salesforce DX MCP Server and Tools** [docs]: Use the Salesforce DX MCP Server and its tools to enter natural language prompts in your IDE to complete standard DX tasks like syncing metadata, runn  
  Mentioned as "Salesforce DX MCP Server"  
  https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-mcp.html
- **Get Started** [docs]: Salesforce Hosted MCP Servers give AI agents a secure, governed way to interact with Salesforce data and automation. Using the open  
  Mentioned as "Hosted MCP Server"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide
- **Advanced setup - Claude Code Docs** [other]: System requirements, platform-specific installation, version management, and uninstallation for Claude Code.  
  Mentioned as "Claude Code"  
  https://code.claude.com/docs/en/setup
- **Salesforce CLI** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  https://developer.salesforce.com/tools/salesforcecli
- **Test a mod - Claude Code Docs** [other]: Write automated tests for a Claude Code mod that fire events, stub Claude Code's answers, and press buttons, with no session, sign-in, or network.  
  Mentioned as "Test a Mod"  
  https://code.claude.com/docs/en/plugins/mods/test
- **Quick Start** [docs]: Salesforce CLI is a command-line interface that simplifies development and build automation when working with your Salesforce org. Use it to create an  
  Mentioned as "Salesforce CLI Setup Guide"  
  https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm
- **Scratch Orgs** [docs]: The scratch org is a source-driven and disposable deployment of Salesforce code and metadata. A scratch org is fully configurable, allowing developers  
  Mentioned as "Salesforce DX Developer Guide"  
  https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs.htm

## Suggested tasks
- [ ] Clone sf-headless-band and install it (S)
- [ ] Build my own Claude Code mod (e.g. a blog-digest status band) using the same pattern (M)

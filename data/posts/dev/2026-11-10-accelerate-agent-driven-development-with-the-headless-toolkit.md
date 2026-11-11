---
title: "Accelerate Agent-Driven Development with the Headless Toolkit"
url: https://developer.salesforce.com/blogs/2026/11/accelerate-agent-driven-development-with-the-headless-toolkit
source: dev
date: 2026-11-10
authors: ["Mohith Shrivastava"]
topics: ["Agentforce & AI", "DevOps & Tooling", "Apex & Code"]
---

- The Headless Toolkit combines the Salesforce Skills Library (sf-skills, 250+ skills following the open Agent Skills spec), Hosted MCP Servers, and the Salesforce CLI so coding agents like Claude Code, Codex, Cursor, and Agentforce Vibes can build, test, and deploy on Salesforce.
- It proposes a seven-stage agent-driven loop (ground, specify, build, verify, review, release, observe), where each stage leaves a repo artifact such as a feature map, ontology.yaml, living spec, or review report, and each agent mistake feeds back into a new test, rule, or spec.
- Grounding uses a feature map, a business-term ontology.yaml, and the read-only Metadata Grounding MCP Server (Beta), which needs Data 360, API access, and Salesforce Catalog, is unavailable in scratch orgs and namespaced Developer Edition orgs, and can lag on recent changes.
- Hosted MCP Servers are off by default and must be enabled in Setup under MCP Servers (API Catalog), with activation taking up to two minutes; the author recommends spec-anchored specs for non-trivial work but skipping them for small fixes.
- The author advises keeping context lean (deep work under roughly 300K tokens to avoid context rot) and using subagents, defined in .claude/agents/ with scoped skills and tools, only for substantial standalone work since each adds cost and latency.

## Links
- **Welcome to Salesforce Headless Toolkit** [docs]: For years, using Salesforce meant opening a web browser and logging into the Lightning interface. The headless approach is a fundamental shift that de  
  Mentioned as "Headless Toolkit"  
  https://developer.salesforce.com/docs/platform/headless-get-started/guide/headless-get-started.html
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "Salesforce Skills Library"  
  https://github.com/forcedotcom/sf-skills
- **Get Started** [docs]: Salesforce Hosted MCP Servers give AI agents a secure, governed way to interact with Salesforce data and automation. Using the open  
  Mentioned as "Hosted Model Context Protocol (MCP) Servers"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html
- **Salesforce CLI** [repo]: no description available  
  https://github.com/salesforcecli
- **Claude Code** [other]: no description available  
  https://code.claude.com/docs/en/how-claude-code-works
- **context rot** [other]: no description available  
  https://www.trychroma.com/research/context-rot
- **over 80% of the Claude Code system prompt** [other]: no description available  
  https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/
- **Agent Skills specification** [other]: no description available  
  https://agentskills.io/
- **Metadata Grounding MCP Server** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/references/reference/metadata-grounding.html
- **/grill-me** [repo]: no description available  
  https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md
- **spec-writing skill** [repo]: no description available  
  https://github.com/msrivastav13/salesforce-write-spec-skill
- **subagent** [other]: no description available  
  https://code.claude.com/docs/en/sub-agents
- **Salesforce UI Script Recorder** [other]: no description available  
  https://marketplace.visualstudio.com/items?itemName=salesforce.salesforce-ui-script-recorder
- **Salesforce Well-Architected** [other]: no description available  
  https://architect.salesforce.com/docs/architect/well-architected/guide/framework.html
- **building a large app with Codex** [other]: no description available  
  https://openai.com/index/harness-engineering/
- **Snyk found** [other]: no description available  
  https://labs.snyk.io/resources/copilot-amplifies-insecure-codebases-by-replicating-vulnerabilities/
- **ApexGuru** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.apexguru_workflow.htm&type=5
- **sf-skills/plugins/builder/salesforce-development at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/plugins/builder/salesforce-development at main · forcedotcom/sf-skills  
  Mentioned as "Salesforce Development plugin"  
  https://github.com/forcedotcom/sf-skills/tree/main/plugins/builder/salesforce-development
- **Salesforce Code Quality plugin** [repo]: no description available  
  https://github.com/forcedotcom/sf-skills/tree/main/plugins/builder/salesforce-code-quality
- **Activate MCP Servers** [docs]: MCP servers are disabled in your org by default and must be enabled by an administrator before clients can connect. This is a security measure — capab  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/activate-mcp-servers.html
- **GitHub** [repo]: no description available  
  https://github.com/msrivastav13

## Suggested tasks
- [ ] Enable the Hosted MCP Servers in a sandbox or dev org via Setup > MCP Servers and install the salesforce-development plugin for Claude Code (S)
- [ ] Draft an ontology.yaml and a feature map for one business capability in your repo and reference them from AGENTS.md (M)
- [ ] Try the full loop on one multi-metadata feature: write a spec, build with a scoped subagent, then run an adversarial review pass and record what the harness missed (L)

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
- **Salesforce CLI · GitHub** [repo]: The Salesforce CLI is a collection of command line interfaces and tools that simplify development and build automation when working with your Salesforce org - Salesforce CLI  
  Mentioned as "Salesforce CLI"  
  https://github.com/salesforcecli
- **How Claude Code works - Claude Code Docs** [other]: Understand the agentic loop, built-in tools, and how Claude Code interacts with your project.  
  Mentioned as "Claude Code"  
  https://code.claude.com/docs/en/how-claude-code-works
- **Context Rot: How Increasing Input Tokens Impacts LLM Performance** [other]: Large Language Models (LLMs) are typically presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assumption does not hold. We observe that model performance varies significantly as input length changes, even on simple tasks. In this report, we evaluate 18 LLMs, including the state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. Our results reveal that models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows.  
  Mentioned as "context rot"  
  https://www.trychroma.com/research/context-rot
- **The new rules of context engineering for Claude 5 generation models / claude.dev Blog** [other]: We removed over 80% of Claude Code's system prompt for more advanced models. How to apply the lessons we learned to your own context engineering in Claude Code and with your own agents.  
  Mentioned as "over 80% of the Claude Code system prompt"  
  https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/
- **Agent Skills Overview - Agent Skills** [other]: A standardized way to give AI agents new capabilities and expertise.  
  Mentioned as "Agent Skills specification"  
  https://agentskills.io/
- **Reference** [docs]: Reference  
  Mentioned as "Metadata Grounding MCP Server"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/references/reference/metadata-grounding.html
- **skills/skills/productivity/grill-me/SKILL.md at main · mattpocock/skills · GitHub** [repo]: Skills for Real Engineers. Straight from my .agents directory. - skills/skills/productivity/grill-me/SKILL.md at main · mattpocock/skills  
  Mentioned as "/grill-me"  
  https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md
- **GitHub - msrivastav13/salesforce-write-spec-skill · GitHub** [repo]: Contribute to msrivastav13/salesforce-write-spec-skill development by creating an account on GitHub.  
  Mentioned as "spec-writing skill"  
  https://github.com/msrivastav13/salesforce-write-spec-skill
- **Create custom subagents - Claude Code Docs** [other]: Create and use specialized AI subagents in Claude Code for task-specific workflows and improved context management.  
  Mentioned as "subagent"  
  https://code.claude.com/docs/en/sub-agents
- **Salesforce UI Script Recorder - Visual Studio Marketplace** [other]: Extension for Visual Studio Code - VS Code Extension wrapping a CLI tool for recording Salesforce UI browser interactions with an overlay interface  
  Mentioned as "Salesforce UI Script Recorder"  
  https://marketplace.visualstudio.com/items?itemName=salesforce.salesforce-ui-script-recorder
- **Well-Architected Framework** [other]: The Salesforce Well-Architected Framework gives architects a shared, principled foundation for making the decisions that help a solution succeed over  
  Mentioned as "Salesforce Well-Architected"  
  https://architect.salesforce.com/docs/architect/well-architected/guide/framework.html
- **Harness engineering: leveraging Codex in an agent-first world** [other]: By Ryan Lopopolo, Member of the Technical Staff  
  Mentioned as "building a large app with Codex"  
  https://openai.com/index/harness-engineering/
- **Copilot amplifies insecure codebases by replicating vulnerabilities in your projects** [other]: no description available  
  Mentioned as "Snyk found"  
  https://labs.snyk.io/resources/copilot-amplifies-insecure-codebases-by-replicating-vulnerabilities/
- **ApexGuru** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.apexguru_workflow.htm&type=5
- **sf-skills/plugins/builder/salesforce-development at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/plugins/builder/salesforce-development at main · forcedotcom/sf-skills  
  Mentioned as "Salesforce Development plugin"  
  https://github.com/forcedotcom/sf-skills/tree/main/plugins/builder/salesforce-development
- **sf-skills/plugins/builder/salesforce-code-quality at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/plugins/builder/salesforce-code-quality at main · forcedotcom/sf-skills  
  Mentioned as "Salesforce Code Quality plugin"  
  https://github.com/forcedotcom/sf-skills/tree/main/plugins/builder/salesforce-code-quality
- **Activate MCP Servers** [docs]: MCP servers are disabled in your org by default and must be enabled by an administrator before clients can connect. This is a security measure — capab  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/activate-mcp-servers.html
- **msrivastav13 (Mohith Shrivastava) · GitHub** [repo]: Principal Developer Advocate @salesforce. msrivastav13 has 99 repositories available. Follow their code on GitHub.  
  Mentioned as "GitHub"  
  https://github.com/msrivastav13

## Suggested tasks
- [ ] Enable the Hosted MCP Servers in a sandbox or dev org via Setup > MCP Servers and install the salesforce-development plugin for Claude Code (S)
- [ ] Draft an ontology.yaml and a feature map for one business capability in your repo and reference them from AGENTS.md (M)
- [ ] Try the full loop on one multi-metadata feature: write a spec, build with a scoped subagent, then run an adversarial review pass and record what the harness missed (L)

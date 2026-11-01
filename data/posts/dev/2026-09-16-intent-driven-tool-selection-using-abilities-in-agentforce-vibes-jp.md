---
title: "\u958b\u767a\u306e\u610f\u56f3\u306b\u5fdc\u3058\u3066\u30c4\u30fc\u30eb\u3092\u81ea\u52d5\u3067\u9078\u629e \u2013 Agentforce Vibes\u306e\u65b0\u6a5f\u80fd\u300c\u30a2\u30d3\u30ea\u30c6\u30a3\u300d"
url: https://developer.salesforce.com/blogs/2026/09/intent-driven-tool-selection-using-abilities-in-agentforce-vibes-jp
source: dev
date: 2026-09-16
authors: ["odasho"]
topics: ["Agentforce & AI", "DevOps & Tooling", "Apex & Code"]
---

- Agentforce Vibes has a new feature called Abilities, which automatically picks the Salesforce DX MCP Server tools that fit a developer's intent. Developers no longer need to hand-pick tools or switch modes.
- The problem it addresses: more than 80 DX MCP tools are available, but enabling all of them bloats prompts, hurts output quality and raises token cost. Only a default subset is on, and customizing it means hand-editing the local mcp_config.json with internal tool names.
- Abilities are domain-specific capability groups, such as Apex and LWC development, DevOps operations, mobile development and core platform management. An internal Ability Coordinator evaluates each prompt and prepares the toolset before the model is called. Abilities can combine within one request.
- Tool selection uses RAG-based semantic search in three phases. Tool definitions (name, description, parameters, usage context) are embedded and stored in a vector database. The prompt is embedded with the same model and matched by cosine similarity, typically returning about 10 tools. Those tools are then injected into the model's context as a temporary function catalog.
- Orchestrator tools often need helper tools that the search may not return, so Abilities add dependent tools after selection. Skills are separate: Abilities decide which tools are available, while Skills define reusable task workflows (e.g. refactoring triggers, generating tests, deploying).

## Links
- **Salesforce DX MCP Server and Tools** [docs]: Use the Salesforce DX MCP Server and its tools to enter natural language prompts in your IDE to complete standard DX tasks like syncing metadata, runn  
  Mentioned as "Salesforce DX MCP Server"  
  https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_mcp.htm
- **Agentforce Vibes Overview** [docs]: Welcome to the next generation of AI-driven development! The all-new Agentforce Vibes is re-engineered from the ground up to bring you smarter, faster  
  Mentioned as "Agentforce Vibes"  
  https://developer.salesforce.com/docs/platform/einstein-for-devs/overview
- **Agentforce Vibes Overview** [docs]: Welcome to the next generation of AI-driven development! The all-new Agentforce Vibes is re-engineered from the ground up to bring you smarter, faster  
  Mentioned as "アビリティ"  
  https://developer.salesforce.com/docs/platform/einstein-for-devs/guide/abilities.html
- **https://d259t2jj6zp7qm.cloudfront.net/images/20260507124128/abilities.mp4** [other]: no description available  
  https://d259t2jj6zp7qm.cloudfront.net/images/20260507124128/abilities.mp4
- **Retrieval-augmented generation - Wikipedia** [other]: no description available  
  Mentioned as "検索拡張生成"  
  https://en.wikipedia.org/wiki/Retrieval-augmented_generation
- **Quick Start: Troubleshoot Code with AI Tools** [trailhead]: Explore how to refine your Apex and Lightning Web Components using AI coding assistance. This project guides you through the setup of your development environment and  
  Mentioned as "クイックスタート：Agentforce Vibesを使用してコードをトラブルシューティングする"  
  https://trailhead.salesforce.com/content/learn/projects/quick-start-troubleshoot-code-with-dev-agent
- **Get Started with Agentforce Vibes Trailmix** [trailhead]: A collection of resources to get started with Agentforce Vibes  
  Mentioned as "Get Started with Agentforce Vibes（英語）"  
  https://trailhead.salesforce.com/users/pozil/trailmixes/agentforce-vibes
- **Agentforce Vibes Decoded（英語）** [other]: no description available  
  https://www.youtube.com/watch?v=HByDCHMFdsY&list=PLgIMQe2PKPSIPk_YOY4XZn72y0yl-Zqt4

## Suggested tasks
- [ ] Try Abilities in Agentforce Vibes with prompts spanning Apex, LWC and deploy tasks, and compare the tools it selects (S)
- [ ] Review your local mcp_config.json for manually enabled DX MCP tools and test whether Abilities make them unnecessary (S)
- [ ] Read the Agentforce Vibes developer guide on Abilities and Skills, then draft a reusable Skill (e.g. test generation) that pairs with Abilities (M)

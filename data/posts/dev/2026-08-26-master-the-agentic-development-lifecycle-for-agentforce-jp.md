---
title: "Agentforce\u306e\u30a8\u30fc\u30b8\u30a7\u30f3\u30c6\u30a3\u30c3\u30af\u958b\u767a\u30e9\u30a4\u30d5\u30b5\u30a4\u30af\u30eb\u3092\u30de\u30b9\u30bf\u30fc\u3059\u308b"
url: https://developer.salesforce.com/blogs/2026/08/master-the-agentic-development-lifecycle-for-agentforce-jp
source: dev
date: 2026-08-26
authors: ["Mohith Shrivastava"]
topics: ["Agentforce & AI", "DevOps & Tooling", "Apex & Code"]
---

- With Salesforce Headless 360, Agentforce configuration (data model, Flow/Apex actions, agent definitions, permissions) is exposed through APIs, MCP tools and CLI commands, so coding agents such as Claude Code, Codex and Agentforce Vibes can drive the whole development lifecycle from natural language.
- Installing the open-source skill library with `npx skills add forcedotcom/sf-skills` gives the assistant three core skills: developing-agentforce (design, build, deploy, debug), testing-agentforce (test specs and batch runs) and observing-agentforce (production traces in Data 360); Node.js and Salesforce CLI are prerequisites.
- The post's key habit is to design before building: use plan mode and a prompt that makes the assistant interview you one question at a time as a decision tree. Split subagents by domain rather than task difficulty (typically 1-5), using a hub-and-spoke layout when work spans several domains.
- The assistant generates an authoring bundle with Agent Script, validates it locally, deploys the underlying Flow/Apex and then the bundle (`sf agent generate/validate authoring-bundle`, `sf project deploy start --metadata ...`), and retries automatically on deploy errors. The post recommends scoping each deploy to specific metadata, working only in scratch orgs or sandboxes, and explicitly asking for permission sets (FLS/CRUD).
- Testing has two modes, quick `sf agent preview start/send/end` smoke tests and YAML test specs run with `sf agent test create/run` (assertions: expectedTopic, expectedActions, expectedOutcome, with the LLM-judged expectedOutcome the most reliable). Multi-turn and state-variable injection support is still being added.

## Links
- **Get Started** [docs]: Agentforce is the agent-driven layer of the Salesforce Platform, and it helps you deploy AI agents that work side-by-side with your employees to exten  
  Mentioned as "Agentforce"  
  https://developer.salesforce.com/docs/ai/agentforce/guide
- **What Salesforce Headless 360 Means For Developers** [other]: Headless 360 exposes every Salesforce capability as an API, MCP tool, or CLI command. Learn why your platform expertise matters more in an agentic world.  
  Mentioned as "Salesforce Headless 360"  
  https://developer.salesforce.com/blogs/2026/05/headless-360-what-it-means-for-developers
- **Agentforce Vibes Overview** [docs]: Welcome to the next generation of AI-driven development! The all-new Agentforce Vibes is re-engineered from the ground up to bring you smarter, faster  
  Mentioned as "Agentforce Vibes"  
  https://developer.salesforce.com/docs/platform/einstein-for-devs/guide/einstein-overview.html
- **Agent Skills Overview - Agent Skills** [other]: A standardized way to give AI agents new capabilities and expertise.  
  Mentioned as "エージェントスキル"  
  https://agentskills.io/home
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "Salesforceスキルライブラリ"  
  https://github.com/forcedotcom/sf-skills
- **Salesforce CLI** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  https://developer.salesforce.com/tools/salesforcecli
- **ドキュメント** [repo]: no description available  
  https://github.com/forcedotcom/sf-skills/tree/main/skills/developing-agentforce
- **ドキュメント** [repo]: no description available  
  https://github.com/forcedotcom/sf-skills/tree/main/skills/testing-agentforce
- **ドキュメント** [repo]: no description available  
  https://github.com/forcedotcom/sf-skills/tree/main/skills/observing-agentforce
- **Node.js — Run JavaScript Everywhere** [other]: Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.  
  Mentioned as "Node.js"  
  https://nodejs.org
- **Build a Salesforce Agent Skill with Claude Code** [other]: Learn how to build authoring skills for consistently producing high quality code across the Salesforce ecosystem using structured workflows, code templates, and automated validators.  
  Mentioned as "独自のエージェントスキルを作成"  
  https://developer.salesforce.com/blogs/2026/05/build-a-salesforce-agent-skill-with-claude-code
- **リリースノート** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein_platform.htm&release=262&type=5
- **Git** [other]: no description available  
  https://git-scm.com/
- **Session Trace Data Model（STDM）** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.generative_ai_session_trace_data_model.htm&type=5
- **AgentLens: Debug Agentforce with Interactive Visualizations** [other]: Debug subagent routing and orchestration in minutes using AgentLens, a free open source tool that visualizes Agentforce agent traces as interactive graphs, FSM diagrams, and step-by-step instructors.  
  Mentioned as "AgentLens"  
  https://developer.salesforce.com/blogs/2026/05/agentlens-debug-agentforce-with-interactive-visualizations
- **Agentforceオブザーバビリティ（英語）** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=005226932&type=1
- **Group Detail** [trailhead]: no description available  
  Mentioned as "Salesforce Developers Trailblazer Community"  
  https://trailhead.salesforce.com/trailblazer-community/groups/0F93A000000DJbJSAW?tab=discussion&sort=LAST_MODIFIED_DATE_DESC
- **Agentforce** [other]: Agentforce  
  Mentioned as "Agentforce Developer Center（英語）"  
  https://developer.salesforce.com/developer-centers/agentforce
- **Agentforce DX - Visual Studio Marketplace** [other]: Extension for Visual Studio Code - Provides a suite of tools to iteratively build, preview, and test agents right in your IDE.  
  Mentioned as "Agentforce DX Visual Studio Code拡張機能（英語）"  
  https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-vscode-agents

## Suggested tasks
- [ ] Install forcedotcom/sf-skills in a scratch-org project and have your coding agent scaffold a simple single-subagent Agentforce agent via plan-mode interview (M)
- [ ] Write a YAML test spec with expectedTopic, expectedActions and expectedOutcome, then run it with `sf agent test create` and `sf agent test run` (S)
- [ ] Preview an agent with `sf agent preview`, then feed a local trace JSON to your assistant to diagnose and fix a routing or action issue (S)

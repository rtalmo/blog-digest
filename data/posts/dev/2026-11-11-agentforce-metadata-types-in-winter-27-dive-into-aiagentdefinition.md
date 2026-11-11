---
title: "Agentforce Metadata Types in Winter \u201927: Dive into AiAgentDefinition"
url: https://developer.salesforce.com/blogs/2026/11/agentforce-metadata-types-in-winter-27-dive-into-aiagentdefinition
source: dev
date: 2026-11-11
authors: ["Sarah Welker"]
topics: ["DevOps & Tooling", "Agentforce & AI", "Releases"]
---

- Winter '27 (API version 68.0) adds two metadata types, AiAgentDefinition (agent-level settings) and AiAgentDefinitionVersion (one version, with an inline <planner> element holding subagents and actions), replacing the Bot, BotVersion and GenAiPlannerBundle split for Agentforce agents.
- In the sample TestAgent (1 version, 10 subagents, 26 actions), all 37 generated-suffix names like ServiceCustomerVerification_1796152b9540575 disappear, and localDeveloperName becomes the name used for subagent-to-action links, so diffs between versions get much smaller.
- Welcome, error and escalation dialogs collapse into three simple elements (welcomeMessage, errorMessage, escalationMessage), and Salesforce builds the dialogs on deploy.
- The # member syntax selects versions (TestAgent#1, TestAgent#* for all versions of an agent, * for all agents), shrinking a hand-written manifest from 7 types and 14 members to 2 types, and AiAuthoringBundle folders always carry a version suffix such as TestAgent_1.
- Caveats: at API 68.0, retrieving or deploying Agentforce agents as Bot or BotVersion errors out (Bot types are now for classic Einstein Bots, so stay on 67.0 to keep using them), and the # syntax plus --root-type-with-dependencies need Salesforce CLI 2.149.9 or later (run sf update).

## Links
- **Winter ’27 release** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_agentforce_metadata.htm&release=264&type=5
- **The New Agentforce Metadata and Development Lifecycle** [other]: Streamline your CI/CD pipelines by leveraging the new versioned metadata model and human-readable Agent Scripts. Learn how bundleized assets eliminate “global ripples” and simplify peer reviews for more reliable agent deployments.  
  https://developer.salesforce.com/blogs/2026/05/new-agentforce-metadata-and-development-lifecycle
- **string replacement** [docs]: no description available  
  https://developer.salesforce.com/docs/ai/agentforce/guide/string-replace-example.html
- **Use Metadata to Move an Agent to a New Org** [docs]: no description available  
  https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-deploy-metadata.html
- **Define Agent Metadata (v67 and Earlier)** [docs]: no description available  
  https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-api-v67-earlier.html
- **project retrieve start** [docs]: no description available  
  https://developer.salesforce.com/docs/atlas.en-us.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_project_commands_unified.htm
- **Metadata Coverage Report** [docs]: no description available  
  https://developer.salesforce.com/docs/metadata-coverage
- **Intro to Agent Script Language Fundamentals** [other]: Learn how to master Agent Script to build agents using hybrid reasoning: the perfect balance of deterministic logic and generative power.  
  https://developer.salesforce.com/blogs/2026/02/agent-script-decoded-intro-to-agent-script-language-fundamentals
- **Create and Activate Your Agent with Agent Script Techniques** [trailhead]: Learn how to author agents using Agent Script and publishing techniques. This unit covers the full lifecycle from development to activation  
  https://trailhead.salesforce.com/content/learn/projects/create-an-agent-using-pro-code-tools/create-an-agent-from-your-dx-project

## Suggested tasks
- [ ] Run sf update, then retrieve an existing agent at API 68.0 in a scratch org using TestAgent#* and compare the folder layout to the 67.0 retrieve (S)
- [ ] Rewrite my agent package.xml to the two-type AiAgentDefinition/AiAgentDefinitionVersion manifest and test sf project retrieve start with --root-type-with-dependencies AiAgentDefinitionVersion (M)
- [ ] Audit my CI/CD pipeline and scripts for hard-coded Bot, GenAiPlannerBundle or suffixed-name references that will break when moving to API 68.0 (M)

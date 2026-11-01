---
title: "Migrate Legacy Agents to the New Agentforce Builder"
url: https://developer.salesforce.com/blogs/2026/08/migrate-legacy-agents-to-the-new-agentforce-builder
source: dev
date: 2026-08-06
authors: ["Mohith Shrivastava"]
topics: ["Agentforce & AI", "DevOps & Tooling", "Releases"]
---

- Starting the week of July 13, 2026, new agents can only be created in the new Agentforce Builder; existing legacy agents keep working and stay editable, so migration is now the path forward.
- The legacy engine classifies a message into one subagent and then runs a ReAct loop. The new engine is graph-based, with subagents as nodes, transitions between them, and variables that carry state, and it is authored in Agent Script (hybrid natural-language and programmatic logic).
- In Setup, Agentforce Studio → Agentforce Agents → 'Upgrade to New Builder' creates a new version with all subagents, actions, system messages, settings and connections converted to Agent Script, and the original agent stays active and untouched.
- The recommended approach is to migrate as-is first, confirm the agent works with tests, and only then harden it with variables, conditionals, filters and transitions where decisions have business consequences, in small batches.
- Regression testing runs the same suite against v1 and v2 with the Salesforce CLI. Add `--test-runner agentforce-studio` to `sf agent test create` and `sf agent test run` to target the Beta AiTestingDefinition metadata (using `<scorer>` tags) instead of the legacy AiEvaluationDefinition.

## Links
- **Introduction to Agentforce Builder Features** [trailhead]: Discover Agentforce Builder's features for creating and customizing agents to optimize your business tasks. Start enhancing productivity today.  
  Mentioned as "Agentforce Builder"  
  https://trailhead.salesforce.com/content/learn/modules/introduction-to-agent-builder
- **agent creation moved exclusively to the new builder** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_agentforce_legacy_agent_creation.htm&release=262&type=5
- **What Are ReAct Agents?** [other]: Learn about the ReAct (Reason and Act) framework for building autonomous LLM agents. Discover the core thought-action loop and best practices. Start building today.  
  Mentioned as "ReAct pattern"  
  https://www.salesforce.com/agentforce/ai-agents/react-agents/
- **Agent Script** [docs]: Get to know the language for building agents in Agentforce Builder. Use Agent Script to build predictable, context-aware agent workflows that don't re  
  https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html
- **Agentforce DX** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx.html
- **Agentforce Voice** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=005226934&type=1
- **migration guidance** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.agent_migrate_parent.htm&type=5
- **coral-cloud/cc-employee-app/main/default at main · trailheadapps/coral-cloud · GitHub** [repo]: Sample application that showcases Data Cloud, Agents and Prompts. - coral-cloud/cc-employee-app/main/default at main · trailheadapps/coral-cloud  
  Mentioned as "Coral Cloud Employee Agent"  
  https://github.com/trailheadapps/coral-cloud/tree/main/cc-employee-app/main/default
- **AiEvaluationDefinition** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_aievaluationdefinition.htm
- **scorers** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.generative_ai_optimize_scorers.htm&type=5
- **Create Custom Scorers** [docs]: Custom scorers allow you to define evaluation logic for agent testing.  
  Mentioned as "custom scorers guide"  
  https://developer.salesforce.com/docs/ai/agentforce/guide/testing-api-custom-scorers.html
- **Set Up and Run Tests in Agentforce Studio (Beta)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.agent_studio_testing_center_setup_tests.htm&type=5
- **agent test create** [docs]: Create an agent test in your org using a local test spec YAML file.  
  Mentioned as "Agent test create CLI command"  
  https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_agent_test_create.html
- **agent test run** [docs]: Start an agent test in your org.  
  Mentioned as "Agent test run CLI command"  
  https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_agent_test_run.html

## Suggested tasks
- [ ] Run 'Upgrade to New Builder' on a non-production agent in a sandbox and review the generated Agent Script in Canvas view (M)
- [ ] Write a baseline YAML test spec with topic_sequence_match, action_sequence_match and bot_response_rating, then run it against both v1 (testing-center) and v2 (agentforce-studio) via sf agent test (M)
- [ ] Update the Salesforce CLI and agent plugin (sf update) and verify the --test-runner flag is recognized (S)

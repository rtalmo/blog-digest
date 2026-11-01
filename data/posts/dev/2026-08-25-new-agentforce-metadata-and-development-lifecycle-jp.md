---
title: "\u65b0\u3057\u3044Agentforce\u30e1\u30bf\u30c7\u30fc\u30bf\u3068\u958b\u767a\u30e9\u30a4\u30d5\u30b5\u30a4\u30af\u30eb"
url: https://developer.salesforce.com/blogs/2026/08/new-agentforce-metadata-and-development-lifecycle-jp
source: dev
date: 2026-08-25
authors: ["Alba Rivas"]
topics: ["Agentforce & AI", "DevOps & Tooling", "Apex & Code"]
---

- The new Agentforce Builder (GA in Spring '26) separates developer intent from runtime execution: authors write a human-readable Agent Script stored as a single .agent file in the new AiAuthoringBundle metadata type, and the draft stays editable until a version is committed.
- Committing a version makes the platform convert the .agent script into the runtime Bot and GenAiPlannerBundle metadata, and preview mode (including a simulation mode isolated from org data) lets you test drafts before that.
- GenAiPlannerBundle was restructured into a per-version bundle folder containing the .genAiPlannerBundle file, agentGraph JSON, an agentScript snapshot for sync detection, plannerActions, and localActions with input/output schema.json, so deployments carry all dependencies.
- Local assets (local subagents and actions) are clones of global assets tied to one agent version, so editing them no longer ripples to every agent that shares the global subagent; GenAiPlannerBundle version numbers follow commit order and may not match AiAuthoringBundle versions.
- The package.xml must include GenAiFunction, Bot, GenAiPlannerBundle, GenAiPlugin and AiAuthoringBundle at API version 66.0 or later.

## Links
- **The New Agentforce Metadata and Development Lifecycle** [other]: Streamline your CI/CD pipelines by leveraging the new versioned metadata model and human-readable Agent Scripts. Learn how bundleized assets eliminate “global ripples” and simplify peer reviews for more reliable agent deployments.  
  https://developer.salesforce.com/blogs/2026/05/new-agentforce-metadata-and-development-lifecycle
- **新しいAgentforce Builder** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.agent_builder_intro.htm&type=5
- **GenAiPlannerBundleメタデータ** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_genaiplannerbundle.htm
- **Create and Activate Your Agent with Agent Script Techniques** [trailhead]: Learn how to author agents using Agent Script and publishing techniques. This unit covers the full lifecycle from development to activation  
  Mentioned as "こちらのTrailheadモジュール"  
  https://trailhead.salesforce.com/content/learn/projects/create-an-agent-using-pro-code-tools/create-an-agent-from-your-dx-project
- **Intro to Agent Script Language Fundamentals** [other]: Learn how to master Agent Script to build agents using hybrid reasoning: the perfect balance of deterministic logic and generative power.  
  Mentioned as "ブログ"  
  https://developer.salesforce.com/blogs/2026/02/agent-script-decoded-intro-to-agent-script-language-fundamentals
- **YouTubeのAgent Script Decodedシリーズ** [other]: no description available  
  https://www.youtube.com/playlist?list=PLgIMQe2PKPSJNLEQTPkr06gKhjnHgI1Jb
- **Salesforce Dev, Architect & Admin Events** [other]: Join Salesforce experts for live AMAs, coding, and workshops. Register for technical sessions on Agentforce, Data 360, and the platform to build skills.  
  Mentioned as "Agentforce Builderのワークショップ"  
  https://developer.salesforce.com/events
- **エージェントのバージョン管理と編集** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.agent_versions_lifecycle.htm&type=5
- **改良されたエージェントバージョン機能を使用したエージェントのテストとカスタマイズ（英語）** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein_agentforce_versioning_improvements.htm&release=256&type=5
- **標準エージェントアクションの参照アクションの編集** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.copilot_actions_edit_reference.htm&type=5
- **Package Agentforce Metadata Components** [docs]: Bring the power of conversational AI to your apps with Agentforce.  
  Mentioned as "Agentforceメタデータコンポーネントのパッケージ化（英語）"  
  https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_packageable_agentforce_md.htm
- **Develop and Package Agent Templates Using Scratch Orgs** [docs]: At a high-level, agents are distributed by ISVs as agent templates. To package an agent template, you first create and test an agent in a namespaced s  
  Mentioned as "スクラッチ組織を使用したAIエージェントテンプレートの開発とパッケージ化（英語）"  
  https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_package_agent_templates.htm
- **GenAiFunction** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_genaifunction.htm
- **GenAiPlugin** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_genaiplugin.htm
- **GenAiPluginInstructionDef** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_genaiplugininstructiondef.htm

## Suggested tasks
- [ ] Retrieve an existing agent as AiAuthoringBundle plus GenAiPlannerBundle in a scratch org using a package.xml at API 66.0, and inspect the file layout (S)
- [ ] Prototype a CI pipeline that deploys AiAuthoringBundle, publishes it with sf agent publish authoring-bundle, then activates the chosen version (M)
- [ ] Compare the fully automated deploy (AiAuthoringBundle,GenAiPlannerBundle together) with the publish-and-activate flow, and note which suits your release process (M)

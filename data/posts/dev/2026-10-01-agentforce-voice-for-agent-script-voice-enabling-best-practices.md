---
title: "Agentforce Voice for Agent Script: Voice-Enabling Best Practices"
url: https://developer.salesforce.com/blogs/2026/10/agentforce-voice-for-agent-script-voice-enabling-best-practices
source: dev
date: 2026-10-01
authors: ["Alex Martinez"]
topics: ["Agentforce & AI", "Apex & Code", "DevOps & Tooling"]
---

- Voice-enabling an Agent Script agent is not a rewrite: you enable Agentforce Voice in the org, add three voice blocks to the script, and retune the instructions for listeners.
- The org must have Agentforce Voice turned on (it runs on Salesforce Voice with Telephony Providers). You can check by searching for Telephony under Add Connections in Agentforce Builder, and a free Developer Edition org currently doesn't support it.
- The three required script blocks are a top-level `language` (default_locale), `connection telephony` (which makes it a voice agent), and `modality voice` (outbound persona_id and model.id, inbound filler_words_detection).
- `language` must appear both at the top level and inside `modality voice`, because the persona_id resolves against a model and language and otherwise silently falls back to the default voice.
- Supported voice models are eleven_v3_conversational, eleven_flash_v2_5, eleven_flash_v2 (English only) and kotoba (Japanese). The model can only be set in Script view, and the legacy flat voice_id format cannot pick a model.

## Links
- **Agent Script** [docs]: Get to know the language for building agents in Agentforce Builder. Use Agent Script to build predictable, context-aware agent workflows that don't re  
  https://developer.salesforce.com/docs/einstein/genai/guide/agent-script.html
- **Agentforce Voice: AI Voice Agents For Every Channel** [other]: Deliver fast, natural conversations across phone, web, and mobile. Tailor agents to reflect your unique brand voice and provide consistent, trusted support.  
  Mentioned as "Agentforce Voice"  
  https://www.salesforce.com/ca/agentforce/voice/
- **agent-script-recipes/force-app/main/01_languageEssentials/languageSettings at main · trailheadapps/agent-script-recipes · GitHub** [repo]: A collection of easy-to-digest Agent Script examples. - agent-script-recipes/force-app/main/01_languageEssentials/languageSettings at main · trailheadapps/agent-script-recipes  
  Mentioned as "LanguageSettings recipe"  
  https://github.com/trailheadapps/agent-script-recipes/tree/main/force-app/main/01_languageEssentials/languageSettings
- **Voice Catalog** [docs]: This catalog lists the voice personas available for each Agentforce Voice model. To set a voice, open the page for your selected model, find the voice  
  Mentioned as "Voice Catalog for Agentforce Voice"  
  https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-voice-catalog.html
- **GitHub - trailheadapps/agent-script-recipes: A collection of easy-to-digest Agent Script examples. · GitHub** [repo]: A collection of easy-to-digest Agent Script examples. - trailheadapps/agent-script-recipes  
  Mentioned as "Agent Script Recipes repo"  
  https://github.com/trailheadapps/agent-script-recipes
- **Trailblazer Community** [trailhead]: no description available  
  https://trailhead.salesforce.com/trailblazercommunity
- **Get Started** [docs]: Agentforce is the agent-driven layer of the Salesforce Platform, and it helps you deploy AI agents that work side-by-side with your employees to exten  
  Mentioned as "Agentforce Developer Guide"  
  https://developer.salesforce.com/docs/einstein/genai/guide/get-started.html
- **Salesforce Developers YouTube** [other]: no description available  
  https://www.youtube.com/@SalesforceDevs
- **Learn MuleSoft: Video Tutorials, DataWeave & ACB** [other]: ProstDev — where MuleSoft mastery meets fun. Easy-to-follow video tutorials, AI experiments, and deep-dive articles on MuleSoft, DataWeave, Anypoint Code Builder, and integration.  
  Mentioned as "ProstDev"  
  https://prostdev.com
- **Trailblazer** [other]: Trailblazer Profile  
  Mentioned as "Trailblazer Community"  
  https://www.salesforce.com/trailblazer/devalexmartinez

## Suggested tasks
- [ ] Check whether your org has Agentforce Voice by looking for Telephony under Add Connections in Agentforce Builder (S)
- [ ] Clone Agent Script Recipes, deploy the voiceAgent recipe to a voice-enabled org, and test it by describing a bug out loud (M)
- [ ] Add language, connection telephony and modality voice blocks plus STT-repair instructions to an existing text Agent Script agent, and compare the voice behavior (L)

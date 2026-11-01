---
title: "Agentforce Voice for Agent Script: Route Real Phone Calls to Your Agent"
url: https://developer.salesforce.com/blogs/2026/10/agentforce-voice-for-agent-script-route-real-phone-calls-to-your-agent
source: dev
date: 2026-10-21
authors: ["Alex Martinez"]
topics: ["Agentforce & AI"]
---

- Second post in a series: take a voice-ready Agent Script agent and route real inbound phone calls to it. The script logic doesn't change.
- Needs an org with full Agentforce Voice (not a free Developer Edition), plus a phone number and an agent user.
- Check entitlements first with a SOQL query on `TenantUsageEntitlement` (ten-digit long code numbers and inbound voice credits).
- Setup is mostly Salesforce CLI from a DX project; the post ends with checking a call after you hang up.

## Links
- **Agentforce Voice for Agent Script: Voice-Enabling Best Practices** [other]: Learn how to voice-enable an Agent Script agent with Agentforce Voice, from configuring voice settings to writing instructions that make spoken conversations clear and natural.  
  https://developer.salesforce.com/blogs/2026/10/agentforce-voice-for-agent-script-voice-enabling-best-practices
- **Quick Start** [docs]: Salesforce CLI is a command-line interface that simplifies development and build automation when working with your Salesforce org. Use it to create an  
  Mentioned as "Salesforce CLI"  
  https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-setup-intro.html
- **Create Project** [docs]: Launch your VS Code desktop application and follow the given steps to create a Salesforce DX project:  
  Mentioned as "create a project in VS Code"  
  https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/create-project.html
- **Salesforce Extensions for Visual Studio Code** [docs]: The Salesforce Extension pack includes tools for developing on the Salesforce platform in the lightweight, extensible VS Code editor. These tools prov  
  Mentioned as "Salesforce Extensions"  
  https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/vscode-overview.html
- **Trailblazer Community** [trailhead]: no description available  
  https://trailhead.salesforce.com/trailblazer-community
- **Agentforce Voice: AI Voice Agents For Every Channel** [other]: Deliver fast, natural conversations across phone, web, and mobile. Tailor agents to reflect your unique brand voice and provide consistent, trusted support.  
  Mentioned as "Agentforce Voice"  
  https://www.salesforce.com/agentforce/voice/
- **Agent Script** [docs]: Get to know the language for building agents in Agentforce Builder. Use Agent Script to build predictable, context-aware agent workflows that don't re  
  Mentioned as "Agent Script (Agentforce Developer Guide)"  
  https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html
- **Salesforce CLI Command Reference** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.sfdx_cli_reference.meta/sfdx_cli_reference/
- **Omni-Channel Flows (Salesforce Help)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=service.how_does_an_omni_channel_flow_work.htm&type=5
- **Agent Platform Tracing: Debug Agentforce with Trace Trees, SOQL, and Slack** [other]: Trace Agentforce actions by capturing LLM calls, Flows, and Apex executions as queryable trees in Data 360. Learn to enable this service-level visibility and use Slackbot to pinpoint root causes instantly with natural language.  
  https://developer.salesforce.com/blogs/2026/05/agent-platform-tracing-debug-agentforce-with-trace-trees-soql-and-slack
- **GitHub - trailheadapps/agent-script-recipes: A collection of easy-to-digest Agent Script examples. · GitHub** [repo]: A collection of easy-to-digest Agent Script examples. - trailheadapps/agent-script-recipes  
  Mentioned as "Agent Script Recipes (GitHub)"  
  https://github.com/trailheadapps/agent-script-recipes

## Suggested tasks
- [ ] Check whether any org I have access to has Agentforce Voice entitlements (S)
- [ ] Read the prior 'Voice-Enabling Best Practices' post and voice-enable an agent in agent-script-recipes (M)

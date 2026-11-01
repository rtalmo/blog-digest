---
title: "Building Interactive UI with Headless Experience Layer"
url: https://developer.salesforce.com/blogs/2026/10/building-interactive-ui-with-hxl
source: dev
date: 2026-10-07
authors: ["Akshata Sawant"]
topics: ["Agentforce & AI", "LWC / UI", "Integration & APIs"]
---

- The Headless Experience Layer (HXL), part of the Headless Toolkit in AIforce, lets you define an interactive widget once in declarative JSON and render it natively in Agentforce and in MCP clients that support MCP Apps, such as Claude and ChatGPT.
- HXL has three core concepts: Components (surface-aware UI primitives), Widgets (composed experiences, stored as a UiWidgetBundle under uiWidgets/<name>/ with a .uiwidget-meta.xml, a composition JSON, and an optional schema.json), and Custom Lightning Types (CLTs) that bind data shape to a widget through renderer.json.
- Widgets are not LWC or React and contain no JavaScript. They use {!$attrs.x} placeholders and forEach/forItem for lists, and the data comes from an Apex invocable action, so existing sharing and field-level security still apply.
- Agentforce needs one CLT typed to the Apex class, and the Agent Script output must set complex_data_type_name and is_displayable: True. MCP needs two nested CLTs (inner mirrors the Apex output, outer mirrors the actionName/isSuccess/outputValues envelope) with paths like {!$attrs.outputValues.reviews.averageRating}, plus a uiResource on the MCP server tool definition.
- The beta supports two client actions, sendMessage and openLink. Agentforce may sometimes return follow-up answers as text instead of the card, so name the action explicitly in the subagent instructions. The HXL Playground previews can differ from live surfaces, so test on each target.

## Links
- **AIforce: Salesforce AI, Wherever You Already Work** [other]: Salesforce Einstein is your end to end solution to becoming an AI-first company.  
  Mentioned as "AIforce"  
  https://www.salesforce.com/artificial-intelligence/
- **Agentforce** [other]: Agentforce  
  https://developer.salesforce.com/developer-centers/agentforce
- **Headless Experience Layer** [other]: Headless Experience Layer (HXL) is Salesforce's agentic experience layer for securely deploying logic to any external app.  
  Mentioned as "Headless Experience Layer (HXL)"  
  https://www.salesforce.com/headless/agentic-experience-layer/
- **MCP Apps - Model Context Protocol** [other]: Interactive UI applications that render inside MCP hosts like Claude Desktop  
  Mentioned as "MCP Apps"  
  https://modelcontextprotocol.io/extensions/apps/overview
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "Salesforce Skills library"  
  https://github.com/forcedotcom/sf-skills
- **HXL Playground** [other]: Explore the Headless Experience Layer — build surface-agnostic widgets with Mosaic, preview them across Agentforce, Slack, and ChatGPT.  
  https://www.headlessexperiencelayer.com
- **Build a Rich UI for Agentforce Action Output** [docs]: Present structured output from an Agentforce action as a Headless Experience Layer (HXL) widget in the conversation.  
  Mentioned as "how to render a widget in Agentforce"  
  https://developer.salesforce.com/docs/platform/hxl/guide/agentforce-action-output.html
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "Apex invocable action"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm
- **HXL Playground** [other]: Explore the Headless Experience Layer — build surface-agnostic widgets with Mosaic, preview them across Agentforce, Slack, and ChatGPT.  
  https://www.headlessexperiencelayer.com/playground/
- **Build a Rich UI for External Agents** [docs]: Some AI agents use MCP to interact with data in your org, such as Claude Desktop, Slackbot, and ChatGPT. HXL widgets are compatible with the  
  Mentioned as "HXL MCP channels guide"  
  https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-channels.html
- **Give Agents UI with the Headless Experience Layer** [other]: no description available  
  https://developer.salesforce.com/workshops/aiforce-workshop/give-agents-ui-with-the-headless-experience-layer-hxl/overview
- **Trailblazer Community** [trailhead]: no description available  
  https://trailhead.salesforce.com/trailblazer-community
- **Get Started** [docs]: Headless Experience Layer (HXL) is a unified experience engine and platform designed to deliver consistent, portable, and rich user experiences across  
  Mentioned as "Headless Experience Layer: Get Started"  
  https://developer.salesforce.com/docs/platform/hxl/guide/get-started.html
- **Learn About HXL** [docs]: Widgets are platform-independent UI compositions. With widgets, you define rich, interactive interfaces once and deploy them across supported Salesfor  
  Mentioned as "Build Rich UI with HXL"  
  https://developer.salesforce.com/docs/platform/hxl/guide/hxl-rich-ui.html
- **Salesforce CLI** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  https://developer.salesforce.com/tools/salesforcecli
- **Use Agentforce Vibes to Build Widgets** [docs]: Agentforce Vibes provides the  
  Mentioned as "Use Agentforce Vibes to Build Widgets | Headless Experience Layer Developer Guide (Beta)"  
  https://developer.salesforce.com/docs/platform/hxl/guide/hxl-vibes.html

## Suggested tasks
- [ ] Paste the Pronto customerReviews.json composition into the HXL Playground and tweak the layout with sample data (S)
- [ ] Build a widget plus CLT for an existing Apex invocable action in a scratch org and render it in Agentforce Builder (M)
- [ ] Add the nested CLTs and a uiResource to an MCP server definition and test rendering the widget in Claude or ChatGPT (L)

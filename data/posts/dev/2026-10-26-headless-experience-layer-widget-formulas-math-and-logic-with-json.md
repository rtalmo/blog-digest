---
title: "Headless Experience Layer Widget Formulas: Math and Logic with JSON"
url: https://developer.salesforce.com/blogs/2026/10/headless-experience-layer-widget-formulas-math-and-logic-with-json
source: dev
date: 2026-10-26
authors: ["Charles Watkins"]
topics: ["LWC / UI", "Agentforce & AI"]
---

- HXL widgets (beta) are declarative JSON UI components that can be embedded in Claude, ChatGPT and Agentforce, with no JavaScript or lifecycle hooks.
- Formulas in `{!...}` expressions (based on the open-source Salesforce formula engine) let widgets do math and logic with IF, CASE, AND, LEN and so on.
- That moves display logic (win rate, phone-number check, badge variant) out of Apex and into the widget, next to the display.
- Includes a before/after of an account card widget and a link to a playground.

## Links
- **Building Interactive UI with Headless Experience Layer** [other]: Learn how the Headless Experience Layer (HXL) lets you build one interactive widget that renders in Agentforce and MCP clients like Claude and ChatGPT.  
  https://developer.salesforce.com/blogs/2026/10/building-interactive-ui-with-hxl
- **Composition File** [docs]: The  
  Mentioned as "formulas"  
  https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-composition.html
- **GitHub - salesforce/formula-engine: Extensible Formula Parser Engine with a Java, SQL, and Javascript execution engine. · GitHub** [repo]: Extensible Formula Parser Engine with a Java, SQL, and Javascript execution engine. - salesforce/formula-engine  
  Mentioned as "Salesforce formula engine"  
  https://github.com/salesforce/formula-engine
- **HXL Playground** [other]: Explore the Headless Experience Layer — build surface-agnostic widgets with Mosaic, preview them across Agentforce, Slack, and ChatGPT.  
  Mentioned as "Headless Experience Layer Playground"  
  https://www.headlessexperiencelayer.com/playground/?renderer=mcp-app&theme=chatgpt
- **Learn About HXL** [docs]: Widgets are platform-independent UI compositions. With widgets, you define rich, interactive interfaces once and deploy them across supported Salesfor  
  Mentioned as "Custom Lightning Type"  
  https://developer.salesforce.com/docs/platform/hxl/guide/hxl-rich-ui.html
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "Salesforce skills"  
  https://github.com/forcedotcom/sf-skills

## Suggested tasks
- [ ] Build the account card HXL widget in the playground (S)
- [ ] Refactor an Apex-computed display field into a widget formula (M)

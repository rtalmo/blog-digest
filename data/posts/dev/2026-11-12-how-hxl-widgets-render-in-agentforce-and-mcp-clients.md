---
title: "How HXL Widgets Render in Agentforce and MCP Clients"
url: https://developer.salesforce.com/blogs/2026/11/how-hxl-widgets-render-in-agentforce-and-mcp-clients
source: dev
date: 2026-11-12
authors: ["Alba Rivas"]
topics: ["Agentforce & AI", "Integration & APIs", "LWC / UI"]
---

- The Headless Experience Layer (HXL) beta lets you define a widget once and render it as an interactive card in Agentforce, Slackbot, Claude, and ChatGPT.
- Route 1 (Agentforce): the runtime stores the action output under a __tool_idx__ and sets __supports_result_display__ only if the output is marked is_displayable: True in Agent Script. The LLM must then choose to call the built-in __show_tool_results__ action, so the card is not guaranteed.
- In Route 1 the Agentforce Conversation Client hydrates the Custom Lightning Type (CLT) widget's {!$attrs...} placeholders in the browser and draws it as Lightning web components, with only JSON sent over the wire.
- Route 2 (MCP): the tool advertises a ui:// renderer in _meta.ui.resourceUri, the server hydrates the widget and returns it in _meta['salesforce/uiMetadata'], and the host draws it in a sandboxed iframe. The LLM reads only content and never sees _meta.
- Troubleshooting: for Route 1 check is_displayable, complex_data_type_name, and the trace for the __show_tool_results__ call. For Route 2 use MCP Inspector to check tools/list, resources/read, and isError. Claude Code in the terminal does not render widgets, and Slackbot shows HTML styled like Block Kit.

## Links
- **Get Started** [docs]: Headless Experience Layer (HXL) is a unified experience engine and platform designed to deliver consistent, portable, and rich user experiences across  
  Mentioned as "Headless Experience Layer (HXL)"  
  https://developer.salesforce.com/docs/platform/hxl/guide/get-started.html
- **Building Interactive UI with Headless Experience Layer** [other]: Learn how the Headless Experience Layer (HXL) lets you build one interactive widget that renders in Agentforce and MCP clients like Claude and ChatGPT.  
  https://developer.salesforce.com/blogs/2026/10/building-interactive-ui-with-hxl
- **GitHub - trailheadapps/pronto: Pronto sample app that showcases the Headless Toolkit · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - trailheadapps/pronto  
  Mentioned as "Pronto"  
  https://github.com/trailheadapps/pronto
- **pronto/src-base/main/default/aiAuthoringBundles/Employee_Assistant/Employee_Assistant.agent at main · trailheadapps/pronto · GitHub** [repo]: Pronto sample app that showcases the Headless Toolkit - pronto/src-base/main/default/aiAuthoringBundles/Employee_Assistant/Employee_Assistant.agent at main · trailheadapps/pronto  
  Mentioned as "getCustomerReviews action"  
  https://github.com/trailheadapps/pronto/blob/main/src-base/main/default/aiAuthoringBundles/Employee_Assistant/Employee_Assistant.agent
- **GetCustomerReviewsAction Apex class** [repo]: no description available  
  https://github.com/trailheadapps/pronto/blob/main/src-base/main/default/classes/actions/reviews/GetCustomerReviewsAction.cls
- **customerReviews widget** [repo]: no description available  
  https://github.com/trailheadapps/pronto/tree/main/src-base/main/default/uiWidgets/customerReviews
- **Build a Rich UI for Agentforce Action Output** [docs]: Present structured output from an Agentforce action as a Headless Experience Layer (HXL) widget in the conversation.  
  Mentioned as "Agentforce action output guide"  
  https://developer.salesforce.com/docs/platform/hxl/guide/agentforce-action-output.html
- **Agentforce Session Tracing** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.generative_ai_session_trace.htm&type=5
- **Build a Rich UI for External Agents** [docs]: Some AI agents use MCP to interact with data in your org, such as Claude Desktop, Slackbot, and ChatGPT. HXL widgets are compatible with the  
  Mentioned as "HXL MCP channels guide"  
  https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-channels.html
- **MCP Apps protocol** [repo]: no description available  
  https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx
- **Pronto Employee Server MCP server definition** [other]: no description available  
  https://example.com
- **MCP Inspector** [repo]: no description available  
  https://github.com/modelcontextprotocol/inspector
- **Build Rich Agentic UI with Headless Experience Layer** [other]: no description available  
  https://www.youtube.com/watch?v=LQHv9hMhqa4
- **Ask Me Anything (AMA)** [other]: no description available  
  https://www.youtube.com/watch?v=mnvGnN3ny-o
- **HXL Playground** [other]: Explore the Headless Experience Layer — build surface-agnostic widgets with Mosaic, preview them across Agentforce, Slack, and ChatGPT.  
  https://www.headlessexperiencelayer.com/playground/
- **MCP Apps overview** [other]: no description available  
  https://modelcontextprotocol.io/extensions/apps
- **GitHub** [repo]: no description available  
  https://github.com/albarivas

## Suggested tasks
- [ ] Deploy the Pronto sample app to a scratch org and test the customerReviews widget in Agentforce, checking the trace for the __show_tool_results__ call (M)
- [ ] Connect MCP Inspector to a Salesforce MCP server definition and verify tools/list _meta.ui.resourceUri, resources/read, and salesforce/uiMetadata in tools/call (M)
- [ ] Audit an existing Agent Script action output for is_displayable: True and a CLT complex_data_type_name, and add an instruction asking the agent to show the card (S)

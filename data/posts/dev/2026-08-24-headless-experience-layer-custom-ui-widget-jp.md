---
title: "Headless Experience Layer \u306b\u3088\u308b\u30ab\u30b9\u30bf\u30e0\u30a6\u30a3\u30b8\u30a7\u30c3\u30c8\uff1aMCP \u7d4c\u7531\u3067\u53d6\u5f15\u5148\u306e\u5546\u8ac7\u30b5\u30de\u30ea\u30fc\u3092 AI \u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u30a2\u30d7\u30ea\u306b\u8868\u793a\u3059\u308b"
url: https://developer.salesforce.com/blogs/2026/08/headless-experience-layer-custom-ui-widget-jp
source: dev
date: 2026-08-24
authors: ["Hiroyuki Inaba"]
topics: ["Agentforce & AI", "Integration & APIs", "LWC / UI"]
---

- The Headless Experience Layer (HXL), announced at TDX 2026, entered beta in August 2026 and lets Salesforce data appear as rich custom UI widgets in external AI agent apps such as Slackbot, ChatGPT and Claude.
- The post builds an account opportunity summary widget in 7 steps: an Apex invocable class, LightningTypes with a renderer, a UiWidgetBundle, a GenAiFunction, a McpServerDefinition, deployment, and enabling the MCP server and connecting from an agent app.
- Data flows through two separate paths: tools (the Apex action, registered through GenAiFunction in the API catalog) and resources (the widget UI), and McpServerDefinition ties them together.
- The MCP response is a 3-layer envelope (Result → OutputValues → Apex Summary), and renderer.json maps values into widget attributes with expressions like {!$attrs.outputValues.summary.accountName}. A wrong path depth means nothing displays.
- Widgets are built as JSON trees of tile/* components (row, column, avatar, badge, text, icon). Using a nonexistent tile/icon name such as 'currency' crashes the whole widget with a NullPointerException and only a generic 'unexpected error' message; 'briefcase' and 'dollar-sign' work.

## Links
- **Headless Experience Layer** [docs]: Develop UI-agnostic agentic apps that deliver consistent, rich, portable, and reusable AI-powered user experiences across various surfaces and inputs.  
  Mentioned as "Headless Experience Layer Developer Guide (Beta)"  
  https://developer.salesforce.com/docs/platform/hxl/overview
- **Trust Status** [other]: no description available  
  Mentioned as "Salesforce Status"  
  https://status.salesforce.com/
- **GitHub - hinabasfdc/hxl-mcp-widget-sample: HXL / MCP サンプル：取引先の商談サマリを AI エージェントアプリにカードとして表示するカスタムウィジェット · GitHub** [repo]: HXL / MCP サンプル：取引先の商談サマリを AI エージェントアプリにカードとして表示するカスタムウィジェット - hinabasfdc/hxl-mcp-widget-sample  
  Mentioned as "hinabasfdc/hxl-mcp-widget-sample"  
  https://github.com/hinabasfdc/hxl-mcp-widget-sample
- **Salesforce Hosted MCP Server 使い始め** [other]: Salesforce Hosted MCP Serverで生成AIエージェントからSalesforceデータに安全にアクセス。外部クライアントアプリの作成、MCP Serverの有効化、クライアント設定まで初期セットアップを画像付きで解説します。  
  https://developer.salesforce.com/jpblogs/2026/04/salesforce-hosted-mcp-server-jp

## Suggested tasks
- [ ] Enable HXL in a Developer Edition org on Summer '26 Patch 14.4+ and deploy the hxl-mcp-widget-sample repo (M)
- [ ] Connect the deployed MCP server to Claude or ChatGPT and test the account opportunity summary widget with real data (M)
- [ ] Build a second HXL widget for a different object, trying out other tile/* components and checking valid icon names (L)

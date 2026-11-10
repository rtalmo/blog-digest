---
title: "Amazon Bedrock \u304b\u3089 MCP \u30b5\u30fc\u30d0\u30fc\u7d4c\u7531\u3067 Salesforce \u3092\u89e6\u308b"
url: https://developer.salesforce.com/blogs/2026/11/jp-access-salesforce-from-amazon-bedrock-via-mcp-server
source: dev
date: 2026-11-06
authors: ["odasho"]
topics: ["Agentforce & AI", "Integration & APIs", "Security & Admin"]
---

- The post shows how to build a Python agent with AWS's open-source Strands Agents SDK that reads Salesforce Cases through the Salesforce Hosted MCP Server, has an Amazon Bedrock model (Amazon Nova 2 Lite) judge priority, and writes the Priority field back without any Salesforce API code.
- Setup: enable the sobject-reads and sobject-mutations servers under Setup > MCP Servers (up to 2 minutes to go live), then create an External Client App with the mcp_api and refresh_token/offline_access scopes and a localhost callback. The app can take up to 30 minutes to become usable.
- Access is narrowed in four layers: the authorizing user's permissions, using sobject-mutations (which has no delete tool), Strands `tool_filters` limiting tools to soqlQuery and updateSobjectRecord, and an optional Strands Interrupts human-approval step that the post leaves out.
- Authentication uses an OAuth 2.0 authorization code flow with PKCE, handled by a small sf_auth.py script that stores the token at ~/.config with 0600 permissions and refreshes it after 60 minutes.
- Caveats: Nova 2 reasoning must be enabled or the model sometimes skips the update tool call. The agent re-queries after updating to verify the writes. One run used about 10k input and 3.5k output tokens. Hosted MCP Server may incur Flex Credits charges, and it isn't available in orgs that lack the MCP Servers setup page.

## Links
- **Developer Edition with Agentforce and Data 360** [other]: Build enterprise-quality apps fast and get hands-on with Agentforce and Data 360.  
  Mentioned as "Developer Edition"  
  https://developer.salesforce.com/signup
- **Salesforce CLI** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  https://developer.salesforce.com/tools/salesforcecli
- **Update Salesforce CLI** [docs]: If you want to ensure that you’re running the latest version of Salesforce CLI, you can manually update it.  
  https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-setup-update-cli.html
- **uv** [other]: uv is an extremely fast Python package and project manager, written in Rust.  
  https://docs.astral.sh/uv/
- **Installation** [other]: uv is an extremely fast Python package and project manager, written in Rust.  
  Mentioned as "Upgrading uv"  
  https://docs.astral.sh/uv/getting-started/installation/
- **Find Your Server URL** [docs]: Each MCP client connects to a Salesforce Hosted MCP Server through a server URL. The URL format depends on your org type and on whether you connect th  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/server-urls.html
- **Salesforce Hosted MCP Server 使い始め** [other]: Salesforce Hosted MCP Serverで生成AIエージェントからSalesforceデータに安全にアクセス。外部クライアントアプリの作成、MCP Serverの有効化、クライアント設定まで初期セットアップを画像付きで解説します。  
  https://developer.salesforce.com/jpblogs/2026/04/salesforce-hosted-mcp-server-jp
- **Get Started** [docs]: Salesforce Hosted MCP Servers give AI agents a secure, governed way to interact with Salesforce data and automation. Using the open  
  Mentioned as "Hosted MCP Servers: Get Started"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html
- **SObject Reads** [docs]: The  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/sobject-reads.html
- **SObject Mutations** [docs]: The  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/sobject-mutations.html
- **Create an External Client App** [docs]: To integrate third-party applications with your Salesforce org via APIs and security controls, you must use an External Client App for registration an  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/create-external-client-app.html
- **Log Into Your Org** [docs]: Your MCP client authenticates with your org by using OAuth in a web browser. The MCP specification doesn't support multitenant systems like Salesforce  
  Mentioned as "Log In to Your Org"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/log-into-org.html
- **Connect your agent to MCP tools** [other]: Connect AI agents to any MCP server for tool access. Strands agents integrate and invoke MCP tools without custom integration code.  
  https://strandsagents.com/docs/user-guide/sdk/tools/mcp-tools/
- **MCP Transports** [other]: How a Strands agent reaches an MCP server: stdio for local processes, Streamable HTTP and SSE for remote servers, with OAuth and AWS IAM authentication.  
  https://strandsagents.com/docs/user-guide/sdk/tools/mcp-transports/
- **Amazon Bedrock** [other]: Use Amazon Bedrock models in Strands agents. Configure AWS credentials, model settings, guardrails, prompt caching, and multi-modal input.  
  https://strandsagents.com/docs/user-guide/sdk/model-providers/amazon-bedrock/
- **Interrupts** [other]: Pause AI agents mid-execution for human approval, input, or review. Build human-in-the-loop workflows with interrupt and resume patterns.  
  https://strandsagents.com/docs/user-guide/sdk/interrupts/
- **API キー - Amazon Bedrock** [other]: Amazon Bedrock API キーを生成して使用し、 AWS 認証情報を設定せずに API リクエストを認証します。  
  Mentioned as "API キー"  
  https://docs.aws.amazon.com/ja_jp/bedrock/latest/userguide/api-keys.html
- **Nova 2 Lite - Amazon Bedrock** [other]: bedrock-runtimeエンドポイントを使用した暗黙的および明示的なプロンプトキャッシュ  
  Mentioned as "Nova 2 Lite"  
  https://docs.aws.amazon.com/ja_jp/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html
- **ツールの使用 (関数呼び出し) - Amazon Nova** [other]: 関数呼び出しを使用して、外部ツールと API で Amazon Nova 機能を拡張する方法について説明します。  
  Mentioned as "ツールの使用 (関数呼び出し)"  
  https://docs.aws.amazon.com/ja_jp/nova/latest/nova2-userguide/using-tools.html
- **トラブルシューティング - Amazon Nova** [other]: このセクションでは、Amazon Nova モデルを使用する際の一般的な問題の解決策を示します。  
  Mentioned as "トラブルシューティング"  
  https://docs.aws.amazon.com/ja_jp/nova/latest/nova2-userguide/troubleshooting.html

## Suggested tasks
- [ ] Enable sobject-reads and sobject-mutations in a Developer Edition org, create the External Client App, and run sf_auth.py login to verify the PKCE flow (M)
- [ ] Build the Strands Agents + Bedrock case-triage agent against the BEDROCK-DEMO test Cases and confirm the Priority updates and the re-query check (M)
- [ ] Add a Strands Interrupts human-approval step before updateSobjectRecord and compare behavior with and without it (S)

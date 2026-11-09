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
- **Developer Edition** [other]: no description available  
  https://developer.salesforce.com/signup
- **Salesforce CLI** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  https://developer.salesforce.com/tools/salesforcecli
- **Update Salesforce CLI** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/sfdx-setup/guide/sfdx-setup-update-cli.html
- **uv** [other]: no description available  
  https://docs.astral.sh/uv/
- **Upgrading uv** [other]: no description available  
  https://docs.astral.sh/uv/getting-started/installation/
- **Find Your Server URL** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/server-urls.html
- **Salesforce Hosted MCP Server 使い始め** [other]: Salesforce Hosted MCP Serverで生成AIエージェントからSalesforceデータに安全にアクセス。外部クライアントアプリの作成、MCP Serverの有効化、クライアント設定まで初期セットアップを画像付きで解説します。  
  https://developer.salesforce.com/jpblogs/2026/04/salesforce-hosted-mcp-server-jp
- **Get Started** [docs]: Salesforce Hosted MCP Servers give AI agents a secure, governed way to interact with Salesforce data and automation. Using the open  
  Mentioned as "Hosted MCP Servers: Get Started"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html
- **SObject Reads** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/sobject-reads.html
- **SObject Mutations** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/sobject-mutations.html
- **Create an External Client App** [docs]: To integrate third-party applications with your Salesforce org via APIs and security controls, you must use an External Client App for registration an  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/create-external-client-app.html
- **Log In to Your Org** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/log-into-org.html
- **Connect your agent to MCP tools** [other]: no description available  
  https://strandsagents.com/docs/user-guide/sdk/tools/mcp-tools/
- **MCP Transports** [other]: no description available  
  https://strandsagents.com/docs/user-guide/sdk/tools/mcp-transports/
- **Amazon Bedrock** [other]: no description available  
  https://strandsagents.com/docs/user-guide/sdk/model-providers/amazon-bedrock/
- **Interrupts** [other]: no description available  
  https://strandsagents.com/docs/user-guide/sdk/interrupts/
- **API キー** [other]: no description available  
  https://docs.aws.amazon.com/ja_jp/bedrock/latest/userguide/api-keys.html
- **Nova 2 Lite** [other]: no description available  
  https://docs.aws.amazon.com/ja_jp/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html
- **ツールの使用 (関数呼び出し)** [other]: no description available  
  https://docs.aws.amazon.com/ja_jp/nova/latest/nova2-userguide/using-tools.html
- **トラブルシューティング** [other]: no description available  
  https://docs.aws.amazon.com/ja_jp/nova/latest/nova2-userguide/troubleshooting.html

## Suggested tasks
- [ ] Enable sobject-reads and sobject-mutations in a Developer Edition org, create the External Client App, and run sf_auth.py login to verify the PKCE flow (M)
- [ ] Build the Strands Agents + Bedrock case-triage agent against the BEDROCK-DEMO test Cases and confirm the Priority updates and the re-query check (M)
- [ ] Add a Strands Interrupts human-approval step before updateSobjectRecord and compare behavior with and without it (S)

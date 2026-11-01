---
title: "Salesforce Hosted MCP Server\u3092\u30bb\u30ad\u30e5\u30a2\u306b\u3059\u308b\u65b9\u6cd5"
url: https://developer.salesforce.com/blogs/2026/09/how-to-secure-salesforce-hosted-mcp-servers-jp
source: dev
date: 2026-09-16
authors: ["Philippe Ozil"]
topics: ["Security & Admin", "Agentforce & AI", "Integration & APIs"]
---

- Salesforce Hosted MCP Server security is built in layers: authentication, authorization, permission control (object/field level), and logging for audit.
- Authentication supports only the OAuth 2.0 authorization code flow through an External Client App (ECA). Shared service or integration-user sessions are called an anti-pattern, and machine-to-machine flows are not planned.
- A dedicated ECA per MCP client (Claude, ChatGPT, Cursor) is strongly recommended. The new `mcp_api` OAuth scope grants MCP server access without the broad `api` scope.
- Authorization controls include restricting ECA access to approved profiles or permission sets (for example an "MCP Client User" permission set), trusted IP ranges, and a shorter refresh token lifetime (the default is 1 year). Tokens can be revoked in Setup under OAuth Usage.
- All MCP servers are disabled by default, so enable only the ones you want to expose. Tool annotations (for example destructive or idempotent hints) help agents behave safely, but clients are not required to honor them.

## Links
- **Get Started** [docs]: Salesforce Hosted MCP Servers give AI agents a secure, governed way to interact with Salesforce data and automation. Using the open  
  Mentioned as "Salesforce Hosted MCP（Model Context Protocol）Server"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html
- **Standard Servers** [docs]: Salesforce provides a set of standard MCP servers that expose built-in platform and product capabilities. These servers are pre-configured by Salesfor  
  Mentioned as "標準機能"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/servers-reference.html
- **Build Custom MCP Servers** [docs]: Salesforce ships various standard MCP servers bundling out-of-box capabilities oriented around discrete product areas. To combine MCP tools from diffe  
  Mentioned as "カスタム機能"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/custom-servers.html
- **Authorization - Model Context Protocol** [other]: no description available  
  Mentioned as "MCPの仕様"  
  https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- **RFC 6749 - The OAuth 2.0 Authorization Framework** [other]: The OAuth 2.0 Authorization Framework (RFC 6749, )  
  Mentioned as "OAuth 2.0"  
  https://datatracker.ietf.org/doc/html/rfc6749
- **外部クライアントアプリ** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5
- **認可コードフロー** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_web_server_flow.htm&type=5
- **OAuth範囲** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_tokens_scopes.htm&type=5
- **アプリケーションポリシー** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.preauth_user_app_access_through_eca.htm&type=5
- **Create an External Client App** [docs]: To integrate third-party applications with your Salesforce org via APIs and security controls, you must use an External Client App for registration an  
  Mentioned as "こちらのドキュメント"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/create-external-client-app.html
- **有効** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.api_catalog_activate_salesforce_mcp_servers.htm&type=5
- **アノテーションを付ける** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.api_catalog_create_custom_salesforce_mcp_servers.htm&type=5
- **Schema Reference - Model Context Protocol** [other]: no description available  
  Mentioned as "MCPツールのアノテーション"  
  https://modelcontextprotocol.io/specification/2025-06-18/schema
- **中核的なセキュリティモデル** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.security_data_access.htm&type=5
- **Security Best Practices** [docs]: Secure your deployment with proper authentication, permission controls, and monitoring.  
  Mentioned as "カスタムツールを実装する"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/security-best-practices.html
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "セキュリティのベストプラクティス"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_perms_enforcing.htm
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "メソッド"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing_tools_runas.htm
- **Salesforce Hosted MCP Servers** [docs]: Give AI agents a secure, governed way to interact with Salesforce data and automation using the Model Context Protocol (MCP). Any compatible AI client  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers
- **APIカタログでのMCPサーバーの管理** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.api_catalog_manage_mcp_servers.htm
- **権限セット** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=sf.perm_sets_overview.htm
- **Home · forcedotcom/mcp-hosted Wiki · GitHub** [repo]: Salesforce Hosted MCP Servers. Contribute to forcedotcom/mcp-hosted development by creating an account on GitHub.  
  Mentioned as "Community Wiki"  
  https://github.com/forcedotcom/mcp-hosted/wiki
- **pozil (Philippe Ozil) · GitHub** [repo]: Principal Developer Advocate at Salesforce. Full stack coder, DevOps expert, ex VR dev and robot master. - pozil  
  Mentioned as "GitHubのプロジェクト"  
  https://github.com/pozil

## Suggested tasks
- [ ] Create a dedicated ECA with the mcp_api scope, restricted to an MCP Client User permission set, in a scratch org or sandbox (M)
- [ ] Shorten the refresh token policy and add trusted IP ranges on the MCP ECA, then test token revocation under OAuth Usage (S)
- [ ] Pull the API Total Usage event log and filter for SALESFORCE_HOSTED_MCP rows to review user, status code, and IP patterns (S)

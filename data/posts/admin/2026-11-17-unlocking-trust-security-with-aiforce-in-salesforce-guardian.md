---
title: "Unlocking Trust & Security with AIforce in Salesforce Guardian"
url: https://admin.salesforce.com/blog/2026/unlocking-trust-security-with-aiforce-in-salesforce-guardian
source: admin
date: 2026-11-17
authors: ["Kate Lessard"]
topics: ["Security & Admin", "Agentforce & AI", "Data Cloud"]
---

- Salesforce security is a shared responsibility split into three layers: Foundationals (built-in, maintained by Salesforce), Configurables (MFA, IP allowlisting, permission sets, Health Check), and Enhanceables (the Salesforce Guardian product portfolio).
- Salesforce Guardian rests on three pillars: Data Security (Shield, Security Center), Data Compliance (Privacy Center, Data Mask & Seed), and Data Resilience (Backup & Recover, Archive).
- Compliance Agent, part of Privacy Center, scans core metadata to set a compliance baseline, produces a compliance score tied to regulatory goals, and offers actionable remediation plans; it depends on classified grounding data (GDPR, HIPAA, PII categories) to work well.
- Security Mesh, part of Security Center, normalizes security signals from partners like Okta and CrowdStrike into a single view and supports detections such as Impossible Travel.
- MCP Security (currently in beta, part of Security Center) scans each MCP server at registration and shows Low/Medium/High risk scores so admins can block risky servers before agents reach them.

## Links
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20261116105320/3layerssecurityarch.jpg** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20261116105320/3layerssecurityarch.jpg
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20261116105700/securitymeshdataflow.jpg** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20261116105700/securitymeshdataflow.jpg
- **Model Context Protocol (MCP) Security** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_security_security_center_mcp_servers.htm&language=en_US&r=https%3A%2F%2Fwww.google.com%2F&type=5
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20261116105839/securitycentermcpserversdashboard.jpg** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20261116105839/securitycentermcpserversdashboard.jpg
- **Protecting Data with the Principle of Least Privilege** [other]: Traditional network security is not enough to stay ahead of threats. Learn how the principle of least privilege can help protect your data.  
  Mentioned as "Principle of Least Privilege"  
  https://www.salesforce.com/blog/principle-of-least-privilege/
- **MCP Security beta** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_security_security_center_mcp_servers.htm&release=264&type=5
- **Trusted Enterprise Security: Built on Salesforce – salesforcesecurity.go-vip.net** [other]: no description available  
  Mentioned as "Trusted Enterprise Security: Built on Salesforce"  
  https://security.salesforce.com/security-video-series/
- **Unify Your Security Data with Salesforce Security Mesh** [other]: Discover how Salesforce Security Mesh unifies disparate security data to simplify threat detection and enhance your security posture.  
  Mentioned as "Introducing Security Mesh: Unify Your Security Data for Greater Visibility"  
  https://www.salesforce.com/blog/security-mesh/
- **Explore New Enhancements in Trusted and Developer Services** [trailhead]: Discover the latest features in Platform Trusted and Developer Services. Learn how these enhancements empower the development of trusted AI applications  
  Mentioned as "See What’s New: Platform Trusted and Developer Services"  
  https://trailhead.salesforce.com/content/learn/modules/summer-26-release-highlights/see-whats-new-platform-trusted-and-developer-services
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Audit agent and user permission sets for least privilege and classify the data used to ground agents (M)
- [ ] Try the MCP Security beta in a sandbox and review the risk scores for registered MCP servers (S)

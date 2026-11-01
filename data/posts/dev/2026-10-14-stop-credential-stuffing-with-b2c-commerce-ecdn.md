---
title: "Stop Credential Stuffing with B2C Commerce eCDN"
url: https://developer.salesforce.com/blogs/2026/10/stop-credential-stuffing-with-b2c-commerce-ecdn
source: dev
date: 2026-10-14
authors: ["Sarah Welker"]
topics: ["Security & Admin", "Releases"]
---

- B2C Commerce release 26.9 adds four eCDN detection fields (`cf.waf.credential_check.*`) for leaked-credential detection, with no third-party bot-management entitlement needed.
- Use them in firewall and rate-limiting rules; Managed Challenge is available as a rule action.
- Prerequisite: Salesforce must enable the Leaked-Credential-Check managed transform for your zone via a support case.
- Covers SFRA, SLAS (Basic auth is decoded, so PWA Kit and headless are covered), a working SFRA example that prompts a password reset, and how to monitor detections.

## Links
- **SFRA Features and Components** [docs]: SFRA is carefully architected so that it's easy to use as a blueprint for your own storefront. Built-in features and components provide a range of opt  
  Mentioned as "SFRA"  
  https://developer.salesforce.com/docs/commerce/sfra/guide/b2c-sfra-features-and-comps.html
- **eCDN Custom Rules** [docs]: Use custom rules to control incoming traffic by setting up security policies based on request parameters. With custom rules, you have complete control  
  Mentioned as "custom-rules examples"  
  https://developer.salesforce.com/docs/commerce/commerce-api/guide/cdn-zones-custom-rules.html
- **eCDN Rate Limiting Rules** [docs]: Use rate limiting rules to specify rate limits for requests that match a particular expression and then perform an action when those rate limits are r  
  Mentioned as "Allow verified search crawlers and detect leaked credentials"  
  https://developer.salesforce.com/docs/commerce/commerce-api/guide/cdn-rate-limiting-rules.html
- **Warn Shoppers About Leaked Credentials in SFRA (B2C Commerce eCDN 26.9) · GitHub** [repo]: Warn Shoppers About Leaked Credentials in SFRA (B2C Commerce eCDN 26.9) - 0_README.md  
  Mentioned as "full SFRA walkthrough gist"  
  https://gist.github.com/rvenkatraman101/e322f71d91c63533e5b16c83da999ff4
- **eCDN Logpush** [docs]: eCDN Logpush delivers eCDN logs in batches to specified destinations. eCDN logs contain valuable information, such as the client IP address, the reque  
  https://developer.salesforce.com/docs/commerce/commerce-api/guide/cdn-zones-logpush.html
- **https://youtu.be/vr3n6XLgEtU** [other]: no description available  
  https://youtu.be/vr3n6XLgEtU
- **Bot Management** [docs]: Successful bot protection and management for Salesforce B2C Commerce storefronts is a shared responsibility between Salesforce and our customers. Thes  
  Mentioned as "Bot Management Developer Guide"  
  https://developer.salesforce.com/docs/commerce/commerce-solutions/guide/bot-management.html
- **Bot Mitigation Best Practices for Flash Sales** [docs]: As you might expect, flash sales are an extremely attractive target for bot attacks. During a flash sale (also called a hype or high-volume sale), a l  
  https://developer.salesforce.com/docs/commerce/commerce-solutions/guide/bot-mitigation-sk.html
- **SLAS Best Practices** [docs]: Follow best practices for the Shopper Login and API Access Service (SLAS) to maximize security and performance. Recommended steps include using a priv  
  https://developer.salesforce.com/docs/commerce/commerce-api/guide/slas-best-practices.html
- **Leaked Credentials release notes** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_b2c_ecdn_leaked_credentials.htm&release=262&type=5

## Suggested tasks
- [ ] Review the SFRA example and decide whether it applies to any storefront I work on (S)

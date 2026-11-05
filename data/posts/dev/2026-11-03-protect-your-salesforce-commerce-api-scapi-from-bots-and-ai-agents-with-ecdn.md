---
title: "Protect Your Salesforce Commerce API (SCAPI) from Bots and AI Agents with eCDN"
url: https://developer.salesforce.com/blogs/2026/11/protect-your-salesforce-commerce-api-scapi-from-bots-and-ai-agents-with-ecdn
source: dev
date: 2026-11-03
authors: ["Sarah Welker"]
topics: ["Security & Admin", "Integration & APIs", "Releases"]
---

- The October 2026 B2C Commerce release makes the SCAPI zone (the eCDN zone in front of Commerce API traffic) manageable in Business Manager and the CDN API. One zone is shared across Dev, Staging, and Production and is managed from Production only.
- The SCAPI zone supports custom firewall rules, rate limiting, IP access lists, analytics, and cache purge. It does not support WAF managed rulesets, mTLS, TLS 1.3 settings, HSTS, Page Shield, or Under Attack Mode, and the Crypto tab is read-only.
- The new SCAPI Identity Header (SIH) lets you accept Shopper API traffic only from Managed Runtime. Enable the Managed Runtime SCAPI Request Identification feature per instance, then add a custom block rule on the instance's path segment (e.g. f_ecom_abcd_prd plus /shopper) after the locked managed allow rule. Start in Log mode before switching to Block.
- Custom BFFs, mobile backends, and partner integrations can't present the SIH, so each needs its own allow rule with a server-side shared-secret header, placed above the block rule. SLAS hardening: Strict Client Auth requires an x-slas-client-auth header for private clients, but PWA Kit and Storefront Next don't send it yet, so enabling it for those clients breaks shopper login with 401s. SLAS also throttles refresh-token exchanges to 3 per 60 seconds, returning a 429 beyond that.
- Two new fields work on every eCDN zone: Known Bot (cf.client.bot) and Verified Bot Category (cf.verified_bot_category, 17 categories such as AI Crawler, AI Search, AI Assistant, and Search Engine Crawler). Use them to rate limit AI traffic on expensive endpoints like product search (example: 30 requests per 60 seconds per IP, log first). They cover only Cloudflare-verified bots, so unverified or spoofed automation needs bot scores or a third-party bot manager.

## Links
- **SCAPI** [docs]: The B2C Commerce API (SCAPI) is a set of RESTful APIs for building storefronts, merchant tools, and integrations on the B2C Commerce platform. It also  
  Mentioned as "B2C Commerce API (SCAPI)"  
  https://developer.salesforce.com/docs/commerce/commerce-api/guide/scapi-get-started.html
- **Under Attack Mode** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=cc.b2c_enable_under_attack_mode.htm&type=5
- **SLAS Best Practices** [docs]: Follow best practices for the Shopper Login and API Access Service (SLAS) to maximize security and performance. Recommended steps include using a priv  
  https://developer.salesforce.com/docs/commerce/commerce-api/guide/slas-best-practices.html
- **SEO & Discoverability for B2C Commerce** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=cc.b2c_seo_overview.htm&type=5
- **Bot Management** [docs]: Successful bot protection and management for Salesforce B2C Commerce storefronts is a shared responsibility between Salesforce and our customers. Thes  
  Mentioned as "Bot Management Developer Guide"  
  https://developer.salesforce.com/docs/commerce/commerce-solutions/guide/bot-management.html
- **Stop Credential Stuffing with B2C Commerce eCDN** [other]: Protect your B2C Commerce storefront from credential stuffing with new eCDN leaked-credential detection. Learn how to configure firewall and rate-limiting rules, detect suspicious login attempts, and prompt shoppers to reset exposed passwords.  
  Mentioned as "Stop Credential Stuffing at the Edge with B2C Commerce eCDN"  
  https://developer.salesforce.com/blogs/2026/10/stop-credential-stuffing-with-b2c-commerce-ecdn
- **SCAPI Zone overview** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=cc.b2c_scapi_zone.htm&type=5
- **Restrict SCAPI Access to Managed Runtime Traffic** [docs]: Lock down Shopper API requests so that they are accepted only from your Managed Runtime (MRT) environments, closing off the direct-access path that bo  
  Mentioned as "Restrict SCAPI Access to Managed Runtime Traffic (SCAPI Identity Header)"  
  https://developer.salesforce.com/docs/commerce/pwa-kit-managed-runtime/guide/scapi-request-identification.html
- **Secure Your Site** [docs]: Ensuring data privacy and trusted access to ecommerce systems is a critical part of the B2C Commerce platform. All interactions with the B2C Commerce  
  Mentioned as "SCAPI Security"  
  https://developer.salesforce.com/docs/commerce/commerce-api/guide/security.html
- **Allow Traffic from Search Engine and Other Verified Bots with eCDN Rules** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_b2c_ecdn_verified_bots.htm&release=262&type=5
- **Create a Custom Firewall Rule for an eCDN Zone** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=cc.b2c_create_eCDN_firewall_rule.htm&language=en_US&type=5
- **Create a Rate Limiting Rule for an eCDN Zone** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=cc.b2c_eCDN_create_rate_limiting_rule.htm&language=en_US&type=5
- **Knowledge Article: Mitigating Scrapers and AI Crawlers** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=000391633&type=1
- **Knowledge Article: AI Crawler and Agent Traffic** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=005460913&type=1

## Suggested tasks
- [ ] Audit which API clients call Shopper API directly (BFFs, mobile, partners) and map them to needed SIH allow rules (M)
- [ ] Create a Log-mode custom firewall rule on the SCAPI zone for direct /shopper traffic and review Security Analytics matches before enforcing (M)
- [ ] Add a Log-mode rate limiting rule for AI Crawler and AI Search categories on product-search and review thresholds against real traffic (S)

---
title: "Protect Apex Shares: Custom Row Causes on Standard Objects"
url: https://developer.salesforce.com/blogs/2026/10/protect-apex-shares-custom-row-causes-on-standard-objects
source: dev
date: 2026-10-20
authors: ["Larry Tung"]
topics: ["Apex & Code", "Security & Admin", "Releases"]
---

- Standard objects now support custom row causes (Apex sharing reasons), rolling out to all orgs by end of October 2026; this removes the old reliance on the Manual row cause.
- New setting 'Keep Manual Shares when Transferring Records' (available now) stops manual shares being deleted on owner change.
- Define the reason in Metadata API (`sharingReasons`, e.g. `Case.On_Call_Expert__c`), then use it in Apex (`CaseShare.RowCause`) or in Flow.
- Benefit: Apex shares stay separate from users' manual shares, and admins can see why each user has access.

## Links
- **rolling out for standard objects** [docs]: no description available  
  https://help.salesforce.com/s/articleView?language=en_US&id=release-notes.rn_apex_standard_sharing_reasons.htm&release=264&type=5
- **Keep Manual Shares when Transferring Records** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.security_sharing_keep_manual_transfer.htm&type=5
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "Sharing a Record Using Apex"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_bulk_sharing_creating_with_apex.htm
- **AIforce** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_headless360.htm&release=264&type=5
- **Setup with Agentforce** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.setup_agentforce_overview.htm&type=5
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "Understanding Apex Managed Sharing"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_bulk_sharing.htm
- **Protecting Force.com Custom Sharing Code** [other]: The programmatic sharing capabilities of the Force.com platform are very powerful and flexible, but you have to practice a bit of defensive coding to keep our code from undoing yours. With Apex sharing reasons or one of the strategies described in this post, you can keep the shares you create from being deleted by record owner changes and maintain the integrity of your custom sharing model.  
  Mentioned as "Protecting Force.com Custom Sharing Code (2013)"  
  https://developer.salesforce.com/blogs/2013/02/protecting-force-com-custom-sharing-code
- **Salesforce Data Security Model — Explained Visually** [other]: To provide a security model that satisfies numerous, unique real-world business cases, Salesforce provides a comprehensive and flexible data security model to secure data at different levels. Salesforce also provides sharing tools to open up and allow secure access to data based on business needs. In this post, I explain how security features work together by taking a real-world scenario and describing it using images and GIFs.  
  Mentioned as "Salesforce Data Security Model — Explained Visually (2017)"  
  https://developer.salesforce.com/blogs/developer-relations/2017/04/salesforce-data-security-model-explained-visually
- **IdeaExchange** [other]: no description available  
  Mentioned as "IdeaExchange: Allow Custom RowCause values for Standard Objects"  
  https://ideas.salesforce.com/s/idea/a0B8W00000GddnHUAR/allow-custom-rowcause-values-for-standard-objects-ie-accountshare

## Suggested tasks
- [ ] Audit my Apex sharing code for Manual-row-cause workarounds that can be deleted (M)
- [ ] Prototype the On-Call Expert CaseShare example in a scratch org (S)

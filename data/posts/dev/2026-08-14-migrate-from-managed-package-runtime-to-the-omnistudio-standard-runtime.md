---
title: "Migrate From Managed Package Runtime to the Omnistudio Standard Runtime"
url: https://developer.salesforce.com/blogs/2026/08/migrate-from-managed-package-runtime-to-the-omnistudio-standard-runtime
source: dev
date: 2026-08-14
authors: ["Sarah Welker"]
topics: ["Releases", "DevOps & Tooling", "Integration & APIs"]
---

- The Omnistudio Migration Assistant (OMA), a Salesforce CLI plugin, automates moving Flexcards, Omniscripts, Data Mappers and Integration Procedures from managed package runtimes (Vlocity Industries or Omnistudio Foundation) to the Omnistudio standard runtime.
- Salesforce cites internal testing in which execution averaged 2112 ms on the standard runtime versus 5061 ms on a managed package runtime, with claimed gains of up to 5x for Flexcards, 4x for Integration Procedures, 3x for Data Mappers and 2x for Omniscripts.
- Migration has three phases (development, validation, production). The first runs OMA in Assess mode, fixes flagged issues until the report is clean, then runs Migrate mode. The tool is installed with `sf plugins install @salesforce/plugin-omnistudio-migration-tool@2.0.0-rc.57`, and the commands are `sf omnistudio:migration:assess` and `sf omnistudio:migration:migrate` with `-u` and `-a`.
- Prerequisites and caveats: upgrade to Vlocity Industries managed package Winter '26 or later first; never migrate directly in production; and do not uninstall the package afterward, because existing workflows may still rely on its schema.
- OMA is said to cut manual effort by 95%, but older Angular-based components and industry-specific object mappings still need manual work. Customers already on the standard runtime need no action, and Omnistudio has been package-free for new customers since Summer '25.

## Links
- **@salesforce/plugin-omnistudio-migration-tool - npm** [other]: This SFDX plugin migrates FlexCard, OmniScript, DataRaptor, and Integration Procedure custom objects to standard objects.. Latest version: 1.7.0, last published: a year ago. Start using @salesforce/plugin-omnistudio-migration-tool in your project by running `npm i @salesforce/plugin-omnistudio-migration-tool`. There are no other projects in the npm registry using @salesforce/plugin-omnistudio-migration-tool.  
  Mentioned as "Omnistudio Migration Assistant (OMA)"  
  https://www.npmjs.com/package/@salesforce/plugin-omnistudio-migration-tool?activeTab=versions
- **Communications Cloud** [other]: Run your communications business smarter, faster, and more efficiently with Communications Cloud the #1 AI CRM for communications built on the Salesforce Platform.  
  Mentioned as "Communications"  
  https://www.salesforce.com/communications/cloud/
- **Best CRM for Media Companies: Media Cloud** [other]: Explore media CRM pricing for Salesforce Media Cloud and find the right solution for your business needs.  
  Mentioned as "Media"  
  https://www.salesforce.com/media/cloud/
- **Energy & Utilities Cloud** [other]: See how Energy & Utilities Cloud improves service and drives business agility for digital utilities.  
  Mentioned as "Energy"  
  https://www.salesforce.com/energy-utilities/cloud/
- **Digital Insurance Solutions** [other]: With Salesforce's digital insurance solutions, you can harmonize core processes, unify customer data, and deploy new insurance products quickly.  
  Mentioned as "Insurance"  
  https://www.salesforce.com/financial-services/digital-insurance-software/
- **Public Sector Solutions** [other]: Deploy faster, innovate faster, and increase government case worker productivity with public sector software and solutions from Salesforce.  
  Mentioned as "Public Sector"  
  https://www.salesforce.com/government/solutions/
- **Financial Services: Best Financial Services CRM** [other]: Get business results faster with Salesforce designed specifically for Financial Services.  
  Mentioned as "Financial Services Cloud (now Agentforce Financial Services)"  
  https://www.salesforce.com/financial-services/cloud/
- **Health Cloud Industry Solutions by Salesforce** [other]: Learn how Health Cloud seamlessly connects systems and organizes data in a meaningful way to scale 1-to-1 engagement with every stakeholder.  
  Mentioned as "Health Cloud (now Agentforce Health)"  
  https://www.salesforce.com/healthcare/cloud/
- **New Salesforce Omnistudio: Faster, Native, Low-Code** [other]: Build guided digital experiences with the all-new Omnistudio on Salesforce Core. Enjoy faster activation, native LWC tools, and better runtime.  
  Mentioned as "Omnistudio standard runtime"  
  https://www.salesforce.com/industries/omnistudio/omnistudio-on-core-guide/
- **Agentforce integration for your Integration Procedures** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_omnistudio_configure_integration_procedure_on_agentforce.htm&release=256&type=5
- **LearnExperienceCloud.com** [other]: no description available  
  Mentioned as "Lightning Web Runtime (LWR)"  
  https://www.learnexperiencecloud.com/topic/a081U00000OhIqgQAF/lightning-web-runtime-lwr
- **LearnExperienceCloud.com** [other]: no description available  
  Mentioned as "Experience Cloud"  
  https://www.learnexperiencecloud.com/
- **Create Faster, Lighter Experience Cloud Sites with Omnistudio Components and LWR** [other]: Learn how to boost site performance by running Omnistudio components on Lightning Web Runtime (LWR) for a faster, lighter customer experience without changing your design.  
  Mentioned as "Deploying changes"  
  https://developer.salesforce.com/blogs/2026/01/create-faster-lighter-experience-cloud-sites-with-omnistudio-components-and-lwr
- **the core differences between the managed package runtime and the standard runtime** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.os_differences_between_omnistudio_and_omnistudio_for_vlocity.htm&type=5
- **OMA** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.os_migrate_install_oma.htm&type=5
- **command-line interface (CLI)** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  https://developer.salesforce.com/tools/salesforcecli
- **enabling Omnistudio Metadata API support** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.os_enable_omnistudio_metadata_api_support.htm&type=5
- **Salesforce Omnistudio: Build Guided Digital Experiences** [other]: Rapidly build industry-specific digital experiences. Create guided workflows and pixel-perfect UIs with Salesforce Omnistudio’s low-code tools.  
  Mentioned as "Omnistudio"  
  https://www.salesforce.com/products/omnistudio/overview/
- **Omnistudio Development Essentials for Digital Solutions** [trailhead]: Master Omnistudio to create seamless omnichannel experiences. Explore standard designers, best practices, and essential developer tools to enhance your skills.  
  Mentioned as "Omnistudio Development Essentials"  
  https://trailhead.salesforce.com/content/learn/modules/omnistudio-development-essentials
- **Omniscript Fundamentals: Simplify User Processes** [trailhead]: Discover how to use Omniscripts for efficient user interactions. Learn to integrate data, enhance UI, and create guided experiences effectively.  
  Mentioned as "Omnistudio Omniscript Fundamentals"  
  https://trailhead.salesforce.com/content/learn/modules/omnistudio-omniscript-fundamentals
- **YouTube: Build Low-Code Digital Experiences with All-New OmniStudio | TDX Bengaluru** [other]: no description available  
  https://youtu.be/x7kwVCFpKyM?si=k7V_kyNXkUpMv1q4
- **Migrate Omnistudio Components from Vlocity Industries Managed Packages and Custom Data Model to Omnistudio Standard Runtime** [docs]: no description available  
  https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.os_migrate_omnistudio_custom_objects_to_standard_objects.htm&type=5&_ga=2.251188102.1251986665.1771926946-585422095.1771404282

## Suggested tasks
- [ ] Install the OMA plugin in a sandbox and run `sf omnistudio:migration:assess -a` to produce a baseline migration-blocker report (S)
- [ ] Record a baseline of automated regression and smoke tests for key Omnistudio flows, to compare against after migration (M)
- [ ] Inventory Angular-based Omniscripts and custom-object mappings that OMA can't migrate automatically, and estimate the manual rework (M)

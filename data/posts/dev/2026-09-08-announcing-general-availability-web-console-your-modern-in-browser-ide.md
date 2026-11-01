---
title: "Announcing General Availability: Web Console \u2013 Your Modern In-Browser IDE"
url: https://developer.salesforce.com/blogs/2026/09/announcing-general-availability-web-console-your-modern-in-browser-ide
source: dev
date: 2026-09-08
authors: ["Karen Fidelak"]
topics: ["DevOps & Tooling", "Apex & Code", "LWC / UI"]
---

- Web Console, a browser-based IDE built on VS Code for the Web and the Salesforce Extensions for VS Code, is now Generally Available as a modern alternative to Developer Console.
- It supports Apex editing, Anonymous Apex, SOQL with SOQL Builder and query plans, Apex tests, trace flags and debug logs, and Org Browser metadata retrieval.
- Unlike Developer Console, it adds Lightning Web Component viewing and editing; Certinia Apex Log Analyzer log analysis is listed as coming soon.
- Apex editing is read-only in production orgs and allowed inline in sandboxes and other non-production orgs.
- It is enabled by default for users with admin permissions and launches from the Setup gear menu with no local install.

## Links
- **Salesforce Extensions for Visual Studio Code** [docs]: Salesforce Extensions for Visual Studio Code are a set of open-source extensions that come with rich tools for developing on the Salesforce platform.  
  https://developer.salesforce.com/docs/platform/sfvscode-extensions/overview
- **Get Started** [docs]: Agentforce Vibes IDE is a web-based integrated development environment that delivers the full power and flexibility of Visual Studio Code in your brow  
  Mentioned as "Agentforce Vibes IDE"  
  https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-overview.html
- **Org Browser** [docs]: The Org Browser makes it easy to retrieve your org metadata sources by listing org metadata types and their corresponding components. Click the cloud  
  Mentioned as "Learn More"  
  https://developer.salesforce.com/docs/platform/webconsole/guide/org-browser.html
- **Use Anonymous Apex** [docs]: ::include{src="../../../shared/apex-anonymous.md"}  
  Mentioned as "Learn More"  
  https://developer.salesforce.com/docs/platform/webconsole/guide/webconsole-apex-anonymous.html
- **Query Records** [docs]: You can use Salesforce Object Query Language (SOQL) queries in Web Console to query the records in your org. To query records:  
  Mentioned as "Learn More"  
  https://developer.salesforce.com/docs/platform/webconsole/guide/query-records.html
- **Test Apex Code** [docs]: Use the Apex extension to run Apex tests and verify your code  
  Mentioned as "Learn More"  
  https://developer.salesforce.com/docs/platform/webconsole/guide/webconsole-apex-tests.html
- **Debug Apex Code** [docs]: Use debug logs to track events that occur in your org. To generate debug logs in Web Console,  
  Mentioned as "Learn More"  
  https://developer.salesforce.com/docs/platform/webconsole/guide/debug-your-code.html
- **Launch Web Console** [docs]: When Web Console is enabled, you can open it from these locations on the Setup page.  
  Mentioned as "How to launch Web Console"  
  https://developer.salesforce.com/docs/platform/webconsole/guide/launch.html
- **Issues · forcedotcom/web-console-feedback · GitHub** [repo]: This repository is used to collect feedback for the Web Console beta. - Issues · forcedotcom/web-console-feedback  
  Mentioned as "share your feedback"  
  https://github.com/forcedotcom/web-console-feedback/issues
- **Get Started** [docs]: Web Console is a modern, lightweight, browser-based IDE serving as the editing suite that scales across ecosystems. This chapter explains:  
  Mentioned as "Web Console documentation"  
  https://developer.salesforce.com/docs/platform/webconsole/guide
- **GitHub - forcedotcom/web-console-feedback: This repository is used to collect feedback for the Web Console beta. · GitHub** [repo]: This repository is used to collect feedback for the Web Console beta. - forcedotcom/web-console-feedback  
  Mentioned as "Feedback/Issues repository on GitHub"  
  https://github.com/forcedotcom/web-console-feedback

## Suggested tasks
- [ ] Open Web Console in a sandbox and edit an Apex class and an LWC via Org Browser, then run its tests (S)
- [ ] Reproduce a failing Apex job in a sandbox and debug it in Web Console using trace flags, debug logs, and tests (M)
- [ ] Check the Web Console and Developer Console settings in Setup for your orgs and decide whether to keep the legacy Developer Console enabled (S)

---
title: "Flow Test Mode (Beta): The Future of Flow Testing"
url: https://admin.salesforce.com/blog/2026/flow-test-mode-beta-the-future-of-flow-testing
source: admin
date: 2026-09-29
authors: ["Adam White"]
topics: ["Flow & Automation", "Agentforce & AI", "DevOps & Tooling"]
---

- Flow Test Mode (Beta) is a dedicated testing workspace that replaces the Debug button in Flow Builder and merges debugging and automated testing into one experience.
- Debug runs can be saved as named manual test scenarios that keep the triggering record, input variables, and mocked outputs, so they can be reused or shared with coworkers.
- Saved scenarios can be turned into permanent regression tests by adding assertions (expected results), using Apex test classes to create isolated test data for each test.
- New inputs include static 15- or 18-character record IDs (useful for Cases, Campaign Members, Content Document, and Setup objects) and primitive collections, which can be entered as a semicolon-delimited list.
- Subflow and action outputs can be mocked, for example to fake an HTTP callout response, and flow coverage visualization on the canvas arrives in Winter '27 along with Agentforce for Flow Headless test generation.

## Links
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260928102907/Screenshot-2026-09-28-at-12.28.48%E2%80%AFPM.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260928102907/Screenshot-2026-09-28-at-12.28.48%E2%80%AFPM.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103030/Screenshot-2026-09-28-at-12.30.11%E2%80%AFPM.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103030/Screenshot-2026-09-28-at-12.30.11%E2%80%AFPM.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103141/Screenshot-2026-09-28-at-12.31.29%E2%80%AFPM.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103141/Screenshot-2026-09-28-at-12.31.29%E2%80%AFPM.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103244/Screenshot-2026-09-28-at-12.32.33%E2%80%AFPM.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103244/Screenshot-2026-09-28-at-12.32.33%E2%80%AFPM.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103354/Screenshot-2026-09-28-at-12.33.39%E2%80%AFPM.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103354/Screenshot-2026-09-28-at-12.33.39%E2%80%AFPM.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103505/Screenshot-2026-09-28-at-12.34.49%E2%80%AFPM.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260928103505/Screenshot-2026-09-28-at-12.34.49%E2%80%AFPM.png
- **Test Flows in a Dedicated Test Mode (Beta)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_flow_test_mode.htm&release=264&type=5
- **Testing Your Flow in Test Mode (Beta)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.automate_flow_test_mode.htm&type=5
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Enable Flow Test Mode (Beta) in a sandbox or scratch org and save two manual test scenarios on a record-triggered flow (S)
- [ ] Convert a saved scenario into an automated regression test with assertions and mock an HTTP callout action, then check whether deployment to another org requires the beta setting (M)

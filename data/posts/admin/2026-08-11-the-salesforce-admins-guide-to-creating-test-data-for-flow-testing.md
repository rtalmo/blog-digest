---
title: "The Salesforce Admin\u2019s Guide to Creating Test Data for Flow Testing"
url: https://admin.salesforce.com/blog/2026/the-salesforce-admins-guide-to-creating-test-data-for-flow-testing
source: admin
date: 2026-08-11
authors: ["Joshua Birk"]
topics: ["Flow & Automation", "Apex & Code", "DevOps & Tooling"]
---

- Dedicated, system-generated test data makes flow tests predictable, because tests no longer depend on records that may be deleted, changed, or missing in another org.
- Flow tests that rely on org data break when the chosen record changes or when a flow version moves to a data-dry sandbox or Developer Edition org.
- Test data comes from an Apex class that is annotated @isTest, has a method annotated @testSetup, and is declared global so the flow testing UI can see it.
- The data is ephemeral: it exists only while the test runs and is never written to the data layer, so you can create, update, and delete records freely.
- Admins should give developers a brief on the flow's purpose, the trigger record and fields, related records, and the data volume needed (for example 500 records instead of 5), then attach the class on the flow test's Test Setup tab.

## Links
- **Test for Outcomes with Flow Testing Upgrades - Salesforce Admins** [other]: Every admin knows the rule: Test in a sandbox before it breaks in production. Or as the saying goes, measure twice and cut once. When new or updated solutions are released to your users, you want to be able to predict that they will have the experience you intend. This also goes for ensuring that […]  
  Mentioned as "Test for Outcomes with Flow Testing Upgrades"  
  https://admin.salesforce.com/blog/2026/test-for-outcomes-with-flow-testing-upgrades
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Write a global @isTest class with a @testSetup method for a simple flow, deploy it to a scratch org, and attach it on the flow test's Test Setup tab (M)
- [ ] Audit existing flow tests for dependence on specific org records and list candidates to move to dedicated Apex test data (S)

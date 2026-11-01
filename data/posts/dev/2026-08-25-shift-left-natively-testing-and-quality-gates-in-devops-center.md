---
title: "Shift Left Natively: Testing and Quality Gates in DevOps Center"
url: https://developer.salesforce.com/blogs/2026/08/shift-left-natively-testing-and-quality-gates-in-devops-center
source: dev
date: 2026-08-25
authors: ["spadmannagari"]
topics: ["DevOps & Tooling", "Agentforce & AI", "Apex & Code"]
---

- DevOps Center Testing is now generally available natively in DevOps Center, acting as a single source of truth for test definitions and results across tools.
- Built-in test providers are Apex unit tests (with code coverage tracking), Flow tests, and Salesforce Code Analyzer v5 (PMD, ESLint, Flow Scanner), while partner tools from ACCELQ, Copado, Panaya, Provar, Quality Clouds, and Tricentis are coming soon.
- Automated quality gates can be set per pipeline stage, such as on pull request creation or pre-promotion, and they block promotion on failing Apex tests, coverage below threshold, or critical Code Analyzer findings, with feedback shown in the work item.
- Four new Agentforce Vibes skills (dx-devops-test-pipeline-configure, dx-devops-test-suite-assignments-configure, dx-devops-test-suite-run, dx-devops-test-failures-analyze) support configuring gates, assigning and running suites, and analyzing failures, and can optionally create a fix WorkItem on explicit request.
- To get started, open the new Tests tab in your DevOps Center pipeline, add providers, and define gate thresholds, then trigger the same gates from existing CI tools via the Salesforce CLI or REST API.

## Links
- **DevOps Center Testing** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.devops_center_testing_setup.htm&type=5
- **Salesforce Code Analyzer** [docs]: Ensure your code adheres to best practices, helping you identify problems earlier while you develop. Code Analyzer brings together multiple code scann  
  Mentioned as "Code Analyzer"  
  https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/overview
- **Automated quality gates** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.devops_testing_ensure_high_quality_work_items_with_quality_gate_rules.htm&type=5
- **Flow Scanner** [docs]: Use the Flow Scanner engine to audit Salesforce Flows and report detailed information about security issues.  
  https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/engine-flow.html
- **reference documentation** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.devops_center_testing_setup.htm&language=en_US&type=5
- **Release Notes** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_deployment_devops_center_testing.htm&release=262&type=5
- **Object References** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_list.htm
- **CI/CD Integration** [docs]: We recommend that you integrate Salesforce Code Analyzer into your Continuous Integration/Continuous Development (CI/CD) process to scan your code reg  
  Mentioned as "Code Analyzer"  
  https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/ci-cd.html
- **Google Search** [trailhead]: no description available  
  Mentioned as "DevOps Center Trailblazer Group"  
  https://www.google.com/search?q=https://trailhead.salesforce.com/trailblazer-community/groups/0F94V000000HeS0SAK
- **DX Inspector Documentation** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.devops_center_dx_inspector.htm&language=en_US&type=5
- **Salesforce CLI Command Reference** [docs]: This command reference contains information about the Salesforce CLI commands and their flags. Use these commands to build Agentforce agents, manage S  
  Mentioned as "Salesforce CLI Reference"  
  https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference.html
- **Next Generation DevOps Center documentation** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.next_generation_devops_center.htm&type=5

## Suggested tasks
- [ ] Enable DevOps Center Testing in a sandbox pipeline, add Apex, Flow, and Code Analyzer providers, and configure a pre-promotion quality gate (M)
- [ ] Try the dx-devops-test-failures-analyze Agentforce Vibes skill against a deliberately failing Apex test and review its fix suggestions (S)
- [ ] Prototype triggering DevOps Center test gates from an existing CI script via the CLI or REST API (L)

---
title: "Salesforce\u306e\u30b9\u30ad\u30eb\u3092\u6d3b\u7528\u3057\u3066\u3001Claude Code\u3067\u672c\u756a\u904b\u7528\u53ef\u80fd\u306a\u30a2\u30d7\u30ea\u3092\u69cb\u7bc9\u3059\u308b"
url: https://developer.salesforce.com/blogs/2026/08/build-production-ready-apps-in-claude-code-with-salesforce-skills-jp
source: dev
date: 2026-08-12
authors: ["Akshata Sawant"]
topics: ["Agentforce & AI", "Apex & Code", "LWC / UI"]
---

- Salesforce Skills for Claude Code (installed via `npx skills add forcedotcom/sf-skills`) generate Apex, LWC, and test classes from natural-language prompts, with output checked by Salesforce Code Analyzer and at least 75% test coverage.
- Claude maps the prompt to skills such as generating-apex, generating-apex-test, generating-lwc-components, and debugging-apex-logs, then applies guardrails like no SOQL in loops, enforced sharing rules, and mandatory test generation.
- Before reporting completion, the skills run `sf code-analyzer` and `sf apex run test`; the tutorial's Account creation form (LWC + AccountCreationController + test class) reached 100% coverage, including bulk tests with 251+ records.
- The sf-skills library has 60+ skills, covering batch jobs (Database.Stateful), service-selector-domain layers, screen flows (generating-flow), Apex log analysis, OmniStudio, Trigger Actions Framework, and Custom REST resources; it is open source and can be forked for team conventions.
- Caveats: it is distributed through GitHub rather than as a Salesforce npm package, the 'skills' npm package is not owned by Salesforce, and output must be reviewed and tested in a sandbox (field API names, FLS, sharing) before production deployment.

## Links
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "Salesforceスキル"  
  https://github.com/forcedotcom/sf-skills
- **Salesforce Code Analyzer** [docs]: Ensure your code adheres to best practices, helping you identify problems earlier while you develop. Code Analyzer brings together multiple code scann  
  https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/overview
- **Claude Code** [other]: A shared Claude Code session on claude.ai/code  
  https://claude.ai/code
- **Salesforce CLI** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  https://developer.salesforce.com/tools/salesforcecli
- **skills - npm** [other]: The open agent skills ecosystem. Latest version: 1.7.4, last published: 13 days ago. Start using skills in your project by running `npm i skills`. There are 131 other projects in the npm registry using skills.  
  Mentioned as "「skills」npmパッケージ"  
  https://www.npmjs.com/package/skills
- **sf-skills/CONTRIBUTING.md at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/CONTRIBUTING.md at main · forcedotcom/sf-skills  
  Mentioned as "コントリビューションガイド"  
  https://github.com/forcedotcom/sf-skills/blob/main/CONTRIBUTING.md
- **Claude Code for VS Code - Visual Studio Marketplace** [other]: Extension for Visual Studio Code - Claude Code for VS Code: Harness the power of Claude Code without leaving your IDE  
  Mentioned as "Claude CodeのVS Code拡張機能"  
  https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code
- **Feed** [other]: no description available  
  Mentioned as "Salesforceの開発者コミュニティ"  
  https://developer.salesforce.com/forums
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "Salesforceスキルライブラリ（英語）"  
  http://github.com/forcedotcom/sf-skills
- **Claude Code** [other]: A shared Claude Code session on claude.ai/code  
  Mentioned as "Claude Codeドキュメント"  
  http://claude.ai/code
- **Overview - Claude Code Docs** [other]: Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools. Available in your terminal, IDE, desktop app, and browser.  
  Mentioned as "Claude Code入門ガイド"  
  http://docs.anthropic.com/claude-code
- **Agent Skills Overview - Agent Skills** [other]: A standardized way to give AI agents new capabilities and expertise.  
  Mentioned as "Agent Skillsの仕様（英語）"  
  http://agentskills.io
- **Salesforce CLIリファレンス** [other]: Salesforce CLI is a command-line interface for Salesforce DX features.  
  http://developer.salesforce.com/tools/salesforcecli
- **Trailhead：Lightning Web コンポーネントの基本** [trailhead]: no description available  
  http://trailhead.salesforce.com/content/learn/modules/lightning-web-components-basics
- **Trailhead：Apexテスト** [trailhead]: no description available  
  http://trailhead.salesforce.com/content/learn/modules/apex_testing

## Suggested tasks
- [ ] Install forcedotcom/sf-skills in a scratch org project and build the accountCreationForm tutorial end to end (S)
- [ ] Prompt Claude to generate a Database.Stateful batch job with tests, then run Code Analyzer manually and compare findings (M)
- [ ] Fork sf-skills and add a custom skill or template encoding your team's naming and trigger framework conventions (L)

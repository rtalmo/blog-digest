---
title: "AI\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u7528\u306e\u610f\u601d\u6c7a\u5b9a\u30b9\u30b3\u30a2\u30ea\u30f3\u30b0\u30b9\u30ad\u30eb\u3092\u4f5c\u6210\u3059\u308b"
url: https://developer.salesforce.com/blogs/2026/09/build-a-decision-scoring-skill-for-any-agent-jp
source: dev
date: 2026-09-16
authors: ["Dave Norris"]
topics: ["Agentforce & AI", "DevOps & Tooling", "Apex & Code"]
---

- The post introduces /decide, a structured skill in the open-source Salesforce Ada Agent Skills repo. It makes a coding agent run a technical decision through a pipeline and write the result to disk as an Architectural Decision Record (ADR).
- The pipeline has five steps: gather context, list solution options from official docs, define evaluation criteria, assess risk per option (Low/Medium/High with citations), and compute a decision score. The human reviews and confirms after the options, criteria and risk steps, and the agent pauses at each of these checkpoints.
- Scoring is rule-based. Risk levels map to fixed values (Low=85, Medium=55, High=25), which are weighted by Well-Architected pillars: Reliability 20%, Stability 20%, Operational Excellence 20%, Resource Optimization 15%, Cost Optimization 15%, Fairness 10%. The highest score is always the recommendation.
- Design patterns include a folder layout with CLAUDE.md global rules plus SKILL.md pipeline logic, separate format template files per step, and a roughly 350-line scoring file loaded only at the final step. Critical rules are repeated in at least two files so they survive long conversations.
- Facts are checked against docs via an MCP server. The authors built a custom salesforce-content server with keyword and vector search, the repo includes a Context7 fallback, and the skill falls back to web search or model knowledge if no MCP is available. The skill is demonstrated with Claude Code, and the repo has templates for Gemini and Codex CLI.

## Links
- **GitHub - deejay-hub/salesforce-ada-agent-skills: Salesforce agent skills to learn and make decisions · GitHub** [repo]: Salesforce agent skills to learn and make decisions - GitHub - deejay-hub/salesforce-ada-agent-skills: Salesforce agent skills to learn and make decisions  
  Mentioned as "Salesforce Ada Agent Skills"  
  https://github.com/deejay-hub/salesforce-ada-agent-skills
- **GitHub - deejay-hub/salesforce-ada-content-mcp-server: A Salesforce content MCP with official documentation sources · GitHub** [repo]: A Salesforce content MCP with official documentation sources - deejay-hub/salesforce-ada-content-mcp-server  
  Mentioned as "salesforce-content"  
  https://github.com/deejay-hub/salesforce-ada-content-mcp-server
- **Well-Architectedフレームワーク** [other]: no description available  
  https://www.youtube.com/watch?v=Gt9tMPl_Kf8&list=PLn15mOuXqGJWg9YJNnAqO-Rv-dN3MngoT
- **Architectural Decision Records · GitHub** [repo]: Architectural Decision Records has 20 repositories available. Follow their code on GitHub.  
  Mentioned as "Architectural Decision Record (ADR)"  
  https://github.com/adr
- **Codebase Explorer** [other]: no description available  
  Mentioned as "Anthropicのスキル公式ドキュメント"  
  https://code.claude.com/docs/en/skills.md
- **Anthropicのスキル活用に関するベストプラクティス** [other]: no description available  
  https://code.claude.com/docs/en/best-practices.md
- **Homepage** [other]: Discover trusted architecture guidance from Salesforce. Explore the Well-Architected Framework, decision guides, and resources built for Salesforce architects.  
  Mentioned as "Salesforce Well-Architected"  
  https://architect.salesforce.com/docs/architect/well-architected/guide/overview
- **The Next Chapter of the Well-Architected Framework** [other]: no description available  
  https://www.youtube.com/watch?v=Gt9tMPl_Kf8

## Suggested tasks
- [ ] Clone salesforce-ada-agent-skills and run /decide on a real packaging or architecture question in Claude Code (S)
- [ ] Review the generated ADR and risk matrix, then adjust the Well-Architected pillar weights in CLAUDE.md to match your team's priorities (M)
- [ ] Build a custom decision-scoring skill for your own domain, with format templates, a fixed risk-to-score mapping and human review checkpoints (L)

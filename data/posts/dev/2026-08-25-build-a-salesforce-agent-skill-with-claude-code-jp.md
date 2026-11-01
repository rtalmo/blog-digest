---
title: "Claude Code\u3067Salesforce\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u30b9\u30ad\u30eb\u3092\u69cb\u7bc9\u3059\u308b"
url: https://developer.salesforce.com/blogs/2026/08/build-a-salesforce-agent-skill-with-claude-code-jp
source: dev
date: 2026-08-25
authors: ["Dave Norris"]
topics: ["Agentforce & AI", "Apex & Code", "DevOps & Tooling"]
---

- Agent Skills are structured prompt packages (SKILL.md plus references/, assets/, and hooks/scripts/) that make Claude Code produce Apex that passes security review, respects governor limits, follows team frameworks, and scores well in static analysis.
- SKILL.md frontmatter uses a description with TRIGGER when / DO NOT TRIGGER when conditions so the right skill activates (for example authoring-apex vs authoring-lwc), and the body defines a fixed multi-phase workflow (Author, Validate with Code Analyzer and tests, Report) with explicit exit criteria.
- The references/ files (best-practices, design-patterns, anti-patterns, security-guide, transaction-security-policy) work best when short, one rule per section, with BAD/GOOD code pairs, reasons for failures, and positively phrased rules. The assets/ templates (service, selector, batch, queueable, transaction-security-policy) act as few-shot examples.
- Hooks such as UserPromptSubmit and PostToolUse (matcher Write|Edit) run Python validation scripts. The example preflight script checks that @salesforce/plugin-code-analyzer is installed at version 5.5.0 or later, which gives mechanical enforcement on top of instructions. Hooks are Claude Code-specific, while the skill content is portable.
- The SKILL.md format is an open spec under Apache 2.0, supported by 30+ agents (Agentforce Vibes, Cursor, VS Code, Gemini CLI, Codex, and others). The post stresses that LLM output is probabilistic, so preventive structure and detective validation are both needed. It also points to Anthropic's skill-creator skill as a starting point.

## Links
- **Build a Salesforce Agent Skill with Claude Code** [other]: Learn how to build authoring skills for consistently producing high quality code across the Salesforce ecosystem using structured workflows, code templates, and automated validators.  
  https://developer.salesforce.com/blogs/2026/05/build-a-salesforce-agent-skill-with-claude-code
- **Agent Skills Overview - Agent Skills** [other]: A standardized way to give AI agents new capabilities and expertise.  
  Mentioned as "エージェントスキル"  
  https://agentskills.io/home
- **Agent Skills Overview - Agent Skills** [other]: A standardized way to give AI agents new capabilities and expertise.  
  Mentioned as "SKILL.md"  
  http://skill.md
- **Prompting best practices - Claude Platform Docs** [other]: Comprehensive guide to prompt engineering techniques for Claude's latest models, covering clarity, examples, XML structuring, thinking, and agentic systems.  
  Mentioned as "ベストプラクティス"  
  https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **anti-patterns.md** [other]: no description available  
  http://anti-patterns.md
- **Homepage** [other]: Discover trusted architecture guidance from Salesforce. Explore the Well-Architected Framework, decision guides, and resources built for Salesforce architects.  
  Mentioned as "こちらのドキュメント"  
  https://architect.salesforce.com/docs/architect/well-architected-tools/guide/anti-patterns.html
- **skills/skills/skill-creator/SKILL.md at main · anthropics/skills · GitHub** [repo]: Public repository for Agent Skills. Contribute to anthropics/skills development by creating an account on GitHub.  
  Mentioned as "スキル"  
  https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "Agentforce Vibesスキルライブラリ"  
  https://github.com/forcedotcom/afv-library
- **Prompt Fundamentals: Write Effective Prompts for AI** [trailhead]: Prompt Fundamentals teaches how to write effective prompts for generative AI, starting with the six components that make prompts clear and actionable  
  Mentioned as "プロンプトの基本事項"  
  https://trailhead.salesforce.com/content/learn/modules/prompt-fundamentals
- **Advanced Techniques for Prompt Engineering** [trailhead]: Elevate your prompt engineering skills through advanced techniques like few-shot and chain-of-thought prompting. Start creating effective prompts now.  
  Mentioned as "プロンプトエンジニアリングのテクニック"  
  https://trailhead.salesforce.com/content/learn/modules/prompt-engineering-techniques
- **Extend Claude with skills - Claude Code Docs** [other]: Create, manage, and share skills to extend Claude's capabilities in Claude Code. Includes custom commands and bundled skills.  
  Mentioned as "Claude Code"  
  https://docs.anthropic.com/en/docs/claude-code/skills

## Suggested tasks
- [ ] Scaffold a minimal authoring-apex skill (SKILL.md with TRIGGER/DO NOT TRIGGER description plus one anti-patterns.md reference) in a scratch project and test Claude Code on a trigger handler (M)
- [ ] Add the preflight hook script that checks the Salesforce Code Analyzer plugin version, and confirm it warns when the plugin is missing or outdated (S)
- [ ] Audit your repo's Apex conventions (sharing, USER_MODE, trigger framework) and turn them into BAD/GOOD reference sections and service/selector templates (L)

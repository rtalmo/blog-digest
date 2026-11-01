---
title: "Skills in Agentforce Vibes: A Guide for Admins"
url: https://admin.salesforce.com/blog/2026/skills-in-agentforce-vibes-a-guide-for-admins
source: admin
date: 2026-09-22
authors: ["Joshua Birk"]
topics: ["Agentforce & AI", "Security & Admin", "DevOps & Tooling"]
---

- Agentforce Vibes opens from Setup as a cloud-hosted Visual Studio Code instance configured for your org, so admins work in a virtualized environment rather than directly in the org.
- Skills are packaged instructions for distinct tasks, such as creating objects, adding fields or validation rules, and deploying metadata. Vibes picks the matching skill from the verbs in your prompt, which avoids guessing and wasting tokens.
- A library of Salesforce and Trailblazer Community skills now comes pre-installed. Find them under Toolkit > Skills, add more with + Add Skill, or get them from the GitHub repo forcedotcom/afv-library.
- Plan mode shows a plan for approval before Vibes executes anything. All changes stay on Vibes' own filesystem until you explicitly ask it to deploy, so you should try it in a Developer Edition, scratch org or sandbox.
- In the author's example, a prompt to build a report of active system administrators led to a deploy that initially failed because Vibes guessed the wrong report type. It then retried with other APIs, and the author warns that technical errors such as access tokens may appear along the way.

## Links
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260921085226/Screenshot-2026-09-21-at-10.51.27%E2%80%AFAM.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260921085226/Screenshot-2026-09-21-at-10.51.27%E2%80%AFAM.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260921085536/Screenshot-2026-09-21-at-10.55.25%E2%80%AFAM.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260921085536/Screenshot-2026-09-21-at-10.55.25%E2%80%AFAM.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260921090135/Screenshot-2026-09-21-at-11.01.22%E2%80%AFAM.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260921090135/Screenshot-2026-09-21-at-11.01.22%E2%80%AFAM.png
- **Leverage AI for Effective Development with Agentforce Vibes** [trailhead]: Explore how to utilize AI to enhance your development process with Agentforce Vibes. Discover key features like execution modes and prompting techniques for better  
  Mentioned as "Agentforce Vibes Basics"  
  https://trailhead.salesforce.com/content/learn/modules/agentforce-vibes-basics
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "forcedotcom/afv-library"  
  https://github.com/forcedotcom/afv-library
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] In a sandbox or scratch org, open Agentforce Vibes, set up a Standard project, and use Plan mode to create and deploy a report from a prompt (S)
- [ ] Browse the pre-installed skills in Toolkit > Skills and the forcedotcom/afv-library repo, then try a permission set or record-triggered flow skill in a sandbox (M)

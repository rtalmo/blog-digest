---
title: "Bring CRM Conversations Into Slack With Salesforce Channels and Slackbot"
url: https://admin.salesforce.com/blog/2026/bring-crm-conversations-into-slack-with-salesforce-channels-and-slackbot
source: admin
date: 2026-08-25
authors: ["Piyusha Pilania"]
topics: ["Security & Admin", "Agentforce & AI", "Integration & APIs"]
---

- Salesforce channels create a dedicated Slack channel for a Salesforce record (Accounts, Opportunities, Cases, Campaigns, or custom objects), so conversations stay tied to CRM data.
- Setup is in Setup > Slack Channels for Records: enable Show Slack Button on Selected Objects, pick objects (Accounts, Opportunities and Cases are suggested starting points), and add them via Add Objects if needed.
- Admins then add the Slack component to Lightning record pages in Lightning App Builder and activate the page as Org Default, App Default, or by App, Record Type, or Profile.
- Default channel preferences, set from the Slack organization's settings, cover channel name, channel privacy, and which related lists show in the channel.
- Slackbot can summarize a record (e.g. 'Catch me up on the Acme account'), create or update Salesforce records, and answer questions from Salesforce data and Slack conversations.

## Links
- **Your Step-by-Step Guide to Connecting Salesforce and Slack - Salesforce Admins** [other]: It was so fun working with Mike Reynolds on an episode of Slack School, where we showed how easy it is to connect Salesforce and Slack. I, of course, played the role of Salesforce Admin. 😉 And Mike, the Slack admin. Slack is a conversational interface, the place where your employees work and collaborate. Salesforce […]  
  Mentioned as "step-by-step guide"  
  https://admin.salesforce.com/blog/2025/your-step-by-step-guide-to-connecting-salesforce-and-slack
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083024/Step-1.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083024/Step-1.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083212/Step-2.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083212/Step-2.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083319/Step-3.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083319/Step-3.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083539/Step-4.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083539/Step-4.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083725/Step-4-1.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083725/Step-4-1.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083843/Step-5.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083843/Step-5.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083949/Step-5.5.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824083949/Step-5.5.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824084103/Step-6.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824084103/Step-6.png
- **Salesforce Channels: Enhance Collaboration and Data Flow** [trailhead]: Discover how to set up Salesforce channels for real-time collaboration across teams. Improve customer engagement and streamline workflows in Salesforce and Slack.  
  Mentioned as "Salesforce Channels"  
  https://trailhead.salesforce.com/content/learn/modules/salesforce-channels
- **Unlock the Power of Slackbot for Enhanced Productivity** [trailhead]: Discover how to leverage Slackbot as your personal AI agent for work. Learn to interact effectively and boost your productivity through smart prompting  
  Mentioned as "Slackbot: Quick Look"  
  https://trailhead.salesforce.com/content/learn/modules/slackbot-quick-look
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Enable Salesforce channels for Account in a sandbox, add the Slack component to the Account record page, and create a test record channel (S)
- [ ] Draft a channel naming convention and pilot plan for Accounts, Opportunities and Cases, and try Slackbot record summaries and updates in the pilot channels (M)

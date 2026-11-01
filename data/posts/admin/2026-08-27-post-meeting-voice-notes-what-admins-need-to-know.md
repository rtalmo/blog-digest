---
title: "Post-Meeting Voice Notes: What Admins Need to Know"
url: https://admin.salesforce.com/blog/2026/post-meeting-voice-notes-what-admins-need-to-know
source: admin
date: 2026-08-27
authors: ["Daivat Dholakia"]
topics: ["Agentforce & AI", "Security & Admin", "Flow & Automation"]
---

- Post-Meeting Voice Notes lets reps record a single-user spoken debrief in the Salesforce mobile app when a live meeting wasn't transcribed, for example when the customer declined recording or the rep forgot to start it.
- It is enabled as part of the In-Person Meeting Assistant, and because only the logged-in rep speaks, no verbal consent workflow is needed.
- Privacy matches the In-Person Meeting Assistant: audio is processed on-device and never leaves it, only the text transcript syncs, and transcripts are wiped on logout.
- It uses the existing Conversation Intelligence permission sets, so no permission changes are needed. Transcripts feed call summaries and next steps, keyword insights, Flow invocable actions and Prompt Builder follow-up email templates.
- Requirements and caveats: users must be on the New Seller Experience (Sales Cloud Mobile), devices must have an NPU (capable iPhones, iPads or Android devices), and a network connection is required to sync because offline use is not supported at GA.

## Links
- **Turn Conversations Into Actionable CRM Data With the In-Person Meeting Assistant - Salesforce Admins** [other]: Admins: Transform in-person meetings into trusted CRM data with the Mobile Meeting Assistant's secure, on-device AI transcription.  
  Mentioned as "In-Person Meeting Assistant"  
  https://admin.salesforce.com/blog/2026/turn-conversations-into-data-with-the-in-person-meeting-assistant
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824090616/VoiceNotesDisclaimer.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824090616/VoiceNotesDisclaimer.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260824090719/Transcribed-Text.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260824090719/Transcribed-Text.png
- **New Seller Experience (Sales Cloud Mobile)** [docs]: no description available  
  https://help.salesforce.com/s/articleView?language=en_US&id=sales.sales_mobile_app.htm&type=5
- **Capture Post-Meeting Insights with Voice Notes** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.salesforce_app_post_meeting_notes.htm&type=5
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Audit Conversation Intelligence permission sets, New Seller Experience assignment and NPU device compatibility for reps before enabling voice notes (M)
- [ ] Draft rep guidance on when to use the In-Person Meeting Assistant versus Post-Meeting Voice Notes, including the network sync requirement (S)

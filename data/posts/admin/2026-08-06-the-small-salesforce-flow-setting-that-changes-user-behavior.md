---
title: "The Small Salesforce Flow Setting That Changes User Behavior"
url: https://admin.salesforce.com/blog/2026/the-small-salesforce-flow-setting-that-changes-user-behavior
source: admin
date: 2026-08-06
authors: ["Neil Foglio"]
topics: ["Flow & Automation", "Security & Admin"]
---

- Pairing a boolean toggle (e.g., tgl_update_client) with the Read Only and Disabled settings on Screen Flow components lets you capture user intent, not just the final field values.
- A boolean formula resource that inverts the toggle (True when the toggle is off) is applied to the Read Only or Disabled setting on every field, so fields stay locked until the user turns the toggle on.
- The toggle's own Disabled setting is set to tgl_update_client.value, so once it's on it can't be switched off. This stops users from thinking they need to uncheck it to 'lock in' their edits.
- Read Only fields still allow highlighting and copying text, while Disabled fields are grayed out and block copy-paste. Static booleans can permanently lock fields such as name and date of birth.
- Caveat: toggles aren't always initialized to False, so a skipped screen or conditional visibility can leave the value null, and writing null to a checkbox field errors. Set it to False in an Assignment element before the record update.

## Links
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260729104430/Flow-Image-1.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260729104430/Flow-Image-1.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260729104909/Flow-Image-2.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260729104909/Flow-Image-2.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105013/Flow-Image-3.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105013/Flow-Image-3.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105129/Flow-Image-4.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105129/Flow-Image-4.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105233/Flow-Image-5-1.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105233/Flow-Image-5-1.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105320/Flow-Image-6.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105320/Flow-Image-6.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105438/Flow-Image-7.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105438/Flow-Image-7.png
- **https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105533/Flow-Image-8.png** [other]: no description available  
  https://d3nqfz2gm66yqg.cloudfront.net/images/20260729105533/Flow-Image-8.png
- **The Salesforce Admin's Guide to Choosing the Right Flow - Salesforce Admins** [other]: All Salesforce Admins face the question: What flow should I use in this situation? Learn which flows to use when and tips to help you choose.  
  Mentioned as "The Salesforce Admin’s Guide to Choosing the Right Flow"  
  https://admin.salesforce.com/blog/2026/the-salesforce-admins-guide-to-choosing-the-right-flow
- **Create Interactive Automations** [trailhead]: Learn how to create automation that guides and interacts with users. Dive into Screen Flows module on Salesforce Trailhead.  
  Mentioned as "Screen Flows"  
  https://trailhead.salesforce.com/content/learn/modules/screen-flows
- **The Ultimate Guide to Flow Best Practices and Standards - Salesforce Admins** [other]: Learn Flow best practices, ‘gotchas,’ and design tips for admins to make your flows scale with your organization.  
  Mentioned as "The Ultimate Guide to Flow Best Practices and Standards"  
  https://admin.salesforce.com/blog/2021/the-ultimate-guide-to-flow-best-practices-and-standards
- **Spring '26: Design Screen Flows With Intent Using Styling Overrides - Salesforce Admins** [other]: The Salesforce Spring ’26 release introduces Screen & Component Styling Overrides in Flow Builder. More control over look & feel for admins.  
  Mentioned as "Spring ’26: Design Screen Flows With Intent Using Styling Overrides"  
  https://admin.salesforce.com/blog/2026/spring-26-design-screen-flows-with-intent-using-styling-overrides
- **Restrict User Input on Screen Components with the Disabled and Read Only Fields** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_flow_builder_disabled_and_read_only_fields.htm&release=250&type=5
- **Flow Variable Considerations** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.flow_considerations_feature_variable.htm&type=5
- **Basics of User Experience Design** [trailhead]: Explore user experience design with a deep dive into UX principles, design process, and frameworks. Improve app and website usability.  
  Mentioned as "User Experience Basics"  
  https://trailhead.salesforce.com/content/learn/modules/ux-basics/learn-about-user-experience-design
- **Usability Testing Can Offer Quick Website Fixes** [other]: Usability testing is a user research tool that can help you figure out quick ways to fix your website experience for your users.  
  Mentioned as "How Usability Testing Led to 5 Instant UX Fixes"  
  https://www.salesforce.com/blog/usability-testing-design/
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Build a scratch-org Screen Flow with a toggle, an inverse formula resource, and Read Only/Disabled fields, then write the toggle to a checkbox field (S)
- [ ] Audit existing Screen Flows that pre-populate record data and add 'section changed' toggles, with an Assignment element to default them to False (M)

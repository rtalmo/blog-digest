---
title: "From Inbox Requests to a User Management System"
url: https://admin.salesforce.com/blog/2026/from-inbox-requests-to-a-user-management-system-podcast
source: admin
date: 2026-08-06
authors: ["mgerholdt@salesforce.com"]
topics: ["Flow & Automation", "Security & Admin", "Community & Events"]
---

- Michelle Wolfe, a Platform Engineer, built a no-code, Flow-powered user management system that handles requests, approvals, user creation, permissions, communications and onboarding.
- The problem was onboarding classes of 80+ new hires, where managers emailed individual members of a three-person admin team who then created each account by hand.
- A screen flow now collects the request details and creates a case, which centralizes intake and lets the team track productivity, due dates and workload.
- After the manager approves, an autolaunched flow validates the data, creates the alias and username, and sets the profile and permissions from the request. A second autolaunched flow closes the case and sends a confirmation email and a welcome email.
- She replaced Add Multiple Users and bulk upload because Add Multiple Users doesn't support custom fields, so records failed her validation rules, and bulk upload broke on typos.

## Links
- **Salesforce Admins Podcast - Podcast - Apple Podcasts** [other]: Listen to Mike Gerholdt's Salesforce Admins Podcast podcast on Apple Podcasts.  
  Mentioned as "subscribe"  
  https://itunes.apple.com/us/podcast/buttonclick-admin-podcast/id914088438?mt=2&ign-mpt=uo%3D4
- **Admins** [other]: Admins  
  Mentioned as "Salesforce Admins on the Trailhead Store"  
  https://trailheadstoreamer.com/category/salesforce-admins
- **Group Detail** [other]: no description available  
  Mentioned as "Admin Trailblazers Community Group"  
  https://sforce.co/4977GHH
- **Mike Gerholdt (@mikegerholdt) • Threads, Say more** [other]: 238 Followers • 280 Threads • Salesforce Admin Evangelist I live with @Gunnarthebasenji 🐶 These inspiring words are my own. See the latest conversations with @mikegerholdt.  
  Mentioned as "Mike on Threads"  
  https://www.threads.net/@mikegerholdt/
- **Salesforce Admins** [other]: This is a site for Salesforce Admins to stay up to date on product updates, events, tools, and resources. Learn more about automation, app building, analytics.  
  https://admin.salesforce.com

## Suggested tasks
- [ ] Prototype a screen flow in a scratch org that captures new-user request details (including a custom Team Name field) and creates a Case (M)
- [ ] Build an approval-triggered autolaunched flow that creates a User with a generated alias and username and assigns a profile and permission set (L)

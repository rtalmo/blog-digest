---
title: "Salesforce Microfrontends: Embed Web Apps in Lightning"
url: https://developer.salesforce.com/blogs/2026/10/salesforce-microfrontends-embed-web-apps-in-lightning
source: dev
date: 2026-10-13
authors: ["SANGEETA PATNAIK"]
topics: ["LWC / UI", "Integration & APIs"]
---

- Salesforce Microfrontends (via UI Embedding) embed React, Angular, Vue and other web apps inside Lightning alongside LWC.
- Architecture: a custom LWC host renders `lightning-ui-embedding`; the guest app runs in a sandboxed iframe and exchanges context, data and events with the host.
- Example use: an Account page keeps native LWC for record details and actions, and shows an embedded React app for a specialized experience.
- Post walks through a simple host/guest build and places Microfrontends within the wider Multi-Framework story.

## Links
- **Get Started** [docs]: Use the Lightning Web Components (LWC) framework to build custom user interfaces, web and mobile apps, and digital experiences on the Salesforce Platf  
  Mentioned as "Lightning Web Components (LWC)"  
  https://developer.salesforce.com/docs/platform/lwc/guide
- **Get Started with UI Embedding** [docs]: Embed an existing external web app directly in Salesforce so your users work in one place instead of switching to a separate tab or window. With UI Em  
  Mentioned as "UI Embedding setup documentation"  
  https://developer.salesforce.com/docs/platform/microfrontend/guide/get-started.html
- **Exchange Data Between the Page and an Embedded App** [docs]: Move data both ways between Salesforce and an embedded app so the two stay in sync. The Salesforce host sends the embedded app its current data and UI  
  https://developer.salesforce.com/docs/platform/microfrontend/guide/exchange-data.html
- **Embed an Internally Hosted App as a UI Bundle (Beta)** [docs]: Host your app inside Salesforce infrastructure instead of on your own domain, and embed it with the same  
  Mentioned as "current framework support documentation"  
  https://developer.salesforce.com/docs/platform/microfrontend/guide/internal-ui-bundles.html?utm_source=chatgpt.com
- **UI Embedding Recipes** [docs]: Explore working sample apps that embed a web app in Salesforce with  
  Mentioned as "UI Embedding recipes"  
  https://developer.salesforce.com/docs/platform/microfrontend/guide/recipes.html
- **Build with React on Salesforce: Multi-Framework Is Now GA** [other]: Ship production-ready React apps natively on Salesforce — with authentication, security, and governance built in. Here’s what changed in Multi-Framework since beta, and how to migrate.  
  Mentioned as "Salesforce Multi-Framework"  
  https://developer.salesforce.com/blogs/2026/07/build-with-react-on-salesforce-multi-framework-is-now-ga
- **Build Embedded Apps in the Framework You Prefer** [docs]: UI Embedding works with externally hosted apps regardless of the front-end framework they're built in. You can reuse an app you already have instead o  
  Mentioned as "Explore framework support"  
  https://developer.salesforce.com/docs/platform/microfrontend/guide/framework-support.html
- **Style an Embedded App to Match Salesforce** [docs]: Keep an embedded app visually consistent with the surrounding Salesforce experience. Salesforce passes styling values to the embedded app as CSS custo  
  Mentioned as "Style an embedded application"  
  https://developer.salesforce.com/docs/platform/microfrontend/guide/style-embedded-app.html
- **Embed an Internally Hosted App as a UI Bundle (Beta)** [docs]: Host your app inside Salesforce infrastructure instead of on your own domain, and embed it with the same  
  Mentioned as "Embed an internally hosted UI Bundle"  
  https://developer.salesforce.com/docs/platform/microfrontend/guide/internal-ui-bundles.html
- **Salesforce Multi-Framework** [docs]: Use Salesforce Multi-Framework to build apps using industry-standard UI frameworks, such as React and Angular, that run on the Salesforce Platform wit  
  Mentioned as "Learn more about Salesforce Multi-Framework"  
  https://developer.salesforce.com/docs/platform/multiframework/overview
- **GitHub - trailheadapps/multiframework-recipes: A collection of easy-to-digest code examples for React, Angular, and microfrontends on Salesforce Platform · GitHub** [repo]: A collection of easy-to-digest code examples for React, Angular, and microfrontends on Salesforce Platform - trailheadapps/multiframework-recipes  
  Mentioned as "Explore Multi-Framework Recipes on GitHub"  
  https://github.com/trailheadapps/multiframework-recipes

## Suggested tasks
- [ ] Build a host LWC + embedded React guest from the multiframework-recipes repo (M)
- [ ] Evaluate which existing web app in my repo could be embedded instead of rebuilt as LWC (S)

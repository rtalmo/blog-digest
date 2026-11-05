---
title: "Runtime Behavior Anti-Patterns in Lightning Web Components"
url: https://developer.salesforce.com/blogs/2026/11/runtime-behavior-anti-patterns-in-lightning-web-components
source: dev
date: 2026-11-04
authors: ["Tim Dionne"]
topics: ["LWC / UI", "Apex & Code", "Security & Admin"]
---

- This is the third post in the LWC anti-patterns series. It covers DOM access, async timing, lifecycle hooks, performance, and base component usage.
- Don't use document.querySelector, innerHTML, or #id selectors, because LWC rewrites ids and scopes shadow DOM. Use this.template.querySelector or lwc:ref (this.refs.x) instead, and use lightning-formatted-rich-text for trusted rich HTML.
- Don't use setTimeout to wait for data or re-renders. Use async/await for data, and use renderedCallback() with a guard flag for DOM work, since it fires after every render.
- Don't read @api properties or touch the DOM in constructor() or connectedCallback(), because values and children aren't ready yet. Use connectedCallback, @wire, or renderedCallback, and avoid this.template.children.
- Under Lightning Web Security, clone Apex/LDS data once on arrival before looping, and prefer plain objects and arrays over Set/Map for large collections.

## Links
- **Security Anti-Patterns in Lightning Web Components** [other]: Learn how the platform’s three independent security layers operate, how Lightning Web Security (LWS) distorts common APIs, and how to avoid the cross-namespace mistakes that lead to silent data failures.  
  Mentioned as "first post"  
  https://developer.salesforce.com/blogs/2026/06/security-anti-patterns-in-lightning-web-components
- **second post** [other]: no description available  
  https://developer.salesforce.com/blogs/2026/08/data-and-communication-anti-patterns-in-lightning-web-components
- **DOM access** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-dom.html
- **component lifecycle** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-lifecycle-hooks.html
- **shadow DOM** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-dom-intro.html
- **document.querySelector()** [other]: no description available  
  https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector
- **lwc:ref** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-components-dom-work.html
- **no-inner-html** [repo]: no description available  
  https://github.com/salesforce/eslint-plugin-lwc/blob/master/docs/rules/no-inner-html.md
- **renderedCallback()** [docs]: The  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-lifecycle-hooks-rendered.html
- **this.template.children** [other]: no description available  
  https://developer.mozilla.org/en-US/docs/Web/API/Element/children
- **Set** [other]: no description available  
  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
- **Map** [other]: no description available  
  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map
- **lightning/platformShowToastEvent** [docs]: no description available  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-platform-show-toast-event/documentation
- **lightning/toast** [docs]: no description available  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-toast/documentation
- **lightning/modal** [docs]: no description available  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-modal/documentation
- **lightning/datatable** [docs]: no description available  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-datatable/documentation
- **styling hooks** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-custom-properties.html
- **lightning-button** [docs]: no description available  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-button/documentation
- **rendering multiple templates** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-render.html
- **Component Reference** [docs]: no description available  
  https://developer.salesforce.com/docs/component-library
- **@salesforce/client/formFactor** [docs]: no description available  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-client-form-factor.html
- **GitHub - salesforce/eslint-plugin-lwc: Official ESLint rules for LWC · GitHub** [repo]: Official ESLint rules for LWC. Contribute to salesforce/eslint-plugin-lwc development by creating an account on GitHub.  
  Mentioned as "@lwc/eslint-plugin-lwc rules"  
  https://github.com/salesforce/eslint-plugin-lwc

## Suggested tasks
- [ ] Run the LWC ESLint plugin (including no-inner-html) over your repo and fix flagged document.querySelector, innerHTML, and #id selector usage (S)
- [ ] Replace ShowToastEvent with lightning/toast in components used on LWR or Experience Cloud sites and verify toasts appear in a scratch org (M)
- [ ] Audit components for setTimeout-based waits and constructor/connectedCallback DOM or @api access, and refactor to renderedCallback, async/await, or @wire (M)

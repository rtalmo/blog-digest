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
- **Data and Communication Anti-Patterns in Lightning Web Components** [other]: Learn how the wire service, public properties, and events move data through Lightning web components, and how to avoid reactivity and communication mistakes that cause stale UI, lost events, and hard-to-reproduce state bugs.  
  Mentioned as "second post"  
  https://developer.salesforce.com/blogs/2026/08/data-and-communication-anti-patterns-in-lightning-web-components
- **Shadow DOM** [docs]: Shadow DOM is a standard that encapsulates the internal document object model (DOM) structure of a web component. Encapsulating the DOM gives develope  
  Mentioned as "DOM access"  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-dom.html
- **Lifecycle Hooks** [docs]: A  
  Mentioned as "component lifecycle"  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-lifecycle-hooks.html
- **Work with the DOM** [docs]: The Document Object Model (DOM) represents the HTML page so that you can work with its content, structure, and style using JavaScript or the standard  
  Mentioned as "shadow DOM"  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-dom-intro.html
- **Document: querySelector() method - Web APIs** [other]: The Document method querySelector() returns the first Element within the document that matches the specified CSS selector, or group of CSS selectors. If no matches are found, null is returned.  
  Mentioned as "document.querySelector()"  
  https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector
- **Access Elements the Component Owns** [docs]: To access elements rendered by a component with standard DOM APIs, use  
  Mentioned as "lwc:ref"  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-components-dom-work.html
- **eslint-plugin-lwc/docs/rules/no-inner-html.md at master · salesforce/eslint-plugin-lwc · GitHub** [repo]: Official ESLint rules for LWC. Contribute to salesforce/eslint-plugin-lwc development by creating an account on GitHub.  
  Mentioned as "no-inner-html"  
  https://github.com/salesforce/eslint-plugin-lwc/blob/master/docs/rules/no-inner-html.md
- **renderedCallback()** [docs]: The  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-lifecycle-hooks-rendered.html
- **Element: children property - Web APIs** [other]: The read-only children property returns a live HTMLCollection which contains all of the child elements of the element upon which it was called.  
  Mentioned as "this.template.children"  
  https://developer.mozilla.org/en-US/docs/Web/API/Element/children
- **Set - JavaScript** [other]: The Set object lets you store unique values of any type, whether primitive values or object references.  
  Mentioned as "Set"  
  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
- **Map - JavaScript** [other]: The Map object holds key-value pairs and remembers the original insertion order of the keys. Any value (both objects and primitive values) may be used as either a key or a value.  
  Mentioned as "Map"  
  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map
- **Platform Show Toast Event** [docs]: Salesforce Developer Website  
  Mentioned as "lightning/platformShowToastEvent"  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-platform-show-toast-event/documentation
- **Toast** [docs]: Salesforce Developer Website  
  Mentioned as "lightning/toast"  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-toast/documentation
- **Modal** [docs]: Salesforce Developer Website  
  Mentioned as "lightning/modal"  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-modal/documentation
- **Datatable** [docs]: Salesforce Developer Website  
  Mentioned as "lightning/datatable"  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-datatable/documentation
- **SLDS Styling Hooks** [docs]: Salesforce Lightning Design System (SLDS) styling hooks make it easy to customize component styling and express your brand. Use styling hooks to acces  
  Mentioned as "styling hooks"  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-custom-properties.html
- **Button** [docs]: Salesforce Developer Website  
  Mentioned as "lightning-button"  
  https://developer.salesforce.com/docs/component-library/bundle/lightning-button/documentation
- **Render Multiple Templates** [docs]: You may want to render a component with more than one look and feel, but not want to mix the HTML in one file. For example, one version of the compone  
  Mentioned as "rendering multiple templates"  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-render.html
- **Get Started** [docs]: The Component Reference documents the full set of base components for both the Lightning Web Components (LWC) and Aura programming models. Base compon  
  Mentioned as "Component Reference"  
  https://developer.salesforce.com/docs/component-library
- **Client Form Factor** [docs]: To access the form factor of the hardware the browser is running on, import the  
  Mentioned as "@salesforce/client/formFactor"  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-client-form-factor.html
- **GitHub - salesforce/eslint-plugin-lwc: Official ESLint rules for LWC · GitHub** [repo]: Official ESLint rules for LWC. Contribute to salesforce/eslint-plugin-lwc development by creating an account on GitHub.  
  Mentioned as "@lwc/eslint-plugin-lwc rules"  
  https://github.com/salesforce/eslint-plugin-lwc

## Suggested tasks
- [ ] Run the LWC ESLint plugin (including no-inner-html) over your repo and fix flagged document.querySelector, innerHTML, and #id selector usage (S)
- [ ] Replace ShowToastEvent with lightning/toast in components used on LWR or Experience Cloud sites and verify toasts appear in a scratch org (M)
- [ ] Audit components for setTimeout-based waits and constructor/connectedCallback DOM or @api access, and refactor to renderedCallback, async/await, or @wire (M)

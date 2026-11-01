---
title: "Salesforce Microfrontend (UI Embedding) \u3067 React \u30a2\u30d7\u30ea\u306e\u57cb\u3081\u8fbc\u307f\u3092\u8a66\u3059"
url: https://developer.salesforce.com/blogs/2026/09/salesforce-microfrontend-ui-embedding-jp
source: dev
date: 2026-09-17
authors: ["Hiroyuki Inaba"]
topics: ["LWC / UI", "Integration & APIs", "Releases"]
---

- Salesforce Microfrontend (UI Embedding), currently Beta and tested on a Winter '27 Preview scratch org (API 68.0), lets a React UI Bundle from Multi-Framework be embedded in Lightning Experience record pages via `lightning-ui-embedding`.
- Embedding needs a thin wrapper LWC that passes the app's `*.salesforce.app` URL as `src` to `<lightning-ui-embedding>`. The app URL must also be registered under Setup > Trusted URLs with the `frame-src` CSP context enabled.
- `recordId` did not arrive in `state.props`, which was empty on the record page. The reliable route was custom events on the `sf-embedding` channel: the LWC dispatches `caseRecordId` and the app dispatches `requestRecordId`.
- Waiting only for `sf-embedding.component.ready` dropped the event, because the app registers its listener after `createViewSDK()` resolves. A handshake fixed this: the app registers its listener and then requests the recordId, and the LWC replies on either `ready` or the request.
- Two other pitfalls: keep `src` as a fixed base URL after mount, and avoid `100vh`/`min-h-screen` inside the iframe, which makes the auto-resizer grow the iframe without end. The post suggests using `height:auto` instead, and the LWC height is a design attribute clamped to 420–720px.

## Links
- **Get Started with UI Embedding** [docs]: Embed an existing external web app directly in Salesforce so your users work in one place instead of switching to a separate tab or window. With UI Em  
  Mentioned as "Salesforce Microfrontend: Get Started"  
  https://developer.salesforce.com/docs/platform/microfrontend/guide/get-started.html
- **Salesforce Mult-Framework を使用した React による UI 開発** [other]: TDX 2026で発表されたSalesforce Multi-Framework（ベータ版）を使い、ReactでSalesforce UIを開発する手順を解説。Developer Editionのスクラッチ組織でシンプルなUI を作成し、取引先データを表示するまでのステップを公開します。  
  Mentioned as "Salesforce で React アプリをマルチフレームワークで動かす"  
  https://developer.salesforce.com/jpblogs/2026/04/salesforce-mult-framework-react-jp
- **Exchange Data Between the Page and an Embedded App** [docs]: Move data both ways between Salesforce and an embedded app so the two stay in sync. The Salesforce host sends the embedded app its current data and UI  
  Mentioned as "Exchange Data ガイド"  
  https://developer.salesforce.com/docs/platform/microfrontend/guide/exchange-data.html

## Suggested tasks
- [ ] Build a wrapper LWC with lightning-ui-embedding in a Winter '27 scratch org and embed a React UI Bundle on a Case page (M)
- [ ] Implement the recordId handshake (caseRecordId / requestRecordId custom events) and test for dropped events on page navigation (S)
- [ ] Audit the React app's CSS for 100vh/min-h-screen usage that would trigger the iframe auto-resize loop (S)

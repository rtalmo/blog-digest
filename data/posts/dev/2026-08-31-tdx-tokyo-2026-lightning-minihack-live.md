---
title: "\u3010TDX Tokyo 2026\u3011Lightning MiniHack Live \u30d5\u30a1\u30a4\u30ca\u30ea\u30b9\u30c8\u5ea7\u8ac7\u4f1a: \u521d\u4ee3\u30c1\u30e3\u30f3\u30d4\u30aa\u30f3\u3068\u6311\u6226\u8005\u305f\u3061\u304c\u8a9e\u308b\u300c\u6700\u901f\u300d\u306e\u821e\u53f0\u88cf\u3068 AI \u6642\u4ee3\u306e\u5b9f\u88c5\u529b"
url: https://developer.salesforce.com/blogs/2026/08/tdx-tokyo-2026-lightning-minihack-live
source: dev
date: 2026-08-31
authors: ["odasho"]
topics: ["Community & Events", "Flow & Automation", "Agentforce & AI"]
---

- Lightning MiniHack Live, a speed-and-accuracy Salesforce implementation contest, was held for the first time at TDX Tokyo 2026 (Agentforce World Tour Tokyo) in June 2026, with four finalists in a 1 vs 1 tournament.
- The final challenge was a validation requirement that could be built with a validation rule, Flow, or Apex trigger, with the exception logic "skip the budget-overrun check when the urgent flag is on".
- Finalists chose different implementations: Apex trigger (Suzuki, to cut UI click time and make a single save round-trip), Flow (Omuro, for stable timing), a custom error (Hasegawa, for certainty), and Flow with hotkeys and formulas (Madani, the champion).
- Champion Madani won by practicing with video timing analysis, using Flow while doing other work during load times, and delegating tasks to AI (including Agentforce Grid) while working on non-AI tasks in parallel.
- The finalists agreed that implementation skill in the AI era means precisely describing requirements, being able to converse with customers, and reviewing and correcting AI output, since AI often produces plausible but wrong results.

## Links

## Suggested tasks
- [ ] Time yourself building the same validation (urgent flag skips budget check) as a validation rule, a record-triggered Flow, and an Apex trigger in a scratch org, then compare speed and reliability (M)
- [ ] Try Agentforce Grid in a Developer Edition org to see which implementation steps you can delegate to AI while working on others in parallel (M)

---
title: "Improve Enterprise RAG Accuracy in Data 360"
url: https://developer.salesforce.com/blogs/2026/09/improve-enterprise-rag-accuracy-in-data-360
source: dev
date: 2026-09-02
authors: ["Barnali Patnaik"]
topics: ["Data Cloud", "Agentforce & AI"]
---

- Enterprise RAG failures compound across four stages (content processing, content splitting, search, generation), and the post argues accuracy is mostly a configuration problem rather than an LLM problem.
- Intelligent Parsing routes each page to text or vision-model extraction, raising OHR-Bench v2 end-to-end accuracy from 65% to 84.4% (charts/diagrams 57.9% to 76.3%, reading order 11.9% to 67.1%) and keeping tables intact; it is listed as expected November 2026.
- Enriched Indexing, toggled in Search Index Setup, generates metadata and anticipated-question chunks for each chunk, adding +2.4 pp (84.4% to 86.8%) on OHR-Bench v2.
- Tuning chunk size (512 to 2048 tokens), top-k (10 to 30) and a domain-tuned generation prompt took WixQA knowledge-base accuracy from 62.5% to 92.5% with no code changes.
- Knowledge Graph (GA expected November 2026) and auto-tuning (found the optimal configuration in three iterations in early testing) are coming; the post recommends building a 20-50 question golden dataset to evaluate your own pipeline in Intelligent Context.

## Links
- **RAG** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_rag_overview.htm&type=5
- **OHR-Bench** [other]: no description available  
  https://arxiv.org/pdf/2412.02592
- **enriched indexing.** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_search_index_enriched_index.htm&type=5
- **[2505.08643] WixQA: A Multi-Dataset Benchmark for Enterprise Retrieval-Augmented Generation** [other]: Abstract page for arXiv paper 2505.08643: WixQA: A Multi-Dataset Benchmark for Enterprise Retrieval-Augmented Generation  
  Mentioned as "WixQA"  
  https://arxiv.org/abs/2505.08643
- **Intelligent Context** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_intelligent_context.htm&type=5
- **Trailblazer Community** [trailhead]: no description available  
  https://trailhead.salesforce.com/trailbl%20%20%20%20%20%20azer-community/groups/0F94S000000kQixSAE
- **Data 360 Documentation** [docs]: no description available  
  https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_data_cloud.htm&type=5
- **[2501.00321] OCRBench v2: An Improved Benchmark for Evaluating Large Multimodal Models on Visual Text Localization and Reasoning** [other]: Abstract page for arXiv paper 2501.00321: OCRBench v2: An Improved Benchmark for Evaluating Large Multimodal Models on Visual Text Localization and Reasoning  
  Mentioned as "OHR-Bench v2"  
  https://arxiv.org/abs/2501.00321
- **[2407.01523] MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations** [other]: Abstract page for arXiv paper 2407.01523: MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations  
  Mentioned as "MMLongBench-Doc"  
  https://arxiv.org/abs/2407.01523
- **[2605.05253] EnterpriseRAG-Bench: A RAG Benchmark for Company Internal Knowledge** [other]: Abstract page for arXiv paper 2605.05253: EnterpriseRAG-Bench: A RAG Benchmark for Company Internal Knowledge  
  Mentioned as "Enterprise RAG Bench"  
  https://arxiv.org/abs/2605.05253
- **Data 360 on Trailhead** [trailhead]: no description available  
  https://trailhead.salesforce.com/data-cloud-trail
- **AI - Artificial Intelligence Resources, Events and Tips** [other]: Artificial intelligence moves fast. Keep up with the latest AI trends and learn more about how to make AI work for your organization.  
  Mentioned as "Salesforce AI Blog"  
  https://www.salesforce.com/blog/ai/

## Suggested tasks
- [ ] Build a 20-50 question golden Q&A set from your own docs and run a baseline evaluation in Data 360 Intelligent Context (M)
- [ ] In a Data 360 sandbox, test chunk size 2048, top-k 30 and a domain-tuned generation prompt against the baseline (M)
- [ ] Enable Enriched Indexing on a search index and compare retrieval for differently-worded queries (S)

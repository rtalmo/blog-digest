---
title: "Pro-Code Chunking of Data 360 Search Indexes for Agentforce"
url: https://developer.salesforce.com/blogs/2026/09/pro-code-chunking-of-data-360-search-indexes-for-agentforce
source: dev
date: 2026-09-24
authors: ["spatlori"]
topics: ["Data Cloud", "Agentforce & AI", "Apex & Code"]
---

- Native Data 360 chunking (section-aware, semantic passage extraction) works for clean content but breaks down on dense tables, multispeaker transcripts, and PII-laden documents in complex PDFs.
- Data 360 Code Extension functions let you deploy sandboxed, stateless Python chunking scripts inside the Salesforce trust boundary, authored locally with the Data Custom Code SDK, deployed via Salesforce CLI or UI, and wired in at search index creation.
- For tables, a structure-aware function detects markdown, grid and HTML tables, keeps each as a unit, and repeats column headers in every sub-chunk when a table exceeds the size limit; in the example, the agent went from being unable to interpret '42.1 35.8 22.4...' to correctly reporting 87.9% YoY growth and a 28.1% operating margin for AI & Automation.
- For multispeaker dialogue, a sliding window (WINDOW_SIZE=6 turns, STRIDE=3, MAX_CHUNK_CHARS=1500) preserves speaker attribution and timestamps and keeps questions co-located with answers, fixing native chunks where speakers and topics were mashed together.
- Caveat from the author: the sample code relies on regex heuristics, covers only happy-path inputs, and can produce false positives and negatives, so production use needs hardening; the post also covers a third use case, masking exposed PII, though the provided text is truncated before it.

## Links
- **chunking** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_search_index_grounding.htm&type=5
- **Use Custom Functions in Data 360** [docs]: Create custom chunking functions for the search index builder by using the Salesforce CLI, the code extension plugin, and the Data Custom Code Python  
  Mentioned as "Data 360 Code Extension functions"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/use-custom-function.html
- **Mechanisms** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_search_index_supported_chunking_strategies.htm&type=5
- **GitHub - forcedotcom/datacloud-customcode-python-sdk · GitHub** [repo]: Contribute to forcedotcom/datacloud-customcode-python-sdk development by creating an account on GitHub.  
  Mentioned as "Data Custom Code SDK"  
  http://github.com/forcedotcom/datacloud-customcode-python-sdk
- **Write and Validate a Custom Chunking Function** [docs]: In code extension, function runs are specific to search index chunking, where your code controls how content is split before vectorization and indexin  
  Mentioned as "developer documentation"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/write-custom-chunking-function.html
- **Data 360 Code Extension: structure-aware chunking function that preserves table integrity for Agentforce search indexes. Companion code for the Salesforce Developers blog "Pro-Code Chunking of Data 360 Search Indexes for Agentforce." · GitHub** [repo]: Data 360 Code Extension: structure-aware chunking function that preserves table integrity for Agentforce search indexes. Companion code for the Salesforce Developers blog "Pro-Code Chunking of Data 360 Search Indexes for Agentforce." - datacloud_code_extension_table_aware_chunking.py  
  Mentioned as "Sample code"  
  https://gist.github.com/Samaritha/abfaffb55f416922933caebe3da3dbd5
- **Data 360 Code Extension: windowed sliding-dialogue chunking function that preserves speaker turns in multispeaker transcripts. Companion code for the Salesforce Developers blog "Pro-Code Chunking of Data 360 Search Indexes for Agentforce." · GitHub** [repo]: Data 360 Code Extension: windowed sliding-dialogue chunking function that preserves speaker turns in multispeaker transcripts. Companion code for the Salesforce Developers blog "Pro-Code Chunking of Data 360 Search Indexes for Agentforce." - datacloud_code_extension_multispeaker_dialogue_chunking.py  
  Mentioned as "Sample code"  
  https://gist.github.com/Samaritha/dff3dc671eaffd62def9d952dd8b6ff2
- **Data 360 Code Extension: regex-based PII and regulated-identifier masking function applied before chunking for vector indexing. Companion code for the Salesforce Developers blog "Pro-Code Chunking of Data 360 Search Indexes for Agentforce." · GitHub** [repo]: Data 360 Code Extension: regex-based PII and regulated-identifier masking function applied before chunking for vector indexing. Companion code for the Salesforce Developers blog "Pro-Code Chunking of Data 360 Search Indexes for Agentforce." - datacloud_code_extension_pii_masking_chunking.py  
  Mentioned as "Sample code"  
  https://gist.github.com/Samaritha/a4a5d2ce427471608b222ae266d9269e
- **Extend Data 360 with Code Extension YouTube playlist** [other]: no description available  
  https://www.youtube.com/playlist?list=PLACV3VmGs318

## Suggested tasks
- [ ] Build a header-preserving table chunker with the Data Custom Code SDK and test it locally on a sample multi-page PDF (M)
- [ ] Deploy a Code Extension chunking function to a scratch/dev org and compare its chunks against native ADL chunks using vector_search queries (L)
- [ ] Audit existing Data 360 search indexes for documents with tables or transcripts that native chunking likely fragments (S)

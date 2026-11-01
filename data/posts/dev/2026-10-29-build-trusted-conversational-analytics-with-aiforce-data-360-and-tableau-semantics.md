---
title: "Build Trusted Conversational Analytics with AIforce, Data 360, and Tableau Semantics"
url: https://developer.salesforce.com/blogs/2026/10/build-trusted-conversational-analytics-with-aiforce-data-360-and-tableau-semantics
source: dev
date: 2026-10-29
authors: ["Ravindra Varshney"]
topics: ["Data Cloud", "Agentforce & AI"]
---

- A shared semantic layer gives people and agents consistent metric definitions such as revenue and pipeline, instead of logic scattered across queries and reports.
- Stack: Data 360 DLOs/DMOs for data, a Tableau semantic data model (SDM) for definitions, relationships and calculations, an Agentforce agent to answer questions, and MCP for external AI clients.
- Governance comes from Data 360 classifications, tags and policies; there are also notes on SDM calibration and optimizing the model for AI.
- Links to Semantic Layer Query API and Connect API docs, and an open-source converter (apache/ossie).

## Links
- **Data 360** [other]: Ingest, clean, and unify your customer data from Salesforce and other systems. Take action on insights with AI and automation in apps, components, and flows.  
  https://developer.salesforce.com/developer-centers/data-cloud
- **Data lake objects** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_concepts_data_cloud_objects.htm
- **Tableau Semantics Concepts** [docs]: Tableau Semantics provides business context and a single source of truth for data in Salesforce Data 360 by enabling a flexible and governed place for  
  Mentioned as "Tableau semantic data model"  
  https://developer.salesforce.com/docs/data/semantic-layer/guide/tableau-semantics-concepts.html
- **Data 360 classifications, governance tags, and policies** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=analytics.tua_governance.htm&language=en_US&type=5
- **Learn to Create Data Streams with Data 360 Technology** [trailhead]: Discover how to effectively create data streams using Data 360 technology. This educational unit guides you through connecting data and defining data lake objects  
  Mentioned as "Data streams"  
  https://trailhead.salesforce.com/content/learn/projects/explore-data-cloud-core-functionality/create-data-streams-1
- **Open Semantic Interchange (OSI) specification** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=analytics.c360_a_sl_osi_support_tab_semantics.htm&language=en_US&type=5
- **Salesforce converter** [repo]: no description available  
  https://github.com/apache/ossie/tree/main/converters/salesforce
- **Overview** [docs]: The Semantic Query API lets you query your data in Data 360 through a Semantic Data Model rather than against physical tables. You send a logical requ  
  Mentioned as "Semantic Query API"  
  https://developer.salesforce.com/docs/data/semantic-layer/guide/query-api-in-depth-overview.html
- **Salesforce CRM** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_salesforce_crm_connector.htm&type=5
- **OSI workflow** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=analytics.c360_a_sl_osi_workflow.htm&language=en_US&type=5
- **business preferences** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=analytics.c360_a_sl_biz_preferences_set.htm&type=5
- **Q&A Calibration** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=analytics.tua_data_sdm_qa_calibration.htm&language=en_US&type=5
- **Tableau Next** [docs]: The  
  Mentioned as "Tableau Next MCP"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/tableau-next.html
- **GitHub - apache/ossie: Apache Ossie, industry wide specification effort to standardize how we exchange semantic metadata across analytics, AI and BI platforms, providing a vendor neutral, single source of truth for semantic data · GitHub** [repo]: Apache Ossie, industry wide specification effort to standardize how we exchange semantic metadata across analytics, AI and BI platforms, providing a vendor neutral, single source of truth for semantic data - apache/ossie  
  Mentioned as "OSI / Apache Ossie project"  
  https://github.com/apache/ossie
- **Aggregation and Totals** [docs]: Aggregation controls how a semantic query summarizes measure values across the rows in each group. Set the aggregation for a field with  
  Mentioned as "Aggregation and totals"  
  https://developer.salesforce.com/docs/data/semantic-layer/guide/query-api-in-depth-aggregation.html
- **Authoring API Entities** [docs]: The following are the top-level entities that compose the Tableau Semantics Authoring API and their API names (in parenthesis):  
  Mentioned as "Semantic authoring API entities"  
  https://developer.salesforce.com/docs/data/semantic-layer/guide/connect-api-in-depth-entities.html
- **Business preferences best practices** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=analytics.c360_a_sl_biz_preferences_bestp.htm&language=en_US&type=5
- **Optimize and test a semantic model** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=analytics.tua_ai_optimize_model.htm&language=en_US&type=5
- **Data 360 governance considerations** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_before_you_begin_data_gov.htm&language=en_US&type=5

## Suggested tasks
- [ ] Build a small SDM over a Data 360 DMO and query it from an agent (L)
- [ ] Read the Semantic Layer Query API overview (S)

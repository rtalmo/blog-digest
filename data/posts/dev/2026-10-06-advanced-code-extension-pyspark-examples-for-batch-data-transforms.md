---
title: "Advanced Code Extension PySpark Examples for Batch Data Transforms"
url: https://developer.salesforce.com/blogs/2026/10/advanced-code-extension-pyspark-examples-for-batch-data-transforms
source: dev
date: 2026-10-06
authors: ["Mark DeLaVergne"]
topics: ["Data Cloud", "Apex & Code", "Integration & APIs"]
---

- Code Extension lets you run custom PySpark scripts against DLOs and DMOs in an isolated Spark environment in Data 360, driving the same batch transform pipeline as native transforms; batch transform support is now GA.
- The workflow uses the datacustomcode SDK's Client() with `sf data-code-extension script run` for local runs (reads the first 1000 rows by default, writes only to console) and `sf data-code-extension script deploy` (zips the project via Docker and uploads it through the Connect API) for deployed runs with no default row limit.
- Example 1 rolls up account hierarchy ARR to any depth with an iterative join loop in plain Python over DataFrames, writing to Account_Rollup__dll; it assumes an acyclic hierarchy, so cyclic parent_id__c data needs a max-depth counter to avoid hanging the job.
- Example 2 flattens a JSON-array event column into one row per event using from_json and explode_outer, with the reusable parsing helper placed in the exact-named payload/py-files/ directory and the entrypoint in payload/entrypoint.py.
- Example 3 scores leads with a bundled scikit-learn model: it ships the model zip in payload/files/, declares scikit-learn, joblib and pandas in requirements.txt, scores a small grid of categorical combinations with predict_proba and left-joins it to the leads DLO, coalescing nulls to `__unknown__`.

## Links
- **Code Extension scripts for batch data transform** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_code_extension.htm&language=en_US&type=5
- **Data 360 (Formerly Data Cloud)** [other]: Unify all customer data with Data 360 (formerly Data Cloud). Get the real-time insights you need to personalize every customer experience.  
  Mentioned as "Data 360"  
  https://www.salesforce.com/data/
- **Essential Guide to Batch Data Transforms in Data 360** [trailhead]: Unlock the potential of batch data transforms in Data 360 with this comprehensive guide. Learn how to create and manage batch data transforms effectively  
  Mentioned as "Batch Data Transforms in Data 360 Trailhead module"  
  https://trailhead.salesforce.com/content/learn/modules/batch-data-transforms-in-data-cloud-quick-look/get-started-with-batch-data-transforms-in-data-360
- **Extend Data 360 with the Power of Code: Introducing Code Extension - Salesforce** [other]: In the era of Agentforce and AI, data is the fuel behind intelligent customer experiences. Salesforce Data 360 has transformed how organizations unify and harmonize data using no-code and low-code tools. But as…  
  Mentioned as "Extend Data 360 with the Power of Code."  
  https://www.salesforce.com/blog/extend-data-360-with-the-power-of-code-introducing-code-extension/
- **Extend Data 360 with Code Extension.** [other]: no description available  
  https://www.youtube.com/playlist?list=PLACV3VmGs318
- **Explore Code Extension for Advanced Data Transformations** [trailhead]: Uncover the essentials of Code Extension in Data 360 for advanced data transformations. Learn how to build and deploy custom Python scripts effectively  
  Mentioned as "Code Extension in Data 360 Module."  
  https://trailhead.salesforce.com/content/learn/modules/code-extension-in-data-360
- **GitHub - forcedotcom/datacloud-customcode-python-sdk · GitHub** [repo]: Contribute to forcedotcom/datacloud-customcode-python-sdk development by creating an account on GitHub.  
  Mentioned as "datacustomcode SDK"  
  https://github.com/forcedotcom/datacloud-customcode-python-sdk/
- **Set Up Salesforce CLI for Code Extension** [docs]: Salesforce CLI, the Code Extension plugin, and the Data Custom Code Python SDK work together as your local toolchain for Code Extension. Use this setu  
  Mentioned as "Salesforce Command Line Interface (SF CLI) for Code Extension"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/set-up-sdk.html
- **Write and Validate Custom Script** [docs]: Write custom scripts for batch data transforms in a standard Python environment by using your preferred IDE and validate them locally against a sandbo  
  Mentioned as "docs"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/author-custom-script.html
- **Run Complex Data Transformations in Data 360 with Code Extension** [other]: Build, deploy, run, and troubleshoot complex transformations with Python and PySpark while keeping execution governed by Data 360.  
  https://developer.salesforce.com/blogs/2026/09/build-deploy-run-and-troubleshoot-complex-transformations-with-python-and-pyspark-while-keeping-execution-governed-by-data-360
- **pyspark.sql.DataFrame — PySpark 4.3.0 documentation** [other]: no description available  
  Mentioned as "DataFrames"  
  https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.html
- **datacloud-customcode-python-sdk/docs/examples/script/account_rollup at main · forcedotcom/datacloud-customcode-python-sdk · GitHub** [repo]: Contribute to forcedotcom/datacloud-customcode-python-sdk development by creating an account on GitHub.  
  Mentioned as "docs/examples/script/account_rollup"  
  https://github.com/forcedotcom/datacloud-customcode-python-sdk/tree/main/docs/examples/script/account_rollup
- **datacloud-customcode-python-sdk/docs/examples/script/json_explode at main · forcedotcom/datacloud-customcode-python-sdk · GitHub** [repo]: Contribute to forcedotcom/datacloud-customcode-python-sdk development by creating an account on GitHub.  
  Mentioned as "docs/examples/script/json_explode"  
  https://github.com/forcedotcom/datacloud-customcode-python-sdk/tree/main/docs/examples/script/json_explode
- **datacloud-customcode-python-sdk/docs/examples/script/lead_scoring/train_model.py at main · forcedotcom/datacloud-customcode-python-sdk · GitHub** [repo]: Contribute to forcedotcom/datacloud-customcode-python-sdk development by creating an account on GitHub.  
  Mentioned as "training script"  
  https://github.com/forcedotcom/datacloud-customcode-python-sdk/blob/main/docs/examples/script/lead_scoring/train_model.py
- **Make Data 360 Objects Searchable in Agentforce Coworker** [docs]: When you turn on Agentforce Coworker, your Salesforce CRM data is automatically added as a source. To also search Data Model Objects (DMOs) from Data  
  Mentioned as "Coworker"  
  https://developer.salesforce.com/docs/data/agentforce-coworker/guide/agentforce-coworker-connect-to-existing-data-sources.html
- **datacloud-customcode-python-sdk/docs/examples/script/lead_scoring at main · forcedotcom/datacloud-customcode-python-sdk · GitHub** [repo]: Contribute to forcedotcom/datacloud-customcode-python-sdk development by creating an account on GitHub.  
  Mentioned as "docs/examples/script/lead_scoring"  
  https://github.com/forcedotcom/datacloud-customcode-python-sdk/tree/main/docs/examples/script/lead_scoring
- **Considerations When Writing Code Extension** [docs]: To write code extension logic in Data 360, follow these best practices, architectural constraints, and Spark API limitations.  
  Mentioned as "Considerations When Writing Code Extensions"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/considerations-when-writing-custom-code.html
- **GitHub - forcedotcom/datacloud-customcode-python-sdk · GitHub** [repo]: Contribute to forcedotcom/datacloud-customcode-python-sdk development by creating an account on GitHub.  
  Mentioned as "forcedotcom/datacloud-customcode-python-sdk"  
  https://github.com/forcedotcom/datacloud-customcode-python-sdk
- **Client Challenge** [other]: no description available  
  Mentioned as "PyPI"  
  https://pypi.org/project/salesforce-data-customcode/
- **GitHub - salesforcecli/plugin-data-code-extension · GitHub** [repo]: Contribute to salesforcecli/plugin-data-code-extension development by creating an account on GitHub.  
  Mentioned as "salesforcecli/plugin-data-code-extension"  
  https://github.com/salesforcecli/plugin-data-code-extension
- **Code Extension in Data 360** [docs]: :::note As of October 14, 2025, Data Cloud has been rebranded to Data 360. During this transition, you may see references to Data Cloud in our applica  
  Mentioned as "Data 360 Code Extension"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/use-custom-code.html
- **Batch Data Transforms Overview** [docs]: no description available  
  https://help.salesforce.com/apex/HTViewHelpDoc?id=data.c360_a_batch_transform_overview.htm

## Suggested tasks
- [ ] Clone the datacloud-customcode-python-sdk repo and run the account_rollup example locally with `sf data-code-extension script run` (S)
- [ ] Deploy the json_explode example to a Data 360 sandbox/scratch org and compare the full-scale run against the 1000-row local run (M)
- [ ] Prototype a bundled scikit-learn scoring transform (churn or propensity) using the lead_scoring pattern and the categorical-grid join approach (L)

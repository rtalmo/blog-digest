---
title: "Run Complex Data Transformations in Data 360 with Code Extension"
url: https://developer.salesforce.com/blogs/2026/09/build-deploy-run-and-troubleshoot-complex-transformations-with-python-and-pyspark-while-keeping-execution-governed-by-data-360
source: dev
date: 2026-09-10
authors: ["Chandan Agarwal"]
topics: ["Data Cloud", "Apex & Code", "DevOps & Tooling"]
---

- Data 360 Code Extension lets developers write complex batch transformations in Python and PySpark, package them as a script, deploy to Data 360, and invoke them through a batch data transform, so governed data never leaves the platform.
- A package contains payload/config.json (sdkVersion 6.1.0, entryPoint, dataspace, explicit read/write DLO permissions) and entrypoint.py, which uses the Data Custom Code SDK to read DLOs as Spark DataFrames and write with WriteMode.MERGE; a script must read and write the same object type (DLO-to-DLO or DMO-to-DMO, not mixed).
- Local validation uses Salesforce CLI with the @salesforce/plugin-data-code-extension plugin, Python 3.11 and salesforce-data-customcode==6.1.0, running `sf data-code-extension script run` against a sandbox on up to 1,000 sampled records with console-only output; performance must be measured after deployment.
- Deploy via Setup (Code Extension page) or `sf data-code-extension script zip/deploy` with --cpu-size CPU_L/XL/2XL/4XL; the CLI has a documented limitation for DMO-to-DMO transforms, which require the UI path.
- The transform is created in the Data Transforms UI or via the Connect API (POST /ssot/data-transforms with a BYOC_SCRIPT macro), then run and monitored through the actions/run and run-history endpoints; creation can outlive the wait window, so check MktDataTransform before resubmitting.

## Links
- **Essential Guide to Batch Data Transforms in Data 360** [trailhead]: Unlock the potential of batch data transforms in Data 360 with this comprehensive guide. Learn how to create and manage batch data transforms effectively  
  Mentioned as "batch data transforms"  
  https://trailhead.salesforce.com/content/learn/modules/batch-data-transforms-in-data-cloud-quick-look/get-started-with-batch-data-transforms-in-data-360
- **Client Challenge** [other]: no description available  
  Mentioned as "Data Custom Code SDK"  
  https://pypi.org/project/salesforce-data-customcode/
- **How to Power Data 360 with Code Extension - Salesforce** [other]: Explore how to architect Data 360 to solve complex data challenges securely with Python and Code Extension.  
  Mentioned as "How to Power Data 360 with Code Extension"  
  https://www.salesforce.com/blog/power-data-360-code-extension/
- **Running Python with Data Cloud's Bring Your Own Code Architecture** [other]: Learn how Salesforce delivered a full-stack product while architecting tenant-isolated runtime environments to execute Python at enterprise scale.  
  Mentioned as "Securely Running Python with Data Cloud’s Bring Your Own Code Architecture"  
  https://engineering.salesforce.com/securely-running-python-with-data-clouds-new-bring-your-own-code-architecture/
- **Quick Start** [docs]: Set up your sandbox and local environment to run a sample batch data transform script locally against the sandbox. Deploy the script to your sandbox,  
  Mentioned as "Code Extension quick start"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/quickstart.html
- **Deploy Custom Script to Data 360 Sandbox Using CLI** [docs]: The deployment process packages your Python script, its dependencies, and Data 360 configuration, and then uploads them to Data 360.  
  Mentioned as "Deploy a Custom Script to Data 360 Sandbox by Using CLI"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/deploy-custom-script-cli.html
- **Migrate Custom Script to Production** [docs]: Use a DevOps data kit to move code extension deployments or batch data transforms created by using code extension from sandbox to production. When you  
  Mentioned as "DevOps data kit"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/migrate-code-to-prod.html
- **Invoke Code Extension by Creating a Batch Data Transform** [docs]: Invoke your code extension by creating a batch data transform that uses your deployed custom script.  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/create-batch-transform.html
- **Data 360 Connect API** [docs]: Data 360 Connect API  
  Mentioned as "Data 360 Connect REST API reference"  
  https://developer.salesforce.com/docs/data/connectapi/references/spec
- **Extend Data 360 with Code Extension** [other]: no description available  
  https://www.youtube.com/playlist?list=PLACV3VmGs318
- **Code Extension in Data 360** [docs]: :::note As of October 14, 2025, Data Cloud has been rebranded to Data 360. During this transition, you may see references to Data Cloud in our applica  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/use-custom-code.html
- **GitHub - salesforcecli/plugin-data-code-extension · GitHub** [repo]: Contribute to salesforcecli/plugin-data-code-extension development by creating an account on GitHub.  
  Mentioned as "Salesforce CLI Code Extension plugin"  
  https://github.com/salesforcecli/plugin-data-code-extension

## Suggested tasks
- [ ] Build a small Code Extension package (config.json + entrypoint.py) and run it locally against a sandbox with `sf data-code-extension script run` (M)
- [ ] Deploy the script to a sandbox with the CLI, wire it to a batch data transform, and compare run time at CPU_2XL versus another size (M)
- [ ] Write a Data 360 SQL query against DataCustomCodeLogs__dll and SOQL checks on DataCustomCode and MktDataTransform to build a troubleshooting runbook (S)

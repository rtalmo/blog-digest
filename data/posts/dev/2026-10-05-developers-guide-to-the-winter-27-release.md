---
title: "The Salesforce Developer\u2019s Guide to the Winter \u201927 Release"
url: https://developer.salesforce.com/blogs/2026/10/developers-guide-to-the-winter-27-release
source: dev
date: 2026-10-05
authors: ["Mohith Shrivastava"]
topics: ["Agentforce & AI", "DevOps & Tooling", "LWC / UI"]
---

- Winter '27 completes rollout on October 9, 2026, and the headline developer theme is the Headless Toolkit, which exposes Salesforce capabilities as APIs, MCP tools, or CLI commands for any authenticated caller, including AI agents.
- The new Salesforce Development plugin for Claude Code installs with `/plugin install salesforce-development@claude-plugins-official` and adds Salesforce skills, org context through Salesforce-hosted MCP servers, and an Apex/SOQL language server; the skills library also works with other agents via `npx skills add forcedotcom/sf-skills`.
- The plugin can now recommend specialized plugins from a catalog (dx-org-lifecycle, dx-devops, agentforce-adlc, experience-lwc/experience-react, integration), searchable with `/salesforce-development:discover plugins <task>`.
- Salesforce Multi-Framework adds Angular alongside React, with templates angularinternalapp, angularexternalapp and angularbasic. Apps are a UIBundle metadata type, and Winter '27 also adds 2GP packaging and Scale Center insights (Beta).
- The Data SDK gains extensions via defineDataExtension (called as sdk.ext.<name>), a labels extension, minimum API version, per-request headers (included in the cache key), and an i18n module. Microfrontend embedding (Beta) uses lightning-ui-embedding with props and CustomEvents, supports internal React/Angular apps on the salesforce.app domain, and needs event listeners added in renderedCallback because the event names contain dots.

## Links
- **Admin Release Countdown: Get Ready for Winter '27 - Salesforce Admins** [other]: Get ready for the Salesforce Winter ’27 Release with key dates, release readiness tips, sandbox preview deadlines, Release Notes, and resources every Salesforce Admin needs.  
  Mentioned as "Winter ’27 release"  
  https://admin.salesforce.com/blog/2026/admin-winter-27-release-countdown
- **Trust Status** [other]: no description available  
  Mentioned as "maintenance schedule"  
  https://status.salesforce.com/products/all/maintenances
- **AIforce: Salesforce AI, Wherever You Already Work** [other]: Salesforce Einstein is your end to end solution to becoming an AI-first company.  
  Mentioned as "AIforce"  
  https://www.salesforce.com/artificial-intelligence/?d=cta-body-promo-8
- **sf-skills/plugins/builder/salesforce-development at main · forcedotcom/sf-skills · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - sf-skills/plugins/builder/salesforce-development at main · forcedotcom/sf-skills  
  Mentioned as "Salesforce Development plugin"  
  https://github.com/forcedotcom/sf-skills/tree/main/plugins/builder/salesforce-development
- **GitHub - forcedotcom/sf-skills: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. · GitHub** [repo]: Salesforce's curated collection of agent skills for building applications. Optimized for Agentforce Vibes, compatible with all AI tools. - forcedotcom/sf-skills  
  Mentioned as "Salesforce skills library"  
  https://github.com/forcedotcom/sf-skills
- **Salesforce Multi-Framework Overview** [docs]: Use Salesforce Multi-Framework, a framework-agnostic runtime, to build Salesforce apps with frontend frameworks, such as React or Angular, and run the  
  Mentioned as "Salesforce Multi-Framework"  
  https://developer.salesforce.com/docs/platform/multiframework/guide
- **GitHub - trailheadapps/multiframework-recipes: A collection of easy-to-digest code examples for React, Angular, and microfrontends on Salesforce Platform · GitHub** [repo]: A collection of easy-to-digest code examples for React, Angular, and microfrontends on Salesforce Platform - trailheadapps/multiframework-recipes  
  Mentioned as "Multi-Framework Recipes sample repository"  
  https://github.com/trailheadapps/multiframework-recipes
- **Work with the Data SDK** [docs]: The Data SDK handles authentication, CSRF tokens, and base path resolution internally. To work with Data SDK, import the functions from  
  Mentioned as "Data SDK"  
  https://developer.salesforce.com/docs/platform/multiframework/guide/data-sdk-intro.html
- **Data SDK Extensions** [docs]: A Data SDK extension adds a self-contained, named API that gives the SDK instance extra capabilities. Use an extension that comes with the SDK, such a  
  Mentioned as "extension"  
  https://developer.salesforce.com/docs/platform/multiframework/guide/data-sdk-extension.html
- **Get Started** [docs]: Headless Experience Layer (HXL) is a unified experience engine and platform designed to deliver consistent, portable, and rich user experiences across  
  Mentioned as "Headless Experience Layer (HXL)"  
  https://developer.salesforce.com/docs/platform/hxl/guide/get-started.html
- **Build a Rich UI for External Agents** [docs]: Some AI agents use MCP to interact with data in your org, such as Claude Desktop, Slackbot, and ChatGPT. HXL widgets are compatible with the  
  Mentioned as "custom MCP server"  
  https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-channels.html
- **HXL Playground** [other]: Explore the Headless Experience Layer — build surface-agnostic widgets with Mosaic, preview them across Agentforce, Slack, and ChatGPT.  
  https://www.headlessexperiencelayer.com/playground/
- **Get Started** [docs]: Salesforce Hosted MCP Servers give AI agents a secure, governed way to interact with Salesforce data and automation. Using the open  
  Mentioned as "Salesforce Hosted MCP Servers"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide
- **Agentforce** [docs]: Expose Agentforce agents and Prompt Builder templates as MCP tools to allow external AI assistants to invoke Salesforce's native AI capabilities as pa  
  Mentioned as "custom MCP server"  
  https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/agentforce.html
- **AgentExchange** [other]: AgentExchange is the unified marketplace to discover, buy, and deploy trusted agents, apps, and capabilities that extend Salesforce wherever your people and agents choose to work.  
  https://agentexchange.salesforce.com/
- **API Catalog** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=platform.api_catalog.htm&language=en_US
- **The MCP Server for Marketing Cloud Engagement is Now GA** [other]: Learn how to securely connect external AI agents to Marketing Cloud Engagement and expose core capabilities like data extensions and journeys as natural language tools.  
  Mentioned as "Marketing Cloud Engagement MCP server"  
  https://developer.salesforce.com/blogs/2026/06/the-mcp-server-for-marketing-cloud-engagement-is-now-ga
- **Salesforce CLI Command Reference** [docs]: This command reference contains information about the Salesforce CLI commands and their flags. Use these commands to build Agentforce agents, manage S  
  Mentioned as "Salesforce CLI"  
  https://developer.salesforce.com/docs/atlas.en-us.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_top.htm
- **cli/releasenotes/README.md at main · forcedotcom/cli · GitHub** [repo]: Salesforce CLI - Issues and Discussions only. Contribute to forcedotcom/cli development by creating an account on GitHub.  
  Mentioned as "Salesforce CLI release notes"  
  https://github.com/forcedotcom/cli/blob/main/releasenotes/README.md
- **login()** [docs]: Logs in to the login server and starts a client session.  
  Mentioned as "SOAP API login()"  
  https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_login.htm
- **retires in Summer ’27** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=005132110&type=1&language=en_US
- **external client apps** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5&language=en_US
- **retired** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=000380623&type=1&language=en_US
- **List Available REST API Versions** [docs]: Use the Versions resource to list summary information about each REST API version currently available, including the version, label, and a link to eac  
  https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_versions.htm
- **CompositeApi** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_composite_api.htm
- **API Versioning** [docs]: | AVAILABLE API VERSIONS | | ------------------------------------ | | Available in LWC API v59.0 and later |  
  Mentioned as "LWC API version 68.0"  
  https://developer.salesforce.com/docs/platform/lwc/guide/get-started-api-versioning.html
- **Template Expressions** [docs]: Add sophisticated presentation logic to your LWC template files, and remove extra code from your component implementation. Beginning in Spring ’26, a  
  Mentioned as "template expressions"  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-components-html-expressions.html
- **Use Third-Party Web Components in LWC** [docs]: Use third-party web components in an LWC app. Third-party web components render as native web components in LWC templates. Although you can use third-  
  Mentioned as "third-party web component"  
  https://developer.salesforce.com/docs/platform/lwc/guide/create-use-third-party-components.html
- **w27-rating-stars: a framework-free web component used with lwc:external (Salesforce Winter '27 developer guide) · GitHub** [repo]: w27-rating-stars: a framework-free web component used with lwc:external (Salesforce Winter '27 developer guide) - w27RatingStars.js  
  Mentioned as "w27-rating-stars"  
  https://gist.github.com/msrivastav13/691a13d17394d5b3f42be7e4d3bf5dbf
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "Apex heap limit"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "Integration tests"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing_integration_testing.htm
- **FORMULA() (Beta)** [docs]: Use the  
  Mentioned as "FORMULA()"  
  https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_formula.htm
- **Apex Reference Guide** [docs]: Apex Reference Guide  
  Mentioned as "Database.QueryOptions"  
  https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_Database_QueryOptions.htm
- **SET OPTIONS** [docs]: Use the  
  https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_set_options.htm
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "Prevent Field Name Collisions in Managed SOQL Queries"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_manpkgs_dynamic_soql.htm
- **Apex Symbol API** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_resources_apex_symbols.htm
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "Apex cursors"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_cursors.htm
- **Test Discovery API** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_resources_testing_discovery.htm
- **apexCompileResults** [docs]: Salesforce Developer Website  
  https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_resources_recompile_invalid_apex.htm
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "API version 20.0 or later"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_version_settings_api.htm
- **Apex Developer Guide** [docs]: Apex Developer Guide  
  Mentioned as "Elastic limits"  
  https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_limits_elastic_limits.htm
- **Agent Script** [docs]: Get to know the language for building agents in Agentforce Builder. Use Agent Script to build predictable, context-aware agent workflows that don't re  
  https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html
- **Conditional Expressions** [docs]: if  
  Mentioned as "expression functions"  
  https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-expressions.html
- **Variables (System)** [docs]: Agent Script provides predefined, prepopulated system variables that you can use in your agent. To access system variables, use  
  Mentioned as "system variables"  
  https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-variables-system.html
- **connection instructions** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.agent_connection_instructions.htm&language=en_US
- **Agent Script Blocks** [docs]: A script consists of blocks where each block contains a set of properties. These properties can describe data or procedures. Agent Script contains sev  
  Mentioned as "config block"  
  https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-blocks.html
- **Multi-Agent Orchestration** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=ai.agent_multi_orch.htm&type=5&language=en_US
- **metadata types** [docs]: no description available  
  https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-metadata.html
- **GitHub - salesforce/agentscript: An open, schema-driven language for configuring agent orchestration systems · GitHub** [repo]: An open, schema-driven language for configuring agent orchestration systems - salesforce/agentscript  
  Mentioned as "Agent Script repository"  
  https://github.com/salesforce/agentscript
- **release notes** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.rn_change_log.htm&release=264&type=5
- **context precision score** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_ai_retriever_test_metrics.htm&language=en_US
- **Billing Considerations for Testing Retrievers** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=data.c360_a_ai_retriever_test_billing.htm&language=en_US
- **Write and Validate Custom Script** [docs]: Write custom scripts for batch data transforms in a standard Python environment by using your preferred IDE and validate them locally against a sandbo  
  Mentioned as "Code extension"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/author-custom-script.html
- **Read Zero-Copy Data in Code Extension** [docs]: Write code extension scripts that read a data lake object (DLO) backed by a zero-copy connector or a data model object (DMO) mapped from that DLO. Bec  
  Mentioned as "zero-copy data"  
  https://developer.salesforce.com/docs/data/data-cloud-code-ext/guide/read-zero-copy-sources.html
- **GitHub - salesforcecli/plugin-data-code-extension · GitHub** [repo]: Contribute to salesforcecli/plugin-data-code-extension development by creating an account on GitHub.  
  Mentioned as "Code Extension plugin for Salesforce CLI (Beta)"  
  https://github.com/salesforcecli/plugin-data-code-extension
- **pyspark.sql.DataFrame — PySpark 4.3.0 documentation** [other]: no description available  
  Mentioned as "PySpark DataFrame"  
  https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.html
- **pandas.DataFrame — pandas 3.1.0 documentation** [other]: no description available  
  Mentioned as "DataFrame"  
  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
- **Announcing General Availability: Web Console – Your Modern In-Browser IDE** [other]: Learn how the generally available Web Console brings a modern, browser-based IDE to Salesforce so you can edit, debug, test, and validate without leaving your org.  
  Mentioned as "Web Console"  
  https://developer.salesforce.com/blogs/2026/09/announcing-general-availability-web-console-your-modern-in-browser-ide
- **Supported Org Types** [docs]: Note that the available functionality in various orgs varies. For instance, full Apex development and feature access are available on active productio  
  Mentioned as "supported editions"  
  https://developer.salesforce.com/docs/platform/webconsole/guide/supported-orgs.html
- **Issues · forcedotcom/web-console-feedback · GitHub** [repo]: This repository is used to collect feedback for the Web Console beta. - Issues · forcedotcom/web-console-feedback  
  Mentioned as "Web Console feedback repository"  
  https://github.com/forcedotcom/web-console-feedback/issues
- **Performance-First Apex Development with ApexGuru in Salesforce DX MCP Server** [other]: Shift your performance analysis left with ApexGuru and the Salesforce DX MCP Server. Now, you can catch and fix costly Apex bottlenecks directly in your IDE before you ever hit deploy.  
  Mentioned as "ApexGuru in the Salesforce DX MCP Server"  
  https://developer.salesforce.com/blogs/2026/04/performance-first-apex-development-with-apexguru-in-salesforce-dx-mcp-server
- **Enable Geo Aware Routing** [docs]: Agentforce Vibes supports geo-aware model routing. When your Salesforce admin enables geo-aware model routing, Agentforce Vibes routes all large langu  
  Mentioned as "model endpoint closest to your Salesforce org"  
  https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-geo-aware-routing.html
- **Group Detail** [trailhead]: no description available  
  Mentioned as "Salesforce Developers Trailblazer Community"  
  https://trailhead.salesforce.com/trailblazer-community/groups/0F93A000000DJbJSAW?tab=discussion&sort=LAST_MODIFIED_DATE_DESC
- **Developer Portal** [other]: Learn how to build mobile and enterprise applications and agents on Salesforce and deliver innovative experiences using the Agentforce 360 Platform.  
  Mentioned as "Salesforce Developers"  
  https://developer.salesforce.com/
- **official release notes** [docs]: no description available  
  https://help.salesforce.com/s/articleView?id=release-notes.salesforce_release_notes.htm&release=264&type=5
- **Group Detail** [trailhead]: no description available  
  Mentioned as "Release Readiness Trailblazers Community group"  
  https://trailhead.salesforce.com/trailblazer-community/groups/0F9300000001okuCAA?tab=discussion&sort=LAST_MODIFIED_DATE_DESC

## Suggested tasks
- [ ] Install the Salesforce Development plugin in Claude Code and try it against a scratch org project (S)
- [ ] Scaffold an Angular app with the angularinternalapp template, add a Data SDK extension, and deploy it to a scratch org (M)
- [ ] Build the HXL snow-report style widget for an Agentforce agent action using a custom Lightning type and UiWidgetBundle (L)

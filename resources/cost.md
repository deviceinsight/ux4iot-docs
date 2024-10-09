# Pricing

## General

The costs of ux4iot are divided into two parts: Azure Infrastructure Costs and fees for ux4iot itself.

* **Azure Infrastructure Costs** are approximately €0.07 - €0.08 per hour (€50 - €60 per month). The costs are slightly dependent on usage.

Generally, all costs are calculated based on the handled workload.

* **Fees for ux4iot** are €0.09 per hour (€70 per month).

Both costs are charged by Microsoft as part of your Azure bill.

## Logging

Beginning with version 4, ux4iot switched to workspace based application insights logging. This means that a separate log analytics service is deployed within the managed application. When ux4iot is logging internally, any logs that are above level "warn" will be written into application insights. You can configure the log analytics table tier of table "traces" with the configuration setting `logAnalyticsTracesTableTier`. The default value is "Analytics". Logs will then be kept for 90 days and all queries can be done according to the kusto query language.

If you choose basic, you will only get 8 days of retention time and you have restricted querying tools. However the costs per GB of logs will be drastically reduced to about a 3rd of a cost. [Read more about it here](https://azure.microsoft.com/de-de/pricing/details/monitor/).


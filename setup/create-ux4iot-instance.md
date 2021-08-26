# Create your ux4iot Instance

ux4iot is installed in your Azure subscription as a Managed Application. Billing will be handled by Microsoft.

## Creating via the Portal UI

Visit the [offer on Azure Marketplace](https://azuremarketplace.microsoft.com/) and click "Create". 

## Creating via the command line

TODO: Describe

{% tabs %}
{% tab title="AZ CLI" %}
```text
RESOURCE_GROUP=ux4iot
SUBSCRIPTION=yourazuresubscription

az managedapp create \
  --name ux4iot \
  --location westeurope \
  --kind marketplace \
  --resource-group $RESOURCE_GROUP \
  --managed-rg-id /subscriptions/${SUBSCRIPTION}/resourceGroups/ux4iot-resources \
  --plan-product ux4iot \
  --plan-name ux4iot \
  --plan-version 1.0 \
  --plan-publisher DeviceInsight
  --parameters "{\"iotHubEventHubConnectionString\": {\"value\": \"${IOT_HUB_EVENT_HUB_CONNECTION_STRING}\"}, \"iotHubServiceConnectionString\": {\"value\": \"${IOT_HUB_CONNECTION_STRING}\"}}"
```
{% endtab %}
{% endtabs %}

## Parameters

Specifying the Event Hub compatible connection is required. Configuring the service connection string is optional. It is necessary for the following hooks:

* [useDirectMethod](../using-react/hooks.md#usedirectmethod)
* [usePatchDesiredProperties](../using-react/hooks.md#usepatchdesiredproperties)

In effect, everything that not only consumes information but accesses the devices in some way.


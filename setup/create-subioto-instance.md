# Create your Subioto Instance

Subioto is installed in your Azure subscription as a Managed Application. Billing will be handled via your Microsoft subscription.

### Creating via the Portal UI

Visit the [offer on Azure Marketplace](https://azuremarketplace.microsoft.com/) and click "Create". Alternatively, you can click on the button below, which will bring you directly to the creation screen:

![](../.gitbook/assets/deploy-to-azure.png)

### Creating via the command line

TODO: Describe

{% tabs %}
{% tab title="AZ CLI" %}
```text
RESOURCE_GROUP=subioto
SUBSCRIPTION=yourazuresubscription

az managedapp create \
  --name subioto \
  --location westeurope \
  --kind marketplace \
  --resource-group $RESOURCE_GROUP \
  --managed-rg-id /subscriptions/${SUBSCRIPTION}/resourceGroups/subioto-resources \
  --plan-product subioto \
  --plan-name subioto \
  --plan-version 1.0 \
  --plan-publisher DeviceInsight
  --parameters "{\"iotHubEventHubConnectionString\": {\"value\": \"${IOT_HUB_EVENT_HUB_CONNECTION_STRING}\"}, \"iotHubServiceConnectionString\": {\"value\": \"${IOT_HUB_CONNECTION_STRING}\"}}"
```
{% endtab %}
{% endtabs %}

### Parameters

Specifying the Event Hub compatible connection is required. Configuring the service connection string is optional. It is necessary for the following hooks:

* [useDirectMethod](../using-react/hooks.md#usedirectmethod)
* [usePatchDesiredProperties](../using-react/hooks.md#usepatchdesiredproperties)

In effect, everything that not only consumes information but accesses the devices in some way.


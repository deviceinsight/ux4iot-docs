# Create your ux4iot Instance

ux4iot is installed in your Azure subscription as a Managed Application. Billing will be handled by Microsoft.

### Creating via Azure Marketplace

Visit the [offer on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/deviceinsightgmbh-4961725.ux4iot) and click "Get It Now".

### Creating via Azure Portal

Go to [https://portal.azure.com](https://portal.azure.com) and search for "ux4iot".

### Creating via the command line

If you prefer the command line, the following snippet shows how to do it. See further below for how to retrieve the values for the two parameters.

{% tabs %}
{% tab title="AZ CLI" %}
```
RESOURCE_GROUP=ux4iot
SUBSCRIPTION=yourazuresubscription

az managedapp create \
  --name ux4iot \
  --location westeurope \
  --kind marketplace \
  --resource-group $RESOURCE_GROUP \
  --managed-rg-id /subscriptions/${SUBSCRIPTION}/resourceGroups/ux4iot-resources \
  --plan-product ux4iot \
  --plan-name standard \
  --plan-version 1.5.0 \
  --plan-publisher deviceinsightgmbh-4961725 \
  --parameters "{\"iotHubEventHubConnectionString\": {\"value\": \"${IOT_HUB_EVENT_HUB_CONNECTION_STRING}\"}, \"iotHubServiceConnectionString\": {\"value\": \"${IOT_HUB_CONNECTION_STRING}\"}}"
```
{% endtab %}
{% endtabs %}

Concerning the parameters: Specifying the Event Hub compatible connection is required. Configuring the service connection string is optional. It is necessary for the following hooks:

* [useDirectMethod](../using-react/hooks.md#usedirectmethod)
* [usePatchDesiredProperties](../using-react/hooks.md#usepatchdesiredproperties)

In effect, everything that not only consumes information but accesses the devices in some way.

You can retrieve the service connection string for the IoT Hub with:

```
IOT_HUB_CONNECTION_STRING=$(az iot hub connection-string show \
  --resource-group RESOURCE_GROUP_OF_IOT_HUB \
  --subscription SUBSCRIPTION \
  --hub-name NAME_OF_IOT_HUB \
  --policy-name service
  --query connectionString \
  -o tsv)
```

You can retrieve the Event Hub compatible endpoint connection string with:

```
IOT_HUB_EVENT_HUB_CONNECTION_STRING=$(az iot hub connection-string show \
  --resource-group RESOURCE_GROUP_OF_IOT_HUB \
  --subscription SUBSCRIPTION \
  --hub-name NAME_OF_IOT_HUB \
  --query connectionString \
  --default-eventhub \
  --policy-name service \
  -o tsv)
```

Replace `RESOURCE_GROUP_OF_IOT_HUB` with the resource group that your IoT Hub resides in. Replace`NAME_OF_IOT_HUB` with the name of the IoT Hub. Replace `SUBSCRIPTION` with your Azure Subscription.

### Creating via Bicep (Azure Resource Manager)

Here is an example Bicep template that you can use to deploy a ux4iot instance.

```
resource managedApp 'Microsoft.Solutions/applications@2019-07-01' = {
  name: 'ux4iot'
  kind: 'marketplace'
  location: resourceGroup().location
  plan: {
    name: 'standard'
    product: 'ux4iot'
    publisher: 'deviceinsightgmbh-4961725'
    version: '1.5.0'
  }
  properties: {
    managedResourceGroupId: 'ux4iot-resources'
    parameters: {
      // Required
      iotHubEventHubConnectionString: {
        value: iotHubEventHubConnectionString
      }
      // Optional
      iotHubServiceConnectionString: {
        value: iotHubServiceConnectionString
      }
      // Optional
      dnsLabelOverride: {
        value: 'ux4iot-snapshot'
      }
      // Optional
      sku: {
        value: 'standard'
      }
      // Optional
      eventHubConsumerGroup: {
        value: '$Default'
      }
      // Optional
      primaryAdminSecret: {
        value: 'supersecret'
      }
      // Optional
      secondaryAdminSecret: {
        value: 'supersecretaswell'
      }

    }
  }
}
```

{% hint style="info" %}
Any tags you specify for the managed app will be inherited by the created managed resource group.
{% endhint %}

Before deploying **for the first time**, you will have to accept the legal terms:

```
az vm image accept-terms \
  --publisher 'deviceinsightgmbh-4961725' \
  --offer 'ux4iot' \
  --plan 'standard'
```

You can now deploy the Bicep template:

```
az deployment group create \
  --resource-group ux4iot \
  --subscription yourazuresubscription \
  --template-file template.bicep 
```

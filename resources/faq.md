# Known Bugs & Nice to know's

## How can the connection string and websocket URL be retrieved from az cli?

Here is an example for the websocket URL:

```
# ID of your Azure subscription
SUB="..."
# Name of the resource group containing the ux4iot instance
RG="..."
# Name of the ux4iot instance
NAME="ux4iot"

RESOURCE_ID="/subscriptions/$SUB/resourceGroups/$RG/providers/Microsoft.Solutions/applications/$NAME"

az resource show \
  --ids $RESOURCE_ID/customwebsocketUrls/url \
  --api-version 2018-09-01-preview \
  --query properties.value \
  --output tsv
```

Here is an example for the primary admin connection string

```
# ID of your Azure subscription
SUB="..."
# Name of the resource group containing the ux4iot instance
RG="..."
# Name of the ux4iot instance
NAME="ux4iot"

RESOURCE_ID="/subscriptions/$SUB/resourceGroups/$RG/providers/Microsoft.Solutions/applications/$NAME"

az resource show \
  --ids $RESOURCE_ID/customsharedAccessPolicies/Primary \
  --api-version 2018-09-01-preview \
  --query properties.connectionString \
  --output tsv
```

{% hint style="info" %}
You can quite easily find the `RESOURCE_ID` of the ux4iot instance in the Azure portal if you navigate to the ux4iot instance and copy the highlighted section of the URL:

<img src="../.gitbook/assets/image (2).png" alt="" data-size="original">
{% endhint %}

## Failed to publish event hub message ... "$cbs" endpoint timed out&#x20;

This is a bug that was communicated to the azure support, and that has still not been resolved yet. It occurred when subscribing directly to an IoTHub and caused message loss. We don't know where it comes from or what the issue is. When this happens to you, try to deploy an EventHub and redirect the messages from your IoTHub there. Then let your ux4iot use the connection string of the EventHub to subscribe to messages. You will need to restart your ux4iot service after a successful deployment. This is now possible in the managed application mainscreen on the top icon bar.

# FAQ

### How can the connection string and websocket URL be retrieved from az cli?

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
  --ids $RESOURCE_ID/customwebsocketUrls/url
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
  --ids $RESOURCE_ID/customsharedAccessPolicies/Primary
  --api-version 2018-09-01-preview \
  --query properties.value \
  --output tsv
```

{% hint style="info" %}
You can quite easily find the `RESOURCE_ID` of the ux4iot instance in the Azure portal if you navigate to the ux4iot instance and copy the highlighted section of the URL:

![](<../.gitbook/assets/image (5).png>)
{% endhint %}

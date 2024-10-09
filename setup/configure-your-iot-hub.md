# Configure your existing IoT Hub

{% hint style="danger" %}
We recommend using a **separate** EventHub for the iotHubEventHubConnectionString to subscribe to messages. Your IoTHub should forward the messages to this EventHub or be consumed by an azure function that then sends the messages to this EventHub. This is because of a bug (appearantly in the built-in EventHub of the IoTHub) that causes messages to get lost.

In order to use your IoTHub you can still provide the Shared Access Key of the IoTHub with Registry Read and Service Connect priviledges, to get access to the direct method, device twin and desired property features of ux4iot. &#x20;
{% endhint %}

In order to use the following hooks, you need to perform additional setup steps:

* [useConnectionState](../using-react/hooks.md#useconnectionstate)
* [useDeviceTwin](../using-react/hooks.md#usedevicetwin)

In both cases, the IoT Hub routing must be configured.

## Device Twin Changed Events

For 'Device Twin Changed Events', which are required for the [useDeviceTwin](../using-react/hooks.md#usedevicetwin) hook, a routing rule must be added as follows:

![](<../.gitbook/assets/image (18).png>)

If you want to use Azure CLI, you can accomplish the same in the following way:

{% tabs %}
{% tab title="AZ CLI" %}
```bash
az iot hub route create \
  --route-name ux4iot-twinchanges  \
  --hub-name IOT_HUB_NAME \
  --resource-group RESOURCE_GROUP_OF_IOT_HUB \
  --condition true \
  --endpoint events \
  --source twinchangeevents
```
{% endtab %}
{% endtabs %}

## Connection State Events

For 'Connection State Events', which are required for the [useConnectionState](../using-react/hooks.md#useconnectionstate) hook, a routing rule must be added as follows:

![](<../.gitbook/assets/image (19).png>)

If you want to use Azure CLI, you can accomplish the same in the following way:

{% tabs %}
{% tab title="AZ CLI" %}
```bash
az iot hub route create \
  --route-name ux4iot-connectionevents  \
  --hub-name IOT_HUB_NAME\
  --resource-group RESOURCE_GROUP_OF_IOT_HUB \
  --condition true \
  --endpoint events \
  --source deviceconnectionstateevents
```
{% endtab %}
{% endtabs %}

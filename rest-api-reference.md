---
description: Ux4iot REST API
---

# REST API Reference

Ux4iot exposes a REST API that you can use in your security backend and in your own apps to manage subscription workflow. These APIs are used by ux4iot-react hooks to communicate with security backends and ux4iot.

We recommend using the [ux4iot-admin-node](https://github.com/deviceinsight/ux4iot-admin-node) library when using the REST API. At the moment, we only support typescript.

The only time you will need to directly use the ux4iot REST api is in your security backend to forward grants and in your DevOps to ensure the ux4iot is running correctly. All other resources are mainly used by the [ux4iot-react](https://github.com/deviceinsight/ux4iot-react) library.&#x20;

In order to use the REST API you will need the Shared-Access-Key of the Ux4iot. You can find it as part of the ux4iot connection string. Get the connection string by using the left sidebar in your ux4iot instance.

![](.gitbook/assets/image.png)

There are api resources to perform actions against the IoTHub. They are only available if you use an IoTHub service connection string in your ux4iot deployment parameters.

## Common

## Get the server version of ux4iot

<mark style="color:blue;">`GET`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/version`

This resource can always be requested without any credentials.

{% tabs %}
{% tab title="200: OK version" %}

{% endtab %}
{% endtabs %}

## Get the current status of ux4iot

<mark style="color:blue;">`GET`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/status`

Helpful when you want to ensure the correct deployment of ux4iot.

{% tabs %}
{% tab title="200: OK OK" %}

{% endtab %}

{% tab title="503: Service Unavailable Still initializing " %}

{% endtab %}

{% tab title="500: Internal Server Error EventHub connection string misformed. Please check the iotHubEventHubConnectionString environment variable in your deployment file for ux4iot" %}

{% endtab %}

{% tab title="500: Internal Server Error IoTHub connection string misformed. Please check the iotHubServiceConnectionString environment variable in your deployment file for ux4iot." %}

{% endtab %}
{% endtabs %}

## Set the log level of ux4iot

<mark style="color:orange;">`PUT`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/logLevel/:level`

#### Path Parameters

| Name                                    | Type   | Description                                         |
| --------------------------------------- | ------ | --------------------------------------------------- |
| level<mark style="color:red;">\*</mark> | String | 'error' \| 'warn' \| 'info' \| 'verbose' \| 'debug' |

#### Headers

| Name                                                | Type   | Description |
| --------------------------------------------------- | ------ | ----------- |
| Shared-Access-Key<mark style="color:red;">\*</mark> | String |             |

{% tabs %}
{% tab title="204: No Content " %}

{% endtab %}

{% tab title="400: Bad Request Unknown log level" %}

{% endtab %}
{% endtabs %}

## Sessions

## Opens a new session in ux4iot

<mark style="color:green;">`POST`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/session`

{% tabs %}
{% tab title="200: OK " %}
```javascript
{
    sessionId: "string"
}
```
{% endtab %}
{% endtabs %}

## Delete a session by ID

<mark style="color:red;">`DELETE`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/sessions/:sessionId`

#### Path Parameters

| Name                                        | Type   | Description                     |
| ------------------------------------------- | ------ | ------------------------------- |
| sessionId<mark style="color:red;">\*</mark> | String | The ID of the session to delete |

#### Headers

| Name                                                | Type   | Description                                                                |
| --------------------------------------------------- | ------ | -------------------------------------------------------------------------- |
| Shared-Access-Key<mark style="color:red;">\*</mark> | String | The shared-access-key of the the connection string of your ux4iot instance |

{% tabs %}
{% tab title="204: No Content " %}

{% endtab %}

{% tab title="401: Unauthorized " %}

{% endtab %}
{% endtabs %}

## Delete all sessions

<mark style="color:red;">`DELETE`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/sessions`

#### Headers

| Name                                                | Type   | Description                                                                |
| --------------------------------------------------- | ------ | -------------------------------------------------------------------------- |
| Shared-Access-Key<mark style="color:red;">\*</mark> | String | The shared-access-key of the the connection string of your ux4iot instance |

{% tabs %}
{% tab title="204: No Content " %}

{% endtab %}

{% tab title="401: Unauthorized " %}

{% endtab %}
{% endtabs %}

## Grants

Grants authorize a session to subscribe to resources, patch desired properties and execute direct methods.

### GrantRequest Types

GrantRequest types only differ in the "type" property. For Telemetry and DirectMethods you can add an additional property to restrict specific telemetry keys or direct methods respectively.

{% code fullWidth="true" %}
```typescript
type DeviceTwinGrantRequest = { sessionId: string; deviceId: string; type: 'deviceTwin'; }
type ConnectionStateGrantRequest = { sessionId: string; deviceId: string; type: 'connectionState'; }
type D2CMessageGrantRequest = { sessionId: string; deviceId: string; type: 'd2cMessages'; }
type DesiredPropertiesGrantRequest = { sessionId: string; deviceId: string; type: 'desiredProperties'; }
type TelemetryGrantRequest = {
  sessionId: string;
  deviceId: string;
  type: 'telemetry';
  telemetryKey: string | null;
}
type DirectMethodGrantRequest = {
  sessionId: string;
  deviceId: string;
  type: 'telemetry';
  directMethodName: string | null;
}
```
{% endcode %}

## Forward a grant

<mark style="color:orange;">`PUT`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/grants`

Add a grant for the `sessionId` contained in the grant.

#### Headers

| Name                                                | Type   | Description                                   |
| --------------------------------------------------- | ------ | --------------------------------------------- |
| Shared-Access-Key<mark style="color:red;">\*</mark> | string | The Shared Access Key used for authentication |

#### Request Body

| Name                                        | Type           | Description                                                                                                                 |
| ------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| telemetryKey                                | string \| null | <p>available on type: "telemetry"</p><p>used to grant a specific telemetryKey. use null for all telemetry of the device</p> |
| deviceId<mark style="color:red;">\*</mark>  | string         | The IoT Hub device ID                                                                                                       |
| sessionId<mark style="color:red;">\*</mark> | string         | The sessionId for which the grant is requested                                                                              |
| type<mark style="color:red;">\*</mark>      | string         | 'telemetry' \| 'deviceTwin' \| 'connectionState' \| 'desiredProperties' \| 'directMethod' \| 'd2cMessages'                  |
| directMethodName                            | string         | available on type: 'directMethod' used to grant a specific directMethod. use null for all direct methods of the device      |

{% tabs %}
{% tab title="204: No Content " %}
```
NO CONTENT
```
{% endtab %}

{% tab title="400: Bad Request unknown grant type" %}
```
unknown grant type
```
{% endtab %}

{% tab title="401: Unauthorized no or invalid shared access key header" %}
```
Unauthorized: {error description}
```
{% endtab %}

{% tab title="404: Not Found no such sessionId" %}

{% endtab %}

{% tab title="400: Bad Request Grant unavailable (when IoT Hub API is disabled)" %}

{% endtab %}
{% endtabs %}

## Revoke a grant

<mark style="color:red;">`DELETE`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/grants`

Revoke the grant given&#x20;

#### Headers

| Name                                                | Type   | Description                                   |
| --------------------------------------------------- | ------ | --------------------------------------------- |
| Shared-Access-Key<mark style="color:red;">\*</mark> | string | The Shared Access Key used for authentication |

#### Request Body

| Name                                        | Type           | Description                                                                                                                 |
| ------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| deviceId<mark style="color:red;">\*</mark>  | string         | The device for which to revoke the grant                                                                                    |
| type<mark style="color:red;">\*</mark>      | string         | The grant type to revoke                                                                                                    |
| sessionId<mark style="color:red;">\*</mark> | string         | The session ID that the grant belongs to                                                                                    |
| telemetryKey                                | string \| null | <p>available on type: "telemetry"</p><p>used to grant a specific telemetryKey. use null for all telemetry of the device</p> |
| directMethodName                            | string \| null | available on type: 'directMethod' used to grant a specific directMethod. use null for all direct methods of the device      |

{% tabs %}
{% tab title="204: No Content " %}
```
```
{% endtab %}

{% tab title="400: Bad Request unknown grant type" %}

{% endtab %}

{% tab title="400: Bad Request Grant unavailable (when IoTHub API is disabled)" %}

{% endtab %}

{% tab title="401: Unauthorized no or invalid shared access key header" %}

{% endtab %}

{% tab title="404: Not Found no such sessionId" %}

{% endtab %}
{% endtabs %}

## Subscriptions

A subscription request lets a session subscribe to live data from the EventHub. Similar to GrantRequests, there are multiple SubscriptionRequest types:

{% code fullWidth="true" %}
```typescript
export type TelemetrySubscriptionRequest = {
  sessionId: string;
  deviceId: string;
  type: 'telemetry';
  telemetryKey: string | null; 
};
export type DeviceTwinSubscriptionRequest = { sessionId: string; deviceId: string; type: 'deviceTwin'; };
export type ConnectionStateSubscriptionRequest = { sessionId: string; deviceId: string; type: 'connectionState'; };
export type D2CMessageSubscriptionRequest = { sessionId: string; deviceId: string; type: 'd2cMessages'; };
```
{% endcode %}

## Subscribe to live data

<mark style="color:orange;">`PUT`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/subscription`

#### Request Body

| Name                                        | Type           | Description                                                                                |
| ------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------ |
| sessionId<mark style="color:red;">\*</mark> | string         |                                                                                            |
| deviceId<mark style="color:red;">\*</mark>  | string         |                                                                                            |
| type<mark style="color:red;">\*</mark>      | string         | one of 'telemetry' \| 'deviceTwin' \| 'connectionState' \| 'd2cMessages'                   |
| telemetryKey                                | string \| null | Only available on type: "telemetry". use null for subscribing to all telemetry of a device |

{% tabs %}
{% tab title="204: No Content " %}

{% endtab %}

{% tab title="403: Forbidden subscription request not granted" %}

{% endtab %}

{% tab title="404: Not Found No such sessionId" %}

{% endtab %}

{% tab title="400: Bad Request unknown subscription type" %}

{% endtab %}
{% endtabs %}

## Unsubscribe from live data

<mark style="color:red;">`DELETE`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/subscription`

#### Request Body

| Name                                        | Type           | Description                                                                                |
| ------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------ |
| sessionId<mark style="color:red;">\*</mark> | string         |                                                                                            |
| deviceId<mark style="color:red;">\*</mark>  | string         |                                                                                            |
| type<mark style="color:red;">\*</mark>      | string         | one of 'telemetry' \| 'deviceTwin' \| 'connectionState' \| 'd2cMessages'                   |
| telemetryKey                                | string \| null | Only available on type: "telemetry". use null for subscribing to all telemetry of a device |

{% tabs %}
{% tab title="204: No Content " %}

{% endtab %}

{% tab title="403: Forbidden subscription request not granted" %}

{% endtab %}

{% tab title="404: Not Found No such sessionId" %}

{% endtab %}

{% tab title="400: Bad Request unknown subscription type" %}

{% endtab %}
{% endtabs %}

## Bulk subscribe to multiple devices

<mark style="color:orange;">`PUT`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/subscriptions`

You have to send a list of subscription requests as body. If this list contains an invalid subscription request, the entire request will fail without applying any subscription requests. If you have a missing grant for some of the subscription requests, they will be skipped.

The response will contain a body that gives you the list of applied subscription requests. If you have valid grants for all subscription requests, the response body will match your request body.&#x20;

{% tabs %}
{% tab title="200: OK added SubscriptionRequests[]" %}

{% endtab %}

{% tab title="400: Bad Request Not all elements in the request body are subscription requests" %}

{% endtab %}
{% endtabs %}

## Bulk unsubscribe from multiple devices

<mark style="color:red;">`DELETE`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/subscriptions`

You have to send a list of subscription requests as body. If this list contains an invalid subscription request, the entire request will fail without removing any subscription requests. If you have a missing grant for some of the subscription requests, they will be skipped.

The response will contain a body that gives you the list of applied subscription requests. If you have valid grants for all subscription requests, the response body will match your request body.&#x20;

{% tabs %}
{% tab title="200: OK removed SubscriptionRequests[]" %}

{% endtab %}

{% tab title="400: Bad Request Not all elements in the request body are subscription requests" %}

{% endtab %}
{% endtabs %}

## Last Values

## Read last telemetry values for device

<mark style="color:blue;">`GET`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/lastValue/:deviceId/:telemetryKey?`

This endpoint both supports requests with sessionId header or requests with Shared-Access-Key header.

If you use a sessionId, then it will be check whether a grant for the device telemetry exists before the last values are returned.

If you use a Shared-Access-Key, then any last value will be returned, without grants being checked.

#### Path Parameters

| Name                                       | Type   | Description                                       |
| ------------------------------------------ | ------ | ------------------------------------------------- |
| deviceId<mark style="color:red;">\*</mark> | String |                                                   |
| telemetryKey                               | String | if omitted, returns all last values of the device |

{% tabs %}
{% tab title="200: OK Response structure depends on existence of telemetryKey" %}
<pre class="language-typescript"><code class="lang-typescript"><strong>// telemetryKey provided
</strong><strong>{ 
</strong>  deviceId: string;
  data: {
    [telemetryKey]: any;
  }
  timestamp: string; // iso date
}

// telemetryKey not provided
{
  deviceId: string;
  data: {
    [telemetryKey]: {
      value: any;
      timestamp: string; // iso date
    }
  }
  timestamp: '';
}
</code></pre>


{% endtab %}

{% tab title="404: Not Found No last telemetry found" %}

{% endtab %}

{% tab title="401: Unauthorized Provide either a Shared-Access-Key or a sessionId header" %}

{% endtab %}

{% tab title="403: Forbidden Forbidden to read last value of device: missing grant" %}

{% endtab %}

{% tab title="404: Not Found No such sessionId" %}

{% endtab %}

{% tab title="403: Forbidden Forbidden to read last value of device: invalid shared-access-key" %}

{% endtab %}
{% endtabs %}

## Remove all last values for a device

<mark style="color:red;">`DELETE`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/lastValue/:deviceId`

This endpoint both supports requests with sessionId header or requests with Shared-Access-Key header.

If you use a sessionId, then it will be check whether a grant for the device telemetry exists before the last values are returned.

If you use a Shared-Access-Key, then any last value will be returned, without grants being checked.

#### Path Parameters

| Name                                       | Type   | Description                                       |
| ------------------------------------------ | ------ | ------------------------------------------------- |
| deviceId<mark style="color:red;">\*</mark> | String |                                                   |
| telemetryKey                               | String | if omitted, returns all last values of the device |

{% tabs %}
{% tab title="200: OK Response structure depends on existence of telemetryKey" %}
<pre class="language-typescript"><code class="lang-typescript"><strong>// telemetryKey provided
</strong><strong>{ 
</strong>  deviceId: string;
  data: {
    [telemetryKey]: any;
  }
  timestamp: string; // iso date
}

// telemetryKey not provided
{
  deviceId: string;
  data: {
    [telemetryKey]: {
      value: any;
      timestamp: string; // iso date
    }
  }
  timestamp: '';
}
</code></pre>


{% endtab %}

{% tab title="401: Unauthorized Provide either a Shared-Access-Key or a sessionId header" %}

{% endtab %}

{% tab title="403: Forbidden Forbidden to read last value of device: missing grant" %}

{% endtab %}

{% tab title="404: Not Found No such sessionId" %}

{% endtab %}

{% tab title="403: Forbidden Forbidden to read last value of device: invalid shared-access-key" %}

{% endtab %}
{% endtabs %}

## Read last device twin for device

<mark style="color:blue;">`GET`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/deviceTwin/:deviceId`

Returns the last device twin for a device, if you have provided a IoTHub service connection string in your ux4iot deployment parameters.

#### Path Parameters

| Name                                       | Type   | Description |
| ------------------------------------------ | ------ | ----------- |
| deviceId<mark style="color:red;">\*</mark> | string |             |

{% tabs %}
{% tab title="200: OK LastValueResponse<DeviceTwin>" %}
<pre class="language-typescript"><code class="lang-typescript"><strong>{
</strong>  deviceId,
  data: DeviceTwin
  timestamp: string // iso date
}
</code></pre>
{% endtab %}

{% tab title="404: Not Found No last devicetwin found" %}

{% endtab %}

{% tab title="400: Bad Request IoT Hub API disabled, cannot invoke direct method" %}

{% endtab %}

{% tab title="401: Unauthorized Provide either a Shared-Access-Key or a sessionId" %}

{% endtab %}

{% tab title="403: Forbidden Forbidden to read last value of device: missing grant" %}

{% endtab %}

{% tab title="403: Forbidden Forbidden to read last value of device: invalid shared-access-key" %}

{% endtab %}
{% endtabs %}

## Read last connection state for device

<mark style="color:blue;">`GET`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/connectionState/:deviceId`

Returns the last connection state for a device.

If you have provided a IoTHub service connection string in your ux4iot deployment parameters and if there is no connection state found in the ux4iot's cache, ux4iot will also check the IoTHub for the connected property in the device twin for a last connection state.

[Read more about the connection state concept here](concepts.md)

#### Path Parameters

| Name                                       | Type   | Description |
| ------------------------------------------ | ------ | ----------- |
| deviceId<mark style="color:red;">\*</mark> | string |             |

{% tabs %}
{% tab title="200: OK LastValueResponse<boolean>" %}
<pre class="language-typescript"><code class="lang-typescript"><strong>{
</strong>  deviceId,
  data: DeviceTwin
  timestamp: string // iso date
}
</code></pre>
{% endtab %}

{% tab title="404: Not Found No device found" %}

{% endtab %}

{% tab title="400: Bad Request IoT Hub API disabled, cannot invoke direct method" %}

{% endtab %}

{% tab title="401: Unauthorized Provide either a Shared-Access-Key or a sessionId" %}

{% endtab %}

{% tab title="403: Forbidden Forbidden to read last value of device: missing grant" %}

{% endtab %}

{% tab title="403: Forbidden Forbidden to read last value of device: invalid shared-access-key" %}

{% endtab %}
{% endtabs %}

## IoTHub Methods

These api resources are only available if you provided an IoTHub service connection string in your ux4iot deployment parameters.

### Direct Method

We use the IoTHub parameters that you will need to send in the direct method request:

{% code fullWidth="true" %}
```typescript
type DirectMethodRequestBody = { 
  deviceId: string; 
  methodParams: {
    // The name of the method to call on the device.
    methodName: string;
    // The method payload that will be sent to the device.
    payload?: any;
    // The maximum time a device should take to respond to the method.
    responseTimeoutInSeconds?: number;
    // The maximum time the service should try to connect to the device before declaring the device is unreachable.
    connectTimeoutInSeconds?: number;
  }
}
```
{% endcode %}

When authorized and grants are set, ux4iot will send a request to IoTHub to execute the requested direct method. We forward the [HTTP response codes from the IoTHub](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-direct-methods#response).

## Executes a direct method on an IoTHub device

<mark style="color:green;">`POST`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/directMethod`

Provide a body containing the following

#### Request Body

| Name                                           | Type               | Description |
| ---------------------------------------------- | ------------------ | ----------- |
| deviceId<mark style="color:red;">\*</mark>     | String             |             |
| methodParams<mark style="color:red;">\*</mark> | DeviceMethodParams |             |

{% tabs %}
{% tab title="200: OK IoTHub Response: success" %}
<pre class="language-json"><code class="lang-json"><strong>{
</strong>    "status" : 201,
    "payload" : {...}
}
</code></pre>
{% endtab %}

{% tab title="404: Not Found No such sessionId" %}

{% endtab %}

{% tab title="403: Forbidden Forbidden" %}

{% endtab %}

{% tab title="400: Bad Request IoT Hub API disabled, cannot invoke direct method" %}

{% endtab %}

{% tab title="404: Not Found IoTHub Response: device ID is invalid" %}

{% endtab %}

{% tab title="504: Gateway Timeout IoTHub Response: device not responding to a direct method" %}

{% endtab %}
{% endtabs %}

### Patch Desired Properties

Apply a patch to desired properties of a device using the following request body:

```typescript
type PatchDesiredPropertiesRequestBody = { 
  deviceId: string;
  desiredPropertyPatch: Record<string, any>
}
```

## Executes a patch of desired properties on a device twin

<mark style="color:purple;">`PATCH`</mark> `https://ux4iot-xyz.westeurope.azurecontainer.io/deviceTwinDesiredProperties`

#### Request Body

| Name                                                   | Type                 | Description |
| ------------------------------------------------------ | -------------------- | ----------- |
| deviceId<mark style="color:red;">\*</mark>             | String               |             |
| desiredPropertyPatch<mark style="color:red;">\*</mark> | Record\<string, any> |             |

{% tabs %}
{% tab title="403: Forbidden Forbidden" %}

{% endtab %}

{% tab title="404: Not Found No such sessionId" %}

{% endtab %}

{% tab title="400: Bad Request IoT Hub API disabled, cannot invoke direct method" %}

{% endtab %}

{% tab title="500: Internal Server Error IoTHub Response: error" %}

{% endtab %}

{% tab title="200: OK " %}
```
{
   status: number;
   payload: Record<string, any>;
}
```
{% endtab %}
{% endtabs %}

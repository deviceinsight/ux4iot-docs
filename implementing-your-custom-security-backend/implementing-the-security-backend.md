# Security Backend

Your security backend must provide a _single_ HTTP resource that receives grant requests from the UI, more specifically by your [frontend's Grant Request Function](../using-react/implementing-the-grantrequestforwarder-function.md). The security backend has the following responsibilities:

* Authenticating the user or application that performed the request. You should use the authentication mechanism of your application, e.g. Bearer Tokens, Basic Authentication, etc.
* Checking if the grant request is allowed for this user or application.

If the grant request should be accepted, the backend should do the following things:

* Forward the grant request to ux4iot's Admin API, using an [SDK](broken-reference) or the [REST API](broken-reference)
* Return the HTTP response codes 200 or 204 (this is our recommendation, but no requirement)

If invalid authentication credentials were provided, the backend should return the HTTP response code 401 (Unauthorized).

If the user credentials are valid, but the grant request is not within the permissions of the user, the backend should return the HTTP response code 403 (Forbidden)

{% hint style="info" %}
You have to implement the client to your security backend in your user interface code in the Grant Request Function. This gives you full flexibility when it comes to your authentication scheme. It also means that you can use other ways to indicate success or failure. Using HTTP response codes as described above is merely our recommendation.
{% endhint %}

The grant requests are JSON objects that are passed to your local`grantRequestForwader` function and that you should forward to your security backend. They have the following structure:

## Invoke direct methods

```javascript
{
  "type": "directMethod",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123",
  "directMethodName": "reset"
}
```

If you forward this grant request to ux4iot, it means that the client can call the direct method `reset` on the device with the id `d123` . This is not an actual invocation of the method, but merely the permission to call the method at a later point in time.

## Subscribe to telemetry

```javascript
{
  "type": "telemetry",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123",
  "telemetryKey": "temperature"
}
```

If you forward this grant request to ux4iot, it means that the client subscribes to updates to the telemetry key `temperature` of the device `d123`. If the `telemetryKey` is omitted the grant is valid for all telemetry keys of the device.

{% hint style="info" %}
In contrast to other request like `invokeDirectMethod,`this not only approves the permission but also actively subscribes to updates.
{% endhint %}

## Subscribe to device twin changes

```javascript
{
  "type": "deviceTwin",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123" 
}
```

If you forward this grant request to ux4iot, it means that the client subscribes to updates to changes in the device twin of the device `d123`. It includes updates to the reported properties, desired properties and tags.

It is currently not possible to restrict this to a sub section of the device twin.

{% hint style="info" %}
In contrast to other request like `invokeDirectMethod`, this not only approves the permission but also actively subscribes to updates.
{% endhint %}

## Subscribe to connection State

```javascript
{
  "type": "connectionState",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123" 
}
```

If you forward this grant request to ux4iot, it means that the client subscribes to updates to changes to the connection state of the device `d123`.

{% hint style="info" %}
In contrast to other request like `invokeDirectMethod`, this not only approves the permission but also actively subscribes to updates.
{% endhint %}

## Modify desired properties

```javascript
{
  "type": "desiredProperties",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123" 
}
```

If you forward this grant request to ux4iot, it means that the client can patch the desired properties in the device twin of the device with id `d123` .

It is currently not possible to restrict this to a sub section of the desired properties.

## Subscribe to D2C messages

```javascript
{
  "type": "d2cMessages",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123" 
}
```

If you forward this grant request to ux4iot, it means that the client subscribes to all D2C messages sent by device `d123`.

{% hint style="info" %}
In contrast to other request like `invokeDirectMethod`, this not only approves the permission but also actively subscribes to updates.
{% endhint %}

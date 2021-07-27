# Implementing the Security Backend

Your security backend must provide a _single_ HTTP resource that receives grant requests from the UI, more specifically by your [frontend's `grantRequestForwarder` function](implementing-the-grantrequestforwarder-function.md). The security backend has the following responsibilities:

* Authenticating the user or application that performed the request. You should use the authentication mechanism of your application, e.g. Bearer Tokens, Basic Authentication, etc.
* Checking if the grant request is allowed for this user or application.

If the grant request should be accepted, the backend should do the following things:

* Forward the grant request to ux4iot's Admin API, using an [SDK](admin-sdks/) or the [REST API](admin-rest-api.md)
* Return the HTTP response codes 200 or 204 \(this is our recommendation, but no requirement\)

If invalid authentication credentials were provided, the backend should return the HTTP response code 401 \(Unauthorized\).

If the user credentials are valid, but the grant request is not within the permissions of the user, the backend should return the HTTP response code 403 \(Forbidden\)

{% hint style="info" %}
You have to implement the client to your security backend in your user interface code in the `grantRequestForwarder` function \(see [here](implementing-the-grantrequestforwarder-function.md) for details\). This gives you full flexibility when it comes to your authentication scheme. It also means that you can use other ways to indicate success or failure. Using HTTP response codes as described above is merely our recommendation.
{% endhint %}

The grant requests are JSON objects that are passed to your local`grantRequestForwader` function and that you should forward to your security backend. They have the following structure:

### Direct method request

```text
{
  "grantType": "directMethod",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123",
  "details":  {
    "directMethodName": "reset"
  }
}
```

If you forward this grant request to ux4iot, it means that the client can call the direct method `reset` on the device with the id `d123` . This is not an actual invocation of the method, but merely the permission to call the method at a later point in time.

### Telemetry request

```text
{
  "grantType": "telemetry",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123",
  "details":  {
    "telemetryKey": "temperature"
  }
}
```

If you forward this grant request to ux4iot, it means that the client subscribes to updates to the telemetry key `temperature` of the device `d123`.

{% hint style="info" %}
In contrast to other request like `diretMethod`, this not only approves the permission but also actively subscribes to updates.
{% endhint %}


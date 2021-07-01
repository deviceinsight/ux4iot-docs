# Implementing the security backend

Your security backend must provide a single HTTP resource that is called by the UI. It has the following responsibilities:

* Authenticating the user or application that performed the request. You should use the authentication mechanism of your application, e.g. Bearer Tokens, Basic Authentication, etc.
* Checking if the requested operation is allowed for this user or application.

If the requested operation is allowed, the backend should do the following things:

* Forward the requested operation to Subioto's admin API
* Return the HTTP response codes 200 or 204 \(this is our recommendation, but no requirement\)

If invalid authentication credentials were provided, the backend should return the HTTP response code 401 \(Unauthorized\).

If the user credentials are valid, but the requested operation is not allowed, the backend should return the HTTP response code 403 \(Forbidden\)

{% hint style="info" %}
You have to implement the client to your security backend in your user interface code. This gives you full flexibility when it comes to your authentication scheme. It also means that you can use other ways to indicate success or failure. Using HTTP response codes as described above is merely our recommendation.
{% endhint %}

The JSON objects that are passed to your `localAccessFunction` and that you should pass to your security backend, have the following structure:

### Direct method request

```text
{
  "type": "directMethod",
  "deviceId": "d123",
  "details":  {
    "directMethodName": "reset"
  }
}
```

If you forward this request to Subioto, it means that the client can call the direct method `reset` on the device with the id `d123` . This is not an actual invocation of the method, but merely the permission to call the method at a later point in time.

### Telemetry request

```text
{
  "type": "telemetry",
  "deviceId": "d123",
  "details":  {
    "telemetryKey": "temperature"
  }
}
```

If you forward this request to Subioto, it means that the client subscribes to updates to the telemetry key `temperature` of the device `d123`.

{% hint style="info" %}
In contrast to other request like `diretMethod`, this not only approves the permission but also actively subscribes to updates.
{% endhint %}


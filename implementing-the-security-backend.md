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


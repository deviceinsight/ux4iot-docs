# Node.js

First, add the dependency:

{% tabs %}
{% tab title="NPM" %}
```bash
npm install subioto-admin-sdk
```
{% endtab %}

{% tab title="Yarn" %}
```bash
yarn add subioto-admin-sdk
```
{% endtab %}
{% endtabs %}

Initialize the SDK using the connection string. You can retrieve the connection string from the Azure portal.

```javascript
const subiotoAdmin = require('subioto-admin');
subiotoAdmin.init({
    connectionString: "HostName=...;Key=secret";
});
```

Now you can whitelist grant requests using:

```javascript
subiotoAdmin.grant(grantRequest);
```

Usually, the `grantRequest` will be exactly identical to the body received by the custom security backend. In the security backend, you merely decide which grant requests to forward and which not to forward.

You can optionally pass along a user identifier, in order to be able to invalidate all sessions of a particular user \(e.g. when that user logs out of your system\): \(see [https://trello.com/c/L5mGgQXt/28-add-correlationid-feature](https://trello.com/c/L5mGgQXt/28-add-correlationid-feature)\)

```javascript
subiotoAdmin.grant(grantRequest, { userCorrelationId: "4711" });
```

If you want to revoke the grant at a later point in time, you can do this using:

```javascript
subiotoAdmin.revoke({
  sessionId: "ijfoewio22490320",
  deviceId: "d123",
  grantType: "telemetry"
});
```

You can revoke all grants for a session with this:

```javascript
subiotoAdmin.revoke({
  sessionId: "ijfoewio22490320"
});
```

You can even revoke all sessions:

```javascript
subiotoAdmin.revokeAll();
```




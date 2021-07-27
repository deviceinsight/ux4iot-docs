# Node.js

First, add the dependency:

{% tabs %}
{% tab title="NPM" %}
```bash
npm install ux4iot-admin-sdk
```
{% endtab %}

{% tab title="Yarn" %}
```bash
yarn add ux4iot-admin-sdk
```
{% endtab %}
{% endtabs %}

Initialize the SDK using the connection string. You can retrieve the connection string from the Azure portal.

```javascript
const ux4iotAdmin = require('ux4iot-admin');
ux4iotAdmin.init({
    connectionString: "HostName=...;Key=secret";
});
```

Now you can whitelist grant requests using:

```javascript
ux4iotAdmin.grant(grantRequest);
```

Usually, the `grantRequest` will be exactly identical to the body received by the custom security backend. In the security backend, you merely decide which grant requests to forward and which not to forward.

You can optionally pass along a user identifier, in order to be able to invalidate all sessions of a particular user \(e.g. when that user logs out of your system\): \(see [https://trello.com/c/L5mGgQXt/28-add-correlationid-feature](https://trello.com/c/L5mGgQXt/28-add-correlationid-feature)\)

```javascript
ux4iotAdmin.grant(grantRequest, { userCorrelationId: "4711" });
```

If you want to revoke the grant at a later point in time, you can do this using:

```javascript
ux4iotAdmin.revoke({
  sessionId: "ijfoewio22490320",
  deviceId: "d123",
  grantType: "telemetry"
});
```

You can revoke all grants for a session with this:

```javascript
ux4iotAdmin.revoke({
  sessionId: "ijfoewio22490320"
});
```

You can even revoke all sessions:

```javascript
ux4iotAdmin.revokeAll();
```




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


# Node.js Admin SDK

First, add the dependency:

=== "NPM"

    ```bash
    npm install ux4iot-admin-sdk
    ```

=== "Yarn"

    ```bash
    yarn add ux4iot-admin-sdk
    ```

Initialize the SDK using the connection string. You can retrieve the connection string from the Azure portal.

```javascript
const ux4iotAdmin = require('ux4iot-admin');
ux4iotAdmin.init({
    connectionString: "HostName=...;Key=secret";
});
```

Now you can whitelist grant requests:

```javascript
ux4iotAdmin.grant(grantRequest);
```

Usually, the `grantRequest` will be exactly identical to the body received by the custom security backend. In the security backend, you merely decide which grant requests to forward and which not to forward.



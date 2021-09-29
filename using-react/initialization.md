# Initialization

You initialize the ux4iot React library by wrapping your components with a `Ux4iotContext`

```javascript
import {Ux4iotContext} from "ux4iot-react";
...
function App() {
  return (
    <div className="App">
      <Ux4iotContext.Provider 
          options={options}
      >
          <MyView />
      </Ux4iotContext.Provider>
    </div>
  );
}
```

There are two modes of operations for using the library: Development mode and production mode. The initialization of the frontend libraries differs between the two modes.

### Development Mode

```jsx
const UX4IOT_ADMIN_CONNECTION_STRING = "Endpoint=...SharedAccessKey=...";

const devOptions: InitializeDevOptions = {
   adminConnectionString: UX4IOT_ADMIN_CONNECTION_STRING 
};

...
  <Ux4iotContext.Provider options={devOptions}>
  ...
  </Ux4iotContextProvider>
...
```

You can see a complete example in the [tutorial using create-react-app](tutorial-using-create-react-app.md).

The value of the `adminConnectionString` can be retrieved via the Azure portal:

![](../.gitbook/assets/image%20%287%29.png)

You can select either the Primary or the Secondary connection string.

Usually, the admin connection string is used by the [Security Backend](../implementing-your-custom-security-backend/introduction.md), but as there is no Security Backend in development mode, the frontend accesses the [Admin API](../implementing-your-custom-security-backend/admin-rest-api.md) on its own. For this reason the frontend requires the admin connection string.

#### Usage of Development Mode

{% hint style="danger" %}
Under no circumstances should you publish your web application in development mode. It allows anyone with access to the web applications to perform any requests towards your IoT devices and it also exposes the admin connection string that must be kept secret.
{% endhint %}

### Production Mode

For using production mode you need to provide a security backend for managing access permissions. You also need a [Grant Request Function](implementing-the-grantrequestforwarder-function.md) that acts as an adapter between the ux4iot library and this backend.

```jsx
const UX4IOT_WEBSOCKET_URL 'https://ux4iot-xxx.westeurope.azurecontainer.io';

const prodOptions: InitializeProdOptions = {
   ux4iotURL: UX4IOT_WEBSOCKET_URL
   grantRequestFunction: customGrantRequestFunction
};

...
  <Ux4iotContext.Provider options={prodOptions}>
  ...
  </Ux4iotContextProvider>
...
```

The value for the `ux4iotURL` parameter is available on your ux4iot instance in the Azure portal:

![](../.gitbook/assets/image%20%288%29.png)

For detailed information on how to implement the Grant Request Function, see [the dedicated chapter](implementing-the-grantrequestforwarder-function.md).


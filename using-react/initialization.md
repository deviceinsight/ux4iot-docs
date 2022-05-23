# Initialization

You initialize the ux4iot React library by wrapping your components with a `Ux4iotContext`

```javascript
import {Ux4iotContextProvider} from "ux4iot-react";
...
function App() {
  return (
    <div className="App">
      <Ux4iotContextProvider 
          options={options}
      >
          <MyView />
      </Ux4iotContextProvider>
    </div>
  );
}
```

There are two modes of operations for the library: Development mode and production mode. The initialization differs between the two modes.

### Development Mode

```jsx
const UX4IOT_ADMIN_CONNECTION_STRING = "Endpoint=...SharedAccessKey=...";

const devOptions: InitializeDevOptions = {
   adminConnectionString: UX4IOT_ADMIN_CONNECTION_STRING 
};

...
  <Ux4iotContextProvider options={devOptions}>
  ...
  </Ux4iotContextProvider>
...
```

You can see a complete example in the [tutorial using create-react-app](tutorial-using-create-react-app.md).

The value of the `adminConnectionString` option can be retrieved via the Azure portal:

![](<../.gitbook/assets/image (7).png>)

You can select either the Primary or the Secondary connection string.

In production mode the admin connection string is used by the [Security Backend](../implementing-your-custom-security-backend/introduction.md), but as there is no Security Backend in development mode, the frontend accesses the [Admin API](../implementing-your-custom-security-backend/admin-rest-api.md) on its own. For this reason the frontend requires the admin connection string.

#### Usage of Development Mode

{% hint style="danger" %}
Under no circumstances should you publish your web application in development mode. It allows anyone with access to the web application to perform any requests towards your IoT devices and it also exposes the admin connection string that must be kept secret.
{% endhint %}

### Production Mode

For production mode you need to provide a security backend for managing access permissions. You also need a [Grant Request Function](implementing-the-grantrequestforwarder-function.md) that acts as an adapter between the ux4iot library and this backend.

```jsx
const UX4IOT_WEBSOCKET_URL 'https://ux4iot-xxx.westeurope.azurecontainer.io';

const prodOptions: InitializeProdOptions = {
   ux4iotURL: UX4IOT_WEBSOCKET_URL
   grantRequestFunction: customGrantRequestFunction
};

...
  <Ux4iotContextProvider options={prodOptions}>
  ...
  </Ux4iotContextProvider>
...
```

The value for the `ux4iotURL` parameter is available on your ux4iot instance in the Azure portal:

![](<../.gitbook/assets/image (8).png>)

For detailed information on how to implement the Grant Request Function, see [the dedicated chapter](implementing-the-grantrequestforwarder-function.md).

### onSocketConnectionUpdate

In both Development and Production mode you can pass a function to the options of the `Ux4iotContextProvider`&#x20;

```typescript
const devOptions: InitializeDevOptions = {
   adminConnectionString: UX4IOT_ADMIN_CONNECTION_STRING
   onSocketConnectionUpdate: (reason, description) => { /* handle update */ }
};
const prodOptions: InitializeProdOptions = {
   ux4iotURL: UX4IOT_WEBSOCKET_URL
   grantRequestFunction: customGrantRequestFunction
   onSocketConnectionUpdate: (reason, description) => { /* handle update */ }
};
```

It takes two arguments:

*   reason - can be one of four strings:

    * &#x20;`socket_connect` - called when the socket is established with the server
    * `socket_connect_error` called when the client throws an error when establishing the socket
    * `socket_disconnect` - called when the socket is disconnected
    * `ux4iot_unreachable` - called when a sessionId cannot be fetched from the ux4iot instance

    Every reason except for `ux4iot_unreachable` originates from socket.io and is documented here: [https://socket.io/docs/v4/client-api/#event-connect](https://socket.io/docs/v4/client-api/#event-connect)&#x20;
* description - `string | undefined` : error explanation provided in `socket_connect_error`, `socket_disconnect` and `ux4iot_unreachable`&#x20;

The full function type you need to provide is

```typescript
export type ConnectionUpdateReason =
	| 'socket_connect'
	| 'socket_connect_error'
	| 'socket_disconnect'
	| 'ux4iot_unreachable';

export type ConnectionUpdateFunction = (
  reason: ConnectionUpdateReason,
  description?: string
) => void;
```


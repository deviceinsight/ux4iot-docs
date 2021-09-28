# Grant Request Function

The `grantRequestFunction` is a function in your frontend that acts as an adapter between the ux4iot library \(that e.g. provides the React hooks\) and your custom security backend. It must be passed to the `Ux4iotContext` upon initialization.

### Ux4iotContextProvider

`import {Ux4iotContextProvider} from 'ux4iot-react'`

The `Ux4iotContextProvider` is a provider implementation of `Ux4iotContext`. It can take two different argument types. One for development, one for production mode, both typed by `InitializeDevOptions` and `InitializeProdOptions` respectively:

#### Development Mode

```jsx
const devOptions: InitializeDevOptions = {
   adminConnectionString: UX4IOT_ADMIN_CONNECTION_STRING 
};

return <Ux4iotContext.Provider options={devOptions}>...</Ux4iotContextProvider>
```

You have already seen how this works in the [tutorial using create-react-app](../using-react/tutorial-using-create-react-app.md).

#### Usage of Development Mode

{% hint style="danger" %}
Under no circumstances should you publish your web application in development mode. It allows anyone with access to the web applications to perform any requests towards your IoT devices and it also exposes the admin connection string that must be kept secret.
{% endhint %}

#### Production Mode

```jsx
const prod: InitializeProdOptions = {
   ux4iotURL: UX4IOT_WEBSOCKET_URL // http://ux4iot-example.westeurope.azurecontainer.io
   grantRequestFunction: customGrantRequestFunction
};

return <Ux4iotContext.Provider options={prodOptions}>...</Ux4iotContextProvider>
```

The `UX4IOT_WEBSOCKET_URL` is available on your ux4iot instance in the Azure portal in the sidebar, right below "Admin Connection String".

The type of `InitializeProdOptions` is defined as follows:

```typescript
export type InitializeProdOptions = {
	ux4iotURL: string;
	grantRequestFunction: GrantRequestFunctionType;
}
```

Meaning, if you want to run ux4iot-react in production mode you must implement a function of type `GrantRequestFunctionType`.

### GrantRequestFunction

`GrantRequestFunctionType` is defined as follows:

```typescript
enum GRANT_RESPONSES {
	FORBIDDEN = 'FORBIDDEN',
	UNAUTHORIZED = 'UNAUTHORIZED',
	GRANTED = 'GRANTED',
	ERROR = 'ERROR',
}

type GrantRequestFunctionType = (grant: GrantRequest) => Promise<GRANT_RESPONSES>
```

For now we do not care about `GrantRequest`. Internally, ux4iot-react uses this function to perform grant requests to either ux4iot directly \(development mode\) or your security backend \(production mode\).

A custom `grantRequestFunction` could look like this:

```javascript
import axios from 'axios'
import {GrantRequestFunctionType, GRANT_RESPONSES} from 'ux4iot-react';

const UX4IOT_URL = 'https://ux4iot-xyz.westeurope.azurecontainer.io'
const CUSTOM_BACKEND = 'https://your-iot-app.com/api/ux4iot-grant-requests'

const customGrantRequestFunction: GrantRequestFunctionType = async grantRequest => {
  const config = {
    headers: {
      Authorization: "Bearer " + getCurrentAccessToken()
    }
  };
  try {
		await axios.put(CUSTOM_BACKEND, grantRequest, config);
	} catch (error) {
		if (axios.isAxiosError(error)) {
			if (error.response) {
				if (error.response.status === 401) {
					return GRANT_RESPONSES.UNAUTHORIZED;
				} else if (error.response.status === 403) {
					return GRANT_RESPONSES.FORBIDDEN;
				}
			}
		}
		return GRANT_RESPONSES.ERROR;
	}
	return GRANT_RESPONSES.GRANTED;
};

```

Your full app can then look like this, combining the `Ux4iotContextProvider` with your custom `grantRequestFunction`:

```jsx
import axios from 'axios'
import {
  GrantRequestFunctionType, 
  GRANT_RESPONSES,
  Ux4iotContextProvider
} from 'ux4iot-react';

const UX4IOT_URL = 'https://ux4iot-xyz.westeurope.azurecontainer.io'
const CUSTOM_BACKEND = 'https://your-iot-app.com/api/ux4iot-grant-requests'

const customGrantRequestFunction: GrantRequestFunctionType = async grantRequest => {
  const config = {
    headers: {
      Authorization: "Bearer " + getCurrentAccessToken()
    }
  };
  try {
		await axios.put(CUSTOM_BACKEND, grantRequest, config);
	} catch (error) {
		if (axios.isAxiosError(error)) {
			if (error.response) {
				if (error.response.status === 401) {
					return GRANT_RESPONSES.UNAUTHORIZED;
				} else if (error.response.status === 403) {
					return GRANT_RESPONSES.FORBIDDEN;
				}
			}
		}
		return GRANT_RESPONSES.ERROR;
	}
	return GRANT_RESPONSES.GRANTED;
};

export function App() {
  const prod: InitializeProdOptions = {
    ux4iotURL: UX4IOT_WEBSOCKET_URL // http://ux4iot-example.westeurope.azurecontainer.io
    grantRequestFunction: customGrantRequestFunction
  };
  
  return <Ux4iotContextProvider options={prodOptions}>...</Ux4iotContextProvider>
}
```

As you can see, you initiate a HTTP request to your backend using your HTTP library of choice \(in this case [axios](https://github.com/axios/axios) is used\). You use your usual authentication mechanism \(in this case an OAuth2 access token\).

{% hint style="info" %}
The `GRANT_RESPONSES` are forwarded to the `onGrantError` callback of the exported ux4iot-react hooks. Obviously, you could always return `GRANT_RESPONSES.GRANTED` in  your custom `grantRequestFunction`. The return type was chosen to be this simplistic, so that you receive a state in your components that use the hooks to notify the user in the frontend with a suitable error message when the grant was denied.

Example:

```typescript
const temperature = useSingleTelemetry(
  'my-device',
  'temperature',
  undefined,
  error => {
    if(error === GRANT_RESPONSES.UNAUTHORIZED) {
      displayUnauthorizedError(error);
    }
  }
);
```
{% endhint %}


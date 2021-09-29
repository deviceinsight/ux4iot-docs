# Grant Request Function

The Grant Request Function in your frontend acts as an adapter between the ux4iot library \(that e.g. provides the React hooks\) and your [custom security backend](../implementing-your-custom-security-backend/introduction.md). You provide it during [initialization](initialization.md).

The Grant Request Function is called by the ux4iot library with Grant Requests that are derived from the hooks and functions used in your components. It must forward these Grant Requests to the security backend and return the responses of these request.

This is the type definition of the function:

```typescript
enum GRANT_RESPONSES {
	FORBIDDEN = 'FORBIDDEN',
	UNAUTHORIZED = 'UNAUTHORIZED',
	GRANTED = 'GRANTED',
	ERROR = 'ERROR',
}

type GrantRequestFunctionType = (grant: GrantRequest) => Promise<GRANT_RESPONSES>
```

You can largely ignore `GrantRequest`for now as it is usually simply passed through the function to your security backend. 

A custom Grant Request Function could look like this:

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

As you can see that you have full control over:

* the library to use for the requests \(in the example [axios](https://github.com/axios/axios) is used\) 
* the mechanism used for authenticating against your backend \(in the example and OAuth2 access token is used\)
* how the response to the REST requests are mapped to the response of the function

Due to this flexibility, you can integrate the security backend into your existing API and use established conventions and mechanisms.

Your full app can then look like this:

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
    ux4iotURL: UX4IOT_WEBSOCKET_URL
    grantRequestFunction: customGrantRequestFunction
  };
  
  return <Ux4iotContextProvider options={prodOptions}>...</Ux4iotContextProvider>
}
```

The `GRANT_RESPONSES` are forwarded to the `onGrantError` callback of the hooks. Here is an example:

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


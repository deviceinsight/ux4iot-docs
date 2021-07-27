# Implementing the grantRequestForwarder Function

In your frontend code, you need to implement a function for forwarding grant requests to your custom security backend. This function exists to give you full control over the request so that you can use your existing authentication mechanism.

There usually is little to no logic in the function. Here is an example:

```javascript
const UX4IOT_URL = 'https://ux4iot-xyz.westeurope.azurecontainer.io'
const CUSTOM_BACKEND = 'https://your-iot-app.com/api/ux4iot-grant-requests'

const grantRequestFunction = grantRequest => {
  return axios.put(CUSTOM_BACKEND, grantRequest, {
    headers: {
      Authorization: "Bearer " + getCurrentAccessToken()
    }
  });
};

const ux4iot = initUx4iot(UX4IOT_URL, grantRequestFunction);
```

TODO: Handle response status, define return type of function

As you can see, you initiate a HTTP request to your backend using your HTTP library of choice \(in the example [axios](https://github.com/axios/axios) is used\). You use your usual authentication mechanism \(in this case an OAuth2 access token\).


# Implementing the grantRequestForwarder Function

In your frontend code, you need to implement a middleware function for forwarding grant requests to your custom security backend. This function exists to give you full control over the request so that you can use your existing authentication mechanism.

There usually is little to no logic in the function. Here is an example:

```javascript
const SUBIOTO_URL = 'https://subioto-xyz.westeurope.azurecontainer.io'
const CUSTOM_BACKEND = 'https://your-iot-app.com/api/subioto-grant-requests'

const subioto = initSubioto(SUBIOTO_URL, grantRequest => {
    return axios.put(CUSTOM_BACKEND, grantRequest, {
        headers: {
            Authorization: "Bearer " + getCurrentAccessToken()
        }
    });
});
```

TODO: Handle response status, define return type of function

As you can see, you initiate a HTTP request to your backend using your HTTP library of choice. You use your usual authentication mechanism \(in this case an OAuth2 access token\).


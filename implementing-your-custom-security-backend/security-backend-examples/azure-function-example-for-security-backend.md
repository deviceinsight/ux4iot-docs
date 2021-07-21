# Azure Function using Javascript

The following is an example implementation of a custom security backend using Azure Functions and Node.js

```javascript
const subiotoAdmin = require('subioto-admin');
subiotoAdmin.init({
    connectionString: "HostName=...;Key=secret";
});

module.exports = async function (context, req) {
    
    // This is *your* custom authentication approach
    const bearerToken = req.headers('Authentication');    
    const {userId} = await evaluateBearerToken(bearerToken);
    
    if (!userId) {
    
        context.res = {
            body: "Unauthorized",
            status: 401
        };
        
    } else {
        
        // All users can subscribe to telemetry events that are visible for them
        // using *your* custom access control scheme, which defines which users 
        // have access to which IoT devices.
        if (req.body.type === 'telemetry' && isDeviceVisibleForUser(req.body.device, userId)) {
            subiotoAdmin.grant(req.body);
            context.res = {
                status: 204
            };
        } else {
            context.res = {
               body: "Forbidden",
               status: 403
            };
        }
    }
    
    context.done();    
}
```

{% hint style="info" %}
In this example `isDeviceVisibleForUser` is a custom method that implements the access control mechanism of your app. `evaluateBearerToken` is a custom method that implements your authentication scheme \(e.g. using OAuth2\).
{% endhint %}

As you can see, you have full flexibility when it comes to determine which users may perform which actions.

You can find a working example on GitHub \(TODO\)


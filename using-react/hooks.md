# Hooks

### useTelemetry

The `useTelemetry` hook returns a variable that is updated as soon as new values of the given telemetry key are received. This hook relies on the assumption that your Device-to-Cloud messages are JSON documents where the key is the telemetry key and the value is the current telemetry value. We plan to support more complex payloads in the future \(selecting using JSON Path, Avro, etc\). If you have other message payloads, you can use the useD2CMessages hook, see below.

```javascript
const temperature = useTelemetry("simulated-device", "temperature");
```

When the following D2C message is received, the variable temperature is updated \(and a render is triggered\):

```javascript
{
  "temperature": 42.1,
  "pressure": 0.5
}
```

### useDirectMethod

The `useDirectMethod` hook returns a Javascript function that, when invoked, calls a direct method on the target device. It returns a Promise that resolves to the direct method result that the device returns \(or an error when the direct method could not be executed if the device is e.g. offline\).

```javascript
const enableFastLogging = useDirectMethod("simulated-device", {
        methodName: 'SetTelemetryInterval',
        payload: 1
    });
```

You can now call the function and await the result

```javascript
const result = await enableFastLogging();
```

TODO: Do something with the result

### useDeviceTwin

The `useDeviceTwin` returns a variable that is updated as soon as the device twin of the device changes.

```javascript
const deviceTwin = useDeviceTwin("simulated-device");
```

Here is an example of the returned device twin:

```javascript
{
  "version": 2,
  "tags": {
    "$etag": "123",
    "deploymentLocation": {
      "building": "43",
      "floor": "1"
    }
  },
  "properties": {
    "desired": {
      "telemetryConfig": {
        "sendFrequency": "5m"
      },
      "$version": 1
    },
    "reported": {
      "telemetryConfig": {
        "sendFrequency": "5m",
        "status": "success"
      },
      "batteryLevel": 55,
      "$version": 4
    }
  }
}
```

### useConnectionState

The `useConnectionState` hook returns a variable that is updated as soon as the connection state changes, i.e. as soon as a device connects or disconnects. 

```javascript
const connectionState = useConnectionState("simulated-device");
```

{% hint style="warning" %}
The connection state information can be quite delayed \(up to 1 minute\). This is not a Subioto issue, but an issue with IoT Hub itself.
{% endhint %}

### usePatchDesiredProperties

```javascript
const patchDesiredProperties = usePatchDesiredProperties("simulated-device");
```

You can now update the desired properties by calling this function:

```javascript
patchDesiredProperties({
  sendInterval: 2
});
```

### useD2CMessages

Use the `useD2CMessages` hook to receive Device-to-Cloud messages of a device.

```javascript
const unsubscribe = useD2CMessages("simulated-device", msg => {
  console.log("Received the D2C message:", msg);
});
```

You can use the returned function to cancel the subscription.


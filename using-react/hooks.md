# Hooks

## useTelemetry

The `useTelemetry` hook makes it very easy to just listen to telemetry on a single device.

```typescript
const value = useTelemetry(deviceId, telemetryKey, onData, onGrantError);
```

#### Arguments

<table><thead><tr><th>Argument</th><th>Description</th><th>Type</th><th data-type="checkbox">Required?</th></tr></thead><tbody><tr><td>deviceId</td><td>The device ID of the device from which to receive telemetry data</td><td><code>string</code></td><td>true</td></tr><tr><td>telemetryKey</td><td>The key of the telemetry item</td><td><code>string</code></td><td>true</td></tr><tr><td>onData</td><td>Callback, executed when new telemetry of <code>telemetryKey</code> is received on the device</td><td><code>(data: unknown) => void</code></td><td>false</td></tr><tr><td>onGrantError</td><td>Callback, executed when the <code>grantRequestFunction</code> fails to grant the direct method request</td><td><code>GrantErrorCallback</code></td><td>false</td></tr></tbody></table>

#### Return Value

This hook returns a single value. Every time the device sends new telemetry with key `telemetryKey` this hook will update this value.

{% hint style="info" %}
This hook relies on the assumption that your Device-to-Cloud messages are JSON documents where the key is the telemetry key and the value is the current telemetry value. We plan to support more complex payloads in the future (selecting using JSON Path, Avro, etc). If you have other message payloads, you can use the [useD2CMessage hook](hooks.md#used-2-cmessages).
{% endhint %}

#### Example

A component subscribing to the `temperature` telemetry.

```jsx
const temperature = useTelemetry('simulated-device', 'temperature');

return (
    <div>
        <h3>Current Temperature of simulated-device</h3>
        <div>{temperature}</div>
    </div>
);
```

The D2C messages are expected to look like this:

```jsx
{
  "temperature": 42.1,
  ...
}
```

## useMultiTelemetry

The `useMultiTelemetry` hook is a more sophisticated variant of `useTelemetry`. It is designed to cover use-cases where a several streams of telemetry of multiple devices need to be subscribed to.

```typescript
    const {
        telemetry,
        toggleTelemetry,
        isSubscribed,
        currentSubscribers,
        addTelemetry,
        removeTelemetry,
    } = useMultiTelemetry(
        { [deviceId]: ['temperature', 'pressure'] },
        (deviceId, key, value) => console.log(deviceId, key, value),
        error => console.log(error)
    );
```

#### Arguments

<table><thead><tr><th>Argument</th><th>Description</th><th>Type</th><th data-type="checkbox">Required?</th></tr></thead><tbody><tr><td>initialSubscribers</td><td>Object of key-value pairs, with keys: the device IDs of your IoTHub devices, and value: a list of strings, defining the telemetryKeys to subscribe to</td><td><code>Record&#x3C;string, string[]></code></td><td>false</td></tr><tr><td>onData</td><td>Callback, executed when a new <code>value</code> for a <code>telemetryKey</code> is sent by a device with ID <code>deviceId</code></td><td><code>(deviceId: string, telemetryKey: string, value: unknown) => void</code></td><td>false</td></tr><tr><td>onGrantError</td><td>Callback, executed when the <code>grantRequestFunction</code> fails to grant the subscription request.</td><td><code>GrantErrorCallback</code></td><td>false</td></tr></tbody></table>

{% hint style="info" %}
Do not try to perform subscription updates over the `initialSubscribers` object. This object is meant solely as an option for use cases where you always have an initial set of subscribers. Updates to `initialSubscribers` will not trigger updates in the hook.
{% endhint %}

#### Return Value

This hook returns an object containing other objects and functions to interact with telemetry subscriptions.

| Key                | Value                                                                                                           | Type                                                  |
| ------------------ | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| telemetry          | Object holding the current values of all your telemetry subscriptions                                           | `Record<string, Record<string, unknown>`              |
| toggleTelemetry    | Toggles a telemetry subscription for a `deviceId` and `telemetryKey`                                            | `(deviceId: string, telemetryKey: string) => void`    |
| addTelemetry       | Adds a telemetry subscription for a `deviceId` and multiple `telemetryKeys`                                     | `(deviceId: string, telemetryKeys: string[]) => void` |
| removeTelemetry    | Removes a telemetry subscription for a `deviceId` and multiple `telemetryKeys`                                  | `(deviceId: string, telemetryKeys: string[]) => void` |
| isSubscribed       | Checks whether a telemetry subscription for a `deviceId` and `telemetryKey` exists                              | `(deviceId: string, telemetryKey: string) => boolean` |
| currentSubscribers | Object containing all current subscribers with key being the `deviceId` and value being the telemetryKey names. | `Record<string, string[]>`                            |

TODO: Add example for `useMultiTelemetry`

## useDirectMethod

The `useDirectMethod` hook returns a function that, when invoked, calls a direct method on the target device. It returns a Promise that resolves to the direct method result that the device returns (or an error when the direct method could not be executed, e.g. if the device is offline).

```typescript
const reboot = useDirectMethod(deviceId, methodName, onGrantError);
```

#### Arguments

<table><thead><tr><th>Argument</th><th>Description</th><th>Type</th><th data-type="checkbox">Required?</th></tr></thead><tbody><tr><td>deviceId</td><td>The device ID of the device to execute the direct method on</td><td><code>string</code></td><td>true</td></tr><tr><td>methodName</td><td>The name of the method to execute on the device</td><td><code>string</code></td><td>true</td></tr><tr><td>onGrantError</td><td>Callback, executed when the <code>grantRequestFunction</code> fails to grant the direct method request</td><td><code>GrantErrorCallback</code></td><td>false</td></tr></tbody></table>

#### Return Value

This hook returns a function: `(params: Record<string, unknown>) => Promise<unknown>`

You pass the method payload to this function and it outputs the[ result of the direct method invocation on the device](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-direct-methods#response-1).

{% hint style="info" %}
Do not confuse the `onGrantError` handler of `useDirectMethod` with the catch block of the direct method itself. `onGrantError` will only be executed when this hook is rendered by react and the security backend fails to grant the direct method. The error that `reboot` may throw is an HTTP error that could occur when the function is executed.
{% endhint %}

#### Example

```jsx
const reboot = useDirectMethod(deviceId, 'reboot', error => console.log(error));
const result = useState<unknown>();
const error = useState<string>();

const handleClick = () => {
    const payload = { delay: 2000 };

    reboot(payload)
        .then(result => setState(result))
        .catch(error => setError(error));
}

return <button onClick={() => handleClick()}>Reboot Device</button>
```

## useDeviceTwin

The `useDeviceTwin` hook subscribes to device twin updates.

```javascript
const deviceTwin = useDeviceTwin(deviceId, onData, onGrantError);
```

#### Arguments

<table><thead><tr><th>Argument</th><th>Description</th><th>Type</th><th data-type="checkbox">Required?</th></tr></thead><tbody><tr><td>deviceId</td><td>The device id of the device you want to subscribe to.</td><td><code>string</code></td><td>true</td></tr><tr><td>onData</td><td>Callback, executed when a new twin updated is received.</td><td><code>(twin: Twin) => void</code></td><td>false</td></tr><tr><td>onGrantError</td><td>Callback, executed when the <code>grantRequestFunction</code> fails to grant the subscription request.</td><td><code>GrantErrorCallback</code></td><td>false</td></tr></tbody></table>

#### Return Value

This hook returns a value: `Twin`

This hook returns the device twin whenever twin updates are made on the IoTHub device. This hook uses the `Twin` typescript type provided from the [azure-iothub library](https://www.npmjs.com/package/azure-iothub).

Here is an example of a returned device twin:

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

## useConnectionState

The `useConnectionState` hook subscribes to the connection state of a device. This state can change, i.e as soon as a device connects or disconnects.

```javascript
const connectionState = useConnectionState(deviceId, onData, onGrantError);
```

#### Arguments

| Argument     | Description                                                                                 | Type                                 |          |
| ------------ | ------------------------------------------------------------------------------------------- | ------------------------------------ | -------- |
| deviceId     | The device id of the device you want to subscribe to.                                       | `string`                             | Required |
| onData       | Callback, executed when a new connection state updated is received.                         | `(connectionState: boolean) => void` | Optional |
| onGrantError | Callback, executed when the `grantRequestFunction` fails to grant the subscription request. | `GrantErrorCallback`                 | Optional |

#### Return Value

This hook returns a value: `boolean`

This value changed as soon as a device connects or disconnects.

{% hint style="warning" %}
The connection state information can be quite delayed (up to 1 minute). This is not a ux4iot issue, but an issue with IoT Hub itself (see [here](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-event-grid#limitations-for-device-connected-and-device-disconnected-events) and [here](https://docs.microsoft.com/en-us/answers/questions/434493/device-connection-state-events-delayed.html)).
{% endhint %}

## usePatchDesiredProperties

The `usePatchDesiredProperties` hook is used to perform desired property updates on devices.

```javascript
const patchDesiredProperties = usePatchDesiredProperties(deviceId, onGrantError);
```

#### Arguments

| Argument     | Description                                                                                            | Type                 |          |
| ------------ | ------------------------------------------------------------------------------------------------------ | -------------------- | -------- |
| deviceId     | The device id of the device onto which to patch the desired properties                                 | `string`             | Required |
| onGrantError | Callback, executed when the `grantRequestFunction` fails to grant the patch desired properties request | `GrantErrorCallback` | Optional |

#### Return Value

This hook returns a function: `(desiredProperties: Record<string, unknown>) => Promise<IoTHubResponse | void>`

The hook takes in an object of desired properties to send to the device with the specified device ID.

{% hint style="info" %}
When you call the function returned by this hook you will inevitably perform a device twin update. This means you will receive an update of the output of `useDeviceTwin`
{% endhint %}

#### Example

```jsx
const patchDesiredProperties = usePatchDesiredProperties('simulated-device');

const handleClick = () => {
    patchDesiredProperties({
        temperature: 21
    });
}

return <button onClick={() => handleClick()}>Update desired properties</button>
```

## useD2CMessages

```typescript
const lastMessage = useD2CMessages(deviceId, onData, onGrantError);
```

#### Arguments

| Argument     | Description                                                                                 | Type                                      |          |
| ------------ | ------------------------------------------------------------------------------------------- | ----------------------------------------- | -------- |
| deviceId     | The device ID of the device you want to subscribe to.                                       | `string`                                  | Required |
| onData       | Callback, executed when the device sends a new message.                                     | `(data: Record<string, unknown>) => void` | Optional |
| onGrantError | Callback, executed when the `grantRequestFunction` fails to grant the subscription request. | `GrantErrorCallback`                      | Optional |

#### Return Value

This hook returns an object: `Record<string, unknown>`

We assume that every message a device sends will be an object. The return value of this hook will always be the last message sent by the device.

## Final Note

The hooks provided by ux4iot-react are using a specific authorization mechanism. They are designed to provide the easiest API to cover your use-case and hide the most complexity possible. There are two callbacks that are available on (almost) every hook.

#### `onData`

A convenient callback to have a custom callback whenever data is received. You will receive updates of subscription hooks mostly over the return value. However, if you want to use custom logic whenever an update is received you would need to use custom hooks to listen for these changes like this:

```jsx
const value = useX(deviceId, ...);

useEffect(() => {
   console.log('Update to value detected')
}, [value]);
```

Therefore `onData` as function in subscription hooks, removes the burden of you needing to decide when to notice value changes.

#### `onGrantError`

This callback exists on every hook. The purpose of this callback is to inform you about errors that the custom `grantRequestFunction` returns. The `grantRequestFunction` is something that you need to implement yourself when you want to use ux4iot in production. The purpose of this function is to determine whether you as a user of the react application have the permission to subscribe to telemetry / device twin / connection state or perform a direct method / desired property patch.

Read more about this [here](../implementing-your-custom-security-backend/implementing-the-security-backend.md).

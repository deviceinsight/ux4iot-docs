---
description: Clarifications on the concepts ux4iot uses internally
---

# How Ux4iot works

Ux4iot serves as a consumer of an IoTHub / EventHub, providing an API to subscribe to the received data without needing to worry about subscription handling.

Ux4iot was built for the purpose to easily subscribe to device data that arrives at an EventHub in your frontend.

Meaning, once you have an EventHub and connect it with your Ux4iot, subscribing to telemetry data in your frontend will then become as easy as writing.

```
const telemetry = useTelemetry('my-device', 'my-telemetry-key')
```

While this is the primary use-case, a lot of additional features are built into ux4iot like:

* last value storage
* multi subscription handling
* security mechanisms so you can ensure only authorized users can subscribe to specific devices and telemetry
* connection state management

When ux4iot consumes a message from an EventHub it will figure out what kind of message it is. There are 3 types of messages:

* Connection State Messages
* Device Twin Update Messages
* Telemetry Messages

Ux4iot then persists telemetry, connection state and device twin as last values and publishes the messages according to the registered subscriptions.

## Sessions, Grants & Subscriptions

A **session** is an object that stores its ID, grants and subscriptions. Any Frontend that uses ux4iot-react and has setup a Ux4iotProvider will get a sessionId, to register subscriptions.

A **grant** is an authorization of a session to publish data. There are 6 types of Grants:

* DeviceTwinGrant&#x20;
* TelemetryGrant&#x20;
* DirectMethodGrant&#x20;
* ConnectionStateGrant&#x20;
* DesiredPropertyGrant&#x20;
* D2CMessageGrant

So if a session has a TelemetryGrant for device id \`my-device\` and telemetryKey \`temperature\`, this means that this session is allowed to publish this data to the subscriber if it arrives over the EventHub. The grants "DirectMethodGrant" and the "DesiredPropertyGrant" are to authorize requests when you are using an IoTHub and you want to change the desired properties of a device twin or execute a direct method on a device.

A **subscription** is a registration within a session to actively subscribe to data. When a session has a grant for Telemetry, it means it can potentially publish telemetry to a subscriber. The subscription tells ux4iot that it should publish data to a subscriber. There are 4 types of Subscriptions:

* TelemetrySubscription
* DeviceTwinSubscription
* ConnectionStateSubscription
* D2CMessageSubscription

{% hint style="info" %}
Notice that for each subscription, there is an equivalent Grant that needs to be issued to ux4iot before being able to subscribe.
{% endhint %}

## Subscription Flow

Ux4iot generally subscribes to all data that is sent to an eventhub.

When you want to subscribe to this data, you will have a setup similar to:

* EventHub -> Ux4iot <-> Ux4iot Security Backend <-> Frontend

The Frontend wants to subscribe to data. The following steps are made before this is possible:

* The frontend want to subscribe to device \`my-device\` on telemetry \`temperature\`.
* The frontend opens a new session with ux4iot and receives a sessionId. This will also open a new websocket from ux4iot-server to the frontend. This sessionId will be included in all further requests to the security backend or ux4iot-server directly.
* The frontend issues a telemetry grant request to a security backend (written by you), for \`my-device\` and telemetry key \`temperature\`
* The security backend decides whether or not the user in the frontend is authorized to subscribe to this data
* If the security backend denies the request, an error is returned to the frontend, to tell the user that there are missing authorities.
* If the security backend approves the request, it forwards the GrantRequest to the ux4iot-server API to add the GrantRequest to the session with the \`sessionId\`.
* The security backend returns a successful state to the frontend.
* The frontend sends a last value request to ux4iot-server. Since the Grant Request to ux4iot has been registered, the request can be now done directly to ux4iot-server, without asking the security backend first.
* The frontend receives the last value or 404 if there is no last value for \`my-device\` and \`temperature\`
* The frontend sends a subscription request to ux4iot-server. Since the Grant Request to ux4iot has been registered, the request can be now done again directly to ux4iot-server, without asking the security backend first.
* After the subscription request has been registered in the session object for the sessionId in ux4iot, every time ux4iot receives a telemetry message for \`my-device\` with a value for \`temperature\` it will be published to the opened websocket.&#x20;

This is the flow for telemetry. The features of the frontend library "ux4iot-react" include hooks to subscribe to multiple telemetry keys and connection states on a single device. If you use an IoTHub there are hooks to patch desired properties on a device twin, send direct methods or subscribe to device twins.

{% hint style="info" %}
The security backend is highly recommended in a production environment. For development purposes, you can use the Admin Connection String in your frontend to test the data subscription.
{% endhint %}

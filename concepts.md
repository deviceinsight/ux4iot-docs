# Concepts

The ux4iot serves as an extension for an EventHub or IoTHub to enable you to easily subscribe to your devices data in your frontend. However, there are some concepts within a IoT architecture that are opinionated.&#x20;

## Device ID

In an IoT project you can have the following scenarios:

* Every device sends their telemetry on its own and is registered within the devices of the IoT Hub.
* Devices are in a private network and send their data to a "Gateway", an IPC for example, that then has an outgoing connection to the IoT Hub.&#x20;
* Data is pulled from a server or sent from a third party service (Another backend, an OPCUA server, etc.) in specific intervals. The data is accumulated and then sent to an Event Hub&#x20;

In all of these scenarios, there should be a point in your application where you are able to collect messages correlated to a single device. At this point, you will have an identifier called the \`deviceId\` to identify messages belonging to a "device". In ux4iot the \`deviceId\` is used to manage subscriptions, last values and IoT Hub operations like direct methods and device twins.

## Connection State

The connection state of a device tells you whether or not a device is "online" or "offline". In IoT projects, this concept is a little bit more complicated.

You can define "online" as: "The device exists and is currently connected to an IoT Hub".

You can define "offline" as "The device exists and is currently not connected to an IoT Hub".

A device that does not exist cannot have any connection state. It would be misleading to call a non-existing device "offline".

In ux4iot there are multiple configurations built around the connection state information. In scenarios where the devices do not directly send their messages but use an intermediate gateway, we cannot rely on the IoTHub to give us their connection state. This is why ux4iot defines the connection state in the following way:

<div data-full-width="true">

<figure><img src=".gitbook/assets/connection state ux4iot.drawio.png" alt=""><figcaption></figcaption></figure>

</div>

The connection state logic of ux4iot works for most use cases. However with the configuration variables for CUSTOM\_CONNECTION\_STATE\_KEY and CONNECTION\_STATE\_ON\_TELEMETRY you have the option of implementing your own connection state logic that your project needs.

&#x20;

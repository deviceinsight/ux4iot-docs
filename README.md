# Introduction

### What is ux4iot?

ux4iot is a tool for directly communicating with your IoT devices from your web frontend.

{% hint style="danger" %}
ux4iot is not released yet and currently in a closed beta. If you are interested in participating, send a mail to [hello@ux4iot.com](mailto:hello@ux4iot.com).
{% endhint %}

### General architecture

![](<.gitbook/assets/ux4iot-architecture (1).png>)

With ux4iot your frontend gets access to Azure IoT Hub's communication primitives without having a custom-built backend middleware translating between IoT Hub and your user interface. No need to design a REST API so that your UI can offer IoT functionality.

The permission logic (which users can perform which actions on which devices) is separated out into a slim backend service that you provide. In this service you focus solely on the permission logic without dealing with any of the communication-related parts - those are handled by ux4iot.

ux4iot is deployed as a Managed Application in your Azure subscription. This means that you have your own dedicated instance of ux4iot and your IoT data does not leave your Azure subscription.

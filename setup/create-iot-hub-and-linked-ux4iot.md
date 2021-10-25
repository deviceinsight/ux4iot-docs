# Create IoT Hub and linked ux4iot

When you do want to use an existing IoT Hub, you can also create an IoT Hub, a ux4iot instance and link them together right from the start. \
\
The easiest way to do this is to push this button:\
&#x20;[![](../.gitbook/assets/deploy-to-azure.png) ](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fdeviceinsight%2Fux4iot-quickstart%2Fmaster%2Fquickstart.json)\
([GitHub repo](https://github.com/deviceinsight/ux4iot-quickstart) for the deployed ARM template)

{% hint style="warning" %}
**Please select one of the following Azure Regions as otherwise the deployment will fail:**

* Australia East
* Australia Southeast
* East US
* West US 2
* West Europe
* North Europe
* Canada Central
* Canada East
{% endhint %}

The resulting instance of ux4iot will already be configured with the necessary credentials to access the created IoT Hub.

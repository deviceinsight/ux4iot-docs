# Quickstart

{% hint style="info" %}
These quickstarts do not include a custom security backend, so you only have to develop in the frontend and only do configuration in the backend.
{% endhint %}

### Quickstart with existing IoT Hub and device

If you have an existing IoT hub and devices, perform the following steps

* [Create your ux4iot instance](setup/create-ux4iot-instance.md) \(10 Minutes\)
* [Configure your IoT Hub](setup/configure-your-iot-hub.md) \(5 Minutes\)
* [Bootstrap your React application, add your first ux4iot hook](using-react/tutorial-using-create-react-app.md) \(10 Minutes\)

### Quickstart with a new IoT Hub and simulated device

If you want to deploy a new IoT Hub for trying out ux4iot, you do this:

* Create a new IoT Hub and ux4iot instance \(10 Minutes\)  
  The easiest way to do this is to push this button:  
   [![](.gitbook/assets/deploy-to-azure.png) ](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fdeviceinsight%2Fux4iot-quickstart%2Fmaster%2Fquickstart.json)  
  \([GitHub repo](https://github.com/deviceinsight/ux4iot-quickstart) for the deployed ARM template\)

  
  **Please select one of the following Azure Regions as otherwise the deployment will fail:**

  * Australia East
  * Australia Southeast
  * East US
  * West US 2
  * West Europe
  * North Europe
  * Canada Central
  * Canada East

* [Bootstrap your React application, add your first ux4iot hook, send simulated data](using-react/tutorial-using-create-react-app.md) \(15 Minutes\)




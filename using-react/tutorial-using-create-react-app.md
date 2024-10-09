---
description: Build a simple app using ux4iot in development
---

# Tutorial using create-react-app

## Setup application

Use [create-react-app](https://github.com/facebook/create-react-app) to bootstrap your React application:

```bash
npx create-react-app my-iot-app
cd my-iot-app
```

Add the dependency:

```bash
npm install ux4iot-react
```

Edit the file `src/App.js` and add the imports:

```javascript
import {Ux4iotContextProvider, useTelemetry} from "ux4iot-react";
```

At the top, add the initialization of the ux4iot instance:

```javascript
const UX4IOT_ADMIN_CONNECTION_STRING = 'YOUR_ADMIN_CONNECTION_STRING';
```

You can retrieve the connection string from the Azure Portal:

![](<../.gitbook/assets/image (1) (1).png>)

![Copy either the "Primary" or "Secondary" connection string](<../.gitbook/assets/image (18).png>)

{% hint style="info" %}
Use `.env` and `.env.local` files to store your app's environment variables. Read more about that in [create-react-app's section on environment variables](https://create-react-app.dev/docs/adding-custom-environment-variables/)
{% endhint %}

Replace the existing `App` component with this:

```javascript
function App() {
  return (
    <div className="App">
      <Ux4iotContextProvider 
          options={{ adminConnectionString: UX4IOT_ADMIN_CONNECTION_STRING }}
      >
          <MyView />
      </Ux4iotContextProvider>
    </div>
  );
}
```

By creating the Context here, all sub-components (like `MyView`) can use the ux4iot hooks. Now, add the `MyView` component:

```javascript
const MyView = props => {
    const temperature = useTelemetry('simulated-device', 'temperature');
    return <div>{temperature}</div>;
}
```

Your `App.js` should now look like this:

```javascript
import './App.css';
import {Ux4iotContextProvider, useTelemetry} from "ux4iot-react";

const UX4IOT_ADMIN_CONNECTION_STRING = 'YOUR_ADMIN_CONNECTION_STRING';

const MyView = props => {
    const temperature = useTelemetry('simulated-device', 'temperature');
    return <div>{temperature}</div>;
}

function App() {
  return (
    <div className="App">
      <Ux4iotContextProvider
          options={{ adminConnectionString: UX4IOT_ADMIN_CONNECTION_STRING }}
      >
          <MyView />
      </Ux4iotContextProvider>
    </div>
  );
}

export default App;
```

As usual with `create-react-app` you can start the application with:

```bash
npm start
```

{% hint style="info" %}
If you use your admin connection string in the frontend, there will be a notification in your browsers console that you're using ux4iot-react in development mode. In order to use ux4iot-react in production mode, you will need to provide your own security backend as explained in the next section.
{% endhint %}

## Send simulated data

If you do not already have an IoT devices sending data, you can easily simulate one. First, create a device with device ID `simulated-device` in the IoT Hub:

![](<../.gitbook/assets/image (3).png>)

![](<../.gitbook/assets/image (6).png>)

Now copy the connection string for the device.

![](<../.gitbook/assets/image (15).png>)

With the connection string you can start a simulator using Docker by invoking the following command. (The GitHub repo of the simulator can be found [here](https://github.com/stefan-hudelmaier/simulated-temperature-sensor).)

```bash
docker run --rm -ti \
  -e DEVICE_CONNECTION_STRING="HostName=xxx.azure-devices.net;DeviceId=simulated-device;SharedAccessKey=xxx" \
  ghcr.io/stefan-hudelmaier/simulated-temperature-sensor:main
```

This will publish a random value of the `temperature` telemetry. The messages look like this:

```bash
{
  "temperature": 42.1
}
```

You should now see the value reflected in your React application.

---
description: Build a simple app using ux4iot in development
---

# Tutorial using create-react-app

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
import {Ux4iotContext, useSingleTelemetry} from "ux4iot-react";
```

At the top, add the initialization of the ux4iot instance:

```javascript
const UX4IOT_ADMIN_CONNECTION_STRING = 'YOUR_ADMIN_CONNECTION_STRING';
```

You can retrieve the connection string from the Azure Portal:

![](../.gitbook/assets/image%20%281%29.png)

{% hint style="info" %}
Use `.env` and `.env.local` files to store your apps environment variables. Read more about that in [create-react-app's section on environment variables](https://create-react-app.dev/docs/adding-custom-environment-variables/)
{% endhint %}

Replace the existing `App` component with this:

```javascript
function App() {
  return (
    <div className="App">
      <Ux4iotContext.Provider 
          options={{ adminConnectionString: UX4IOT_ADMIN_CONNECTION_STRING }}
      >
          <MyView />
      </Ux4iotContext.Provider>
    </div>
  );
}
```

By creating the Context here, all sub-components \(like `MyView`\) can use the ux4iot hooks. Now, add the `MyView` component:

```javascript
const MyView = props => {
    const temperature = useSingleTelemetry('simulated-device', 'temperature');
    return <div>{temperature}</div>;
}
```

Your `App.js` should now look like this:

```javascript
import './App.css';
import {Ux4iotContext, ux4iot, useSingleTelemetry} from "ux4iot-react";
import ReactDOM from "react-dom";

const UX4IOT_ADMIN_CONNECTION_STRING = 'YOUR_ADMIN_CONNECTION_STRING';

const MyView = props => {
    const temperature = useSingleTelemetry('simulated-device', 'temperature');
    return <div>{temperature}</div>;
}

function App() {
  return (
    <div className="App">
      <Ux4iotContext.Provider
          options={{ adminConnectionString: UX4IOT_ADMIN_CONNECTION_STRING }}
      >
          <MyView />
      </Ux4iotContext.Provider>
    </div>
  );
}

export default App;

```

As usual with `create-react-app` you can start the application with:

```bash
npm start
```

As soon as you send in data as `simulated-device` using the IoT Hub SDK, the displayed number will update.

{% hint style="info" %}
If you use your admin connection string in the frontend, there will be a notification in your browsers console that you're using ux4iot-react in development mode. In order to use ux4iot-react in production mode, you will need to provide your own security backend as explained in the next section.
{% endhint %}


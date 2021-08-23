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
import {Ux4iotContext, ux4iot, useTelemetry} from "ux4iot-react";
```

At the top, add the initialization of the ux4iot instance:

```javascript
const UX4IOT_ADMIN_CONNECTION_STRING = 'HostName=;';
const ux4iot = ux4iot.initDevMode(UX4IOT_ADMIN_CONNECTION_STRING);
```

You can retrieve the connection string from the Azure Portal:

![](../.gitbook/assets/image%20%281%29.png)

Replace the existing `App` component with this:

```javascript
function App() {
  return (
    <div className="App">
      <Ux4iotContext.Provider value={ux4iot}>
          <MyView />
      </Ux4iotContext.Provider>
    </div>
  );
}
```

By creating the Context here, all sub-components \(like `MyView`\) can use the ux4iot hooks. Now, add the `MyView` component:

```javascript
const MyView = props => {
    const temperature = useTelemetry('simulated-device', 'temperature');
    return <div>{temperature}</div>;
}
```

Your `App.js` should now look like this:

```javascript
import './App.css';
import {Ux4iotContext, ux4iot, useTelemetry} from "ux4iot-react";
import ReactDOM from "react-dom";

const UX4IOT_ADMIN_CONNECTION_STRING = 'HostName=;';
const ux4iot = ux4iot.initDevMode(UX4IOT_ADMIN_CONNECTION_STRING);

const MyView = props => {
    const temperature = useTelemetry('simulated-device', 'temperature');
    return <div>{temperature}</div>;
}

function App() {
  return (
    <div className="App">
      <Ux4iotContext.Provider value={ux4iot}>
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


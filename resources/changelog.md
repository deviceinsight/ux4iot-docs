# Changelog

## Version 4.2.0

* Migrate custom resource backend from Azure Function to Container Apps
* Remove Azure Function (Plan and Function app)
* Remove restart button
* Remove now superfluous cold start prevention via regular pings
* Publish mainTemplate.bicep to the `ux4iot-shared` storage account. This can be used as an alternative to Managed App deployments.

## Version 4.1.5

* Publish connection state when device does offline due to not sending data (UX4IOT-274).

## Version 4.1.4

Fix bug in config handling regarding `CUSTOM_CONNECTION_STATE_KEY.`

## Version 4.1.0

* If customConnectionStateKey is set, getting the last value for connection state will not request the iothub for the last connection state.

## Version 4.0.0

* In this release, we changed the infrastructure of ux4iot to use Azure Container Apps instead of Azure Container Instances. This change was necessary because of Azure Container Instances being very unreliable in the past. We experienced bugs that caused the ux4iot container to not be available, not deployable and containers randomly terminating and restarting. Therefore we want to switch to azure container apps. This also allows us to better scale containers, since the backbone of container apps is kubernetes.
* The downside to this is switching to container apps hosts the container in a new environment, which results in a new connection string. We provide a migration guide that will help to switch to the new version as smooth as possible.
* A new feature for restarting the ux4iot from the application screen in the portal made it necessary to add a permission during the ux4iot deployment. This means that you need to be Owner of the resource group that you deploy ux4iot in.

### Important&#x20;

In the past we had troubles aligning the versions of these ux4iot modules, especially when a change on one module was not backwards compatible and had effects on the other modules. This resulted in situations like: version 3.2.0 in ux4iot-react is not compatible with ux4iot-server 3.5.0 but compatible with ux4iot-server 3.4.0. ux4iot-react however had no changes. Therefore, starting with 4.0.0 we will always align versions of

* ux4iot-server
* ux4iot-react
* ux4iot-admin-node

### Features

* _breaking_ Switch to Azure Container Apps (see migration guide)
* Fix iothub DeviceNotFound errors and adjust connection state logic to be more robust. See new documentation page "Connection State"
* Add new HTTP endpoint GET /status to return the status of the ux4iot service
* Add log analytics workspace based application insights. This includes a new configuration parameter "logAnalyticsTracesTableTier" with values "Basic" and "Analytics"
* Add restart button for ux4iot users
* Add status button for ux4iot apps
* Fix a bug in ux4iot-react resulting in false connection states for devices
* Remove traefik container
* Update all libraries used in ux4iot-server to the latest version
* Add a potential bugfix for message loss of telemetry messages when consuming from IoTHub built-in eventhub (cbs endpoint timeout).
* Thoroughly update the documentation and drop documentation for 3.x versions.

### Migration Guide to switch to Container Apps

We recommend doing creation and modification of services in your bicep files.

1. Create a new consumer group in the eventhub that you are consuming messages from
2. Deploy ux4iot-containerapps managed application with the same config parameters as the old ux4iot managed application except for the new consumer group, the service name and the managedGroupId.
3. Copy the connection string of your new ux4iot service by navigating to the service in the portal and clicking on Admin Connection Strings in the sidebar.
4. Execute the migration script [migrate-redis.py](changelog.md#migration-redis.py) to transfer your last value file from the old ux4iot to the new one. If you lack permissions and you want all last values from your old 3.x ux4iot transferred to your new ux4iot send us a message.
5. Replace all occurrences of the old connection string with the new one in your application (function apps, frontends, docker containers, etc.)
6. Verify that all functionality of your old ux4iot works in the new one (receive telemetry and connection states, device twins, direct methods, etc.)
7. After everything works with the new ux4iot delete the old ux4iot service from the resource group. You are now running ux4iot 4.0

#### migration-redis.py

{% file src="../.gitbook/assets/migrate-redis.py" %}

## Version 3.6.1

**Fixes**

* Include the telemetry key in the actual telemetry message when it is used as the customConnectionState key

## Version 3.6.0

**Features & Fixes**

* Add support for custom connectionStateKey
* Disable smart app insights rules
* Fix subscriptions endpoints not accepting empty list of subscription requests

**Update subrepositories**

* ux4iot-react@3.4.0

## Version 3.5.0

**Features**

* Add new endpoints
  * PUT `subscriptions` Bulk subscribe to telemetry, deviceTwin or connectionState
  * DELETE `subscriptions` Bulk unsubscribe to telemetry, deviceTwin or connectionState
* Enable shared-access-key to be used in lastValue endpoints

**Update subrepositories accordingly**

Compatible endpoints to ux4iot@3.5.0:

* ux4iot-react@3.3.0
* ux4iot-admin-node@3.1.0

## Version 3.4.0

* Send warning, error logs to Application Insights

## Version 3.3.0

* Use latest commit as default version
* **Remove backwards compatibility for ux4iot v2. (Remove publishing of last values over websocket after grant was added)**

## Version 3.2.1

* Fix bug where connectionState was not published

## Version 3.2.0

* Add option connectionStateOnTelemetry to enable/disable a connection state update whenever a telemetry message is received (enabled by default)

## Version 3.1.0

* Fixed bug where the ux4iot instance was in a broken state, because the custom resource's function app for the managed application was not deployed correctly
* Update all dependencies of ux4iot-server and submodules
* Revert cache to work with ux4iot 2.0 timestamps to ensure backwards compatibility of the redis cache

## Version 3.0.0

**Features**

The subscription flow was updated. Previously, whenever a grant was added, ux4iot began to publish messages to a room, specific to the grant data. Now adding a grant does nothing other than telling ux4iot that a specific session **has the permission to subscribe to SD (SD = telemetry, connection state, device twin, d2c messages)** This breaking change also changes the way the client's websocket receives messages for telemetry. Previously all telemetry in a device's message was split by all keys and for each telemetry key, a single message was published. Now, only one message per device will be published for all subscribed telemetry of that device. A client will therefore just receive one message per device and per connection state, d2c message, devicetwin or telemetry.

* _**breaking**_ Request to PUT /grant endpoint no longer subscribe to SD
* _**breaking**_ Change grant request type parameter key from "grantType" to "type"
* _**breaking**_ Change grant request type parameter values from
  * subscribeToTelemetry -> telemetry
  * subscribeToConnectionState -> connectionState
  * subscribeToDeviceTwin -> deviceTwin
  * subscribeToD2CMessages -> d2cMessages
  * modifyDesiredProperties -> desiredProperties
  * invokeDirectMethod -> directMethod
* Add new endpoint PUT /subscription to subscribe to SD which depends on grants
* Add new endpoint DELETE /subscription to unsubscribe from SD which depends on grants
* Add unit test cases for state management in ux4iot
* Make parameter 'telemetryKey' in GET /lastValue/:deviceId/:telemetryKey optional, omitting it will return all last values for the given device
* Add GET /deviceTwin/:deviceId endpoint to retrieve the last received device twin
* Add GET /connectionState/:deviceId endpoint to retrieve the last received connection state
* ux4iot-admin-node
  * _breaking_ Change methodname 'revokeAll' to 'revokeAllSessions'
  * Add methods for endpoints
    * subscribe -> PUT /subscription
    * unsubscribe -> DELETE /subscription
    * invokeDirectMethod -> POST /directMethod
    * getLastTelemetryValues -> GET /lastValue/:deviceId/:telemetryKey
    * getLastDeviceTwin -> GET /deviceTwin
    * getLastConnectionState -> GET /connectionState
    * patchDesiredProperties -> PATCH /deviceTwinDesiredProperties
* ux4iot-react Complete refactoring of internal ux4iot-react subscription logic. Ux4iot 3.0 delivers telemetry messages in a new way. It will aggregate all subscribed telemetry in one message. Ux4iot-react will distribute these messages over all used hooks. Ux4iot-react 3.0 will use the new subscription mechanism for ux4iot 3.0 in that it uses separate requests for grants and subscriptions. During these changes, a lot of types were changed, which then resulted in breaking changes. These changes however are very minor so there won't be much effort to update from 2.x to 3.0.

Overview of changes:

*   Unify all message callbacks in hooks

    ```ts
    export type MessageCallbackBase<T> = (
      deviceId: string,
      data: T | undefined,
      timestamp: string
    ) => void;

    export type TelemetryCallback = MessageCallbackBase<Record<string, unknown>>;
    export type DeviceTwinCallback = MessageCallbackBase<TwinUpdate>;
    export type ConnectionStateCallback = MessageCallbackBase<boolean>;
    export type D2CMessageCallback = MessageCallbackBase<Record<string, unknown>>;
    ```
* _**breaking**_ useConnectionState `onData: (connectionState: boolean) => void` - changed to `onData: ConnectionStateCallback`
* _**breaking**_ useD2CMessages `onData: (data: T, timestamp: string) => void` - changed to `onData: D2CMessageCallback`
* _**breaking**_ useDeviceTwin `onData: (twin: Twin) => void` - changed to `onData: DeviceTwinCallback`
* _**breaking**_ useMultiTelemetry `onData: (deviceId: string, telemetryKey: string, telemetryValue: unknown, timestamp: string | undefined) => void` - changed to `onData: TelemetryCallback`
* _**breaking**_ useTelemetry `onData<T>: (data: T, timestamp: string | undefined) => void` - changed to `onData<T>: MessageCallbackBase<T>`
* _**breaking**_ Rename type RawD2CMessageCallback to D2CMessageCallback
* _**breaking**_ useConnectionState is now returning `boolean` instead of `{connected: boolean}`

If you're not using onData callbacks, you shouldn't have any breaking changes.

* Add useMultiConnectionState hook
* Add `onSubscriptionError` callback, firing when there are errors on posting requests to subscribe to ux4iot data
* Update ux4iot-shared types to updated ux4iot 3.0 types
* Add typeguards for all message types
* Add separate state handling in ux4iot-react

## Version 2.0.0

**Breaking**

* Rename customTimestampProperty to customTimestampKey

**Misc**

* Changed info log statements that were debug level to debug&#x20;
* Add new setting customDeviceIdKey to be able to set a custom key in messages to be used as deviceId

## Version 1.7.0

* Make it possible to disable TTL for connection cache
* Add parameter `throttlingParameter` to specify the number of milliseconds with which to throttle the telemetry updates sent via websockets. Set this to -1 to disable throttling. This is the default.
* Add special branch `experimental` from which the app definition `ux4iot-experimental` is updated.

## Version 1.6.0

* The connection state received via Event Hub / IoT Hub is cached. This makes it possible to use the `useConnectionState` hook, even if no IoT Hub is used, as you can simulate the connected/disconnected messages using an Event Hub
* Add parameter `customTimestampProperty` with default value `_ts` so that the timestamp can optionally be passed as part of the body of a message. You can still continue to use the message properties
* Add parameter `connectionStateCacheTTL`. This indicates the number of seconds that the connection state should be cached. You can set it to `0` to set the time-to-live to infinity. The default value is `60`
* Fix inconsistencies regarding contents of device twin.

## Version 1.5.0

* Add persistence of complex telemetry values
* Reduce Azure infrastructure costs: Application Insights
* Fix a problem with too low max open file limit in reverse proxy

## Version 1.4.0

* Reduce Azure infrastructure costs: Storage Accounts

## Version 1.3.0

* Reduce Azure infrastructure costs: Application Insights, Storage Accounts

## Version 1.2.1

* ARM Template improvements

## Version 1.2.0

* Add support for timestamps
* Add parameters for ARM template:
  * Add SKUs (small, standard) to make less cost-intensive instances possible (`sku`)
  * Make it possible to inject the primary and secondary secrets (`primaryAdminSecret`, `secondaryAdminSecret`)
  * Make the log level configurable (`logLevel`)

## Version 1.1.0

* The consumer group to use for reading from Event Hub or IoT Hub can be configured
* Slightly improved the wording and detail in the creation screen
* Fix an issue with `patchDesiredProperties`
* Add a UI for manual testing. Is deployed [here](https://ux4iotsnapshotstorage.z6.web.core.windows.net/).
* Fix issues with using ux4iot without an IoT Hub, i.e. only using an Event Hub
* Improve memory attribution between containers
* The DNS label can not be overwritten with the parameter `dnsLabelOverride`
* The custom sub-resource pages for the admin connection strings and websocket url load much faster now

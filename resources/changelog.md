# Changelog

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
* Add a UI for manual testing. Is deployed [here](https://ux4iotsnapshotstorage.z6.web.core.windows.net).
* Fix issues with using ux4iot without an IoT Hub, i.e. only using an Event Hub
* Improve memory attribution between containers
* The DNS label can not be overwritten with the parameter `dnsLabelOverride`
* The custom sub-resource pages for the admin connection strings and websocket url load much faster now

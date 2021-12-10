# Changelog

## Version 1.1.0

* The consumer group to use for reading from Event Hub or IoT Hub can be configured
* Slightly improved the wording and detail in the creation screen
* Fix an issue with `patchDesiredProperties`
* Add a UI for manual testing. Is deployed [here](https://ux4iotsnapshotstorage.z6.web.core.windows.net).
* Fix issues with using ux4iot without an IoT Hub, i.e. only using an Event Hub
* Improve memory attribution between containers
* The DNS label can not be overwritten with the parameter `dnsLabelOverride`
* The custom sub-resource pages for the admin connection strings and websocket url load much faster now

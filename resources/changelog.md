# Changelog

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

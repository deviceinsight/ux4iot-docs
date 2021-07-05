# Create your Subioto Instance

Subioto is installed in your Azure subscription as a Managed Application. 

### TODO

* Create using Portal UI
* Create using command line

Specifying the Event Hub compatible connection is required. Also configuring the service connection string is optional. It is necessary for the following hooks:

* `useDirectMethod`
* `usePatchDesiredProperties`

In effect, everything that not only consumes information but accesses the devices in some way.


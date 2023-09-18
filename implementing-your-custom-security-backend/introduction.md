# Introduction

In a production setting, you do not want every user being able to subscribe to every device, execute every direct method and update every device twin. However, you are the only one to know which user is authorized to subscribe to devices or even just subscribe to a single telemetry.

ux4iot is designed to handle all subscription use cases in your application and additionally support your custom authorization logic.

In order to authorize requests and to enforce the access control policies and permission logic of your application, you need to provide a custom security backend. This backend must run in the cloud, as it contains the credentials for accessing the ux4iot Admin API.

You can use any programming language or runtime environment for your backend, for example:

* Azure Functions
* AWS Lambda
* A virtual machine
* A pod in an Kubernetes cluster

As you most likely already have a backend API for your IoT application, it's probably a good idea to add the security endpoint to your existing ones.

The currently is an Admin SDK for the following languages:

* [Javascript / Typescript](broken-reference)

If you want to use other languages you can use the [REST API](admin-rest-api.md).

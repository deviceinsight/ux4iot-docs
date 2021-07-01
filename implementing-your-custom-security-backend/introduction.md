# Introduction

In order to authorize requests and to enforce the access control policies and permission logic of your application, you need to provide a custom security backend. This backend must run in the cloud, as it contains credentials for accessing the Subioto Admin API.

You can use any programming language or runtime environment for your backend, for example:

* Azure Functions
* AWS Lambda
* A virtual machine
* A pod in an Kubernetes cluster

As you most likely already have a backend API for your IoT application, it's probably a good idea to add the security endpoint to your existing ones.

The currently is an admin SDK for the following languages:

* Javascript / Typescript

If you want to use other languages you can use the REST API.




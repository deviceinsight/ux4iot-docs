# Admin REST API

If you are using a language for the security backend for which no SDK exists, you can use the REST API. Don't worry, it's really simple.

{% api-method method="post" host="https://subioto-xyz.westeurope.azurecontainer.io/" path="api/v1/grants" %}
{% api-method-summary %}
Forward grants
{% endapi-method-summary %}

{% api-method-description %}
Send a grant request to Subioto to apply it for the `sessionId` contained in the grant 
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="X-User-Id" type="string" required=false %}
Your custom identifier for users to pass along as meta-information. If you pass along this identifier, you can remove all sessions with the same user id, e.g. if a user logs out.
{% endapi-method-parameter %}

{% api-method-parameter name="Authorization" type="string" required=true %}
The basic authentication credentials
{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-body-parameters %}
{% api-method-parameter name="details" type="string" required=false %}
Further details of the grant, depends on the grantRequestType
{% endapi-method-parameter %}

{% api-method-parameter name="deviceId" type="string" required=true %}
The IoT Hub device ID
{% endapi-method-parameter %}

{% api-method-parameter name="sessionId" type="string" required=true %}
The sessionId for which the grant is requested
{% endapi-method-parameter %}

{% api-method-parameter name="grantRequestType" type="string" required=true %}
Can be one of 'telemetry', 'directMethod', ...
{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=204 %}
{% api-method-response-example-description %}
The grant was accepted and applied
{% endapi-method-response-example-description %}

```
NO CONTENT
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
There was something wrong with the grant, it has not been applied
{% endapi-method-response-example-description %}

```
{
  "errorMessage": "Required field 'sessionId' is missing"
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=401 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
{
  "errorMessage": "The provided credentials are invalid"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

**Example request**

```javascript
{
  "grantRequestType": "telemetry",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123",
  "details":  {
    "telemetryKey": "temperature"
  }
}
```

{% api-method method="delete" host="https://subioto-xyz.westeurope.azurecontainer.io/" path="api/v1/sessions/:sessionId" %}
{% api-method-summary %}
Delete sessions
{% endapi-method-summary %}

{% api-method-description %}
Remove a session, including all grants
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="sessionId" type="string" required=false %}

{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="Authorization" type="string" required=true %}
The basic authentication credentials
{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=204 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
NO CONTENT
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
{
  "errorMessage": "The session was not found"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="delete" host="https://subioto-xyz.westeurope.azurecontainer.io/" path="api/v1/users/:userId/sessions" %}
{% api-method-summary %}
Delete all user sessions
{% endapi-method-summary %}

{% api-method-description %}
Remove all sessions of a particular user identified by his or her user ID. Useful when a particular user logs out of your system.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="userId" type="string" required=true %}
The userId of the user
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="Authentication" type="string" required=true %}
The basic authentication credentials
{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=204 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
NO CONTENT
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
{
  "errorMessage": "The userId is unknown"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% hint style="info" %}
In order for this to work, you have to pass along the `userId` when forwarding grants.
{% endhint %}


# Admin REST API

If you are using a language for the security backend for which no SDK exists, you can use the REST API. Don't worry, it's really simple.

{% api-method method="post" host="https://ux4iot-xyz.westeurope.azurecontainer.io/" path="grants" %}
{% api-method-summary %}
Forward a grant
{% endapi-method-summary %}

{% api-method-description %}
Send a grant request to ux4iot to apply it for the `sessionId` contained in the grant.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="Shared-Access-Key" type="string" required=true %}
The Shared Access Key used for authentication
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
Can be one of 'subscribeToTelemetry', 'invokeDirectMethod', etc.
{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=204 %}
{% api-method-response-example-description %}
The grant was accepted and applied
{% endapi-method-response-example-description %}

```text
NO CONTENT
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}
There was something wrong with the grant, it has not been applied
{% endapi-method-response-example-description %}

```text
{
  "errorMessage": "Required field 'sessionId' is missing"
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=401 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```text
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
  "grantRequestType": "subscribeToTelemetry",
  "sessionId": "ht9JvTLalcy3GQDttyqu",
  "deviceId": "d123",
  "details":  {
    "telemetryKey": "temperature"
  }
}
```

For a complete list of values for`grantRequestType` see [here](implementing-the-security-backend.md).

{% api-method method="delete" host="https://ux4iot-xyz.westeurope.azurecontainer.io/" path="grants" %}
{% api-method-summary %}
Revoke a grant
{% endapi-method-summary %}

{% api-method-description %}
Revoke the grant given 
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="Shared-Access-Key" type="string" required=true %}
The Shared Access Key used for authentication
{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-body-parameters %}
{% api-method-parameter name="deviceId" type="string" required=true %}
The device for which to revoke the grant
{% endapi-method-parameter %}

{% api-method-parameter name="grantType" type="string" required=true %}
The grant type to revoke
{% endapi-method-parameter %}

{% api-method-parameter name="sessiondId" type="string" required=true %}
The session ID that the grant belongs to
{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="delete" host="https://ux4iot-xyz.westeurope.azurecontainer.io/" path="sessions/:sessionId" %}
{% api-method-summary %}
Delete a sessions
{% endapi-method-summary %}

{% api-method-description %}
Remove a session, including all grants
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="sessionId" type="string" required=true %}
The session to remove
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-headers %}
{% api-method-parameter name="Shared-Access-Key" type="string" required=true %}
The Shared Access Key used for authentication
{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=204 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```text
NO CONTENT
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```text
{
  "errorMessage": "The session was not found"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="delete" host="https://ux4iot-xyz.westeurope.azurecontainer.io/" path="sessions" %}
{% api-method-summary %}
Delete all sessions
{% endapi-method-summary %}

{% api-method-description %}
Remove all sessions
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="Shared-Access-Key" type="string" required=true %}
The Shared Access Key used for authentication
{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}


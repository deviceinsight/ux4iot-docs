# Admin REST API

If you are using a language for the security backend for which no SDK exists, you can use the REST API. Don't worry, it's really simple.

{% swagger baseUrl="https://ux4iot-xyz.westeurope.azurecontainer.io/" path="grants" method="post" summary="Forward a grant" %}
{% swagger-description %}
Send a grant request to ux4iot to apply it for the 

`sessionId`

 contained in the grant.
{% endswagger-description %}

{% swagger-parameter in="header" name="Shared-Access-Key" type="string" %}
The Shared Access Key used for authentication
{% endswagger-parameter %}

{% swagger-parameter in="body" name="details" type="string" %}
Further details of the grant, depends on the grantRequestType
{% endswagger-parameter %}

{% swagger-parameter in="body" name="deviceId" type="string" %}
The IoT Hub device ID
{% endswagger-parameter %}

{% swagger-parameter in="body" name="sessionId" type="string" %}
The sessionId for which the grant is requested
{% endswagger-parameter %}

{% swagger-parameter in="body" name="grantRequestType" type="string" %}
Can be one of 'subscribeToTelemetry', 'invokeDirectMethod', etc.
{% endswagger-parameter %}

{% swagger-response status="204" description="The grant was accepted and applied" %}
```
NO CONTENT
```
{% endswagger-response %}

{% swagger-response status="400" description="There was something wrong with the grant, it has not been applied" %}
```
{
  "errorMessage": "Required field 'sessionId' is missing"
}
```
{% endswagger-response %}

{% swagger-response status="401" description="" %}
```
{
  "errorMessage": "The provided credentials are invalid"
}
```
{% endswagger-response %}
{% endswagger %}

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

{% swagger baseUrl="https://ux4iot-xyz.westeurope.azurecontainer.io/" path="grants" method="delete" summary="Revoke a grant" %}
{% swagger-description %}
Revoke the grant given 
{% endswagger-description %}

{% swagger-parameter in="header" name="Shared-Access-Key" type="string" %}
The Shared Access Key used for authentication
{% endswagger-parameter %}

{% swagger-parameter in="body" name="deviceId" type="string" %}
The device for which to revoke the grant
{% endswagger-parameter %}

{% swagger-parameter in="body" name="grantType" type="string" %}
The grant type to revoke
{% endswagger-parameter %}

{% swagger-parameter in="body" name="sessiondId" type="string" %}
The session ID that the grant belongs to
{% endswagger-parameter %}

{% swagger-response status="200" description="" %}
```
```
{% endswagger-response %}
{% endswagger %}

{% swagger baseUrl="https://ux4iot-xyz.westeurope.azurecontainer.io/" path="sessions/:sessionId" method="delete" summary="Delete a sessions" %}
{% swagger-description %}
Remove a session, including all grants
{% endswagger-description %}

{% swagger-parameter in="path" name="sessionId" type="string" %}
The session to remove
{% endswagger-parameter %}

{% swagger-parameter in="header" name="Shared-Access-Key" type="string" %}
The Shared Access Key used for authentication
{% endswagger-parameter %}

{% swagger-response status="204" description="" %}
```
NO CONTENT
```
{% endswagger-response %}

{% swagger-response status="404" description="" %}
```
{
  "errorMessage": "The session was not found"
}
```
{% endswagger-response %}
{% endswagger %}

{% swagger baseUrl="https://ux4iot-xyz.westeurope.azurecontainer.io/" path="sessions" method="delete" summary="Delete all sessions" %}
{% swagger-description %}
Remove all sessions
{% endswagger-description %}

{% swagger-parameter in="header" name="Shared-Access-Key" type="string" %}
The Shared Access Key used for authentication
{% endswagger-parameter %}

{% swagger-response status="200" description="" %}
```
```
{% endswagger-response %}
{% endswagger %}

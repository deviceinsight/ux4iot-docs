# Admin REST API

If you are using a language for the security backend for which no SDK exists, you can use the REST API

{% api-method method="put" host="https://subioto-xyz.westeurope.azurecontainer.io/" path="api/v1/grants" %}
{% api-method-summary %}
/grants
{% endapi-method-summary %}

{% api-method-description %}
Send a grant request to Subioto to apply it for the `sessionId` contained in the grant request.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="Authorization" type="string" required=true %}
The basic authentication credentials
{% endapi-method-parameter %}
{% endapi-method-headers %}
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


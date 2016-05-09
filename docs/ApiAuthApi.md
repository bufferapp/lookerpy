# lookerpy.ApiAuthApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](ApiAuthApi.md#login) | **POST** /login | login
[**logout**](ApiAuthApi.md#logout) | **DELETE** /logout | logout


# **login**
> AccessToken login(client_id=client_id, client_secret=client_secret)

login

### Login in order to use the API. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ApiAuthApi()
client_id = 'client_id_example' # str | client_id part of API3 Key. (optional)
client_secret = 'client_secret_example' # str | client_secret part of API3 Key. (optional)

try: 
    # login
    api_response = api_instance.login(client_id=client_id, client_secret=client_secret)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiAuthApi->login: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| client_id part of API3 Key. | [optional] 
 **client_secret** | **str**| client_secret part of API3 Key. | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> str logout()

logout

### Logout of the API and invalidate the current access token. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ApiAuthApi()

try: 
    # logout
    api_response = api_instance.logout()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiAuthApi->logout: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


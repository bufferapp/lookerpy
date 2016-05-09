# lookerpy.ConnectionApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_connections**](ConnectionApi.md#all_connections) | **GET** /connections | get all connections
[**all_dialect_infos**](ConnectionApi.md#all_dialect_infos) | **GET** /dialect_info | get all dialect infos
[**connection**](ConnectionApi.md#connection) | **GET** /connections/{connection_name} | get connection
[**create_connection**](ConnectionApi.md#create_connection) | **POST** /connections | create connection
[**delete_connection**](ConnectionApi.md#delete_connection) | **DELETE** /connections/{connection_name} | delete connection
[**test_connection**](ConnectionApi.md#test_connection) | **PUT** /connections/{connection_name}/test | test existing connection
[**test_connection_config**](ConnectionApi.md#test_connection_config) | **PUT** /connections/test | test connection configuration
[**update_connection**](ConnectionApi.md#update_connection) | **PATCH** /connections/{connection_name} | update connection


# **all_connections**
> list[DBConnection] all_connections(fields=fields)

get all connections

### Get information about all connections. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConnectionApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all connections
    api_response = api_instance.all_connections(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectionApi->all_connections: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DBConnection]**](DBConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_dialect_infos**
> list[DialectInfo] all_dialect_infos(fields=fields)

get all dialect infos

### Get information about all dialects. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConnectionApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all dialect infos
    api_response = api_instance.all_dialect_infos(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectionApi->all_dialect_infos: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DialectInfo]**](DialectInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connection**
> DBConnection connection(connection_name, fields=fields)

get connection

### Get information about a connection. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConnectionApi()
connection_name = 'connection_name_example' # str | Name of connection
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get connection
    api_response = api_instance.connection(connection_name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectionApi->connection: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of connection | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DBConnection**](DBConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection**
> DBConnection create_connection(body=body)

create connection

### Create a connection using the specified configuration. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConnectionApi()
body = lookerpy.DBConnection() # DBConnection | connection (optional)

try: 
    # create connection
    api_response = api_instance.create_connection(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectionApi->create_connection: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DBConnection**](DBConnection.md)| connection | [optional] 

### Return type

[**DBConnection**](DBConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> str delete_connection(connection_name)

delete connection

### Delete a connection. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConnectionApi()
connection_name = 'connection_name_example' # str | Name of connection

try: 
    # delete connection
    api_response = api_instance.delete_connection(connection_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectionApi->delete_connection: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of connection | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection**
> DBConnectionTestResult test_connection(connection_name, tests=tests)

test existing connection

### Test an existing connection.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  Unsupported tests in the request will be ignored. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConnectionApi()
connection_name = 'connection_name_example' # str | Name of connection
tests = ['tests_example'] # list[str] | Array of names of tests to run (optional)

try: 
    # test existing connection
    api_response = api_instance.test_connection(connection_name, tests=tests)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectionApi->test_connection: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of connection | 
 **tests** | [**list[str]**](str.md)| Array of names of tests to run | [optional] 

### Return type

[**DBConnectionTestResult**](DBConnectionTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection_config**
> DBConnectionTestResult test_connection_config(body=body, tests=tests)

test connection configuration

### Test a connection configuration.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  Unsupported tests in the request will be ignored. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConnectionApi()
body = lookerpy.DBConnection() # DBConnection | Connection (optional)
tests = ['tests_example'] # list[str] | Array of names of tests to run (optional)

try: 
    # test connection configuration
    api_response = api_instance.test_connection_config(body=body, tests=tests)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectionApi->test_connection_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DBConnection**](DBConnection.md)| Connection | [optional] 
 **tests** | [**list[str]**](str.md)| Array of names of tests to run | [optional] 

### Return type

[**DBConnectionTestResult**](DBConnectionTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection**
> DBConnection update_connection(connection_name, body)

update connection

### Update a connection using the specified configuration. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConnectionApi()
connection_name = 'connection_name_example' # str | Name of connection
body = lookerpy.DBConnection() # DBConnection | connection

try: 
    # update connection
    api_response = api_instance.update_connection(connection_name, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectionApi->update_connection: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_name** | **str**| Name of connection | 
 **body** | [**DBConnection**](DBConnection.md)| connection | 

### Return type

[**DBConnection**](DBConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


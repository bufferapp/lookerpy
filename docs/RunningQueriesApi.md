# lookerpy.RunningQueriesApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_running_queries**](RunningQueriesApi.md#all_running_queries) | **GET** /running_queries | get all running queries
[**kill_query**](RunningQueriesApi.md#kill_query) | **DELETE** /running_queries/{query_slug} | Kill a running query


# **all_running_queries**
> list[RunningQueries] all_running_queries()

get all running queries

Get information about all running queries. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RunningQueriesApi()

try: 
    # get all running queries
    api_response = api_instance.all_running_queries()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RunningQueriesApi->all_running_queries: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RunningQueries]**](RunningQueries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kill_query**
> kill_query(query_slug)

Kill a running query

Kill a query with a specific slug. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RunningQueriesApi()
query_slug = 'query_slug_example' # str | query slug

try: 
    # Kill a running query
    api_instance.kill_query(query_slug)
except ApiException as e:
    print "Exception when calling RunningQueriesApi->kill_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_slug** | **str**| query slug | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


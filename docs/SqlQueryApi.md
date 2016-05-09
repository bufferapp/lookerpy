# lookerpy.SqlQueryApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sql_query**](SqlQueryApi.md#create_sql_query) | **POST** /sql_queries | create SQL Runner query
[**sql_query**](SqlQueryApi.md#sql_query) | **GET** /sql_queries/{slug} | get SQL Runner query


# **create_sql_query**
> SqlQuery create_sql_query(body=body)

create SQL Runner query

create a sql runner query

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SqlQueryApi()
body = lookerpy.SqlQuery() # SqlQuery | SQL Runner query (optional)

try: 
    # create SQL Runner query
    api_response = api_instance.create_sql_query(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SqlQueryApi->create_sql_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SqlQuery**](SqlQuery.md)| SQL Runner query | [optional] 

### Return type

[**SqlQuery**](SqlQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sql_query**
> SqlQuery sql_query(slug)

get SQL Runner query

get a sql runner query

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SqlQueryApi()
slug = 'slug_example' # str | slug of query

try: 
    # get SQL Runner query
    api_response = api_instance.sql_query(slug)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SqlQueryApi->sql_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| slug of query | 

### Return type

[**SqlQuery**](SqlQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# lookerpy.LookApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_looks**](LookApi.md#all_looks) | **GET** /looks | get all looks
[**create_look_prefetch**](LookApi.md#create_look_prefetch) | **POST** /looks/{look_id}/prefetch | create a prefetch
[**look**](LookApi.md#look) | **GET** /looks/{look_id} | get look
[**look_prefetch**](LookApi.md#look_prefetch) | **GET** /looks/{look_id}/prefetch | get a prefetch
[**run_look**](LookApi.md#run_look) | **GET** /looks/{look_id}/run/{format} | run look


# **all_looks**
> list[Look] all_looks(fields=fields)

get all looks

### Get all the looks.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.LookApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all looks
    api_response = api_instance.all_looks(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LookApi->all_looks: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Look]**](Look.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_look_prefetch**
> PrefetchLookRequestMapper create_look_prefetch(look_id, body=body)

create a prefetch

### Create a prefetch for a look with the specified information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.LookApi()
look_id = 'look_id_example' # str | Id of dashboard
body = lookerpy.PrefetchLookRequestMapper() # PrefetchLookRequestMapper | Parameters for prefetch request (optional)

try: 
    # create a prefetch
    api_response = api_instance.create_look_prefetch(look_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LookApi->create_look_prefetch: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **str**| Id of dashboard | 
 **body** | [**PrefetchLookRequestMapper**](PrefetchLookRequestMapper.md)| Parameters for prefetch request | [optional] 

### Return type

[**PrefetchLookRequestMapper**](PrefetchLookRequestMapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **look**
> LookWithQuery look(look_id, fields=fields)

get look

### Get a Look.  Return detailed information about the Look and its associated Query.  

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.LookApi()
look_id = 789 # int | Id of look
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get look
    api_response = api_instance.look(look_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LookApi->look: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Id of look | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**LookWithQuery**](LookWithQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **look_prefetch**
> PrefetchMapper look_prefetch(look_id)

get a prefetch

### Get a prefetch for a look with the specified information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.LookApi()
look_id = 'look_id_example' # str | Id of look

try: 
    # get a prefetch
    api_response = api_instance.look_prefetch(look_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LookApi->look_prefetch: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **str**| Id of look | 

### Return type

[**PrefetchMapper**](PrefetchMapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_look**
> str run_look(look_id, format, limit=limit, apply_formatting=apply_formatting, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production)

run look

### Run a Look.  Given a look id and a format, this will run the look's query and return the results.  Suported formats: - json - plain json - csv - comma separated values with a header - txt - tab separated values with a header - html - simple html - md - simple markdown - sql - shows the generated SQL rather than running the query - png - a PNG image of the visualization of the query - jpg - a JPG image of the visualization of the query - unified - json that is annotated with additional metadata as used by the Looker web application   

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.LookApi()
look_id = 789 # int | Id of look
format = 'format_example' # str | Format of result
limit = 789 # int | Row limit (may override the limit in the saved query). (optional)
apply_formatting = true # bool | Apply model-specified formatting to each result. (optional)
cache = true # bool | Get results from cache if available. (optional)
image_width = 789 # int | Render width for image formats. (optional)
image_height = 789 # int | Render height for image formats. (optional)
generate_drill_links = true # bool | Generate drill links (only applicable to 'unified' format. (optional)
force_production = true # bool | Force use of production models even if the user is in developer mode. (optional)

try: 
    # run look
    api_response = api_instance.run_look(look_id, format, limit=limit, apply_formatting=apply_formatting, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LookApi->run_look: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Id of look | 
 **format** | **str**| Format of result | 
 **limit** | **int**| Row limit (may override the limit in the saved query). | [optional] 
 **apply_formatting** | **bool**| Apply model-specified formatting to each result. | [optional] 
 **cache** | **bool**| Get results from cache if available. | [optional] 
 **image_width** | **int**| Render width for image formats. | [optional] 
 **image_height** | **int**| Render height for image formats. | [optional] 
 **generate_drill_links** | **bool**| Generate drill links (only applicable to &#39;unified&#39; format. | [optional] 
 **force_production** | **bool**| Force use of production models even if the user is in developer mode. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text, application/json, image/png, image/jpg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# lookerpy.SpaceApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_spaces**](SpaceApi.md#all_spaces) | **GET** /spaces | get all spaces
[**create_space**](SpaceApi.md#create_space) | **POST** /spaces | create space
[**delete_space**](SpaceApi.md#delete_space) | **DELETE** /spaces/{space_id} | delete space
[**space**](SpaceApi.md#space) | **GET** /spaces/{space_id} | get space
[**space_ancestors**](SpaceApi.md#space_ancestors) | **GET** /spaces/{space_id}/ancestors | get ancestors of space
[**space_children**](SpaceApi.md#space_children) | **GET** /spaces/{space_id}/children | get children of space
[**space_children_search**](SpaceApi.md#space_children_search) | **GET** /spaces/{space_id}/children/search | search children of space
[**space_parent**](SpaceApi.md#space_parent) | **GET** /spaces/{space_id}/parent | get parent of space
[**update_space**](SpaceApi.md#update_space) | **PATCH** /spaces/{space_id} | update space


# **all_spaces**
> list[SpaceBase] all_spaces(fields=fields)

get all spaces

### Get information about all spaces.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SpaceApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all spaces
    api_response = api_instance.all_spaces(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpaceApi->all_spaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[SpaceBase]**](SpaceBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space**
> Space create_space(body=body)

create space

### Create a space with specified information.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SpaceApi()
body = lookerpy.Space() # Space | space (optional)

try: 
    # create space
    api_response = api_instance.create_space(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpaceApi->create_space: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Space**](Space.md)| space | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_space**
> str delete_space(space_id)

delete space

### Delete the space with a specific id including any children spaces. **DANGER** this will delete all looks and dashboards in the space. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SpaceApi()
space_id = 'space_id_example' # str | Id of space

try: 
    # delete space
    api_response = api_instance.delete_space(space_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpaceApi->delete_space: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space**
> Space space(space_id, fields=fields)

get space

### Get information about the space with a specific id.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get space
    api_response = api_instance.space(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpaceApi->space: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_ancestors**
> Space space_ancestors(space_id, fields=fields)

get ancestors of space

### Get a space's ancestors

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get ancestors of space
    api_response = api_instance.space_ancestors(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpaceApi->space_ancestors: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_children**
> Space space_children(space_id, fields=fields, page=page, per_page=per_page, sorts=sorts)

get children of space

### Get a space's children

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)

try: 
    # get children of space
    api_response = api_instance.space_children(space_id, fields=fields, page=page, per_page=per_page, sorts=sorts)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpaceApi->space_children: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_children_search**
> Space space_children_search(space_id, fields=fields, sorts=sorts, name=name)

search children of space

### Search a space's children

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
name = 'name_example' # str | Match Space name. (optional)

try: 
    # search children of space
    api_response = api_instance.space_children_search(space_id, fields=fields, sorts=sorts, name=name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpaceApi->space_children_search: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **name** | **str**| Match Space name. | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **space_parent**
> Space space_parent(space_id, fields=fields)

get parent of space

### Get a space's parent

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SpaceApi()
space_id = 'space_id_example' # str | Id of space
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get parent of space
    api_response = api_instance.space_parent(space_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpaceApi->space_parent: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_space**
> Space update_space(space_id, body)

update space

### Update the space with a specific id.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.SpaceApi()
space_id = 'space_id_example' # str | Id of space
body = lookerpy.Space() # Space | space

try: 
    # update space
    api_response = api_instance.update_space(space_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SpaceApi->update_space: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Id of space | 
 **body** | [**Space**](Space.md)| space | 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


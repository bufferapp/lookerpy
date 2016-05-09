# lookerpy.ProjectApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_project_to_production**](ProjectApi.md#reset_project_to_production) | **POST** /projects/{project_id}/reset_to_production | Reset a project to the version that is in production.


# **reset_project_to_production**
> bool reset_project_to_production(project_id)

Reset a project to the version that is in production.

### Reset a project with a specified ID to the version of the project that is in production.  **DANGER** this will delete any changes that have not been pushed to a remote repository. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ProjectApi()
project_id = 'project_id_example' # str | Id of project

try: 
    # Reset a project to the version that is in production.
    api_response = api_instance.reset_project_to_production(project_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProjectApi->reset_project_to_production: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Id of project | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


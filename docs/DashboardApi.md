# lookerpy.DashboardApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_dashboards**](DashboardApi.md#all_dashboards) | **GET** /dashboards | get all dashboards
[**copy_dashboards**](DashboardApi.md#copy_dashboards) | **POST** /dashboards/copy | copy dashboards to space
[**create_dashboard**](DashboardApi.md#create_dashboard) | **POST** /dashboards | create dashboard
[**create_dashboard_prefetch**](DashboardApi.md#create_dashboard_prefetch) | **POST** /dashboards/{dashboard_id}/prefetch | create a prefetch
[**dashboard**](DashboardApi.md#dashboard) | **GET** /dashboards/{dashboard_id} | get dashboard
[**dashboard_prefetch**](DashboardApi.md#dashboard_prefetch) | **GET** /dashboards/{dashboard_id}/prefetch | get a prefetch
[**dashboards_move_plan**](DashboardApi.md#dashboards_move_plan) | **GET** /dashboards/move_plan | plan for moving dashboards to space
[**delete_dashboard**](DashboardApi.md#delete_dashboard) | **DELETE** /dashboards/{dashboard_id} | delete dashboard
[**move_dashboards**](DashboardApi.md#move_dashboards) | **PATCH** /dashboards/move | move dashboards to space
[**update_dashboard**](DashboardApi.md#update_dashboard) | **PATCH** /dashboards/{dashboard_id} | update dashboard


# **all_dashboards**
> list[DashboardBase] all_dashboards(fields=fields)

get all dashboards

Get information about all dashboards.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
fields = 'fields_example' # str | Requested fieds. (optional)

try: 
    # get all dashboards
    api_response = api_instance.all_dashboards(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->all_dashboards: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fieds. | [optional] 

### Return type

[**list[DashboardBase]**](DashboardBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_dashboards**
> str copy_dashboards(body=body, space_id=space_id, dashboard_ids=dashboard_ids)

copy dashboards to space

### Copy dashboards with specified ids to space

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
body = lookerpy.Dashboard() # Dashboard | dashboard (optional)
space_id = 'space_id_example' # str | Destination space id. (optional)
dashboard_ids = ['dashboard_ids_example'] # list[str] | Dashboard ids to copy. (optional)

try: 
    # copy dashboards to space
    api_response = api_instance.copy_dashboards(body=body, space_id=space_id, dashboard_ids=dashboard_ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->copy_dashboards: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| dashboard | [optional] 
 **space_id** | **str**| Destination space id. | [optional] 
 **dashboard_ids** | [**list[str]**](str.md)| Dashboard ids to copy. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard**
> Dashboard create_dashboard(body=body)

create dashboard

### Create a dashboard with specified information.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
body = lookerpy.Dashboard() # Dashboard | dashboard (optional)

try: 
    # create dashboard
    api_response = api_instance.create_dashboard(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->create_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| dashboard | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard_prefetch**
> PrefetchDashboardRequestMapper create_dashboard_prefetch(dashboard_id, body=body)

create a prefetch

### Create a prefetch for a dashboard with the specified information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
body = lookerpy.PrefetchDashboardRequestMapper() # PrefetchDashboardRequestMapper | Parameters for prefetch request (optional)

try: 
    # create a prefetch
    api_response = api_instance.create_dashboard_prefetch(dashboard_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->create_dashboard_prefetch: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **body** | [**PrefetchDashboardRequestMapper**](PrefetchDashboardRequestMapper.md)| Parameters for prefetch request | [optional] 

### Return type

[**PrefetchDashboardRequestMapper**](PrefetchDashboardRequestMapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard**
> Dashboard dashboard(dashboard_id, fields=fields)

get dashboard

### Get information about the dashboard with a specific id.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get dashboard
    api_response = api_instance.dashboard(dashboard_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_prefetch**
> PrefetchMapper dashboard_prefetch(dashboard_id, dashboard_filters=dashboard_filters)

get a prefetch

### Get a prefetch for a dashboard with the specified information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
dashboard_filters = [lookerpy.PrefetchDashboardFilterValue()] # list[PrefetchDashboardFilterValue] | JSON encoded string of Dashboard filters that were applied to prefetch (optional)

try: 
    # get a prefetch
    api_response = api_instance.dashboard_prefetch(dashboard_id, dashboard_filters=dashboard_filters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->dashboard_prefetch: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **dashboard_filters** | [**list[PrefetchDashboardFilterValue]**](PrefetchDashboardFilterValue.md)| JSON encoded string of Dashboard filters that were applied to prefetch | [optional] 

### Return type

[**PrefetchMapper**](PrefetchMapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_move_plan**
> LookMovePlan dashboards_move_plan(space_id=space_id, dashboard_ids=dashboard_ids)

plan for moving dashboards to space

### Plan for moving dashboards with specified ids.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
space_id = 'space_id_example' # str | Destination space id. (optional)
dashboard_ids = ['dashboard_ids_example'] # list[str] | Dashboard ids to move. (optional)

try: 
    # plan for moving dashboards to space
    api_response = api_instance.dashboards_move_plan(space_id=space_id, dashboard_ids=dashboard_ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->dashboards_move_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**| Destination space id. | [optional] 
 **dashboard_ids** | [**list[str]**](str.md)| Dashboard ids to move. | [optional] 

### Return type

[**LookMovePlan**](LookMovePlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> str delete_dashboard(dashboard_id)

delete dashboard

### Delete the dashboard with a specific id.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard

try: 
    # delete dashboard
    api_response = api_instance.delete_dashboard(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->delete_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_dashboards**
> str move_dashboards(body, space_id=space_id, dashboard_ids=dashboard_ids)

move dashboards to space

### Move dashboards with specified ids to space

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
body = lookerpy.Dashboard() # Dashboard | dashboard
space_id = 'space_id_example' # str | Destination space id. (optional)
dashboard_ids = ['dashboard_ids_example'] # list[str] | Dashboard ids to move. (optional)

try: 
    # move dashboards to space
    api_response = api_instance.move_dashboards(body, space_id=space_id, dashboard_ids=dashboard_ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->move_dashboards: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| dashboard | 
 **space_id** | **str**| Destination space id. | [optional] 
 **dashboard_ids** | [**list[str]**](str.md)| Dashboard ids to move. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> Dashboard update_dashboard(dashboard_id, body)

update dashboard

### Update the dashboard with a specific id.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
body = lookerpy.Dashboard() # Dashboard | dashboard

try: 
    # update dashboard
    api_response = api_instance.update_dashboard(dashboard_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->update_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **body** | [**Dashboard**](Dashboard.md)| dashboard | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


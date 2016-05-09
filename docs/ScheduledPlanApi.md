# lookerpy.ScheduledPlanApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_scheduled_plans**](ScheduledPlanApi.md#all_scheduled_plans) | **GET** /scheduled_plans | get all scheduled plans
[**create_scheduled_plan**](ScheduledPlanApi.md#create_scheduled_plan) | **POST** /scheduled_plans | create scheduled plan
[**create_scheduled_plan_destination**](ScheduledPlanApi.md#create_scheduled_plan_destination) | **POST** /scheduled_plan_destinations | create scheduled plan destination
[**delete_scheduled_plan**](ScheduledPlanApi.md#delete_scheduled_plan) | **DELETE** /scheduled_plans/{scheduled_plan_id} | delete scheduled plan
[**delete_scheduled_plan_destination**](ScheduledPlanApi.md#delete_scheduled_plan_destination) | **DELETE** /scheduled_plan_destinations/{scheduled_plan_destination_id} | delete scheduled plan destination
[**scheduled_plan**](ScheduledPlanApi.md#scheduled_plan) | **GET** /scheduled_plans/{scheduled_plan_id} | get scheduled plan
[**scheduled_plan_destination**](ScheduledPlanApi.md#scheduled_plan_destination) | **GET** /scheduled_plan_destinations/{scheduled_plan_destination_id} | get scheduled plan destination
[**scheduled_plans_by_dashboard**](ScheduledPlanApi.md#scheduled_plans_by_dashboard) | **GET** /scheduled_plans/dashboard/{dashboard_id} | get all scheduled plans for a given dashboard for the requesting user
[**scheduled_plans_by_look**](ScheduledPlanApi.md#scheduled_plans_by_look) | **GET** /scheduled_plans/look/{look_id} | get all scheduled plans for a given look for the requesting user
[**scheduled_plans_by_lookml_dashboard**](ScheduledPlanApi.md#scheduled_plans_by_lookml_dashboard) | **GET** /scheduled_plans/lookml_dashboard/{lookml_dashboard_id} | get all scheduled plans for a given lookml dashboard for the requesting user
[**scheduled_plans_by_space**](ScheduledPlanApi.md#scheduled_plans_by_space) | **GET** /scheduled_plans/space/{space_id} | get all scheduled plans for a given space for the requesting user
[**update_scheduled_plan**](ScheduledPlanApi.md#update_scheduled_plan) | **PATCH** /scheduled_plans/{scheduled_plan_id} | update scheduled plan
[**update_scheduled_plan_destination**](ScheduledPlanApi.md#update_scheduled_plan_destination) | **PATCH** /scheduled_plan_destinations/{scheduled_plan_destination_id} | update scheduled plan destination


# **all_scheduled_plans**
> list[ScheduledPlan] all_scheduled_plans()

get all scheduled plans

### List all scheduled plans which belong to the requesting user

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()

try: 
    # get all scheduled plans
    api_response = api_instance.all_scheduled_plans()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->all_scheduled_plans: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scheduled_plan**
> ScheduledPlan create_scheduled_plan(body=body)

create scheduled plan

### Schedule a Look or Dashboard by creating a scheduled plan

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
body = lookerpy.ScheduledPlan() # ScheduledPlan | scheduled plan (optional)

try: 
    # create scheduled plan
    api_response = api_instance.create_scheduled_plan(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->create_scheduled_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduledPlan**](ScheduledPlan.md)| scheduled plan | [optional] 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scheduled_plan_destination**
> ScheduledPlanDestination create_scheduled_plan_destination(body=body)

create scheduled plan destination

### Set destinations for a scheduled plan

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
body = lookerpy.ScheduledPlanDestination() # ScheduledPlanDestination | scheduled plan destination (optional)

try: 
    # create scheduled plan destination
    api_response = api_instance.create_scheduled_plan_destination(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->create_scheduled_plan_destination: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduledPlanDestination**](ScheduledPlanDestination.md)| scheduled plan destination | [optional] 

### Return type

[**ScheduledPlanDestination**](ScheduledPlanDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_plan**
> str delete_scheduled_plan(scheduled_plan_id)

delete scheduled plan

### Delete the scheduled plan with the specified id

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
scheduled_plan_id = 789 # int | Scheduled Plan Id

try: 
    # delete scheduled plan
    api_response = api_instance.delete_scheduled_plan(scheduled_plan_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->delete_scheduled_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_id** | **int**| Scheduled Plan Id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_plan_destination**
> str delete_scheduled_plan_destination(scheduled_plan_destination_id)

delete scheduled plan destination

### Delete a scheduled plan destination instance

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
scheduled_plan_destination_id = 789 # int | Scheduled Plan Destination Id

try: 
    # delete scheduled plan destination
    api_response = api_instance.delete_scheduled_plan_destination(scheduled_plan_destination_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->delete_scheduled_plan_destination: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_destination_id** | **int**| Scheduled Plan Destination Id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plan**
> ScheduledPlan scheduled_plan(scheduled_plan_id)

get scheduled plan

### Get information about a scheduled plan

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
scheduled_plan_id = 789 # int | Scheduled Plan Id

try: 
    # get scheduled plan
    api_response = api_instance.scheduled_plan(scheduled_plan_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->scheduled_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_id** | **int**| Scheduled Plan Id | 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plan_destination**
> ScheduledPlanDestination scheduled_plan_destination(scheduled_plan_destination_id)

get scheduled plan destination

### Get scheduled plan destination instance

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
scheduled_plan_destination_id = 789 # int | Scheduled Plan Destination Id

try: 
    # get scheduled plan destination
    api_response = api_instance.scheduled_plan_destination(scheduled_plan_destination_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->scheduled_plan_destination: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_destination_id** | **int**| Scheduled Plan Destination Id | 

### Return type

[**ScheduledPlanDestination**](ScheduledPlanDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_by_dashboard**
> list[ScheduledPlan] scheduled_plans_by_dashboard(dashboard_id)

get all scheduled plans for a given dashboard for the requesting user

### Get scheduled plans by using a dashboard id for the requesting user

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
dashboard_id = 789 # int | Dashboard Id

try: 
    # get all scheduled plans for a given dashboard for the requesting user
    api_response = api_instance.scheduled_plans_by_dashboard(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->scheduled_plans_by_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| Dashboard Id | 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_by_look**
> list[ScheduledPlan] scheduled_plans_by_look(look_id)

get all scheduled plans for a given look for the requesting user

### Get scheduled plans by using a look id for the requesting user

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
look_id = 789 # int | Look Id

try: 
    # get all scheduled plans for a given look for the requesting user
    api_response = api_instance.scheduled_plans_by_look(look_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->scheduled_plans_by_look: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **look_id** | **int**| Look Id | 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_by_lookml_dashboard**
> list[ScheduledPlan] scheduled_plans_by_lookml_dashboard(lookml_dashboard_id)

get all scheduled plans for a given lookml dashboard for the requesting user

### Get scheduled plans by using a LookML dashboard id for the requesting user

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
lookml_dashboard_id = 789 # int | LookML Dashboard Id

try: 
    # get all scheduled plans for a given lookml dashboard for the requesting user
    api_response = api_instance.scheduled_plans_by_lookml_dashboard(lookml_dashboard_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->scheduled_plans_by_lookml_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookml_dashboard_id** | **int**| LookML Dashboard Id | 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_plans_by_space**
> list[ScheduledPlan] scheduled_plans_by_space(space_id)

get all scheduled plans for a given space for the requesting user

### Get scheduled plans by using a space id for the requesting user

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
space_id = 789 # int | Space Id

try: 
    # get all scheduled plans for a given space for the requesting user
    api_response = api_instance.scheduled_plans_by_space(space_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->scheduled_plans_by_space: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **int**| Space Id | 

### Return type

[**list[ScheduledPlan]**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduled_plan**
> ScheduledPlan update_scheduled_plan(scheduled_plan_id, body)

update scheduled plan

### Update the scheduled plan with the specified id

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
scheduled_plan_id = 789 # int | Scheduled Plan Id
body = lookerpy.ScheduledPlan() # ScheduledPlan | scheduled plan

try: 
    # update scheduled plan
    api_response = api_instance.update_scheduled_plan(scheduled_plan_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->update_scheduled_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_id** | **int**| Scheduled Plan Id | 
 **body** | [**ScheduledPlan**](ScheduledPlan.md)| scheduled plan | 

### Return type

[**ScheduledPlan**](ScheduledPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduled_plan_destination**
> ScheduledPlanDestination update_scheduled_plan_destination(scheduled_plan_destination_id, body)

update scheduled plan destination

### Update a scheduled plan destination instance

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ScheduledPlanApi()
scheduled_plan_destination_id = 789 # int | Scheduled Plan Destination Id
body = lookerpy.ScheduledPlanDestination() # ScheduledPlanDestination | scheduled plan destination

try: 
    # update scheduled plan destination
    api_response = api_instance.update_scheduled_plan_destination(scheduled_plan_destination_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ScheduledPlanApi->update_scheduled_plan_destination: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_plan_destination_id** | **int**| Scheduled Plan Destination Id | 
 **body** | [**ScheduledPlanDestination**](ScheduledPlanDestination.md)| scheduled plan destination | 

### Return type

[**ScheduledPlanDestination**](ScheduledPlanDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


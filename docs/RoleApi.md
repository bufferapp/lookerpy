# lookerpy.RoleApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_model_sets**](RoleApi.md#all_model_sets) | **GET** /model_sets | get all model sets
[**all_permission_sets**](RoleApi.md#all_permission_sets) | **GET** /permission_sets | get all permission sets
[**all_permissions**](RoleApi.md#all_permissions) | **GET** /permissions | get all permissions
[**all_roles**](RoleApi.md#all_roles) | **GET** /roles | get all roles
[**create_model_set**](RoleApi.md#create_model_set) | **POST** /model_sets | create a model set
[**create_permission_set**](RoleApi.md#create_permission_set) | **POST** /permission_sets | create a permission set
[**create_role**](RoleApi.md#create_role) | **POST** /roles | create a role
[**delete_model_set**](RoleApi.md#delete_model_set) | **DELETE** /model_sets/{model_set_id} | delete a model set
[**delete_permission_set**](RoleApi.md#delete_permission_set) | **DELETE** /permission_sets/{permission_set_id} | delete a permission set
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /roles/{role_id} | delete a role
[**model_set**](RoleApi.md#model_set) | **GET** /model_sets/{model_set_id} | Get a model set
[**permission_set**](RoleApi.md#permission_set) | **GET** /permission_sets/{permission_set_id} | Get a permission set
[**role**](RoleApi.md#role) | **GET** /roles/{role_id} | Get a role
[**role_users**](RoleApi.md#role_users) | **GET** /roles/{role_id}/users | Get users with role
[**set_role_users**](RoleApi.md#set_role_users) | **PUT** /roles/{role_id}/users | Set users with role
[**update_model_set**](RoleApi.md#update_model_set) | **PATCH** /model_sets/{model_set_id} | update a model set
[**update_permission_set**](RoleApi.md#update_permission_set) | **PATCH** /permission_sets/{permission_set_id} | update a permission set
[**update_role**](RoleApi.md#update_role) | **PATCH** /roles/{role_id} | update a role


# **all_model_sets**
> list[ModelSet] all_model_sets(fields=fields)

get all model sets

### Get information about all model sets. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all model sets
    api_response = api_instance.all_model_sets(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->all_model_sets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[ModelSet]**](ModelSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_permission_sets**
> list[PermissionSet] all_permission_sets(fields=fields)

get all permission sets

### Get information about all permission sets. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all permission sets
    api_response = api_instance.all_permission_sets(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->all_permission_sets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[PermissionSet]**](PermissionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_permissions**
> list[Permission] all_permissions()

get all permissions

### Get all supported permissions.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()

try: 
    # get all permissions
    api_response = api_instance.all_permissions()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->all_permissions: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Permission]**](Permission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_roles**
> list[Role] all_roles(fields=fields)

get all roles

### Get information about all roles. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all roles
    api_response = api_instance.all_roles(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->all_roles: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model_set**
> ModelSet create_model_set(body=body)

create a model set

### Create a model set with the specified information. Model sets are used by Roles. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
body = lookerpy.ModelSet() # ModelSet | ModelSet (optional)

try: 
    # create a model set
    api_response = api_instance.create_model_set(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->create_model_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelSet**](ModelSet.md)| ModelSet | [optional] 

### Return type

[**ModelSet**](ModelSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_permission_set**
> PermissionSet create_permission_set(body=body)

create a permission set

### Create a permission set with the specified information. Permission sets are used by Roles. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
body = lookerpy.PermissionSet() # PermissionSet | PermissionSet (optional)

try: 
    # create a permission set
    api_response = api_instance.create_permission_set(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->create_permission_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermissionSet**](PermissionSet.md)| PermissionSet | [optional] 

### Return type

[**PermissionSet**](PermissionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> Role create_role(body=body)

create a role

### Create a role with the specified information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
body = lookerpy.Role() # Role | Role (optional)

try: 
    # create a role
    api_response = api_instance.create_role(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->create_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Role**](Role.md)| Role | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_set**
> str delete_model_set(model_set_id)

delete a model set

### Delete the model set with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
model_set_id = 789 # int | id of model set

try: 
    # delete a model set
    api_response = api_instance.delete_model_set(model_set_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->delete_model_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_set_id** | **int**| id of model set | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permission_set**
> str delete_permission_set(permission_set_id)

delete a permission set

### Delete the permission set with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
permission_set_id = 789 # int | Id of permission set

try: 
    # delete a permission set
    api_response = api_instance.delete_permission_set(permission_set_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->delete_permission_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_set_id** | **int**| Id of permission set | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> str delete_role(role_id)

delete a role

### Delete the role with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
role_id = 789 # int | id of role

try: 
    # delete a role
    api_response = api_instance.delete_role(role_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->delete_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of role | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_set**
> ModelSet model_set(model_set_id, fields=fields)

Get a model set

### Get information about the model set with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
model_set_id = 789 # int | Id of model set
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get a model set
    api_response = api_instance.model_set(model_set_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->model_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_set_id** | **int**| Id of model set | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**ModelSet**](ModelSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_set**
> PermissionSet permission_set(permission_set_id, fields=fields)

Get a permission set

### Get information about the permission set with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
permission_set_id = 789 # int | Id of permission set
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get a permission set
    api_response = api_instance.permission_set(permission_set_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->permission_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_set_id** | **int**| Id of permission set | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**PermissionSet**](PermissionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role**
> Role role(role_id)

Get a role

### Get information about the role with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
role_id = 789 # int | id of role

try: 
    # Get a role
    api_response = api_instance.role(role_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of role | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_users**
> list[User] role_users(role_id, fields=fields)

Get users with role

### Get information about all the users with the role that has a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
role_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get users with role
    api_response = api_instance.role_users(role_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->role_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_role_users**
> list[User] set_role_users(role_id, body)

Set users with role

### Set all the users of the role with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
role_id = 789 # int | id of role
body = [lookerpy.list[int]()] # list[int] | array of user ids for role

try: 
    # Set users with role
    api_response = api_instance.set_role_users(role_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->set_role_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of role | 
 **body** | **list[int]**| array of user ids for role | 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model_set**
> ModelSet update_model_set(model_set_id, body)

update a model set

### Update information about the model set with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
model_set_id = 789 # int | id of model set
body = lookerpy.ModelSet() # ModelSet | ModelSet

try: 
    # update a model set
    api_response = api_instance.update_model_set(model_set_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->update_model_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_set_id** | **int**| id of model set | 
 **body** | [**ModelSet**](ModelSet.md)| ModelSet | 

### Return type

[**ModelSet**](ModelSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission_set**
> PermissionSet update_permission_set(permission_set_id, body)

update a permission set

### Update information about the permission set with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
permission_set_id = 789 # int | id of permission set
body = lookerpy.PermissionSet() # PermissionSet | PermissionSet

try: 
    # update a permission set
    api_response = api_instance.update_permission_set(permission_set_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->update_permission_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_set_id** | **int**| id of permission set | 
 **body** | [**PermissionSet**](PermissionSet.md)| PermissionSet | 

### Return type

[**PermissionSet**](PermissionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> Role update_role(role_id, body)

update a role

### Update information about the role with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.RoleApi()
role_id = 789 # int | id of role
body = lookerpy.Role() # Role | Role

try: 
    # update a role
    api_response = api_instance.update_role(role_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RoleApi->update_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| id of role | 
 **body** | [**Role**](Role.md)| Role | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


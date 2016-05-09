# lookerpy.UserApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_user_access_filters**](UserApi.md#all_user_access_filters) | **GET** /users/{user_id}/access_filters | get all Access filters
[**all_user_credentials_api3s**](UserApi.md#all_user_credentials_api3s) | **GET** /users/{user_id}/credentials_api3 | get all API 3 credentials
[**all_user_credentials_embeds**](UserApi.md#all_user_credentials_embeds) | **GET** /users/{user_id}/credentials_embed | get all Embedding credentials
[**all_user_sessions**](UserApi.md#all_user_sessions) | **GET** /users/{user_id}/sessions | get all Web login sessions
[**all_users**](UserApi.md#all_users) | **GET** /users | get all users
[**create_user**](UserApi.md#create_user) | **POST** /users | create a user
[**create_user_access_filter**](UserApi.md#create_user_access_filter) | **POST** /users/{user_id}/access_filters | create Access filter
[**create_user_credentials_api**](UserApi.md#create_user_credentials_api) | **POST** /users/{user_id}/credentials_api | create API credential
[**create_user_credentials_api3**](UserApi.md#create_user_credentials_api3) | **POST** /users/{user_id}/credentials_api3 | create API 3 credential
[**create_user_credentials_email**](UserApi.md#create_user_credentials_email) | **POST** /users/{user_id}/credentials_email | create email/password credential
[**create_user_credentials_email_password_reset**](UserApi.md#create_user_credentials_email_password_reset) | **POST** /users/{user_id}/credentials_email/password_reset | create a email/password credential password reset token
[**create_user_credentials_totp**](UserApi.md#create_user_credentials_totp) | **POST** /users/{user_id}/credentials_totp | create Two-factor credential
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{user_id} | delete a user
[**delete_user_access_filter**](UserApi.md#delete_user_access_filter) | **DELETE** /users/{user_id}/access_filters/{access_filter_id} | delete Access filter
[**delete_user_credentials_api**](UserApi.md#delete_user_credentials_api) | **DELETE** /users/{user_id}/credentials_api | delete API credential
[**delete_user_credentials_api3**](UserApi.md#delete_user_credentials_api3) | **DELETE** /users/{user_id}/credentials_api3/{credentials_api3_id} | delete API 3 credential
[**delete_user_credentials_email**](UserApi.md#delete_user_credentials_email) | **DELETE** /users/{user_id}/credentials_email | delete email/password credential
[**delete_user_credentials_embed**](UserApi.md#delete_user_credentials_embed) | **DELETE** /users/{user_id}/credentials_embed/{credentials_embed_id} | delete Embedding credential
[**delete_user_credentials_google**](UserApi.md#delete_user_credentials_google) | **DELETE** /users/{user_id}/credentials_google | delete Google auth credential
[**delete_user_credentials_ldap**](UserApi.md#delete_user_credentials_ldap) | **DELETE** /users/{user_id}/credentials_ldap | delete LDAP credential
[**delete_user_credentials_looker_openid**](UserApi.md#delete_user_credentials_looker_openid) | **DELETE** /users/{user_id}/credentials_looker_openid | delete Looker Openid credential
[**delete_user_credentials_saml**](UserApi.md#delete_user_credentials_saml) | **DELETE** /users/{user_id}/credentials_saml | delete Saml auth credential
[**delete_user_credentials_totp**](UserApi.md#delete_user_credentials_totp) | **DELETE** /users/{user_id}/credentials_totp | delete Two-factor credential
[**delete_user_session**](UserApi.md#delete_user_session) | **DELETE** /users/{user_id}/sessions/{session_id} | delete Web login session
[**me**](UserApi.md#me) | **GET** /user | Get current user
[**search_users**](UserApi.md#search_users) | **GET** /users/search | search users
[**search_users_names**](UserApi.md#search_users_names) | **GET** /users/search/names/{pattern} | search users names
[**set_user_roles**](UserApi.md#set_user_roles) | **PUT** /users/{user_id}/roles | Set roles for a user
[**update_user**](UserApi.md#update_user) | **PATCH** /users/{user_id} | update a user
[**update_user_access_filter**](UserApi.md#update_user_access_filter) | **PATCH** /users/{user_id}/access_filters/{access_filter_id} | update Access filter
[**update_user_credentials_email**](UserApi.md#update_user_credentials_email) | **PATCH** /users/{user_id}/credentials_email | update email/password credential
[**user**](UserApi.md#user) | **GET** /users/{user_id} | Get a user
[**user_access_filter**](UserApi.md#user_access_filter) | **GET** /users/{user_id}/access_filters/{access_filter_id} | get Access filter
[**user_credentials_api**](UserApi.md#user_credentials_api) | **GET** /users/{user_id}/credentials_api | get API credential
[**user_credentials_api3**](UserApi.md#user_credentials_api3) | **GET** /users/{user_id}/credentials_api3/{credentials_api3_id} | get API 3 credential
[**user_credentials_email**](UserApi.md#user_credentials_email) | **GET** /users/{user_id}/credentials_email | get email/password credential
[**user_credentials_embed**](UserApi.md#user_credentials_embed) | **GET** /users/{user_id}/credentials_embed/{credentials_embed_id} | get Embedding credential
[**user_credentials_google**](UserApi.md#user_credentials_google) | **GET** /users/{user_id}/credentials_google | get Google auth credential
[**user_credentials_ldap**](UserApi.md#user_credentials_ldap) | **GET** /users/{user_id}/credentials_ldap | get LDAP credential
[**user_credentials_looker_openid**](UserApi.md#user_credentials_looker_openid) | **GET** /users/{user_id}/credentials_looker_openid | get Looker Openid credential
[**user_credentials_saml**](UserApi.md#user_credentials_saml) | **GET** /users/{user_id}/credentials_saml | get Saml auth credential
[**user_credentials_totp**](UserApi.md#user_credentials_totp) | **GET** /users/{user_id}/credentials_totp | get Two-factor credential
[**user_roles**](UserApi.md#user_roles) | **GET** /users/{user_id}/roles | Get roles for a user
[**user_session**](UserApi.md#user_session) | **GET** /users/{user_id}/sessions/{session_id} | get Web login session


# **all_user_access_filters**
> list[AccessFilter] all_user_access_filters(user_id, fields=fields)

get all Access filters

### Access filter for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all Access filters
    api_response = api_instance.all_user_access_filters(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->all_user_access_filters: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[AccessFilter]**](AccessFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_user_credentials_api3s**
> list[CredentialsApi3] all_user_credentials_api3s(user_id, fields=fields)

get all API 3 credentials

### API 3 login information for the specified user. This is for the newer API keys that can be added for any user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all API 3 credentials
    api_response = api_instance.all_user_credentials_api3s(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->all_user_credentials_api3s: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[CredentialsApi3]**](CredentialsApi3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_user_credentials_embeds**
> list[CredentialsEmbed] all_user_credentials_embeds(user_id, fields=fields)

get all Embedding credentials

### Embed login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all Embedding credentials
    api_response = api_instance.all_user_credentials_embeds(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->all_user_credentials_embeds: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[CredentialsEmbed]**](CredentialsEmbed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_user_sessions**
> list[Session] all_user_sessions(user_id, fields=fields)

get all Web login sessions

### Web login session for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all Web login sessions
    api_response = api_instance.all_user_sessions(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->all_user_sessions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Session]**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_users**
> list[User] all_users(fields=fields, page=page, per_page=per_page, sorts=sorts)

get all users

### Get information about all users. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)

try: 
    # get all users
    api_response = api_instance.all_users(fields=fields, page=page, per_page=per_page, sorts=sorts)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->all_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(body=body)

create a user

### Create a user with the specified information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
body = lookerpy.User() # User | User (optional)

try: 
    # create a user
    api_response = api_instance.create_user(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| User | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_access_filter**
> AccessFilter create_user_access_filter(user_id, body=body, fields=fields)

create Access filter

### Access filter for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
body = lookerpy.AccessFilter() # AccessFilter | Access filter (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # create Access filter
    api_response = api_instance.create_user_access_filter(user_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_user_access_filter: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**AccessFilter**](AccessFilter.md)| Access filter | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**AccessFilter**](AccessFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_api**
> CredentialsApi create_user_credentials_api(user_id, body=body, fields=fields)

create API credential

### API login information for the specified user. This is for 'API Users' used for the 'old' query API.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
body = lookerpy.CredentialsApi() # CredentialsApi | API credential (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # create API credential
    api_response = api_instance.create_user_credentials_api(user_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_user_credentials_api: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**CredentialsApi**](CredentialsApi.md)| API credential | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsApi**](CredentialsApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_api3**
> CredentialsApi3 create_user_credentials_api3(user_id, body=body, fields=fields)

create API 3 credential

### API 3 login information for the specified user. This is for the newer API keys that can be added for any user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
body = lookerpy.CredentialsApi3() # CredentialsApi3 | API 3 credential (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # create API 3 credential
    api_response = api_instance.create_user_credentials_api3(user_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_user_credentials_api3: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**CredentialsApi3**](CredentialsApi3.md)| API 3 credential | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsApi3**](CredentialsApi3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_email**
> CredentialsEmail create_user_credentials_email(user_id, body=body, fields=fields)

create email/password credential

### Email/password login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
body = lookerpy.CredentialsEmail() # CredentialsEmail | email/password credential (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # create email/password credential
    api_response = api_instance.create_user_credentials_email(user_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_user_credentials_email: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**CredentialsEmail**](CredentialsEmail.md)| email/password credential | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmail**](CredentialsEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_email_password_reset**
> CredentialsEmail create_user_credentials_email_password_reset(user_id, expires=expires, fields=fields)

create a email/password credential password reset token

### Create a password reset token. This will create a cryptographically secure random password reset token for the user. If the user already has a password reset token then this invalidates the old token and creates a new one. The token is expressed as the 'password_reset_url' of the user's email/password credential object. This takes an optional 'expires' param to indicate if the new token should be an expiring token. Tokens that expire are typically used for self-service password resets for existing users. Invitiation emails for new users typically are not set to expire. The expire period is always 60 minutes when expires is enabled. This method can be called with an empty body. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | Id of user
expires = true # bool | Expiring token. (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # create a email/password credential password reset token
    api_response = api_instance.create_user_credentials_email_password_reset(user_id, expires=expires, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_user_credentials_email_password_reset: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **expires** | **bool**| Expiring token. | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmail**](CredentialsEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_credentials_totp**
> CredentialsTotp create_user_credentials_totp(user_id, body=body, fields=fields)

create Two-factor credential

### Two-factor login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
body = lookerpy.CredentialsTotp() # CredentialsTotp | Two-factor credential (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # create Two-factor credential
    api_response = api_instance.create_user_credentials_totp(user_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_user_credentials_totp: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**CredentialsTotp**](CredentialsTotp.md)| Two-factor credential | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsTotp**](CredentialsTotp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> str delete_user(user_id)

delete a user

### Delete the user with a specific id.  **DANGER** this will delete the user and all looks and other information owned by the user. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | Id of user

try: 
    # delete a user
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_access_filter**
> str delete_user_access_filter(user_id, access_filter_id)

delete Access filter

### Access filter for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
access_filter_id = 789 # int | id of Access filter

try: 
    # delete Access filter
    api_response = api_instance.delete_user_access_filter(user_id, access_filter_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_access_filter: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **access_filter_id** | **int**| id of Access filter | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_api**
> str delete_user_credentials_api(user_id)

delete API credential

### API login information for the specified user. This is for 'API Users' used for the 'old' query API.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user

try: 
    # delete API credential
    api_response = api_instance.delete_user_credentials_api(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_credentials_api: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_api3**
> str delete_user_credentials_api3(user_id, credentials_api3_id)

delete API 3 credential

### API 3 login information for the specified user. This is for the newer API keys that can be added for any user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
credentials_api3_id = 789 # int | id of API 3 credential

try: 
    # delete API 3 credential
    api_response = api_instance.delete_user_credentials_api3(user_id, credentials_api3_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_credentials_api3: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **credentials_api3_id** | **int**| id of API 3 credential | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_email**
> str delete_user_credentials_email(user_id)

delete email/password credential

### Email/password login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user

try: 
    # delete email/password credential
    api_response = api_instance.delete_user_credentials_email(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_credentials_email: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_embed**
> str delete_user_credentials_embed(user_id, credentials_embed_id)

delete Embedding credential

### Embed login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
credentials_embed_id = 789 # int | id of Embedding credential

try: 
    # delete Embedding credential
    api_response = api_instance.delete_user_credentials_embed(user_id, credentials_embed_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_credentials_embed: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **credentials_embed_id** | **int**| id of Embedding credential | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_google**
> str delete_user_credentials_google(user_id)

delete Google auth credential

### Google authentication login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user

try: 
    # delete Google auth credential
    api_response = api_instance.delete_user_credentials_google(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_credentials_google: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_ldap**
> str delete_user_credentials_ldap(user_id)

delete LDAP credential

### LDAP login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user

try: 
    # delete LDAP credential
    api_response = api_instance.delete_user_credentials_ldap(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_credentials_ldap: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_looker_openid**
> str delete_user_credentials_looker_openid(user_id)

delete Looker Openid credential

### Looker Openid login information for the specified user. Used by Looker Analysts.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user

try: 
    # delete Looker Openid credential
    api_response = api_instance.delete_user_credentials_looker_openid(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_credentials_looker_openid: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_saml**
> str delete_user_credentials_saml(user_id)

delete Saml auth credential

### Saml authentication login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user

try: 
    # delete Saml auth credential
    api_response = api_instance.delete_user_credentials_saml(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_credentials_saml: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_credentials_totp**
> str delete_user_credentials_totp(user_id)

delete Two-factor credential

### Two-factor login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user

try: 
    # delete Two-factor credential
    api_response = api_instance.delete_user_credentials_totp(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_credentials_totp: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_session**
> str delete_user_session(user_id, session_id)

delete Web login session

### Web login session for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
session_id = 789 # int | id of Web login session

try: 
    # delete Web login session
    api_response = api_instance.delete_user_session(user_id, session_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_session: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **session_id** | **int**| id of Web login session | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me**
> User me(fields=fields)

Get current user

### Get information about the current user; i.e. the user account currently calling the API. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get current user
    api_response = api_instance.me(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->me: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> list[User] search_users(fields=fields, page=page, per_page=per_page, sorts=sorts, id=id, first_name=first_name, last_name=last_name, verified_looker_employee=verified_looker_employee, email=email, is_disabled=is_disabled)

search users

### Search users. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
id = 789 # int | Match User Id. (optional)
first_name = 'first_name_example' # str | Match First name. (optional)
last_name = 'last_name_example' # str | Match Last name. (optional)
verified_looker_employee = true # bool | Match Verified Looker employee. (optional)
email = 'email_example' # str | Match Email Address. (optional)
is_disabled = true # bool | Match Is disabled. (optional)

try: 
    # search users
    api_response = api_instance.search_users(fields=fields, page=page, per_page=per_page, sorts=sorts, id=id, first_name=first_name, last_name=last_name, verified_looker_employee=verified_looker_employee, email=email, is_disabled=is_disabled)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->search_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **id** | **int**| Match User Id. | [optional] 
 **first_name** | **str**| Match First name. | [optional] 
 **last_name** | **str**| Match Last name. | [optional] 
 **verified_looker_employee** | **bool**| Match Verified Looker employee. | [optional] 
 **email** | **str**| Match Email Address. | [optional] 
 **is_disabled** | **bool**| Match Is disabled. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_names**
> list[User] search_users_names(pattern, fields=fields, page=page, per_page=per_page, sorts=sorts, id=id, first_name=first_name, last_name=last_name, verified_looker_employee=verified_looker_employee, email=email, is_disabled=is_disabled)

search users names

### Search users where first_name OR last_name OR email matches a string.  The results will be AND'd with any additional search parameters that are (optionally) included. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
pattern = 'pattern_example' # str | Pattern to match.
fields = 'fields_example' # str | Requested fields. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
id = 789 # int | Match User Id. (optional)
first_name = 'first_name_example' # str | Match First name. (optional)
last_name = 'last_name_example' # str | Match Last name. (optional)
verified_looker_employee = true # bool | Match Verified Looker employee. (optional)
email = 'email_example' # str | Match Email Address. (optional)
is_disabled = true # bool | Match Is disabled. (optional)

try: 
    # search users names
    api_response = api_instance.search_users_names(pattern, fields=fields, page=page, per_page=per_page, sorts=sorts, id=id, first_name=first_name, last_name=last_name, verified_looker_employee=verified_looker_employee, email=email, is_disabled=is_disabled)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->search_users_names: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**| Pattern to match. | 
 **fields** | **str**| Requested fields. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **id** | **int**| Match User Id. | [optional] 
 **first_name** | **str**| Match First name. | [optional] 
 **last_name** | **str**| Match Last name. | [optional] 
 **verified_looker_employee** | **bool**| Match Verified Looker employee. | [optional] 
 **email** | **str**| Match Email Address. | [optional] 
 **is_disabled** | **bool**| Match Is disabled. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_roles**
> list[Role] set_user_roles(user_id, body, fields=fields)

Set roles for a user

### Set roles of the user with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
body = [lookerpy.list[int]()] # list[int] | array of roles ids for user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Set roles for a user
    api_response = api_instance.set_user_roles(user_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->set_user_roles: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | **list[int]**| array of roles ids for user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, body)

update a user

### Update information about the user with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | Id of user
body = lookerpy.User() # User | User

try: 
    # update a user
    api_response = api_instance.update_user(user_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->update_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **body** | [**User**](User.md)| User | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_access_filter**
> AccessFilter update_user_access_filter(user_id, access_filter_id, body, fields=fields)

update Access filter

### Access filter for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
access_filter_id = 789 # int | id of Access filter
body = lookerpy.AccessFilter() # AccessFilter | Access filter
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # update Access filter
    api_response = api_instance.update_user_access_filter(user_id, access_filter_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->update_user_access_filter: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **access_filter_id** | **int**| id of Access filter | 
 **body** | [**AccessFilter**](AccessFilter.md)| Access filter | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**AccessFilter**](AccessFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_credentials_email**
> CredentialsEmail update_user_credentials_email(user_id, body, fields=fields)

update email/password credential

### Email/password login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
body = lookerpy.CredentialsEmail() # CredentialsEmail | email/password credential
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # update email/password credential
    api_response = api_instance.update_user_credentials_email(user_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->update_user_credentials_email: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **body** | [**CredentialsEmail**](CredentialsEmail.md)| email/password credential | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmail**](CredentialsEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user**
> User user(user_id, fields=fields)

Get a user

### Get information about the user with a specific id.  If the caller is an admin or the caller is the user being specified, then full user information will be returned. Otherwise, a minimal 'public' variant of the user information will be returned. This contains The user name and avatar url, but no sensitive information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | Id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get a user
    api_response = api_instance.user(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_access_filter**
> AccessFilter user_access_filter(user_id, access_filter_id, fields=fields)

get Access filter

### Access filter for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | Id of user
access_filter_id = 789 # int | Id of Access filter
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get Access filter
    api_response = api_instance.user_access_filter(user_id, access_filter_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_access_filter: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **access_filter_id** | **int**| Id of Access filter | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**AccessFilter**](AccessFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_api**
> CredentialsApi user_credentials_api(user_id, fields=fields)

get API credential

### API login information for the specified user. This is for 'API Users' used for the 'old' query API.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get API credential
    api_response = api_instance.user_credentials_api(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_credentials_api: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsApi**](CredentialsApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_api3**
> CredentialsApi3 user_credentials_api3(user_id, credentials_api3_id, fields=fields)

get API 3 credential

### API 3 login information for the specified user. This is for the newer API keys that can be added for any user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | Id of user
credentials_api3_id = 789 # int | Id of API 3 credential
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get API 3 credential
    api_response = api_instance.user_credentials_api3(user_id, credentials_api3_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_credentials_api3: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **credentials_api3_id** | **int**| Id of API 3 credential | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsApi3**](CredentialsApi3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_email**
> CredentialsEmail user_credentials_email(user_id, fields=fields)

get email/password credential

### Email/password login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get email/password credential
    api_response = api_instance.user_credentials_email(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_credentials_email: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmail**](CredentialsEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_embed**
> CredentialsEmbed user_credentials_embed(user_id, credentials_embed_id, fields=fields)

get Embedding credential

### Embed login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | Id of user
credentials_embed_id = 789 # int | Id of Embedding credential
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get Embedding credential
    api_response = api_instance.user_credentials_embed(user_id, credentials_embed_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_credentials_embed: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **credentials_embed_id** | **int**| Id of Embedding credential | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsEmbed**](CredentialsEmbed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_google**
> CredentialsGoogle user_credentials_google(user_id, fields=fields)

get Google auth credential

### Google authentication login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get Google auth credential
    api_response = api_instance.user_credentials_google(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_credentials_google: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsGoogle**](CredentialsGoogle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_ldap**
> CredentialsLDAP user_credentials_ldap(user_id, fields=fields)

get LDAP credential

### LDAP login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get LDAP credential
    api_response = api_instance.user_credentials_ldap(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_credentials_ldap: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsLDAP**](CredentialsLDAP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_looker_openid**
> CredentialsLookerOpenid user_credentials_looker_openid(user_id, fields=fields)

get Looker Openid credential

### Looker Openid login information for the specified user. Used by Looker Analysts.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get Looker Openid credential
    api_response = api_instance.user_credentials_looker_openid(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_credentials_looker_openid: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsLookerOpenid**](CredentialsLookerOpenid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_saml**
> CredentialsSaml user_credentials_saml(user_id, fields=fields)

get Saml auth credential

### Saml authentication login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get Saml auth credential
    api_response = api_instance.user_credentials_saml(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_credentials_saml: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsSaml**](CredentialsSaml.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_credentials_totp**
> CredentialsTotp user_credentials_totp(user_id, fields=fields)

get Two-factor credential

### Two-factor login information for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get Two-factor credential
    api_response = api_instance.user_credentials_totp(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_credentials_totp: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**CredentialsTotp**](CredentialsTotp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_roles**
> list[Role] user_roles(user_id, fields=fields)

Get roles for a user

### Get information about roles of the user with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | id of user
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get roles for a user
    api_response = api_instance.user_roles(user_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_roles: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| id of user | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_session**
> Session user_session(user_id, session_id, fields=fields)

get Web login session

### Web login session for the specified user.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UserApi()
user_id = 789 # int | Id of user
session_id = 789 # int | Id of Web login session
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get Web login session
    api_response = api_instance.user_session(user_id, session_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_session: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Id of user | 
 **session_id** | **int**| Id of Web login session | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# lookerpy.ConfigApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_legacy_features**](ConfigApi.md#all_legacy_features) | **GET** /legacy_features | get all legacy features
[**all_timezones**](ConfigApi.md#all_timezones) | **GET** /timezones | get all timezones
[**backup_configuration**](ConfigApi.md#backup_configuration) | **GET** /backup_configuration | get backup configuration
[**legacy_feature**](ConfigApi.md#legacy_feature) | **GET** /legacy_features/{legacy_feature_id} | get legacy feature
[**update_backup_configuration**](ConfigApi.md#update_backup_configuration) | **PATCH** /backup_configuration | update backup configuration
[**update_legacy_feature**](ConfigApi.md#update_legacy_feature) | **PATCH** /legacy_features/{legacy_feature_id} | update legacy feature


# **all_legacy_features**
> list[LegacyFeature] all_legacy_features()

get all legacy features

### Get all legacy features.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConfigApi()

try: 
    # get all legacy features
    api_response = api_instance.all_legacy_features()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->all_legacy_features: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LegacyFeature]**](LegacyFeature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_timezones**
> list[Timezone] all_timezones()

get all timezones

### Get a list of timezones that Looker supports (e.g. useful for scheduling tasks). 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConfigApi()

try: 
    # get all timezones
    api_response = api_instance.all_timezones()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->all_timezones: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Timezone]**](Timezone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_configuration**
> BackupConfiguration backup_configuration()

get backup configuration

### Get the current backup configuration 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConfigApi()

try: 
    # get backup configuration
    api_response = api_instance.backup_configuration()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->backup_configuration: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupConfiguration**](BackupConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_feature**
> LegacyFeature legacy_feature(legacy_feature_id)

get legacy feature

### Get information about the legacy feature with a specific id.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConfigApi()
legacy_feature_id = 789 # int | id of legacy feature

try: 
    # get legacy feature
    api_response = api_instance.legacy_feature(legacy_feature_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->legacy_feature: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_feature_id** | **int**| id of legacy feature | 

### Return type

[**LegacyFeature**](LegacyFeature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_backup_configuration**
> BackupConfiguration update_backup_configuration(body)

update backup configuration

### Update Looker Backup Configuration 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConfigApi()
body = lookerpy.BackupConfiguration() # BackupConfiguration | Options for Backup Configuration

try: 
    # update backup configuration
    api_response = api_instance.update_backup_configuration(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->update_backup_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupConfiguration**](BackupConfiguration.md)| Options for Backup Configuration | 

### Return type

[**BackupConfiguration**](BackupConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_legacy_feature**
> LegacyFeature update_legacy_feature(legacy_feature_id, body)

update legacy feature

### Update information about the legacy feature with a specific id.

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.ConfigApi()
legacy_feature_id = 789 # int | id of legacy feature
body = lookerpy.LegacyFeature() # LegacyFeature | legacy feature

try: 
    # update legacy feature
    api_response = api_instance.update_legacy_feature(legacy_feature_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->update_legacy_feature: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_feature_id** | **int**| id of legacy feature | 
 **body** | [**LegacyFeature**](LegacyFeature.md)| legacy feature | 

### Return type

[**LegacyFeature**](LegacyFeature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


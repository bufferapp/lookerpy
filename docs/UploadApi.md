# lookerpy.UploadApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_uploads**](UploadApi.md#all_uploads) | **GET** /uploads | get all uploads
[**create_upload**](UploadApi.md#create_upload) | **POST** /uploads | Upload a csv file and return the inferred table definition
[**delete_upload**](UploadApi.md#delete_upload) | **DELETE** /uploads/{upload_id} | Delete UploadTable and drop upload created table if exists
[**get_upload**](UploadApi.md#get_upload) | **GET** /uploads/{upload_id} | Get table definition for an upload
[**get_upload_lookml**](UploadApi.md#get_upload_lookml) | **GET** /uploads/{upload_id}/lookml | Get the generated lookml for a table created via upload
[**load_upload**](UploadApi.md#load_upload) | **POST** /uploads/{upload_id} | Upload contents of a file to create and load a table in the DB
[**update_upload**](UploadApi.md#update_upload) | **PUT** /uploads/{upload_id} | Update upload table definition and create/load the DB table


# **all_uploads**
> list[UploadTable] all_uploads()

get all uploads

### Get information about all uploaded tables. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UploadApi()

try: 
    # get all uploads
    api_response = api_instance.all_uploads()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UploadApi->all_uploads: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UploadTable]**](UploadTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload**
> UploadTable create_upload(body)

Upload a csv file and return the inferred table definition

### Upload a csv file for user defined table generation/load. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UploadApi()
body = lookerpy.UploadTable() # UploadTable | UploadTable

try: 
    # Upload a csv file and return the inferred table definition
    api_response = api_instance.create_upload(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UploadApi->create_upload: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UploadTable**](UploadTable.md)| UploadTable | 

### Return type

[**UploadTable**](UploadTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_upload**
> bool delete_upload(upload_id)

Delete UploadTable and drop upload created table if exists

### Drop the uploaded table with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UploadApi()
upload_id = 789 # int | Id of uploaded table

try: 
    # Delete UploadTable and drop upload created table if exists
    api_response = api_instance.delete_upload(upload_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UploadApi->delete_upload: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **int**| Id of uploaded table | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload**
> UploadTable get_upload(upload_id)

Get table definition for an upload

### Get information about the specified upload table 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UploadApi()
upload_id = 789 # int | Id of uploaded table

try: 
    # Get table definition for an upload
    api_response = api_instance.get_upload(upload_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UploadApi->get_upload: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **int**| Id of uploaded table | 

### Return type

[**UploadTable**](UploadTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_lookml**
> str get_upload_lookml(upload_id)

Get the generated lookml for a table created via upload

### Get the generated lookML for an uploaded table  **License feature may not be available on your Looker Beta feature not frozen**  

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UploadApi()
upload_id = 789 # int | Id of uploaded table

try: 
    # Get the generated lookml for a table created via upload
    api_response = api_instance.get_upload_lookml(upload_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UploadApi->get_upload_lookml: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **int**| Id of uploaded table | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_upload**
> UploadTable load_upload(upload_id, body)

Upload contents of a file to create and load a table in the DB

### Upload contents of file for user defined table generation/load. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UploadApi()
upload_id = 789 # int | Id of upload table
body = 'body_example' # str | File contents

try: 
    # Upload contents of a file to create and load a table in the DB
    api_response = api_instance.load_upload(upload_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UploadApi->load_upload: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **int**| Id of upload table | 
 **body** | **str**| File contents | 

### Return type

[**UploadTable**](UploadTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, text/csv
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_upload**
> UploadTable update_upload(upload_id, body)

Update upload table definition and create/load the DB table

### Update the upload table definition and create/load the DB table 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.UploadApi()
upload_id = 789 # int | Id of upload table
body = lookerpy.UploadTable() # UploadTable | Specified upload table

try: 
    # Update upload table definition and create/load the DB table
    api_response = api_instance.update_upload(upload_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UploadApi->update_upload: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **int**| Id of upload table | 
 **body** | [**UploadTable**](UploadTable.md)| Specified upload table | 

### Return type

[**UploadTable**](UploadTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


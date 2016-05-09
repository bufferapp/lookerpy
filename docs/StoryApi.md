# lookerpy.StoryApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_stories**](StoryApi.md#all_stories) | **GET** /stories | Get all stories
[**story**](StoryApi.md#story) | **GET** /stories/{story_id} | Get a story
[**story_assets**](StoryApi.md#story_assets) | **GET** /stories/assets | Get assets used by stories


# **all_stories**
> list[StoryListItem] all_stories()

Get all stories

### Get a list of all of the stories (without the html). 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.StoryApi()

try: 
    # Get all stories
    api_response = api_instance.all_stories()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StoryApi->all_stories: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StoryListItem]**](StoryListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **story**
> Story story(story_id)

Get a story

### Get the story with a specific id. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.StoryApi()
story_id = 'story_id_example' # str | Id of story

try: 
    # Get a story
    api_response = api_instance.story(story_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StoryApi->story: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_id** | **str**| Id of story | 

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **story_assets**
> StoryAssets story_assets()

Get assets used by stories

### Get the assets for stories. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.StoryApi()

try: 
    # Get assets used by stories
    api_response = api_instance.story_assets()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StoryApi->story_assets: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoryAssets**](StoryAssets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


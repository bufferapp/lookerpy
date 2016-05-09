# lookerpy.QueryApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_query**](QueryApi.md#create_query) | **POST** /queries | create query
[**create_query_and_run_async**](QueryApi.md#create_query_and_run_async) | **POST** /queries/run_async | Create a Query and run it asynchronously.
[**query**](QueryApi.md#query) | **GET** /queries/{query_id} | get query
[**query_for_slug**](QueryApi.md#query_for_slug) | **GET** /queries/slug/{slug} | get query for slug
[**query_task**](QueryApi.md#query_task) | **GET** /query_tasks/{query_task_id} | Get a Query Task
[**query_task_multi_results**](QueryApi.md#query_task_multi_results) | **GET** /query_tasks/multi_results | Get multiple query task results in one request.
[**query_task_results**](QueryApi.md#query_task_results) | **GET** /query_tasks/{query_task_id}/results | Get a Query Task&#39;s results
[**run_async**](QueryApi.md#run_async) | **POST** /queries/{query_id}/run_async | Run a Query asynchronously.
[**run_inline_query**](QueryApi.md#run_inline_query) | **POST** /queries/run/{format} | run inline query
[**run_query**](QueryApi.md#run_query) | **GET** /queries/{query_id}/run/{format} | run query
[**run_url_encoded_query**](QueryApi.md#run_url_encoded_query) | **GET** /queries/models/{model_name}/views/{view_name}/run/{format} | run url encoded query


# **create_query**
> Query create_query(body=body)

create query

### Create a query.  This allows you to create a new query that you can later run. Looker queries are immutable once created and are not deleted. If you create a query that is exactly like an existing query then the existing query will be returned and no new query will be created. Whether a new query is created or not, you can use the 'id' in the returned query with the 'run' method.  The query parameters are passed as json in the body of the request.  

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
body = lookerpy.Query() # Query | query (optional)

try: 
    # create query
    api_response = api_instance.create_query(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->create_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Query**](Query.md)| query | [optional] 

### Return type

[**Query**](Query.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_query_and_run_async**
> AsyncQuery create_query_and_run_async(body, format=format)

Create a Query and run it asynchronously.

Given a set of properties for a Query, fetches or creates the Query and starts running it asynchronously. The Query Task results endpoint can be used to fetch the query. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
body = lookerpy.Query() # Query | Query data
format = 'format_example' # str | Format of the response. Default is json. (optional)

try: 
    # Create a Query and run it asynchronously.
    api_response = api_instance.create_query_and_run_async(body, format=format)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->create_query_and_run_async: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Query**](Query.md)| Query data | 
 **format** | **str**| Format of the response. Default is json. | [optional] 

### Return type

[**AsyncQuery**](AsyncQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> Query query(query_id, fields=fields)

get query

### Get a previously created query by id.  A Looker query object includes the various parameters that define a database query that has been run or could be run in the future. These parameters include: model, view, fields, filters, pivots, etc. Query *results* are not part of the query object.  Query objects are unique and immutable. Query objects are created automatically in Looker as users explore data. Looker does not delete them; they become part of the query history. When asked to create a query for any given set of parameters, Looker will first try to find an existing query object with matching parameters and will only create a new object when an appropriate object can not be found.  This 'get' method is used to get the details about a query for a given id. See the other methods here to 'create' and 'run' queries.  Note that some fields like 'filter_config' and 'vis_config' etc are specific to how the Looker UI builds queries and visualizations and are not generally useful for API use. They are not required when creating new queries and can usually just be ignored.  

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
query_id = 789 # int | Id of query
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get query
    api_response = api_instance.query(query_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **int**| Id of query | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Query**](Query.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_for_slug**
> Query query_for_slug(slug, fields=fields)

get query for slug

### Get the query for a given query slug.  This returns the query for the 'slug' in a query share URL.  The 'slug' is a randomly chosen short string that is used as an alternative to the query's id value for use in URLs etc. This method exists as a convenience to help you use the API to 'find' queries that have been created using the Looker UI.  You can use the Looker explore page to build a query and then choose the 'Share' option to show the share url for the query. Share urls generally look something like 'https://looker.yourcompany/x/vwGSbfc'. The trailing 'vwGSbfc' is the share slug. You can pass that string to this api method to get details about the query. Those details include the 'id' that you can use to run the query. Or, you can copy the query body (perhaps with your own modification) and use that as the basis to make/run new queries.  

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
slug = 'slug_example' # str | Slug of query
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get query for slug
    api_response = api_instance.query_for_slug(slug, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->query_for_slug: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug of query | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Query**](Query.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_task**
> RunningQueries query_task(query_task_id, fields=fields)

Get a Query Task

Fetch a Query Task.  Query Tasks are generated by running queries asynchronously. They are represented by a GUID returned from one of the async query endpoints. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
query_task_id = 'query_task_id_example' # str | ID of the Query Task
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # Get a Query Task
    api_response = api_instance.query_task(query_task_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->query_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_task_id** | **str**| ID of the Query Task | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**RunningQueries**](RunningQueries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_task_multi_results**
> str query_task_multi_results(query_task_ids)

Get multiple query task results in one request.

Fetch a multiple Query Task results at once. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
query_task_ids = ['query_task_ids_example'] # list[str] | List of Query Task IDs

try: 
    # Get multiple query task results in one request.
    api_response = api_instance.query_task_multi_results(query_task_ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->query_task_multi_results: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_task_ids** | [**list[str]**](str.md)| List of Query Task IDs | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_task_results**
> str query_task_results(query_task_id)

Get a Query Task's results

Fetch a Query Task's results. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
query_task_id = 'query_task_id_example' # str | ID of the Query Task

try: 
    # Get a Query Task's results
    api_response = api_instance.query_task_results(query_task_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->query_task_results: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_task_id** | **str**| ID of the Query Task | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_async**
> AsyncQuery run_async(query_id, body=body)

Run a Query asynchronously.

### Run a saved query asynchronously.  Runs a previously created query asynchronously. Returns a Query Task ID which can be used to fetch the results from the Query Tasks results endpoint.  

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
query_id = 789 # int | ID of query
body = lookerpy.AsyncQuery() # AsyncQuery | async query run (optional)

try: 
    # Run a Query asynchronously.
    api_response = api_instance.run_async(query_id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->run_async: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **int**| ID of query | 
 **body** | [**AsyncQuery**](AsyncQuery.md)| async query run | [optional] 

### Return type

[**AsyncQuery**](AsyncQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_inline_query**
> str run_inline_query(format, body, limit=limit, apply_formatting=apply_formatting, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production)

run inline query

### Run the query that is specified inline in the posted body.  This allows running a query as defined in json in the posted body. This combines the two actions of posting & running a query into one step.  Here is an example body in json: ``` {   "model":"thelook",   "view":"inventory_items",   "fields":["category.name","inventory_items.days_in_inventory_tier","products.count"],   "filters":{"category.name":"socks"},   "sorts":["products.count desc 0"],   "limit":"500",   "query_timezone":"America/Los_Angeles" } ```  When using the Ruby SDK this would be passed as a Ruby hash like: ``` {  :model=>"thelook",  :view=>"inventory_items",  :fields=>   ["category.name",    "inventory_items.days_in_inventory_tier",    "products.count"],  :filters=>{:"category.name"=>"socks"},  :sorts=>["products.count desc 0"],  :limit=>"500",  :query_timezone=>"America/Los_Angeles", } ```  This will return the result of running the query in the format specified by the 'format' paramater.  Suported formats: - json - plain json - csv - comma separated values with a header - txt - tab separated values with a header - html - simple html - md - simple markdown - sql - shows the generated SQL rather than running the query - png - a PNG image of the visualization of the query - jpg - a JPG image of the visualization of the query - unified - json that is annotated with additional metadata as used by the Looker web application   

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
format = 'format_example' # str | Format of result
body = lookerpy.Query() # Query | inline query
limit = 789 # int | Row limit (may override the limit in the saved query). (optional)
apply_formatting = true # bool | Apply model-specified formatting to each result. (optional)
cache = true # bool | Get results from cache if available. (optional)
image_width = 789 # int | Render width for image formats. (optional)
image_height = 789 # int | Render height for image formats. (optional)
generate_drill_links = true # bool | Generate drill links (only applicable to 'unified' format. (optional)
force_production = true # bool | Force use of production models even if the user is in developer mode. (optional)

try: 
    # run inline query
    api_response = api_instance.run_inline_query(format, body, limit=limit, apply_formatting=apply_formatting, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->run_inline_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Format of result | 
 **body** | [**Query**](Query.md)| inline query | 
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

# **run_query**
> str run_query(query_id, format, limit=limit, apply_formatting=apply_formatting, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production)

run query

### Run a saved query.  This runs a previously saved query. You can use this on a query that was generated in the Looker UI or one that you have explicitly created using the API. You can also use a query 'id' from a saved 'Look'.  This will return the result of running the query in the format specified by the 'format' paramater.  Suported formats: - json - plain json - csv - comma separated values with a header - txt - tab separated values with a header - html - simple html - md - simple markdown - sql - shows the generated SQL rather than running the query - png - a PNG image of the visualization of the query - jpg - a JPG image of the visualization of the query - unified - json that is annotated with additional metadata as used by the Looker web application   

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
query_id = 789 # int | Id of query
format = 'format_example' # str | Format of result
limit = 789 # int | Row limit (may override the limit in the saved query). (optional)
apply_formatting = true # bool | Apply model-specified formatting to each result. (optional)
cache = true # bool | Get results from cache if available. (optional)
image_width = 789 # int | Render width for image formats. (optional)
image_height = 789 # int | Render height for image formats. (optional)
generate_drill_links = true # bool | Generate drill links (only applicable to 'unified' format. (optional)
force_production = true # bool | Force use of production models even if the user is in developer mode. (optional)

try: 
    # run query
    api_response = api_instance.run_query(query_id, format, limit=limit, apply_formatting=apply_formatting, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->run_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **int**| Id of query | 
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

# **run_url_encoded_query**
> str run_url_encoded_query(model_name, view_name, format)

run url encoded query

### Run an URL encoded query.  This requires the caller to encode the specifiers for the query into the URL query part using Looker-specific syntax as explained below.  Generally, you would want to use one of the methods that takes the parameters as json in the POST body for creating and/or running queries. This method exists for cases where one really needs to encode the paramaters into the URL of a single 'GET' request. This matches the way that the Looker UI formats 'explore' URLs etc.  The parameters here are very similar to the json body formatting except that the filter syntax is tricky. Unfortunately, this format makes this method not currently callible via the 'Try it out!' button in this documentation page. But, this is callable  when creating URLs manually or when using the Looker SDK.  Here is an example inline query URL:  "https://looker.mycompany.com:19999/api/3.0/queries/models/thelook/views/inventory_items/run/json?fields=category.name,inventory_items.days_in_inventory_tier,products.count&f[category.name]=socks&sorts=products.count+desc+0&limit=500&query_timezone=America/Los_Angeles"  When calling the Ruby SDK, one passes the query parameter parts as a hash. The hash to match the above would like like:  ``` {   :fields => "category.name,inventory_items.days_in_inventory_tier,products.count",   :"f[category.name]" => "socks",   :sorts => "products.count desc 0",   :limit => "500",   :query_timezone => "America/Los_Angeles" } ```  Again, it is generally easier to use the variant of this method that passes the full query in the POST body. This method is available for cases where other alternatives won't fit the need.  Suported formats: - json - plain json - csv - comma separated values with a header - txt - tab separated values with a header - html - simple html - md - simple markdown - sql - shows the generated SQL rather than running the query - png - a PNG image of the visualization of the query - jpg - a JPG image of the visualization of the query - unified - json that is annotated with additional metadata as used by the Looker web application   

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.QueryApi()
model_name = 'model_name_example' # str | Model name
view_name = 'view_name_example' # str | View name
format = 'format_example' # str | Format of result

try: 
    # run url encoded query
    api_response = api_instance.run_url_encoded_query(model_name, view_name, format)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->run_url_encoded_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| Model name | 
 **view_name** | **str**| View name | 
 **format** | **str**| Format of result | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text, application/json, image/png, image/jpg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


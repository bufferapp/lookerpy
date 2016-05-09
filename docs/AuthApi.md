# lookerpy.AuthApi

All URIs are relative to *https://looker.buffer.com:19999/api/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_embed_secrets**](AuthApi.md#all_embed_secrets) | **GET** /embed_config/secrets | get all embed secrets
[**check_embed_domain**](AuthApi.md#check_embed_domain) | **PUT** /embed_config/check_domain | check embed domain
[**create_embed_secret**](AuthApi.md#create_embed_secret) | **POST** /embed_config/secrets | create embed secret
[**create_saml_test_config**](AuthApi.md#create_saml_test_config) | **POST** /saml_test_configs | create saml test configuration
[**delete_embed_secret**](AuthApi.md#delete_embed_secret) | **DELETE** /embed_config/secrets/{embed_secret_id} | delete embed secret
[**delete_saml_test_config**](AuthApi.md#delete_saml_test_config) | **DELETE** /saml_test_configs/{test_slug} | delete saml test configuration
[**embed_config**](AuthApi.md#embed_config) | **GET** /embed_config | get embed config
[**embed_secret**](AuthApi.md#embed_secret) | **GET** /embed_config/secrets/{embed_secret_id} | get embed secret
[**fetch_and_parse_saml_idp_metadata**](AuthApi.md#fetch_and_parse_saml_idp_metadata) | **POST** /fetch_and_parse_saml_idp_metadata | fetch and parse saml idp metadata xml
[**ldap_config**](AuthApi.md#ldap_config) | **GET** /ldap_config | get ldap configuration
[**parse_saml_idp_metadata**](AuthApi.md#parse_saml_idp_metadata) | **POST** /parse_saml_idp_metadata | parse saml idp metadata xml
[**saml_config**](AuthApi.md#saml_config) | **GET** /saml_config | get saml configuration
[**saml_test_config**](AuthApi.md#saml_test_config) | **GET** /saml_test_configs/{test_slug} | get saml test configuration
[**test_ldap_config_auth**](AuthApi.md#test_ldap_config_auth) | **PUT** /ldap_config/test_auth | test ldap auth config
[**test_ldap_config_connection**](AuthApi.md#test_ldap_config_connection) | **PUT** /ldap_config/test_connection | test ldap connection config
[**test_ldap_config_user_auth**](AuthApi.md#test_ldap_config_user_auth) | **PUT** /ldap_config/test_user_auth | test ldap user auth config
[**test_ldap_config_user_info**](AuthApi.md#test_ldap_config_user_info) | **PUT** /ldap_config/test_user_info | test ldap user info config
[**update_embed_config**](AuthApi.md#update_embed_config) | **PATCH** /embed_config | update embed config
[**update_embed_secret**](AuthApi.md#update_embed_secret) | **PATCH** /embed_config/secrets/{embed_secret_id} | update embed secret
[**update_ldap_config**](AuthApi.md#update_ldap_config) | **PATCH** /ldap_config | update ldap configuration
[**update_saml_config**](AuthApi.md#update_saml_config) | **PATCH** /saml_config | update saml configuration


# **all_embed_secrets**
> list[EmbedSecret] all_embed_secrets(fields=fields)

get all embed secrets

### Get information about all embed secrets. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get all embed secrets
    api_response = api_instance.all_embed_secrets(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->all_embed_secrets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[EmbedSecret]**](EmbedSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_embed_domain**
> EmbedCheckDomainResult check_embed_domain(domain=domain)

check embed domain

### Check to see if the proposed domain is allowed based on the embed configuration.  The domain must start with 'http://' or 'https://'. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
domain = 'domain_example' # str | Domain to check. (optional)

try: 
    # check embed domain
    api_response = api_instance.check_embed_domain(domain=domain)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->check_embed_domain: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain to check. | [optional] 

### Return type

[**EmbedCheckDomainResult**](EmbedCheckDomainResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embed_secret**
> EmbedSecret create_embed_secret(body=body)

create embed secret

### Create an embed secret using the specified information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = lookerpy.EmbedSecret() # EmbedSecret | embed secret (optional)

try: 
    # create embed secret
    api_response = api_instance.create_embed_secret(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->create_embed_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmbedSecret**](EmbedSecret.md)| embed secret | [optional] 

### Return type

[**EmbedSecret**](EmbedSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_saml_test_config**
> SamlConfig create_saml_test_config(body)

create saml test configuration

### Create a SAML test configuration. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = lookerpy.SamlConfig() # SamlConfig | SAML test config

try: 
    # create saml test configuration
    api_response = api_instance.create_saml_test_config(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->create_saml_test_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamlConfig**](SamlConfig.md)| SAML test config | 

### Return type

[**SamlConfig**](SamlConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_embed_secret**
> str delete_embed_secret(embed_secret_id)

delete embed secret

### Delete an embed secret. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
embed_secret_id = 789 # int | Id of Embed Secret

try: 
    # delete embed secret
    api_response = api_instance.delete_embed_secret(embed_secret_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->delete_embed_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embed_secret_id** | **int**| Id of Embed Secret | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saml_test_config**
> str delete_saml_test_config(test_slug)

delete saml test configuration

### Delete a SAML test configuration. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
test_slug = 'test_slug_example' # str | Slug of test config

try: 
    # delete saml test configuration
    api_response = api_instance.delete_saml_test_config(test_slug)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->delete_saml_test_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_slug** | **str**| Slug of test config | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **embed_config**
> EmbedConfig embed_config(fields=fields)

get embed config

### Get the embed configuration. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get embed config
    api_response = api_instance.embed_config(fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->embed_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**EmbedConfig**](EmbedConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **embed_secret**
> EmbedSecret embed_secret(embed_secret_id, fields=fields)

get embed secret

### Get information about an embed secret. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
embed_secret_id = 789 # int | Id of Embed Secret
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # get embed secret
    api_response = api_instance.embed_secret(embed_secret_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->embed_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embed_secret_id** | **int**| Id of Embed Secret | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**EmbedSecret**](EmbedSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_and_parse_saml_idp_metadata**
> SamlMetadataParseResult fetch_and_parse_saml_idp_metadata(body)

fetch and parse saml idp metadata xml

### Fetch the given url and parse it as a Saml IdP metadata document and return the result. Note that this requires that the url be public or at least at a location where the Looker instance can fetch it without requiring any special authentication. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = 'body_example' # str | SAML IdP metadata public url

try: 
    # fetch and parse saml idp metadata xml
    api_response = api_instance.fetch_and_parse_saml_idp_metadata(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->fetch_and_parse_saml_idp_metadata: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SAML IdP metadata public url | 

### Return type

[**SamlMetadataParseResult**](SamlMetadataParseResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_config**
> LDAPConfig ldap_config()

get ldap configuration

### Get the LDAP configuration.  Looker can be optionally configured to authenticate users against an Active Directory or other LDAP directory server. LDAP setup requires coordination with an administrator of that directory server.  Only Looker administrators can read and update the LDAP configuration.  Configuring LDAP impacts authentication for all users. This configuration should be done carefully.  Looker maintains a single LDAP configuation. It can be read and updated.       Updates only succeed if the new state will be valid (in the sense that all required fields are populated);       it is up to you to ensure that the configuration is appropriate and correct).  LDAP is enabled or disabled for Looker using the **enabled** field.  Looker will never return an **auth_password** field. That value can be set, but never retreived.  See the [Looker LDAP docs]( http://www.looker.com/docs/admin/security/ldap-setup) for additional information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()

try: 
    # get ldap configuration
    api_response = api_instance.ldap_config()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->ldap_config: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LDAPConfig**](LDAPConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_saml_idp_metadata**
> SamlMetadataParseResult parse_saml_idp_metadata(body)

parse saml idp metadata xml

### Parse the given xml as a Saml IdP metadata document and return the result. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = 'body_example' # str | SAML IdP metadata xml

try: 
    # parse saml idp metadata xml
    api_response = api_instance.parse_saml_idp_metadata(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->parse_saml_idp_metadata: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| SAML IdP metadata xml | 

### Return type

[**SamlMetadataParseResult**](SamlMetadataParseResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **saml_config**
> SamlConfig saml_config()

get saml configuration

### Get the SAML configuration.  Looker can be optionally configured to authenticate users against a SAML authentication server. SAML setup requires coordination with an administrator of that server.  Only Looker administrators can read and update the SAML configuration.  Configuring SAML impacts authentication for all users. This configuration should be done carefully.  Looker maintains a single SAML configuation. It can be read and updated.       Updates only succeed if the new state will be valid (in the sense that all required fields are populated);       it is up to you to ensure that the configuration is appropriate and correct).  SAML is enabled or disabled for Looker using the **enabled** field. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()

try: 
    # get saml configuration
    api_response = api_instance.saml_config()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->saml_config: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SamlConfig**](SamlConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **saml_test_config**
> SamlConfig saml_test_config(test_slug)

get saml test configuration

### Get a SAML test configuration by test_slug. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
test_slug = 'test_slug_example' # str | Slug of test config

try: 
    # get saml test configuration
    api_response = api_instance.saml_test_config(test_slug)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->saml_test_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_slug** | **str**| Slug of test config | 

### Return type

[**SamlConfig**](SamlConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_ldap_config_auth**
> LDAPConfigTestResult test_ldap_config_auth(body)

test ldap auth config

### Test the connection authentication settings for an LDAP configuration.  This tests that the connection is possible and that a 'server' account to be used by Looker can       authenticate to the LDAP server given connection and authentication information.  **connection_host**, **connection_port**, and **auth_username**, are required.       **connection_tls** and **auth_password** are optional.  Example: ```json {   "connection_host": "ldap.example.com",   "connection_port": "636",   "connection_tls": true,   "auth_username": "cn=looker,dc=example,dc=com",   "auth_password": "secret" } ```  Looker will never return an **auth_password**. If this request omits the **auth_password** field, then       the **auth_password** value from the active config (if present) will be used for the test.  The active LDAP settings are not modified.  

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = lookerpy.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # test ldap auth config
    api_response = api_instance.test_ldap_config_auth(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->test_ldap_config_auth: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfigTestResult**](LDAPConfigTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_ldap_config_connection**
> LDAPConfigTestResult test_ldap_config_connection(body)

test ldap connection config

### Test the connection settings for an LDAP configuration.  This tests that the connection is possible given a connection_host and connection_port.  **connection_host** and **connection_port** are required. **connection_tls** is optional.  Example: ```json {   "connection_host": "ldap.example.com",   "connection_port": "636",   "connection_tls": true } ```  No authentication to the LDAP server is attempted.  The active LDAP settings are not modified. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = lookerpy.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # test ldap connection config
    api_response = api_instance.test_ldap_config_connection(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->test_ldap_config_connection: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfigTestResult**](LDAPConfigTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_ldap_config_user_auth**
> LDAPConfigTestResult test_ldap_config_user_auth(body)

test ldap user auth config

### Test the user authentication settings for an LDAP configuration.  This test accepts a full LDAP configuration along with a username/password pair and attempts to       authenticate the user with the LDAP server. The configuration is validated before attempting the       authentication.  Looker will never return an **auth_password**. If this request omits the **auth_password** field, then       the **auth_password** value from the active config (if present) will be used for the test.  **test_ldap_user** and **test_ldap_password** are required.  The active LDAP settings are not modified.  

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = lookerpy.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # test ldap user auth config
    api_response = api_instance.test_ldap_config_user_auth(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->test_ldap_config_user_auth: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfigTestResult**](LDAPConfigTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_ldap_config_user_info**
> LDAPConfigTestResult test_ldap_config_user_info(body)

test ldap user info config

### Test the user authentication settings for an LDAP configuration without authenticating the user.  This test will let you easily test the mapping for user properties and roles for any user without      needing to authenticate as that user.  This test accepts a full LDAP configuration along with a username and attempts to find the full info      for the user from the LDAP server without actually authenticating the user. So, user password is not      required.The configuration is validated before attempting to contact the server.  **test_ldap_user** is required.  The active LDAP settings are not modified.  

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = lookerpy.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # test ldap user info config
    api_response = api_instance.test_ldap_config_user_info(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->test_ldap_config_user_info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfigTestResult**](LDAPConfigTestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_embed_config**
> EmbedConfig update_embed_config(body, fields=fields)

update embed config

### Update the embed configuration. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = lookerpy.EmbedConfig() # EmbedConfig | embed config
fields = 'fields_example' # str | Requested fields. (optional)

try: 
    # update embed config
    api_response = api_instance.update_embed_config(body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->update_embed_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmbedConfig**](EmbedConfig.md)| embed config | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**EmbedConfig**](EmbedConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_embed_secret**
> EmbedSecret update_embed_secret(embed_secret_id, body)

update embed secret

### Update an embed secret using the specified information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
embed_secret_id = 789 # int | Id of Embed Secret
body = lookerpy.EmbedSecret() # EmbedSecret | embed secret

try: 
    # update embed secret
    api_response = api_instance.update_embed_secret(embed_secret_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->update_embed_secret: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embed_secret_id** | **int**| Id of Embed Secret | 
 **body** | [**EmbedSecret**](EmbedSecret.md)| embed secret | 

### Return type

[**EmbedSecret**](EmbedSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ldap_config**
> LDAPConfig update_ldap_config(body)

update ldap configuration

### Update the LDAP configuration.  Configuring LDAP impacts authentication for all users. This configuration should be done carefully.  Only Looker administrators can read and update the LDAP configuration.  LDAP is enabled or disabled for Looker using the **enabled** field.  It is **highly** recommended that any LDAP setting changes be tested using the APIs below before being set globally.  See the [Looker LDAP docs]( http://www.looker.com/docs/admin/security/ldap-setup) for additional information. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = lookerpy.LDAPConfig() # LDAPConfig | LDAP Config

try: 
    # update ldap configuration
    api_response = api_instance.update_ldap_config(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->update_ldap_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LDAPConfig**](LDAPConfig.md)| LDAP Config | 

### Return type

[**LDAPConfig**](LDAPConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saml_config**
> SamlConfig update_saml_config(body)

update saml configuration

### Update the SAML configuration.  Configuring SAML impacts authentication for all users. This configuration should be done carefully.  Only Looker administrators can read and update the SAML configuration.  SAML is enabled or disabled for Looker using the **enabled** field.  It is **highly** recommended that any SAML setting changes be tested using the APIs below before being set globally. 

### Example 
```python
import time
import lookerpy
from lookerpy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lookerpy.AuthApi()
body = lookerpy.SamlConfig() # SamlConfig | SAML Config

try: 
    # update saml configuration
    api_response = api_instance.update_saml_config(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthApi->update_saml_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SamlConfig**](SamlConfig.md)| SAML Config | 

### Return type

[**SamlConfig**](SamlConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# LDAPConfigTestResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Test status code: always &#39;success&#39; or &#39;error&#39; | [optional] 
**message** | **str** | Short human readable test about the result | [optional] 
**details** | **str** | Additional details for error cases | [optional] 
**user** | [**LDAPUser**](LDAPUser.md) | User details from LDAP server for auth tests | [optional] 
**trace** | **str** | A more detailed trace incremental results during auth tests | [optional] 
**url** | **str** | Link to ldap config | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



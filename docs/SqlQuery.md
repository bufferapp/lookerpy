# SqlQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The identifier of the SQL query | [optional] 
**last_runtime** | **float** | Number of seconds this query took to run the most recent time it was run | [optional] 
**run_count** | **int** | Number of times this query has been run | [optional] 
**browser_limit** | **int** | Maximum number of rows this query will display on the SQL Runner page | [optional] 
**sql** | **str** | SQL query text | [optional] 
**last_run_at** | **str** | The most recent time this query was run | [optional] 
**connection** | [**DBConnectionBase**](DBConnectionBase.md) | Connection this query uses | [optional] 
**creator** | [**UserPublic**](UserPublic.md) | User who created this SQL query | [optional] 
**explore_url** | **str** | Explore page URL for this SQL query | [optional] 
**plaintext** | **bool** | Should this query be rendered as plain text | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DBConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the connection. Also used as the unique identifier | [optional] 
**host** | **str** | Host name/address of server | [optional] 
**port** | **str** | Port number on server | [optional] 
**username** | **str** | Username for server authentication | [optional] 
**password** | **str** | (Write-only) Password for server authentication | [optional] 
**certificate** | **str** | (Write-only) Base64 encoded Certificate body for server authentication (when appropriate for dialect). | [optional] 
**database** | **str** | Database name | [optional] 
**db_timezone** | **str** | Time zone of database | [optional] 
**query_timezone** | **str** | Timezone to use in queries | [optional] 
**schema** | **str** | Scheme name | [optional] 
**max_connections** | **int** | Maximum number of concurrent connection to use | [optional] 
**ssl** | **bool** | Use SSL/TLS when connecting to server | [optional] 
**verify_ssl** | **bool** | Verify the SSL | [optional] 
**tmp_db_name** | **str** | Name of temporary database (if used) | [optional] 
**jdbc_additional_params** | **str** | Additional params to add to JDBC connection string | [optional] 
**pool_timeout** | **int** | Pool Timeout | [optional] 
**dialect** | [**Dialect**](Dialect.md) | (Read-only) SQL Dialect details | [optional] 
**dialect_name** | **str** | (Read/Write) SQL Dialect name | [optional] 
**snippets** | **str** | SQL Runner snippets for this connection | [optional] 
**created_at** | **str** | Creation date for this connection | [optional] 
**user_id** | **str** | Id of user who last modified this connection configuration | [optional] 
**example** | **bool** | Is this an example connection | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



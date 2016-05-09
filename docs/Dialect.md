# Dialect

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the dialect | [optional] 
**label** | **str** | The human-readable label of the connection | [optional] 
**supports_cost_estimate** | **bool** | Whether the dialect supports query cost estimates | [optional] 
**supports_upload_tables** | **bool** | Whether the dialect supports uploading tables | [optional] 
**persistent_table_indexes** | **str** | PDT index columns | [optional] 
**persistent_table_sortkeys** | **str** | PDT sortkey columns | [optional] 
**persistent_table_distkey** | **str** | PDT distkey column | [optional] 
**supports_streaming** | **bool** | Suports streaming results | [optional] 
**automatically_run_sql_runner_snippets** | **bool** | Should SQL Runner snippets automatically be run | [optional] 
**connection_tests** | **list[str]** | Array of names of the tests that can be run on a connection using this dialect | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



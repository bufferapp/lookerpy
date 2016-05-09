# ScheduledPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**name** | **str** | Name | [optional] 
**title** | **str** | Title | [optional] 
**user** | [**UserPublic**](UserPublic.md) | User who owns this ScheduledPlan | [optional] 
**enabled** | **bool** | Whether the ScheduledPlan is enabled | [optional] 
**last_run_at** | **datetime** | When the ScheduledPlan was last run | [optional] 
**next_run_at** | **datetime** | When the ScheduledPlan will next run | [optional] 
**look_id** | **int** | Id of a look | [optional] 
**dashboard_id** | **int** | Id of a dashboard | [optional] 
**lookml_dashboard_id** | **str** | Id of a LookML dashboard | [optional] 
**require_results** | **bool** | Delivery should occur if running the dashboard or look returns results | [optional] 
**require_no_results** | **bool** | Delivery should occur if the dashboard look does not return results | [optional] 
**require_change** | **bool** | Delivery should occur if data have changed since the last run | [optional] 
**crontab** | **str** | Vixie-Style crontab specification when to run | [optional] 
**timezone** | **str** | Timezone for interpreting the specified crontab (default is Looker instance timezone) | [optional] 
**scheduled_plan_destination** | [**list[ScheduledPlanDestination]**](ScheduledPlanDestination.md) | Scheduled plan destinations | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ScheduledJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**status** | **str** | Status of the job | [optional] 
**status_detail** | **str** | Optional message describing status of the job | [optional] 
**scheduled_job_stage** | [**list[ScheduledJobStage]**](ScheduledJobStage.md) | Detailed information about the job stage | [optional] 
**row_limit_reached** | **str** | Whether the row limit was reached when running | [optional] 
**created_at** | **datetime** | When the ScheduledJob started | [optional] 
**finalized_at** | **datetime** | When the ScheduledJob finished | [optional] 
**user** | [**UserPublic**](UserPublic.md) | User who owns this ScheduledPlan | [optional] 
**look_id** | **int** | Id of a look | [optional] 
**dashboard_id** | **int** | Id of a dashboard | [optional] 
**lookml_dashboard_id** | **str** | Id of a LookML dashboard | [optional] 
**require_results** | **bool** | Delivery should occur if running the dashboard or look returns results | [optional] 
**require_no_results** | **bool** | Delivery should occur if the dashboard look does not return results | [optional] 
**require_change** | **bool** | Delivery should occur if data have changed since the last run | [optional] 
**crontab** | **str** | Vixie-Style crontab specification when to run | [optional] 
**timezone** | **str** | Timezone for interpreting the specified crontab (default is Looker instance timezone) | [optional] 
**data_slug** | **str** | Used for caching | [optional] 
**data_signature** | **str** | Used for caching | [optional] 
**name** | **str** | Name | [optional] 
**title** | **str** | Title | [optional] 
**scheduled_job_destination** | [**list[ScheduledJobDestination]**](ScheduledJobDestination.md) | Scheduled job destinations | [optional] 
**scheduled_plan** | [**ScheduledPlan**](ScheduledPlan.md) | ScheduledPlan that initiated the ScheduledJob | [optional] 
**runtime** | **int** | Runtime in seconds | [optional] 
**looker_url** | **str** | Url for the scheduled entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



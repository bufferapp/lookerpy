# DashboardFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**name** | **str** | Name of filter | [optional] 
**title** | **str** | Name of title | [optional] 
**type** | **str** | Type of filter: one of date, number, string, or field | [optional] 
**default_value** | **str** | Default value of filter | [optional] 
**model** | **str** | Model of filter (required if type &#x3D; field) | [optional] 
**explore** | **str** | Explore of filter (required if type &#x3D; field) | [optional] 
**dimension** | **str** | Dimension of filter (required if type &#x3D; field) | [optional] 
**field** | **str** | Field information | [optional] 
**listens_to_filters** | **list[str]** | Array of listeners for faceted filters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



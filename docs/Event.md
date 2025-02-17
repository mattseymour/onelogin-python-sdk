# Event


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account that triggered the event. | [optional] 
**actor_system** | **str** | Acting system that triggered the event when the actor is not a user. | [optional] 
**actor_user_id** | **int** | ID of the user whose action triggered the event. | [optional] 
**actor_user_name** | **str** | First and last name of the user whose action triggered the event. | [optional] 
**app_id** | **int** | ID of the app involved in the event, if applicable. | [optional] 
**app_name** | **str** | Name of the app involved in the event, if applicable. | [optional] 
**assuming_acting_user_id** | **int** | ID of the user who assumed the role of the acting user to trigger the event, if applicable. | [optional] 
**client_id** | **str** | Client ID used to generate the access token that made the API call that generated the event. | [optional] 
**created_at** | **str** | ISO8601 Time and date at which the event was created. This value is autogenerated by OneLogin. | [optional] 
**custom_message** | **str** | More details about the event. | [optional] 
**directory_sync_run_id** | **int** | Directory sync run ID. | [optional] 
**error_description** | **str** | Provisioning error details, if applicable. | [optional] 
**event_type_id** | **int** | Type of event triggered. | [optional] 
**group_id** | **int** | ID of a group involved in the event. | [optional] 
**group_name** | **str** | Name of a group involved in the event. | [optional] 
**id** | **int** | Event&#39;s unique ID in OneLogin. Autogenerated by OneLogin. | [optional] 
**ipaddr** | **str** | IP address of the machine used to trigger the event. | [optional] 
**notes** | **str** | More details about the event. | [optional] 
**otp_device_id** | **int** | ID of a device involved in the event. | [optional] 
**otp_device_name** | **str** | Name of a device involved in the event. | [optional] 
**policy_id** | **int** | ID of the policy involved in the event. | [optional] 
**policy_name** | **str** | Name of the policy involved in the event. | [optional] 
**resource_type_id** | **int** | ID of the resource (user, role, group, and so forth) associated with the event. | [optional] 
**role_id** | **int** | ID of a role involved in the event. | [optional] 
**role_name** | **str** | Name of a role involved in the event. | [optional] 
**user_id** | **int** | ID of the user that was acted upon to trigger the event. | [optional] 
**user_name** | **str** | Name of the user that was acted upon to trigger the event. | [optional] 
**risk_cookie_id** | **str** |  | [optional] 
**assumed_by_superadmin_or_reseller** | **int** |  | [optional] 
**certificate_id** | **int** |  | [optional] 
**mapping_id** | **int** |  | [optional] 
**radius_config_id** | **int** |  | [optional] 
**risk_score** | **int** |  | [optional] 
**param** | **str** |  | [optional] 
**adc_id** | **int** |  | [optional] 
**solved** | **bool** |  | [optional] 
**service_directory_id** | **int** |  | [optional] 
**object_id** | **int** |  | [optional] 
**user_field_id** | **int** |  | [optional] 
**risk_reasons** | **str** |  | [optional] 
**policy_type** | **str** |  | [optional] 
**resolved_at** | **str** |  | [optional] 
**trusted_idp_id** | **int** |  | [optional] 
**privilege_id** | **int** |  | [optional] 
**proxy_ip** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



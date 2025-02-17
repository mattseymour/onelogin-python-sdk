# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** | A username for the user. | [optional] 
**email** | **str** | A valid email for the user. | [optional] 
**firstname** | **str** | The user&#39;s first name. | [optional] 
**lastname** | **str** | The user&#39;s last name. | [optional] 
**title** | **str** | The user&#39;s job title. | [optional] 
**department** | **str** | The user&#39;s department. | [optional] 
**company** | **str** | The user&#39;s company. | [optional] 
**comment** | **str** | Free text related to the user. | [optional] 
**group_id** | **int** | The ID of the Group in OneLogin that the user is assigned to. | [optional] 
**role_ids** | **[int]** | A list of OneLogin Role IDs of the user | [optional] 
**phone** | **str** | The E.164 format phone number for a user. | [optional] 
**state** | **int** |  | [optional] 
**status** | **int** |  | [optional] 
**directory_id** | **int** | The ID of the OneLogin Directory of the user. | [optional] 
**trusted_idp_id** | **int** | The ID of the OneLogin Trusted IDP of the user. | [optional] 
**manager_ad_id** | **str** | The ID of the user&#39;s manager in Active Directory. | [optional] 
**manager_user_id** | **str** | The OneLogin User ID for the user&#39;s manager. | [optional] 
**samaccount_name** | **str** | The user&#39;s Active Directory username. | [optional] 
**member_of** | **str** | The user&#39;s directory membership. | [optional] 
**userprincipalname** | **str** | The principle name of the user. | [optional] 
**distinguished_name** | **str** | The distinguished name of the user. | [optional] 
**external_id** | **str** | The ID of the user in an external directory. | [optional] 
**activated_at** | **str** |  | [optional] 
**last_login** | **str** |  | [optional] 
**invitation_sent_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**preferred_locale_code** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**custom_attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**invalid_login_attempts** | **int** |  | [optional] 
**locked_until** | **str** |  | [optional] 
**password_changed_at** | **str** |  | [optional] 
**password** | **str** | The password to set for a user. | [optional] 
**password_confirmation** | **str** | Required if the password is being set. | [optional] 
**password_algorithm** | **str** | Use this when importing a password that&#39;s already hashed. Prepend the salt value to the cleartext password value before SHA-256-encoding it | [optional] 
**salt** | **str** | The salt value used with the password_algorithm. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



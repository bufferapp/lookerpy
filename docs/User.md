# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**display_name** | **str** | Full name for display (available only if both first_name and last_name are set) | [optional] 
**email** | **str** | EMail address | [optional] 
**is_disabled** | **bool** | Account has been disabled | [optional] 
**avatar_url** | **str** | URL for the avatar image (may be generic) | [optional] 
**home_space_id** | **str** | ID string for user&#39;s home space | [optional] 
**access_filters** | [**list[AccessFilter]**](AccessFilter.md) | Model access filters. | [optional] 
**credentials_email** | [**CredentialsEmail**](CredentialsEmail.md) | Email/Password login credentials | [optional] 
**credentials_totp** | [**CredentialsTotp**](CredentialsTotp.md) | Two-factor credentials | [optional] 
**credentials_ldap** | [**CredentialsLDAP**](CredentialsLDAP.md) | LDAP credentials | [optional] 
**credentials_google** | [**CredentialsGoogle**](CredentialsGoogle.md) | Google auth credentials | [optional] 
**credentials_saml** | [**CredentialsSaml**](CredentialsSaml.md) | Saml auth credentials | [optional] 
**credentials_api** | [**CredentialsApi**](CredentialsApi.md) | API user credentials | [optional] 
**credentials_api3** | [**list[CredentialsApi3]**](CredentialsApi3.md) | API 3 credentials | [optional] 
**credentials_embed** | [**list[CredentialsEmbed]**](CredentialsEmbed.md) | Embed credentials | [optional] 
**credentials_looker_openid** | [**CredentialsLookerOpenid**](CredentialsLookerOpenid.md) | LookerOpenID credentials. Used for login by Looker Analysts | [optional] 
**sessions** | [**list[Session]**](Session.md) | Active sessions | [optional] 
**role_ids** | **list[int]** | Array of ids of the roles for this user | [optional] 
**presumed_looker_employee** | **bool** | User is identified as an employee of Looker | [optional] 
**verified_looker_employee** | **bool** | User is identified as an employee of Looker who has been verified via Looker corporate authentication | [optional] 
**url** | **str** | Link to get this item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



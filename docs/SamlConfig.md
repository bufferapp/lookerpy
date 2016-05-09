# SamlConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable/Disable Saml authentication for the server | [optional] 
**idp_cert** | **str** | Identify Provider Certificate (provided by IdP) | [optional] 
**idp_url** | **str** | Identify Provider Url (provided by IdP) | [optional] 
**idp_issuer** | **str** | Identify Provider Issuer (provided by IdP) | [optional] 
**idp_audience** | **str** | Identify Provider Audience (set in IdP config). Optional in Looker. Set this only if you want Looker to validate the audience value returned by the IdP. | [optional] 
**user_attribute_map_email** | **str** | Name of user record attributes used to indicate email address field | [optional] 
**user_attribute_map_first_name** | **str** | Name of user record attributes used to indicate first name | [optional] 
**user_attribute_map_last_name** | **str** | Name of user record attributes used to indicate last name | [optional] 
**new_user_migration_types** | **str** | Merge first-time saml login to existing user account by email addresses. When a user logs in for the first time via saml this option will connect this user into their existing account by finding the account with a matching email address by testing the given types of credentials for existing users. Otherwise a new user account will be created for the user. This list (if provided) must be a comma separated list of string like &#39;email,ldap,google&#39; | [optional] 
**alternate_email_login_allowed** | **bool** | Allow alternate email-based login via &#39;/login/email&#39; for admins and for specified users with the &#39;login_special_email&#39; permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled. | [optional] 
**test_slug** | **str** | Slug to identify configurations that are created in order to run a Saml config test | [optional] 
**modified_at** | **str** | When this config was last modified | [optional] 
**modified_by** | **str** | User id of user who last modified this config | [optional] 
**default_new_user_roles** | [**Role**](Role.md) | (Read-only) Roles that will be applied to new users the first time they login via Saml | [optional] 
**default_new_user_role_ids** | **list[int]** | (Write-only) Array of ids of roles that will be applied to new users the first time they login via Saml | [optional] 
**set_roles_from_groups** | **bool** | Set user roles in Looker based on groups from Saml | [optional] 
**groups_attribute** | **str** | Name of user record attributes used to indicate groups | [optional] 
**groups** | [**SamlGroupRead**](SamlGroupRead.md) | (Read-only) Array of mappings between Saml Groups and Looker Roles | [optional] 
**groups_with_role_ids** | [**SamlGroupWrite**](SamlGroupWrite.md) | (Write-only) Array of mappings between Saml Groups and arrays of Looker Role ids | [optional] 
**auth_requires_role** | **bool** | Users will not be allowed to login at all unless a role for them is found in Saml if set to true | [optional] 
**url** | **str** | Link to get this item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



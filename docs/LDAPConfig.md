# LDAPConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable/Disable LDAP authentication for the server | [optional] 
**connection_host** | **str** | LDAP server hostname | [optional] 
**connection_port** | **str** | LDAP host port | [optional] 
**connection_tls** | **bool** | Use Transport Layer Security | [optional] 
**auth_username** | **str** | Distinguished name of LDAP account used to access the LDAP server | [optional] 
**auth_password** | **str** | (Write-only) Password for the LDAP account used to access the LDAP server | [optional] 
**has_auth_password** | **bool** | (Read-only) Has the password been set for the LDAP account used to access the LDAP server | [optional] 
**user_bind_base_dn** | **str** | Distinguished name of LDAP node used as the base for user searches | [optional] 
**user_id_attribute_names** | **str** | Name(s) of user record attributes used for matching user login id (comma separated list) | [optional] 
**user_objectclass** | **str** | (Optional) Name of user record objectclass used for finding user during login id | [optional] 
**user_attribute_map_email** | **str** | Name of user record attributes used to indicate email address field | [optional] 
**user_attribute_map_first_name** | **str** | Name of user record attributes used to indicate first name | [optional] 
**user_attribute_map_last_name** | **str** | Name of user record attributes used to indicate last name | [optional] 
**user_attribute_map_ldap_id** | **str** | Name of user record attributes used to indicate unique record id | [optional] 
**merge_new_users_by_email** | **bool** | Merge first-time ldap login to existing user account by email addresses. When a user logs in for the first time via ldap this option will connect this user into their existing account by finding the account with a matching email address. Otherwise a new user account will be created for the user. | [optional] 
**alternate_email_login_allowed** | **bool** | Allow alternate email-based login via &#39;/login/email&#39; for admins and for specified users with the &#39;login_special_email&#39; permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled. | [optional] 
**modified_at** | **str** | When this config was last modified | [optional] 
**modified_by** | **str** | User id of user who last modified this config | [optional] 
**default_new_user_roles** | [**Role**](Role.md) | (Read-only) Roles that will be applied to new users the first time they login via LDAP | [optional] 
**default_new_user_role_ids** | **list[int]** | (Write-only) Array of ids of roles that will be applied to new users the first time they login via LDAP | [optional] 
**set_roles_from_groups** | **bool** | Set user roles in Looker based on groups from LDAP | [optional] 
**groups** | [**LDAPGroupRead**](LDAPGroupRead.md) | (Read-only) Array of mappings between LDAP Groups and Looker Roles | [optional] 
**groups_with_role_ids** | [**LDAPGroupWrite**](LDAPGroupWrite.md) | (Write-only) Array of mappings between LDAP Groups and arrays of Looker Role ids | [optional] 
**auth_requires_role** | **bool** | Users will not be allowed to login at all unless a role for them is found in LDAP if set to true | [optional] 
**groups_finder_type** | **str** | Identifier for a strategy for how Looker will search for groups in the LDAP server | [optional] 
**groups_base_dn** | **str** | Base dn for finding groups in LDAP searches | [optional] 
**groups_member_attribute** | **str** | LDAP Group attribute that signifies the members of the groups. Most commonly &#39;member&#39; | [optional] 
**groups_user_attribute** | **str** | LDAP Group attribute that signifies the user in a group. Most commonly &#39;dn&#39; | [optional] 
**groups_objectclasses** | **str** | Optional comma-separated list of supported LDAP objectclass for groups when doing groups searches | [optional] 
**force_no_page** | **bool** | Don&#39;t attempt to do LDAP search result paging (RFC 2696) even if the LDAP server claims to support it. | [optional] 
**url** | **str** | Link to get this item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



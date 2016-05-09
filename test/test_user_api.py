# coding: utf-8

"""
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """ UserApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.user_api.UserApi()

    def tearDown(self):
        pass

    def test_all_user_access_filters(self):
        """
        Test case for all_user_access_filters

        get all Access filters
        """
        pass

    def test_all_user_credentials_api3s(self):
        """
        Test case for all_user_credentials_api3s

        get all API 3 credentials
        """
        pass

    def test_all_user_credentials_embeds(self):
        """
        Test case for all_user_credentials_embeds

        get all Embedding credentials
        """
        pass

    def test_all_user_sessions(self):
        """
        Test case for all_user_sessions

        get all Web login sessions
        """
        pass

    def test_all_users(self):
        """
        Test case for all_users

        get all users
        """
        pass

    def test_create_user(self):
        """
        Test case for create_user

        create a user
        """
        pass

    def test_create_user_access_filter(self):
        """
        Test case for create_user_access_filter

        create Access filter
        """
        pass

    def test_create_user_credentials_api(self):
        """
        Test case for create_user_credentials_api

        create API credential
        """
        pass

    def test_create_user_credentials_api3(self):
        """
        Test case for create_user_credentials_api3

        create API 3 credential
        """
        pass

    def test_create_user_credentials_email(self):
        """
        Test case for create_user_credentials_email

        create email/password credential
        """
        pass

    def test_create_user_credentials_email_password_reset(self):
        """
        Test case for create_user_credentials_email_password_reset

        create a email/password credential password reset token
        """
        pass

    def test_create_user_credentials_totp(self):
        """
        Test case for create_user_credentials_totp

        create Two-factor credential
        """
        pass

    def test_delete_user(self):
        """
        Test case for delete_user

        delete a user
        """
        pass

    def test_delete_user_access_filter(self):
        """
        Test case for delete_user_access_filter

        delete Access filter
        """
        pass

    def test_delete_user_credentials_api(self):
        """
        Test case for delete_user_credentials_api

        delete API credential
        """
        pass

    def test_delete_user_credentials_api3(self):
        """
        Test case for delete_user_credentials_api3

        delete API 3 credential
        """
        pass

    def test_delete_user_credentials_email(self):
        """
        Test case for delete_user_credentials_email

        delete email/password credential
        """
        pass

    def test_delete_user_credentials_embed(self):
        """
        Test case for delete_user_credentials_embed

        delete Embedding credential
        """
        pass

    def test_delete_user_credentials_google(self):
        """
        Test case for delete_user_credentials_google

        delete Google auth credential
        """
        pass

    def test_delete_user_credentials_ldap(self):
        """
        Test case for delete_user_credentials_ldap

        delete LDAP credential
        """
        pass

    def test_delete_user_credentials_looker_openid(self):
        """
        Test case for delete_user_credentials_looker_openid

        delete Looker Openid credential
        """
        pass

    def test_delete_user_credentials_saml(self):
        """
        Test case for delete_user_credentials_saml

        delete Saml auth credential
        """
        pass

    def test_delete_user_credentials_totp(self):
        """
        Test case for delete_user_credentials_totp

        delete Two-factor credential
        """
        pass

    def test_delete_user_session(self):
        """
        Test case for delete_user_session

        delete Web login session
        """
        pass

    def test_me(self):
        """
        Test case for me

        Get current user
        """
        pass

    def test_search_users(self):
        """
        Test case for search_users

        search users
        """
        pass

    def test_search_users_names(self):
        """
        Test case for search_users_names

        search users names
        """
        pass

    def test_set_user_roles(self):
        """
        Test case for set_user_roles

        Set roles for a user
        """
        pass

    def test_update_user(self):
        """
        Test case for update_user

        update a user
        """
        pass

    def test_update_user_access_filter(self):
        """
        Test case for update_user_access_filter

        update Access filter
        """
        pass

    def test_update_user_credentials_email(self):
        """
        Test case for update_user_credentials_email

        update email/password credential
        """
        pass

    def test_user(self):
        """
        Test case for user

        Get a user
        """
        pass

    def test_user_access_filter(self):
        """
        Test case for user_access_filter

        get Access filter
        """
        pass

    def test_user_credentials_api(self):
        """
        Test case for user_credentials_api

        get API credential
        """
        pass

    def test_user_credentials_api3(self):
        """
        Test case for user_credentials_api3

        get API 3 credential
        """
        pass

    def test_user_credentials_email(self):
        """
        Test case for user_credentials_email

        get email/password credential
        """
        pass

    def test_user_credentials_embed(self):
        """
        Test case for user_credentials_embed

        get Embedding credential
        """
        pass

    def test_user_credentials_google(self):
        """
        Test case for user_credentials_google

        get Google auth credential
        """
        pass

    def test_user_credentials_ldap(self):
        """
        Test case for user_credentials_ldap

        get LDAP credential
        """
        pass

    def test_user_credentials_looker_openid(self):
        """
        Test case for user_credentials_looker_openid

        get Looker Openid credential
        """
        pass

    def test_user_credentials_saml(self):
        """
        Test case for user_credentials_saml

        get Saml auth credential
        """
        pass

    def test_user_credentials_totp(self):
        """
        Test case for user_credentials_totp

        get Two-factor credential
        """
        pass

    def test_user_roles(self):
        """
        Test case for user_roles

        Get roles for a user
        """
        pass

    def test_user_session(self):
        """
        Test case for user_session

        get Web login session
        """
        pass


if __name__ == '__main__':
    unittest.main()
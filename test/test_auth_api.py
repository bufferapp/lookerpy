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
from swagger_client.apis.auth_api import AuthApi


class TestAuthApi(unittest.TestCase):
    """ AuthApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.auth_api.AuthApi()

    def tearDown(self):
        pass

    def test_all_embed_secrets(self):
        """
        Test case for all_embed_secrets

        get all embed secrets
        """
        pass

    def test_check_embed_domain(self):
        """
        Test case for check_embed_domain

        check embed domain
        """
        pass

    def test_create_embed_secret(self):
        """
        Test case for create_embed_secret

        create embed secret
        """
        pass

    def test_create_saml_test_config(self):
        """
        Test case for create_saml_test_config

        create saml test configuration
        """
        pass

    def test_delete_embed_secret(self):
        """
        Test case for delete_embed_secret

        delete embed secret
        """
        pass

    def test_delete_saml_test_config(self):
        """
        Test case for delete_saml_test_config

        delete saml test configuration
        """
        pass

    def test_embed_config(self):
        """
        Test case for embed_config

        get embed config
        """
        pass

    def test_embed_secret(self):
        """
        Test case for embed_secret

        get embed secret
        """
        pass

    def test_fetch_and_parse_saml_idp_metadata(self):
        """
        Test case for fetch_and_parse_saml_idp_metadata

        fetch and parse saml idp metadata xml
        """
        pass

    def test_ldap_config(self):
        """
        Test case for ldap_config

        get ldap configuration
        """
        pass

    def test_parse_saml_idp_metadata(self):
        """
        Test case for parse_saml_idp_metadata

        parse saml idp metadata xml
        """
        pass

    def test_saml_config(self):
        """
        Test case for saml_config

        get saml configuration
        """
        pass

    def test_saml_test_config(self):
        """
        Test case for saml_test_config

        get saml test configuration
        """
        pass

    def test_test_ldap_config_auth(self):
        """
        Test case for test_ldap_config_auth

        test ldap auth config
        """
        pass

    def test_test_ldap_config_connection(self):
        """
        Test case for test_ldap_config_connection

        test ldap connection config
        """
        pass

    def test_test_ldap_config_user_auth(self):
        """
        Test case for test_ldap_config_user_auth

        test ldap user auth config
        """
        pass

    def test_test_ldap_config_user_info(self):
        """
        Test case for test_ldap_config_user_info

        test ldap user info config
        """
        pass

    def test_update_embed_config(self):
        """
        Test case for update_embed_config

        update embed config
        """
        pass

    def test_update_embed_secret(self):
        """
        Test case for update_embed_secret

        update embed secret
        """
        pass

    def test_update_ldap_config(self):
        """
        Test case for update_ldap_config

        update ldap configuration
        """
        pass

    def test_update_saml_config(self):
        """
        Test case for update_saml_config

        update saml configuration
        """
        pass


if __name__ == '__main__':
    unittest.main()
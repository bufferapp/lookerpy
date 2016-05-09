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
from swagger_client.apis.role_api import RoleApi


class TestRoleApi(unittest.TestCase):
    """ RoleApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.role_api.RoleApi()

    def tearDown(self):
        pass

    def test_all_model_sets(self):
        """
        Test case for all_model_sets

        get all model sets
        """
        pass

    def test_all_permission_sets(self):
        """
        Test case for all_permission_sets

        get all permission sets
        """
        pass

    def test_all_permissions(self):
        """
        Test case for all_permissions

        get all permissions
        """
        pass

    def test_all_roles(self):
        """
        Test case for all_roles

        get all roles
        """
        pass

    def test_create_model_set(self):
        """
        Test case for create_model_set

        create a model set
        """
        pass

    def test_create_permission_set(self):
        """
        Test case for create_permission_set

        create a permission set
        """
        pass

    def test_create_role(self):
        """
        Test case for create_role

        create a role
        """
        pass

    def test_delete_model_set(self):
        """
        Test case for delete_model_set

        delete a model set
        """
        pass

    def test_delete_permission_set(self):
        """
        Test case for delete_permission_set

        delete a permission set
        """
        pass

    def test_delete_role(self):
        """
        Test case for delete_role

        delete a role
        """
        pass

    def test_model_set(self):
        """
        Test case for model_set

        Get a model set
        """
        pass

    def test_permission_set(self):
        """
        Test case for permission_set

        Get a permission set
        """
        pass

    def test_role(self):
        """
        Test case for role

        Get a role
        """
        pass

    def test_role_users(self):
        """
        Test case for role_users

        Get users with role
        """
        pass

    def test_set_role_users(self):
        """
        Test case for set_role_users

        Set users with role
        """
        pass

    def test_update_model_set(self):
        """
        Test case for update_model_set

        update a model set
        """
        pass

    def test_update_permission_set(self):
        """
        Test case for update_permission_set

        update a permission set
        """
        pass

    def test_update_role(self):
        """
        Test case for update_role

        update a role
        """
        pass


if __name__ == '__main__':
    unittest.main()
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
from swagger_client.apis.space_api import SpaceApi


class TestSpaceApi(unittest.TestCase):
    """ SpaceApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.space_api.SpaceApi()

    def tearDown(self):
        pass

    def test_all_spaces(self):
        """
        Test case for all_spaces

        get all spaces
        """
        pass

    def test_create_space(self):
        """
        Test case for create_space

        create space
        """
        pass

    def test_delete_space(self):
        """
        Test case for delete_space

        delete space
        """
        pass

    def test_space(self):
        """
        Test case for space

        get space
        """
        pass

    def test_space_ancestors(self):
        """
        Test case for space_ancestors

        get ancestors of space
        """
        pass

    def test_space_children(self):
        """
        Test case for space_children

        get children of space
        """
        pass

    def test_space_children_search(self):
        """
        Test case for space_children_search

        search children of space
        """
        pass

    def test_space_parent(self):
        """
        Test case for space_parent

        get parent of space
        """
        pass

    def test_update_space(self):
        """
        Test case for update_space

        update space
        """
        pass


if __name__ == '__main__':
    unittest.main()
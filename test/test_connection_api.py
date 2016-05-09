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
from swagger_client.apis.connection_api import ConnectionApi


class TestConnectionApi(unittest.TestCase):
    """ ConnectionApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.connection_api.ConnectionApi()

    def tearDown(self):
        pass

    def test_all_connections(self):
        """
        Test case for all_connections

        get all connections
        """
        pass

    def test_all_dialect_infos(self):
        """
        Test case for all_dialect_infos

        get all dialect infos
        """
        pass

    def test_connection(self):
        """
        Test case for connection

        get connection
        """
        pass

    def test_create_connection(self):
        """
        Test case for create_connection

        create connection
        """
        pass

    def test_delete_connection(self):
        """
        Test case for delete_connection

        delete connection
        """
        pass

    def test_test_connection(self):
        """
        Test case for test_connection

        test existing connection
        """
        pass

    def test_test_connection_config(self):
        """
        Test case for test_connection_config

        test connection configuration
        """
        pass

    def test_update_connection(self):
        """
        Test case for update_connection

        update connection
        """
        pass


if __name__ == '__main__':
    unittest.main()
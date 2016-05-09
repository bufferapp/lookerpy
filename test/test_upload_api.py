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
from swagger_client.apis.upload_api import UploadApi


class TestUploadApi(unittest.TestCase):
    """ UploadApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.upload_api.UploadApi()

    def tearDown(self):
        pass

    def test_all_uploads(self):
        """
        Test case for all_uploads

        get all uploads
        """
        pass

    def test_create_upload(self):
        """
        Test case for create_upload

        Upload a csv file and return the inferred table definition
        """
        pass

    def test_delete_upload(self):
        """
        Test case for delete_upload

        Delete UploadTable and drop upload created table if exists
        """
        pass

    def test_get_upload(self):
        """
        Test case for get_upload

        Get table definition for an upload
        """
        pass

    def test_get_upload_lookml(self):
        """
        Test case for get_upload_lookml

        Get the generated lookml for a table created via upload
        """
        pass

    def test_load_upload(self):
        """
        Test case for load_upload

        Upload contents of a file to create and load a table in the DB
        """
        pass

    def test_update_upload(self):
        """
        Test case for update_upload

        Update upload table definition and create/load the DB table
        """
        pass


if __name__ == '__main__':
    unittest.main()
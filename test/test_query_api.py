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
from swagger_client.apis.query_api import QueryApi


class TestQueryApi(unittest.TestCase):
    """ QueryApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.query_api.QueryApi()

    def tearDown(self):
        pass

    def test_create_query(self):
        """
        Test case for create_query

        create query
        """
        pass

    def test_create_query_and_run_async(self):
        """
        Test case for create_query_and_run_async

        Create a Query and run it asynchronously.
        """
        pass

    def test_query(self):
        """
        Test case for query

        get query
        """
        pass

    def test_query_for_slug(self):
        """
        Test case for query_for_slug

        get query for slug
        """
        pass

    def test_query_task(self):
        """
        Test case for query_task

        Get a Query Task
        """
        pass

    def test_query_task_multi_results(self):
        """
        Test case for query_task_multi_results

        Get multiple query task results in one request.
        """
        pass

    def test_query_task_results(self):
        """
        Test case for query_task_results

        Get a Query Task's results
        """
        pass

    def test_run_async(self):
        """
        Test case for run_async

        Run a Query asynchronously.
        """
        pass

    def test_run_inline_query(self):
        """
        Test case for run_inline_query

        run inline query
        """
        pass

    def test_run_query(self):
        """
        Test case for run_query

        run query
        """
        pass

    def test_run_url_encoded_query(self):
        """
        Test case for run_url_encoded_query

        run url encoded query
        """
        pass


if __name__ == '__main__':
    unittest.main()
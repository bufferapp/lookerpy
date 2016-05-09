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
from swagger_client.apis.dashboard_api import DashboardApi


class TestDashboardApi(unittest.TestCase):
    """ DashboardApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.dashboard_api.DashboardApi()

    def tearDown(self):
        pass

    def test_all_dashboards(self):
        """
        Test case for all_dashboards

        get all dashboards
        """
        pass

    def test_copy_dashboards(self):
        """
        Test case for copy_dashboards

        copy dashboards to space
        """
        pass

    def test_create_dashboard(self):
        """
        Test case for create_dashboard

        create dashboard
        """
        pass

    def test_create_dashboard_prefetch(self):
        """
        Test case for create_dashboard_prefetch

        create a prefetch
        """
        pass

    def test_dashboard(self):
        """
        Test case for dashboard

        get dashboard
        """
        pass

    def test_dashboard_prefetch(self):
        """
        Test case for dashboard_prefetch

        get a prefetch
        """
        pass

    def test_dashboards_move_plan(self):
        """
        Test case for dashboards_move_plan

        plan for moving dashboards to space
        """
        pass

    def test_delete_dashboard(self):
        """
        Test case for delete_dashboard

        delete dashboard
        """
        pass

    def test_move_dashboards(self):
        """
        Test case for move_dashboards

        move dashboards to space
        """
        pass

    def test_update_dashboard(self):
        """
        Test case for update_dashboard

        update dashboard
        """
        pass


if __name__ == '__main__':
    unittest.main()
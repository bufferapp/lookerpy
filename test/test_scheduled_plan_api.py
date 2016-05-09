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
from swagger_client.apis.scheduled_plan_api import ScheduledPlanApi


class TestScheduledPlanApi(unittest.TestCase):
    """ ScheduledPlanApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.scheduled_plan_api.ScheduledPlanApi()

    def tearDown(self):
        pass

    def test_all_scheduled_plans(self):
        """
        Test case for all_scheduled_plans

        get all scheduled plans
        """
        pass

    def test_create_scheduled_plan(self):
        """
        Test case for create_scheduled_plan

        create scheduled plan
        """
        pass

    def test_create_scheduled_plan_destination(self):
        """
        Test case for create_scheduled_plan_destination

        create scheduled plan destination
        """
        pass

    def test_delete_scheduled_plan(self):
        """
        Test case for delete_scheduled_plan

        delete scheduled plan
        """
        pass

    def test_delete_scheduled_plan_destination(self):
        """
        Test case for delete_scheduled_plan_destination

        delete scheduled plan destination
        """
        pass

    def test_scheduled_plan(self):
        """
        Test case for scheduled_plan

        get scheduled plan
        """
        pass

    def test_scheduled_plan_destination(self):
        """
        Test case for scheduled_plan_destination

        get scheduled plan destination
        """
        pass

    def test_scheduled_plans_by_dashboard(self):
        """
        Test case for scheduled_plans_by_dashboard

        get all scheduled plans for a given dashboard for the requesting user
        """
        pass

    def test_scheduled_plans_by_look(self):
        """
        Test case for scheduled_plans_by_look

        get all scheduled plans for a given look for the requesting user
        """
        pass

    def test_scheduled_plans_by_lookml_dashboard(self):
        """
        Test case for scheduled_plans_by_lookml_dashboard

        get all scheduled plans for a given lookml dashboard for the requesting user
        """
        pass

    def test_scheduled_plans_by_space(self):
        """
        Test case for scheduled_plans_by_space

        get all scheduled plans for a given space for the requesting user
        """
        pass

    def test_update_scheduled_plan(self):
        """
        Test case for update_scheduled_plan

        update scheduled plan
        """
        pass

    def test_update_scheduled_plan_destination(self):
        """
        Test case for update_scheduled_plan_destination

        update scheduled plan destination
        """
        pass


if __name__ == '__main__':
    unittest.main()
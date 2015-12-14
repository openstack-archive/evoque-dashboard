# Copyright 2015 Huawei Technologies Co., Ltd.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from openstack_dashboard.test import helpers

from evoqueclient import client as evoque_client

from evoque_dashboard import api
from evoque_dashboard.test.test_data import utils


def create_stubs(stubs_to_create={}):
    return helpers.create_stubs(stubs_to_create)


class EvoqueTestsMixin(object):
    def _setup_test_data(self):
        super(EvoqueTestsMixin, self)._setup_test_data()
        utils.load_test_data(self)


class TestCase(EvoqueTestsMixin, helpers.TestCase):
    pass


class APITestCase(EvoqueTestsMixin, helpers.APITestCase):
    def setUp(self):
        super(APITestCase, self).setUp()

        # Store the original evoque client
        self._original_evoqueclient = api.evoque.evoqueclient

        # Replace the clients with our stubs.
        api.evoque.evoqueclient = lambda request: self.stub_evoqueclient()

    def tearDown(self):
        super(APITestCase, self).tearDown()
        api.evoque.evoqueclient = self._original_evoqueclient

    def stub_evoqueclient(self):
        if not hasattr(self, "evoqueclient"):
            self.mox.StubOutWithMock(evoque_client, 'Client')
            self.evoqueclient = self.mox.CreateMock(evoque_client.Client)
        return self.evoqueclient

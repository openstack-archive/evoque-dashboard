# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import mock

from openstack_dashboard.test.test_data import utils as test_data_utils


def data(TEST):

    # Workflows
    TEST.workflows = test_data_utils.TestDataContainer()
    workflow_1 = mock.Mock()
    workflow_1.name = "test-workflow"

    TEST.workflows.add(workflow_1)

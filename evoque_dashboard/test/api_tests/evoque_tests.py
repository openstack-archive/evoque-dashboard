# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from evoque_dashboard import api
from evoque_dashboard.test import helpers as test


class EvoqueApiTests(test.APITestCase):

    def test_workflow_list(self):
        workflows = self.workflows.list()
        evoqueclient = self.stub_evoqueclient()
        evoqueclient.list = self.mox.CreateMockAnything()
        evoqueclient.list().AndReturn(workflows)
        self.mox.ReplayAll()

        api.evoque.workflow_list(self.request)

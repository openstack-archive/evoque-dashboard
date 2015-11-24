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

from evoqueclient.common import exceptions as evoque_exceptions

from openstack_dashboard.test.test_data.exceptions \
    import create_stubbed_exception
from openstack_dashboard.test.test_data import utils


def data(TEST):
    TEST.exceptions = utils.TestDataContainer()

    evoque_exception = evoque_exceptions.HTTPException
    TEST.exceptions.evoque = create_stubbed_exception(evoque_exception)

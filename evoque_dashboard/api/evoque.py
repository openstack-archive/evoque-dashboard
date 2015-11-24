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

from django.conf import settings

from horizon.utils import memoized

from openstack_dashboard.api import base

from evoqueclient import client as evoque_client

USER_AGENT = 'python-senlinclient'


class Workflow(base.APIResourceWrapper):
    _attrs = ['id', 'name', 'created_at', 'updated_at']


def _get_endpoint(request):
    endpoint = getattr(
        settings, 'EVOQUE_API_URL', "http://127.0.0.1:8808")

    return endpoint


@memoized.memoized
def evoqueclient(request):
    endpoint = _get_endpoint(request)

    return evoque_client.Client(1, endpoint=endpoint,
                                token=request.user.token.id,
                                tenant=request.user.tenant_id)


def workflow_list(request):
    """Returns all workflows."""
    workflows = evoqueclient(request).workflows.list()
    return [Workflow(c) for c in workflows]

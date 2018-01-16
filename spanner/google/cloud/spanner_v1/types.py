# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import sys

from google.api_core.protobuf_helpers import get_messages

from google.api import http_pb2
from google.cloud.spanner_v1.proto import keys_pb2
from google.cloud.spanner_v1.proto import mutation_pb2
from google.cloud.spanner_v1.proto import query_plan_pb2
from google.cloud.spanner_v1.proto import result_set_pb2
from google.cloud.spanner_v1.proto import spanner_pb2
from google.cloud.spanner_v1.proto import transaction_pb2
from google.cloud.spanner_v1.proto import type_pb2
from google.protobuf import descriptor_pb2
from google.protobuf import duration_pb2
from google.protobuf import empty_pb2
from google.protobuf import struct_pb2
from google.protobuf import timestamp_pb2

names = []
for module in (
        http_pb2,
        keys_pb2,
        mutation_pb2,
        query_plan_pb2,
        result_set_pb2,
        spanner_pb2,
        transaction_pb2,
        type_pb2,
        descriptor_pb2,
        duration_pb2,
        empty_pb2,
        struct_pb2,
        timestamp_pb2,
):
    for name, message in get_messages(module).items():
        message.__module__ = 'google.cloud.spanner_v1.types'
        setattr(sys.modules[__name__], name, message)
        names.append(name)

__all__ = tuple(sorted(names))

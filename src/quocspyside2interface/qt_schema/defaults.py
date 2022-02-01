# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright 2021-  QuOCS Team
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def enum_defaults(schema):
    try:
        return schema["enum"][0]
    except IndexError:
        return None


def object_defaults(schema):
    return {k: compute_defaults(s) for k, s in schema["properties"].items()}


def array_defaults(schema):
    items_schema = schema['items']
    if isinstance(items_schema, dict):
        return []

    return [compute_defaults(s) for s in schema["items"]]


def compute_defaults(schema):
    if "default" in schema:
        return schema["default"]

    # Enum
    if "enum" in schema:
        return enum_defaults(schema)

    schema_type = schema["type"]

    if schema_type == "object":
        return object_defaults(schema)

    elif schema_type == "array":
        return array_defaults(schema)

    return None

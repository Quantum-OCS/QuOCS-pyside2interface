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

import sys
from json import dumps

from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.widgetbuilder import WidgetBuilder

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Create the builder for the widget
    # I should provide a validator for the schema
    builder = WidgetBuilder()

    schema = {
        "type": "object",
        "title": "Number fields and widgets",
        "properties": {
            "schema_path": {
                "title": "Schema path",
                "type": "string"
            },
            "integerRangeSteps": {
                "title": "Integer range (by 10)",
                "type": "integer",
                "minimum": 55,
                "maximum": 100,
                "multipleOf": 10
            },
            "sky_colour": {
                "type": "string"
            },
            "names": {
                "type": "array",
                "items": [
                    {
                        "type": "string",
                        "pattern": "[a-zA-Z\-'\s]+",
                        "enum": [
                            "Jack", "Jill"
                        ]
                    },
                    {
                        "type": "string",
                        "pattern": "[a-zA-Z\-'\s]+",
                        "enum": [
                            "Alice", "Bob"
                        ]
                    },
                ],
                "additionalItems": {
                    "type": "number"
                },
            }
        }
    }

    ui_schema = {
        "schema_path": {
            "ui:widget": "filepath"
        },
        "sky_colour": {
            "ui:widget": "colour"
        }

    }
    form = builder.create_form(schema, ui_schema)
    # Initial values for the widgets inside the form
    form.widget.state = {
        "schema_path": "some_file.py",
        "integerRangeSteps": 60,
        "sky_colour": "#8f5902",
        "names": [
            "Jack",
            "Bob"
        ]
    }
    form.show()
    # When a widget inside the form changes, send a signal and print the current json dictionary
    form.widget.on_changed.connect(lambda d: print(dumps(d, indent=4)))

    app.exec_()

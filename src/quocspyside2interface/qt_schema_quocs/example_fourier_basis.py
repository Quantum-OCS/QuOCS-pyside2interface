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

    builder = WidgetBuilder()

    schema = {
        "type": "object",
        "title": "Fourier Basis test",
        "properties": {
            "floatAmplitude": {
                "title": "Amplitude",
                "type": "number",
                "minimum": 0.0,
                "maximum": 10.0
            }
        }
    }

    ui_schema = {
        "floatAmplitude": {
            "ui:widget": "scientific"
        }
    }
    form = builder.create_form(schema, ui_schema)
    form.widget.state = {
        "floatAmplitude": 5.0
    }
    form.show()
    form.widget.on_changed.connect(lambda d: print(dumps(d, indent=4)))

    app.exec_()
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

from json import dumps

from qtpy import QtWidgets

from quocspyside2interface.logic.utilities.readjson import readjson
from quocspyside2interface.qt_schema_quocs.widgetbuilder import WidgetBuilder


def main():
    app = QtWidgets.QApplication()

    # Create the builder
    builder = WidgetBuilder()

    # Read the schema, ui_schema, and initial state
    schema = readjson("fourier_basis.json")[1]
    ui_schema = readjson("ui_schema_fourier_basis.json")[1]
    state_schema = readjson("state_fourier_basis.json")[1]

    # Create the form with builder object
    form = builder.create_form(schema, ui_schema)

    # Initialize the form values
    form.widget.state = state_schema

    form.show()

    # Print data form when it changes
    form.widget.on_changed.connect(lambda d: print(dumps(d, indent=4)))

    app.exec_()


if __name__ == "__main__":
    main()

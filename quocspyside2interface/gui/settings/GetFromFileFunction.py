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

from qtpy import QtWidgets
import os

from quocspyside2interface.gui.uiclasses.GetFromFileFunctionUI import Ui_Form


class GetFromFileFunction(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pulses_data = None
        # TODO Enable list index spinbox only when the json file is available

    def get_from_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open Pulse file",
                                                         os.getcwd(), "json (*.json)", options=
                                                         QtWidgets.QFileDialog.DontUseNativeDialog)
        from quocspyside2interface.logic.utilities.readjson import readjson
        err_code, self.pulses_data = readjson(filename[0])
        if err_code != 0:
            print("")

    def check_pulse(self):
        # Get the list from file and plot it out to verify how it looks
        pass

    def get_dictionary(self):
        pass

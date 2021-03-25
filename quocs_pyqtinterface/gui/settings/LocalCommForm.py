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

from quocs_pyqtinterface.gui.uiclasses.LocalCommunicationUI import Ui_Form


class LocalCommForm(QtWidgets.QWidget, Ui_Form):
    """Widget for the Local communication"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.get_shared_folder_button.clicked.connect(self.get_shared_folder)
        self.get_results_folder_button.clicked.connect(self.get_results_folder)

    def get_results_folder(self):
        # TODO get the results folder
        pass

    def get_shared_folder(self):
        # TODO get the shared folder
        pass

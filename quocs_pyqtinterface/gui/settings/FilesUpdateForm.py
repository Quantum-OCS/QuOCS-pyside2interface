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

from quocs_pyqtinterface.gui.uiclasses.FilesUpdateUI import Ui_Form


class FilesUpdateForm(QtWidgets.QWidget, Ui_Form):
    """Widget for the Files Update Communication"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Button connection
        self.get_update_folder_button.clicked.connect(self.get_update_folder)

    def get_update_folder(self):
        # TODO get the results folder
        pass

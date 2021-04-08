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

import os
from qtpy import QtWidgets

from quocs_pyside2interface.logic.utilities.readjson import readjson
from quocs_pyside2interface.logic.ComunicationSettingsDictionaries.RemoteCommunicationDictionary \
    import RemoteCommunicationDictionary
from quocs_pyside2interface.gui.uiclasses.RemoteConnectionUI import Ui_Form


class RemoteCommForm(QtWidgets.QWidget, Ui_Form):
    """ Widget for the Remote Communication """
    credential_data = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Dictionary
        self.remote_communication_dictionary = RemoteCommunicationDictionary()
        # Connection
        self.get_credential_file_button.clicked.connect(self.get_credential_filename)
        self.check_connection_button.clicked.connect(self.check_connection)
        self.get_shared_folder_button.clicked.connect(self.get_shared_folder)
        self.get_results_folder_button.clicked.connect(self.get_results_folder)
        # Initialization
        self._initialization()

    def _initialization(self):

        pass

    def get_results_folder(self):
        # TODO get the results folder
        pass

    def get_shared_folder(self):
        # TODO get the shared folder
        pass

    def get_credential_filename(self):
        """Get the credential data from a json file"""
        filename = QtWidgets.QFileDialog.getOpenFileName(self,
                    "Open credential file", os.getcwd(), "json (*.json)", options=QtWidgets.QFileDialog.DontUseNativeDialog)
        err_stat, credential_data = readjson(filename[0])
        self.credential_data = credential_data
        self.credential_file_edit_line.setText(filename[0])

    def check_connection(self):
        """Check the connection before starting the optimization"""
        # TODO Check connection by using the remote connection class (_init and end)
        pass

    def get_dictionary(self):
        return self.remote_communication_dictionary.get_dictionary()

    def get_summary_list(self):
        return self.remote_communication_dictionary.get_summary_list()
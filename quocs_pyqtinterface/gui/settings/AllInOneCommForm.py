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

from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.AllInOneCommunicationDictionary import \
    AllInOneCommunicationDictionary
from qtpy import QtWidgets
from quocs_pyqtinterface.gui.uiclasses.AllInOneCommunicationUI import Ui_Form


class AllInOneCommForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None, loaded_dictionary=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()
        # dictionary
        self.all_in_one_communication_dictionary = AllInOneCommunicationDictionary(loaded_dictionary=loaded_dictionary)
        # Connections
        self.get_results_folder_button.clicked.connect(self.get_results_folder)
        self.results_folder_edit_line.textChanged.connect(self.results_folder_changed)
        # initialization
        self._initialization()

    def _initialization(self):
        self.results_folder_edit_line.setText(self.all_in_one_communication_dictionary.results_folder)

    def results_folder_changed(self, results_folder_path):
        if os.path.isdir(results_folder_path):
            self.all_in_one_communication_dictionary.results_folder = results_folder_path
        else:
            self.all_in_one_communication_dictionary.results_folder = os.path.join(os.getcwd(), "QuOCS_Results")

    def get_results_folder(self):
        # Get the results folder form a file
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Get results directory", os.getcwd(),
                                                            options=QtWidgets.QFileDialog.DontUseNativeDialog)
        self.results_folder_edit_line.setText(folder)

    def get_dictionary(self):
        return self.all_in_one_communication_dictionary.get_dictionary()

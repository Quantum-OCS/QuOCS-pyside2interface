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

from quocs_pyqtinterface.gui.settings.CommunicationFoMSettings import CommFom


class GeneralOptimizationDialog(QtWidgets.QDialog):
    general_optimization_tab: QtWidgets.QWidget
    optimization_dictionary_obj = None

    def __init__(self, load_full_dictionary_signal=None, plugin_name: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_full_dictionary_signal = load_full_dictionary_signal
        self.general_optimization_tab.currentChanged.connect(self.set_curr_tab_index)
        self.curr_tab_index = -1
        self.plugin_name = plugin_name

    def set_communication_fom(self, comm_fom_settings: [dict, dict]):
        # Communication and Figure of merit calculation
        self.general_optimization_tab.addTab(CommFom(loaded_dictionary=comm_fom_settings, plugin_name=self.plugin_name),
                                             "Communication and FoM Settings")

    def set_optimization_client_name(self, optimization_name):
        self.optimization_dictionary_obj.optimization_client_name = optimization_name

    def set_curr_tab_index(self, index):
        # Update the previous widget
        self._update_dictionary_tab()
        # Set the new tab index
        self.curr_tab_index = index

    def _update_dictionary_tab(self):
        opti_widget = self.general_optimization_tab.widget(self.curr_tab_index)
        # Update the dictionary of the previous settings tab
        if opti_widget is not None:
            self.optimization_dictionary_obj.update_dictionary(opti_widget.get_dictionary())

    def _loop_over_all_tabs(self):
        # Loop over all the tabs to update the dictionary
        for i in range(self.general_optimization_tab.count()):
            self.general_optimization_tab.setCurrentIndex(i)
        # Change to the first one to make sure all tabs are updated
        self.general_optimization_tab.setCurrentIndex(0)

    def save_opti_dictionary(self):
        """Save the opti dictionary in a file"""
        self._loop_over_all_tabs()
        #
        total_dictionary = self.optimization_dictionary_obj.get_dictionary()
        # TODO Add checks
        # Save the dictionary into a json file
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save config file",
                                                         os.getcwd(), "json (*.json)", options=
                                                         QtWidgets.QFileDialog.DontUseNativeDialog)
        from quocs_pyqtinterface.logic.utilities.writejsonfile import writejsonfile
        writejsonfile(filename[0], total_dictionary)

    def load_opti_dictionary(self):
        """Send a signal to the main window with the total dictionary and close the dialog"""
        self._loop_over_all_tabs()
        # TODO Check for errors before starting the loading
        self.load_full_dictionary_signal.emit(self.optimization_dictionary_obj.get_dictionary())
        self.close()

    def closeEvent(self, event):
        # TODO something to prevent unwanted closing
        print("I am closing the Optimization Dialog")

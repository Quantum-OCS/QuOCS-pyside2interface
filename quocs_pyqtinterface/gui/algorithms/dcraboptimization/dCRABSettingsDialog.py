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

from qtpy import QtCore
from qtpy import QtWidgets
import os

from quocs_pyqtinterface.gui.algorithms.dcraboptimization.ControlSettings import ControlsSettings
from quocs_pyqtinterface.gui.algorithms.dcraboptimization.dCRABSettings import dCRABSettings
from quocs_pyqtinterface.gui.freegradients.GeneralSettingsNM import GeneralSettingsNM
from quocs_pyqtinterface.gui.settings.CommunicationFoMSettings import CommFom
from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.dCRABGlobalDictionary import dCRABGlobalDictionary
from quocs_pyqtinterface.gui.uiclasses.dCRABOptimizationDialogUI import Ui_Dialog


class dCRABSettingsDialog(QtWidgets.QDialog, Ui_Dialog):
    """Dialogue for dCRAB"""

    dropout_summary = None
    close_dropout_summary_signal = QtCore.Signal()
    comm_fom_dictionary_signal = QtCore.Signal(dict, list)
    comm_fom_dictionary = None
    comm_fom_list = None
    total_dictionary = None

    def __init__(self, parent=None, load_full_dictionary_signal=None, loaded_dictionary=None):
        super().__init__(parent)
        self.setupUi(self)
        ######################################################
        # Dictionary Settings
        ######################################################
        [opti_dictionary, dcrab_settings, general_settings_nm, controls_settings, comm_fom_settings] = \
            [None for _ in range(5)]
        if loaded_dictionary is not None:
            opti_dictionary = loaded_dictionary["optimization_dictionary"]
            dcrab_settings = opti_dictionary["algorithm_settings"]
            general_settings_nm = opti_dictionary["dsm_settings"]
            controls_settings = [opti_dictionary["pulses"], opti_dictionary["parameters"], opti_dictionary["times"]]
            comm_fom_settings = [loaded_dictionary["communication"], loaded_dictionary["figure_of_merit"]]
        self.dcrab_global_dictionary = dCRABGlobalDictionary(loaded_dictionary=opti_dictionary)
        ######################################################
        # Tabs Initialization
        ######################################################

        self.curr_tab_index = -1
        # dCRAB Settings
        dcrab_settings_index = self.general_dcrab_tab.addTab(dCRABSettings(loaded_dictionary=dcrab_settings), "dCRAB Settings")
        # self.dcrab_settings = self.general_dcrab_tab.widget(dcrab_settings_index)
        # Direct Search Method Settings
        general_settings_index = self.general_dcrab_tab.addTab(GeneralSettingsNM(loaded_dictionary=general_settings_nm), "Direct Search Method Settings")
        # self.general_settings_widget = self.general_dcrab_tab.widget(general_settings_index)
        # stopping_criteria_index = self.general_dcrab_tab.addTab(StoppingCriteriaNM(), "Stopping Criteria")
        # self.stopping_criteria_widget = self.general_dcrab_tab.widget(stopping_criteria_index)
        # # Controls
        controls_settings_index = self.general_dcrab_tab.addTab(ControlsSettings(loaded_dictionary=controls_settings), "Controls Settings")
        # self.controls_settings_widget = self.general_dcrab_tab.widget(controls_settings_index)
        # Figure of merit calculation
        comm_fom_settings_index = self.general_dcrab_tab.addTab(CommFom(loaded_dictionary=comm_fom_settings), "Communication and FoM Settings")
        # self.comm_fom_widget = self.general_dcrab_tab.widget(comm_fom_settings_index)

        # Signal when the window is closed
        self.load_full_dictionary_signal = load_full_dictionary_signal
        # Connection
        self.optimization_name_edit_line.textChanged. connect(self.set_optimization_client_name)
        self.general_dcrab_tab.currentChanged.connect(self.set_curr_tab_index)
        self.save_button.clicked.connect(self.save_opti_dictionary)
        self.load_button.clicked.connect(self.load_opti_dictionary)
        # Initialization
        self._initialization()

    def _initialization(self):
        self.general_dcrab_tab.setCurrentIndex(0)
        self.curr_tab_index = 0
        self.optimization_name_edit_line.setText(self.dcrab_global_dictionary.optimization_client_name)

    def set_optimization_client_name(self, optimization_name):
        self.dcrab_global_dictionary.optimization_client_name = optimization_name

    def set_curr_tab_index(self, index):
        # Update the previous widget
        self._update_dictionary_tab()
        # Set the new tab index
        self.curr_tab_index = index

    def _update_dictionary_tab(self):
        dcrab_widget = self.general_dcrab_tab.widget(self.curr_tab_index)
        # Update the dictionary of the previous settings tab
        if dcrab_widget is not None:
            self.dcrab_global_dictionary.update_dictionary(dcrab_widget.get_dictionary())

    def _loop_over_all_tabs(self):
        # Loop over all the tabs to update the dictionary
        for i in range(self.general_dcrab_tab.count()):
            self.general_dcrab_tab.setCurrentIndex(i)
        # Change to the first one to make sure all tabs are updated
        self.general_dcrab_tab.setCurrentIndex(0)

    def save_opti_dictionary(self):
        """Save the opti dictionary in a file"""
        self._loop_over_all_tabs()
        #
        total_dictionary = self.dcrab_global_dictionary.get_dictionary()
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
        # TODO Check for errors before start the loading
        self.load_full_dictionary_signal.emit(self.dcrab_global_dictionary.get_dictionary())
        self.close()

    def closeEvent(self, event):
        # TODO If save button is active ask before quitting otherwise just quick
        print("I am closing the dCRAB Dialog")

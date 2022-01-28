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
from qtpy import uic
import os

from quocspyside2interface.gui.optimalalgorithms.GeneralOptimizationDialog import GeneralOptimizationDialog
from quocspyside2interface.gui.PureControlsSettings import PureControlsSettings
from quocspyside2interface.gui.freegradientsmethods.GeneralSettingsNM import GeneralSettingsNM
from quocspyside2interface.gui.figureofmeritevaluation.CommunicationFoMSettings import CommFom

from quocspyside2interface.logic.optimalalgorithms.PureParametrizationGlobalDictionary \
    import PureParametrizationGlobalDictionary


PureParametersDialog = \
    uic.loadUiType(os.path.join(os.path.dirname(__file__), "PureParametersOptimizationSettings.ui"))[0]


class DirectSearchSettingsDialog(GeneralOptimizationDialog, PureParametersDialog):
    """Dialogue for dCRAB"""

    total_dictionary = None

    def __init__(self, parent=None, load_full_dictionary_signal=None, loaded_dictionary=None, is_test: bool = False):
        super().__init__(parent=parent)
        self.setupUi(self)
        if is_test:
            return
        ######################################################
        # Dictionary Settings
        ######################################################
        self.pure_global_dictionary = PureParametrizationGlobalDictionary()
        ######################################################
        # Tabs Initialization
        ######################################################
        [dcrab_settings, general_settings_nm, controls_settings, comm_fom_settings] = [None, None, None, None]
        if loaded_dictionary is not None:
            opti_dictionary = loaded_dictionary["optimization_dictionary"]
            dcrab_settings = opti_dictionary["algorithm_settings"]
            general_settings_nm = opti_dictionary["dsm_settings"]
            controls_settings = [opti_dictionary["pulses"], opti_dictionary["parameters"], opti_dictionary["times"]]
            comm_fom_settings = [loaded_dictionary["communication"], loaded_dictionary["figure_of_merit"]]

        self.curr_tab_index = -1
        # Direct Search Method Settings
        general_settings_index = self.general_pure_tab.addTab(
            GeneralSettingsNM(loaded_dictionary=general_settings_nm), "Direct Search Method Settings")
        # Controls
        controls_settings_index = self.general_pure_tab.addTab(
            PureControlsSettings(loaded_dictionary=controls_settings), "Controls Settings")
        # Communication and Figure of merit calculation
        comm_fom_settings_index = self.general_pure_tab.addTab(
            CommFom(loaded_dictionary=comm_fom_settings), "Communication and FoM Settings")

        # Signal when the window is closed
        self.load_full_dictionary_signal = load_full_dictionary_signal
        # Connection
        self.optimization_name_edit_line.textChanged.connect(self.set_optimization_client_name)
        self.general_pure_tab.currentChanged.connect(self.set_curr_tab_index)
        self.save_button.clicked.connect(self.save_opti_dictionary)
        self.load_button.clicked.connect(self.load_opti_dictionary)
        # Initialization
        self._initialization()

    def _initialization(self):
        self.general_pure_tab.setCurrentIndex(0)
        self.curr_tab_index = 0
        self.optimization_name_edit_line.setText(self.pure_global_dictionary.optimization_client_name)

    def set_optimization_client_name(self, optimization_name):
        self.pure_global_dictionary.optimization_client_name = optimization_name

    def set_curr_tab_index(self, index):
        # Update the previous widget
        self._update_dictionary_tab()
        # Set the new tab index
        self.curr_tab_index = index

    def _update_dictionary_tab(self):
        pure_widget = self.general_pure_tab.widget(self.curr_tab_index)
        # Update the dictionary of the previous settings tab
        if pure_widget is not None:
            self.pure_global_dictionary.update_dictionary(pure_widget.get_dictionary())

    def _loop_over_all_tabs(self):
        # Loop over all the tabs to update the dictionary
        for i in range(self.general_pure_tab.count()):
            self.general_pure_tab.setCurrentIndex(i)
        # Change to the first one to make sure all tabs are updated
        self.general_pure_tab.setCurrentIndex(0)

    def save_opti_dictionary(self):
        """Save the opti dictionary in a file"""
        self._loop_over_all_tabs()
        #
        total_dictionary = self.pure_global_dictionary.get_dictionary()
        # TODO Add checks before saving
        # Save the dictionary into a json file
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save config file",
                                                         os.getcwd(), "json (*.json)", options=
                                                         QtWidgets.QFileDialog.DontUseNativeDialog)
        from quocspyside2interface.logic.utilities.writejsonfile import writejsonfile
        writejsonfile(filename[0], total_dictionary)

    def load_opti_dictionary(self):
        """Send a signal to the main window with the total dictionary and close the dialog"""
        self._loop_over_all_tabs()
        # TODO Check for errors before start the loading
        self.load_full_dictionary_signal.emit(self.pure_global_dictionary.get_dictionary())
        self.close()

    def closeEvent(self, event):
        # TODO If save button is active ask before quitting otherwise just quick
        print("I am closing the Pure Parameters Dialog")

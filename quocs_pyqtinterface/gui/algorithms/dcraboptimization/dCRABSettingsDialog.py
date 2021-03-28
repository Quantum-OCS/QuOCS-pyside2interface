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

from quocs_pyqtinterface.gui.algorithms.GeneralOptimizationDialog import GeneralOptimizationDialog
from quocs_pyqtinterface.gui.algorithms.dcraboptimization.ControlSettings import ControlsSettings
from quocs_pyqtinterface.gui.algorithms.dcraboptimization.dCRABSettings import dCRABSettings
from quocs_pyqtinterface.gui.freegradients.GeneralSettingsNM import GeneralSettingsNM
from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.dCRABGlobalDictionary import dCRABGlobalDictionary
from quocs_pyqtinterface.gui.uiclasses.dCRABOptimizationDialogUI import Ui_Dialog


class dCRABSettingsDialog(GeneralOptimizationDialog, Ui_Dialog):
    """Dialogue for dCRAB"""

    def __init__(self, parent=None, load_full_dictionary_signal=None, loaded_dictionary=None):
        super().__init__(parent=parent, load_full_dictionary_signal=load_full_dictionary_signal)
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
        self.optimization_dictionary_obj = dCRABGlobalDictionary(loaded_dictionary=opti_dictionary)
        ######################################################
        # Tabs Initialization
        ######################################################
        # Get the reference to the general optimization tab
        self.general_optimization_tab = self.general_optimization_tab
        # dCRAB Settings
        self.general_optimization_tab.addTab(dCRABSettings(loaded_dictionary=dcrab_settings), "dCRAB Settings")
        # Direct Search Method Settings
        self.general_optimization_tab.addTab(GeneralSettingsNM(loaded_dictionary=general_settings_nm), "Direct Search Method Settings")
        # Controls
        self.general_optimization_tab.addTab(ControlsSettings(loaded_dictionary=controls_settings), "Controls Settings")
        # Communication and FoM evaluation
        self.set_communication_fom(comm_fom_settings)
        # Connection
        self.save_button.clicked.connect(self.save_opti_dictionary)
        self.load_button.clicked.connect(self.load_opti_dictionary)
        # Initialization
        self.optimization_name_edit_line.textChanged.connect(self.set_optimization_client_name)
        self._initialization()

    def _initialization(self):
        self.general_optimization_tab.setCurrentIndex(0)
        self.curr_tab_index = 0
        self.optimization_name_edit_line.setText(self.optimization_dictionary_obj.optimization_client_name)


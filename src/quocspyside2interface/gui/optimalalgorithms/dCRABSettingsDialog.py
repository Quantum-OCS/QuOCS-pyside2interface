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

from qtpy import uic
import os

from quocspyside2interface.gui.optimalalgorithms.GeneralOptimizationDialog import GeneralOptimizationDialog
from quocspyside2interface.gui.ControlSettings import ControlsSettings
from quocspyside2interface.gui.optimalalgorithms.dCRABSettings import dCRABSettings
from quocspyside2interface.gui.freegradientsmethods.GeneralSettingsNM import GeneralSettingsNM

from quocspyside2interface.logic.optimalalgorithms.dCRABGlobalDictionary import dCRABGlobalDictionary


dCRABOptimizationDialog = uic.loadUiType(os.path.join(os.path.dirname(__file__), "dCRABOptimizationDialog.ui"))[0]


class dCRABSettingsDialog(GeneralOptimizationDialog, dCRABOptimizationDialog):
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
        # Get the reference for the general optimization tab
        self.general_optimization_tab = self.general_dcrab_tab
        # dCRAB Settings
        self.general_optimization_tab.addTab(dCRABSettings(loaded_dictionary=dcrab_settings), "dCRAB Settings")
        # Direct Search Method Settings
        self.general_optimization_tab.addTab(GeneralSettingsNM(loaded_dictionary=general_settings_nm), "Direct Search Method Settings")
        # Controls
        self.general_optimization_tab.addTab(ControlsSettings(loaded_dictionary=controls_settings), "Controls Settings")
        # Communication and FoM evaluation
        self.set_communication_fom(comm_fom_settings)
        # Connection
        self.general_optimization_tab.currentChanged.connect(self.set_curr_tab_index)
        self.save_button.clicked.connect(self.save_opti_dictionary)
        self.load_button.clicked.connect(self.load_opti_dictionary)
        # Initialization
        self.optimization_name_edit_line.textChanged.connect(self.set_optimization_client_name)
        self._initialization()

    def _initialization(self):
        """ Initialize the settings for this dialog """
        self.general_optimization_tab.setCurrentIndex(0)
        self.curr_tab_index = 0
        self.optimization_name_edit_line.setText(self.optimization_dictionary_obj.optimization_client_name)


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
from quocs_pyqtinterface.gui.uiclasses.GeneralSettingsNMUI import Ui_Form
from quocs_pyqtinterface.gui.freegradients.StoppingCriteriaNM import StoppingCriteriaNM
from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.NelderMeadDictionary import NelderMeadDictionary


class GeneralSettingsNM(QtWidgets.QWidget, Ui_Form):
    def __init__(self, loaded_dictionary=None):
        super().__init__()
        self.setupUi(self)

        nm_dictionary, stopping_criteria_dictionary = None, None
        if loaded_dictionary is not None:
            nm_dictionary = loaded_dictionary["general_settings"]
            stopping_criteria_dictionary = loaded_dictionary["stopping_criteria"]
        # Nelder Mead Dictionary
        self.nelder_mead_dictionary = NelderMeadDictionary(loaded_dictionary=nm_dictionary)
        # Create widget
        self.stopping_criteria_form = StoppingCriteriaNM(loaded_dictionary=stopping_criteria_dictionary)
        # Connection
        self.is_adaptive_checkbox.stateChanged.connect(self.set_is_adaptive)

        self._initialization()

    def _initialization(self):
        self.is_adaptive_checkbox.setChecked(self.nelder_mead_dictionary.is_adaptive)
        self.stopping_criteria_scroll_area.setWidget(self.stopping_criteria_form)

    def set_is_adaptive(self):
        self.nelder_mead_dictionary.is_adaptive = self.is_adaptive_checkbox.isChecked()

    def get_dictionary(self):
        return {"dsm_settings": {"general_settings": self.nelder_mead_dictionary.get_dictionary(),
                                 "stopping_criteria": self.stopping_criteria_form.get_dictionary()}}
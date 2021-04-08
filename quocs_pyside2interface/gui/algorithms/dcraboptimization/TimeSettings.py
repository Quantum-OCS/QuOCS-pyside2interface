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
from qtpy import QtGui

from quocs_pyside2interface.logic.OptimalAlgorithmDictionaries.TimeDictionary import TimeDictionary
from quocs_pyside2interface.gui.uiclasses.TimeDefinitionUI import Ui_Form


class TimeSettings(QtWidgets.QWidget, Ui_Form):
    def __init__(self, control_index, update_name_time_signal, update_time_combo_box_pulse, loaded_dictionary=None):
        super().__init__()
        self.setupUi(self)
        # Initialization variables
        self.control_index = control_index
        self.control_type = "time"
        self.update_name_time_signal = update_name_time_signal
        self.update_time_combo_box_pulse = update_time_combo_box_pulse
        # Time dictionary
        self.time_dictionary = TimeDictionary(loaded_dictionary=loaded_dictionary)
        # Set validators
        self.time_guess_validator = QtGui.QDoubleValidator()
        self.time_guess_line_edit.setValidator(self.time_guess_validator)
        # Connection
        self.time_name_line_edit.textChanged.connect(self.set_time_name)
        self.time_guess_line_edit.textChanged.connect(self.set_time_guess)
        # Initialization
        self.is_initialization = True
        self._initialize_settings()
        self.is_initialization = False

    def _initialize_settings(self):
        self.time_name_line_edit.setText(self.time_dictionary.time_name)
        self.time_guess_line_edit.setText(str(self.time_dictionary.initial_value))

    def set_time_name(self, time_name):
        self.time_dictionary.time_name = time_name
        if not self.is_initialization:
            self.update_name_time_signal.emit(time_name)
            self.update_time_combo_box_pulse.emit()

    def set_time_guess(self, time_guess):
        self.time_dictionary.initial_value = float(time_guess)
        if not self.is_initialization:
            self.update_time_combo_box_pulse.emit()

    def get_dictionary(self):
        return self.time_dictionary.get_dictionary()

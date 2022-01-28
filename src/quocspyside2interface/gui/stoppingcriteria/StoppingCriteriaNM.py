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
from qtpy import uic
import os

from quocspyside2interface.logic.stoppingcriteria.StoppingCriteriaNelderMeadDictionary import \
    StoppingCriteriaNelderMeadDictionary


StoppingCriteriaNMWidget = uic.loadUiType(os.path.join(os.path.dirname(__file__), "StoppingCriteriaNM.ui"))[0]


class StoppingCriteriaNM(QtWidgets.QWidget, StoppingCriteriaNMWidget):
    def __init__(self, loaded_dictionary=None, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # Stopping criteria dictionary
        self.stopping_criteria_dictionary = StoppingCriteriaNelderMeadDictionary(loaded_dictionary=loaded_dictionary)

        # Set validators
        self.precision_validator = QtGui.QDoubleValidator()
        self.xatol_edit_line.setValidator(self.precision_validator)
        self.frtol_edit_line.setValidator(self.precision_validator)

        # Connection
        self.iterations_number_spinbox.valueChanged.connect(self.set_iterations_number)
        self.xatol_edit_line.textChanged.connect(self.set_xatol)
        self.frtol_edit_line.textChanged.connect(self.set_frtol)

        # Initialization
        self._initialization()

    def set_iterations_number(self, iterations_number):
        self.stopping_criteria_dictionary.iterations_number = iterations_number

    def set_xatol(self, xatol):
        self.stopping_criteria_dictionary.xatol = float(xatol)

    def set_frtol(self, frtol):
        self.stopping_criteria_dictionary.frtol = float(frtol)

    def _initialization(self):
        self.iterations_number_spinbox.setValue(self.stopping_criteria_dictionary.iterations_number)
        self.xatol_edit_line.setText(str(self.stopping_criteria_dictionary.xatol))
        self.frtol_edit_line.setText(str(self.stopping_criteria_dictionary.frtol))

    def get_dictionary(self):
        return self.stopping_criteria_dictionary.get_dictionary()

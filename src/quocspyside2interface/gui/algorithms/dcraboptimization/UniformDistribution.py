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

from quocspyside2interface.logic.OptimalAlgorithmDictionaries.UniformDistributionDictionary \
    import UniformDistributionDictionary
from quocspyside2interface.gui.uiclasses.UniformDistributionUI import Ui_Form


class UniformDistribution(QtWidgets.QWidget, Ui_Form):
    def __init__(self, loaded_dictionary: dict = None):
        super().__init__()
        self.setupUi(self)

        # Dictionary fro the uniform distribution
        self.distribution_dictionary = UniformDistributionDictionary(loaded_dictionary=loaded_dictionary)

        # Set the validators for all the edit_line in the gui
        self.lower_limit_validator = QtGui.QDoubleValidator()
        self.lower_limit_line_edit.setValidator(self.lower_limit_validator)
        self.upper_limit_validator = QtGui.QDoubleValidator()
        self.upper_limit_line_edit.setValidator(self.upper_limit_validator)

        # Connections
        self.lower_limit_line_edit.textChanged.connect(self.set_lower_limit)
        self.upper_limit_line_edit.textChanged.connect(self.set_upper_limit)

        # Initialization
        self._initialize_settings()

    def set_lower_limit(self, lower_limit: float):
        self.distribution_dictionary.lower_limit = float(lower_limit)

    def set_upper_limit(self, upper_limit: float):
        self.distribution_dictionary.upper_limit = float(upper_limit)

    def _initialize_settings(self):
        self.lower_limit_line_edit.setText(str(self.distribution_dictionary.lower_limit))
        self.upper_limit_line_edit.setText(str(self.distribution_dictionary.upper_limit))

    def get_dictionary(self):
        return self.distribution_dictionary.get_dictionary()

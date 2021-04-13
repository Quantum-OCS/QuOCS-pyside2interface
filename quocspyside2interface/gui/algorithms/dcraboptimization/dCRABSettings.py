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

from quocspyside2interface.logic.OptimalAlgorithmDictionaries.dCRABSettingsDictionary import dCRABSettingsDictionary
from quocspyside2interface.gui.uiclasses.dCRABSettingsUI import Ui_Form


class dCRABSettings(QtWidgets.QWidget, Ui_Form):
    def __init__(self, loaded_dictionary=None):
        super().__init__()
        self.setupUi(self)
        # Dictionary
        self.dcrab_dictionary = dCRABSettingsDictionary(loaded_dictionary=loaded_dictionary)
        # Connections
        self.superiteration_number_spinbox.valueChanged.connect(self.set_super_iteration_number)
        self.iterations_number_spinbox.valueChanged.connect(self.set_iterations_number)
        # Initialization
        self._initialization()

    def _initialization(self):
        # Default values
        self.superiteration_number_spinbox.setValue(self.dcrab_dictionary.super_iteration_number)
        self.iterations_number_spinbox.setValue(self.dcrab_dictionary.maximum_function_evaluations_number)

    def set_super_iteration_number(self):
        # TODO Add check here
        self.dcrab_dictionary.super_iteration_number = self.superiteration_number_spinbox.value()

    def set_iterations_number(self):
        # TODO Add check here
        self.dcrab_dictionary.maximum_function_evaluations_number = self.iterations_number_spinbox.value()

    def get_dictionary(self):
        return {"algorithm_settings": self.dcrab_dictionary.get_dictionary()}

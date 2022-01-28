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

from quocspyside2interface.logic.figureofmeritevaluation.NewPythonArgumentDictionary import NewPythonArgumentDictionary


NewPythonArgumentWidget = uic.loadUiType(os.path.join(os.path.dirname(__file__), "NewPythonArgument.ui"))[0]


class NewPythonArgument(QtWidgets.QWidget, NewPythonArgumentWidget):
    """Create the new python argument for the python script"""
    def __init__(self, argument_index, parent=None, argument=None):
        super().__init__(parent)
        self.setupUi(self)
        # Argument index
        self.argument_index_name = str(argument_index)
        # List of possible type used as python argument
        self.type_list = ["string", "int", "float", "bool"]
        # Dictionary
        self.new_python_argument_dictionary = NewPythonArgumentDictionary(loaded_dictionary=argument)
        # Connection
        self.argument_name_edit_line.textChanged.connect(self.set_argument_name)
        self.argument_type_combobox.currentIndexChanged.connect(self.set_argument_type)
        self.argument_value_edit_line.textChanged.connect(self.set_argument_value)
        # Initialization
        self._initialization()

    def set_argument_name(self, argument_name):
        self.new_python_argument_dictionary.name = argument_name

    def set_argument_value(self, argument_value):
        self.new_python_argument_dictionary.value = argument_value

    def set_argument_type(self, index):
        self.new_python_argument_dictionary.type = self.type_list[index]

    def _initialization(self):
        # Combobox initialization
        for type_name in self.type_list:
            self.argument_type_combobox.addItem(type_name)
        #
        self.argument_name_edit_line.setText(self.new_python_argument_dictionary.name)
        self.argument_type_combobox.itemText(self.type_list.index(self.new_python_argument_dictionary.type))
        self.argument_value_edit_line.setText(self.new_python_argument_dictionary.value)

    def get_dictionary(self):
        return self.new_python_argument_dictionary.get_dictionary()

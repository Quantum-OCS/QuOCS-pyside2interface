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

from quocspyside2interface.logic.OptimalAlgorithmDictionaries.NewPythonArgumentDictionary import NewPythonArgumentDictionary
from quocspyside2interface.gui.uiclasses.NewPythonArgumentUI import Ui_Form


class NewPythonArgument(QtWidgets.QWidget, Ui_Form):
    """Create the new python argument for the python script"""
    def __init__(self, argument_index, parent=None, argument=None):
        # Get the path to the *.ui file
        # ui_file = os.path.join(os.getcwd(), GuiConstants.GUI_PATH, "NewPythonArgument.ui")
        # Load it
        super().__init__(parent)
        # uic.loadUi(ui_file, self)
        self.setupUi(self)

        # Argument index
        self.argument_index_name = str(argument_index)

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
        self.new_python_argument_dictionary.type = self.argument_type_combobox.itemText(index)

    def _initialization(self):
        # Combobox initialization
        type_list = ["string", "int", "float", "bool"]
        for type_name in type_list:
            self.argument_type_combobox.addItem(type_name)

        self.argument_name_edit_line.setText(self.new_python_argument_dictionary.name)
        self.argument_type_combobox.itemText(type_list.index(self.new_python_argument_dictionary.type))
        self.argument_value_edit_line.setText(self.new_python_argument_dictionary.value)

    def get_dictionary(self):
        return self.new_python_argument_dictionary.get_dictionary()

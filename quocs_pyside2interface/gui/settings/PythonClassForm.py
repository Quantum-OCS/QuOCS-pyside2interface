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

from quocs_pyside2interface.gui.settings.NewPythonArgument import NewPythonArgument
from quocs_pyside2interface.logic.OptimalAlgorithmDictionaries.PythonClassFoMDictionary import PythonClassFomDictionary
from quocs_pyside2interface.gui.uiclasses.PythonEvaluationUI import Ui_Form


class PythonClassForm(QtWidgets.QWidget, Ui_Form):
    """Widget for the Python Class communication"""

    def __init__(self, parent=None, loaded_dictionary=None):
        super().__init__(parent)
        self.setupUi(self)

        # Dictionary
        self.python_class_dictionary = PythonClassFomDictionary(loaded_dictionary=loaded_dictionary)

        self.curr_tab_index = -1

        # Signals
        self.add_argument_button.clicked.connect(self.add_empty_argument_widget)
        self.delete_argument_button.clicked.connect(self.remove_argument_widget)
        #  Connection
        self.check_import_button.clicked.connect(self.check_correct_import)
        self.arguments_tab.currentChanged.connect(self.set_curr_tab_index)
        self.module_edit_line.textChanged.connect(self.set_module)
        self.class_edit_line.textChanged.connect(self.set_class)

        self._initialization()

    def check_correct_import(self):
        # TODO Check if the library is imported correctly
        pass

    def _initialization(self):
        self.module_edit_line.setText(self.python_class_dictionary.python_module)
        self.class_edit_line.setText(self.python_class_dictionary.python_class)
        further_args = self.python_class_dictionary.further_args
        for argument in further_args:
            self.add_argument_widget(arg_dict=further_args[argument])

    def add_argument_widget(self, arg_dict=None):
        argument_index = self.python_class_dictionary.argument_index
        argument_widget = NewPythonArgument(argument_index, parent=self, argument=arg_dict)
        self.arguments_tab.addTab(argument_widget, arg_dict["name"])

    def set_module(self, python_module):
        self.python_class_dictionary.python_module = python_module

    def set_class(self, python_class_name):
        self.python_class_dictionary.python_class = python_class_name

    def set_curr_tab_index(self, index):
        self._update_dictionary_tab()
        self.curr_tab_index = index

    def remove_argument_widget(self):
        # Delete the argument in the dictionary class
        argument_widget = self.arguments_tab.widget(self.curr_tab_index)
        argument_index_name = argument_widget.argument_index_name
        self.python_class_dictionary.remove_argument(argument_index_name)
        # Remove the tab
        self.arguments_tab.removeTab(self.curr_tab_index)

    def add_empty_argument_widget(self):
        argument_index = self.python_class_dictionary.argument_index
        argument_widget = NewPythonArgument(argument_index, parent=self)
        # TODO Add signal to change the name of the tab
        self.arguments_tab.addTab(argument_widget, argument_widget.new_python_argument_dictionary.name)
        self.python_class_dictionary.add_argument(argument_widget.argument_index_name, argument_widget.get_dictionary())

    def _update_dictionary_tab(self):
        # Loop over all the tab to update the arguments
        argument_widget = self.arguments_tab.widget(self.curr_tab_index)
        if argument_widget is not None:
            argument_index_name = argument_widget.argument_index_name
            argument_dict = argument_widget.new_python_argument_dictionary.get_dictionary()
            self.python_class_dictionary.update_argument(argument_index_name, argument_dict)

    def get_dictionary(self):
        self._update_dictionary_tab()
        return self.python_class_dictionary.get_dictionary()

    def get_summary_list(self):
        return self.python_class_dictionary.get_summary_list()

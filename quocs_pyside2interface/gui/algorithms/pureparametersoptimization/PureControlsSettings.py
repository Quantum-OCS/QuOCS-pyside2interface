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

from qtpy import QtCore
from qtpy import QtWidgets
from qtpy import QtGui

from quocs_pyside2interface.logic.OptimalAlgorithmDictionaries.ControlDictionary import ControlsDictionary
from quocs_pyside2interface.logic.OptimalAlgorithmDictionaries.ParameterDictionary import ParameterDictionary
from quocs_pyside2interface.gui.uiclasses.PureParametersOptimizationControlsUI import Ui_Form


class PureControlsSettings(QtWidgets.QWidget, Ui_Form):

    def __init__(self, loaded_dictionary: dict = None):
        super().__init__()
        self.setupUi(self)

        # Variables
        self.curr_tab_index = 0
        self.control_dictionary = ControlsDictionary

        # List of parameter object
        self.parameters_obj_list: [ParameterDictionary] = []

        # Set the validators for all the edit_line in the gui
        self.lower_limit_validator = QtGui.QDoubleValidator()
        self.lower_limit_edit_line.setValidator(self.lower_limit_validator)
        self.upper_limit_validator = QtGui.QDoubleValidator()
        self.upper_limit_edit_line.setValidator(self.upper_limit_validator)
        self.initial_value_validator = QtGui.QDoubleValidator()
        self.initial_value_edit_line.setValidator(self.initial_value_validator)
        self.variation_validator = QtGui.QDoubleValidator()
        self.variation_edit_line.setValidator(self.variation_validator)
        # TODO Dynamically change the range of the Gui Validator to avoid wrong values

        # Connection
        self.update_parameters_number_button.clicked.connect(self.update_parameters_number)
        self.remove_parameter_button.clicked.connect(self.remove_parameter)

        # Select parameter
        self.parameter_number_selected_spinbox.valueChanged.connect(self.selected_parameter_number_changed)
        # Parameter name
        self.parameter_name_edit_line.textEdited.connect(self.parameter_name_changed)
        # Initial Value
        self.initial_value_edit_line.textEdited.connect(self.initial_value_changed)
        # Lower Limit
        self.lower_limit_edit_line.textEdited.connect(self.lower_limit_changed)
        # Upper Limit
        self.upper_limit_edit_line.textEdited.connect(self.upper_limit_changed)
        # Variation
        self.variation_edit_line.textEdited.connect(self.variation_changed)
        # apply to all parameters
        self.apply_all_parameters_button.clicked.connect(self.apply_all_parameters_clicked)

        # Initialization
        self._initialization(loaded_dictionary=loaded_dictionary)

    def _initialization(self, loaded_dictionary: dict = None):
        # [pulses, parameters, times]
        if loaded_dictionary is not None:
            parameters_list = loaded_dictionary[1]
            for parameter_dictionary in parameters_list:
                self.create_parameter_obj(parameter_dictionary=parameter_dictionary)
        else:
            self.create_parameter_obj(index="1")
        # Update the total parameters number in the spinbox
        self.parameters_number_spinbox.setValue(len(self.parameters_obj_list))
        # Show the parameter number one
        self.parameter_number_selected_spinbox.setValue(1)
        self.selected_parameter_number_changed(1)
        self.parameter_number_selected_spinbox.setMaximum(len(self.parameters_obj_list))

    def create_parameter_obj(self, parameter_dictionary: dict = None, index: str = ""):
        self.parameters_obj_list.append(ParameterDictionary(parameter_dictionary, index=index))

    def variation_changed(self, amplitude_variation: str):
        index = self.parameter_number_selected_spinbox.value()
        self.parameters_obj_list[index - 1].amplitude_variation = float(amplitude_variation)

    def upper_limit_changed(self, upper_limit: str):
        index = self.parameter_number_selected_spinbox.value()
        self.parameters_obj_list[index - 1].upper_limit = float(upper_limit)

    def lower_limit_changed(self, lower_limit: str):
        index = self.parameter_number_selected_spinbox.value()
        self.parameters_obj_list[index - 1].lower_limit = float(lower_limit)

    def initial_value_changed(self, initial_value: str):
        index = self.parameter_number_selected_spinbox.value()
        self.parameters_obj_list[index - 1].initial_value = float(initial_value)

    def parameter_name_changed(self, parameter_name: str):
        index = self.parameter_number_selected_spinbox.value()
        self.parameters_obj_list[index - 1].parameter_name = parameter_name

    def selected_parameter_number_changed(self, parameter_number_selected: int):
        # Get the selected parameter settings and show it in the window
        self._parameters_settings(self.parameters_obj_list[parameter_number_selected - 1])

    def apply_all_parameters_clicked(self):
        # Get the dictionary of the current parameter
        index = self.parameter_number_selected_spinbox.value()
        # Copy the dictionary content
        parameter_dictionary = self.parameters_obj_list[index - 1].get_dictionary().copy()
        # Exclude the parameter name
        parameter_dictionary.pop("parameter_name")
        # Copy only the element in the dictionary
        for parameter in self.parameters_obj_list:
            for element in parameter_dictionary:
                parameter.__dict__[element] = parameter_dictionary[element]

    def remove_parameter(self):
        # Check: not remove when only 1 parameter exists
        if len(self.parameters_obj_list) == 1:
            print("You cannot remove the last parameter :(")
            return
        parameter_position = self.parameter_number_selected_spinbox.value()
        del self.parameters_obj_list[parameter_position - 1]
        # Update the data in the window
        parameters_number = len(self.parameters_obj_list)
        index = parameter_position
        # TODO Understand why this happens
        if parameter_position > parameters_number:
            index = parameter_position - 1
        # Update the value in the main window
        self._parameters_settings(self.parameters_obj_list[index - 1])
        # Update total number of parameters
        self.parameters_number_spinbox.setValue(parameters_number)
        # Update current selected parameter
        self.parameter_number_selected_spinbox.setValue(index)
        # Update Maximum number
        self.parameter_number_selected_spinbox.setMaximum(parameters_number)

    def _parameters_settings(self, parameter_dictionary_obj: ParameterDictionary):
        self.parameter_name_edit_line.setText(parameter_dictionary_obj.parameter_name)
        self.initial_value_edit_line.setText(str(parameter_dictionary_obj.initial_value))
        self.upper_limit_edit_line.setText(str(parameter_dictionary_obj.upper_limit))
        self.lower_limit_edit_line.setText(str(parameter_dictionary_obj.lower_limit))
        self.variation_edit_line.setText(str(parameter_dictionary_obj.amplitude_variation))

    def update_parameters_number(self):
        parameters_number = self.parameters_number_spinbox.value()
        old_parameters_number = len(self.parameters_obj_list)
        if parameters_number < old_parameters_number:
            # Remove last parameters
            for i in range(parameters_number, old_parameters_number):
                del self.parameters_obj_list[-1]
        else:
            for i in range(old_parameters_number, parameters_number):
                self.create_parameter_obj(index=str(i + 1))
        self.parameter_number_selected_spinbox.setMaximum(parameters_number)

    def get_dictionary(self) -> [list, list, list]:
        """ Return the dictionary with the controls"""
        parameters_list = []
        for parameter in self.parameters_obj_list:
            parameters_list.append(parameter.get_dictionary())
        return {"pulses": [], "parameters": parameters_list, "times": []}

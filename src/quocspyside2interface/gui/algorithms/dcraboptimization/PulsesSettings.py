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

from qtpy import QtWidgets, QtGui

from quocspyside2interface.gui.algorithms.dcraboptimization.FourierBasis import FourierBasis
from quocspyside2interface.gui.algorithms.dcraboptimization.SigmoidBasis import SigmoidBasis
from quocspyside2interface.gui.algorithms.dcraboptimization.ChebyshevBasis import ChebyshevBasis
from quocspyside2interface.gui.settings.GetFromFileFunction import GetFromFileFunction
from quocspyside2interface.gui.algorithms.dcraboptimization.LambdaFunction import LambdaFunction
from quocspyside2interface.gui.algorithms.dcraboptimization.ListFunction import ListFunction
from quocspyside2interface.logic.OptimalAlgorithmDictionaries.PulseDictionary import PulseDictionary
from quocspyside2interface.gui.uiclasses.PulseDefinitionUI import Ui_Form


class PulseSettings(QtWidgets.QWidget, Ui_Form):

    def __init__(self, control_index, update_name_signal, loaded_dictionary=None):
        super().__init__()
        self.setupUi(self)

        self.control_index = control_index
        self.control_type = "pulse"
        self.update_name_signal = update_name_signal

        self.pulse_dictionary = PulseDictionary(loaded_dictionary=loaded_dictionary)

        # Initial guess QButtonGroup
        self.initial_guess_button_group = QtWidgets.QButtonGroup()
        self.initial_guess_button_group.addButton(self.lambda_initial_guess_radio_button)
        self.initial_guess_button_group.addButton(self.list_initial_guess_radio_button)
        self.initial_guess_button_group.addButton(self.from_file_initial_guess_radio_button)

        # Scaling function QButtonGroup
        self.scaling_function_button_group = QtWidgets.QButtonGroup()
        self.scaling_function_button_group.addButton(self.lambda_scaling_function_radio_button)
        self.scaling_function_button_group.addButton(self.list_scaling_function_radio_button)
        self.scaling_function_button_group.addButton(self.from_file_scaling_function_radio_button)

        # Default initial and scaling functions
        self.lambda_initial_guess_radio_button.setChecked(True)
        self.lambda_scaling_function_radio_button.setChecked(True)

        # Create the widget objects
        # Basis form objects
        # TODO Take the list of available bases from a module or class
        self.basis_name = self.pulse_dictionary.basis.setdefault("basis_name", "Fourier")
        self.basis_list = ["Fourier", "Sigmoid", "Chebyshev"]
        basis_dict = self.pulse_dictionary.basis
        self.fourier_basis_form = FourierBasis(
            loaded_dictionary=self._load_dictionary(self.basis_name, "Fourier", basis_dict))
        self.sigmoid_basis_form = SigmoidBasis(
            loaded_dictionary=self._load_dictionary(self.basis_name, "Sigmoid", basis_dict))
        self.chebyshev_basis_form = ChebyshevBasis(
            loaded_dictionary=self._load_dictionary(self.basis_name, "Chebyshev", basis_dict))
        self.basis_obj = [self.fourier_basis_form, self.sigmoid_basis_form, self.chebyshev_basis_form]
        self.basis_funs = [self.set_fourier_basis_widget, self.set_sigmoid_basis_widget, self.set_chebyshev_basis_widget]
        # Initial Guess
        # TODO Think how to load the dictionary based fro different initial guess
        self.initial_guess_lambda_function_form = LambdaFunction(loaded_dictionary=self.pulse_dictionary.initial_guess)
        self.initial_guess_list_function_form = ListFunction()
        self.initial_guess_get_from_file_form = GetFromFileFunction()
        # Scaling Function
        # TODO Think how to load the dictionary based fro different initial guess
        self.scaling_function_lambda_function_form = \
            LambdaFunction(loaded_dictionary=self.pulse_dictionary.scaling_function)
        self.scaling_function_list_function_form = ListFunction()
        self.scaling_function_get_from_file_form = GetFromFileFunction()

        # Adjustments
        self.bins_number_spinbox.setMaximum(10001)
        self.time_line_edit.setReadOnly(True)

        # Set validator
        self.upper_limit_line_edit.setValidator(QtGui.QDoubleValidator())
        self.upper_limit_line_edit.setValidator(QtGui.QDoubleValidator())
        self.amplitude_variation_line_edit.setValidator(QtGui.QDoubleValidator())

        # Connections
        self.lambda_initial_guess_radio_button.pressed.connect(self.set_initial_guess_lambda_function_widget)
        self.list_initial_guess_radio_button.pressed.connect(self.set_initial_guess_list_function_widget)
        self.from_file_initial_guess_radio_button.pressed.connect(self.set_initial_guess_get_from_file_function_widget)

        self.lambda_scaling_function_radio_button.pressed.connect(self.set_scaling_function_lambda_function_widget)
        self.list_scaling_function_radio_button.pressed.connect(self.set_scaling_function_list_function_widget)
        self.from_file_scaling_function_radio_button.pressed.connect(
            self.set_scaling_function_get_from_file_function_widget)

        self.pulse_name_line_edit.textChanged.connect(self.set_pulse_name)
        self.upper_limit_line_edit.textChanged.connect(self.set_upper_limit)
        self.lower_limit_line_edit.textChanged.connect(self.set_lower_limit)
        self.amplitude_variation_line_edit.textChanged.connect(self.set_amplitude_variation)
        self.bins_number_spinbox.valueChanged.connect(self.set_bins_number)

        self.basis_combobox.currentIndexChanged.connect(self.set_basis)

        self.time_name_combobox.currentIndexChanged.connect(self.set_time_combobox)

        self.is_initialization = True
        # Initialization
        self._initialize_settings()
        self.is_initialization = False

        self.times_value_list = []

    def _load_dictionary(self, arg1: str, arg2: str, dictionary: dict) -> dict:
        if arg1 == arg2:
            return dictionary
        else:
            return {}

    def _initialize_settings(self):
        # Set initial widgets
        # Set basis accordingly to the basis name
        self.basis_scroll_area.setWidget(self.basis_obj[self.basis_list.index(self.basis_name)])
        self.initial_guess_scroll_area.setWidget(self.initial_guess_lambda_function_form)
        self.scaling_function_scroll_area.setWidget(self.scaling_function_lambda_function_form)
        self.initial_guess_scroll_area.setWidgetResizable(True)
        self.basis_scroll_area.setWidgetResizable(True)
        # Pulse Name
        self.pulse_name_line_edit.setText(self.pulse_dictionary.pulse_name)
        # Amplitude Limits
        self.upper_limit_line_edit.setText(str(self.pulse_dictionary.upper_limit))
        self.lower_limit_line_edit.setText(str(self.pulse_dictionary.lower_limit))
        # Amplitude variation
        self.amplitude_variation_line_edit.setText(str(self.pulse_dictionary.amplitude_variation))
        # Time Settings
        self.bins_number_spinbox.setValue(self.pulse_dictionary.bins_number)
        # Basis
        for basis in self.basis_list:
            self.basis_combobox.addItem(basis)
        self.basis_combobox.setCurrentIndex(self.basis_list.index(self.basis_name))

    def update_time_values(self, time_dict):
        # Clear the time
        self.times_value_list = []
        # Clear the combobox
        self.time_name_combobox.clear()
        # In case the time_dict is empty, leave the time edit blank
        if len(time_dict) == 0:
            self.time_line_edit.setText("")
        # Otherwise fill the combobox
        else:
            for element in time_dict:
                self.times_value_list.append(time_dict[element])
                self.time_name_combobox.addItem(element)

    def set_time_combobox(self, index):
        if index != -1:
            self.time_line_edit.setText(str(self.times_value_list[index]))
            self.pulse_dictionary.time_name = self.time_name_combobox.itemText(index)

    def get_dictionary(self):
        pulse_dict = self.pulse_dictionary.get_dictionary()
        basis_dict = self.basis_scroll_area.widget().get_dictionary()
        scaling_function_dict = self.scaling_function_scroll_area.widget().get_dictionary()
        initial_guess_dict = self.initial_guess_scroll_area.widget().get_dictionary()
        full_dict = {**pulse_dict, "basis": basis_dict, "scaling_function": scaling_function_dict,
                     "initial_guess": initial_guess_dict}
        return full_dict

    def set_basis(self, basis_index:int):
        self.basis_funs[basis_index]()

    def set_amplitude_variation(self, amplitude_variation):
        self.pulse_dictionary.amplitude_variation = float(amplitude_variation)

    def set_upper_limit(self, upper_limit):
        self.pulse_dictionary.upper_limit = float(upper_limit)

    def set_lower_limit(self, lower_limit):
        self.pulse_dictionary.lower_limit = float(lower_limit)

    def set_bins_number(self, bins_number):
        self.pulse_dictionary.bins_number = bins_number

    def set_pulse_name(self, pulse_name):
        # Update the pulse name in the dictionary
        self.pulse_dictionary.pulse_name = pulse_name
        # update tab name only outside the initialization mode to prevent wrong tab name update!
        if not self.is_initialization:
            self.update_name_signal.emit(pulse_name)

    def set_initial_guess_lambda_function_widget(self):
        self.initial_guess_scroll_area.takeWidget()
        self.initial_guess_scroll_area.setWidget(self.initial_guess_lambda_function_form)
        self.initial_guess_lambda_function_form = self.initial_guess_scroll_area.widget()

    def set_fourier_basis_widget(self):
        self.basis_scroll_area.takeWidget()
        self.basis_scroll_area.setWidget(self.fourier_basis_form)
        self.fourier_basis_form = self.basis_scroll_area.widget()

    def set_sigmoid_basis_widget(self):
        self.basis_scroll_area.takeWidget()
        self.basis_scroll_area.setWidget(self.sigmoid_basis_form)
        self.sigmoid_basis_form = self.basis_scroll_area.widget()

    def set_chebyshev_basis_widget(self):
        self.basis_scroll_area.takeWidget()
        self.basis_scroll_area.setWidget(self.chebyshev_basis_form)
        self.chebyshev_basis_form = self.basis_scroll_area.widget()

    def set_scaling_function_lambda_function_widget(self):
        self.scaling_function_scroll_area.takeWidget()
        self.scaling_function_scroll_area.setWidget(self.scaling_function_lambda_function_form)
        self.scaling_function_lambda_function_form = self.scaling_function_scroll_area.widget()

    def set_initial_guess_list_function_widget(self):
        self.initial_guess_scroll_area.takeWidget()
        self.initial_guess_scroll_area.setWidget(self.initial_guess_list_function_form)
        self.initial_guess_list_function_form = self.initial_guess_scroll_area.widget()

    def set_scaling_function_list_function_widget(self):
        self.scaling_function_scroll_area.takeWidget()
        self.scaling_function_scroll_area.setWidget(self.scaling_function_list_function_form)
        self.scaling_function_list_function_form = self.scaling_function_scroll_area.widget()

    def set_initial_guess_get_from_file_function_widget(self):
        self.initial_guess_scroll_area.takeWidget()
        self.initial_guess_scroll_area.setWidget(self.initial_guess_get_from_file_form)
        self.initial_guess_get_from_file_form = self.initial_guess_scroll_area.widget()

    def set_scaling_function_get_from_file_function_widget(self):
        self.scaling_function_scroll_area.takeWidget()
        self.scaling_function_scroll_area.setWidget(self.scaling_function_get_from_file_form)
        self.scaling_function_get_from_file_form = self.scaling_function_scroll_area.widget()

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

from quocspyside2interface.gui.algorithms.dcraboptimization.UniformDistribution import UniformDistribution
from quocspyside2interface.logic.OptimalAlgorithmDictionaries.SigmoidBasisDictionary import SigmoidBasisDictionary
from quocspyside2interface.gui.uiclasses.SigmoidBasisUI import Ui_Form


class SigmoidBasis(QtWidgets.QWidget, Ui_Form):
    def __init__(self, loaded_dictionary):
        super().__init__()
        self.setupUi(self)
        # Dictionary
        self.basis_dictionary = SigmoidBasisDictionary(loaded_dictionary=loaded_dictionary)
        # uniform distribution
        self.uniform_distribution_form = UniformDistribution(
            loaded_dictionary=loaded_dictionary.setdefault("random_super_parameter_distribution", {}))

        # Connection
        self.basis_vector_number_spinbox.valueChanged.connect(self.set_basis_vector_number)
        self.sigma_doubleSpinBox.valueChanged.connect(self.set_sigma)
        self.offset_doubleSpinBox.valueChanged.connect(self.set_offset)
        # Initialization
        self._initialize_settings()

    def _initialize_settings(self):
        self.super_parameter_setting_area.setWidget(self.uniform_distribution_form)
        self.super_parameter_setting_area.setWidgetResizable(True)
        self.basis_vector_number_spinbox.setValue(self.basis_dictionary.basis_vector_number)
        super_parameter_distribution_list = ["Uniform"]
        for distribution in super_parameter_distribution_list:
            self.freq_distribution_combobox.addItem(distribution)
        distribution_type = self.super_parameter_setting_area.widget().distribution_dictionary.distribution_name
        self.freq_distribution_combobox.itemText(super_parameter_distribution_list.index(distribution_type))
        self.sigma_doubleSpinBox.setValue(self.basis_dictionary.sigma)
        self.offset_doubleSpinBox.setValue(self.basis_dictionary.offset)
        #self.basis_dictionary.offset = 0.1 # ADD TO GUI
        #self.basis_dictionary.sigma = 0.1 # ADD TO GUI

    def set_basis_vector_number(self, basis_vector_number: int):
        self.basis_dictionary.basis_vector_number = basis_vector_number

    def set_sigma(self, sigma: float):
        self.basis_dictionary.sigma = sigma

    def set_offset(self, offset: float):
        self.basis_dictionary.offset = offset

    def get_dictionary(self):
        # Get the dictionary from the super_parameter distribution
        self.basis_dictionary.random_super_parameter_distribution = self.uniform_distribution_form.get_dictionary()
        return self.basis_dictionary.get_dictionary()

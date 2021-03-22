from qtpy import QtWidgets

from quocs_pyqtinterface.gui.algorithms.dcraboptimization.UniformDistribution import UniformDistribution
from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.FourierBasisDictionary import FourierBasisDictionary
from quocs_pyqtinterface.gui.uiclasses.FourierBasisUI import Ui_Form


class FourierBasis(QtWidgets.QWidget, Ui_Form):
    def __init__(self, loaded_dictionary):
        super().__init__()
        self.setupUi(self)
        # Dictionary
        self.basis_dictionary = FourierBasisDictionary(loaded_dictionary)
        # uniform distribution
        self.uniform_distribution_form = UniformDistribution(loaded_dictionary=loaded_dictionary["random_frequencies_distribution"])
        # Connection
        self.basis_vector_number_spinbox.valueChanged.connect(self.set_basis_vector_number)
        # Initialization
        self._initialize_settings()

    def _initialize_settings(self):
        self.frequency_setting_area.setWidget(self.uniform_distribution_form)
        self.basis_vector_number_spinbox.setValue(self.basis_dictionary.basis_vector_number)
        frequency_distribution_list = ["Uniform"]
        for distribution in frequency_distribution_list:
            self.freq_distribution_combobox.addItem(distribution)
        distribution_type = self.frequency_setting_area.widget().distribution_dictionary.distribution_name
        self.freq_distribution_combobox.itemText(frequency_distribution_list.index(distribution_type))

    def set_basis_vector_number(self):
        self.basis_dictionary.basis_vector_number = self.basis_vector_number_spinbox.value()

    def get_dictionary(self):
        return self.basis_dictionary.get_dictionary()

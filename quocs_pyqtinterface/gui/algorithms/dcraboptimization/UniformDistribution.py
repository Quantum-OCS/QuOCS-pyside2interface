from qtpy import QtWidgets
from qtpy import QtGui

from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.UniformDistributionDictionary \
    import UniformDistributionDictionary
from quocs_pyqtinterface.gui.uiclasses.UniformDistributionUI import Ui_Form


class UniformDistribution(QtWidgets.QWidget, Ui_Form):
    def __init__(self, loaded_dictionary):
        super().__init__()
        self.setupUi(self)

        # Dictionary fro the uniform distribution
        self.distribution_dictionary = UniformDistributionDictionary(loaded_dictionary)

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

    def set_lower_limit(self, lower_limit):
        self.distribution_dictionary.lower_limit = float(lower_limit)

    def set_upper_limit(self, upper_limit):
        self.distribution_dictionary.upper_limit = float(upper_limit)

    def _initialize_settings(self):
        self.lower_limit_line_edit.setText(str(self.distribution_dictionary.lower_limit))
        self.upper_limit_line_edit.setText(str(self.distribution_dictionary.upper_limit))

    def get_dictionary(self):
        return self.distribution_dictionary.get_dictionary()

from qtpy import QtWidgets, QtGui

from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.ParameterDictionary import ParameterDictionary
from quocs_pyqtinterface.gui.uiclasses.ParameterDefinitionUI import Ui_Form


class ParameterSettings(QtWidgets.QWidget, Ui_Form):
    def __init__(self, control_index, update_name_signal, loaded_dictionary=None):
        super().__init__()
        self.setupUi(self)

        self.control_index = control_index
        self.control_type = "parameter"
        self.update_name_signal = update_name_signal

        self.parameter_dictionary = ParameterDictionary(loaded_dictionary=loaded_dictionary)

        # Validator
        self.lower_limit_line_edit.setValidator(QtGui.QDoubleValidator())
        self.upper_limit_line_edit.setValidator(QtGui.QDoubleValidator())
        self.initial_value_line_edit.setValidator(QtGui.QDoubleValidator())
        self.initial_variation_line_edit.setValidator(QtGui.QDoubleValidator())

        # Connection
        self.parameter_name_line_edit.textChanged.connect(self.set_parameter_name)
        self.lower_limit_line_edit.textChanged.connect(self.set_lower_limit)
        self.upper_limit_line_edit.textChanged.connect(self.set_upper_limit)
        self.initial_value_line_edit.textChanged.connect(self.set_initial_value)
        self.initial_variation_line_edit.textChanged.connect(self.set_initial_variation)

        self.is_initialization = True
        # Initialization
        self._initialize_settings()
        self.is_initialization = False

    def _initialize_settings(self):
        self.parameter_name_line_edit.setText(self.parameter_dictionary.parameter_name)
        self.lower_limit_line_edit.setText(str(self.parameter_dictionary.lower_limit))
        self.upper_limit_line_edit.setText(str(self.parameter_dictionary.upper_limit))
        self.initial_value_line_edit.setText(str(self.parameter_dictionary.initial_value))
        self.initial_variation_line_edit.setText(str(self.parameter_dictionary.amplitude_variation))

    def set_parameter_name(self, parameter_name):
        self.parameter_dictionary.parameter_name = parameter_name
        if not self.is_initialization:
            self.update_name_signal.emit(parameter_name)

    def set_lower_limit(self, lower_limit):
        # TODO add gui validator
        self.parameter_dictionary.lower_limit = float(lower_limit)

    def set_upper_limit(self, upper_limit):
        # TODO add gui validator
        self.parameter_dictionary.upper_limit = float(upper_limit)

    def set_initial_value(self, initial_value):
        # TODO add gui validator
        self.parameter_dictionary.initial_value = float(initial_value)

    def set_initial_variation(self, initial_variation):
        # TODO add gui validator
        self.parameter_dictionary.amplitude_variation = float(initial_variation)

    def get_dictionary(self):
        return self.parameter_dictionary.get_dictionary()

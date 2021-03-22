from qtpy import QtWidgets

from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.dCRABSettingsDictionary import dCRABSettingsDictionary
from quocs_pyqtinterface.gui.uiclasses.dCRABSettingsUI import Ui_Form


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

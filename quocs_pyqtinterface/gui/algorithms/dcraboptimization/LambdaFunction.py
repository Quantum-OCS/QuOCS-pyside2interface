from qtpy import QtWidgets

from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.LambdaFunctionDictionary import LambdaFunctionDictionary
from quocs_pyqtinterface.gui.uiclasses.LambdaFunctionUI import Ui_Form


class LambdaFunction(QtWidgets.QWidget, Ui_Form):
    def __init__(self, loaded_dictionary=None):
        super().__init__()
        self.setupUi(self)
        # Create the dictionary
        self.lambda_function_dictionary = LambdaFunctionDictionary(loaded_dictionary=loaded_dictionary)
        # Initialization
        self._initialize_settings()

    def _initialize_settings(self):
        self.lambda_function_line_edit.setText(self.lambda_function_dictionary.lambda_function)

    def get_dictionary(self):
        return self.lambda_function_dictionary.get_dictionary()

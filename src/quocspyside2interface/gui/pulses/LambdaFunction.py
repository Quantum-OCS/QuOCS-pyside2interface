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
from qtpy import uic

import os

from quocspyside2interface.logic.pulses.LambdaFunctionDictionary import LambdaFunctionDictionary


LambdaFunctionWidget = uic.loadUiType(os.path.join(os.path.dirname(__file__), "LambdaFunction.ui"))[0]


class LambdaFunction(QtWidgets.QWidget, LambdaFunctionWidget):
    def __init__(self, loaded_dictionary=None, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # Create the dictionary
        self.lambda_function_dictionary = LambdaFunctionDictionary(loaded_dictionary=loaded_dictionary)
        # Connection
        self.lambda_function_line_edit.textChanged.connect(self.set_lambda_function)
        # Initialization
        self._initialize_settings()

    def _initialize_settings(self):
        self.lambda_function_line_edit.setText(self.lambda_function_dictionary.lambda_function)

    def set_lambda_function(self, lambda_function):
        self.lambda_function_dictionary.lambda_function = lambda_function

    def get_dictionary(self):
        return self.lambda_function_dictionary.get_dictionary()

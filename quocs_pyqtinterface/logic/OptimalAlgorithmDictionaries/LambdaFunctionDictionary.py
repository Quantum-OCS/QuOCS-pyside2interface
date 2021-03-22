from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class LambdaFunctionDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.function_type = "lambda_function"
        self.lambda_function = "lambda t: 1.0 + 0.0*t"

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

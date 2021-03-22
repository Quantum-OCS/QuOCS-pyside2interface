from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class ListFunctionDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.list_function = [0.0 for i in range(10)]
        self.function_type = "list_function"
        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

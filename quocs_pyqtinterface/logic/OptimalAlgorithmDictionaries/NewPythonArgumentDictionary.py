from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class NewPythonArgumentDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.name = "python_argument"
        self.type = "string"
        self.value = "test"

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

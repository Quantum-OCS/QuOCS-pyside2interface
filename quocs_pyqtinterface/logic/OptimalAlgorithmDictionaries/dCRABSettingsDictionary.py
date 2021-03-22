from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class dCRABSettingsDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.super_iteration_number = 2
        self.maximum_function_evaluations_number = 10

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

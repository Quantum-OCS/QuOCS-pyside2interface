from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class TimeDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.time_name = "time"
        self.initial_value = 1.0

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

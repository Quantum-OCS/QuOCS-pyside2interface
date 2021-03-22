from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class StoppingCriteriaNelderMeadDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.iterations_number = 100
        self.xatol = 1e-14
        self.frtol = 1e-14

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class NelderMeadDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.dsm_name = "nelder_mead"
        self.is_adaptive = True

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

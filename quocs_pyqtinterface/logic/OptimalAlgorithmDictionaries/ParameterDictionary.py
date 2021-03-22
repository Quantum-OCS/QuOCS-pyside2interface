from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class ParameterDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary: dict = None, index: str = ""):
        # Default values
        self.parameter_name = "Parameter" + index
        self.lower_limit = -2.0
        self.upper_limit = 2.0
        self.initial_value = 0.0
        self.amplitude_variation = 0.5

        super().__init__(loaded_dictionary)

    def get_dictionary(self) -> dict:
        return self.__dict__

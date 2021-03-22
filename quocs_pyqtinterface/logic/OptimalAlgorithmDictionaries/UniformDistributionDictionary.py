from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class UniformDistributionDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.distribution_name = "Uniform"
        self.lower_limit = 0.1
        self.upper_limit = 3.0

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

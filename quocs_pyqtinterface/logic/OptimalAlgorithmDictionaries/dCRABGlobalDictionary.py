from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class dCRABGlobalDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.optimization_client_name = "Optimization_dCRAB_Test"
        self.opti_algorithm_name = "dCRAB"
        self.algorithm_settings = {}
        self.dsm_settings = {}
        self.pulses = []
        self.times = []
        self.parameters = []
        self.communication = {}
        self.figure_of_merit = {}
        super().__init__(loaded_dictionary)

    def update_dictionary(self, new_dictionary):
        for element in new_dictionary:
            if element in self.__dict__:
                self.__dict__[element] = new_dictionary[element]

    def get_dictionary(self):
        optimization_dictionary = self.__dict__.copy()
        optimization_dictionary.pop("communication", None)
        optimization_dictionary.pop("figure_of_merit", None)

        return {"optimization_dictionary": optimization_dictionary, "communication": self.communication,
                "figure_of_merit": self.figure_of_merit}

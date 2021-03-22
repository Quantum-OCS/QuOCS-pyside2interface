from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary
import os


class AllInOneCommunicationDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.communication_type = "AllInOneCommunication"
        self.results_folder = os.path.join(os.getcwd(), "QuOCS_Results")

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

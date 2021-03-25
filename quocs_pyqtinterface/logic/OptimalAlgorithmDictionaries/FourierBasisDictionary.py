from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class FourierBasisDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.basis_name = "Fourier"
        self.basis_class = "Fourier"
        self.basis_module = "quocs_optlib.pulses.basis.Fourier"
        self.basis_vector_number = 2
        self.random_frequencies_distribution = {}

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

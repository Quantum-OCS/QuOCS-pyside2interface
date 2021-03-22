from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class PulseDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.pulse_name = "Pulse"
        self.upper_limit = 1.0
        self.lower_limit = -1.0
        self.bins_number = 101
        self.time_name = "Time"
        self.amplitude_variation = 0.1
        self.basis = {
            "basis_name": "Fourier",
            "basis_vector_number": 2,
            "random_frequencies_distribution": {
                "distribution_name": "Uniform",
                "lower_limit": 0.1,
                "upper_limit": 5.0
            }
        }
        self.scaling_function = {
            "function_type": "lambda_function",
            "lambda_function": "lambda t: 1.0 + 0.0*t"
        }
        self.initial_guess = {
            "function_type": "lambda_function",
            "lambda_function": "lambda t: 0.0*t"
        }
        # Load the dictionary in case there is one
        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

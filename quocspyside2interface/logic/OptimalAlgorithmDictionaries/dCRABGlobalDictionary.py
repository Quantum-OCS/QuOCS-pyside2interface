# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright 2021-  QuOCS Team
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from quocspyside2interface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class dCRABGlobalDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.optimization_client_name = "Optimization_dCRAB_Test"
        self.opti_algorithm_name = "dCRAB"
        self.opti_algorithm_module = "quocs_optlib.optimalalgorithms.dCRABAlgorithm"
        self.opti_algorithm_class = "DCrabAlgorithm"
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

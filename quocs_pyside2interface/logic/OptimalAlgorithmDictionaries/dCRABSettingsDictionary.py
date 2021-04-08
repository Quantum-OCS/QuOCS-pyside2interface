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

from quocs_pyside2interface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class dCRABSettingsDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.super_iteration_number = 2
        self.maximum_function_evaluations_number = 10

        super().__init__(loaded_dictionary)

    def get_dictionary(self):
        return self.__dict__

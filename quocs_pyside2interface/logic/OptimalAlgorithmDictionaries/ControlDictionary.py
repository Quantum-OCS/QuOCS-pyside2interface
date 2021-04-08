"""#####"""

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


class ControlsDictionary:

    def __init__(self):
        # Default values
        self.pulses = {}
        self.parameters = {}
        self.times = {}

        self.index_number = 0

    def remove_control(self, control_type_to_remove, index_name):
        control_list = [self.pulses, self.parameters, self.times]
        control_type = ["pulse", "parameter", "time"]
        #
        for c_t, c_l in zip(control_type, control_list):
            if control_type_to_remove == c_t:
                c_l.pop(index_name)

    def add_control(self, control_type_to_add, dictionary_to_add, index_name):
        control_list = [self.pulses, self.parameters, self.times]
        control_type = ["pulse", "parameter", "time"]
        # TODO Add the control
        for c_t, c_l in zip(control_type, control_list):
            if control_type_to_add == c_t:
                c_l[index_name] = dictionary_to_add
        #
        self.index_number += 1

    def get_dictionary(self):
        return self.__dict__

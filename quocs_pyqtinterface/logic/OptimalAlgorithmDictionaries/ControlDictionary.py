"""#####"""

from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


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

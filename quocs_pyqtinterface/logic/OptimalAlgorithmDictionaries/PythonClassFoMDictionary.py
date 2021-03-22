from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.SettingsDictionary import SettingsDictionary


class PythonClassFomDictionary(SettingsDictionary):

    def __init__(self, loaded_dictionary=None):
        # Default values
        self.program_type = "TestClass"
        self.python_module = "OptimalControlProblems.OneQubitClass"
        self.python_class = "OneQubit"
        self.further_args = {}

        # Other variables
        self.argument_index = 0

        super().__init__(loaded_dictionary)

    def remove_argument(self, name):
        self.further_args.pop(name, None)

    def add_argument(self, argument_index_name, argument_dict):
        self.further_args[argument_index_name] = argument_dict
        self.argument_index += 1

    def update_argument(self, argument_index_name, argument_dict):
        # TODO Error in case two arguments have the same names
        self.further_args[argument_index_name] = argument_dict

    # TODO Change this module
    def get_arguments_list(self):
        further_args = self.python_class_dictionary["FurtherArgs"]
        arguments_list = []
        for argument in further_args:
            argument_dict = {}
            value = further_args[argument]
            type_value = "string"
            if type(value) is float:
                type_value = "float"
            elif type(value) is int:
                type_value = "int"
            elif type(value) is bool:
                type_value = "bool"
            argument_dict["type"] = type_value
            argument_dict["name"] = argument
            argument_dict["value"] = value
            arguments_list.append(argument_dict)

        return arguments_list

    def get_dictionary(self):
        # TODO Rethink what to do here
        further_args = {}
        for element in self.further_args:
            further_args[self.further_args[element]["name"]] = self.further_args[element]
        total_dict = self.__dict__.copy()
        total_dict.pop("further_args", None)
        total_dict.pop("argument_index", None)
        return {"further_args": further_args, **total_dict}

    def get_summary_list(self):
        # Modify this module
        summary_list = []
        summary_list.append("Python Class FoM evaluation")
        summary_list.append("Python Module: " + str(self.python_class_dictionary["PythonModule"]) )
        summary_list.append("Python Class: " + str(self.python_class_dictionary["PythonClass"]))
        summary_list.append("Further args")
        further_args = self.python_class_dictionary["FurtherArgs"]
        for element in further_args:
            summary_list.append(element + " : " + str(further_args[element]))
        return summary_list

from abc import abstractmethod


class SettingsDictionary:

    def __init__(self, loaded_dictionary):
        if loaded_dictionary is not None:
            for element in loaded_dictionary:
                setattr(self, element, loaded_dictionary[element])

    @abstractmethod
    def get_dictionary(self):
        raise NotImplementedError("This method has to be implemented in the Settings class")

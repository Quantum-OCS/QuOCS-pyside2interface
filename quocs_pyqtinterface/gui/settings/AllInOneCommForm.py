import os

from quocs_pyqtinterface.logic.OptimalAlgorithmDictionaries.AllInOneCommunicationDictionary import \
    AllInOneCommunicationDictionary
from qtpy import QtWidgets
from quocs_pyqtinterface.gui.uiclasses.AllInOneCommunicationUI import Ui_Form


class AllInOneCommForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None, loaded_dictionary=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()
        # dictionary
        self.all_in_one_communication_dictionary = AllInOneCommunicationDictionary(loaded_dictionary=loaded_dictionary)
        # Button connection
        self.get_results_folder_button.clicked.connect(self.get_results_folder)
        # initialization
        self._initialization()

    def _initialization(self):
        self.results_folder_edit_line.setText(self.all_in_one_communication_dictionary.results_folder)

    def get_results_folder(self):
        # TODO get the results folder
        pass

    def get_dictionary(self):
        return self.all_in_one_communication_dictionary.get_dictionary()

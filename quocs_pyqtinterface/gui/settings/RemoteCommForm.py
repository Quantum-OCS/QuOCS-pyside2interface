import os
from qtpy import QtWidgets

from quocs_pyqtinterface.logic.utilities.readjson import readjson
from quocs_pyqtinterface.logic.ComunicationSettingsDictionaries.RemoteCommunicationDictionary \
    import RemoteCommunicationDictionary
from quocs_pyqtinterface.gui.uiclasses.RemoteConnectionUI import Ui_Form


class RemoteCommForm(QtWidgets.QWidget, Ui_Form):
    """ Widget for the Remote Communication """
    credential_data = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Dictionary
        self.remote_communication_dictionary = RemoteCommunicationDictionary()
        # Connection
        self.get_credential_file_button.clicked.connect(self.get_credential_filename)
        self.check_connection_button.clicked.connect(self.check_connection)
        self.get_shared_folder_button.clicked.connect(self.get_shared_folder)
        self.get_results_folder_button.clicked.connect(self.get_results_folder)
        # Initialization
        self._initialization()

    def _initialization(self):

        pass

    def get_results_folder(self):
        # TODO get the results folder
        pass

    def get_shared_folder(self):
        # TODO get the shared folder
        pass

    def get_credential_filename(self):
        """Get the credential data from a json file"""
        filename = QtWidgets.QFileDialog.getOpenFileName(self,
                    "Open credential file", os.getcwd(), "json (*.json)", options=QtWidgets.QFileDialog.DontUseNativeDialog)
        err_stat, credential_data = readjson(filename[0])
        self.credential_data = credential_data
        self.credential_file_edit_line.setText(filename[0])

    def check_connection(self):
        """Check the connection before starting the optimization"""
        # TODO Check connection by using the remote connection class (_init and end)
        pass

    def get_dictionary(self):
        return self.remote_communication_dictionary.get_dictionary()

    def get_summary_list(self):
        return self.remote_communication_dictionary.get_summary_list()
from qtpy import QtWidgets

from quocs_pyqtinterface.gui.uiclasses.LocalCommunicationUI import Ui_Form


class LocalCommForm(QtWidgets.QWidget, Ui_Form):
    """Widget for the Local communication"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.get_shared_folder_button.clicked.connect(self.get_shared_folder)
        self.get_results_folder_button.clicked.connect(self.get_results_folder)

    def get_results_folder(self):
        # TODO get the results folder
        pass

    def get_shared_folder(self):
        # TODO get the shared folder
        pass

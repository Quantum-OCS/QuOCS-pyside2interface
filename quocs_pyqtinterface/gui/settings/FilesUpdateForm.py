from qtpy import QtWidgets

from quocs_pyqtinterface.gui.uiclasses.FilesUpdateUI import Ui_Form


class FilesUpdateForm(QtWidgets.QWidget, Ui_Form):
    """Widget for the Files Update Communication"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Button connection
        self.get_update_folder_button.clicked.connect(self.get_update_folder)

    def get_update_folder(self):
        # TODO get the results folder
        pass

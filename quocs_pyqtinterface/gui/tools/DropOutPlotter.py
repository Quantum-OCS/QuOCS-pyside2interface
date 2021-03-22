from qtpy import QtWidgets

from quocs_pyqtinterface.gui.uiclasses.DropOutPlotterUI import Ui_Dialog


class DropOutPlotter(QtWidgets.QDialog, Ui_Dialog):
    """Drop out dialogue for the plotter"""
    def __init__(self, id_window, remove_window_signal, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.id_window = id_window
        self.remove_window_signal = remove_window_signal

    def closeEvent(self, event):
        """Delete the plotter from the plotter """
        # Send signal to delete the plotter from the fom_plotter dictionary
        self.remove_window_signal.emit(self.id_window)
        # Close the window
        event.accept()

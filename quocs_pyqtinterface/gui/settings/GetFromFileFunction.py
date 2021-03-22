from qtpy import QtWidgets
import os

from quocs_pyqtinterface.gui.uiclasses.GetFromFileFunctionUI import Ui_Form


class GetFromFileFunction(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pulses_data = None
        # TODO Enable list index spinbox only when the json file is available

    def get_from_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open Pulse file",
                                                         os.getcwd(), "json (*.json)", options=
                                                         QtWidgets.QFileDialog.DontUseNativeDialog)
        from quocs_pyqtinterface.logic.utilities.readjson import readjson
        err_code, self.pulses_data = readjson(filename[0])
        if err_code != 0:
            print("")

    def check_pulse(self):
        # Get the list from file and plot it out to verify how it looks
        pass

    def get_dictionary(self):
        pass

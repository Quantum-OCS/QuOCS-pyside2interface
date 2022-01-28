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

from qtpy import QtWidgets
from qtpy import uic
import os


DropOutPlotterWidget = uic.loadUiType(os.path.join(os.path.dirname(__file__), "DropOutPlotter.ui"))[0]


class DropOutPlotter(QtWidgets.QDialog, DropOutPlotterWidget):
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

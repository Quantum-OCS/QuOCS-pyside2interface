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

from random import randint
from qtpy import QtWidgets
from qtpy import QtCore
import numpy as np

from quocspyside2interface.gui.OptimizationBasicGui import OptimizationBasicGui
from quocspyside2interface.logic.OptimizationBasic import OptimizationBasic
import time


class Optimizer:
    def __init__(self, fom_plotter_signal, controls_update_signal, handle_exit_obj):
        self.controls_update_signal = controls_update_signal
        self.fom_plotter_signal = fom_plotter_signal
        self.handle_exit_obj = handle_exit_obj

    def begin(self):
        print("Start the initialization")
        time.sleep(2.0)

    def run(self):
        print("Run the optimization")
        pulses_number = 5
        parameters_number = 3
        time_grids_list = [np.linspace(0.0, 1.0 * (i + 1), 100 * (i + 1)) for i in range(pulses_number)]
        for i in range(100):
            time.sleep(0.2)
            self.fom_plotter_signal.emit(i, randint(0, 100))
            pulses_list = [np.random.rand(100 * (ii + 1), ) for ii in range(pulses_number)]
            parameters_list = [np.random.rand() for _ in range(parameters_number)]
            self.controls_update_signal.emit(pulses_list, time_grids_list, parameters_list)
            if not self.handle_exit_obj.is_user_running:
                return

    def end(self):
        print("End the optimization")


class OptimizationLogic(QtCore.QObject, OptimizationBasic):
    def start_optimization(self, opti_comm_dict):
        print("The dictionary you used")
        optimizer_obj = Optimizer(self.fom_plot_signal, self.controls_update_signal, self.handle_exit_obj)
        try:
            optimizer_obj.begin()
            optimizer_obj.run()
        except Exception as ex:
            print("Unhandled exception: {}".format(ex.args))
            print("something goes wrong")
        finally:
            optimizer_obj.end()
        self.message_label_signal.emit("The optimization is finished")
        self.is_running_signal.emit(False)


class OptimizationSuiteGui(QtWidgets.QMainWindow, OptimizationBasicGui):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.optimizationlogic = OptimizationLogic()

        # Handle Thread for the optimization
        self.thread_optimization = QtCore.QThread(self)
        self.optimizationlogic.moveToThread(self.thread_optimization)
        self.thread_optimization.start()

        self.handle_ui_elements()
        self._mw.closeEvent = self.closeEvent
        # Activate the start button for testing
        self._mw.start_optimization_button.setEnabled(True)

    def closeEvent(self, event):
        # Send the signal to the handle exit obj
        print("I am closing the Main Window ...")
        self.stop_optimization_signal.emit(False)
        print("Emitted signal to stop the optimization")
        # Close the optimization thread
        self.thread_optimization.quit()
        print("I am quitting the optimization thread")
        while self.thread_optimization.isRunning():
            print("The thread is still running ...")
            time.sleep(0.05)
        print("The thread is closed.")
        print("Bye Bye QuOCS")
        event.accept()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = OptimizationSuiteGui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

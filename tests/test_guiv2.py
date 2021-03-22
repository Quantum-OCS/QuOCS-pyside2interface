from random import randint
from qtpy import QtWidgets
from qtpy import QtCore
import numpy as np

from quocs_pyqtinterface.gui.OptimizationBasicGui import OptimizationBasicGui
from quocs_pyqtinterface.logic.OptimizationBasic import OptimizationBasic
import time


class Optimizer:
    def __init__(self, fom_plotter_signal, pulse_plotter_signal):
        self.pulse_plotter_signal = pulse_plotter_signal
        self.fom_plotter_signal = fom_plotter_signal

    def begin(self):
        print("Start the initialization")
        time.sleep(2.0)

    def run(self):
        print("Run the optimization")
        time_grid = np.linspace(0.0, 1.0, 100)
        for i in range(100):
            time.sleep(0.2)
            self.fom_plotter_signal.emit(i, randint(0, 100))
            self.pulse_plotter_signal.emit([time_grid, time_grid], [np.random.rand(100,), - np.random.rand(100,)])

    def end(self):
        print("End the optimization")


class OptimizationLogic(QtCore.QObject, OptimizationBasic):
    def start_optimization(self, opti_comm_dict):
        print("The dictionary you used")
        optimizer_obj = Optimizer(self.fom_plot_signal, self.pulse_plot_signal)
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

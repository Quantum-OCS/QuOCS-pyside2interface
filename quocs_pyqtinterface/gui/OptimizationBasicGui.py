# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright [2021] Optimal Control Suite
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
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os

from qtpy import QtCore
from qtpy import QtWidgets
import pyqtgraph as pg

from quocs_pyqtinterface.gui.tools.DropOutPlotter import DropOutPlotter
from quocs_pyqtinterface.logic.utilities.readjson import readjson
from quocs_pyqtinterface.gui.algorithms.dcraboptimization.dCRABSettingsDialog import dCRABSettingsDialog
from quocs_pyqtinterface.gui.algorithms.pureparametersoptimization.DirectSearchSettingsDialog import \
    DirectSearchSettingsDialog
from quocs_pyqtinterface.gui.uiclasses.MainWindowUI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


class OptimizationBasicGui:
    optimizationlogic = None
    ########################
    # Signal to logic class
    ########################
    # Start optimization
    start_optimization_signal = QtCore.Signal(dict)
    # Stop Optimization
    stop_optimization_signal = QtCore.Signal(bool)
    # Update dictionary fom plotter
    update_plotter_dictionary_signal = QtCore.Signal(int)
    # Dictionary signal
    load_dictionary_signal = QtCore.Signal(dict)
    ##################################
    # Items to plot
    ##################################
    # Logo
    logo_item = None
    # Pulse
    pulse_item = None
    ###################################
    # Windows
    ###################################
    _mw: QtWidgets.QMainWindow
    ###################################
    # Other variables
    ###################################
    # parameters list
    parameters_list = [""]
    # Current fom plotter dictionary
    fom_plotter_dict = {}
    pulses_plotter_dict = {}
    pulses_plotter_list: list = [{"pulse_index": 0, "plotter": {"pyqt_obj": None, "data_obj": None}}]
    pulses_data_dict = {}
    iterations_number: list = []
    fom_evaluation: list = []
    # Optimization - Communication dictionary
    opti_comm_dict: dict = {"version": "dev"}

    def handle_ui_elements(self):
        ###################################
        # Windows
        ###################################
        self._mw = MainWindow()
        # Check if the optimization object was initialized in the sub class
        if self.optimizationlogic is None:
            raise Exception("Optimization logic object is not initialized in the sub class")
        ########################################################################
        #                            Configure widgets                         #
        ########################################################################
        self._mw.stop_optimization_button.setEnabled(False)
        self._mw.start_optimization_button.setEnabled(False)
        self._mw.main_operations_label.setText("Open or create a new configuration file")
        self._mw.optimization_details_plain_text.setReadOnly(True)
        #########################################################################
        # Connect buttons with functions
        #########################################################################
        # Start Button
        self._mw.start_optimization_button.clicked.connect(self.start_optimization)
        # Stop Button
        self._mw.stop_optimization_button.clicked.connect(self.stop_optimization)
        # Drop out plotter
        self._mw.drop_out_fom_button.clicked.connect(self.drop_out_plotter)
        # Connect spinbox with function
        self._mw.select_parameter_spinbox.setMinimum(1)
        self._mw.select_parameter_spinbox.valueChanged.connect(self._update_parameter_choice)
        # Connect file menu action
        # self._mw.new_action.triggered.connect(self._get_pure_parameters_optimization_dialog)
        self._mw.parameters_optimization_action.triggered.connect(self._get_pure_parameters_optimization_dialog)
        self._mw.dcrab_optimization_action.triggered.connect(self._get_dcrab_optimization_dialog)
        self._mw.load_file_action.triggered.connect(self._load_configuration_file)
        # Other operations
        self.fom_plotter_dict["0"] = self._mw.fom_plotter
        self.pulses_plotter_dict["0"] = self._mw.pulses_plotter
        self.pulses_data_dict["0"] = None
        self.pulses_plotter_list[0]["plotter"]["pyqt_obj"] = self._mw.pulses_plotter
        self._mw.previous_pulse_plot_button.clicked.connect(self.previous_plot_pulse)
        self._mw.next_pulse_plot_button.clicked.connect(self.next_plot_pulse)

        #########################################################################
        # Signals
        #########################################################################
        # Start optimization signal
        self.start_optimization_signal.connect(self.optimizationlogic.start_optimization)
        # Update status optimization signal from is_running logic to the optimization logic
        # TODO check the status optimization here
        # Update status optimization signal from Optimization logic to GUI
        self.optimizationlogic.is_running_signal.connect(self.finished_optimization)
        # Update fom plotter dictionary
        self.update_plotter_dictionary_signal.connect(self.update_fom_plotter_dictionary)
        # Stop signal
        self.stop_optimization_signal.connect(self.optimizationlogic.handle_exit_obj.set_is_user_running)
        # Update message signal
        self.optimizationlogic.message_label_signal.connect(self.label_messages)
        # Update the plot data signal
        self.optimizationlogic.fom_plot_signal.connect(self.update_fom_graph)
        # Update the pulse plot
        self.optimizationlogic.pulse_plot_signal.connect(self.update_pulses_graph)
        # Update the parameters array
        self.optimizationlogic.parameters_update_signal.connect(self.update_parameters_list)
        # Dictionaries signal
        self.load_dictionary_signal.connect(self.update_optimization_dictionary)

    def next_plot_pulse(self):
        # [{"pulse_index": 0, "plotter": {"pyqt_obj": None, "data_obj": None}}]
        # TODO Put limits on pulse index
        self.pulses_plotter_list[0]["pulse_index"] += 1

    def previous_plot_pulse(self):
        # [{"pulse_index": 0, "plotter": {"pyqt_obj": None, "data_obj": None}}]
        # TODO Put limits on pulse_index
        self.pulses_plotter_list[0]["pulse_index"] -= 1

    @QtCore.Slot(int)
    def update_fom_plotter_dictionary(self, id_window):
        """Remove plotter from the dictionary"""
        del self.fom_plotter_dict[str(id_window)]

    def _get_pure_parameters_optimization_dialog(self):
        print("Try to open pure parametrization settings")
        pure_parameter_optimization_dialog = \
            DirectSearchSettingsDialog(load_full_dictionary_signal=self.load_dictionary_signal)
        pure_parameter_optimization_dialog.exec_()

    def _get_dcrab_optimization_dialog(self):
        print("Try to open dcrab optimization settings")
        dcrab_optimization_dialog = dCRABSettingsDialog(load_full_dictionary_signal=self.load_dictionary_signal)
        dcrab_optimization_dialog.exec_()

    def _load_configuration_file(self):
        #
        print("Try to load an optimization Dialog")
        # Get the file
        filename = QtWidgets.QFileDialog.getOpenFileName(self._mw,
                                                         "Open credential file", os.getcwd(), "json (*.json)",
                                                         options=QtWidgets.QFileDialog.DontUseNativeDialog)
        err_stat, user_data = readjson(filename[0])
        # Open the json file and get the dictionary
        if err_stat != 0:
            # TODO Error in the GUI
            pass
        else:
            implemented_algorithms = {"dCRAB": dCRABSettingsDialog, "DirectSearchMethod": DirectSearchSettingsDialog}
            opti_algorithm_name = user_data["optimization_dictionary"]["opti_algorithm_name"]
            if opti_algorithm_name in implemented_algorithms:
                print("I am loading {0} dialog".format(opti_algorithm_name))
                optimization_dialog = implemented_algorithms[opti_algorithm_name](loaded_dictionary=user_data, load_full_dictionary_signal=self.load_dictionary_signal)
                optimization_dialog.exec_()
            else:
                # TODO Raise error in the GUI
                pass

    def drop_out_plotter(self):
        """Drop out the plotter"""
        id_plotter_window = len(self.fom_plotter_dict)
        plotter_window = DropOutPlotter(id_plotter_window, self.update_plotter_dictionary_signal, parent=self._mw)
        self.fom_plotter_dict[str(id_plotter_window)] = plotter_window.fom_plotter
        plotter_window.show()

    @QtCore.Slot(list)
    def update_parameters_list(self, parameters_list):
        """Update the parameters list at every iteration"""
        self.parameters_list = parameters_list
        # Update parameter range in the spinbox
        self._mw.select_parameter_spinbox.setMaximum(len(parameters_list))
        # Update parameter also in the label
        self._update_parameter_choice()

    def _update_parameter_choice(self):
        """display in the parameter label the parameter you choose"""
        parameter_value = str(self.parameters_list[self._mw.select_parameter_spinbox.value() - 1])
        self._mw.value_parameter_label.setText(parameter_value)

    @QtCore.Slot()
    def finished_optimization(self):
        """The optimization is finished. Update buttons"""
        # Disable the stop button
        self._mw.stop_optimization_button.setEnabled(False)
        # Enable the start button
        self._mw.start_optimization_button.setEnabled(True)

    @QtCore.Slot(list, list)
    def update_pulses_graph(self, time_grids_list, pulses_list):
        """Update all the current pulses plotters"""
        index_list = [i for i in range(len(pulses_list))]
        print("I am in the update pulses module")
        for time_grid, pulse, index in zip(time_grids_list, pulses_list, index_list):
            # [{"pulse_index": 0, "plotter": {"pyqt_obj": None, "data_obj": None}}]
            for plotter_obj in self.pulses_plotter_list:
                if plotter_obj["pulse_index"] == index:
                    if plotter_obj["plotter"]["data_obj"] is None:
                        print("First iteration")
                        pen = pg.mkPen(color=(255, 0, 0))
                        plotter_obj["plotter"]["data_obj"] = plotter_obj["plotter"]["pyqt_obj"].plot(time_grid, pulse,
                                                                                                     pen=pen)
                    else:
                        print("Update")
                        plotter_obj["plotter"]["data_obj"].setData(time_grid, pulse)

    @QtCore.Slot(int, float)
    def update_fom_graph(self, iteration_number, fom):
        """update all the current fom plotters"""
        # TODO Substitute scatter plot with fom plotter
        self.fom_evaluation.append(fom)
        self.iterations_number.append(iteration_number)
        for plotter_id in self.fom_plotter_dict:
            # If the first iteration create the line
            if len(self.fom_evaluation) == 1:
                pen = pg.mkPen(color=(255, 0, 0))
                self.fom_data = self.fom_plotter_dict[plotter_id].plot(self.iterations_number, self.fom_evaluation,
                                                                       pen=pen, symbol='o')
            else:
                # Set the data
                self.fom_data.setData(self.iterations_number, self.fom_evaluation)

    @QtCore.Slot(dict)
    def update_optimization_dictionary(self, opti_comm_dict):
        # Update the optimization dictionary in the optimization details and in the internal dictionary before starting
        # the optimization
        self.opti_comm_dict = opti_comm_dict
        # Update opti dictionary
        self._mw.optimization_details_plain_text.setPlainText(str(opti_comm_dict))
        # Enable start button
        self._mw.start_optimization_button.setEnabled(True)
        # Update label message
        self.label_messages("It is possible to start the optimization")

    def clear_fom_graph(self):
        """Clean the data points and the list"""
        for plotter_id in self.fom_plotter_dict:
            self.fom_plotter_dict[plotter_id].clear()
        self.fom_evaluation = []
        self.iterations_number = []

    def start_optimization(self):
        """Emit the start optimization signal"""
        # Disable the start button
        self._mw.start_optimization_button.setEnabled(False)
        # Send the signal to the handle exit obj
        self.stop_optimization_signal.emit(True)
        # Remove the logo from the canvas
        if self.logo_item is not None:
            self._mw.fom_plotter.removeItem(self.logo_item)
        # Start the optimization
        self.clear_fom_graph()
        # Send the optimization dictionary with the comm fom settings to the optimization logic interface
        self.start_optimization_signal.emit(self.opti_comm_dict)
        # Enable stop optimization button
        self._mw.stop_optimization_button.setEnabled(True)

    def stop_optimization(self):
        """Stop the counter"""
        # Disable the stop button
        self._mw.stop_optimization_button.setEnabled(False)
        # Send the signal to the handle exit obj
        self.stop_optimization_signal.emit(False)
        # Enable the start button
        self._mw.start_optimization_button.setEnabled(True)

    @QtCore.Slot(str)
    def label_messages(self, message):
        """Update the label with the message"""
        self._mw.main_operations_label.setText(message)

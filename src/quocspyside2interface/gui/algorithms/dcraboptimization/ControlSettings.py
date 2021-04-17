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

from qtpy import QtCore
from qtpy import QtWidgets

from quocspyside2interface.gui.algorithms.dcraboptimization.ParameterSettings import ParameterSettings
from quocspyside2interface.gui.algorithms.dcraboptimization.PulsesSettings import PulseSettings
from quocspyside2interface.gui.algorithms.dcraboptimization.TimeSettings import TimeSettings
from quocspyside2interface.logic.OptimalAlgorithmDictionaries.ControlDictionary import ControlsDictionary
from quocspyside2interface.gui.uiclasses.ControlsTabUI import Ui_Form


class ControlsSettings(QtWidgets.QWidget, Ui_Form):
    # Signals
    update_tab_name_signal = QtCore.Signal(str)
    update_time_combo_box_pulse = QtCore.Signal()
    update_time_value_signal = QtCore.Signal(str)

    def __init__(self, loaded_dictionary=None):
        super().__init__()
        self.setupUi(self)
        # Variables
        self.curr_tab_index = 0
        # Dictionary class
        self.control_dictionary = ControlsDictionary()
        # Connection
        self.add_pulse_button.clicked.connect(self.add_pulse_widget)
        self.add_parameter_button.clicked.connect(self.add_parameter_widget)
        self.add_time_button.clicked.connect(self.add_time_widget)
        self.controls_tab.currentChanged.connect(self.set_curr_tab_index)
        self.remove_control_button.clicked.connect(self.remove_control_widget)
        self.update_tab_name_signal.connect(self.update_widget_name)
        self.update_time_combo_box_pulse.connect(self.update_time_for_pulse_combobox)
        # Initialization
        self._initialization(loaded_dictionary=loaded_dictionary)

    def _initialization(self, loaded_dictionary=None):
        # [pulses, parameters, times]
        if loaded_dictionary is not None:
            [pulses_list, parameters_list, times_list] = [loaded_dictionary[0], loaded_dictionary[1], loaded_dictionary[2]]
            for pulse_dictionary in pulses_list:
                self.initialize_pulse_widget(pulse_dictionary=pulse_dictionary)
            for time_dictionary in times_list:
                self.initialize_time_widget(time_dictionary=time_dictionary)
            for parameter_dictionary in parameters_list:
                self.initialize_parameter_widget(parameter_dictionary=parameter_dictionary)

    def initialize_pulse_widget(self, pulse_dictionary=None):
        index_name = str(self.control_dictionary.index_number)
        control_widget = PulseSettings(index_name, self.update_tab_name_signal, loaded_dictionary=pulse_dictionary)
        pulse_name = control_widget.pulse_dictionary.pulse_name
        tab_index = self.controls_tab.addTab(control_widget, pulse_name)
        self.control_dictionary.add_control("pulse", control_widget.get_dictionary(), index_name)
        self.controls_tab.setCurrentIndex(tab_index)

    def initialize_time_widget(self, time_dictionary=None):
        index_name = str(self.control_dictionary.index_number)
        control_widget = TimeSettings(index_name, self.update_tab_name_signal, self.update_time_combo_box_pulse,
                                      loaded_dictionary=time_dictionary)
        time_name = control_widget.time_dictionary.time_name
        tab_index = self.controls_tab.addTab(control_widget, time_name)
        self.control_dictionary.add_control("time", control_widget.get_dictionary(), index_name)
        self.controls_tab.setCurrentIndex(tab_index)
        self.update_time_for_pulse_combobox()

    def initialize_parameter_widget(self, parameter_dictionary=None):
        index_name = str(self.control_dictionary.index_number)
        control_widget = ParameterSettings(index_name, self.update_tab_name_signal,
                                           loaded_dictionary=parameter_dictionary)
        parameter_name = control_widget.parameter_dictionary.parameter_name
        tab_index = self.controls_tab.addTab(control_widget, parameter_name)
        self.control_dictionary.add_control("parameter", control_widget.get_dictionary(), index_name)
        self.controls_tab.setCurrentIndex(tab_index)

    def add_pulse_widget(self):
        self.initialize_pulse_widget()

    def add_parameter_widget(self):
        self.initialize_parameter_widget()

    def add_time_widget(self):
        self.initialize_time_widget()

    def update_widget_name(self, tab_name):
        #print("{0}, {1}".format(self.curr_tab_index, self.controls_tab.currentIndex()))
        if self.curr_tab_index == self.controls_tab.currentIndex():
            self.controls_tab.setTabText(self.curr_tab_index, tab_name)

    # def update_time_in_pulse_combobox(self, previous_time_name, new_time_name, time_value):
    #     # Get the total number of tab
    #     tabs_number = self.controls_tab.count()
    #     for i in range(tabs_number):
    #         control_widget = self.controls_tab.widget(i)
    #         if control_widget.control_type == "pulse":
    #             control_widget.update_time_values(previous_time_name, new_time_name, time_value)

    def update_time_for_pulse_combobox(self):
        time_dict = {}
        # Get the time in the controls and fill a dictionary
        tabs_number = self.controls_tab.count()
        for i in range(tabs_number):
            control_widget = self.controls_tab.widget(i)
            if control_widget.control_type == "time":
                time_dict[control_widget.time_dictionary.time_name] = control_widget.time_dictionary.initial_value
        # Update the time combobox in all pulses
        for i in range(tabs_number):
            control_widget = self.controls_tab.widget(i)
            if control_widget.control_type == "pulse":
                control_widget.update_time_values(time_dict)

    def remove_control_widget(self):
        control_widget = self.controls_tab.widget(self.curr_tab_index)
        if control_widget is not None:
            control_type = control_widget.control_type
            # TODO Check if the widget is removable, i.e. if the time is connected to a pulse
            self.control_dictionary.remove_control(control_widget.control_type, control_widget.control_index)
            self.controls_tab.removeTab(self.curr_tab_index)
            # If a time control is removed then update the time combobox pulse
            if control_type == "time":
                self.update_time_for_pulse_combobox()

    def set_curr_tab_index(self, index):
        # Update the previous widget
        control_widget = self.controls_tab.widget(self.curr_tab_index)
        # Update the dictionary of the previous dictionary
        if control_widget is not None:
            self.control_dictionary.add_control(control_widget.control_type, control_widget.get_dictionary(), control_widget.control_index)
        # Set the new tab index
        self.curr_tab_index = index

    def get_dictionary(self):
        number_of_widgets = self.controls_tab.count()
        pulses_list = []
        paras_list = []
        times_list = []
        for i in range(number_of_widgets):
            control_dict = self.controls_tab.widget(i).get_dictionary()
            control_type = self.controls_tab.widget(i).control_type
            if control_type == "pulse":
                pulses_list.append(control_dict)
            elif control_type == "parameter":
                paras_list.append(control_dict)
            elif control_type == "time":
                times_list.append(control_dict)
            else:
                # TODO Thinks what to do in this case
                pass
        return {"pulses": pulses_list, "parameters": paras_list, "times": times_list}

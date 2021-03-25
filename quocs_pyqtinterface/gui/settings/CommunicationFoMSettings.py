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
from qtpy import QtWidgets

from quocs_pyqtinterface.gui.settings.AllInOneCommForm import AllInOneCommForm
from quocs_pyqtinterface.gui.settings.FilesUpdateForm import FilesUpdateForm
from quocs_pyqtinterface.gui.settings.LocalCommForm import LocalCommForm
from quocs_pyqtinterface.gui.settings.PythonClassForm import PythonClassForm
from quocs_pyqtinterface.gui.settings.RemoteCommForm import RemoteCommForm
from quocs_pyqtinterface.gui.uiclasses.CommFomSettingsUI import Ui_Form


class CommFom(QtWidgets.QWidget, Ui_Form):
    """Dialogue for the Communication - Figure of merit evaluation"""
    def __init__(self, parent=None, loaded_dictionary=None):
        super().__init__(parent)
        self.setupUi(self)
        # Communication QButtonGroup
        self.comm_button_group = QtWidgets.QButtonGroup()
        # self.comm_button_group.addButton(self.remote_radio_button)
        # self.comm_button_group.addButton(self.local_radio_button)
        self.comm_button_group.addButton(self.allinone_radio_button)
        # Not available buttons
        self.no_available_button_group = QtWidgets.QButtonGroup()
        self.no_available_button_group.addButton(self.remote_radio_button)
        self.no_available_button_group.addButton(self.local_radio_button)
        self.no_available_button_group.addButton(self.files_exchange_radio_button)
        self.no_available_button_group.setExclusive(False)
        # self.test_radio_button.setChecked(True)
        # Fom QButtonGroup
        self.fom_button_group = QtWidgets.QButtonGroup()
        self.fom_button_group.addButton(self.python_class_radio_button)
        # self.fom_button_group.addButton(self.files_exchange_radio_button)
        # Create the widget object and set it
        communication_dictionary, figure_of_merit_dictionary = None, None
        if loaded_dictionary is not None:
            communication_dictionary = loaded_dictionary[0]
            figure_of_merit_dictionary = loaded_dictionary[1]
        # Comm
        self.remote_comm_form = RemoteCommForm()
        self.local_comm_form = LocalCommForm()
        self.all_in_one_comm_form = AllInOneCommForm(loaded_dictionary=communication_dictionary)
        # Fom
        self.python_class_form = PythonClassForm(loaded_dictionary=figure_of_merit_dictionary)
        self.files_update_form = FilesUpdateForm()
        # Comm
        # self.remote_radio_button.pressed.connect(self.set_remote_widget)
        # self.local_radio_button.pressed.connect(self.set_local_widget)
        self.allinone_radio_button.pressed.connect(self.set_all_in_one_widget)
        # Fom
        self.python_class_radio_button.pressed.connect(self.set_python_class_widget)
        # self.files_exchange_radio_button.pressed.connect(self.set_files_update_widget)

        self.no_available_button_group.buttonReleased.connect(self.no_available_button_unchecked)
        # Initialization
        self._initialization()

    def _initialization(self):
        # Set initial widgets
        self.allinone_radio_button.setChecked(True)
        self.comm_scroll_area.setWidget(self.all_in_one_comm_form)
        #
        self.python_class_radio_button.setChecked(True)
        self.fom_scroll_area.setWidget(self.python_class_form)
        #
        self.comm_scroll_area.setWidgetResizable(True)

    @staticmethod
    def no_available_button_unchecked(no_available_button):
        """Just a module to disabled button action"""
        if no_available_button is not None:
            no_available_button.setChecked(False)

    def get_dictionary(self):
        communication_dict = self.comm_scroll_area.widget().get_dictionary()
        figure_of_merit_dict = self.fom_scroll_area.widget().get_dictionary()
        return {"communication": communication_dict, "figure_of_merit": figure_of_merit_dict}

    def set_remote_widget(self):
        self.comm_scroll_area.takeWidget()
        self.comm_scroll_area.setWidget(self.remote_comm_form)
        self.remote_comm_form = self.comm_scroll_area.widget()

    def set_local_widget(self):
        self.comm_scroll_area.takeWidget()
        self.comm_scroll_area.setWidget(self.local_comm_form)
        self.local_comm_form = self.comm_scroll_area.widget()

    def set_all_in_one_widget(self):
        self.comm_scroll_area.takeWidget()
        self.comm_scroll_area.setWidget(self.all_in_one_comm_form)
        self.all_in_one_comm_form = self.comm_scroll_area.widget()

    def set_python_class_widget(self):
        self.fom_scroll_area.takeWidget()
        self.fom_scroll_area.setWidget(self.python_class_form)
        self.python_class_form = self.fom_scroll_area.widget()

    def set_files_update_widget(self):
        self.fom_scroll_area.takeWidget()
        self.fom_scroll_area.setWidget(self.files_update_form)
        self.files_update_form = self.fom_scroll_area.widget()

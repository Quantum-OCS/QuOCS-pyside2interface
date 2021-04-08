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
from abc import abstractmethod

from qtpy import QtCore

from quocs_pyside2interface.logic.HandleExitBasic import HandleExitBasic as HE
# TODO !!! Put the dependency of the quocs_optlib here !!!


class OptimizationBasic:
    #####################
    # Signals
    #####################
    # Optimization status signal
    is_running_signal = QtCore.Signal(bool)
    # Update label with text
    message_label_signal = QtCore.Signal(str)
    # Fom plot
    fom_plot_signal = QtCore.Signal(int, float)
    # Pulses, time grids, parameters update
    controls_update_signal = QtCore.Signal(list, list, list)
    # Handle exit obj
    handle_exit_obj = HE()

    @QtCore.Slot(dict)
    @abstractmethod
    def start_optimization(self, **kwargs):
        """
        Main handler for the optimization. The GUI sends here the dictionary with the optimization details and the
        dictionary with the communication options. The signals are passed by reference to the Analysis steering object.
        The handle exit job checks if any errors occurs during the optimization process or a stop signal is
        emitted from the GUI.

        @param opti_comm_dict:

        """

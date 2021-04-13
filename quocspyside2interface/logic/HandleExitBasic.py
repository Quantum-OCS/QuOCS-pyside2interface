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

import logging

from qtpy import QtCore


class HandleExitBasic(QtCore.QObject):
    """This class check and update the current optimization status and notify the Client Interface and the Optimization
    code about it"""

    logger = logging.getLogger("oc_logger")

    is_user_running = True

    @QtCore.Slot(bool)
    def set_is_user_running(self, is_running: bool):
        """
        Module connected with the Client Interface GUI. Stop the communication when the user presses to the Stop button
        :param bool is_running:
        :return:
        """
        self.is_user_running = is_running

    def check_communication(self, communication: dict) -> bool:
        """
        Update the Client Interface and Optimization Code numbers and return the running status
        :param dict communication:
        :return: bool : True if it is still running, False stopped by the interface or the optimization code
        """
        if not self.is_user_running:
            return False
        # Check the communication dictionary
        server_number = communication["server_number"]
        if server_number == -1 or server_number == 4:
            self.logger.info("End of communications")
            return False
        else:
            return True

    def get_terminate_reason(self) -> str:
        """
        Get the ending reason
        :return: str : terminate reason
        """
        print("Something to write here")
        return "No idea"

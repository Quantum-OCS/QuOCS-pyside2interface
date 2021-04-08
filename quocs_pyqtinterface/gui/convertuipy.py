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

import os

ui_folder = os.path.join(os.getcwd(), "uifiles")
class_folder = os.path.join(os.getcwd(), "uiclasses")
for file in os.scandir(ui_folder):
    if file.path.endswith(".ui"):
        class_file = os.path.splitext(file)[0] + "UI.py"
        os.system("pyside2-uic {0} -o {1}".format(file.path, class_file))
        os.system("mv {0} {1}".format(class_file, class_folder))

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

from setuptools import setup, find_packages

requirements = [
    "setuptools>=44.0.0",
    "QtPy==1.9.0",
    "PyQt5==5.15.2",
    "pyqt5-tools==5.15.2.3.0.2",
    "numpy>=1.19.2",
    "scipy>=1.5.4",
    "pyqtgraph>=0.11.1",
    "PySide2>=5.15.2"
]

setup(name="quocs_pyqtinterface", packages=find_packages(), version="dev", install_requires=requirements)

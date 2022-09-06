# QuOCS-pyside2interface

A PySide2 interface for QuOCS

## Unittesting

[![Build Status](https://github.com/Quantum-OCS/QuOCS-pyside2interface/actions/workflows/unit_testing_linux.yml/badge.svg)](https://github.com/Quantum-OCS/QuOCS-pyside2interface/actions)
[![Build Status](https://github.com/Quantum-OCS/QuOCS-pyside2interface/actions/workflows/unit_testing_windows.yml/badge.svg)](https://github.com/Quantum-OCS/QuOCS-pyside2interface/actions)

## Installation

1) Download this repository as a compressed file and extract it on your computer or clone this repository via git

2) Install quocs_pyside2interface by running the following command in the main folder

~~~bash
python -m pip install -e .
~~~

3) Convert the ui files for the GUI with PySide2 and PyQt5

~~~bash
python src/quocspyside2interface/gui/convertuipy.py
python src/quocspyside2interface/gui/convertuipy_pyqt5.py
~~~
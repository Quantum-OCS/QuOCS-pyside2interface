# QuOCS-pyside2interface

A PySide2 interface for QuOCS

## Unittesting

[![Build Status](https://github.com/Quantum-OCS/QuOCS-pyside2interface/actions/workflows/unit_testing_linux.yml/badge.svg)](https://github.com/Quantum-OCS/QuOCS-pyside2interface/actions)
[![Build Status](https://github.com/Quantum-OCS/QuOCS-pyside2interface/actions/workflows/unit_testing_windows.yml/badge.svg)](https://github.com/Quantum-OCS/QuOCS-pyside2interface/actions)

## Create a virtual environment

Create a virtual environment:
```bash
python3 -m venv ../quocspyside2interface-venv
```
Activate your virtual environment:
```bash
source ../pyside2interface-venv/bin/activate
```
Install basic packages
```bash
python -m pip install --upgrade pip setuptools wheel
```
## Installation

Install quocs_pyside2interface in your virtual environment
```bash
python -m pip install -e .
```

## QtDesigner

In the Linux OS you can install the qt designer with
```bash
sudo apt install qttools5-dev-tools
```
and run the designer
```bash
designer
```
Then the convertuipy.py script will convert all the ui files in the uifiles folder in the respective python classes

## Tests

Now you are able to use the tests scripts in the tests folder
:)



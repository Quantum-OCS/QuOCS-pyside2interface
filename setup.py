from setuptools import setup, find_packages

requirements = [
    "setuptools>=44.0.0",
    "QtPy==1.9.0",
    "PyQt5==5.15.2",
    "pyqt5-tools==5.15.2.3.0.2",
    "numpy>=1.20.1",
    "scipy>=1.6.1",
    "pyqtgraph>=0.11.1",
    "PySide2>=5.15.2"
]

setup(name="quocs_pyqtinterface", packages=find_packages(), version="develop", install_requires=requirements)

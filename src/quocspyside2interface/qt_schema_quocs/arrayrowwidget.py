""" Put header here """
from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.arraycontrolswidget import ArrayControlsWidget


class ArrayRowWidget(QtWidgets.QWidget):

    def __init__(self, widget: QtWidgets.QWidget, controls: ArrayControlsWidget):
        super().__init__()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(controls)
        self.setLayout(layout)

        self.widget = widget
        self.controls = controls

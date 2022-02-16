""" Put header here """
from typing import List

from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin


class FormWidget(QtWidgets.QWidget):

    def __init__(self, widget_schema: SchemaWidgetMixin, parent=None):
        super().__init__(parent=parent)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.error_widget = QtWidgets.QGroupBox(parent=parent)
        self.error_widget.setTitle("Errors")
        self.error_layout = QtWidgets.QVBoxLayout()
        self.error_widget.setLayout(self.error_layout)
        self.error_widget.hide()

        layout.addWidget(self.error_widget)
        layout.addWidget(widget_schema.widget)

        self.widget = widget_schema.widget

    def display_errors(self, errors: List[Exception]):
        self.error_widget.show()

        layout = self.error_widget.layout()
        while True:
            item = layout.takeAt(0)
            if not item:
                break
            item.widget().deleteLater()

        for err in errors:
            widget = QtWidgets.QLabel(f"<b>.{'.'.join(err.path)}</b> {err.message}")
            layout.addWidget(widget)

    def clear_errors(self):
        self.error_widget.hide()

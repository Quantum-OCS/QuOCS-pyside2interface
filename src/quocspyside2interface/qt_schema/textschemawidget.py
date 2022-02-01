""" Put header here """
from qtpy import QtWidgets
from quocspyside2interface.qt_schema.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema.utils import state_property


class TextSchemaWidget(SchemaWidgetMixin, QtWidgets.QLineEdit):

    def configure(self):
        self.widget = self
        self.textChanged.connect(self.on_changed.emit)

    @state_property
    def state(self) -> str:
        return str(self.text())

    @state.setter
    def state(self, state: str):
        self.setText(state)

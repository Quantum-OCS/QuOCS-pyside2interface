""" Put header here """
from qtpy import QtWidgets

from quocspyside2interface.qt_schema.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema.utils import state_property


class TextAreaSchemaWidget(SchemaWidgetMixin, QtWidgets.QTextEdit):

    @property
    def state(self):
        return self._state

    @state_property
    def state(self) -> str:
        return str(self.toPlainText())

    @state.setter
    def state(self, state: str):
        self.setPlainText(state)

    def configure(self):
        self.widget = self
        self.textChanged.connect(lambda: self.on_changed.emit(self.state))

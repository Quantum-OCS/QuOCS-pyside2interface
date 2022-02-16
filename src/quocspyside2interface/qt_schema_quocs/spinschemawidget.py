""" Put header here """
from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema_quocs.utils import state_property


class SpinSchemaWidget(SchemaWidgetMixin, QtWidgets.QSpinBox):

    @state_property
    def state(self) -> int:
        return self.value()

    @state.setter
    def state(self, state: int):
        self.setValue(state)

    def configure(self):
        self.widget = self
        self.valueChanged.connect(self.on_changed.emit)

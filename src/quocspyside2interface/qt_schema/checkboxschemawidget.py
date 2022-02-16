""" Put header here """
from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema.utils import state_property


class CheckboxSchemaWidget(SchemaWidgetMixin, QtWidgets.QCheckBox):

    @property
    def state(self):
        return self._state

    @state_property
    def state(self) -> bool:
        return self.isChecked()

    @state.setter
    def state(self, checked: bool):
        self.setChecked(checked)

    def configure(self):
        self.widget = self
        self.stateChanged.connect(lambda _: self.on_changed.emit(self.state))

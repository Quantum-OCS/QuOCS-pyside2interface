""" Put header here """
from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema_quocs.utils import state_property
from quocspyside2interface.qt_schema_quocs.scientificdoublespinboxwidget import ScientificDoubleSpinBox


class ScientificSpinDoubleSchemaWidget(SchemaWidgetMixin, ScientificDoubleSpinBox):

    @state_property
    def state(self) -> float:
        return self.value()

    @state.setter
    def state(self, state: float):
        self.setValue(state)

    def configure(self):
        self.widget = self
        self.valueChanged.connect(self.on_changed.emit)

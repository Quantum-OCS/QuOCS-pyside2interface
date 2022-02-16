""" Put header here """
from qtpy import QtWidgets, QtCore

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema_quocs.utils import state_property


class IntegerRangeSchemaWidget(SchemaWidgetMixin, QtWidgets.QSlider):

    def __init__(self, schema: dict, ui_schema: dict, widget_builder: object):
        super().__init__(schema, ui_schema, widget_builder, orientation=QtCore.Qt.Horizontal)

    @state_property
    def state(self) -> int:
        return self.value()

    @state.setter
    def state(self, state: int):
        self.setValue(state)

    def configure(self):
        self.widget = self
        self.valueChanged.connect(self.on_changed.emit)

        minimum = 0
        if "minimum" in self.schema:
            minimum = self.schema["minimum"]
            if self.schema.get("exclusiveMinimum"):
                minimum += 1

        maximum = 0
        if "maximum" in self.schema:
            maximum = self.schema["maximum"]
            if self.schema.get("exclusiveMaximum"):
                maximum -= 1

        if "multipleOf" in self.schema:
            self.setTickInterval(self.schema["multipleOf"])
            self.setSingleStep(self.schema["multipleOf"])
            self.setTickPosition(self.TicksBothSides)

        self.setRange(minimum, maximum)

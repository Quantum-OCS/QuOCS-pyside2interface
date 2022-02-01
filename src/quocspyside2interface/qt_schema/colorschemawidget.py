""" Put header here """
from quocspyside2interface.qt_schema.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema.qcolorbutton import QColorButton
from quocspyside2interface.qt_schema.utils import state_property


class ColorSchemaWidget(SchemaWidgetMixin, QColorButton):
    """Widget representation of a string with the 'color' format keyword."""

    @property
    def state(self):
        return self._state

    def configure(self):
        self.widget = self
        self.colorChanged.connect(lambda: self.on_changed.emit(self.state))

    @state_property
    def state(self) -> str:
        return self.color()

    @state.setter
    def state(self, data: str):
        self.setColor(data)

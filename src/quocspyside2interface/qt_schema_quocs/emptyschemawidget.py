""" Put header here """
from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema_quocs.utils import state_property


class EmptySchemaWidget(SchemaWidgetMixin, QtWidgets.QScrollArea):

    def __init__(self, schema: dict, ui_schema: dict, widget_builder: object, **kwargs):
        super().__init__(schema, ui_schema, widget_builder, **kwargs)

    @property
    def state(self):
        return self._state

    @state_property
    def state(self) -> dict:
        return {}

    @state.setter
    def state(self, data_dict: bool):
        pass

    def configure(self):
        self.widget = self

""" Put header here """
from functools import partial
from typing import Tuple, Dict

from qtpy import QtWidgets, QtCore

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema_quocs.utils import state_property


class ObjectSchemaWidget(SchemaWidgetMixin, QtWidgets.QGroupBox):

    def __init__(self, schema: dict,
                 ui_schema: dict,
                 widget_builder: object,
                 parent: object = None):
        super().__init__(schema=schema,
                         ui_schema=ui_schema,
                         widget_builder=widget_builder)
        self.parent = parent
        self.widgets = self.populate_from_schema(schema, ui_schema, widget_builder)

    @property
    def state(self):
        return self._state

    @state_property
    def state(self) -> dict:
        return {k: w.state for k, w in self.widgets.items()}

    def configure(self):
        self.widget = self

    @state.setter
    def state(self, state: dict):
        for name, value in state.items():
            self.widgets[name].state = value

    def handle_error(self, path: Tuple[str], err: Exception):
        name, *tail = path
        self.widgets[name].handle_error(tail, err)

    def widget_on_changed(self, name: str, value):
        self.state[name] = value
        self.on_changed.emit(self.state)

    def populate_from_schema(self, schema: dict,
                             ui_schema: dict,
                             widget_builder: object) -> Dict[str, QtWidgets.QWidget]:
        layout = QtWidgets.QFormLayout(parent=self.parent)
        self.setLayout(layout)
        layout.setAlignment(QtCore.Qt.AlignTop)
        self.setFlat(False)

        if 'title' in schema:
            self.setTitle(schema['title'])

        if 'description' in schema:
            self.setToolTip(schema['description'])

        # Populate rows
        widgets = {}

        # Loop over all the sub schema in the schema widget

        for name, sub_schema in schema['properties'].items():
            sub_ui_schema = ui_schema.get(name, {})
            widget = widget_builder.create_widget(schema=sub_schema,
                                                  ui_schema=sub_ui_schema)
            # TODO Change widgets when json schema change?
            widget.on_changed.connect(partial(self.widget_on_changed, name))
            label = sub_schema.get("title", name)
            layout.addRow(label, widget)
            widgets[name] = widget

        return widgets

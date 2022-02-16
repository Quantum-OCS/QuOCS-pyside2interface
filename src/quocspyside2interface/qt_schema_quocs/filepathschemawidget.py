""" Put header here """

from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema_quocs.utils import state_property


class FilepathSchemaWidget(SchemaWidgetMixin, QtWidgets.QWidget):

    def __init__(self, schema: dict, ui_schema: dict, widget_builder: object):
        super().__init__(schema, ui_schema, widget_builder)

        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)

        self.path_widget = QtWidgets.QLineEdit()
        self.button_widget = QtWidgets.QPushButton("Browse")
        layout.addWidget(self.path_widget)
        layout.addWidget(self.button_widget)

        self.button_widget.clicked.connect(self._on_clicked)
        self.path_widget.textChanged.connect(self.on_changed.emit)

    def _on_clicked(self, flag):
        path, filter = QtWidgets.QFileDialog.getOpenFileName()
        self.path_widget.setText(path)

    @state_property
    def state(self) -> str:
        return self.path_widget.text()

    @state.setter
    def state(self, state: str):
        self.path_widget.setText(state)

    def configure(self):
        self.widget = self

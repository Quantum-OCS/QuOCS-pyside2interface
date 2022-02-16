""" Put header here """
from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema_quocs.utils import state_property


class EnumSchemaWidget(SchemaWidgetMixin, QtWidgets.QComboBox):

    @property
    def state(self):
        return self._state

    @state_property
    def state(self):
        return self.itemData(self.currentIndex())

    @state.setter
    def state(self, value):
        index = self.findData(value)
        if index == -1:
            raise ValueError(value)
        self.setCurrentIndex(index)

    def configure(self):
        self.widget = self
        options = self.schema["enum"]
        for i, opt in enumerate(options):
            self.addItem(str(opt))
            self.setItemData(i, opt)

        self.currentIndexChanged.connect(lambda _: self.on_changed.emit(self.state))

    def _index_changed(self, index: int):
        self.on_changed.emit(self.state)

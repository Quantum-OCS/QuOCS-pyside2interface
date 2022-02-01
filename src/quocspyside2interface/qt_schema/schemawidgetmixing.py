""" Put here header """
from typing import Tuple

from qtpy import QtWidgets, QtGui

from quocspyside2interface.qt_schema.signal import Signal
from quocspyside2interface.qt_schema.utils import iter_layout_widgets, state_property, is_concrete_schema


class SchemaWidgetMixin:

    on_changed = Signal()

    VALID_COLOUR = '#ffffff'
    INVALID_COLOUR = '#f6989d'

    widget: QtWidgets.QWidget

    def __init__(self, schema: dict, ui_schema: dict, widget_builder: object, **kwargs):
        super().__init__(**kwargs)

        self.schema = schema
        self.ui_schema = ui_schema
        self.widget_builder = widget_builder

        self.on_changed.connect(lambda _: self.clear_error())
        self.configure()

    def configure(self):
        """ Set the palette and the background """

    @state_property
    def state(self):
        raise NotImplementedError(f"{self.__class__.__name__}.state")

    @state.setter
    def state(self, state):
        raise NotImplementedError(f"{self.__class__.__name__}.state")

    def handle_error(self, path: Tuple[str], err: Exception):
        if path:
            raise ValueError("Cannot handle nested error by default")
        self._set_valid_state(err)

    def clear_error(self):
        self._set_valid_state(None)

    def _set_valid_state(self, error: Exception = None):
        palette = self.widget.palette()
        colour = QtGui.QColor()
        colour.setNamedColor(self.VALID_COLOUR if error is None else self.INVALID_COLOUR)
        palette.setColor(self.widget.backgroundRole(), colour)

        self.widget.setPalette(palette)
        # self.setToolTip("" if error is None else error.message)  # TODO

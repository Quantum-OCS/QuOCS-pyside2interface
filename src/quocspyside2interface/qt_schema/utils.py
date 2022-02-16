from functools import wraps
from typing import Iterator

from qtpy import QtWidgets
from quocspyside2interface.qt_schema_quocs.baseform import BaseForm


class StateProperty(property):

    def setter(self, fset: object) -> object:
        @wraps(fset)
        def _setter(*args):
            *head, value = args
            if value is not None:
                fset(*head, value)

        return super().setter(_setter)


state_property = StateProperty


def reject_none(func):
    """Only invoke function if state argument is not None"""

    @wraps(func)
    def wrapper(self, state):
        if state is None:
            return
        func(self, state)

    return wrapper


def is_concrete_schema(schema: dict) -> bool:
    return "type" in schema


def iter_layout_items(layout) -> Iterator[QtWidgets.QLayoutItem]:
    return (layout.itemAt(i) for i in range(layout.count()))


def iter_layout_widgets(layout: QtWidgets.QLayout) -> Iterator[QtWidgets.QWidget]:
    return (i.widget() for i in iter_layout_items(layout))


def update_internal_widget(new_widget: QtWidgets.QWidget, old_widget: QtWidgets.QWidget) -> QtWidgets.QWidget:
    """ Move the distribution widget inside the Fourier Basis widget"""
    old_widget.takeWidget()
    old_widget.setWidget(new_widget)
    new_widget = old_widget
    return new_widget


def update_error_functions(schema_obj: BaseForm,
                           validate_func: callable, error_func: callable, remove_error: callable):
    """ """
    # Disconnect the old validation and connect the signal to the new one
    schema_obj.widget_schema.on_changed.disconnect()
    schema_obj.widget_schema.on_changed.connect(validate_func)
    # Update the external error functions
    schema_obj.external_errors = error_func
    schema_obj.remove_error = remove_error

""" Test class for uniform distribution schema """

from qtpy import QtWidgets

from quocspyside2interface.logic.utilities.readjson import readjson
from quocspyside2interface.qt_schema_quocs.baseform import BaseForm

schema = readjson("uniform_distribution.json")[1]
# ui schema
ui_schema = readjson("ui_schema_uniform_distribution.json")[1]
# initial state
state_schema = readjson("state_uniform_distribution.json")[1]


class QError:
    path = ("lower_limit",)
    message = "Ciao"
    validation_origin = "lower_limit"


class UniformDistribution(QtWidgets.QWidget,
                          BaseForm):
    external_errors_func: callable

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        # Setup all the widgets
        self.setupUi(Form=parent, schema=schema, ui_schema=ui_schema, state_schema=state_schema)

        # Connections
        self.widget_schema.widget.widgets["lower_limit"].valueChanged.connect(self.test_function)

    def test_function(self, value: float):
        print("Value: {0}".format(value))
        if value > 2.0:
            self.external_errors(errors=[QError],
                                 validation_origin="lower_limit",
                                 widget_schema=self.widget_schema)

""" Test class for uniform distribution schema """

from qtpy import QtWidgets

from quocspyside2interface.logic.utilities.readjson import readjson
from quocspyside2interface.qt_schema_quocs.baseform import BaseForm

import os

# json schema
schema = readjson(os.path.join(os.path.dirname(__file__), "uniform_distribution.json"))[1]
# ui schema
ui_schema = readjson(os.path.join(os.path.dirname(__file__), "ui_schema_uniform_distribution.json"))[1]
# initial state
state_schema = readjson(os.path.join(os.path.dirname(__file__), "state_uniform_distribution.json"))[1]


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
        self.uniform_dict = state_schema
        # Connections
        self.widget_schema.widget.widgets["lower_limit"].valueChanged.connect(self.test_function)

    def update_dictionary(self, data):
        self.uniform_dict = data

    def test_function(self, value: float):
        print("Value: {0}".format(value))
        if value > 2.0:
            self.external_errors(errors=[QError],
                                 validation_origin="lower_limit",
                                 widget_schema=self.widget_schema)

    def get_dictionary(self):
        return self.uniform_dict

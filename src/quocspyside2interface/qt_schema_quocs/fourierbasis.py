""" Test class for uniform distribution schema """

from qtpy import QtWidgets

from quocspyside2interface.logic.utilities.readjson import readjson
from quocspyside2interface.qt_schema_quocs.baseform import BaseForm
from quocspyside2interface.qt_schema_quocs.uniformdistribution import UniformDistribution

from quocspyside2interface.qt_schema_quocs.utils import update_internal_widget, update_error_functions

# json schema
schema = readjson("fourier_basis.json")[1]
# ui schema
ui_schema = readjson("ui_schema_fourier_basis.json")[1]
# initial state
state_schema = readjson("state_fourier_basis.json")[1]


class QError:
    path = ("basisVectorNumber",)
    message = "Ciao"
    validation_origin = "basisVectorNumber"


class FourierBasis(QtWidgets.QWidget,
                   BaseForm):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        # Setup all the widgets
        self.setupUi(Form=parent, schema=schema, ui_schema=ui_schema, state_schema=state_schema)
        # Widgets
        self.widgets = self.widget_schema.widget.widgets

        # Load here the Uniform distribution widget
        self.uniform_distribution_obj = UniformDistribution()

        # Update the widget contained in the Fourier basis form
        self.uniform_distribution_obj.widget_schema.widget = \
            update_internal_widget(new_widget=self.uniform_distribution_obj.widget_schema.widget,
                                   old_widget=self.widgets["distributionArea"])
        # Update the error functions
        update_error_functions(schema_obj=self.uniform_distribution_obj,
                               validate_func=self.validate,
                               error_func=self.external_errors,
                               remove_error=self.remove_error)

        # Connections
        self.widgets["basisVectorNumber"].valueChanged.connect(self.test_function)

    def test_function(self, value: int):
        # To prevent double click
        self.widgets["basisVectorNumber"].setEnabled(False)
        print("Value: {0}".format(value))
        if value > 3:
            self.external_errors(errors=[QError], validation_origin="basisVectorNumber")
        self.widgets["basisVectorNumber"].setEnabled(True)

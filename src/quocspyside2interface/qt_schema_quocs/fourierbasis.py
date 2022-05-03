""" Test class for uniform distribution schema """

from qtpy import QtWidgets
from quocspyside2interface.logic.utilities.utils import load_dictionary, combine_dict

from quocspyside2interface.logic.pulses.basis.FourierBasisDictionary import FourierBasisDictionary
from quocspyside2interface.logic.utilities.readjson import readjson
from quocspyside2interface.qt_schema_quocs.baseform import BaseForm
from quocspyside2interface.qt_schema_quocs.uniformdistribution import UniformDistribution

from quocspyside2interface.qt_schema_quocs.utils import update_internal_widget, update_error_functions

import os

# json schema
schema = readjson(os.path.join(os.path.dirname(__file__), "fourier_basis.json"))[1]
# ui schema
ui_schema = readjson(os.path.join(os.path.dirname(__file__), "ui_schema_fourier_basis.json"))[1]
# initial state
state_schema = readjson(os.path.join(os.path.dirname(__file__), "state_fourier_basis.json"))[1]


class QError(BaseException):
    path = ("basis_vector_number",)
    message = "Ciao"
    validation_origin = "basisVectorNumber"


class FourierBasis(QtWidgets.QWidget,
                   BaseForm):

    def __init__(self, loaded_dictionary, parent=None, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        # Create the initial dictionary as a union of the old dictionary and
        initial_dictionary = combine_dict(state_schema, loaded_dictionary)
        # Setup all the widgets
        self.setupUi(Form=self, schema=schema, ui_schema=ui_schema, state_schema=initial_dictionary)
        # Widgets
        self.widgets = self.widget_schema.widget.widgets
        # Fourier dictionary
        # self.fourier_dict = state_schema
        self.basis_dictionary = FourierBasisDictionary(loaded_dictionary=initial_dictionary)

        self.form_name = "Fourier Basis"

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
        self.widgets["basis_vector_number"].valueChanged.connect(self.set_basis_vector_number)

        # Get the data every time the widget change
        self.widget_schema.on_changed.connect(self.update_dictionary)

    def set_basis_vector_number(self, value: int):
        """ Set the basis vector number """
        # To prevent double click
        self.widgets["basis_vector_number"].setEnabled(False)
        print("Value: {0}".format(value))
        if value > 10:
            QError.message = "Basis vector number cannot be grater than 10"
            self.external_errors(errors=[QError], validation_origin="basisVectorNumber")
        self.widgets["basis_vector_number"].setEnabled(True)

    def update_dictionary(self, data: dict):
        """ Update the dictionary of the Fourier basis """
        self.basis_dictionary.update_dictionary(data)

    def get_dictionary(self):
        """ Get all the data from the current widget """
        uniform_dict = self.uniform_distribution_obj.get_dictionary()
        self.basis_dictionary.update_dictionary({"random_super_parameter_distribution": uniform_dict})
        return self.basis_dictionary.get_dictionary()

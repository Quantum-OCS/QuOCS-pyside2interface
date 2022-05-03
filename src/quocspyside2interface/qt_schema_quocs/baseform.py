""" Put header here """
from typing import Dict, List

from qtpy import QtWidgets

from quocspyside2interface.qt_schema_quocs.errorwidget import ErrorWidget
from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema_quocs.widgetbuilder import WidgetBuilder


class BaseForm:
    formLayout: QtWidgets.QFormLayout
    error_widget: QtWidgets.QWidget
    widget_layout: QtWidgets.QVBoxLayout
    widget_schema:  SchemaWidgetMixin
    widget_builder_obj: WidgetBuilder
    validator: None
    error_plain_text: QtWidgets.QPlainTextEdit
    form_name: str

    def setupUi(self, Form: QtWidgets.QWidget = None,
                schema: Dict = None,
                ui_schema: Dict = None,
                state_schema: Dict = None):
        """ Setup Ui """
        # Create the form layout
        self.formLayout = QtWidgets.QFormLayout(parent=Form)
        ################################################################################################################
        # Error Widget
        ################################################################################################################
        self.error_widget = QtWidgets.QWidget(parent=Form)
        error_widget_layout = QtWidgets.QHBoxLayout()
        self.error_plain_text = ErrorWidget()
        self.error_widget.setLayout(error_widget_layout)
        error_widget_layout.addWidget(self.error_plain_text)

        self.error_widget.hide()
        ################################################################################################################
        # Load json schema
        ################################################################################################################
        # Create the widget schema
        self.widget_builder_obj = WidgetBuilder()
        self.widget_schema = self.widget_builder_obj.create_widget(schema=schema,
                                                                   ui_schema=ui_schema,
                                                                   state=state_schema)
        self.widget_layout = QtWidgets.QVBoxLayout()
        self.widget_schema.widget.setLayout(self.widget_layout)
        # Validation the data function
        self.validator = self.widget_builder_obj.create_validator(schema=schema)
        ################################################################################################################
        # Add widgets to the main layout
        ################################################################################################################
        self.formLayout.addWidget(self.error_widget)
        self.formLayout.addWidget(self.widget_schema.widget)
        ################################################################################################################
        # Validation of json schema and external constraints at any change
        ################################################################################################################
        # Every time the data change, check with the validate function
        self.widget_schema.on_changed.connect(self.validate)
        # Every time the data change, remove the old errors in that schema
        widgets = self.widget_schema.widget.widgets
        for widget_name in widgets:
            widgets[widget_name].on_changed.connect(
                lambda data, name=widget_name:
                self.remove_error(name))

    def remove_error(self, name: str = ""):
        """ Remove previous error in the error widget """
        self.error_plain_text.removeError(name)
        # Update the plain text in the widget
        self.error_plain_text.set_text()
        if not self.error_plain_text.error_dict:
            self.clear_errors()

    def validate(self, data):
        errors = [*self.validator.iter_errors(data)]
        # Clear old errors for the widget schema
        for err in errors:
            self.error_plain_text.removeError(err.path[0])
        # Check if errors coming from other schema are still present
        if not self.error_plain_text.error_dict or errors:
            self.clear_errors()
        # Load the new errors and show in the error widget
        if errors:
            self.display_errors(errors)
        # Update the plain text in the widget
        self.error_plain_text.set_text()
        # Handle the errors
        for err in errors:
            self.widget_schema.handle_error(err.path, err)

    def external_errors(self, errors: List[Exception],
                        validation_origin: str = None,
                        widget_schema: SchemaWidgetMixin = None):
        """ Display errors coming from external constraints """
        # Remove the error if any for the validation origin
        self.error_plain_text.removeError(validation_origin)
        if not self.error_plain_text.error_dict or errors:
            self.clear_errors()
        # Display the errors if any
        if errors:
            self.display_errors(errors=errors)
        # Update the widget color
        if widget_schema is None:
            widget_schema = self.widget_schema
        for err in errors:
            widget_schema.handle_error(err.path, err)
        # Update the plain text in the widget
        self.error_plain_text.set_text()

    def display_errors(self, errors: List[Exception]):
        """ Display the errors in the plain text """
        self.error_widget.show()
        # Populate the error widget layout with the errors encountered during the validation checking
        for err in errors:
            self.error_plain_text.addError(widget_error=err.path[0],
                                           exception_obj=err)

    def clear_errors(self):
        """ Clean the errors in the widget """
        self.error_widget.hide()

    def update_dictionary(self, data):
        """ Update the dictionary at every form update """
        raise ImportError("Implement the update dictionary in the {0} class".format(self.form_name))

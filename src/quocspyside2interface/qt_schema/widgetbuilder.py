""" Put header here """
from copy import deepcopy

from jsonschema.validators import validator_for

from quocspyside2interface.qt_schema_quocs.schemawidgetmixing import SchemaWidgetMixin
from quocspyside2interface.qt_schema.arrayschemawidget import ArraySchemaWidget
from quocspyside2interface.qt_schema.checkboxschemawidget import CheckboxSchemaWidget
from quocspyside2interface.qt_schema.colorschemawidget import ColorSchemaWidget
from quocspyside2interface.qt_schema.enumschemawidget import EnumSchemaWidget
from quocspyside2interface.qt_schema.filepathschemawidget import FilepathSchemaWidget
from quocspyside2interface.qt_schema.form import get_schema_type, get_widget_state
from quocspyside2interface.qt_schema.formwidget import FormWidget
from quocspyside2interface.qt_schema.integerrangeschemawidget import IntegerRangeSchemaWidget
from quocspyside2interface.qt_schema.objectschemawidget import ObjectSchemaWidget
from quocspyside2interface.qt_schema.passwordwidget import PasswordWidget
from quocspyside2interface.qt_schema.spindoubleschemawidget import SpinDoubleSchemaWidget
from quocspyside2interface.qt_schema.spinschemawidget import SpinSchemaWidget
from quocspyside2interface.qt_schema.textareaschemawidget import TextAreaSchemaWidget
from quocspyside2interface.qt_schema.textschemawidget import TextSchemaWidget
from quocspyside2interface.qt_schema.scientificdoublespinboxschemawidget import ScientificSpinDoubleSchemaWidget


class WidgetBuilder:
    """ This class build all the widgets defined in the json schema """
    # Default mapping between the key in the json schema and the widget schema
    default_widget_map = {
        "boolean": {"checkbox": CheckboxSchemaWidget, "enum": EnumSchemaWidget},
        "object": {"object": ObjectSchemaWidget, "enum": EnumSchemaWidget},
        "number": {"spin": SpinDoubleSchemaWidget, "text": TextSchemaWidget, "enum": EnumSchemaWidget,
                   "scientific": ScientificSpinDoubleSchemaWidget},
        "string": {"textarea": TextAreaSchemaWidget, "text": TextSchemaWidget, "password": PasswordWidget,
                   "filepath": FilepathSchemaWidget, "colour": ColorSchemaWidget, "enum": EnumSchemaWidget},
        "integer": {"spin": SpinSchemaWidget, "text": TextSchemaWidget, "range": IntegerRangeSchemaWidget,
                    "enum": EnumSchemaWidget},
        "array": {"array": ArraySchemaWidget, "enum": EnumSchemaWidget}
    }
    # Default values in case any keys are not present inside the dictionary
    default_widget_variants = {
        "boolean": "checkbox",
        "object": "object",
        "array": "array",
        "number": "spin",
        "integer": "spin",
        "string": "text"
    }
    # I do not know what happens here
    widget_variant_modifiers = {
        "string": lambda schema: schema.get("format", "text")
    }

    def __init__(self, validator_cls=None):
        # Copy the map into a variable to be re-used later
        self.widget_map = deepcopy(self.default_widget_map)
        # Save the validator
        self.validator_cls = validator_cls

    def create_form(self, schema: dict, ui_schema: dict, state=None) -> FormWidget:
        validator_cls = self.validator_cls
        if validator_cls is None:
            validator_cls = validator_for(schema)

        validator_cls.check_schema(schema)
        validator = validator_cls(schema)
        # Loop over all the  widget inside the  form
        schema_widget = self.create_widget(schema, ui_schema, state)
        # Create the form
        form = FormWidget(schema_widget)

        # Validate the data function
        def validate(data):
            form.clear_errors()
            errors = [*validator.iter_errors(data)]

            if errors:
                form.display_errors(errors)

            for err in errors:
                schema_widget.handle_error(err.path, err)

        # Every time the data change, check with the validate function
        schema_widget.on_changed.connect(validate)

        return form

    def create_widget(self, schema: dict, ui_schema: dict, state=None) -> SchemaWidgetMixin:
        schema_type = get_schema_type(schema)

        # Check if the schema type belongs to widget variants, and they are applicable
        try:
            default_variant = self.widget_variant_modifiers[schema_type](schema)
        except KeyError:
            default_variant = self.default_widget_variants[schema_type]

        if "enum" in schema:
            default_variant = "enum"

        widget_variant = ui_schema.get('ui:widget', default_variant)
        widget_cls = self.widget_map[schema_type][widget_variant]

        widget = widget_cls(schema, ui_schema, self)

        default_state = get_widget_state(schema, state)
        if default_state is not None:
            widget.state = default_state
        return widget

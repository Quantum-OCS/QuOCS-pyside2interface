""" Put header here """
from quocspyside2interface.qt_schema_quocs.textschemawidget import TextSchemaWidget


class PasswordWidget(TextSchemaWidget):

    def configure(self):
        super().configure()

        self.setEchoMode(self.Password)


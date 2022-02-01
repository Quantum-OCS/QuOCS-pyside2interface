""" Put header here """
from quocspyside2interface.qt_schema.textschemawidget import TextSchemaWidget


class PasswordWidget(TextSchemaWidget):

    def configure(self):
        super().configure()

        self.setEchoMode(self.Password)


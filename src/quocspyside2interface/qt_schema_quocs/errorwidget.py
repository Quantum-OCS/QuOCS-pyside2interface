""" Class for the error widget """

from qtpy import QtWidgets
from qtpy import QtCore


class ErrorWidget(QtWidgets.QPlainTextEdit):
    validation_origin: str
    validation_error_object: Exception

    def __init__(self, text: str = "Test", validation_origin: str = "Test", exception_obj: Exception = None,
                 parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.error_dict = {}
        # self.validation_origin = validation_origin
        # if exception_obj is not None:
        #     # self.setText(f"<b>.{'.'.join(exception_obj.path)}</b> {exception_obj.message}")
        #     self.setText("Three random words: \n {0} \n {1} \n {2}".format("a", "b", "c"))
        # else:
        #     self.setText(text)
        # self.setAlignment(QtCore.Qt.AlignBottom)
        self.setReadOnly(True)

    def set_text(self):
        error_message = ""
        for widget_error in self.error_dict:
            # TODO Set the widget name as bold
            # error_message += f"<b>.{'.'.join(widget_error)}</b>: {self.error_dict[widget_error]}"
            error_message += f"{widget_error}: {self.error_dict[widget_error]} \n"
        self.setPlainText(error_message)

    def addError(self, widget_error: str, exception_obj: Exception = None):
        """ Add error """
        # if widget_error in self.error_dict:
        #     self.error_dict[widget_error] = exception_obj
        self.error_dict[widget_error] = exception_obj.message

    def removeError(self, widget_error: str):
        """ Remove a particular key in the dictionary """
        if widget_error in self.error_dict:
            self.error_dict.pop(widget_error)

    def getErrors(self) -> dict:
        """ Return the error dictionary """
        return self.error_dict




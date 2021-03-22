

class DropOutSummary(QtWidgets.QDialog, Ui_Form):
    """Drop out dialogue for the summary"""
    def __init__(self, close_signal, summary_list, parent=None):
        # Get the path to the *.ui file
        # ui_file=os.path.join(os.getcwd(), GuiConstants.GUI_PATH, "DropOutSummary.ui")
        # Load it
        super().__init__(parent)
        # uic.loadUi(ui_file, self)
        self.setupUi(self)
        self.close_signal = close_signal
        self.summary_edit_line.setReadOnly(True)
        self.update_summary(summary_list)

    def update_summary(self, summary_list):
        self.summary_edit_line.setPlainText("")
        for element in summary_list:
            self.summary_edit_line.appendPlainText(element)

    def closeEvent(self, event):
        # Send a signal to the main window to delete the object
        self.close_signal.emit()
        # Close the window
        event.accept()
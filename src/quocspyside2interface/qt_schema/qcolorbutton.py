""" Put header here """
from qtpy import QtWidgets, QtCore, QtGui


class QColorButton(QtWidgets.QPushButton):
    """Color picker widget QPushButton subclass.

    Implementation derived from https://martinfitzpatrick.name/article/qcolorbutton-a-color-selector-tool-for-pyqt/
    """

    colorChanged = QtCore.Signal()

    def __init__(self, *args, **kwargs):
        super(QColorButton, self).__init__(*args, **kwargs)

        self._color = None
        self.pressed.connect(self.onColorPicker)

    def color(self):
        return self._color

    def setColor(self, color):
        if color != self._color:
            self._color = color
            self.colorChanged.emit()

        if self._color:
            self.setStyleSheet("background-color: %s;" % self._color)
        else:
            self.setStyleSheet("")

    def onColorPicker(self):
        dlg = QtWidgets.QColorDialog(self)
        if self._color:
            dlg.setCurrentColor(QtGui.QColor(self._color))

        if dlg.exec_():
            self.setColor(dlg.currentColor().name())

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.setColor(None)

        return super(QColorButton, self).mousePressEvent(event)

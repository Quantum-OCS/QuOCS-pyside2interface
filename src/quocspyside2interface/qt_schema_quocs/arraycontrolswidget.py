""" Put header here """
from qtpy import QtWidgets, QtCore


class ArrayControlsWidget(QtWidgets.QWidget):
    on_delete = QtCore.Signal()
    on_move_up = QtCore.Signal()
    on_move_down = QtCore.Signal()

    def __init__(self):
        super().__init__()

        style = self.style()

        self.up_button = QtWidgets.QPushButton()
        self.up_button.setIcon(style.standardIcon(QtWidgets.QStyle.SP_ArrowUp))
        self.up_button.clicked.connect(lambda _: self.on_move_up.emit())

        self.delete_button = QtWidgets.QPushButton()
        self.delete_button.setIcon(style.standardIcon(QtWidgets.QStyle.SP_DialogCancelButton))
        self.delete_button.clicked.connect(lambda _: self.on_delete.emit())

        self.down_button = QtWidgets.QPushButton()
        self.down_button.setIcon(style.standardIcon(QtWidgets.QStyle.SP_ArrowDown))
        self.down_button.clicked.connect(lambda _: self.on_move_down.emit())

        group_layout = QtWidgets.QHBoxLayout()
        self.setLayout(group_layout)
        group_layout.addWidget(self.up_button)
        group_layout.addWidget(self.down_button)
        group_layout.addWidget(self.delete_button)
        group_layout.setSpacing(0)
        group_layout.addStretch(0)

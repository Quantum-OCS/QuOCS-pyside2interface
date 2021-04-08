# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AllInOneCommunication.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(745, 43)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.results_folder_edit_line = QLineEdit(Form)
        self.results_folder_edit_line.setObjectName(u"results_folder_edit_line")

        self.horizontalLayout.addWidget(self.results_folder_edit_line)

        self.get_results_folder_button = QPushButton(Form)
        self.get_results_folder_button.setObjectName(u"get_results_folder_button")

        self.horizontalLayout.addWidget(self.get_results_folder_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Results Folder", None))
        self.get_results_folder_button.setText(QCoreApplication.translate("Form", u"Get Folder", None))
    # retranslateUi


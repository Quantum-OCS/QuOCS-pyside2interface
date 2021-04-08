# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PythonEvaluation.ui'
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
        Form.resize(677, 493)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.module_edit_line = QLineEdit(Form)
        self.module_edit_line.setObjectName(u"module_edit_line")

        self.horizontalLayout.addWidget(self.module_edit_line)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.class_edit_line = QLineEdit(Form)
        self.class_edit_line.setObjectName(u"class_edit_line")

        self.horizontalLayout_2.addWidget(self.class_edit_line)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.check_import_button = QPushButton(Form)
        self.check_import_button.setObjectName(u"check_import_button")

        self.horizontalLayout_4.addWidget(self.check_import_button)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.add_argument_button = QPushButton(Form)
        self.add_argument_button.setObjectName(u"add_argument_button")

        self.horizontalLayout_3.addWidget(self.add_argument_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.delete_argument_button = QPushButton(Form)
        self.delete_argument_button.setObjectName(u"delete_argument_button")

        self.horizontalLayout_3.addWidget(self.delete_argument_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.arguments_tab = QTabWidget(Form)
        self.arguments_tab.setObjectName(u"arguments_tab")

        self.verticalLayout.addWidget(self.arguments_tab)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Python Module", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Python Class", None))
        self.check_import_button.setText(QCoreApplication.translate("Form", u"Check Import", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Further arguments", None))
        self.add_argument_button.setText(QCoreApplication.translate("Form", u"Add argument", None))
        self.delete_argument_button.setText(QCoreApplication.translate("Form", u"Delete Argument", None))
    # retranslateUi


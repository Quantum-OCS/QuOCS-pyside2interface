# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoteConnection.ui'
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
        Form.resize(805, 136)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.credential_file_edit_line = QLineEdit(Form)
        self.credential_file_edit_line.setObjectName(u"credential_file_edit_line")

        self.horizontalLayout.addWidget(self.credential_file_edit_line)

        self.get_credential_file_button = QPushButton(Form)
        self.get_credential_file_button.setObjectName(u"get_credential_file_button")

        self.horizontalLayout.addWidget(self.get_credential_file_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.check_connection_button = QPushButton(Form)
        self.check_connection_button.setObjectName(u"check_connection_button")

        self.horizontalLayout_3.addWidget(self.check_connection_button)

        self.status_edit_line = QLineEdit(Form)
        self.status_edit_line.setObjectName(u"status_edit_line")

        self.horizontalLayout_3.addWidget(self.status_edit_line)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.shared_folder_edit_line = QLineEdit(Form)
        self.shared_folder_edit_line.setObjectName(u"shared_folder_edit_line")

        self.horizontalLayout_2.addWidget(self.shared_folder_edit_line)

        self.get_shared_folder_button = QPushButton(Form)
        self.get_shared_folder_button.setObjectName(u"get_shared_folder_button")

        self.horizontalLayout_2.addWidget(self.get_shared_folder_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.results_folder_eddit_line = QLineEdit(Form)
        self.results_folder_eddit_line.setObjectName(u"results_folder_eddit_line")

        self.horizontalLayout_4.addWidget(self.results_folder_eddit_line)

        self.get_results_folder_button = QPushButton(Form)
        self.get_results_folder_button.setObjectName(u"get_results_folder_button")

        self.horizontalLayout_4.addWidget(self.get_results_folder_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Credentials File", None))
        self.get_credential_file_button.setText(QCoreApplication.translate("Form", u"Get File", None))
        self.check_connection_button.setText(QCoreApplication.translate("Form", u"Check Connection", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Shared Folder", None))
        self.get_shared_folder_button.setText(QCoreApplication.translate("Form", u"Get Folder", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Results Folder", None))
        self.get_results_folder_button.setText(QCoreApplication.translate("Form", u"Get Folder", None))
    # retranslateUi


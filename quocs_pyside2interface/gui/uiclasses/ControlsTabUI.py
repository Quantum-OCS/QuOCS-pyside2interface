# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControlsTab.ui'
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
        Form.resize(1309, 795)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.controls_tab = QTabWidget(Form)
        self.controls_tab.setObjectName(u"controls_tab")

        self.verticalLayout.addWidget(self.controls_tab)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_pulse_button = QPushButton(Form)
        self.add_pulse_button.setObjectName(u"add_pulse_button")

        self.horizontalLayout.addWidget(self.add_pulse_button)

        self.add_parameter_button = QPushButton(Form)
        self.add_parameter_button.setObjectName(u"add_parameter_button")

        self.horizontalLayout.addWidget(self.add_parameter_button)

        self.add_time_button = QPushButton(Form)
        self.add_time_button.setObjectName(u"add_time_button")

        self.horizontalLayout.addWidget(self.add_time_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.remove_control_button = QPushButton(Form)
        self.remove_control_button.setObjectName(u"remove_control_button")

        self.horizontalLayout.addWidget(self.remove_control_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.add_pulse_button.setText(QCoreApplication.translate("Form", u"Add Pulse", None))
        self.add_parameter_button.setText(QCoreApplication.translate("Form", u"Add Parameter", None))
        self.add_time_button.setText(QCoreApplication.translate("Form", u"Add Time", None))
        self.remove_control_button.setText(QCoreApplication.translate("Form", u"Remove control", None))
    # retranslateUi


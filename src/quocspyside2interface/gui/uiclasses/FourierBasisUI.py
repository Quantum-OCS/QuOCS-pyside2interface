# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FourierBasis.ui'
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
        Form.resize(901, 229)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(901, 100))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.basis_vector_number_spinbox = QSpinBox(Form)
        self.basis_vector_number_spinbox.setObjectName(u"basis_vector_number_spinbox")

        self.horizontalLayout.addWidget(self.basis_vector_number_spinbox)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.freq_distribution_combobox = QComboBox(Form)
        self.freq_distribution_combobox.setObjectName(u"freq_distribution_combobox")

        self.horizontalLayout.addWidget(self.freq_distribution_combobox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.super_parameter_setting_area = QScrollArea(Form)
        self.super_parameter_setting_area.setObjectName(u"super_parameter_setting_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.super_parameter_setting_area.sizePolicy().hasHeightForWidth())
        self.super_parameter_setting_area.setSizePolicy(sizePolicy1)
        self.super_parameter_setting_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 881, 100))
        self.super_parameter_setting_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.super_parameter_setting_area)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Number Basis vector", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Random Frequencies distribution", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SigmoidBasis.ui'
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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.sigma_doubleSpinBox = QDoubleSpinBox(Form)
        self.sigma_doubleSpinBox.setObjectName(u"sigma_doubleSpinBox")

        self.horizontalLayout_2.addWidget(self.sigma_doubleSpinBox)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.offset_doubleSpinBox = QDoubleSpinBox(Form)
        self.offset_doubleSpinBox.setObjectName(u"offset_doubleSpinBox")

        self.horizontalLayout_2.addWidget(self.offset_doubleSpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 881, 68))
        self.super_parameter_setting_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.super_parameter_setting_area)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Sigmoid width:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Initial/Final sigmoid offset:", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Number of basis vectors:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Random step distribution type:", None))
    # retranslateUi


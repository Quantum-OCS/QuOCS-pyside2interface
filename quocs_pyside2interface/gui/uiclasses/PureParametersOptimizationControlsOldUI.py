# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PureParametersOptimizationControlsOld.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1233, 1093)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_16.addWidget(self.label)

        self.parameters_number_spinbox = QSpinBox(Dialog)
        self.parameters_number_spinbox.setObjectName(u"parameters_number_spinbox")
        self.parameters_number_spinbox.setMinimum(1)
        self.parameters_number_spinbox.setMaximum(100)

        self.horizontalLayout_16.addWidget(self.parameters_number_spinbox)

        self.update_parametes_number_button = QPushButton(Dialog)
        self.update_parametes_number_button.setObjectName(u"update_parametes_number_button")

        self.horizontalLayout_16.addWidget(self.update_parametes_number_button)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_17.addWidget(self.label_16)

        self.parameter_number_selected_spinbox = QSpinBox(Dialog)
        self.parameter_number_selected_spinbox.setObjectName(u"parameter_number_selected_spinbox")
        self.parameter_number_selected_spinbox.setMinimum(1)
        self.parameter_number_selected_spinbox.setMaximum(100)

        self.horizontalLayout_17.addWidget(self.parameter_number_selected_spinbox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout.addWidget(self.label_15)

        self.parameter_name_edit_line = QLineEdit(Dialog)
        self.parameter_name_edit_line.setObjectName(u"parameter_name_edit_line")

        self.horizontalLayout.addWidget(self.parameter_name_edit_line)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_20)

        self.remove_parameter_button = QPushButton(Dialog)
        self.remove_parameter_button.setObjectName(u"remove_parameter_button")

        self.horizontalLayout.addWidget(self.remove_parameter_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 150))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1213, 148))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.initial_value_edit_line = QLineEdit(self.scrollAreaWidgetContents)
        self.initial_value_edit_line.setObjectName(u"initial_value_edit_line")

        self.horizontalLayout_10.addWidget(self.initial_value_edit_line)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lower_limit_edit_line = QLineEdit(self.scrollAreaWidgetContents)
        self.lower_limit_edit_line.setObjectName(u"lower_limit_edit_line")

        self.horizontalLayout_4.addWidget(self.lower_limit_edit_line)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.upper_limit_edit_line = QLineEdit(self.scrollAreaWidgetContents)
        self.upper_limit_edit_line.setObjectName(u"upper_limit_edit_line")

        self.horizontalLayout_3.addWidget(self.upper_limit_edit_line)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.variation_edit_line = QLineEdit(self.scrollAreaWidgetContents)
        self.variation_edit_line.setObjectName(u"variation_edit_line")

        self.horizontalLayout_7.addWidget(self.variation_edit_line)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_21)

        self.apply_all_parameters_button = QPushButton(Dialog)
        self.apply_all_parameters_button.setObjectName(u"apply_all_parameters_button")

        self.horizontalLayout_18.addWidget(self.apply_all_parameters_button)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.verticalSpacer = QSpacerItem(20, 754, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Controls", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Number of parameters", None))
        self.update_parametes_number_button.setText(QCoreApplication.translate("Dialog", u"Update parameters number", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Select Parameter number", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Parameter Name", None))
        self.remove_parameter_button.setText(QCoreApplication.translate("Dialog", u"Remove parameter", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Initial Value", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Lower Limit", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Upper Limit", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Variation", None))
        self.apply_all_parameters_button.setText(QCoreApplication.translate("Dialog", u"Apply to all parameters", None))
    # retranslateUi


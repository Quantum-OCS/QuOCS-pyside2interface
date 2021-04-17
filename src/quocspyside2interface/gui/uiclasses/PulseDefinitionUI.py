# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PulseDefinition.ui'
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
        Form.resize(1086, 538)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.pulse_name_line_edit = QLineEdit(Form)
        self.pulse_name_line_edit.setObjectName(u"pulse_name_line_edit")

        self.horizontalLayout_7.addWidget(self.pulse_name_line_edit)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.upper_limit_line_edit = QLineEdit(Form)
        self.upper_limit_line_edit.setObjectName(u"upper_limit_line_edit")

        self.horizontalLayout_8.addWidget(self.upper_limit_line_edit)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lower_limit_line_edit = QLineEdit(Form)
        self.lower_limit_line_edit.setObjectName(u"lower_limit_line_edit")

        self.horizontalLayout_8.addWidget(self.lower_limit_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.amplitude_variation_line_edit = QLineEdit(Form)
        self.amplitude_variation_line_edit.setObjectName(u"amplitude_variation_line_edit")

        self.horizontalLayout_12.addWidget(self.amplitude_variation_line_edit)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_19)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.time_name_combobox = QComboBox(Form)
        self.time_name_combobox.setObjectName(u"time_name_combobox")

        self.horizontalLayout_11.addWidget(self.time_name_combobox)

        self.time_line_edit = QLineEdit(Form)
        self.time_line_edit.setObjectName(u"time_line_edit")

        self.horizontalLayout_11.addWidget(self.time_line_edit)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.bins_number_spinbox = QSpinBox(Form)
        self.bins_number_spinbox.setObjectName(u"bins_number_spinbox")

        self.horizontalLayout_11.addWidget(self.bins_number_spinbox)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_18)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.basis_combobox = QComboBox(Form)
        self.basis_combobox.setObjectName(u"basis_combobox")

        self.horizontalLayout.addWidget(self.basis_combobox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.basis_scroll_area = QScrollArea(Form)
        self.basis_scroll_area.setObjectName(u"basis_scroll_area")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basis_scroll_area.sizePolicy().hasHeightForWidth())
        self.basis_scroll_area.setSizePolicy(sizePolicy)
        self.basis_scroll_area.setMinimumSize(QSize(901, 100))
        self.basis_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1066, 122))
        self.basis_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.basis_scroll_area)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lambda_initial_guess_radio_button = QRadioButton(Form)
        self.lambda_initial_guess_radio_button.setObjectName(u"lambda_initial_guess_radio_button")

        self.horizontalLayout_4.addWidget(self.lambda_initial_guess_radio_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.list_initial_guess_radio_button = QRadioButton(Form)
        self.list_initial_guess_radio_button.setObjectName(u"list_initial_guess_radio_button")

        self.horizontalLayout_4.addWidget(self.list_initial_guess_radio_button)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.from_file_initial_guess_radio_button = QRadioButton(Form)
        self.from_file_initial_guess_radio_button.setObjectName(u"from_file_initial_guess_radio_button")

        self.horizontalLayout_4.addWidget(self.from_file_initial_guess_radio_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.initial_guess_scroll_area = QScrollArea(Form)
        self.initial_guess_scroll_area.setObjectName(u"initial_guess_scroll_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.initial_guess_scroll_area.sizePolicy().hasHeightForWidth())
        self.initial_guess_scroll_area.setSizePolicy(sizePolicy1)
        self.initial_guess_scroll_area.setMinimumSize(QSize(901, 50))
        self.initial_guess_scroll_area.setMaximumSize(QSize(16777215, 70))
        self.initial_guess_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1066, 68))
        self.initial_guess_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.initial_guess_scroll_area)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.lambda_scaling_function_radio_button = QRadioButton(Form)
        self.lambda_scaling_function_radio_button.setObjectName(u"lambda_scaling_function_radio_button")

        self.horizontalLayout_6.addWidget(self.lambda_scaling_function_radio_button)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.list_scaling_function_radio_button = QRadioButton(Form)
        self.list_scaling_function_radio_button.setObjectName(u"list_scaling_function_radio_button")

        self.horizontalLayout_6.addWidget(self.list_scaling_function_radio_button)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.from_file_scaling_function_radio_button = QRadioButton(Form)
        self.from_file_scaling_function_radio_button.setObjectName(u"from_file_scaling_function_radio_button")

        self.horizontalLayout_6.addWidget(self.from_file_scaling_function_radio_button)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.scaling_function_scroll_area = QScrollArea(Form)
        self.scaling_function_scroll_area.setObjectName(u"scaling_function_scroll_area")
        sizePolicy1.setHeightForWidth(self.scaling_function_scroll_area.sizePolicy().hasHeightForWidth())
        self.scaling_function_scroll_area.setSizePolicy(sizePolicy1)
        self.scaling_function_scroll_area.setMinimumSize(QSize(901, 50))
        self.scaling_function_scroll_area.setMaximumSize(QSize(16777215, 70))
        self.scaling_function_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1066, 68))
        self.scaling_function_scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scaling_function_scroll_area)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Pulse name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Amplitude limits", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Upper Limit", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Lower Limit", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Amplitude Variation", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Time Settings", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Time Name", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Bin number", None))
        self.label.setText(QCoreApplication.translate("Form", u"Basis ", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Initial guess", None))
        self.lambda_initial_guess_radio_button.setText(QCoreApplication.translate("Form", u"Lambda function", None))
        self.list_initial_guess_radio_button.setText(QCoreApplication.translate("Form", u"List", None))
        self.from_file_initial_guess_radio_button.setText(QCoreApplication.translate("Form", u"From File", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Scaling function", None))
        self.lambda_scaling_function_radio_button.setText(QCoreApplication.translate("Form", u"Lambda function", None))
        self.list_scaling_function_radio_button.setText(QCoreApplication.translate("Form", u"List", None))
        self.from_file_scaling_function_radio_button.setText(QCoreApplication.translate("Form", u"From File", None))
    # retranslateUi


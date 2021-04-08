# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PureParametersOptimizationDialog.ui'
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
        Dialog.resize(1233, 1095)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.optimization_name_edit_line = QLineEdit(Dialog)
        self.optimization_name_edit_line.setObjectName(u"optimization_name_edit_line")

        self.horizontalLayout_2.addWidget(self.optimization_name_edit_line)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.dsm_name_comboBox = QComboBox(Dialog)
        self.dsm_name_comboBox.setObjectName(u"dsm_name_comboBox")

        self.horizontalLayout_6.addWidget(self.dsm_name_comboBox)

        self.horizontalSpacer_19 = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_19)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.algorithm_settings_tab = QTabWidget(Dialog)
        self.algorithm_settings_tab.setObjectName(u"algorithm_settings_tab")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithm_settings_tab.sizePolicy().hasHeightForWidth())
        self.algorithm_settings_tab.setSizePolicy(sizePolicy)
        self.algorithm_settings_tab.setMinimumSize(QSize(1170, 200))

        self.verticalLayout.addWidget(self.algorithm_settings_tab)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
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

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_17)

        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_23)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.comm_fom_settings_button = QPushButton(Dialog)
        self.comm_fom_settings_button.setObjectName(u"comm_fom_settings_button")

        self.horizontalLayout_13.addWidget(self.comm_fom_settings_button)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_24)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.comm_fom_edit_line = QLineEdit(Dialog)
        self.comm_fom_edit_line.setObjectName(u"comm_fom_edit_line")

        self.horizontalLayout_13.addWidget(self.comm_fom_edit_line)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_25)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.update_summary_button = QPushButton(Dialog)
        self.update_summary_button.setObjectName(u"update_summary_button")

        self.horizontalLayout_11.addWidget(self.update_summary_button)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.drop_out_summary_button = QPushButton(Dialog)
        self.drop_out_summary_button.setObjectName(u"drop_out_summary_button")

        self.horizontalLayout_11.addWidget(self.drop_out_summary_button)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_16)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.summary_edit_line = QPlainTextEdit(Dialog)
        self.summary_edit_line.setObjectName(u"summary_edit_line")

        self.verticalLayout.addWidget(self.summary_edit_line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.description_edit_line = QPlainTextEdit(Dialog)
        self.description_edit_line.setObjectName(u"description_edit_line")

        self.verticalLayout.addWidget(self.description_edit_line)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)

        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_15.addWidget(self.save_button)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_22)

        self.load_button = QPushButton(Dialog)
        self.load_button.setObjectName(u"load_button")

        self.horizontalLayout_15.addWidget(self.load_button)


        self.verticalLayout.addLayout(self.horizontalLayout_15)


        self.retranslateUi(Dialog)

        self.algorithm_settings_tab.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Optimization Name", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Algorithm settings", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Name of Direct Search Method", None))
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
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Communication and FoM Evalutation", None))
        self.comm_fom_settings_button.setText(QCoreApplication.translate("Dialog", u"Open Settings", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Status:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Summary", None))
        self.update_summary_button.setText(QCoreApplication.translate("Dialog", u"Update ", None))
        self.drop_out_summary_button.setText(QCoreApplication.translate("Dialog", u"Drop Out", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.load_button.setText(QCoreApplication.translate("Dialog", u"Load", None))
    # retranslateUi


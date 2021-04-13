# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CommFomSettings.ui'
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
        Form.resize(1249, 1073)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)

        self.remote_radio_button = QRadioButton(Form)
        self.remote_radio_button.setObjectName(u"remote_radio_button")

        self.horizontalLayout_6.addWidget(self.remote_radio_button)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)

        self.local_radio_button = QRadioButton(Form)
        self.local_radio_button.setObjectName(u"local_radio_button")

        self.horizontalLayout_6.addWidget(self.local_radio_button)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_15)

        self.allinone_radio_button = QRadioButton(Form)
        self.allinone_radio_button.setObjectName(u"allinone_radio_button")

        self.horizontalLayout_6.addWidget(self.allinone_radio_button)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.comm_scroll_area = QScrollArea(Form)
        self.comm_scroll_area.setObjectName(u"comm_scroll_area")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comm_scroll_area.sizePolicy().hasHeightForWidth())
        self.comm_scroll_area.setSizePolicy(sizePolicy)
        self.comm_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1229, 204))
        self.comm_scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.comm_scroll_area)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_21)

        self.python_class_radio_button = QRadioButton(Form)
        self.python_class_radio_button.setObjectName(u"python_class_radio_button")

        self.horizontalLayout_9.addWidget(self.python_class_radio_button)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_22)

        self.files_exchange_radio_button = QRadioButton(Form)
        self.files_exchange_radio_button.setObjectName(u"files_exchange_radio_button")

        self.horizontalLayout_9.addWidget(self.files_exchange_radio_button)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_23)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.fom_scroll_area = QScrollArea(Form)
        self.fom_scroll_area.setObjectName(u"fom_scroll_area")
        sizePolicy.setHeightForWidth(self.fom_scroll_area.sizePolicy().hasHeightForWidth())
        self.fom_scroll_area.setSizePolicy(sizePolicy)
        self.fom_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1229, 204))
        self.fom_scroll_area.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.fom_scroll_area)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Communication", None))
        self.remote_radio_button.setText(QCoreApplication.translate("Form", u"Remote", None))
        self.local_radio_button.setText(QCoreApplication.translate("Form", u"Local", None))
        self.allinone_radio_button.setText(QCoreApplication.translate("Form", u"All-in-one", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Figure of merit calculation", None))
        self.python_class_radio_button.setText(QCoreApplication.translate("Form", u"Python Class", None))
        self.files_exchange_radio_button.setText(QCoreApplication.translate("Form", u"Files exchange", None))
    # retranslateUi


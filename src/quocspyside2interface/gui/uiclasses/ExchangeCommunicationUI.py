# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ExchangeCommunication.ui'
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
        Dialog.resize(679, 626)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.remote_radio_button = QRadioButton(Dialog)
        self.remote_radio_button.setObjectName(u"remote_radio_button")

        self.horizontalLayout_3.addWidget(self.remote_radio_button)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.local_radio_button = QRadioButton(Dialog)
        self.local_radio_button.setObjectName(u"local_radio_button")

        self.horizontalLayout_3.addWidget(self.local_radio_button)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.allinone_radio_button = QRadioButton(Dialog)
        self.allinone_radio_button.setObjectName(u"allinone_radio_button")

        self.horizontalLayout_3.addWidget(self.allinone_radio_button)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.comm_scroll_area = QScrollArea(Dialog)
        self.comm_scroll_area.setObjectName(u"comm_scroll_area")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comm_scroll_area.sizePolicy().hasHeightForWidth())
        self.comm_scroll_area.setSizePolicy(sizePolicy)
        self.comm_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 659, 68))
        self.comm_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.comm_scroll_area)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.python_class_radio_button = QRadioButton(Dialog)
        self.python_class_radio_button.setObjectName(u"python_class_radio_button")

        self.horizontalLayout_2.addWidget(self.python_class_radio_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.files_exchange_radio_button = QRadioButton(Dialog)
        self.files_exchange_radio_button.setObjectName(u"files_exchange_radio_button")

        self.horizontalLayout_2.addWidget(self.files_exchange_radio_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.fom_scroll_area = QScrollArea(Dialog)
        self.fom_scroll_area.setObjectName(u"fom_scroll_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fom_scroll_area.sizePolicy().hasHeightForWidth())
        self.fom_scroll_area.setSizePolicy(sizePolicy1)
        self.fom_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 659, 366))
        self.fom_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.fom_scroll_area)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_5.addWidget(self.cancel_button)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_5.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Communication", None))
        self.remote_radio_button.setText(QCoreApplication.translate("Dialog", u"Remote", None))
        self.local_radio_button.setText(QCoreApplication.translate("Dialog", u"Local", None))
        self.allinone_radio_button.setText(QCoreApplication.translate("Dialog", u"All-in-one", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Figure of merit calculation", None))
        self.python_class_radio_button.setText(QCoreApplication.translate("Dialog", u"Python Class", None))
        self.files_exchange_radio_button.setText(QCoreApplication.translate("Dialog", u"Files exchange", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi


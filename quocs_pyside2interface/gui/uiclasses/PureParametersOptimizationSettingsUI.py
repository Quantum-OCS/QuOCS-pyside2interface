# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PureParametersOptimizationSettings.ui'
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
        Dialog.resize(1233, 939)
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

        self.general_pure_tab = QTabWidget(Dialog)
        self.general_pure_tab.setObjectName(u"general_pure_tab")

        self.verticalLayout.addWidget(self.general_pure_tab)

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

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Optimization Name", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.load_button.setText(QCoreApplication.translate("Dialog", u"Load", None))
    # retranslateUi


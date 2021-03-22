# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mrossign/QuOCS/PyQtInterface/quocs_pyqtinterface/gui/uifiles/PureParametersOptimizationControlsOld.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1233, 1093)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_16.addWidget(self.label)
        self.parameters_number_spinbox = QtWidgets.QSpinBox(Dialog)
        self.parameters_number_spinbox.setMinimum(1)
        self.parameters_number_spinbox.setMaximum(100)
        self.parameters_number_spinbox.setObjectName("parameters_number_spinbox")
        self.horizontalLayout_16.addWidget(self.parameters_number_spinbox)
        self.update_parametes_number_button = QtWidgets.QPushButton(Dialog)
        self.update_parametes_number_button.setObjectName("update_parametes_number_button")
        self.horizontalLayout_16.addWidget(self.update_parametes_number_button)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_17.addWidget(self.label_16)
        self.parameter_number_selected_spinbox = QtWidgets.QSpinBox(Dialog)
        self.parameter_number_selected_spinbox.setMinimum(1)
        self.parameter_number_selected_spinbox.setMaximum(100)
        self.parameter_number_selected_spinbox.setObjectName("parameter_number_selected_spinbox")
        self.horizontalLayout_17.addWidget(self.parameter_number_selected_spinbox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.parameter_name_edit_line = QtWidgets.QLineEdit(Dialog)
        self.parameter_name_edit_line.setObjectName("parameter_name_edit_line")
        self.horizontalLayout.addWidget(self.parameter_name_edit_line)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.remove_parameter_button = QtWidgets.QPushButton(Dialog)
        self.remove_parameter_button.setObjectName("remove_parameter_button")
        self.horizontalLayout.addWidget(self.remove_parameter_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 150))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1213, 148))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.initial_value_edit_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.initial_value_edit_line.setObjectName("initial_value_edit_line")
        self.horizontalLayout_10.addWidget(self.initial_value_edit_line)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lower_limit_edit_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lower_limit_edit_line.setObjectName("lower_limit_edit_line")
        self.horizontalLayout_4.addWidget(self.lower_limit_edit_line)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.upper_limit_edit_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.upper_limit_edit_line.setObjectName("upper_limit_edit_line")
        self.horizontalLayout_3.addWidget(self.upper_limit_edit_line)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.variation_edit_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.variation_edit_line.setObjectName("variation_edit_line")
        self.horizontalLayout_7.addWidget(self.variation_edit_line)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem8)
        self.apply_all_parameters_button = QtWidgets.QPushButton(Dialog)
        self.apply_all_parameters_button.setObjectName("apply_all_parameters_button")
        self.horizontalLayout_18.addWidget(self.apply_all_parameters_button)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        spacerItem9 = QtWidgets.QSpacerItem(20, 754, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "Controls"))
        self.label.setText(_translate("Dialog", "Number of parameters"))
        self.update_parametes_number_button.setText(_translate("Dialog", "Update parameters number"))
        self.label_16.setText(_translate("Dialog", "Select Parameter number"))
        self.label_15.setText(_translate("Dialog", "Parameter Name"))
        self.remove_parameter_button.setText(_translate("Dialog", "Remove parameter"))
        self.label_10.setText(_translate("Dialog", "Initial Value"))
        self.label_3.setText(_translate("Dialog", "Lower Limit"))
        self.label_2.setText(_translate("Dialog", "Upper Limit"))
        self.label_9.setText(_translate("Dialog", "Variation"))
        self.apply_all_parameters_button.setText(_translate("Dialog", "Apply to all parameters"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

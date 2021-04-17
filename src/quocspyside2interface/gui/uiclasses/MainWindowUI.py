# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1402, 882)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.parameters_optimization_action = QAction(MainWindow)
        self.parameters_optimization_action.setObjectName(u"parameters_optimization_action")
        self.dcrab_optimization_action = QAction(MainWindow)
        self.dcrab_optimization_action.setObjectName(u"dcrab_optimization_action")
        self.load_file_action = QAction(MainWindow)
        self.load_file_action.setObjectName(u"load_file_action")
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_7 = QVBoxLayout(self.main_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.main_commands_layout = QVBoxLayout()
        self.main_commands_layout.setObjectName(u"main_commands_layout")
        self.start_optimization_button = QPushButton(self.main_widget)
        self.start_optimization_button.setObjectName(u"start_optimization_button")

        self.main_commands_layout.addWidget(self.start_optimization_button)

        self.main_operations_label = QLabel(self.main_widget)
        self.main_operations_label.setObjectName(u"main_operations_label")

        self.main_commands_layout.addWidget(self.main_operations_label)

        self.stop_optimization_button = QPushButton(self.main_widget)
        self.stop_optimization_button.setObjectName(u"stop_optimization_button")

        self.main_commands_layout.addWidget(self.stop_optimization_button)


        self.verticalLayout_7.addLayout(self.main_commands_layout)

        self.vertical_buttons_plotter_spacer_2 = QSpacerItem(1135, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.vertical_buttons_plotter_spacer_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.label_7 = QLabel(self.main_widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.optimization_details_plain_text = QPlainTextEdit(self.main_widget)
        self.optimization_details_plain_text.setObjectName(u"optimization_details_plain_text")

        self.verticalLayout_7.addWidget(self.optimization_details_plain_text)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label = QLabel(self.main_widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalSpacer_8 = QSpacerItem(148, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_10.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.label_3 = QLabel(self.main_widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_parameter_label = QLabel(self.main_widget)
        self.name_parameter_label.setObjectName(u"name_parameter_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.name_parameter_label.sizePolicy().hasHeightForWidth())
        self.name_parameter_label.setSizePolicy(sizePolicy2)
        self.name_parameter_label.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.name_parameter_label)

        self.select_parameter_spinbox = QSpinBox(self.main_widget)
        self.select_parameter_spinbox.setObjectName(u"select_parameter_spinbox")
        self.select_parameter_spinbox.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.select_parameter_spinbox)

        self.value_parameter_label = QLabel(self.main_widget)
        self.value_parameter_label.setObjectName(u"value_parameter_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.value_parameter_label.sizePolicy().hasHeightForWidth())
        self.value_parameter_label.setSizePolicy(sizePolicy3)
        self.value_parameter_label.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.value_parameter_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.drop_out_parameter_button = QPushButton(self.main_widget)
        self.drop_out_parameter_button.setObjectName(u"drop_out_parameter_button")

        self.horizontalLayout.addWidget(self.drop_out_parameter_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)

        self.pulse_index_label = QLabel(self.main_widget)
        self.pulse_index_label.setObjectName(u"pulse_index_label")

        self.horizontalLayout_2.addWidget(self.pulse_index_label)

        self.horizontalSpacer_7 = QSpacerItem(78, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fom_plotter = PlotWidget(self.main_widget)
        self.fom_plotter.setObjectName(u"fom_plotter")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.fom_plotter.sizePolicy().hasHeightForWidth())
        self.fom_plotter.setSizePolicy(sizePolicy4)
        self.fom_plotter.setMinimumSize(QSize(300, 300))

        self.verticalLayout.addWidget(self.fom_plotter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.drop_out_fom_button = QPushButton(self.main_widget)
        self.drop_out_fom_button.setObjectName(u"drop_out_fom_button")

        self.horizontalLayout_3.addWidget(self.drop_out_fom_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.previous_pulse_plot_button = QPushButton(self.main_widget)
        self.previous_pulse_plot_button.setObjectName(u"previous_pulse_plot_button")

        self.verticalLayout_2.addWidget(self.previous_pulse_plot_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.pulses_plotter = PlotWidget(self.main_widget)
        self.pulses_plotter.setObjectName(u"pulses_plotter")
        sizePolicy4.setHeightForWidth(self.pulses_plotter.sizePolicy().hasHeightForWidth())
        self.pulses_plotter.setSizePolicy(sizePolicy4)
        self.pulses_plotter.setMinimumSize(QSize(300, 300))

        self.horizontalLayout_5.addWidget(self.pulses_plotter)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.next_pulse_plot_button = QPushButton(self.main_widget)
        self.next_pulse_plot_button.setObjectName(u"next_pulse_plot_button")

        self.verticalLayout_3.addWidget(self.next_pulse_plot_button)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.drop_out_pulse_button = QPushButton(self.main_widget)
        self.drop_out_pulse_button.setObjectName(u"drop_out_pulse_button")

        self.horizontalLayout_4.addWidget(self.drop_out_pulse_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.main_widget)
        self.bar_menu = QMenuBar(MainWindow)
        self.bar_menu.setObjectName(u"bar_menu")
        self.bar_menu.setGeometry(QRect(0, 0, 1402, 22))
        self.file_menu = QMenu(self.bar_menu)
        self.file_menu.setObjectName(u"file_menu")
        self.menuNew = QMenu(self.file_menu)
        self.menuNew.setObjectName(u"menuNew")
        MainWindow.setMenuBar(self.bar_menu)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.bar_menu.addAction(self.file_menu.menuAction())
        self.file_menu.addAction(self.menuNew.menuAction())
        self.file_menu.addAction(self.load_file_action)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.parameters_optimization_action)
        self.menuNew.addAction(self.dcrab_optimization_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.parameters_optimization_action.setText(QCoreApplication.translate("MainWindow", u"Parameters Optimization", None))
        self.dcrab_optimization_action.setText(QCoreApplication.translate("MainWindow", u"dCRAB Optimization", None))
        self.load_file_action.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.start_optimization_button.setText(QCoreApplication.translate("MainWindow", u"Start Optimization", None))
        self.main_operations_label.setText(QCoreApplication.translate("MainWindow", u"Hello", None))
        self.stop_optimization_button.setText(QCoreApplication.translate("MainWindow", u"Stop Optimization", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Optimization details", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Figure of Merit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.name_parameter_label.setText(QCoreApplication.translate("MainWindow", u"Parameter", None))
        self.value_parameter_label.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.drop_out_parameter_button.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None))
        self.pulse_index_label.setText(QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.drop_out_fom_button.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None))
        self.previous_pulse_plot_button.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.next_pulse_plot_button.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.drop_out_pulse_button.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


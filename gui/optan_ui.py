# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optan.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 875)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(10, 10, 1491, 791))
        self.tabs.setObjectName("tabs")
        self.load_tab = QtWidgets.QWidget()
        self.load_tab.setObjectName("load_tab")
        self.load_exp = QtWidgets.QGroupBox(self.load_tab)
        self.load_exp.setGeometry(QtCore.QRect(10, 10, 251, 201))
        self.load_exp.setObjectName("load_exp")
        self.folder_load_btn = QtWidgets.QPushButton(self.load_exp)
        self.folder_load_btn.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.folder_load_btn.setObjectName("folder_load_btn")
        self.deg_collected_list = QtWidgets.QComboBox(self.load_exp)
        self.deg_collected_list.setGeometry(QtCore.QRect(87, 20, 71, 31))
        self.deg_collected_list.setObjectName("deg_collected_list")
        self.line = QtWidgets.QFrame(self.load_exp)
        self.line.setGeometry(QtCore.QRect(-10, 50, 271, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox = QtWidgets.QCheckBox(self.load_exp)
        self.checkBox.setGeometry(QtCore.QRect(20, 66, 121, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.load_exp)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 86, 121, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.line_2 = QtWidgets.QFrame(self.load_exp)
        self.line_2.setGeometry(QtCore.QRect(-10, 105, 271, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.folder_load_go_btn = QtWidgets.QPushButton(self.load_exp)
        self.folder_load_go_btn.setGeometry(QtCore.QRect(165, 20, 71, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.folder_load_go_btn.setPalette(palette)
        self.folder_load_go_btn.setAutoFillBackground(False)
        self.folder_load_go_btn.setStyleSheet("background-color: rgb(195, 200, 0);")
        self.folder_load_go_btn.setObjectName("folder_load_go_btn")
        self.max_hist_2 = QtWidgets.QSpinBox(self.load_exp)
        self.max_hist_2.setGeometry(QtCore.QRect(40, 150, 81, 31))
        self.max_hist_2.setKeyboardTracking(False)
        self.max_hist_2.setMaximum(1200)
        self.max_hist_2.setSingleStep(10)
        self.max_hist_2.setObjectName("max_hist_2")
        self.min_hist_2 = QtWidgets.QSpinBox(self.load_exp)
        self.min_hist_2.setGeometry(QtCore.QRect(40, 120, 81, 31))
        self.min_hist_2.setKeyboardTracking(False)
        self.min_hist_2.setMaximum(1200)
        self.min_hist_2.setSingleStep(10)
        self.min_hist_2.setObjectName("min_hist_2")
        self.label_23 = QtWidgets.QLabel(self.load_exp)
        self.label_23.setGeometry(QtCore.QRect(3, 154, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_3 = QtWidgets.QLabel(self.load_exp)
        self.label_3.setGeometry(QtCore.QRect(6, 127, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.toggle_hist_2 = QtWidgets.QRadioButton(self.load_exp)
        self.toggle_hist_2.setGeometry(QtCore.QRect(130, 130, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toggle_hist_2.setFont(font)
        self.toggle_hist_2.setObjectName("toggle_hist_2")
        self.recon_live_4 = PlotWidget(self.load_tab)
        self.recon_live_4.setGeometry(QtCore.QRect(310, 50, 541, 691))
        self.recon_live_4.setObjectName("recon_live_4")
        self.tabs.addTab(self.load_tab, "")
        self.sino_tab = QtWidgets.QWidget()
        self.sino_tab.setObjectName("sino_tab")
        self.calc_3Dsin_btn = QtWidgets.QPushButton(self.sino_tab)
        self.calc_3Dsin_btn.setGeometry(QtCore.QRect(30, 20, 111, 51))
        self.calc_3Dsin_btn.setObjectName("calc_3Dsin_btn")
        self.label_22 = QtWidgets.QLabel(self.sino_tab)
        self.label_22.setGeometry(QtCore.QRect(120, 70, 81, 31))
        self.label_22.setObjectName("label_22")
        self.horizontalSlider = QtWidgets.QSlider(self.sino_tab)
        self.horizontalSlider.setGeometry(QtCore.QRect(120, 100, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_4 = QtWidgets.QLabel(self.sino_tab)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 81, 31))
        self.label_4.setObjectName("label_4")
        self.recon_live_2 = PlotWidget(self.sino_tab)
        self.recon_live_2.setGeometry(QtCore.QRect(30, 180, 691, 531))
        self.recon_live_2.setObjectName("recon_live_2")
        self.tabs.addTab(self.sino_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 26))
        self.menubar.setObjectName("menubar")
        self.menuddd = QtWidgets.QMenu(self.menubar)
        self.menuddd.setObjectName("menuddd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuddd.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_exp.setTitle(_translate("MainWindow", "Load experiment"))
        self.folder_load_btn.setText(_translate("MainWindow", "Folder"))
        self.deg_collected_list.setToolTip(_translate("MainWindow", "Select camera type, if you do not have one, select \'virtual\' and we generate data for you"))
        self.checkBox.setText(_translate("MainWindow", "Average frames"))
        self.checkBox_2.setText(_translate("MainWindow", "Average sweeps"))
        self.folder_load_go_btn.setText(_translate("MainWindow", "GO"))
        self.label_23.setText(_translate("MainWindow", "Max"))
        self.label_3.setText(_translate("MainWindow", "Min"))
        self.toggle_hist_2.setText(_translate("MainWindow", "toggle\n"
" levels"))
        self.tabs.setTabText(self.tabs.indexOf(self.load_tab), _translate("MainWindow", "Load"))
        self.calc_3Dsin_btn.setText(_translate("MainWindow", "Calc 3D\n"
" sinogram"))
        self.label_22.setText(_translate("MainWindow", "IDX"))
        self.label_4.setText(_translate("MainWindow", "Sinogram"))
        self.tabs.setTabText(self.tabs.indexOf(self.sino_tab), _translate("MainWindow", "Sinogram"))
        self.menuddd.setTitle(_translate("MainWindow", "File"))
from pyqtgraph import PlotWidget

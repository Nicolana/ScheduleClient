# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xhu_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(990, 700)
        MainWindow.setMinimumSize(QtCore.QSize(990, 700))
        MainWindow.setMaximumSize(QtCore.QSize(990, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scoreTable = QtWidgets.QTableWidget(self.centralwidget)
        self.scoreTable.setGeometry(QtCore.QRect(190, 40, 791, 631))
        self.scoreTable.setMinimumSize(QtCore.QSize(791, 631))
        self.scoreTable.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.scoreTable.setFont(font)
        self.scoreTable.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.scoreTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scoreTable.setAutoFillBackground(True)
        self.scoreTable.setLineWidth(1)
        self.scoreTable.setAutoScrollMargin(7)
        self.scoreTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.scoreTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.scoreTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.scoreTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.scoreTable.setRowCount(21)
        self.scoreTable.setObjectName("scoreTable")
        self.scoreTable.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.scoreTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.scoreTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scoreTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.scoreTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.scoreTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.scoreTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.scoreTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.scoreTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.scoreTable.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.scoreTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scoreTable.setItem(2, 0, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 360, 161, 311))
        self.tableWidget_2.setDragDropOverwriteMode(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(8, 0, item)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 70, 81, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 70, 72, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 130, 141, 211))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 100, 161, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scoreTable.setToolTip(_translate("MainWindow", "成绩课表"))
        item = self.scoreTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.scoreTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "课程名称"))
        item = self.scoreTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "课程性质"))
        item = self.scoreTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "开课学院"))
        item = self.scoreTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "学分"))
        item = self.scoreTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "绩点"))
        item = self.scoreTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "成绩"))
        __sortingEnabled = self.scoreTable.isSortingEnabled()
        self.scoreTable.setSortingEnabled(False)
        self.scoreTable.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "年级"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "学院"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "专业"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "平均绩点"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "绩点评价"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "学年"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "学期"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "数据"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item.setText(_translate("MainWindow", "2"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.comboBox.setItemText(0, _translate("MainWindow", "成绩"))
        self.comboBox.setItemText(1, _translate("MainWindow", "课表"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.label.setText(_translate("MainWindow", "<h3>绩点计算软件</h3><p>西华大学计算机协会出品</p><p>Version :  1.0.0</p>联系方式 ： 854630101<p><p>作者 ：Nicolana </p>"))
        self.pushButton.setText(_translate("MainWindow", "切换"))


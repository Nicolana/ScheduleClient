#coding: utf-8
# the view of app
from PIL import Image
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QWidget, QMessageBox, QMainWindow,\
QPushButton, QLabel, QLineEdit, QTableWidgetItem
from xhu_MainWindow import Ui_MainWindow
from xhu.xhu import XHU
from model import INFO

class Windows_Main(Ui_MainWindow):

	def __init__(self, name, class_, credit, academy, major):
		"""
			@param:
				name: 学生姓名
				class_: 学生年级
				credit: 学号
				academy: 所属学院
				major: 专业
		"""
		super(Windows_Main, self).__init__()
		self.q = QMainWindow()
		self.setupUi(self.q)
		self.scoreTable.setColumnWidth(0, 200)
		self.scoreTable.setColumnWidth(1, 150)

		item = QTableWidgetItem()
		self.q.setWindowIcon(QIcon('./images/index.png'))
		item = self.tableWidget_2.item(0, 0)
		item.setText(name)
		item = self.tableWidget_2.item(1, 0)
		item.setText(class_)
		item = self.tableWidget_2.item(2, 0)
		item.setText(credit) # xuehao
		item = self.tableWidget_2.item(3, 0)
		item.setText(academy) # 学院
		item = self.tableWidget_2.item(4, 0)
		item.setText(major)
		self.pushButton.clicked.connect(self.changeState)

	def insert_table(self, XN, XQ):
		"""
		@para: 
			XN: 学年
			XQ: 学期
		@description: 
			根据学年和学期从数据库中获取该学年学期的课表，并更新到表格之中
		"""
		info = INFO()
		info = info.cx.execute("select className, classProperty, open_academy, credits, GPA , grade from xhu_" + str(XN)[:4] + "_" + str(XN)[5:] + '_' + str(XQ)).fetchall()
		for info_item in range(len(info)):
			for i in range(len(info[info_item])):
				item = QTableWidgetItem()
				self.scoreTable.setItem(info_item, i, item)
				item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
				item.setText(str(info[info_item ][i]))

	def update_info(self, points, evaluate, years, semester):
     	# update the left bottom table 
		item = self.tableWidget_2.item(4, 0)
		item.setText(points)
		item = self.tableWidget_2.item(5, 0)
		item.setText(evaluate)
		item = self.tableWidget_2.item(6, 0)
		item.setText(years)
		item = self.tableWidget_2.item(7, 0)
		item.setText(semester)

	def changeState(self):
		# 根据下拉框中的数据更新表众的数据
		self.scoreTable.clearContents()
		year = self.comboBox_2.currentText()
		semester = self.comboBox_3.currentText()
		self.insert_table(year, semester)

	def init_comboBox(self, years):
		# 初始化选择框
		for index in range(len(years)):
			self.comboBox_2.setItemText(index, str(years[index]))


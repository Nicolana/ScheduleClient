# coding:utf-8
# 西华成绩、课程、绩点计算软件
# 西华网络与计算机出品
# 联系人   ： Nicolana
# 联系方式 ： QQ 854630101

import sys
import sqlite3
import json
import threading
# from view import XHU_Dialog
from view import Windows_Main
from model import INFO

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QCoreApplication,QRect
from PyQt5.QtGui import QIcon
from xhu.xhu import XHU
from xhu_ui import Ui_xhu

db = INFO()
# db.insertTranscript(params)
# db.insertUserInfo(params)


class XHU_Dialog(Ui_xhu):

	def __init__(self):
		super(XHU_Dialog, self).__init__()
		self.w = QDialog()
		self.setupUi(self.w)
		self.pushButton.clicked.connect(self.login)
		self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
		self.w.setWindowIcon(QIcon('./images/index.png'))


	def checkDialog(self):

		self.m = QDialog(self.w)
		self.m.setObjectName("CheckCode")
		self.m.resize(250, 150)
		self.m.setWindowTitle("验证码")

		# check code image
		code_label = QLabel(self.m)
		code_label.setGeometry(QRect(90, 20, 72, 27))
		code_label.setObjectName("codeLabel")
		code_label.setText("<img src=\"./images/code.gif\">")

		# checkcode input 
		self.code_Edit = QLineEdit(self.m)
		self.code_Edit.setGeometry(QRect(90, 67, 72, 27))


		pushButton_3 = QPushButton("Ok", self.m)
		pushButton_3.resize(pushButton_3.sizeHint())
		pushButton_3.move(90, 115)
		pushButton_3.clicked.connect(self.showCheck)
		self.m.show()
		self.m.exec_()

	def showCheck(self):
		newCode = self.code_Edit.text()
		self.m.close()

		if newCode:
			self.xhu.xhu_login_acount(newCode)
			self.w.close()
			for _xn in self.xhu.info["XN"]:
				for _xq in self.xhu.info["XQ"]:
					db.xhu_db_create(_xn, _xq)
			self.xhu.xhu_grade()
			db.insertUserInfo(tuple(self.xhu.get_stu_info()))
			for items in self.xhu.tds:
				for item in items:
					db.insertTranscript(tuple(item[0]), item[1], item[2])
			self.main_window()

	def login(self):
		user = self.lineEdit.text()
		password = self.lineEdit_2.text()
		if user!= "":
			if password != "":
				self.xhu = XHU(user, password)
				self.checkDialog()
			else:
				# return "Please Enter password"
				QMessageBox.warning(self.w, "错误提示", "登录失败，请输入密码",\
				 QMessageBox.Ok)
		else:
			# return "Please Enter username"
				QMessageBox.warning(self.w, "错误提示", "登录失败, 请输入账号",\
					QMessageBox.Ok)

	def main_window(self):
		self.window = Windows_Main(self.xhu.xm, self.xhu.info["forwarding"], self.xhu.user ,\
			self.xhu.info["academy"] , self.xhu.info["major"])
		self.window.init_comboBox(self.xhu.info["XN"])
		self.window.changeState()
		self.window.q.show()
		# self.window.q.exec_()



if __name__ == "__main__":

	"""
		credits :绩点
		grade : 成绩
		GPA : 学分
		open_academy: 开课学院
	"""
	
	app = QApplication(sys.argv)
	content = None
	try:
		connect = sqlite3.connect("xhu.db")
		cur = connect.cursor()
		cur.execute("select * from xhu_user")
		content = cur.fetchall()
	except sqlite3.Error as e:
		print(e)

	if content:
		content = content[0]
		user  = content[0] # 学号
		name 	= content[2] # 姓名
		class_  = content[3] # 年级
		academy = content[4] # 学院
		major 	= content[5] # 专业
		XN 		= json.loads(content[6]) # 学年
		# load_main_window(name, class_,  user, academy, major, XN)
		window = Windows_Main(name, class_, user ,\
		academy , major)
		window.init_comboBox(XN)
		window.changeState()
		window.q.show()

	else:
		xhu_login_dialog = XHU_Dialog()
		xhu_login_dialog.w.show()
		
	sys.exit(app.exec_())
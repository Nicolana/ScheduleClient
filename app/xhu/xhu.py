# 爬虫引擎模块
import sys
import os
import json
import threading
from functools import reduce
# from collections import OrderedDict
import requests
import urllib.parse
from bs4 import BeautifulSoup

from xhu.parse import *

# constant variable
gnmkdm = "N121605"
check_code_url = "http://jwc.xhu.edu.cn/CheckCode.aspx"
xhu_login_url = "http://jwc.xhu.edu.cn/default2.aspx"
grade_url = "http://jwc.xhu.edu.cn/xscjcx.aspx"
TIMEOUT = 20
proxies = {}

class XHU():

	def __init__(self, user, password):
		self.user = user
		self.password = password
		self.s = requests.Session()
		self.s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
		self.xm = ""
		self.grade_url = "" # get credits point url
		self.lock = threading.Lock()
		self.tds = [] # 课表信息
		self.info = {} # 学生身份信息

		# 检查数据库是否存在
		# if not self.isDBExists():
		# 	self.initDB()

		self.xhu_login()

	def isDBExists(self):
		"""
			@description: 数据库存在检查
		"""
		return os.path.exists("xhu.db")

	def xhu_login(self):
		"""
			@description: 获取验证码并保存
		"""
		r = self.s.get(check_code_url) # check code url 
		with open('./images/code.gif','wb') as f:
			f.write(r.content)
			f.close()
		 

	def xhu_login_acount(self, Code):
		"""
			@schedule: 1、获取VIEWSTATE和 cookies
			2、 登录账号密码
		"""
		try:
			login_bg  = self.s.get(xhu_login_url, proxies = proxies, timeout = TIMEOUT)
		except ConnectionError as e:
			print(e)
		except:
			return False

		viewstate = VIEWSTATE(login_bg)
		
		content = {
			"__VIEWSTATE": viewstate,
			"txtUserName": self.user,
			"TextBox2": self.password,
			"txtSecretCode": Code,
			"RadioButtonList1": "学生".encode("gb2312"),
			"Button1": "",
			"lbLanguage": "",
			"hidPdrs": "",
			"hidsc": ""
		}

		login_r = self.s.post(xhu_login_url, data = content, proxies = proxies, timeout = TIMEOUT)
		self.xm = GetName(login_r)
		self.xhu_student_info()
		

	def xhu_student_info(self):
		# 获取相关信息
		self.grade_url = "http://jwc.xhu.edu.cn/xscjcx.aspx?xh=" + self.user + "&xm=" + urllib.parse.quote(self.xm.encode("gb2312")) +"&gnmkdm=N121605"
		payload = {"xh": self.user, "xm": urllib.parse.quote(self.xm.encode("gb2312")), "gnmkdm": "N121605"}
		self.s.headers['Referer'] = self.grade_url
		try:
			response = self.s.get(grade_url, params = payload ,allow_redirects = False, timeout = TIMEOUT, proxies = proxies)
		except ConnectionError as e:
			print(e)
		except:
			return False

		self.info = GetStudentInfo(response)

		# return (__VIEWSTATE, student_name, student_academy, student_major_forwarding, student_major, XN, XQ)


	def xhu_grade(self):
		# 获取绩点
		# get the credits point 
		threads = []
		for _xn in self.info["XN"]:
			for _xq in self.info["XQ"]:
				# self.xhu_db_create(_xn,_xq)
				content = {
					"__EVENTTARGET": "xqd",
					"__VIEWSTATE": self.info["__VIEWSTATE"],
					"hidLanguage": "",
					"ddlXQ": _xq,
					"btn_xq":"学期成绩",
					"ddl_kcxz":"",
					"ddlXN": _xn,
					"__EVENTARGUMENT": ""
				}
				t = threading.Thread(target=self.post_grade, args=(content,_xn, _xq))
				# t.setDaemon(True)
				# t.start()
				threads.append(t)
		for t in threads:
			t.start()
			t.join()


	def post_grade(self, content, _xn, _xq):
		# 获取成绩信息
		try:
			r = self.s.post(self.grade_url, data = content, proxies = proxies, timeout = TIMEOUT) # grade_url : In xhu_student_info class method 
		except ConnectionError as e:
			print(e)

		self.tds.append(GetClassSchedule(r, _xn, _xq))


	def xhu_credits_average(self):
		# 计算绩点平均值
		self.cx.execute("select credits from db_xhu")
		credits = self.cx.fetchall()[1:]

		all_sum = 0
		# all_files = self.cx.execute("select count(*) from db_xhu")
		average = reduce(lambda x,y : x + y, map(lambda x: float(x[0]), credits)) / len(credits)
		print("你的平均绩点为 {0}".format(average))
		return average

	def get_stu_info(self):
		info = [self.user, 
			self.password, 
			self.info["name"], 
			self.info["forwarding"],
			self.info["academy"],
			self.info["major"],
			json.dumps(self.info["XN"])]
		return info

	def get_tds(self):
		if self.tds:
			return self.tds
		return False


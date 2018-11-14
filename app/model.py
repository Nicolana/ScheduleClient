# 数据库处理
import sqlite3


class INFO:

	def __init__(self):
		self.cu = sqlite3.connect("xhu.db")
		self.cx = self.cu.cursor()
		self.create_userTable()
		self.tablename = ""
		# self.XN = XN 	# 学年  year 
		# self.XQ = XQ 	# 学期  semester

	def xhu_db_create(self, XN, XQ):
		"""
			credits :学分
			grade : 成绩
			GPA : 绩点
			open_academy: 开课学院
		"""
		self.cx.execute("select count(*) from sqlite_master where type = 'table' AND name = 'xhu_" +str(XN)[:4] + "_" + str(XN)[5:] + '_' + str(XQ) + "'")
		number = self.cx.fetchall()[0][0]
		# id integer primary key autoincrement not NULL,\
		if number == 0:
			self.cx.execute("create table xhu_" + str(XN)[:4] + "_" + str(XN)[5:] + '_' + str(XQ) + " (\
				year text not NULL , \
				semester integer,\
				classCode text not NULL,\
				className text not NULL,\
				classProperty text NULL,\
				classBelongs text NULL,\
				credits REAL NULL,\
				GPA REAL NULL,\
				grade integer NULL,\
				minor_sign integer,\
				makeup_grade text NULL,\
				rebuid_grade text NULL,\
				open_academy text not NULL,\
				remark text NULL,\
				rebuid_sign text NULL)")

	def create_userTable(self):
		number = self.cx.execute("select count(*) from sqlite_master where type = 'table' AND name = 'xhu_user'").fetchall()[0][0]
		if number == 0:
			self.cx.execute("create table xhu_user (\
				user text not null, \
				password text not null,\
				name text not null,\
				class_ text,\
				academy text,\
				major text,\
				XN text)")


	def insertTranscript(self, value, XN, XQ):
		"""
			 id, year, classCode, className, classProperty, classBelongs, credits, GPA, grade, minor_sign, makeup_grade,rebuid_grade, open_academy, remark, rebuid_sign
		"""
		self.cx.execute("insert into xhu_" + XN.replace('-', '_') + '_' + str(XQ) + " values{0}".format(value))
		self.cu.commit()

	def insertUserInfo(self, *params):
		self.cx.execute("insert into xhu_user values{0}".format(*params))
		self.cu.commit()

	def xhu_db_update(self):
		pass

	def xhu_db_delete(self):
		pass

	def xhu_db_drop(self):
		self.cx.execute("DROP TABLE db_xhu")
		self.cu.commit()

	def db_close(self):
		self.cu.close()

	def initDB(self):
		self.cu = sqlite3.connect("xhu.db")
		self.cx = self.cu.cursor()
		self.create_userTable()
		self.tablename = ""

# 爬虫解析模块
from bs4 import BeautifulSoup


def HtmlDecoding(rawContent):
	"""
		@description: transfer raw response content to text
	"""
	rawContent.coding = "gb2312"
	return rawContent.text

def GetStudentInfo(response):
	"""
		@response: raw response content
	"""
	d = {}

	soup = BeautifulSoup(HtmlDecoding(response), "lxml")

	d["__VIEWSTATE"] = soup.find_all('input')[2]['value']
	d["name"] = soup.find(id = "lbl_xm").text # 姓名
	d["academy"] = soup.find(id = "lbl_xy").text # 学院
	d["major"] = soup.find(id = "lbl_zymc").text # 专业
	d["forwarding"] = soup.find(id = "lbl_xzb").text # 专业方向及班级
	# print(student_major_forwarding)
	XN_temp = soup.find(id = "ddlXN").find_all('option') # 学年
	XN = []   # 学年的列表
	for item in XN_temp:
		if item.string:
			XN.append(item.string)
	XQ = [1,2]

	d["XN"] = XN
	d["XQ"] = XQ

	return d

def VIEWSTATE(response):
	"""
		@params:
			raw: 网页文本数据
		@return:
			viewstate: 返回从网页中解析出来的viewstate
	"""
	try:
		viewstate = BeautifulSoup(HtmlDecoding(response), "lxml").find(class_="login_bg").find("input")['value']
	except Exception as e:
		return False
	return viewstate

def GetName(response):
	soup = BeautifulSoup(HtmlDecoding(response), "lxml")
	try:
		xm = soup.find(id="xhxm").text[:-2]
	except:
		xm = "未知"
	return xm

def GetClassSchedule(response, _xn, _xq):
	"""
		@description: parse out all the transcripts
		@解析： 解析出所有的成绩单
	"""
	d = [] # empty class schedule
	soup = BeautifulSoup(HtmlDecoding(response), "lxml")
	trs = soup.find(id = "Datagrid1").find_all('tr')
	index = 0
	for tr in trs:
		tds = tr.find_all('td')
		td_tuple = []
		# td_tuple.append(index)
		for td in tds:
			if td.string == None:
				td_tuple.append('')

			else:
				td_tuple.append(td.string.strip())
		# 跳过第一次循环，去掉冗余信息
		if index > 0:
			# self.xhu_db_insert(tuple(td_tuple), _xn, _xq)
			d.append([td_tuple, _xn, _xq])
		index += 1
	return d

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

class MZITU(object):
	"""docstring for MZITU"""
	def __init__(self):
		self.headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
	
	def getPageCode(self, url):
		response = requests.get(url, headers=self.headers)
		return response
	
	def getAllUrl(self, url):
		soup = BeautifulSoup(self.getPageCode(url).text, 'lxml')
		items = soup.find('div',attrs={'class':'all'}).find_all('a')	
		for item in items:
			title = item.get_text()
			print u'开始保存', title
			path = str(title)
			self.mkdir(path)
			os.chdir('/home/yuzhehui/Pictures/' + path)
			href = item['href']
			self.html(href)

	def html(self, url):	
		html = self.getPageCode(url)
		max_span = BeautifulSoup(html.text, 'lxml').find('div',class_ = 'pagenavi').find_all('span')[-2].get_text()
		for page in range(1, int(max_span)+1):
			page_url = url + '/' + str(page)
			self.img(page_url)

	def img(self, url):
		img_html = self.getPageCode(url)
		img_url = BeautifulSoup(img_html.text, 'lxml').find('div',class_='main-image').find('img')['src']
		self.save(img_url)

	def save(self, url):
		name = url[-9:-4]
		img = self.getPageCode(url)
		f = open(name + '.jpg', 'ab')
		f.write(img.content)
		f.close()

	def mkdir(self, path):
		path = path.strip()
		isExists = os.path.exists(os.path.join('/home/yuzhehui/Pictures/', path))
		if not isExists:
			print u'建了一个名字叫做', path, u'的文件夹！'
			os.makedirs(os.path.join('/home/yuzhehui/Pictures/', path))
			return True
		else:
			print u'名字叫做', path, u'的文件夹已经存在了！'
			return False
mzitu = MZITU()
mzitu.getAllUrl('http://www.mzitu.com/all')
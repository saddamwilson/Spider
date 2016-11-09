# -*- coding: utf-8 -*-
import urllib2     # 导入urllib2模块
req = urllib2.urlopen('https://www.nuomi.com/?cid=002540')
buf = req.read()

import re         # 导入re模块
listurl = re.findall(r'http:.+\.jpg',buf)   #正则表达式，匹配图片格式
print listurl     # 将图片的格式放入list中

i = 0
for url in listurl:
	f = open(str(i)+'.jpg',"wb")    #打开文件
	try:
		req = urllib2.urlopen(url)
	except:
		print 'wrong'
	buf = req.read()              #读出文件
	f.write(buf)                  #写入文件
	i = i + 1                     #更改文件名

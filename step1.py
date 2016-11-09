# -*- coding: utf-8 -*-
#目标：下载各目录的壁纸（大图）
from bs4 import BeautifulSoup
import urllib2
import urllib
import re
import os
import chardet
import sys

#创建壁纸下载文件夹
path = '/home/yuzhehui/Pictures/'
if not os.path.isdir(path):
    os.makedirs(path)
#目录
big_title = []

#首页打开
url = 'http://www.zasv.com/forum-105-1.html' 
headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
soup = BeautifulSoup(response, "lxml")
print sys.getfilesystemencoding() 
#print 'Html is encoding by : %s' % chardet.detect(response.read())

# pat_menu_link = re.compile('<a href="(http://www\.zasv\.com/thread-[0-9]{7}-[0-9]{1}-[0-9][0-9]*\.html)" onclick="atarget\(this\)" class="s xst">',re.S)
# menu_link = re.findall(pat_menu_link,response.read().decode('GB18030').encode('utf-8'))

# for c_item in menu_link:
# 	print c_item


my_girl = soup.find_all('a', class_ = "s xst")
for girl in my_girl:
    link = girl.get('href') 
    print link
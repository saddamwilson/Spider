# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import sys
url = 'http://www.qiushibaike.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    # print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

content = response.read().decode('utf-8')
soup = BeautifulSoup(content, "lxml")
# print sys.getfilesystemencoding() 
# pattern = re.compile(r'<a href=".*?" target="_blank" class="contentHerf" ><div class="content"><span>(.*?)</span></div></a>',re.S)
# items = re.findall(pattern,content)
items = soup.find_all('a',attrs={'class':'contentHerf'})
# print items
for item in items:
	print item.span.get_text()
# -*- coding: utf-8 -*-
#目标：下载各目录的壁纸（大图）
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
url = 'http://www.netbian.com/' 
headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)

print sys.getfilesystemencoding() 
#print 'Html is encoding by : %s' % chardet.detect(response.read())

#首页目录源代码获取
pat_menu = re.compile(r'<ul class="menu">(.*?)</a></div>',re.S)
code_menu = re.search(pat_menu,response.read().decode('GB2312').encode('utf-8'))

#目录标题
pat_menu_title = re.compile(r'<a href=".*?" title="(.*?)">',re.S)
menu_title = re.findall(pat_menu_title,code_menu.group(1))
for a_item in menu_title:
    big_title.append(a_item)
    print a_item

#目录链接
pat_menu_link = re.compile(r'<a href="(.*?)" title=".*?">',re.S)
menu_link = re.findall(pat_menu_link,code_menu.group(1))

for c_item in menu_link:
	print c_item


#进入目录
j = 0
for b_item in menu_link:
    url_menu = 'http://www.netbian.com/' + b_item
    print b_item
    request_son = urllib2.Request(url_menu,headers = headers)
    try:
        response_son = urllib2.urlopen(request_son)
    except:
        print 'wrong'
        continue
    #获得每个目录的图片标题，链接
    
    #获得子目录标题
    title_son = []
    pat_title_son = re.compile('<img src=".*?" data-src=".*?" alt="(.*?)"/>',re.S)
    res_title = re.findall(pat_title_son,response_son.read().decode('GB2312').encode('utf-8'))
    for c_item in res_title:
        title_son.append(c_item)

    #筛选出子目录代码
    pat_code_son = re.compile('<ul>(.*?)</ul>',re.S)
    middle_pattern = urllib2.Request(url_menu,headers = headers)
    middle_response = urllib2.urlopen(middle_pattern)
    res_code_son = re.search(pat_code_son,middle_response.read().decode('GB2312').encode('utf-8'))
    
    #获得子目录链接，合成大图网页链接
    pat_link_son = re.compile('<li><a href="(.*?)" target="_blank"><img',re.S)
    res_link = re.findall(pat_link_son,res_code_son.group(1))
    i = 0
    #显示进度
    print big_title[j]
    for d_item in res_link:
        #获得大图下载链接
        if d_item == 'http://www.mmmwu.com/':
            pass
        else:
            new_link = 'http://www.netbian.com/' + d_item[:-4] + '-1920x1080.htm'
            print new_link
            request_real = urllib2.Request(new_link,headers = headers)
            response_real = urllib2.urlopen(request_real)
            pat_real = re.compile('<img src="(.*?)" alt=".*?"/></td></tr>')
            
            link_real = re.search(pat_real,response_real.read().decode('GB2312').encode('utf-8'))
            #跳过vip壁纸
            if link_real:
                fina_link = link_real.group(1)
                #创建下载目录
                path_final = '/home/yuzhehui/Pictures/' + big_title[j] + '\\'
                if not os.path.isdir(path_final):
                    os.makedirs(path_final)
                path_pic = path_final + title_son[i] + '.jpg'
                f = open(path_pic,'wb')
                data = urllib.urlopen(fina_link)
                f.write(data.read())
                f.close()
                if not data:
                    print "Download Failed."
            i += 1
    print 'One menu download OK.'
    j += 1


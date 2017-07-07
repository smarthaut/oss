#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/7 16:43
# @Author  : huanghe
# @Site    : 
# @File    : list_device.py
# @Software: PyCharm Community Edition
#http://172.30.66.163:9090/WebServlet?attribute=oss_list_device&home_id=10000049
import urllib.parse
import urllib.request
date = urllib.parse.urlencode({'attribute':'oss_list_device','home_id':10000049})
date = date.encode('utf-8')
request = urllib.request.Request("http://172.30.66.163:9090/WebServlet")
f = urllib.request.urlopen(request, date)
print(f.read().decode('utf-8'))

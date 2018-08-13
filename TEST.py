# -*- coding:utf-8 -*-
'''
@project=爬虫
@file=TEST
@Author=Administrator
@creat_time=2018/8/1319:13
'''
from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar=MozillaCookieJar('cookie.txt')
cookiejar.load(ignore_discard=True)

handle=request.HTTPCookieProcessor(cookiejar)
opener=request.build_opener(handle)

resp=opener.open('http://httpbin.org/cookies')

# cookiejar.save(ignore_discard=True)
for cookie in cookiejar:
    print(cookie)
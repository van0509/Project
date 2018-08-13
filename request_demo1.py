# -*- coding:utf-8 -*-
'''
@project=爬虫
@file=request_demo1
@Author=Administrator
@creat_time=2018/8/1319:47
'''
import requests
kw={'wd':'中国'}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
reponse=requests.get('https://www.baidu.com/s',params=kw,headers=headers)
# resp=reponse.content.decode('utf-8')
# requests
# print(reponse.url,reponse.encoding,reponse.status_code)
with open('baidu.html','w',encoding='utf-8') as f:
    f.write(reponse.content.decode('utf-8'))
# -*- coding:utf-8 -*-
'''
@project=爬虫
@file=TEST
@Author=Administrator
@creat_time=2018/8/1319:13
'''
import re,UA
import requests
from MySqlHeper import DBHelper
start_url='http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
base_url='http://www.ygdy8.net/'
headers={
'User-Agent': UA.UA().userAgent()
}
def get_detail_urls(url):
    response=requests.get(url,headers=headers).text
    pattern='<td[\s\S]*?<a href="([\S]*?)" class="ulink">'
    resp=re.findall(pattern,response)
    # print(resp)
    urls=map(lambda url:base_url+url,resp)
    return urls
def parse_detail_page(url):
    # movies={}
    response=requests.get(url,headers=headers).content.decode('gbk')
    # print(response)
    pattern='<font color=#07519a>([\S]*?)</font>[\s\S]*?<img[\s\S]*?src="([\S]*?)"[\s\S]*?<a href="([\S]*?)">'
    Infos=re.findall(pattern,response)
    print(Infos)
    # movies['title']=Infos[0][0]
    # movies['cover']=Infos[0][1]
    # movies['download']=Infos[0][2]
    dbhelper = DBHelper()
    # 插入一条数据
    name = Infos[0][0]
    picture = Infos[0][1]
    downlink = Infos[0][2]
    sql = "INSERT INTO seven.movies(name,picture,downlink) VALUES(%s,%s,%s)"
    params = (name,picture,downlink)
    result = dbhelper.execute(sql, params)
    if result == True:
        print("Insert 成功")
    else:
        print("Insert 失败")
    dbhelper.close()


def spider():
    page_url='http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    for i in range(1,178):
        urls=page_url.format(i)
        moive=get_detail_urls(urls)
        for url in moive:
            parse_detail_page(url)


if __name__ == '__main__':
    spider()


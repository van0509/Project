# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:19:12 2018

@author: Administrator
"""

from urllib import request
from urllib import error
from urllib import parse
import time
import random

import logging
import sys

# 获取logger的实例
logger = logging.getLogger('testLogger')
# 指定当前日志格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# 创建日志对象的Handler
# 文件日志
file_handler = logging.FileHandler("testLogger3.log")
file_handler.setFormatter(formatter)
# 终端日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
# 设置一个默认的级别，低于这个级别的信息将不会被写入日志系统
logger.setLevel(logging.DEBUG)
# 把文件日志，终端日志handlers 添加到日志处理系统中
logger.addHandler(file_handler)
logger.addHandler(console_handler)


minSleeptime = 1
maxSleeptime = 10
def downloadHtml(url,headers=[], proxy={},
                 useProxyRate=0,
                 decodeInfo="utf-8",
                 numRetries=10):
    """
    下载url的数据
    这个方法支持HTTP Request Headers, 能设置UA;
    支持Proxy代理；
    支持网页编码设置
    支持4XX,5XX错误处理
    """
    # 随机确定是否使用代理，默认不使用，可以通过useProxyRate来
    #改变使用代理的行为
    if random.randint(1,10) > useProxyRate:
        proxy = None
    
    # 创建Proxy Handler
    proxy_handler = request.ProxyHandler(proxy)
    # 创建opener
    opener = request.build_opener(proxy_handler)
    # 设置http request的headers
    opener.addheaders = headers#[('User-agent', client_version)]
    # 把proxy hander安装到urllib库中
    request.install_opener(opener)
    
    
    html = None #一开始把返回值赋初值
    try:
        # 发起http request,得到response,读取返回
        resp = request.urlopen(url)
        html = resp.read().decode(decodeInfo)
    except UnicodeDecodeError:
        logger.error("UnicodeDecodeError")
        return html
    except error.URLError or error.HTTPError as e:
        ## 4XX: 一般需要获取日志信息，进行爬虫策略的跳转
        if hasattr(e, 'code') and 400 <= e.code < 500:
            logger.error("Client Error: ",e.code)
            return html
        ## 5XX: 服务器的问题
        if numRetries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                time.sleep(random.randint(minSleeptime,
                                          maxSleeptime))#最好有一个等待的策略
                html = downloadHtml(url, headers, proxy, useProxyRate,
                                    decodeInfo, numRetries-1)
    return html
        
headers = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")]
print(downloadHtml("http://www.baid.com", headers=headers))

# 不用这个日志handlers时，需要移除
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)

import urllib,ssl
from urllib import request,parse
url='http://www.12306.cn/mormhweb/'
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

context=ssl._create_default_https_context()

req=urllib.request.Request(url,headers=header)

response=urllib.request.urlopen(req,context=context)


print(response)

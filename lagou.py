# from urllib import request
import requests,re
url="https://www.qiushibaike.com/"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

req=requests.get(url,headers=header).content.decode()
pattern='<div class="content">[\s]*?<span>([\s\S]*?)</span>[\s\S]*?'
# pattern='<div class="content">[\s]*?<span>([\s\S]*?)</span>[\s\S]*?<div class="thumb">[\s\S]*?<img src="([\s\S]*?)"[\s\S]*?'
text=re.findall(pattern,req)
for x in text:
    print(x.strip())


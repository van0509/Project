import requests,re
import urllib
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

url="https://www.baidu.com/s?"

keyword=input("请输入您要查询的数据")
wd={"wd":keyword}
wd=urllib.parse.urlencode(wd)
urls=url+wd
resp=requests.get(urls,headers=header)
pattern='<th><a href="([\s\S]*?)">([\s\S]*?)</a></th>'
resp=re.findall(pattern,resp.text)
for _ in resp:
    print("https://www.baidu.com"+_[0],_[1])
# with open('baiduSearch.html','wb') as f:
#     f.write(resp.text.encode())

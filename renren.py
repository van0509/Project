from http import cookiejar
from urllib import request,parse

#创建一个cookiejar的对象
cookiej=cookiejar.CookieJar()


#通过HHTCookieProcess对象来处理cookiej
cookoe_handler=request.HTTPCookieProcessor(cookiej)

#构建一个opener
#用一个新的可以处理cookie的Handler取代原来默认的http handler
#从而加强http handler的功能,实现其可以处理cookie
#下面就可以使用opener去发送http的请求
opener=request.build_opener(cookoe_handler)

opener.add_handler([('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')])
# 准备登陆
url='http://www.renren.com/'

data={'email':'xxx','password':'YYY'}

#post请求
data=parse.urlencode(data).encode('utf-8')

req=request.Request(url,data,method='POST')
response=opener.open(req)


#登陆成功后,去抓取首页数据

responsemyrenren=opener.open('http://www.renren.com/')
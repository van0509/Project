# from urllib import request
# import requests,random,re
# from selenium import webdriver
import hashlib
#
# User_AgentList=[
#     'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
#     'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
#     'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
#     'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
#     'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)'
# ]
#
# for i in range(10):
#     header={
#         'User_Agent':random.choice(User_AgentList)
#     }
#     resp=requests.get('https://www.baidu.com',headers=header)
#
#     print(resp.status_code)
# pattern="[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
# resp=re.findall(pattern,'hello_Python3_world!')
# print(resp)
# str=input('请输入要反转的句子')
#
# s=str.split(' ')
# a=" ".join(s[::-1])

# def reverseSenten(s):
#     '''
#     输入一个英文句子,反转句子中的单词的顺序,但单词内字符的顺序不变.
#     :param s:
#     :return:
#     '''
#     s=s.split(" ")
#     # return " ".join(s[::-1])
#     return " ".join(sorted(s,reverse=True))
# s=input('请输入要反转的句子')
# a=reverseSenten(s)
# print(a)
#

# firefox=webdriver.Chrome()
# firefox.get("http://fanyi.youdao.com/")
# firefox.find_element_by_id("inputOriginal").send_keys('Spider man')
# firefox.find_element_by_id('sb_form_go').click()
# print(firefox.page_source)
# firefox.quit()
# # firefox.close()

def hashStr(strInfo):
    h=hashlib.sha512()
    h.update(strInfo.encode('utf-8'))

    return h.hexdigest()

print(hashStr('Hello World'))


def hashFile(filename):
    h=hashlib.sha3_512()
    with open(filename,'rb') as f:
        while True:
            chunk=f.read(4096)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()

print(hashFile('maoyan_yeild.txt'))
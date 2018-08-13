from selenium import webdriver
import time

broswer=webdriver.Chrome()

broswer.get("http://index.baidu.com/#/")

broswer.find_element_by_xpath('//*[@id="home"]/div[1]/div[2]/div[1]/div[4]/span/span').click()
time.sleep(3)
broswer.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('15091536181')
broswer.find_element_by_id('TANGRAM__PSP_4__password').send_keys('*******')
broswer.find_element_by_id('TANGRAM__PSP_4__submit').click()



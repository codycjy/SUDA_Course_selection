from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

# ________________________
# 改成自己的学号和密码
studentPassword = ""
studentId = ""
# _______________________
wd = webdriver.Chrome(r'./chromedriver.exe')
wd.get('http://xk.suda.edu.cn/')

sleep(2)
wd.find_element_by_id('TextBox1').send_keys(studentId)
wd.find_element_by_id('TextBox2').send_keys(studentPassword)
verCode = input('请输入验证码，并以回车结束:')
wd.find_element_by_id('TextBox3').send_keys(verCode)
wd.find_element_by_id('Button1').click()
try:
    wd.find_element_by_id('btnqd').click()
except:
    pass
sleep(5)
wd.find_element_by_xpath('//*[@id="navxl"]/li[2]/a/span').click()
sleep(1)
wd.find_element_by_xpath('//*[@id="navxl"]/li[2]/ul/li[3]/a').click()
wd.find_element_by_xpath('//*[@id="Label3"]').click()

sleep(5)
wd.switch_to.frame(wd.find_element_by_id('iframeautoheight'))
s = Select(wd.find_element_by_id('ddl_sksj'))
s.select_by_index(0)
wd.find_element_by_id('TextBox1').send_keys(input('输入课程名称'))

while True:
    try:
        wd.find_element_by_id('Button2').click()
        wd.find_element_by_id('kcmcGrid_xk_0').click()
        wd.find_element_by_id('Button1').click()
        print("抢课结束 请确定是否成功")
        break
    except:
        sleep(5)
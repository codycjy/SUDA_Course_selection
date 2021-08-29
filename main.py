from selenium import webdriver
from selenium.webdriver.support.select import Select
import selenium
from time import sleep
import sys

# ________________________
studentPassword = sys.argv[2]
studentId = sys.argv[1]
# _______________________

wd = webdriver.Chrome(r'./chromedriver.exe')
wd.get('http://xk.suda.edu.cn/')

sleep(2)
wd.find_element_by_id('TextBox1').send_keys(studentId)
wd.find_element_by_id('TextBox2').send_keys(studentPassword)
verCode = input('请输入验证码，并以回车结束:')
wd.find_element_by_id('TextBox3').send_keys(verCode)
wd.find_element_by_id('Button1').click()

try: # 这一段为了处理未缴费弹窗 没错我忘记交了
    wd.find_element_by_id('btnqd').click()
except:
    pass

sleep(5)
wd.find_element_by_xpath('//*[@id="navxl"]/li[2]/a/span').click()
sleep(2)
wd.find_element_by_xpath('//*[@id="navxl"]/li[2]/ul/li[3]/a').click()

sleep(5)
wd.switch_to.frame(wd.find_element_by_id('iframeautoheight'))
s = Select(wd.find_element_by_id('ddl_sksj'))
aviTimeLst=[i.text for i in s.options]
cnt=0
for i in range(len(aviTimeLst)):
    print(cnt+1,aviTimeLst[i],end='\t')
    cnt+=1;
    if cnt%4==0:print()

s.select_by_index(int(input("输入所需要时间的序号"))-1)
wd.find_element_by_id('TextBox1').send_keys(input('输入课程名称'))

while True:
    try:
        wd.find_element_by_id('Button2').click()
        wd.find_element_by_id('kcmcGrid_xk_0').click()
        wd.find_element_by_id('Button1').click()
        try:
            print(wd.switch_to.alert.text)
        except:
            pass
        print("抢课结束 请确定是否成功")

        break
    except:
        print("暂时没课哦，再等等看?")
        sleep(5)
try:
    wd.close()
except:
    pass


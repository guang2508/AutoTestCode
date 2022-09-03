# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-11-26
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
brower=webdriver.Chrome()
brower.maximize_window()
brower.implicitly_wait(10)
brower.get('https://www.qcc.com/?utm_source=baidu&utm_medium=cpc&utm_term=%E5%A4%A9%E7%9C%BC%E6%9F%A5%E5%AE%9A%E6%8A%95')
time.sleep(3)
cookies='QCCSESSID=kt5dc60n6gir634tau0sgsjt12; zg_did=%7B%22did%22%3A%20%2217604420a9953b-093555f607ff9e-3e3e5f0e-1fa400-17604420a9a869%22%7D; UM_distinctid=17604420c575d3-0dc62e3a0e31ca-3e3e5f0e-1fa400-17604420c5832c; hasShow=1; _uab_collina=160638920645628606357947; acw_tc=7250181816064112069644068eec6e968e10acae9bc462aa043664e0aa; CNZZDATA1254842228=230905684-1606387875-https%253A%252F%252Fwww.baidu.com%252F%7C1606406879; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201606409218984%2C%22updated%22%3A%201606411339106%2C%22info%22%3A%201606389205664%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%22efaf661dbcacb0a2e9b325ca773c75ba%22%7D'

cookies=cookies.replace(' ','')

list1=cookies.split(';')
dict1={}
for ll in list1:
    ld=ll.split('=')
    dict1[ld[0]]=ld[1]
for one in dict1:
    tt={'value':dict1[one],'name':one}
    brower.add_cookie(cookie_dict=tt)

brower.get('https://www.qcc.com/?utm_source=baidu&utm_medium=cpc&utm_term=%E5%A4%A9%E7%9C%BC%E6%9F%A5%E5%AE%9A%E6%8A%95')
ActionChains(brower).move_by_offset(20, 500).click().perform()
companyName='江苏今点软件有限公司'
inputText=brower.find_element_by_css_selector('#searchkey').send_keys(companyName+'\n')#点击华为官方


time.sleep(1)
eles=brower.find_elements_by_xpath('//*[@class="ntable ntable-list"]/tr[1]//em')
namelists=[]
for ele in eles:
    namelists.append(ele.text)
companyNameCheck=''.join(namelists)
if companyName!=companyNameCheck:
    #########################################################
    quit()

brower.find_element_by_xpath('//*[@class="ntable ntable-list"]/tr[1]//em[1]').click()
time.sleep(2)
hands=brower.window_handles   #获取窗口数
brower.switch_to.window(hands[1])   #定位第二窗口

addr=brower.find_element_by_xpath('//*[@id="Cominfo"]/table//tr[last()-1]/td[2]').text
addr=addr.replace(' 查看地图 附近企业','')
print(addr)

bussScope=brower.find_element_by_xpath('//*[@id="Cominfo"]/table//tr[last()]/td[2]').text
print(bussScope)



hands=brower.window_handles   #获取窗口数
brower.switch_to.window(hands[1])   #定位第二窗口
menu=brower.find_elements_by_css_selector('ul [class^="nav"]')  #定位菜单栏
subMenus=[]
demandMenu=['手机','笔记本','平板','穿戴','智能家居','更多产品','软件应用','服务支持']
for subMenu in menu:
    subMenus.append(subMenu.text)
flag1=[False for c in demandMenu if c not in subMenus]  #判断菜单栏是否包含给出的元素
if flag1:
    print('官方菜单异常')
else:
    print('官方菜单正常')
brower.switch_to.window(hands[0])   #定位第一页面
time.sleep(1)
move=brower.find_element_by_id('zxnav_1')   #定位笔记本&平板栏
ActionChains(brower).move_to_element(move).perform()    #鼠标移到上述位置
time.sleep(1)
saleMunes=brower.find_elements_by_css_selector('[class="category-panels category-panels-1"] li span') #定位text级
computerMunes=[]
computerMune=['平板电脑','笔记本电脑','笔记本配件']
for saleMune in saleMunes:
    print(saleMune.text)
    computerMunes.append(saleMune.text)
flag2=[False for c in computerMune if c not in computerMunes]   #判断商城菜单是否包含给出元素
if flag2:
    print('商城菜单异常')
else:
    print('商城菜单正常')
brower.quit()

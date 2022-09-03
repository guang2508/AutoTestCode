# -*- coding: utf-8 -*-
# __author__:汤继光
# 2021-05-25
# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-11-26
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
brower=webdriver.Chrome()
brower.maximize_window()
brower.implicitly_wait(10)
pageId=1
namelists=[]
for i in range(1,14):
    brower.get(f'http://www.china-audit.com/lhd_0zftl8lxn168ub00wpi6_{i}.html')
    # time.sleep(3)
    eles=brower.find_elements_by_xpath('//*[@class="center"]//p')
    for ele in eles:
        namelists.append(ele.text)
tt='\n'.join(i for i in namelists)
with open(r'C:\Users\Administrator\Desktop\tt.txt','w') as f2:
    f2.write(tt)


# if companyName!=companyNameCheck:
#     #########################################################
#     quit()
#
# brower.find_element_by_xpath('//*[@class="ntable ntable-list"]/tr[1]//em[1]').click()
# time.sleep(2)
# hands=brower.window_handles   #获取窗口数
# brower.switch_to.window(hands[1])   #定位第二窗口
#
# addr=brower.find_element_by_xpath('//*[@id="Cominfo"]/table//tr[last()-1]/td[2]').text
# addr=addr.replace(' 查看地图 附近企业','')
# print(addr)
#
# bussScope=brower.find_element_by_xpath('//*[@id="Cominfo"]/table//tr[last()]/td[2]').text
# print(bussScope)
#
#
#
# hands=brower.window_handles   #获取窗口数
# brower.switch_to.window(hands[1])   #定位第二窗口
# menu=brower.find_elements_by_css_selector('ul [class^="nav"]')  #定位菜单栏
# subMenus=[]
# demandMenu=['手机','笔记本','平板','穿戴','智能家居','更多产品','软件应用','服务支持']
# for subMenu in menu:
#     subMenus.append(subMenu.text)
# flag1=[False for c in demandMenu if c not in subMenus]  #判断菜单栏是否包含给出的元素
# if flag1:
#     print('官方菜单异常')
# else:
#     print('官方菜单正常')
# brower.switch_to.window(hands[0])   #定位第一页面
# time.sleep(1)
# move=brower.find_element_by_id('zxnav_1')   #定位笔记本&平板栏
# ActionChains(brower).move_to_element(move).perform()    #鼠标移到上述位置
# time.sleep(1)
# saleMunes=brower.find_elements_by_css_selector('[class="category-panels category-panels-1"] li span') #定位text级
# computerMunes=[]
# computerMune=['平板电脑','笔记本电脑','笔记本配件']
# for saleMune in saleMunes:
#     print(saleMune.text)
#     computerMunes.append(saleMune.text)
# flag2=[False for c in computerMune if c not in computerMunes]   #判断商城菜单是否包含给出元素
# if flag2:
#     print('商城菜单异常')
# else:
#     print('商城菜单正常')
# brower.quit()



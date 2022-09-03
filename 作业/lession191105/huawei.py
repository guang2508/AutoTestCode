# author：tang   time:2019-11-04
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
brower=webdriver.Chrome()
brower.implicitly_wait(10)
brower.get('https://www.vmall.com/')
offical=brower.find_element_by_css_selector('[href="http://consumer.huawei.com/cn/"]').click()#点击华为官方
time.sleep(3)
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




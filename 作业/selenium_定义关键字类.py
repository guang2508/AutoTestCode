# -*- coding: utf-8 -*-
from selenium import webdriver


def browser(type_):
    #定义driver的值：判断type是什么内容，则生成对应的浏览器对象即可
    try:
        driver = getattr(webdriver,type_)
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver

class WebKeys:
    # #虚拟driver
    # driver=webdriver.Chrome()

    #构造函数
    def __init__(self,type_):
        self.driver=browser(type_)

    #访问url
    def open(self,url):
        self.driver.get(url)

    #元素定位
    def locator(self,name,value):
        return self.driver.find_element(name,value)

    #输入
    def input_(self,name,value,txt):
        self.locator(name,value).send_keys(txt)

    #点击
    def click(self,name,value):
        self.locator(name,value).click()

    #退出
    def quit(self):
        self.driver.quit()
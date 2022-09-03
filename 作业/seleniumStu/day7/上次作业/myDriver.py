# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/5/27

from selenium import webdriver
from study.seleniumStu.day7.上次作业.mySettings import DOMAIN, driverPath


class Driver:
    # 浏览器驱动对象，初始化为空
    # 类成员，保存在类当中，实现唯一性
    _driver = None

    @classmethod
    def get_driver(cls, browser_name="Chrome"):
        """
        获取浏览器对象
        :param browser_name: 浏览器类型，比如 Chrome、Ie
        :return: 浏览器驱动对象
        """
        # 如果不为空就不需要创建了
        if cls._driver is None:
            if browser_name == "Chrome":
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
            elif browser_name == "Firefox":
                cls._driver = webdriver.Firefox(driverPath["Firefox"])
            # ...... 省略其他的浏览器声明

            # 最大化窗口
            cls._driver.maximize_window()
            # 访问默认的网址
            cls._driver.get(DOMAIN)
            # 执行登录
            cls.__login()

        return cls._driver

    @classmethod
    def __login(cls):
        # 登录逻辑， 在 driver 初始化的时候被调用一次，去操作登录页面
        cls._driver.find_element_by_name("username").send_keys("libai")
        cls._driver.find_element_by_name("password").send_keys("opmsopms123")
        cls._driver.find_element_by_tag_name("button").click()




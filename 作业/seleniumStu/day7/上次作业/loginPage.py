# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/5/27


from selenium.webdriver.common.by import By
from study.seleniumStu.day7.上次作业.basePage import BasePage


class LoginPage(BasePage):
    """登录页面"""

    def __init__(self):
        # 执行父类的构造方法
        super().__init__()

        # 用户名输入框
        self.userinpLo = (By.NAME, "username")
        # 密码输入框
        self.pwdInpLo = (By.NAME, "password")
        # 登录按钮
        self.loginButtonLo = (By.CSS_SELECTOR, "button")

    def userInpBox(self):
        """实时获取用户名输入框"""
        return self.get_element(self.userinpLo)

    def pwdInpBox(self):
        """实时获取密码输入框"""
        return self.get_element(self.pwdInpLo)

    def loginButtonBox(self):
        """实时获取登录按钮"""
        return self.get_element(*self.loginButtonLo)


# 抽离出页面动作类，继承页面类, 把常用的公共方法封装起来
class LoginPageAction(LoginPage):
    def login(self):
        # 输入用户名
        self.userInpBox().send_keys("libai")
        # 输入密码
        self.pwdInpBox().send_keys("opmsopms123")
        # 点击登录按钮
        self.loginButtonBox().click()


if __name__ == '__main__':
    LoginPageActionObj = LoginPageAction()
    LoginPageActionObj.login()

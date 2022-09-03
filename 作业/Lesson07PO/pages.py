import time
from selenium import webdriver
#创建一个基础页面用于存放一些页面操作的公共方法
from selenium.webdriver.common.by import By
from commonlib import load_eles
class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
    def click_ele(self,locator):
        self.driver.find_element(locator[0],locator[1]).click()
    def input_text(self,locator,text):
        print(locator)
        self.driver.find_element(locator[0], locator[1]).clear()
        self.driver.find_element(locator[0], locator[1]).send_keys(text)
    def get_eles(self,locator):
        return self.driver.find_elements(locator[0], locator[1])
#具体的业务页面
class LoginPage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        locators=load_eles('LoginPage')
        self.user=locators['user']
        self.passwd=locators['passwd']
        self.login_btn=locators['login_btn']

    def login(self,username,password):
        self.driver.get('http://localhost:81/mgr/login/login.html')
        self.input_text(self.user,username)
        self.input_text(self.passwd,password)
        self.click_ele(self.login_btn)

#替换元素定位，用Yaml配置文件进行分配，可以参考Loginpage代码
class CoursePage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self, driver)
        locators = load_eles('CoursePage')
        self.add_btn = locators['add_btn']
        self.name_text = locators['name_text']
        time.sleep(1)
        self.desc_text = locators['desc_text']
        self.idx_text = locators['idx_text']
        self.create_btn=locators['create_btn']

    def goto_course(self):
        self.driver.get('http://localhost:81/mgr/ps/mgr/index.html#/')

    def quit_page(self):
        self.driver.quit()

    #添加课程
    def add_course(self,name,desc,idx):
        self.click_ele(self.add_btn)
        self.input_text(self.name_text,name)
        self.input_text(self.desc_text,desc)
        self.input_text(self.idx_text,idx)
        self.click_ele(self.create_btn)

    #删除课程
    def del_all_courses(self):
        self.driver.implicitly_wait(1)
        while 1:
            del_btns = self.get_eles([By.CSS_SELECTOR,'[ng-click="delOne(one)"]'])
            if del_btns==[]:
                break
            del_btns[0].click()#取第一个元素操作
            self.click_ele([By.CSS_SELECTOR, '.btn-primary'])
            time.sleep(1)
        self.driver.implicitly_wait(10)

#测试代码改成Unitest形式，要求重新建一个ts.py在里面实现
if __name__ == '__main__':
    driver=webdriver.Chrome()
    LoginPage(driver).login('auto','sdfsdfsdf')
    cp=CoursePage(driver)
    # cp.goto_course()
    cp.del_all_courses()
    cp.add_course('语文课','语文课描述','1')
    cp.add_course('数学课','数学课描述','2')
    cp.del_all_courses()
    cp.quit_page()



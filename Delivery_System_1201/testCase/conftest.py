#-*- coding: utf-8 -*-
#@File    : conftest.py
#@Time    : 2021/11/19 20:35
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/19 
import pytest
from libs.login import Login
from configs.config import NAME_PSW
from libs.shop import Shop
"""
autouse=True: 一般是整个项目里需要自检操作
autouse=False: 需要手动调用：哪里需要调到哪里去！-----默认就是这个
"""
#没有返回值的fixture
@pytest.fixture(scope='session',autouse=True)
def start_running():
    #---自动化测试前的--环境操作
    print('---外卖项目自动化测试开始执行---')
    yield #-yeild后面没有值就是没有返回值
    print('#自动化执行完成之后，数据清除操作')

@pytest.fixture(scope='class')
def xintian():#没有yeild或者return  也是没有返回值
    print('没有返回值的fixture')

#--------登录操作-----------
#其他的业务层测试代码需要调用这个登录
#返回值的fixture---直接使用这个函数名--就是代表返回值 -login_init == token
@pytest.fixture(scope='session')
def login_init():
    print('---用户操作登录---')
    token = Login().login(NAME_PSW,getToken=True)
    yield token#返回token---有返回值
    print('---登录完成---')#或者可以执行退出操作
    #return token#后面就不能写代码





#-------店铺实例创建------
@pytest.fixture(scope='class')
def shop_init(login_init):
    print('---店铺实例创建开始---')
    shopObject = Shop(login_init)
    yield shopObject#返回值返回店铺实例
    print('---店铺实例创建完成---')


def pytest_collection_modifyitems(items):
    for item in items:
        print('---' * 10)
        item.name = item.name.encode('utf8').decode("unicode_escape")
        item._nodeid = item.nodeid.encode('utf8').decode("unicode_escape")
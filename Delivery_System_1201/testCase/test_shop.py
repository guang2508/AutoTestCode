#-*- coding: utf-8 -*-
#@File    : test_shop.py
#@Time    : 2021/11/19 20:11
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/19
import pytest
from libs.shop import Shop
"""
方案一： 简单好理解
    实现方式：
        1- 在每一个店铺的测试方法里增加 Shop().xxx()
    问题：
        1- 每一个测试方法都有一个  店铺类对应的实例
        2- token需要传递很多次
#---------------
方案二： 剥离的思路----unittest一样的处理
    实现方式：
        1- Shop()增加 setup_class----创建店铺的实例操作放进去，这个测试类里面公用一个实例
    问题：
        1- 登录操作与店铺创建实例的操作，只能在店铺的类使用！，后续的其他模块需要登录，需要重复再写一样的代码！！
    def setup_class(self):#环境初始化
        print('---类初始化方法---')
        #1-登录
        _token = Login().login(NAME_PSW,getToken=True)
        self.shop = Shop(_token)    
        
    def teardown_class(self):#数据清除
        print('---店铺模块执行完成---') 
#-------------------
方案三： 模块化剥离的思路----fixture处理
    实现方式：
        1- Shop()增加 setup_class----创建店铺的实例操作放进去，这个测试类里面公用一个实例
    问题：
        1- 登录操作与店铺创建实例的操作，只能在店铺的类使用！，后续的其他模块需要登录，需要重复再写一样的代码！！
"""
from libs.login import Login
from configs.config import NAME_PSW
from utils.handle_excel import get_excel_data
import allure
from common.baseAPI import ApiAssert
import os,sys
from libs.login import Login

from utils.handle_path import testData_path,report_path
#定义条件跳过的变量
no_ready=pytest.mark.skip(reason='店铺的列出接口后端没有实现，暂时不运行！')#无条件跳过
#@pytest.mark.usefixtures('xintian')#没有返回值的这样手调用！


@pytest.mark.skipif(not Login().login(NAME_PSW)['data'],reason='如果登录失败，直接跳过！')
@allure.epic('外卖项目')
@allure.feature('店铺模块')
#测试类---标签
@pytest.mark.shop
class TestShop:
    #1- 列出店铺
    #@no_ready#调用这个条件跳过！
    @pytest.mark.shop_list#测试方法--标签
    @allure.story('列出店铺')
    @pytest.mark.parametrize('title,inBody,expData', get_excel_data('我的商铺', 'listshopping', '标题', '请求参数', '响应预期结果'))
    @allure.title("{title}")
    @allure.issue('http://www.baidu.com')
    def test_shop_list(self,title,inBody,expData,shop_init):
        res = shop_init.query(inBody)
        #2- 断言
        ApiAssert.define_api_assert(res["code"],'=',expData["code"])

#------------------------------------------------------------
    #2- 更新店铺
    @pytest.mark.shop_update  # 测试方法--标签
    @allure.story('更新店铺')
    @pytest.mark.parametrize('title,inBody,expData', get_excel_data('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    @allure.title("{title}")
    def test_shop_update(self,shop_init,title,inBody,expData):
        with allure.step('1-用户登录+创建店铺'):
            pass
        with allure.step('2-获取店铺id'):
            res = shop_init.query({'page':1,'limit':20})
            shopID = res['data']['records'][0]['id']
        with allure.step('3-文件上传操作'):
            res2 = shop_init.file_upload(os.path.join(testData_path, 'xintian.png'))
            fileInfo = res2['data']['realFileName']
        with allure.step('4-更新店铺操作'):
            res2 = shop_init.update(inBody,shopID,fileInfo)
        with allure.step('5-断言'):
            ApiAssert.define_api_assert(res2["code"],'=',expData["code"])

            """
            流程化：一个业务包含很多个模块（接口）
            举例： 更新接口--查询接口
            方案一：
                直接更新接口响应里就有对应的更新后的结果--可以直接断言这个接口的响应的关键信息
            方案二：
                1-更新接口请求完没有任何有价值数据---可能返回 return code 200--不能直接断言
                2-自动化测试肯定要断言：
                    1- 使用查询接口-查询获取到的是一个列表数据 
                        更新的内容(id) 是否在列表数据里，是否更新 
                    2- 没有查询接口的情况
                        需要操作数据库mysql  mongodb 
            
            
            """






if __name__ == '__main__':
    pytest.main(['test_shop.py', '-s', '--alluredir', f'{report_path}', '--clean-alluredir'])
    os.system(f'allure serve {report_path}')
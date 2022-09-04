#-*- coding: utf-8 -*-
#@File    : login.py
#@Time    : 2021/11/12 20:53
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/12

from common.baseAPI import BaseAPI
from utils.handle_data import get_md5_data
from configs.config import NAME_PSW
import copy
"""
登录这个模块-登录接口使用场景：
    1- 本身的登录接口自动化测试
    2- 为后续接口获取token


"""
from utils.xt import show_time
class Login(BaseAPI):
    @show_time
    def login(self,inData,getToken=False):
        inData = copy.copy(inData)#浅拷贝下数据--避免修改全局数据
        inData['password'] = get_md5_data(inData['password'])
        respData = self.request_send(data=inData)#发送请求
        if getToken: # 获取token
            return respData['data']['token']
        else:#获取响应数据
            return respData




if __name__ == '__main__':
    print(Login().login(NAME_PSW))
    # #1- 编码处理
    # str1 = '你好'
    # str2 = str1.encode('utf-8')
    # print(str2)
    #
    # #2- 解码
    # str3 = str2.decode('gbk')
    # print(str3)
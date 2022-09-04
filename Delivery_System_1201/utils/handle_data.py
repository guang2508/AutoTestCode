#-*- coding: utf-8 -*-
#@File    : handle_data.py
#@Time    : 2021/11/12 22:38
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/12
import hashlib
def get_md5_data(psw:str):
    """
    :param psw: 加密前的密码
    :return: 加密后的密码
    """
    #1- 创建md5实例
    md5 = hashlib.md5()
    #2- 调用加密方法
    md5.update(psw.encode('utf-8'))
    return md5.hexdigest()#加密后的结果
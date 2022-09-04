#-*- coding: utf-8 -*-
#@File    : handle_path.py
#@Time    : 2021/11/14 9:57
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/14 
import os
"""
需求：代码在任意路径都可以获取到项目工程的绝对路径
"""
# print(__file__)#当前文件所在的路径
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
#1- 工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(project_path)

#2- 配置路径
config_path = os.path.join(project_path,'configs')
#print(config_path)

#3- 测试数据路径
testData_path = os.path.join(project_path,'data')
#print(testData_path)

#4- 测试报告路径
report_path = os.path.join(project_path,r'outFiles\report\tmp')
#print(report_path)

#5- log路径
log_path = os.path.join(project_path,r'outFiles\log')
#print(log_path)
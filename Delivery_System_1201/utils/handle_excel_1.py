#-*- coding: utf-8 -*-
#@File    : handle_excel_1.py
#@Time    : 2021/11/14 9:35
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/14 
print()
"""
---------------版本 v1.0---------------
需求：有可能客户或者上下游同事，描述不是很专业
    1- 获取自动化测试用例 excel里面的对应的数据---大功能   
分析需求：
    1- 获取具体哪些数据
        1- 用例标题
        2- 请求body
        3- 预期响应结果
    2- 需要返回什么类型
        1- 客户需要把读取的数据给test_login()   使用的是pytest--数据驱动的方法
            [(),(),()]
解决方案：
    1- 操作execcl库是什么
        1- xlrd  xlwt  操作xx.xls----选定
            xlrd 读操作
            xlwt 写操作---新建一个文件
            xlutils 写操作  在已有的excel文件里修修改（写）
        2- openpyxl   操作xx.xlxs
        3- panda  大数据场景
测试反馈：
版本迭代建议：

"""
import xlrd #pip  install  xlrd
from utils.handle_path import testData_path
import os
def get_excel_data(excelDir,sheetName=None): # 返回值是列表    -> list    def get_excel_data() -> list
    resList = []#存放结果
    #1- 打开一个文件:
    #formatting_info=True 保持原样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)#excel文件
    # sheets = workBook.sheet_names()获取所有的子表名
    #2- 获取需要操作的子表
    workSheet = workBook.sheet_by_name(sheetName)
    #3- 获取一列数据
    #print(workSheet.col_values(0))
    #4- 获取一行数据
    #print(workSheet.row_values(0))

    #获取单元格数据-workSheet.cell(行编号,列编号)
    # print(workSheet.cell(0,0).value)

    #--------获取对应的需求的数据-----------
    rowIndex = 0#行编号的初始值
    for one in workSheet.col_values(0):
        reqBody = workSheet.cell(rowIndex,9).value#请求Body
        respData = workSheet.cell(rowIndex,11).value  # 响应数据
        resList.append((reqBody,respData))#[(请求1，响应1),(请求2，响应2)]
        rowIndex += 1#行编号 加1  下一行操作

    print(resList)
    for one in resList:
        print(one)
    #----------------------------------------
"""
---------------版本 v1.0---------------
测试反馈：
    1- 如果里面有非这个接口需要的用例，会导致自动化测试失败
    2- 如果后续需要获取其他列数据---没有办法-只能改代码！
版本迭代建议：
    1- 需要传递一个对应的接口的筛选的条件 
    2- 提供扩展性  以后可能需要获取用例标题
"""





if __name__ == '__main__':
    fileDir = os.path.join(testData_path,'Delivery_System_V1.5.xls')
    get_excel_data(fileDir,'登录模块')

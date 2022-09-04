#-*- coding: utf-8 -*-
#@File    : handle_excel_1.py
#@Time    : 2021/11/14 9:35
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/14 
print()
"""
---------------版本 v2.0---------------
需求：    
    1- 需要传递一个对应的接口的筛选的条件 
    2- 提供扩展性  以后可能需要获取用例标题
分析需求：
解决方案：
    1- 我们不清楚后续需要获取哪些列数据--可以考虑使用可变数量参数  *args
测试反馈：
版本迭代建议：

"""
import xlrd #pip  install  xlrd
from utils.handle_path import testData_path
import os
def get_excel_data(excelDir,sheetName,caseName,*args): # 返回值是列表    -> list    def get_excel_data() -> list
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

    #--------v2.0新增功能--------------------
    #args---元组类型  ('URL'，‘标题’,'请求体')
    """
    需求分析：用户传入需要获取的列 ，代码去获取对应的列的单元格数据
    方案：
        1- 用户可以这样去调用函数  直接传递列编号 1,3,5,6---> args
            get_excel_data(excelDir,sheetName,caseName,1,3,5,6)
            感受：
                1-代码可读性差
                2- 你内部代码操作起来是方便的
        2- 用户可以这样去调用函数  直接传递-'URL'，‘标题’,'请求体'---> args
            get_excel_data(excelDir,sheetName,caseName,'URL'，‘标题’,'请求体')
            感受：
                1-代码可读性好，好理解业务需求
                2- 你内部代码操作起来是不方便： 需要把列名--转化为---列编号
    """
    colIndexList = []#存放用户输入列名对应的列编号
    for i in args:# ('URL'，‘标题’,'请求体')遍历
        colIndexList.append(workSheet.row_values(0).index(i))#获取编号

    print(colIndexList)


    #--------------------------------------


    #--------获取对应的需求的数据-----------
    rowIndex = 0#行编号的初始值
    for one in workSheet.col_values(0):
        if caseName in one:#筛选下
            #遍历那个列编号--列表
            getColData = []
            for num in colIndexList: #[4,5]
                tmp = workSheet.cell(rowIndex, num).value
                getColData.append(tmp)
            resList.append(list(getColData))#[(请求1，响应1),(请求2，响应2)]
        rowIndex += 1#行编号 加1  下一行操作

    print(resList)
    for one in resList:
        print(one)
    #----------------------------------------
"""
---------------版本 v2.0---------------
数据处理的思维：
    1- 直接获取数据，在登录的业务代码去转化
    2- 在获取数据的 源头就把数据搞好！
测试反馈：
    1- 外卖自动化业务代码，都需要字典类型---excel获取出来是字符串类型
        1- 像url  不是json---不需要转化
        2- 像请求的body，是json ---需要转化
    2- 做测试--冒烟测试--不是全部去执行所有的用例---用例执行筛选！
    
    pytest框架的定制化执行：
        1- -mark  指定对应的接口跑自动化---不能选择里面具体某一条用例
        2- 数据层定制  数据驱动，我们筛选出我们需要执行的用例条数
    
    
        

"""





if __name__ == '__main__':
    fileDir = os.path.join(testData_path,'Delivery_System_V1.5.xls')
    get_excel_data(fileDir,'登录模块','Login','URL','标题','前置条件')

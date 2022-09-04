#-*- coding: utf-8 -*-
#@File    : xt.py
#@Time    : 2021/11/24 20:42
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/24 
print()
import time
"""
v1.0版本代码
    接口自动化测试代码
    def test():
        print（）
新需求：需要知道每一个用例的执行时间
"""


#-----------方案1--小明--------
# def test():
#     print('---开始自动化测试---')
#     startTime = time.time()
#     time.sleep(1)#模拟接口的操作
#     endTime = time.time()
#     print('接口执行耗时>>> ',endTime-startTime)
"""
测试反馈：
    1- 你直接修改了代码--重构代码----100个---维护麻烦
    2- 后续还有需求，你的思路就改代码，不断改
"""

#-----------方案2--小李-------------
"""
方案：
    1- 不能修源代码
    2- 新增的功能单独写
"""

#
#
# def show_time(func):
#     print('---开始自动化测试---')
#     startTime = time.time()
#     func()
#     endTime = time.time()
#     print('接口执行耗时>>> ',endTime-startTime)
"""
测试反馈：
    1- 没有修改源接口代码
    2- 改变了函数的执行方式！----没有达到预期
"""

#-----------方案3--小刘-------------
"""
方案：
    1- 不能修源代码
    2- 不能改变函数调用方式
    3- 新增功能新增上去
操作流程：
    1- Python装饰器（Decorators）用于不改变函数源代码的基础上---函数功能扩展！
    2- 闭包的概念：
        在Python这门语言中，函数内部还可以定义函数，如果内部函数使用了外层函数的变量，外函数返回值是内函数的函数名！
    3- 相似概念：
        装包  def a(*args)---把传入形参---装成一个元组
        解包  list = [100,200]  函数调用a(*list)
"""
# def show_time(func):#外函数
#     def inner():#内函数
#         startTime = time.time()
#         func()
#         endTime = time.time()
#         print('接口执行耗时>>> ',endTime-startTime)
#     return inner#函数对象
#
# @show_time#等价于----test=show_time(test)#函数对象 test=inner
# def test():
#     print('---开始自动化测试---')
#     time.sleep(1)#模拟接口的操作

# @show_time #test02=show_time(test02)#函数对象 test02=inner
# def test02():
#     print('---开始自动化测试 test02---')
#     time.sleep(1)#模拟接口的操作

"""
闭包函数是好用，但是我们每一个需要新增功能的函数都得加一行代码
优化：语法糖 @show_time这个装饰器在什么函数前面加等价于
    函数名变量 = show_time(函数名)


"""
#-------带参数传递的装饰器-----
def show_time(func):#外函数
    def inner(*args,**kwargs):#内函数
        startTime = time.time()
        res = func(*args,**kwargs)
        endTime = time.time()
        print('接口执行耗时>>> ',endTime-startTime)
        return res #这个返回值就是 inner函数的返回值
    return inner#函数对象

@show_time#等价于----test=show_time(test)#函数对象 test=inner
def test(*args,**kwargs):
    print('---开始自动化测试---',args)
    time.sleep(1)#模拟接口的操作




if __name__ == '__main__':
    # test=show_time(test)#函数对象 test=inner
    test(100)
"""
payload = 
    {
        "id":"id",
        "idMenu":"23324",
        "idShop":"6938",
        "name":"蒙牛",
        "specsJson":[{"specs":"默认","packing_fee":0,"price":20}]
        }

需要数据处理
payload["specsJson"] = json.dumps(payload["specsJson"])

如果这个参数是选填：
    if 用例里有这个选填--才转化
    没有不需要转化

"""
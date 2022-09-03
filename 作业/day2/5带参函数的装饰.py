# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/2
import time


def bar(func):
    def inner(case_name):
        begin_time = time.time()
        print("%s执行了测试用例")
        func(case_name)
        end_time = time.time()
        print("总计用时：", end_time - begin_time)
    return inner


@bar # foo = bar(foo)
def foo(case_name):
    # begin_time = time.time()
    print("执行了一系列接口测试用例", case_name)
    time.sleep(1)
    # end_time = time.time()
    # print("总计用时：", end_time - begin_time)


foo("支付宝广告内嵌需求测试用例")

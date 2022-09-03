# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/2

import time

def bar(func):
    def inner():
        begin_time = time.time()
        func()
        end_time = time.time()
        print("总计用时：", end_time - begin_time)
    return inner


@bar # foo = bar(foo)
def foo():
    # begin_time = time.time()
    print("执行了一系列接口测试用例")
    time.sleep(1)
    # end_time = time.time()
    # print("总计用时：", end_time - begin_time)

# foo()

# if foo == bar(foo)
# foo = bar(foo)

foo()





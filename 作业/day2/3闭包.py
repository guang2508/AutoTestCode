# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/2



def foo():
    a = 99
    def bar():
        print(a)
    return bar

a = foo()
a()

foo()()


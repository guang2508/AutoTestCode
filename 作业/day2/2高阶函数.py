# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/2

def foo():
    print(233)



# 函数名可以赋值给其他变量
a = foo

# a()


def bar(fun):
    fun()
# 函数名可以作为参数传递
bar(a)


# 函数名可以作为返回值
def foo1():
    def bar1():
        print("函数名可以作为返回值")
    return bar1

b = foo1()
b()

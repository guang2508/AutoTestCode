# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/2

a = 66 # 全局作用域

def foo():
    a = 99 # 局部作用域
    print(a)

    def bar():
        e = 100 # 嵌套作用域
        print("e =", e)
        def foo1():
            ee = 88
            print("ee =", ee)
        foo1()
    bar()



foo()

print(a)
print(__name__) # 内置作用域
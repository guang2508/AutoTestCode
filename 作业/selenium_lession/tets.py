# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-06-24

class A():
    x=19
    def __init__(self):
        self.a=199

    @classmethod
    def foo(cls):
        cls.x += 200
        print(cls.x)

a1=A.x



a2=A.x

print(a2)


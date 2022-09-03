# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-19
def numSum(*args):
    sum=0
    for i in args:
        sum += i
    return sum
print(numSum(1,2,3))
# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-14
def concat(*lists):
    ret=[]
    for i in lists:
        ret +=i
    return ret
print(concat([1,2],[4,2]))

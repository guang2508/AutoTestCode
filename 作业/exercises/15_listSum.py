# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-11
def listSum(alist):
    blist=[]
    for i in range(0,len(alist)):
        asum = 0
        for j in range(0,i+1):
            asum += alist[j]
        blist.append(asum)
    return blist

alist=[1, 2, 3, 4]
print(listSum(alist))
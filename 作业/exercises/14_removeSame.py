# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-11
def removeDups(alist):
    blist=[]
    for i in alist:
        if i not in blist:
            blist.append(i)
    return blist

alist=[1, 0, 1, 0]
print(removeDups(alist))
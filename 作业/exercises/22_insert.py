# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-15
def insertInto(str1,alist):
    if str1>=alist[-1]:
        alist.append(str1)
        return alist
    for i in range(0,len(alist)):
        if alist[i]>str1:
            alist.insert(i,str1)
            return alist
str1=20
alist=[1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
print(insertInto(str1,alist))
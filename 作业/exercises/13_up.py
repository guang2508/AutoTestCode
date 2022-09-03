# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-11
def indexOfCaps(str):
    alist=[]
    for i in range(0,len(str)):
        if str[i].isupper():
            alist.append(i)
    return alist
str=""
print(indexOfCaps(str))
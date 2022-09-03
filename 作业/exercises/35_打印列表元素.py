# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-19
def printall(alist):
    for i in alist:
        if type(i) == list:
            for j in i:
                print(j)
        else:
            print(i)
li = [11,(1,2),4,"daben",[3,7,8,"Susan"],5,"xintian"]
printall(li)
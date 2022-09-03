# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-19
def newlist(alist):
    ali = []
    for i in alist:
        i=i.replace(" ","")

        if (i.startswith('S') or i.startswith("D")) and i.endswith("n"):
            ali.append(i)
    print(ali)
li =["Susan","Xintian","Xiaoxiao ","Xiaozhu","Daben","Xiaoze"]
newlist(li)
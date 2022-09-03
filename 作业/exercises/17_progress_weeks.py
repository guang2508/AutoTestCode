# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-14
def progress_weeks(alist):
    sum=0
    for i in range(1,len(alist)):
        if alist[i]>alist[i-1]:
            sum+=1
    return sum
alist=[3, 4, 1, 2]
print(progress_weeks(alist))

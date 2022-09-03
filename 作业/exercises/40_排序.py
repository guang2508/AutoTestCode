# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-19
def orderBy(str1):
    alist=str1.split(',')
    alist.sort()
    return ','.join(alist)
str1='without,hello,bag,world'
print(orderBy(str1))
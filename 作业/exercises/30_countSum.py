# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-15
str='1234324324fdsaf1fdsaf12'
str=list(str)
counts=0
for i in str:
    if i.isdigit():
       counts +=1
print(counts)
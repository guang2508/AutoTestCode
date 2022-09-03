# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-19
li= [11,22,33,44,55,66,77,88,99,90]
dict1={}
li1=[]
li2=[]
for i in li:
    if i > 66:
        li1.append(i)
    if i< 66:
        li2.append(i)
dict1={'k1':li1,'k2':li2}
print(dict1)
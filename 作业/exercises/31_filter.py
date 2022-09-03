# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-15
# li=["谁啊","牛逼","无语","小朋友"]
# alist=[]
# str1=input()
# if str1.find("谁啊") or str1.find('牛逼') or str1.find("无语") or str1.find("小朋友"):
#     str1=str1.replace("谁啊", "**")
#     str1=str1.replace("牛逼", "**")
#     str1=str1.replace("无语", "**")
#     str1=str1.replace("小朋友", "***")
# alist.append(str1)
# print(alist)
li=["谁啊","牛逼","无语","小朋友"]
alist=[]
str1=input()
for i in li:
    if str1.find(i):
        str1=str1.replace(i,'*'*len(i))
alist.append(str1)
print(alist)

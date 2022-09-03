# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-15
li = ["手机", "电脑", '鼠标垫', '游艇']
adict={}
for i in range(1,len(li)+1):
    adict[i]=li[i-1]
for i in adict:
    print(f'{i} {adict[i]}')
str1=input('选择商品序号,输入Q或q退出程序')
while True:

    if str1.isdigit() and int(str1)>=1 and int(str1)<=len(li):
        print(adict[int(str1)])
        str1 = input('选择商品序号,输入Q或q退出程序')
    elif str1.upper()=='Q':
        break
    else:
        str1=input("输入有误，请重新输入，输入Q或q退出程序")
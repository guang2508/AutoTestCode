# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-22
# def lingxing(x,y):
#     for i in range(0,y):
#         k1=int((y-i)/y*x)
#         k2=int(2*i/y*x)
#         str1=' '
#         str2=' '
#         print(str1*k1+"*"+str2*k2+"*")
#     for i in range(y,-1,-1):
#         k1=int((y-i)/y*x)
#         k2=int(2*i/y*x)
#         str1=' '
#         str2=' '
#         print(str1*k1+"*"+str2*k2+"*")
# lingxing(8,8)
def lingxing(x):
    for i in range(0,x):
        str1=' '
        print(str1*(x-1-i)+"x"*(2*i+1))
    for i in range(x-2,-1,-1):
        str1=' '
        print(str1*(x-1-i)+"x"*(2*i+1))
lingxing(5)
